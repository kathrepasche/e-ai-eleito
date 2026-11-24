E aí, Eleito? é o design system da plataforma cívica e apartidária que ajuda o eleitor a ficar de olho nos políticos que escolheu. Ele aplica a identidade da marca (azul-tinta, papel, grafite e o grifo marca-texto) sobre o kit do Trama, que traz as regras de usabilidade e acessibilidade citadas de onze referências públicas (Apple HIG, GOV.UK, gov.br DS e outras). A meta de acessibilidade é WCAG 2.2 AA.

## Como usar este sistema

- Carregue `tokens.css` e `components/bundle.css`. O kit é só CSS, sem JavaScript.
- Componentes genéricos usam as classes do Trama (`.tr-btn`, `.tr-field`, `.tr-table`, `.tr-msg` e outras). Componentes cívicos da marca usam o prefixo `.ee-`: `.ee-grifo`, `.ee-voto`, `.ee-politico`, `.ee-silencio`, `.ee-cargos`, `.ee-pauta`, `.ee-placar`, `.ee-proposta`, `.ee-cobrar`.
- Use só os tokens alias (`t-*`, `sp-*`, `r-*`, `e-*`, `c-*`). Os globais `g-*` são valores brutos e não entram em produto.
- Tema: `data-theme="light"` ou `data-theme="dark"` no elemento raiz; sem o atributo, segue `prefers-color-scheme`. Para a faixa grafite da marca dentro do tema claro (abertura do site, rodapé), envolva o trecho em `.tr-inverse`.
- As seções do guia e os componentes do kit base foram escritos para o Trama e citam as referências de cada regra. Elas valem integralmente aqui. Onde houver conflito, valem este README e a seção "Marca e neutralidade".

## Conteúdo e voz

**Personalidade.** Um amigo bem informado que lê o noticiário político por você e conta o essencial, sem opinar. Direto, calmo, com humor leve.

**Fatos, não adjetivos.** Escreva "faltou a 3 votações", nunca "deputado faltoso". O humor recai sobre o comportamento ("faltou", "ficou em silêncio"), nunca sobre a pessoa.

**Linguagem para leigos.** Português do Brasil, "você" no singular, frases curtas e voz ativa. Troque o jargão pelo efeito: "o que muda pra você" em vez de "impacto da proposição". Sigla por extenso na primeira vez.

**Vocabulário da marca.**

| Use | Em vez de |
| --- | --- |
| Ficar de olho | Seguir |
| Tirar o olho | Deixar de seguir |
| Tô de olho | Minha semana, Meus políticos |
| Votou a favor / Votou contra | Aprovou / Reprovou |
| Faltou | Ausente |
| Cobrar | Contatar |
| E aí, eleito? | (bordão, no fim de avisos de silêncio e no título da cobrança) |

**Caixa de frase** em títulos, botões, navegação e rótulos. Rótulos de ação com até 3 palavras.

## Neutralidade (regras da marca)

- **Mesmo formato e mesmo peso visual** para todos os políticos, de qualquer partido ou cargo.
- **Votos sem verde e vermelho.** Os ícones de voto usam a mesma cor e mudam só a forma (`.ee-voto`). Cor de status (`t-success`, `t-danger`) é só para o sistema: erro de formulário, confirmação de envio.
- **Argumentos a favor e contra com o mesmo tamanho**, sempre na mesma ordem.
- **Toda informação tem link para a fonte oficial** (Câmara, Senado, Presidência).
- **Sem ranking, nota ou "recomendado para você".** Listas de candidatos ficam em ordem alfabética.

## Fundamentos visuais

**Cor.** Fundo papel `t-bg` (#F7F5F0 no claro, #141418 no escuro), texto grafite `t-fg-1`. A marca azul-tinta `t-brand` (#3B3486) fica no botão primário, no item ativo, em controles marcados e em links; texto sobre ela usa `t-on-brand`. O amarelo marca-texto (`t-mark`, #F5C544) é só grifo e preenchimento, sempre com `t-mark-fg` por cima, nunca como cor de texto. O aviso de silêncio usa `t-warning-subtle` e `t-warning-border`. Contornos de controle usam `t-border-control` (3:1 sobre o papel); divisores, `t-border-subtle`.

**Tipografia.** Space Grotesk nos títulos (`font-display`, grupo Títulos) e Inter no texto (`font-sans`), pelo Google Fonts. Corpo padrão `tr-body` (16/24); mínimo `tr-caption` (12/16), e no produto, texto corrido nunca abaixo de 16px, pensando no público com mais de 60 anos. Números de destaque (placar, presença) em `t-font-display` peso 700.

**Forma.** A marca é arredondada: `r-md` (12px) em controles, `r-lg` (18px) em cards e mensagens, `r-xl` (20px) em diálogos, `r-pill` em chips de pauta, barra de cargos e placar, `r-2xl` (28px) no ícone do app.

**Espaçamento, elevação, estados, foco, densidade e layout** seguem o kit base: base de 4px (`sp-*`), elevações `e-1` a `e-6`, anel de foco `t-focus` de 2px afastado 2px só em `:focus-visible`, alvo de toque mínimo `c-touch` (44 x 44px).

**Grifo.** `.ee-grifo` destaca o número ou o tema principal de um título: "Tô de olho em <grifo>3 políticos</grifo>". No máximo um por bloco.

## Iconografia

- **Ícones de voto** (`.ee-voto`): círculo cheio com check (a favor), círculo com X (contra), círculo com traço (abstenção), círculo tracejado (faltou) e balão (discursou). Sempre com rótulo em texto.
- **Ícones de interface**: Material Symbols Outlined, peso 400, tamanhos `icon-sm` a `icon-lg`, como no kit base. Sem emoji.
- **Olho**: o símbolo de "Ficar de olho" no botão de seguir e na navegação.

## Logo

O conceito é "Depois do FIM": a tela da urna com "FIM" riscado e um balão amarelo "E aí?" saindo dela. Frase de lançamento: "Na urna aparece FIM. Pra gente, é só o começo." Os arquivos estão no grupo de assets Logos:

- `icone-completo.svg`: a partir de 96px.
- `icone-simplificado.svg`: abaixo de 96px, com "?" no lugar de "E aí?".
- `logo-horizontal.svg`: ícone e nome lado a lado, para cabeçalho e documentos.

Nome curto no ícone do celular: "Eleito". A urna é sempre estilizada, sem as cores das teclas reais, para não parecer um produto oficial do TSE. Os textos dos SVGs ainda usam fonte do sistema; converta em curvas antes de imprimir.

## Acessibilidade e legislação

Meta WCAG 2.2 AA, com contraste remedido sobre o fundo papel em cada token (veja as notas em `tokens.json`). Observe a Lei nº 13.146/2015 (Estatuto da Pessoa com Deficiência) e a Lei nº 13.709/2018 (LGPD): guarde o mínimo de dados e nunca registre em quem a pessoa votou. No período de campanha, o Modo eleição não publica resultados somados de respostas (Resolução TSE nº 23.600/2019).
