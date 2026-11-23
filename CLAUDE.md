# Contexto do projeto para o Claude Code

Este arquivo resume a conversa de produto e design em que o projeto nasceu (claude.ai, 23/11/2026). Leia antes de mexer em qualquer coisa.

## Quem é a dona do projeto
Kathleen, Group Product Designer, no Brasil. Fala português; responda em português. Ela decide produto e design; prefere ver as coisas funcionando e iterar rápido.

## O produto
**E aí, Eleito?** — plataforma cívica, apartidária, para o eleitor "ficar de olho" nos políticos que escolheu. Toda segunda, um e-mail personalizado em linguagem simples conta o que eles fizeram e o que deixaram de fazer nas pautas da pessoa. No site, a área **Tô de olho** guarda o histórico completo.

Frase de lançamento: "Na urna aparece FIM. Pra gente, é só o começo."
Público: qualquer eleitor, inclusive leigos em política (teste de clareza: alguém de 60+ ou com pouca escolaridade precisa entender).

## Evidência (pesquisa com 24 eleitores, out–nov/2025)
- 83% dizem que histórico de atuação é o critério nº 1 de voto.
- 71% já votaram com pouca confiança por falta de informação.
- 71% apontam excesso de informação e fake news como maior dificuldade.
- 58% só acompanham eleitos "quando aparece na mídia" → o app precisa ir até a pessoa.
- Amostra enviesada (16 de SC, 20 com superior completo). Falta testar disposição a pagar.

## Decisões já tomadas (não reabrir sem a Kathleen)
- **Canais do MVP:** site + e-mail semanal (Brevo). WhatsApp e SMS foram avaliados e descartados nesta fase (custo; política da Meta proíbe entidades que oferecem serviços relacionados à política).
- **Só resumo personalizado**, nunca resumo geral.
- **Acesso sem senha** por link mágico; sessão longa; dados no servidor (Supabase sugerido).
- **Cargos:** deputado federal, senador e presidente. Presidente aparece como **sugestão** ("Ficar de olho" ou "Agora não, ocultar cargo", restaurável em Preferências). Deputado estadual e vereador: só a explicação do cargo ("em breve").
- **Presidente:** em vez de votos, sanções, vetos e medidas provisórias, ligados às votações que os políticos seguidos fizeram. Decretos numa segunda fase.
- **Pautas:** 3 a 5, ou "Todas as pautas".
- **Tô de olho:** barra de cargos fixa; todas as seções sempre visíveis (vazias com texto bem-humorado); "Tirar o olho" para deixar de seguir; "+ Ficar de olho em mais um" abre busca dentro da seção.
- **Perfil do político:** panorama, "Como votou" (a favor, contra, absteve-se, faltou, com número e lista de quais votações), histórico completo filtrável por pauta, silêncio por pauta, área "E aí, [nome]? Cobre direto" com e-mail, telefone, redes e mensagem pronta editável.
- **Modo eleição "Fica ou troca?":** balanço do mandato; formulário com perguntas tiradas de votações reais (Sim/Não/Tanto faz, "Importante pra mim", botão "Entender a proposta" com o que muda + argumento a favor + argumento contra, mesmo tamanho); comparativo de até 3 nomes em ordem alfabética, tema por tema, "concordou com você em X de Y". Respostas só no aparelho, nunca somadas, sem ranking nem recomendação (TSE proíbe enquetes na campanha). Parecer de advogado eleitoral antes de 2028.

## Marca e design
- Nome curto no ícone: "Eleito". Conceito visual "Depois do FIM": tela da urna com FIM riscado + balão amarelo "E aí?" (versão simplificada abaixo de 96 px troca "E aí?" por "?").
- Cores: azul-tinta #3B3486, amarelo marca-texto #F5C544 (só grifo/balão, nunca texto), grafite #1B1B1F, cinza #5A5A66, papel #F7F5F0.
- Tipos: Space Grotesk (títulos), Inter (texto, mínimo 16 px).
- **Votos sem verde/vermelho:** mesma cor, formas diferentes (sim = círculo cheio com check; não = círculo com X; abstenção = traço; falta = círculo tracejado).
- No tema escuro, texto claro sobre o grifo amarelo leva contorno preto (`--contorno`).
- Tom de voz: conversa direta e bem-humorada; o humor recai sobre o comportamento ("faltou", "sumiu"), nunca sobre a pessoa. Fatos, não adjetivos. Usar "ficar de olho" em vez de "seguir". "Tô de olho" é nome de área interna, não marca (existe um TCC "Tô De Olho" no mesmo nicho).

## O que existe no repositório
- `site/index.html` — protótipo completo, HTML único, dados fictícios (Partido A–G, nomes inventados). Rotas por hash: #inicio, #cadastro, #semana (Tô de olho), #perfil-<id>, #cargos, #eleicao, #preferencias, #entrar.
- `email/email-sua-semana.html` — modelo do e-mail (sintaxe de variáveis do Brevo).
- `coletor/coletor.py` — busca votações da Câmara (API v2) e do Senado (API legada) e salva JSON. Validado contra as APIs reais em 23/11/2026 (semana 16–22/11 e outubro/2026). O que aprendemos:
  - A Câmara devolve no máximo 100 itens por página; o coletor segue o link `next`.
  - Muitas votações da Câmara são simbólicas (sem voto individual) e alguns registros ("Alteração do Regime de Tramitação") dão 404 no detalhe; ambos saem com `nominal: false`.
  - O Senado usa votos como `P-NRV` (presente, não votou) e `Presidente (art. 51 RISF)`; votações secretas não têm voto individual.
  - Na Câmara o `dataFim` é exclusivo; o coletor soma um dia.
  - **"Faltou":** a Câmara só lista quem votou. O coletor completa os 513 cruzando com os deputados em exercício na data e com a presença na sessão. No Senado vêm os 81.
  - **Decisão (Kathleen, 23/11/2026): tudo que não é voto aparece como "faltou"** (`voto = "falta"`). O detalhe fica em `falta_detalhe`, só para transparência: `nao_compareceu` (Câmara: sem presença na sessão; Senado: `NCom`), `nao_votou` (estava na sessão e não votou; Senado: `P-NRV`) e `ausencia_justificada` (Senado: `MIS`, `AP`, `LS`, `LP`…, código em `voto_oficial`). A API da Câmara não informa ausência justificada.
- `db/schema.sql` — esquema Supabase com RLS; guarda o mínimo; apagar o usuário apaga tudo.
- `docs/decisoes.md` — resumo das decisões.

## Próximos passos (em ordem)
1. Rodar o coletor com uma semana real e corrigir o que quebrar.
2. Pipeline de linguagem simples: IA gera frase, "o que muda", argumento a favor e contra; uma pessoa revisa (`revisado = true`) antes de publicar.
3. Classificar cada votação em uma pauta (metodologia pública).
4. Criar o projeto Supabase, rodar o schema, ligar o login por link mágico.
5. Transformar o protótipo em app real conectado ao banco, mantendo design e textos.
6. Job semanal (segunda, 8h) que monta e envia o e-mail de cada pessoa pelo Brevo.
7. Lista de espera e lançamento antes de 1º/2/2027 (posse do novo Congresso).

## Pendências fora do código
- Busca no INPI (classes 9, 38, 41, 42), domínio eaieleito.com.br, @eaieleito.
- Teste de compreensão com 5 pessoas leigas.
- Consulta jurídica: LGPD e direito eleitoral.
- Definir quem revisa os resumos toda semana.

## Regras inegociáveis
Apartidário; mesmo formato e peso visual para todos; toda informação com link para a fonte oficial; nunca guardar em quem a pessoa votou; nada de dinheiro de partido/candidato, anúncio político ou venda de dados.
