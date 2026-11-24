# E aí, Eleito?

> Na urna aparece FIM. Pra gente, é só o começo.

Plataforma cívica e apartidária para o eleitor ficar de olho nos políticos que escolheu: um resumo semanal, personalizado e em linguagem simples, do que eles fizeram (e deixaram de fazer) nas pautas que importam para a pessoa.

## Estrutura

| Pasta | O que tem |
| --- | --- |
| `site/` | Protótipo navegável do site (HTML único, dados fictícios) |
| `email/` | Modelo do e-mail semanal "E aí, eleito?" para o Brevo |
| `coletor/` | Motor de dados: busca votações da Câmara e do Senado nas APIs de dados abertos |
| `db/` | Esquema do banco de dados (Supabase / Postgres) |
| `docs/` | Decisões de produto, regras de neutralidade e LGPD |
| `design-system/` | Design system E aí, Eleito? (tokens, CSS, guias e prévias dos componentes) |

## Primeira versão (MVP)

- Canais: **site + e-mail semanal**. Sem WhatsApp e sem SMS nesta fase.
- Cargos acompanhados: deputados federais, senadores e presidente (sugerido, pode ser ocultado).
- Acesso sem senha, por link mágico enviado por e-mail.
- Dados oficiais: [Dados Abertos da Câmara](https://dadosabertos.camara.leg.br/swagger/api.html) e [Dados Abertos do Senado](https://www12.senado.leg.br/dados-abertos).

## Como rodar o coletor

```bash
cd coletor
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python coletor.py --inicio 2026-11-16 --fim 2026-11-22
```

O resultado vai para `coletor/saida/semana-AAAA-MM-DD.json`.

## Como gerar os textos em linguagem simples

Depois de rodar o coletor:

```bash
cd linguagem
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...   # chave da API do Claude
python simplificar.py ../coletor/saida/semana-2026-11-16.json
```

Para cada votação nominal, o script busca a ementa oficial do projeto e pede à IA a frase simples, "o que muda" e os argumentos a favor e contra. Nada é publicado automaticamente: sai `linguagem/saida/revisao-*.md` para uma pessoa conferir e `textos-*.json` com `revisado: false`. As regras de escrita (metodologia pública) estão em `linguagem/prompt_sistema.md`.

Use `--sem-ia` para ver só o contexto que seria enviado, sem gastar com a API.

## Como ver o protótipo

Abra `site/index.html` no navegador. Os nomes, partidos e votações são fictícios.

## Próximos passos

1. Validar o coletor com uma semana real e medir quanto tempo leva para explicar cada votação.
2. Criar o projeto no Supabase e rodar `db/schema.sql`.
3. Gerar as frases em linguagem simples (IA + revisão humana) e publicar na página Tô de olho e no e-mail.
4. Conectar o site ao banco e ao login por link mágico.
5. Lançar a lista de espera antes da posse do novo Congresso (1º/2/2027).

## Regras inegociáveis

- Apartidário: mesmo critério e mesmo formato para todos os políticos.
- Fato, não opinião: sem adjetivos, sem nota, sem recomendação de voto.
- Toda informação com link para a fonte oficial.
- Nunca guardar em quem a pessoa votou. Dados mínimos e conta apagável (LGPD).
