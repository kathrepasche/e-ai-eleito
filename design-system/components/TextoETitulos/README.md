# TextoETitulos

Os estilos de texto do Trama aplicam a escala tipográfica a títulos, parágrafos, listas, legendas, marcações e código, com semântica HTML correta, hierarquia consistente e espaços entre blocos definidos por token.

Este componente reúne as classes `.tr-caption` a `.tr-display` e as regras para usá-las em elementos reais: `<h1>` a `<h6>`, `<p>`, `<ul>`, `<ol>`, `<dl>`, `<legend>`, `<mark>` e `<code>`. Todos são elementos nativos do HTML, como na tabela de estilos do gov.br ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). A escala e as famílias estão no fundamento Tipografia; a voz e o tom, em Escrita e conteúdo.

Títulos criam a hierarquia visual e funcionam como sumário da página para quem usa leitor de tela ([DKFDS](https://designsystem.dk/styleguide/typografi/overskrifter/)). O Trama separa os dois papéis: o nível semântico segue a estrutura do documento e a classe visual segue o contexto.

## Quando usar

- **Títulos** para estruturar a página e agrupar o conteúdo em blocos lógicos.
- **Parágrafo de abertura** uma vez por página, no topo, para resumir o conteúdo ([GOV.UK](https://design-system.service.gov.uk/styles/paragraphs/)).
- **Corpo** para todo texto corrido; **listas** para quebrar texto em itens fáceis de ler ([GOV.UK](https://design-system.service.gov.uk/styles/lists/)).
- **Marcação** para destacar ocorrências de um termo pesquisado; **código** para trechos que a pessoa vai copiar ou digitar.

## Quando não usar

- **Não use um título para destacar texto que não estrutura a página.** Para destaque, use uma mensagem, uma lista ou o parágrafo de abertura ([DKFDS](https://designsystem.dk/styleguide/typografi/overskrifter/)).
- **Não use negrito como título.** Um parágrafo em negrito não aparece na lista de títulos do leitor de tela ([DKFDS](https://designsystem.dk/styleguide/typografi/tekst/)).
- **Não use `<mark>` para ênfase geral.** Para ênfase dentro da frase, use `<strong>`; para avisos, uma mensagem.
- **Para texto editável**, use campo de texto ou área de texto; para hipertexto, o componente link ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/text/usage)).

## Anatomia

1.  **Legenda de seção (opcional).** Texto curto acima do título que indica a que grupo a página pertence ([GOV.UK](https://design-system.service.gov.uk/styles/headings/)).
2.  **Título.** Elemento `<h1>` a `<h6>` com uma classe da escala.
3.  **Abertura.** Parágrafo curto que introduz a página ou a etapa.
4.  **Corpo.** Parágrafos, listas, listas de definição e citações.
5.  **Elementos em linha.** Marcação, código, ênfase e links.
6.  **Apoio.** Metadados e notas em tamanho menor.

## Tipos

| Estilo      | Classe            | Tamanho/altura, peso | Uso no Trama                                                             |
|-------------|-------------------|----------------------|--------------------------------------------------------------------------|
| Display     | `.tr-display`     | 56/64, 700           | Páginas de entrada. Uma vez por página.                                  |
| Large title | `.tr-large-title` | 40/48, 700           | `<h1>` de páginas de conteúdo longo.                                     |
| Title 1     | `.tr-title-1`     | 32/40, 700           | `<h1>` padrão de páginas de aplicação.                                   |
| Title 2     | `.tr-title-2`     | 28/36, 600           | `<h2>` em páginas longas.                                                |
| Title 3     | `.tr-title-3`     | 24/32, 600           | `<h2>` padrão.                                                           |
| Subtitle    | `.tr-subtitle`    | 20/28, 600           | `<h3>`, títulos de card e de painel, `<legend>` de grupos de formulário. |
| Body large  | `.tr-body-lg`     | 18/28, 400           | Parágrafo de abertura.                                                   |
| Body        | `.tr-body`        | 16/24, 400           | Texto corrido e listas. Padrão.                                          |
| Body small  | `.tr-body-sm`     | 14/20, 400           | Texto em componentes densos, metadados.                                  |
| Caption     | `.tr-caption`     | 12/16, 400           | Legendas, rótulos de eixo, notas. É o menor tamanho do sistema.          |
| Mono        | `.tr-mono`        | 14/20, 400           | Código, identificadores, dados tabulares.                                |

> **Divergência entre referências** O gov.br adota fonte base de 14 px, com parágrafo em 16,8 px na grade de 12 colunas e 14 px na de 4 colunas, e deixa claro que a escolha não é definitiva ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). DKFDS e HDS usam 16 px para o texto corrido ([DKFDS](https://designsystem.dk/styleguide/typografi/tekst/), [HDS](https://hds.hel.fi/foundation/design-tokens/typography)). O Trama segue a decisão D16: Body de 16 px como base em todas as classes de janela, mínimo de 12 px. É a opção com mais margem de legibilidade, e campos em 16 px evitam que navegadores móveis ampliem a página ao focar.

## Boas práticas

**Siga a ordem dos níveis.** Depois de um `<h1>`, o próximo título é `<h2>`, nunca `<h3>` ([HDS](https://hds.hel.fi/foundation/design-tokens/typography)). Use um único `<h1>` por página, com títulos descritivos que organizam a página em torno de um tópico ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Ajuste o visual sem quebrar a semântica.** Quando um `<h3>` precisa parecer menor, troque a classe e mantenha o nível. Teste a acessibilidade sempre que a ordem visual dos títulos for alterada ([GOV.UK](https://design-system.service.gov.uk/styles/headings/)).

**Use o corpo padrão na maior parte do texto.** Body small serve a conteúdo secundário e ao interior de componentes; não o use para parágrafos longos ([GOV.UK](https://design-system.service.gov.uk/styles/paragraphs/)).

**Escreva parágrafos de até quatro linhas e limite a largura da linha.** Texto corrido ocupa no máximo 8 de 12 colunas, cerca de 75 caracteres por linha. Use a abertura uma vez, com no máximo três linhas ([DKFDS](https://designsystem.dk/styleguide/typografi/tekst/)).

**Alinhe à esquerda e não justifique.** Texto justificado cria espaços irregulares entre palavras ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/text/usage)).

**Crie hierarquia com tamanho e peso.** Evite itálico, sublinhado e caixa alta. Sublinhado parece link e itálico reduz a legibilidade ([DKFDS](https://designsystem.dk/styleguide/typografi/tekst/)). Use os pesos 400, 600 e 700.

> **Divergência entre referências** O gov.br estiliza os títulos H5 e H6 em caixa alta e o placeholder em itálico ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). O DKFDS desaconselha itálico e o GOV.UK usa caixa de frase em títulos ([DKFDS](https://designsystem.dk/styleguide/typografi/tekst/), [GOV.UK](https://design-system.service.gov.uk/styles/headings/)). O Trama segue as decisões D1 e D16: nenhum título em caixa alta e nenhum placeholder em itálico.

**Use as cores de texto pelo significado.** `--t-fg-1` para texto principal, `--t-fg-2` para secundário, `--t-fg-3` para apoio e `--t-fg-disabled` só para itens indisponíveis ([HIG](https://developer.apple.com/design/human-interface-guidelines/labels)). Em faixas escuras no tema claro, envolva o texto em `.tr-inverse`.

**Deixe texto útil selecionável.** Mensagens de erro, números de protocolo e endereços devem poder ser copiados ([HIG](https://developer.apple.com/design/human-interface-guidelines/text-views)).

### Espaços entre blocos

O gov.br define margens próprias para cada elemento de texto: títulos com margem superior e inferior, parágrafos e listas com margem inferior, itens de lista com margem menor que a lista inteira, legendas com margem dos dois lados e preenchimento próprio para código em linha e em bloco ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). O Trama adota a mesma estrutura com os tokens de espaçamento. Quando duas margens se encontram, vale a maior; elas não se somam.

| Bloco                        | Margem                        | Token                  |
|------------------------------|-------------------------------|------------------------|
| `<h1>`                       | Abaixo                        | `--sp-600`             |
| `<h2>`                       | Acima, abaixo                 | `--sp-800`, `--sp-300` |
| `<h3>` a `<h6>`              | Acima, abaixo                 | `--sp-600`, `--sp-200` |
| Parágrafo                    | Abaixo                        | `--sp-400`             |
| Lista inteira, item de lista | Abaixo                        | `--sp-400`, `--sp-200` |
| `<legend>`                   | Abaixo                        | `--f-gap-title`        |
| Bloco de código              | Preenchimento interno, abaixo | `--sp-400`, `--sp-400` |
| Código em linha, marcação    | Preenchimento lateral         | `--sp-50`              |

### Listas de texto

**Use `<ul>` para itens sem ordem, `<ol>` quando a ordem importa e `<dl>` para termos e explicações.** ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)) Introduza a lista com uma frase que termina em dois-pontos ([GOV.UK](https://design-system.service.gov.uk/styles/lists/)) e mantenha menos de três níveis ([DKFDS](https://designsystem.dk/styleguide/typografi/lister/)). Itens de lista numerada são frases completas e terminam com ponto ([GOV.UK](https://design-system.service.gov.uk/styles/lists/)). Para pares de chave e valor com ações, use a lista de resumo.

### Legenda de grupo

**Use `<legend>` como título de cada `<fieldset>`.** A legenda usa Subtitle; em grupos aninhados, desça um passo na escala a cada nível, como o gov.br sugere para fieldsets em hierarquia ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). Em páginas de pergunta única, a legenda é a própria pergunta e usa o estilo do `<h1>`.

### Marcação

**Use `<mark class="tr-mark">` para ocorrências de um termo pesquisado.** O fundo `--t-mark` com texto `--t-mark-fg` mantém contraste nos dois temas. Use em resultados de pesquisa, em tabelas filtradas e em trechos citados. Não marque frases inteiras.

### Código

**Use `<code>` com fonte monoespaçada para código, comandos e identificadores que a pessoa vai digitar.** O gov.br usa fonte monoespaçada com fundo cinza claro, em linha e em bloco ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). No Trama, código usa `--t-font-mono` sobre `--t-surface-1`; blocos ficam em `<pre><code>`, rolam na horizontal sem quebrar linhas e, quando a pessoa precisa copiar, trazem um botão Copiar.

**Faça** use títulos reais em ordem, com tamanhos que reforçam a hierarquia.

**Não faça** simular títulos com parágrafos em negrito ou em caixa alta.

### Comportamento

- **Quebra.** Títulos, rótulos e mensagens quebram linha e nunca são truncados. Truncamento só vale em células de tabela, breadcrumb, nomes de arquivo e chips, com o texto completo acessível (veja Excesso de conteúdo).
- **Aumento de texto.** Defina tamanhos em unidades relativas (`rem`), para que a pessoa possa mudar o tamanho do texto ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). O layout funciona com texto a 200% (WCAG 2.2, 1.4.4) e com espaçamento de texto ampliado (WCAG 2.2, 1.4.12).
- **Prioridade ao ampliar.** Ao aumentar o texto, mantenha a hierarquia e empilhe elementos que estavam lado a lado ([HIG](https://developer.apple.com/design/human-interface-guidelines/typography)).

## Conteúdo

- Escreva títulos em caixa de frase: inicial maiúscula só na primeira palavra, em nomes próprios e em siglas ([GOV.UK](https://design-system.service.gov.uk/styles/headings/)). Não termine títulos com ponto.
- Faça títulos que descrevem o conteúdo da seção. Em páginas de pergunta, o título é a própria pergunta.
- Comece a frase pelo objetivo, escreva para "você" e use parágrafos curtos com espaço entre eles ([DKFDS](https://designsystem.dk/styleguide/typografi/tekst/)).
- Escreva o nome completo antes da sigla na primeira menção, com a sigla entre parênteses.
- Escreva números com ponto de milhar e vírgula decimal, e unidades por extenso no texto corrido ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

## Acessibilidade

**Use elementos semânticos.** Títulos são `<h1>` a `<h6>`, parágrafos são `<p>`, listas são `<ul>`, `<ol>` ou `<dl>`. A semântica permite que leitores de tela distingam os elementos do texto ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)); classes visuais não criam semântica ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/text/usage)). Atende ao WCAG 2.2, 1.3.1 e 2.4.6.

**Não transmita significado só pela aparência.** Alguns leitores de tela não anunciam negrito nem itálico ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/text/usage)), e nem todos anunciam `<mark>`. Em resultados de pesquisa, diga também em texto quantas ocorrências há.

**Garanta contraste.** Texto menor que 24 px regular ou 18,66 px em negrito precisa de 4,5:1 com o fundo (WCAG 2.2, 1.4.3). `--t-fg-1`, `--t-fg-2` e `--t-fg-3` atendem a esse mínimo sobre `--t-bg` e `--t-surface-1` nos dois temas. Texto sobre imagem usa a camada de legibilidade (veja Imagem).

**Declare o idioma.** Use `lang="pt-BR"` no documento e `lang` em trechos em outro idioma (WCAG 2.2, 3.1.2).

## Tokens usados

| Elemento                                         | Token                                                 |
|--------------------------------------------------|-------------------------------------------------------|
| Família de texto e títulos, código               | `--t-font-sans`, `--t-font-mono`                      |
| Texto principal, secundário, apoio, indisponível | `--t-fg-1`, `--t-fg-2`, `--t-fg-3`, `--t-fg-disabled` |
| Marcação                                         | `--t-mark`, `--t-mark-fg`                             |
| Fundo de código                                  | `--t-surface-1`                                       |
| Espaços entre blocos                             | `--sp-200` a `--sp-800`, `--f-gap-title`              |
| Ajuste interno de código e marcação              | `--sp-50`                                             |

## Considerações por plataforma

### Web desktop

Use Title 1 no `<h1>` de aplicações e Large title em páginas de conteúdo longo. Limite a coluna de texto a 8 de 12 colunas.

### Web móvel

Mantenha o corpo em 16 px ([HDS](https://hds.hel.fi/foundation/design-tokens/typography)). Reduza um passo os títulos grandes na classe Compacta: Display passa a Large title e Large title passa a Title 1. O DKFDS também reduz os títulos em telas menores, e o gov.br na grade de 4 colunas ([DKFDS](https://designsystem.dk/styleguide/typografi/overskrifter/), [gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). Blocos de código rolam na horizontal dentro do próprio bloco.

### Tablets e dobráveis

Em janelas médias e expandidas, use a escala de desktop. Em layouts de dois painéis, o título do painel de detalhe usa Title 3 ou Subtitle. Ao alternar entre a tela externa e a interna de um dobrável, preserve a posição de leitura ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Tipografia
- Escrita e conteúdo
- Espaçamento
- Listas
- Excesso de conteúdo

### Referências

- [Tipografia](https://www.gov.br/ds/fundamentos-visuais/tipografia) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Labels](https://developer.apple.com/design/human-interface-guidelines/labels) Apple HIG
- [Text views](https://developer.apple.com/design/human-interface-guidelines/text-views) Apple HIG
- [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) Apple HIG
- [Headings](https://design-system.service.gov.uk/styles/headings/) GOV.UK Design System
- [Paragraphs](https://design-system.service.gov.uk/styles/paragraphs/) GOV.UK Design System
- [Lists](https://design-system.service.gov.uk/styles/lists/) GOV.UK Design System
- [Overskrifter](https://designsystem.dk/styleguide/typografi/overskrifter/) DKFDS
- [Tekst](https://designsystem.dk/styleguide/typografi/tekst/) DKFDS
- [Lister](https://designsystem.dk/styleguide/typografi/lister/) DKFDS
- [Typography](https://hds.hel.fi/foundation/design-tokens/typography) Helsinki Design System
- [Text](https://fluent2.microsoft.design/components/web/react/core/text/usage) Fluent 2

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                            |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Entram margens de bloco por token, listas de texto, legenda de grupo, marcação e código; a base de 16 px (D16) e a caixa de frase (D1) são confirmadas contra a escala do gov.br. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                     |
