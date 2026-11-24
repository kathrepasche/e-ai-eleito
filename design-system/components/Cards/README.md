# Cards

Um card é uma superfície delimitada que reúne informação e ações sobre um único assunto ou objeto, como um pedido, um documento ou uma pessoa.

Cards dão proeminência a um bloco de conteúdo e criam um padrão previsível quando se repetem ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/card/usage)). Cada card faz sentido sozinho, sem depender dos elementos ao redor ([gov.br DS](https://www.gov.br/ds/components/card), [DKFDS](https://designsystem.dk/komponenter/cards/)). Use cards com parcimônia: em excesso, eles tornam a interface confusa ([HDS](https://hds.hel.fi/components/card)).

## Quando usar

- Para listar conteúdo heterogêneo que a pessoa navega, como notícias, eventos ou projetos ([HDS](https://hds.hel.fi/components/card)).
- Para agrupar informação e ações sobre um objeto, separadas do restante da página.
- Como ponto de entrada para outra página sobre um único tema ([Ontario](https://designsystem.ontario.ca/components/detail/cards.html)).
- Para organizar gráficos em painéis, com título, fonte e ações do gráfico no próprio card ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).

## Quando não usar

- **Para o conteúdo principal da página.** Deixe-o no fluxo normal, com títulos ([DKFDS](https://designsystem.dk/komponenter/cards/)).
- **Para agrupar campos de formulário.** Use títulos e `<fieldset>` ([DKFDS](https://designsystem.dk/komponenter/cards/)).
- **Para listas longas em que a pessoa procura um item específico.** Use uma lista ou uma tabela ([Ontario](https://designsystem.ontario.ca/components/detail/cards.html)).
- **Para chaves e valores de um objeto.** Use a lista de resumo.
- **Para conteúdo que exigiria rolagem dentro do card.** Mostre o essencial e leve o restante para uma página de detalhe ([gov.br DS](https://www.gov.br/ds/components/card)).

## Anatomia

O card tem uma superfície e pelo menos um conteúdo. A superfície se divide em três áreas: títulos, conteúdo e ações ([gov.br DS](https://www.gov.br/ds/components/card)). No Trama a ordem é fixa, de cima para baixo: mídia, sobretítulo, título, texto e ações. Nem todos os elementos são obrigatórios, mas a ordem não muda ([DKFDS](https://designsystem.dk/komponenter/cards/)).

1.  **Superfície.** `--t-surface-raised` com borda ou sombra.
2.  **Mídia (opcional).** Imagem no topo, em 2:1, 16:9 ou 4:3. Mídia pode sangrar até a borda do card; o restante do conteúdo respeita o preenchimento ([gov.br DS](https://www.gov.br/ds/components/card)).
3.  **Área de título.** Sobretítulo, título e, se houver, ícone, avatar ou tag ([gov.br DS](https://www.gov.br/ds/components/card)).
4.  **Área de conteúdo.** Uma ou duas frases curtas, ou outro componente. Não coloque componentes de navegação, como carrossel, paginação, abas e menu ([gov.br DS](https://www.gov.br/ds/components/card)).
5.  **Área de ações (opcional).** Só botões e links ([gov.br DS](https://www.gov.br/ds/components/card)). A ação principal vem primeiro, alinhada ao início do conteúdo.

## Tipos

| Tipo              | Descrição                                                                                                                                                                                                                       | Regra                                                                                            |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Card de conteúdo  | Reúne informação e uma ou mais ações internas. A superfície não é clicável.                                                                                                                                                     | Use quando houver mais de um elemento interativo ([HDS](https://hds.hel.fi/components/linkbox)). |
| Card de navegação | O card inteiro é um único link. Título sublinhado e seta no canto inferior ([DKFDS](https://designsystem.dk/komponenter/cards/)); se sair do domínio do produto, ícone de link externo com "(site externo)" no texto acessível. | Sem nenhum outro botão ou link dentro ([HDS](https://hds.hel.fi/components/linkbox)).            |
| Card selecionável | Funciona como opção de checkbox ou radio com conteúdo rico ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/card/usage)).                                                                                 | Use um `<input>` real dentro do card, com rótulo.                                                |
| Card expansível   | Mostra informação complementar sob demanda, sem mudar a largura do card ([gov.br DS](https://www.gov.br/ds/components/card)).                                                                                                   | Botão "Mostrar detalhes" com `aria-expanded` e chevron no fim; o card cresce para baixo.         |
| Card horizontal   | Mídia ao lado do texto, para textos curtos em cards largos ([DKFDS](https://designsystem.dk/komponenter/cards/)).                                                                                                               | Na classe Compacta, volta ao layout vertical.                                                    |

Cada tipo tem duas aparências: **contornado** (padrão, borda `--t-border-subtle`) e **elevado** (`.tr-card--elevated`, sombra `--e-2`, camada `--z-1`). Use a aparência elevada quando o card precisa se separar de um fundo com conteúdo.

## Boas práticas

**Um card, um assunto.** Não reúna temas diferentes no mesmo card, não junte dois cards em um e não divida um assunto em vários cards ([gov.br DS](https://www.gov.br/ds/components/card), [DKFDS](https://designsystem.dk/komponenter/cards/)).

**Mostre só o essencial e ofereça o caminho para o resto.** Título no topo, conteúdo principal no centro e ações embaixo ([gov.br DS](https://www.gov.br/ds/components/card)). O texto tem no máximo algumas frases, com poucos links ou botões ([DKFDS](https://designsystem.dk/komponenter/cards/)).

**Nunca use rolagem dentro de um card.** O card cresce com o conteúdo ([gov.br DS](https://www.gov.br/ds/components/card)). Quando cards lado a lado precisam ter a mesma altura, limite o texto com `.tr-clamp-2` ou `.tr-clamp-3` e garanta que o texto completo esteja no destino; títulos nunca são cortados.

**Esconda conteúdo com moderação.** A expansão serve a informações complementares que não precisam ficar visíveis ([gov.br DS](https://www.gov.br/ds/components/card)). O Trama não usa o verso do card (efeito de virar): o conteúdo do verso não é anunciado como relação de expansão e depende de animação. Use a expansão, que funciona com teclado, leitor de tela e movimento reduzido.

> **Divergência entre referências** O gov.br oferece dois comportamentos de conteúdo oculto: expandir e alternar para o verso do card, com efeito de giro ou de esmaecimento, e pede um identificador visível para que o verso não passe despercebido ([gov.br DS](https://www.gov.br/ds/components/card)). As demais referências não tratam do verso. Pelo critério de acessibilidade, o Trama adota só a expansão: um botão com `aria-expanded` comunica o estado a tecnologias assistivas, e o conteúdo continua na mesma ordem de leitura.

**Não misture tipos na mesma lista.** Cards de navegação e de conteúdo lado a lado confundem sobre o que é clicável ([DKFDS](https://designsystem.dk/komponenter/cards/)). Em um conjunto, todos os cards têm imagem ou nenhum tem.

**Use a grade, com largura mínima de 3 colunas.** A largura vem das colunas do layout e nunca fica abaixo de 3 colunas ([gov.br DS](https://www.gov.br/ds/components/card)). Na classe Compacta, com 4 colunas, cada card ocupa a largura toda e fica abaixo do anterior, nunca ao lado ([gov.br DS](https://www.gov.br/ds/components/card)). O espaço entre cards é o gutter da classe de janela.

**Não aninhe cards.** Para subgrupos dentro de um card, use espaço e alinhamento ([gov.br DS](https://www.gov.br/ds/components/card), [HIG](https://developer.apple.com/design/human-interface-guidelines/boxes)).

**Seja coerente com o destino.** O título e a imagem de um card de navegação correspondem ao título e à imagem principal da página de destino ([Ontario](https://designsystem.ontario.ca/components/detail/cards.html)).

**Faça** mantenha o card focado em um objeto, com título, uma linha de contexto e uma ação.

**Não faça** juntar assuntos, texto longo e muitas ações no mesmo card.

### Estados

O card tem poucos estados próprios: hover, desabilitado e arrastando. Os componentes dentro do card acompanham o estado do card ([gov.br DS](https://www.gov.br/ds/components/card)). O Trama acrescenta foco e selecionado para os tipos interativos.

| Estado       | Aparência e regra                                                                                                                                                                                                                                                                     |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Repouso      | Borda `--t-border-subtle` ou sombra `--e-2`.                                                                                                                                                                                                                                          |
| Hover        | Só em cards de navegação e selecionáveis: sombra sobe para `--e-3` em `--m-normal`.                                                                                                                                                                                                   |
| Foco         | Anel `--t-focus` de 2 px afastado 2 px no contorno, só em `:focus-visible`.                                                                                                                                                                                                           |
| Selecionado  | Borda `--t-brand` de `--stroke-thick`, fundo `--t-brand-subtle` e o controle marcado.                                                                                                                                                                                                 |
| Desabilitado | Só quando a pessoa pode habilitar o card por uma ação dela; caso contrário, retire o card. Texto e controles em `--t-fg-disabled`, `aria-disabled="true"` ([gov.br DS](https://www.gov.br/ds/components/card)) e uma frase visível dentro do card que diz o que fazer para liberá-lo. |
| Arrastando   | Em listas reordenáveis, o card arrastado usa `.tr-dragging`: opacidade `--o-xl`, sombra `--e-4` e leve rotação. Ofereça alternativa ao arrasto (veja Arrastar e soltar).                                                                                                              |
| Carregando   | Skeleton com a mesma anatomia do card final.                                                                                                                                                                                                                                          |

## Conteúdo

- O título nomeia o assunto em poucas palavras, em caixa de frase e sem ponto final. Nunca trunque o título; ele quebra linha.
- Em cards de navegação, o título costuma ser o mesmo da página de destino ([Ontario](https://designsystem.ontario.ca/components/detail/cards.html)).
- O texto diz o que a pessoa encontra ou pode fazer, em frases curtas ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/card/usage)).
- Botões usam verbo e objeto, com até duas palavras: "Ativar lembrete", "Comprar de novo".

## Acessibilidade

**Dê nome ao card.** Todo card tem um título visível ou um `aria-label` ([HDS](https://hds.hel.fi/components/card/accessibility)). Em cards de conteúdo, use `<section>` ou `<article>` com `aria-labelledby` no título.

**Deixe claro o que é interativo.** A pessoa precisa saber se o card inteiro é clicável ou só os elementos dentro dele ([gov.br DS](https://www.gov.br/ds/components/card)). Card de navegação recebe foco uma vez: marque-o como um único `<a>` ([HDS](https://hds.hel.fi/components/linkbox)). Com muito texto, deixe só o título como link e estenda a área clicável com um pseudoelemento.

**Siga uma ordem de foco lógica.** Tab e Shift+Tab percorrem todos os elementos de um card antes de passar ao próximo; Enter e Espaço acionam os controles ([gov.br DS](https://www.gov.br/ds/components/card)).

**Garanta contraste do contorno.** Quando a separação entre card e fundo comunica agrupamento importante, use borda `--t-border` ou a aparência elevada ([HDS](https://hds.hel.fi/components/card/accessibility)).

**Imagens com informação recebem texto alternativo; decorativas ficam com `alt=""`.** ([gov.br DS](https://www.gov.br/ds/components/card), [DKFDS](https://designsystem.dk/komponenter/cards/))

## Tokens usados

| Elemento                         | Token                                                                     |
|----------------------------------|---------------------------------------------------------------------------|
| Superfície                       | `--t-surface-raised`                                                      |
| Borda (contornado)               | `--t-border-subtle`, `--stroke-thin`                                      |
| Sombra e camada (elevado, hover) | `--e-2`, `--e-3`, `--z-1`                                                 |
| Raio                             | `--r-lg`                                                                  |
| Preenchimento interno            | `--sp-400`; ícones e botões só de ícone podem ficar a `--sp-200` da borda |
| Espaço entre elementos           | `--sp-300`                                                                |
| Título, sobretítulo              | Body 16/24 peso 600 `--t-fg-1`; `--t-fg-3`                                |
| Selecionado                      | `--t-brand`, `--t-brand-subtle`                                           |
| Desabilitado                     | `--t-fg-disabled`                                                         |
| Arrastando                       | `--o-xl`, `--e-4`                                                         |

## Considerações por plataforma

### Web desktop

Use de 2 a 4 cards por linha, sem passar da largura mínima de 3 colunas. O hover com sombra indica que o card de navegação é clicável.

### Web móvel

Cards ficam empilhados em uma coluna ([gov.br DS](https://www.gov.br/ds/components/card)). Cards horizontais voltam ao layout vertical, e imagens 2:1 ou 16:9 economizam altura ([DKFDS](https://designsystem.dk/komponenter/cards/)). Controles dentro do card têm alvo de `--c-touch`.

### Tablets e dobráveis

Em janelas médias, use duas colunas de cards; em expandidas, três ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)). Ao abrir o dobrável, mantenha o card que estava visível na mesma posição de leitura.

## Recursos

### Relacionados

- Listas
- Imagem
- Elevação
- Layout e grid
- Arrastar e soltar

### Referências

- [Card](https://www.gov.br/ds/components/card) gov.br DS
- [Gráfico](https://www.gov.br/ds/padroes/design/grafico) gov.br DS
- [Boxes](https://developer.apple.com/design/human-interface-guidelines/boxes) Apple HIG
- [Card](https://fluent2.microsoft.design/components/web/react/core/card/usage) Fluent 2
- [Cards](https://designsystem.dk/komponenter/cards/) DKFDS
- [Card](https://hds.hel.fi/components/card) Helsinki Design System
- [Card: accessibility](https://hds.hel.fi/components/card/accessibility) Helsinki Design System
- [Linkbox](https://hds.hel.fi/components/linkbox) Helsinki Design System
- [Cards](https://designsystem.ontario.ca/components/detail/cards.html) Ontario Design System
- [Layout design for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Entram as três áreas do card, a largura mínima de 3 colunas, a proibição de rolagem interna, o card expansível e os estados desabilitado (D9) e arrastando. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                               |
