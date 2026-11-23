"""Coletor semanal do E aí, Eleito?

Busca as votações nominais da Câmara e do Senado num período e o voto de cada
parlamentar, e salva tudo num JSON que alimenta o resumo semanal.

Uso:
    python coletor.py --inicio 2026-11-16 --fim 2026-11-22

Validado contra as APIs reais em 23/11/2026. Votações simbólicas e secretas
não têm voto individual (saem com "nominal": false). A Câmara só lista quem
votou: para saber quem faltou, falta cruzar com os deputados em exercício.
"""

import argparse
import json
import time
from datetime import date
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


def normaliza_voto(texto):
    if not texto:
        return "falta"
    return VOTO_NORMALIZADO.get(texto.strip().lower(), texto.strip().lower())


# ---------- Câmara ----------

def votacoes_camara(inicio, fim):
    """Lista votações do Plenário da Câmara no período (datas AAAA-MM-DD)."""
    # A API devolve no máximo 100 itens por página, então seguimos o link "next".
    votacoes, pagina = [], 1
    while True:
        resposta = get_json(f"{CAMARA}/votacoes", {
            "dataInicio": inicio, "dataFim": fim,
            "idOrgao": 180,  # Plenário
            "itens": 100, "pagina": pagina,
            "ordem": "DESC", "ordenarPor": "dataHoraRegistro",
        }) or {}
        votacoes += resposta.get("dados", [])
        links = {l.get("rel"): l.get("href") for l in resposta.get("links", [])}
        if "next" not in links:
            return votacoes
        pagina += 1


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
        "voto": normaliza_voto(v.get("tipoVoto")),
        "voto_oficial": v.get("tipoVoto"),
    } for v in dados]


def coleta_camara(inicio, fim):
    saida = []
    for v in votacoes_camara(inicio, fim):
        votos = votos_camara(v["id"])
        aprovacao = v.get("aprovacao")
        saida.append({
            "casa": "camara",
            "id": f"camara-{v['id']}",
            "data": (v.get("dataHoraRegistro") or v.get("data") or "")[:10],
            "descricao_oficial": v.get("descricao"),
            "aprovada": None if aprovacao is None else bool(aprovacao),
            "nominal": bool(votos),
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
            "aprovada": RESULTADO_SENADO.get(v.get("Resultado")),
            "secreta": secreta,
            "nominal": bool(votos_raw),
            "votos": [{
                "politico_id": f"sen-{p.get('CodigoParlamentar')}",
                "nome": p.get("NomeParlamentar"),
                "partido": p.get("SiglaPartido"),
                "uf": p.get("SiglaUF"),
                "voto": normaliza_voto(p.get("SiglaVoto") or p.get("Voto")),
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
