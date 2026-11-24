"""Coletor semanal do E aí, Eleito?

Busca as votações nominais da Câmara e do Senado num período e o voto de cada
parlamentar, e salva tudo num JSON que alimenta o resumo semanal.

Uso:
    python coletor.py --inicio 2026-11-16 --fim 2026-11-22

Validado contra as APIs reais em 23/11/2026. Votações simbólicas e secretas
não têm voto individual (saem com "nominal": false).

Valores de "voto": sim, nao, abst, obstrucao, art17 (presidente da Câmara),
presidente (presidente da sessão no Senado) e falta.

Decisão de produto (Kathleen, 23/11/2026): tudo que não é voto aparece como
"faltou". O detalhe fica em "falta_detalhe", para transparência:
  - nao_compareceu: não compareceu / não registrou presença na sessão;
  - nao_votou: estava na sessão, mas não votou nesta votação;
  - ausencia_justificada: Senado, missão, atividade parlamentar ou licença
    (o código original fica em "voto_oficial").
A Câmara só lista quem votou; os ausentes são completados cruzando com os
deputados em exercício na data e com a presença registrada na sessão.
"""

import argparse
import json
import time
from datetime import date, timedelta
from pathlib import Path

import requests

CAMARA = "https://dadosabertos.camara.leg.br/api/v2"
SENADO = "https://legis.senado.leg.br/dadosabertos"
HEADERS = {"Accept": "application/json", "User-Agent": "eaieleito-coletor/0.1"}

# Normaliza os nomes de voto das duas Casas para o vocabulário do app.
VOTO_NORMALIZADO = {
    "sim": "sim",
    "não": "nao",
    "nao": "nao",
    "abstenção": "abst",
    "abstencao": "abst",
    "obstrução": "obstrucao",
    "artigo 17": "art17",
    "art. 17": "art17",
    # Senado: presente, mas não registrou voto.
    "p-nrv": "nao_votou",
    # Senado: quem preside a sessão não vota (art. 51 do Regimento).
    "presidente (art. 51 risf)": "presidente",
    # Senado: não compareceu, sem justificativa registrada.
    "ncom": "nao_compareceu",
    # Senado: ausências justificadas (missão, atividade parlamentar, licenças).
    # O código original fica em "voto_oficial" para o app explicar o motivo.
    "mis": "ausencia_justificada",
    "ap": "ausencia_justificada",
    "ls": "ausencia_justificada",
    "lp": "ausencia_justificada",
    "lg": "ausencia_justificada",
    "lap": "ausencia_justificada",
    "lc": "ausencia_justificada",
}


def get_json(url, params=None, tentativas=3):
    """GET com novas tentativas. Devolve None se o recurso não existe (404)."""
    for i in range(tentativas):
        resp = requests.get(url, params=params, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 404:
            return None
        time.sleep(2 * (i + 1))
    resp.raise_for_status()


TIPOS_DE_FALTA = {"nao_compareceu", "nao_votou", "ausencia_justificada"}


def normaliza_voto(texto):
    if not texto:
        return "nao_compareceu"
    return VOTO_NORMALIZADO.get(texto.strip().lower(), texto.strip().lower())


def registro_de_voto(categoria):
    """Campos "voto" e "falta_detalhe" a partir da categoria interna."""
    if categoria in TIPOS_DE_FALTA:
        return {"voto": "falta", "falta_detalhe": categoria}
    return {"voto": categoria, "falta_detalhe": None}


# ---------- Câmara ----------

def paginas_camara(caminho, params=None):
    """Junta todas as páginas de um endpoint da Câmara (máx. 100 itens cada)."""
    params = dict(params or {}, itens=100)
    itens, pagina = [], 1
    while True:
        resposta = get_json(f"{CAMARA}/{caminho}", dict(params, pagina=pagina)) or {}
        itens += resposta.get("dados", [])
        if not any(l.get("rel") == "next" for l in resposta.get("links", [])):
            return itens
        pagina += 1


_cache_exercicio, _cache_presenca = {}, {}


def deputados_em_exercicio(dia):
    """Deputados em exercício na data (titulares e suplentes): {id: dados}."""
    if dia not in _cache_exercicio:
        lista = paginas_camara("deputados", {"dataInicio": dia, "dataFim": dia})
        _cache_exercicio[dia] = {d["id"]: d for d in lista}
    return _cache_exercicio[dia]


def presentes_na_sessao(id_evento):
    """IDs dos deputados que registraram presença na sessão (evento)."""
    if not id_evento:
        return None
    if id_evento not in _cache_presenca:
        resposta = get_json(f"{CAMARA}/eventos/{id_evento}/deputados")
        _cache_presenca[id_evento] = (
            None if resposta is None else {d["id"] for d in resposta.get("dados", [])}
        )
    return _cache_presenca[id_evento]


def completa_ausentes_camara(votos, dia, id_evento):
    """A Câmara só lista quem votou. Acrescenta quem estava em exercício e não votou.

    Todos saem com voto "falta". Em "falta_detalhe":
    - "nao_votou": registrou presença na sessão, mas não votou nesta votação.
    - "nao_compareceu": não registrou presença na sessão.
    A API não informa ausências justificadas (missão, licença) da Câmara.
    """
    votaram = {v["politico_id"] for v in votos}
    presentes = presentes_na_sessao(id_evento)
    ausentes = []
    for id_dep, d in deputados_em_exercicio(dia).items():
        if f"dep-{id_dep}" in votaram:
            continue
        estava = presentes is not None and id_dep in presentes
        ausentes.append({
            "politico_id": f"dep-{id_dep}",
            "nome": d.get("nome"),
            "partido": d.get("siglaPartido"),
            "uf": d.get("siglaUf"),
            **registro_de_voto("nao_votou" if estava else "nao_compareceu"),
            "voto_oficial": None,
            "presenca_sessao": estava if presentes is not None else None,
        })
    return votos + sorted(ausentes, key=lambda a: a["nome"] or "")


def votacoes_camara(inicio, fim):
    """Lista votações do Plenário da Câmara no período (datas AAAA-MM-DD)."""
    # Na API da Câmara o dataFim é exclusivo: somamos um dia para incluir o último.
    fim_exclusivo = (date.fromisoformat(fim) + timedelta(days=1)).isoformat()
    return paginas_camara("votacoes", {
        "dataInicio": inicio, "dataFim": fim_exclusivo,
        "idOrgao": 180,  # Plenário
        "ordem": "DESC", "ordenarPor": "dataHoraRegistro",
    })


def votos_camara(id_votacao):
    """Voto de cada deputado numa votação. Lista vazia = votação simbólica.

    Alguns registros (ex.: "Alteração do Regime de Tramitação") aparecem na
    lista mas dão 404 no detalhe: não são votações de verdade, então ficam vazios.
    """
    resposta = get_json(f"{CAMARA}/votacoes/{id_votacao}/votos")
    dados = (resposta or {}).get("dados", [])
    return [{
        "politico_id": f"dep-{v['deputado_']['id']}",
        "nome": v["deputado_"]["nome"],
        "partido": v["deputado_"].get("siglaPartido"),
        "uf": v["deputado_"].get("siglaUf"),
        **registro_de_voto(normaliza_voto(v.get("tipoVoto"))),
        "voto_oficial": v.get("tipoVoto"),
    } for v in dados]


def coleta_camara(inicio, fim):
    saida = []
    for v in votacoes_camara(inicio, fim):
        votos = votos_camara(v["id"])
        nominal = bool(votos)
        dia = (v.get("dataHoraRegistro") or v.get("data") or "")[:10]
        if nominal:
            id_evento = (v.get("uriEvento") or "").rstrip("/").rsplit("/", 1)[-1] or None
            votos = completa_ausentes_camara(votos, dia, id_evento)
        aprovacao = v.get("aprovacao")
        saida.append({
            "casa": "camara",
            "id": f"camara-{v['id']}",
            "data": dia,
            "descricao_oficial": v.get("descricao"),
            "aprovada": None if aprovacao is None else bool(aprovacao),
            "nominal": nominal,
            "votos": votos,
            "fonte": f"{CAMARA}/votacoes/{v['id']}",
            "fonte_pagina": pagina_camara(v),
            # Preenchidos depois, com IA + revisão humana:
            "frase_simples": None,
            "pauta": None,
        })
        time.sleep(0.3)  # gentileza com a API
    return saida


def pagina_camara(v):
    """Página pública da proposição na Câmara, para o link "ver na fonte"."""
    uri = v.get("uriProposicaoObjeto") or ""
    id_prop = uri.rstrip("/").rsplit("/", 1)[-1] if uri else v["id"].split("-")[0]
    return f"https://www.camara.leg.br/propostas-legislativas/{id_prop}"


# ---------- Senado ----------

RESULTADO_SENADO = {"A": True, "R": False}

def coleta_senado(inicio, fim):
    """Votações nominais do Plenário do Senado no período (datas AAAAMMDD)."""
    i, f = inicio.replace("-", ""), fim.replace("-", "")
    dados = get_json(f"{SENADO}/plenario/lista/votacao/{i}/{f}.json") or {}
    lista = (dados.get("ListaVotacoes", {}).get("Votacoes", {}) or {}).get("Votacao", [])
    if isinstance(lista, dict):
        lista = [lista]
    saida = []
    for v in lista:
        votos_raw = (v.get("Votos") or {}).get("VotoParlamentar", [])
        if isinstance(votos_raw, dict):
            votos_raw = [votos_raw]
        secreta = v.get("Secreta") == "S"
        if secreta:
            votos_raw = []  # voto secreto: não existe voto individual público
        saida.append({
            "casa": "senado",
            "id": f"senado-{v.get('CodigoSessaoVotacao')}",
            "data": v.get("DataSessao"),
            "descricao_oficial": v.get("DescricaoVotacao"),
            "materia": v.get("DescricaoIdentificacaoMateria"),
            "codigo_materia": v.get("CodigoMateria"),
            "aprovada": RESULTADO_SENADO.get(v.get("Resultado")),
            "secreta": secreta,
            "nominal": bool(votos_raw),
            "votos": [{
                "politico_id": f"sen-{p.get('CodigoParlamentar')}",
                "nome": p.get("NomeParlamentar"),
                "partido": p.get("SiglaPartido"),
                "uf": p.get("SiglaUF"),
                **registro_de_voto(normaliza_voto(p.get("SiglaVoto") or p.get("Voto"))),
                "voto_oficial": p.get("SiglaVoto") or p.get("Voto"),
            } for p in votos_raw],
            "fonte": f"{SENADO}/plenario/lista/votacao/{i}/{f}",
            "fonte_pagina": (
                "https://www25.senado.leg.br/web/atividade/materias/-/materia/"
                f"{v.get('CodigoMateria')}" if v.get("CodigoMateria") else None
            ),
            "frase_simples": None,
            "pauta": None,
        })
    return saida


def main():
    ap = argparse.ArgumentParser(description="Coleta votações da semana")
    ap.add_argument("--inicio", required=True, help="AAAA-MM-DD")
    ap.add_argument("--fim", required=True, help="AAAA-MM-DD")
    args = ap.parse_args()

    resultado = {
        "periodo": {"inicio": args.inicio, "fim": args.fim},
        "coletado_em": date.today().isoformat(),
        "votacoes": coleta_camara(args.inicio, args.fim) + coleta_senado(args.inicio, args.fim),
    }
    pasta = Path(__file__).parent / "saida"
    pasta.mkdir(exist_ok=True)
    arquivo = pasta / f"semana-{args.inicio}.json"
    arquivo.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
    nominais = sum(1 for v in resultado["votacoes"] if v["nominal"])
    print(f"{len(resultado['votacoes'])} votações ({nominais} nominais) salvas em {arquivo}")


if __name__ == "__main__":
    main()
