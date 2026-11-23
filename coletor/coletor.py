"""Coletor semanal do E aí, Eleito?

Busca as votações nominais da Câmara e do Senado num período e o voto de cada
parlamentar, e salva tudo num JSON que alimenta o resumo semanal.

Uso:
    python coletor.py --inicio 2026-11-16 --fim 2026-11-22

Atenção: os caminhos da API do Senado seguem a versão legada
(legis.senado.leg.br/dadosabertos). Confira na documentação atual antes de
colocar em produção, e lembre que votações simbólicas não têm voto individual.
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
}


def get_json(url, params=None, tentativas=3):
    for i in range(tentativas):
        resp = requests.get(url, params=params, headers=HEADERS, timeout=30)
        if resp.status_code == 200:
            return resp.json()
        time.sleep(2 * (i + 1))
    resp.raise_for_status()


def normaliza_voto(texto):
    if not texto:
        return "falta"
    return VOTO_NORMALIZADO.get(texto.strip().lower(), texto.strip().lower())


# ---------- Câmara ----------

def votacoes_camara(inicio, fim):
    """Lista votações do Plenário da Câmara no período (datas AAAA-MM-DD)."""
    votacoes, pagina = [], 1
    while True:
        dados = get_json(f"{CAMARA}/votacoes", {
            "dataInicio": inicio, "dataFim": fim,
            "idOrgao": 180,  # Plenário
            "itens": 200, "pagina": pagina,
            "ordem": "DESC", "ordenarPor": "dataHoraRegistro",
        })["dados"]
        votacoes += dados
        if len(dados) < 200:
            return votacoes
        pagina += 1


def votos_camara(id_votacao):
    """Voto de cada deputado numa votação. Lista vazia = votação simbólica."""
    dados = get_json(f"{CAMARA}/votacoes/{id_votacao}/votos")["dados"]
    return [{
        "politico_id": f"dep-{v['deputado_']['id']}",
        "nome": v["deputado_"]["nome"],
        "partido": v["deputado_"].get("siglaPartido"),
        "uf": v["deputado_"].get("siglaUf"),
        "voto": normaliza_voto(v.get("tipoVoto")),
    } for v in dados]


def coleta_camara(inicio, fim):
    saida = []
    for v in votacoes_camara(inicio, fim):
        votos = votos_camara(v["id"])
        saida.append({
            "casa": "camara",
            "id": v["id"],
            "data": (v.get("dataHoraRegistro") or v.get("data") or "")[:10],
            "descricao_oficial": v.get("descricao"),
            "aprovada": v.get("aprovacao"),
            "nominal": bool(votos),
            "votos": votos,
            "fonte": f"{CAMARA}/votacoes/{v['id']}",
            # Preenchidos depois, com IA + revisão humana:
            "frase_simples": None,
            "pauta": None,
        })
        time.sleep(0.3)  # gentileza com a API
    return saida


# ---------- Senado ----------

def coleta_senado(inicio, fim):
    """Votações nominais do Plenário do Senado no período (datas AAAAMMDD)."""
    i, f = inicio.replace("-", ""), fim.replace("-", "")
    dados = get_json(f"{SENADO}/plenario/lista/votacao/{i}/{f}.json")
    lista = (dados.get("ListaVotacoes", {}).get("Votacoes", {}) or {}).get("Votacao", [])
    if isinstance(lista, dict):
        lista = [lista]
    saida = []
    for v in lista:
        votos_raw = (v.get("Votos") or {}).get("VotoParlamentar", [])
        if isinstance(votos_raw, dict):
            votos_raw = [votos_raw]
        saida.append({
            "casa": "senado",
            "id": v.get("CodigoSessaoVotacao"),
            "data": v.get("DataSessao"),
            "descricao_oficial": v.get("DescricaoVotacao"),
            "aprovada": v.get("Resultado"),
            "nominal": bool(votos_raw),
            "votos": [{
                "politico_id": f"sen-{p.get('CodigoParlamentar')}",
                "nome": p.get("NomeParlamentar"),
                "partido": p.get("SiglaPartido"),
                "uf": p.get("SiglaUF"),
                "voto": normaliza_voto(p.get("SiglaVoto") or p.get("Voto")),
            } for p in votos_raw],
            "fonte": f"{SENADO}/plenario/lista/votacao/{i}/{f}",
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
