"""Pipeline de linguagem simples do E aí, Eleito?

Lê o JSON do coletor, busca o contexto oficial de cada votação nominal
(ementa do projeto e do trecho votado) e pede à IA os textos simples:
frase, "o que muda", argumento a favor e argumento contra.

Nada é publicado daqui: todo texto sai com "revisado": false e vai para
uma planilha de revisão em Markdown. Uma pessoa confere antes de publicar.

Uso:
    python simplificar.py ../coletor/saida/semana-2026-10-14.json
    python simplificar.py ARQUIVO --limite 3       # só as 3 primeiras
    python simplificar.py ARQUIVO --sem-ia         # só monta o contexto (não chama a IA)

Precisa da variável de ambiente ANTHROPIC_API_KEY (exceto com --sem-ia).
"""

import argparse
import json
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import requests

AQUI = Path(__file__).parent
CAMARA = "https://dadosabertos.camara.leg.br/api/v2"
SENADO = "https://legis.senado.leg.br/dadosabertos"
HEADERS = {"Accept": "application/json", "User-Agent": "eaieleito-linguagem/0.1"}

MODELO = "claude-opus-5-5"
PROMPT_SISTEMA = (AQUI / "prompt_sistema.md").read_text(encoding="utf-8")

ESQUEMA = {
    "type": "object",
    "properties": {
        "frase_simples": {"type": "string"},
        "o_que_muda": {"type": "string"},
        "a_favor_diz": {"type": "string"},
        "contra_diz": {"type": "string"},
        "tipo_votacao": {"type": "string", "enum": ["merito", "procedimento"]},
        "informacao_suficiente": {"type": "boolean"},
        "observacao_revisor": {"type": "string"},
    },
    "required": [
        "frase_simples", "o_que_muda", "a_favor_diz", "contra_diz",
        "tipo_votacao", "informacao_suficiente", "observacao_revisor",
    ],
    "additionalProperties": False,
}

ROTULO_VOTO = {"sim": "Sim", "nao": "Não", "abst": "Abstenção", "obstrucao": "Obstrução", "falta": "Faltou"}


# ---------- Contexto oficial ----------

def get_json(url):
    for i in range(3):
        resp = requests.get(url, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 404:
            return None
        time.sleep(2 * (i + 1))
    resp.raise_for_status()


def contexto_camara(votacao):
    id_api = votacao["id"].removeprefix("camara-")
    detalhe = (get_json(f"{CAMARA}/votacoes/{id_api}") or {}).get("dados", {})
    ctx = {"etapa": detalhe.get("descUltimaAberturaVotacao")}
    afetadas = detalhe.get("proposicoesAfetadas") or []
    if afetadas:
        p = afetadas[0]
        ctx["projeto"] = f"{p.get('siglaTipo')} {p.get('numero')}/{p.get('ano')}"
        prop = (get_json(f"{CAMARA}/proposicoes/{p['id']}") or {}).get("dados", {})
        ctx["ementa_projeto"] = prop.get("ementa") or p.get("ementa")
        ctx["ementa_detalhada"] = prop.get("ementaDetalhada") or None
        ctx["palavras_chave"] = encurta(prop.get("keywords")) or None
    objetos = detalhe.get("objetosPossiveis") or []
    if objetos:
        o = objetos[0]
        ctx["item_votado"] = f"{o.get('siglaTipo')}: {o.get('ementa')}"
    return ctx


def contexto_senado(votacao):
    codigo = votacao.get("codigo_materia")
    if not codigo and votacao.get("fonte_pagina"):
        codigo = votacao["fonte_pagina"].rstrip("/").rsplit("/", 1)[-1]
    ctx = {"projeto": votacao.get("materia")}
    if codigo:
        materia = (get_json(f"{SENADO}/materia/{codigo}.json") or {}).get("DetalheMateria", {}).get("Materia", {})
        basicos = materia.get("DadosBasicosMateria", {})
        ctx["ementa_projeto"] = basicos.get("EmentaMateria")
        ctx["explicacao_ementa"] = basicos.get("ExplicacaoEmentaMateria") or None
        ctx["palavras_chave"] = encurta((basicos.get("IndexacaoMateria") or "").strip()) or None
    return ctx


def encurta(texto, limite=500):
    """Palavras-chave da Câmara podem ter milhares de caracteres."""
    if not texto or len(texto) <= limite:
        return texto
    return texto[:limite].rsplit(",", 1)[0] + "…"


def placar(votacao):
    contagem = Counter(v["voto"] for v in votacao["votos"])
    return {ROTULO_VOTO[k]: contagem[k] for k in ROTULO_VOTO if contagem.get(k)}


def monta_entrada(votacao, contexto):
    """Texto enviado à IA: só dados oficiais, sem nomes nem partidos."""
    casa = "Câmara dos Deputados" if votacao["casa"] == "camara" else "Senado Federal"
    dados = {
        "casa": casa,
        "data": votacao["data"],
        "descricao_oficial_da_votacao": votacao["descricao_oficial"],
        "resultado": {True: "aprovada", False: "rejeitada"}.get(votacao.get("aprovada"), "não informado"),
        "placar": placar(votacao),
        **{k: v for k, v in contexto.items() if v},
    }
    return (
        "Dados oficiais da votação:\n\n"
        + json.dumps(dados, ensure_ascii=False, indent=2)
        + "\n\nEscreva os textos seguindo as regras."
    )


# ---------- IA ----------

def gera_textos(cliente, entrada):
    import anthropic

    resposta = cliente.beta.messages.create(
        model=MODELO,
        max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",  # se o modelo recusar, a API tenta outro modelo na mesma chamada
        cache_control={"type": "ephemeral"},  # o prompt de sistema é igual em todas as chamadas
        system=PROMPT_SISTEMA,
        output_config={
            "effort": "medium",
            "format": {"type": "json_schema", "schema": ESQUEMA},
        },
        messages=[{"role": "user", "content": entrada}],
    )
    if resposta.stop_reason == "refusal":
        raise RuntimeError(f"a IA recusou ({getattr(resposta.stop_details, 'category', None)})")
    if resposta.stop_reason == "max_tokens":
        raise RuntimeError("resposta cortada (max_tokens)")
    texto = next(b.text for b in resposta.content if b.type == "text")
    return json.loads(texto), resposta.model


def confere_equilibrio(textos):
    """Regra do produto: a favor e contra com tamanho parecido."""
    a, c = len(textos["a_favor_diz"].split()), len(textos["contra_diz"].split())
    if min(a, c) == 0 or max(a, c) / min(a, c) > 1.2:
        return f"Argumentos desequilibrados: a favor {a} palavras, contra {c}."
    return None


# ---------- Saída ----------

def planilha_revisao(itens, periodo):
    linhas = [
        f"# Revisão dos textos — semana de {periodo['inicio']} a {periodo['fim']}",
        "",
        "Para cada votação: confira com a fonte, corrija o texto no JSON e mude `revisado` para `true`.",
        "",
    ]
    for item in itens:
        t = item.get("textos") or {}
        linhas += [f"## {item['id']} — {item['data']}", ""]
        if item.get("erro"):
            linhas += [f"**Erro:** {item['erro']}", ""]
            continue
        linhas += [
            f"- [ ] Revisado",
            f"- **Oficial:** {item['descricao_oficial']}",
            f"- **Fonte:** {item['fonte_pagina'] or item['fonte']}",
            f"- **Tipo:** {t.get('tipo_votacao')}",
            "",
            f"**Frase:** {t.get('frase_simples')}",
            "",
            f"**O que muda:** {t.get('o_que_muda')}",
            "",
            f"**A favor:** {t.get('a_favor_diz')}",
            "",
            f"**Contra:** {t.get('contra_diz')}",
            "",
        ]
        alertas = [a for a in item.get("alertas", []) if a]
        if alertas:
            linhas += ["> ⚠️ " + " / ".join(alertas), ""]
    return "\n".join(linhas)


def main():
    ap = argparse.ArgumentParser(description="Gera textos em linguagem simples para revisão")
    ap.add_argument("arquivo", help="JSON gerado pelo coletor")
    ap.add_argument("--limite", type=int, help="processa só as N primeiras votações nominais")
    ap.add_argument("--sem-ia", action="store_true", help="monta o contexto sem chamar a IA")
    args = ap.parse_args()

    semana = json.loads(Path(args.arquivo).read_text(encoding="utf-8"))
    votacoes = [v for v in semana["votacoes"] if v["nominal"]][: args.limite]
    print(f"{len(votacoes)} votações nominais para processar")

    cliente = None
    if not args.sem_ia:
        import anthropic
        cliente = anthropic.Anthropic()

    itens = []
    for v in votacoes:
        contexto = contexto_camara(v) if v["casa"] == "camara" else contexto_senado(v)
        entrada = monta_entrada(v, contexto)
        item = {
            "id": v["id"], "data": v["data"], "casa": v["casa"],
            "descricao_oficial": v["descricao_oficial"],
            "fonte": v["fonte"], "fonte_pagina": v.get("fonte_pagina"),
            "contexto": contexto, "textos": None, "alertas": [],
            "revisado": False,
        }
        if args.sem_ia:
            print(f"\n----- {v['id']} -----\n{entrada}")
        else:
            try:
                textos, modelo = gera_textos(cliente, entrada)
                item.update(textos=textos, modelo=modelo,
                            gerado_em=datetime.now(timezone.utc).isoformat(timespec="seconds"))
                item["alertas"] = [
                    confere_equilibrio(textos),
                    None if textos["informacao_suficiente"] else "IA diz que faltou informação",
                    textos["observacao_revisor"] or None,
                ]
                print(f"ok  {v['id']}: {textos['frase_simples']}")
            except Exception as erro:  # registra e segue para a próxima votação
                item["erro"] = f"{type(erro).__name__}: {erro}"
                print(f"ERRO {v['id']}: {item['erro']}", file=sys.stderr)
        itens.append(item)

    if args.sem_ia:
        return
    pasta = AQUI / "saida"
    pasta.mkdir(exist_ok=True)
    nome = Path(args.arquivo).stem.replace("semana-", "")
    (pasta / f"textos-{nome}.json").write_text(
        json.dumps({"periodo": semana["periodo"], "itens": itens}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    (pasta / f"revisao-{nome}.md").write_text(planilha_revisao(itens, semana["periodo"]), encoding="utf-8")
    erros = sum(1 for i in itens if i.get("erro"))
    print(f"\n{len(itens) - erros} textos gerados, {erros} erros. Revisão em {pasta / f'revisao-{nome}.md'}")


if __name__ == "__main__":
    main()
