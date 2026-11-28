# Contexto do projeto para o Claude Code

Este arquivo resume a conversa de produto e design em que o projeto nasceu (claude.ai, 23/11/2026). Leia antes de mexer em qualquer coisa.

## Quem é a dona do projeto
Kathleen, Group Product Designer, no Brasil. Fala português; responda em português. Ela decide produto e design; prefere ver as coisas funcionando e iterar rápido.

## O produto
**E aí, Eleito?** — plataforma cívica, apartidária, para o eleitor "ficar de olho" nos políticos que escolheu. Toda segunda, um e-mail personalizado em linguagem simples conta o que eles fizeram e o que deixaram de fazer nas pautas da pessoa. No site, a área **Tô de olho** é atualizada no mesmo dia e guarda o histórico completo de cada um.

Frase de lançamento: "Na urna aparece FIM. Pra gente, é só o começo."
Público: qualquer eleitor, inclusive leigos em política (teste de clareza: alguém de 60+ ou com pouca escolaridade precisa entender).

## Evidência (pesquisa com 24 eleitores, out–nov/2025)
- 83% dizem que histórico de atuação é o critério nº 1 de voto.
- 71% já votaram com pouca confiança por falta de informação.
- 71% apontam excesso de informação e fake news como maior dificuldade.
- 58% só acompanham eleitos "quando aparece na mídia" → o app precisa ir até a pessoa.
- Amostra enviesada (16 de SC, 20 com superior completo). Falta testar disposição a pagar.

## Decisões já tomadas (não reabrir sem a Kathleen)
- **Canais do MVP:** site + e-mail semanal (Brevo). A ideia de lançar só com o site foi avaliada e descartada em 24/11/2026: o e-mail vai até a pessoa (58% só acompanham "quando aparece na mídia"). WhatsApp e SMS foram descartados nesta fase (custo; política da Meta proíbe entidades que oferecem serviços relacionados à política).
- **Só resumo personalizado**, nunca resumo geral.
- **Acesso sem senha** por link mágico; sessão longa; dados no servidor (Supabase sugerido).
- **Cargos (mudou em 28/11/2026, prioridade urgente): todos os cargos entram no MVP**: vereador, prefeito, deputado estadual, governador, deputado federal, senador e presidente. Motivo: a cobrança mais visível no dia a dia é local (ex.: 39 vereadores de Manaus faltaram à audiência sobre as queimadas). Presidente continua como **sugestão** ("Ficar de olho" ou "Agora não, ocultar cargo"). Executivos (prefeito, governador, presidente) mostram decisões (sanções, vetos, decretos), não votos.
  - **Limite dos dados:** não existe fonte nacional para os 5.570 municípios e 27 assembleias. Muitas câmaras usam o SAPL (Interlegis), que tem API própria por câmara (ex.: Manaus em sapl.cmm.am.gov.br, ainda não testada); outras só publicam PDF. Prefeituras: diários oficiais via Querido Diário (cerca de 350 cidades em 2024). Por isso a cobertura local cresce por cidade/estado, e a interface diz com clareza onde ainda não temos dados.
  - Presença em audiência pública e em comissão também conta como atuação (não só votação em plenário), quando a fonte registrar.
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


## Design system (obrigatório na interface)
O design system **E aí, Eleito?** está em `design-system/` (cópia do publicado no claude.ai em 24/11/2026). Leia `design-system/README.md` antes de qualquer tela.
- Carregue `design-system/tokens.css` e `design-system/components/bundle.css`.
- Componentes genéricos: classes `.tr-*` (kit do Trama). Componentes cívicos: `.ee-*` (grifo, ícones de voto, card do político, aviso de silêncio, barra de cargos, chip de pauta, placar, explicação da proposta, cobrar).
- Cada componente tem guia em `design-system/components/<Nome>/README.md` e exemplo em `preview.html`.
- Use só tokens alias (`t-*`, `sp-*`, `r-*`, `e-*`, `c-*`), nunca os globais `g-*` nem cores soltas.
- Regras da marca e decisões EE1 a EE8: `design-system/11-marca-e-neutralidade.md`.
- O protótipo `site/index.html` usa o design system desde 24/11/2026 (carrega `../design-system/tokens.css` e `components/bundle.css`; o `<style>` da página só tem layout com tokens alias). Prévia privada: https://claude.ai/artifact/B67zivKrNubXZpR65M4Siq (para publicar, copie a página com os caminhos sem `../`). O e-mail (`email/`) ainda não foi migrado.

## O que existe no repositório
- `site/index.html` — protótipo completo, HTML único, dados fictícios (Partido A–G, nomes inventados). Rotas por hash: #inicio, #cadastro, #semana (Tô de olho), #perfil-<id>, #cargos, #eleicao, #preferencias, #entrar.
- `email/email-sua-semana.html` — modelo do e-mail semanal (sintaxe de variáveis do Brevo). Ainda não usa o design system.
- `coletor/coletor.py` — busca votações da Câmara (API v2) e do Senado (API legada) e salva JSON. Validado contra as APIs reais em 23/11/2026 (semana 16–22/11 e outubro/2026). O que aprendemos:
  - A Câmara devolve no máximo 100 itens por página; o coletor segue o link `next`.
  - Muitas votações da Câmara são simbólicas (sem voto individual) e alguns registros ("Alteração do Regime de Tramitação") dão 404 no detalhe; ambos saem com `nominal: false`.
  - O Senado usa votos como `P-NRV` (presente, não votou) e `Presidente (art. 51 RISF)`; votações secretas não têm voto individual.
  - Na Câmara o `dataFim` é exclusivo; o coletor soma um dia.
  - **"Faltou":** a Câmara só lista quem votou. O coletor completa os 513 cruzando com os deputados em exercício na data e com a presença na sessão. No Senado vêm os 81.
  - **Decisão (Kathleen, 23/11/2026): tudo que não é voto aparece como "faltou"** (`voto = "falta"`). O detalhe fica em `falta_detalhe`, só para transparência: `nao_compareceu` (Câmara: sem presença na sessão; Senado: `NCom`), `nao_votou` (estava na sessão e não votou; Senado: `P-NRV`) e `ausencia_justificada` (Senado: `MIS`, `AP`, `LS`, `LP`…, código em `voto_oficial`). A API da Câmara não informa ausência justificada.
- `linguagem/` — pipeline de linguagem simples (passo 2). `simplificar.py` lê o JSON do coletor, busca a ementa oficial (Câmara `/proposicoes`, Senado `/materia`) e chama a API do Claude (`claude-sonnet-5-5`, saída em JSON estruturado, fallback de recusa ligado; ainda uma chamada por votação, falta passar para a Batch API). Gera `saida/revisao-*.md` para revisão humana e `saida/textos-*.json` com `revisado: false`. As regras de escrita ficam em `prompt_sistema.md` (é a metodologia pública: mudanças ali são decisão de produto). O script alerta quando os argumentos a favor e contra diferem mais de 20% em tamanho. Precisa de `ANTHROPIC_API_KEY` (variável de ambiente; segredos de rede não funcionam para hosts da Anthropic). **Ainda não foi rodado com a IA**: só o contexto (`--sem-ia`) foi validado.
- `db/schema.sql` — esquema Supabase com RLS; guarda o mínimo; apagar o usuário apaga tudo.
- `docs/decisoes.md` — resumo das decisões.

## Como a atualização funciona (pipeline)
1. **Coleta (todo dia, de madrugada):** GitHub Actions agendado roda `coletor/coletor.py` e grava votações e votos novos no Supabase. Sem IA. Rodar diariamente também evita a pausa do Supabase gratuito (pausa após 1 semana sem atividade).
2. **Explicação (uma vez por votação, não por usuário):** para cada votação nova, a IA gera `frase_simples`, `o_que_muda`, `a_favor_diz`, `contra_diz` e `pauta`. Usar a Batch API (50% de desconto), pois nada precisa ser instantâneo.
   - Texto: **Claude Sonnet 5.5** (`claude-sonnet-5-5`) — qualidade e neutralidade importam.
   - Classificação de pauta: **Claude Haiku 5.5** (`claude-haiku-5-5`).
   - Instruções do prompt: linguagem para leigos, sem adjetivos, argumentos a favor e contra com o mesmo tamanho, nunca opinar.
3. **Revisão humana:** nada aparece no site sem `revisado = true`.
4. **Página Tô de olho e e-mail semanal:** montados por código (sem IA), cruzando quem a pessoa segue com as votações revisadas. Toda segunda a página é atualizada e o e-mail sai pelo Brevo.

## Custos estimados (piloto)
- Claude API: ~US$ 1–5/mês (cresce com o número de votações, não de usuários).
- Supabase, Vercel, GitHub Actions: plano gratuito.
- Domínio .com.br: ~R$ 40/ano.
- Maior custo real: tempo de revisão humana semanal.

## Próximos passos (em ordem)
1. Rodar o coletor com uma semana real e corrigir o que quebrar.
2. Pipeline de linguagem simples: IA gera frase, "o que muda", argumento a favor e contra; uma pessoa revisa (`revisado = true`) antes de publicar.
3. Classificar cada votação em uma pauta (metodologia pública).
4. Criar o projeto Supabase, rodar o schema, ligar o login por link mágico.
5. Transformar o protótipo em app real conectado ao banco, mantendo design e textos.
6. Job semanal (segunda, 8h) que atualiza a página Tô de olho e envia o e-mail de cada pessoa pelo Brevo; medir abertura do e-mail e retorno ao site.
7. Lista de espera e lançamento antes de 1º/2/2027 (posse do novo Congresso).

## Pendências fora do código
- Busca no INPI (classes 9, 38, 41, 42), domínio eaieleito.com.br, @eaieleito.
- Teste de compreensão com 5 pessoas leigas.
- Consulta jurídica: LGPD e direito eleitoral.
- Definir quem revisa os resumos toda semana.

## Regras inegociáveis
Apartidário; mesmo formato e peso visual para todos; toda informação com link para a fonte oficial; nunca guardar em quem a pessoa votou; nada de dinheiro de partido/candidato, anúncio político ou venda de dados.
