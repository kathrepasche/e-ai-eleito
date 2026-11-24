# PaineisESplitView

Um split view divide a janela em painéis adjacentes, em geral uma lista e o detalhe do item selecionado, para mostrar vários níveis da hierarquia ao mesmo tempo.

Ao selecionar um item no painel principal, o conteúdo dele aparece no painel secundário; um terceiro painel pode mostrar o conteúdo de um item do segundo ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)). Com a navegação achatada assim, a pessoa chega ao conteúdo sem transições de tela inteira ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

O Trama define o comportamento dos painéis pelas classes de janela, nunca pelo tipo de aparelho: uma janela de navegador estreita no desktop e um tablet em retrato caem na mesma classe ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). A mesma estrutura de lista e detalhe vira uma pilha de telas na classe Compacta e dois ou três painéis lado a lado em janelas maiores. Split views são ferramentas de sistema e usam largura fluida, que aproveita todo o espaço da janela ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

## Quando usar

- Para listas com detalhe: caixa de entrada e mensagem, pedidos e pedido, contatos e contato.
- Para navegar por hierarquias de dois ou três níveis, com uma lista de conteúdo entre a navegação e o detalhe ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)).
- Para painéis de apoio ao redor de uma área de edição, como um inspetor de propriedades ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)).
- Para filtrar: categorias no primeiro painel, resultados no segundo ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)).

## Quando não usar

- **Em janelas compactas.** Abaixo de 600 px use um painel por vez; dois painéis ficariam truncados e difíceis de usar ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)).
- **Para uma tarefa curta que interrompe a principal.** Use um popover, um diálogo ou um drawer, que aparecem sobre a tela anterior sem que a pessoa perca o contexto ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)).
- **Para conteúdo sem relação entre os painéis.** Painéis só fazem sentido quando a seleção em um determina o conteúdo do outro, ou quando o painel de apoio age sobre o principal.

## Anatomia

1.  **Painel principal.** Lista ou navegação no lado inicial.
2.  **Painel secundário.** Detalhe do item selecionado, com título próprio.
3.  **Painel terciário (opcional).** Detalhe de um item do secundário, ou inspetor.
4.  **Divisor.** Linha fina vertical entre painéis; pode ser arrastável.
5.  **Controle de recolher (opcional).** Botão que esconde e mostra um painel.
6.  **Barra de ações do painel (opcional).** Ações sobre o conteúdo do painel, alinhadas ao fim, com a ação principal por último (à direita). Empilhadas na classe Compacta, a principal fica em cima.

## Tipos

| Configuração       | Classe                 | Quando                                                                                                                                                                                      |
|--------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Um painel          | pilha de telas         | Janela compacta (abaixo de 600 px).                                                                                                                                                         |
| Dois painéis 42:58 | `.tr-panes` ajustado   | 600 a 959 px ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).                                                                                          |
| Dois painéis 38:62 | `.tr-panes`            | 960 px ou mais ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).                                                                                        |
| Dois painéis 50:50 | `.tr-panes--50`        | Dobrável aberto, com a dobra entre os painéis ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).                                                         |
| Três painéis       | `.tr-panes--3`         | Janela grande (1200 px ou mais), como tablets em paisagem ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).                                             |
| Pilha de painéis   | pilha com botão Voltar | Dentro de um popover ou drawer estreito, cada nível empilha sobre o anterior com um cabeçalho e botão para voltar ([Blueprint](https://blueprintjs.com/docs/#core/components/panel-stack)). |

Na janela média (600 a 839 px), um painel é o recomendado e dois são possíveis; da expandida em diante, dois são o recomendado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

## Boas práticas

**Destaque o item atual em todos os painéis que levam ao detalhe.** O destaque persistente mostra a relação entre os painéis e ajuda a pessoa a se orientar ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)). Escolher um item da lista abre o detalhe na hora, o que é navegação: marque-o com `aria-current` e `--t-brand-subtle`. Reserve `aria-selected` para quando a lista também permite marcar vários itens para uma ação posterior; os dois estados podem coexistir e são visualmente distintos.

**Projete para várias larguras.** Janelas de navegador mudam de tamanho a qualquer momento. Garanta que a navegação entre painéis faça sentido em larguras estreitas, intermediárias e largas ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)). Ao passar para um painel, mostre o detalhe do item selecionado e um botão Voltar para a lista.

**Mostre conteúdo no detalhe desde o início.** Ao abrir a página em janela larga, abra o item mais relevante ou mostre um estado vazio que explica o que escolher. O estado vazio aparece no lugar onde o dado deveria estar, dentro do próprio painel, com texto alinhado ao início em painéis estreitos ([gov.br DS](https://www.gov.br/ds/padroes/design/emptystates)). Nunca deixe o painel secundário em branco.

**Defina limites de tamanho.** Se os painéis forem redimensionáveis, use mínimo e máximo que mantenham o divisor visível e o conteúdo legível ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)). O painel de lista não fica abaixo de 240 px.

**Permita esconder painéis de apoio.** Em áreas de edição, deixe a pessoa recolher painéis para ganhar espaço, e ofereça mais de uma forma de reabri-los, como botão na barra e atalho de teclado ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)). Não esconda a navegação por padrão ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)).

**Use o divisor fino.** Uma linha de 1 px em `--t-border-subtle` dá o máximo de espaço ao conteúdo ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)). A área de arrasto pode ser mais larga que a linha.

**Considere arrastar entre painéis.** Mover um item para outra pasta arrastando-o de um painel a outro é natural em split views ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)). Ofereça sempre uma alternativa por menu (veja Arrastar e soltar).

**Mantenha a mesma densidade nos painéis vizinhos.** Componentes semelhantes lado a lado usam a mesma densidade ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). A densidade alta é permitida em painéis de ferramentas com apontador fino; no toque, todos os painéis usam a baixa.

**Não estique o conteúdo.** Em telas largas, um único painel esticado é difícil de ler e desperdiça espaço; use mais painéis ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

**Faça** mantenha o item selecionado destacado e o título do detalhe igual ao item.

**Não faça** deixar o detalhe vazio e a lista sem indicação do item atual.

### Comportamento entre classes de janela

| Transição            | Comportamento                                                                                                                                           |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dois painéis para um | Se havia item selecionado, mostre o detalhe com botão Voltar; caso contrário, mostre a lista.                                                           |
| Um painel para dois  | Mostre a lista à esquerda e o item que estava aberto à direita.                                                                                         |
| Em todas             | Preserve seleção, rolagem, texto digitado e foco ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). |

## Conteúdo

- Dê um título ao painel de detalhe igual ao nome do item selecionado.
- Use um título único para a página acima dos painéis; não é preciso nomear cada painel visualmente quando a relação de lista e detalhe é óbvia ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)).
- Rotule o controle de recolher com a ação e o painel: "Recolher lista", "Mostrar lista".

## Acessibilidade

**Use marcos para os painéis.** O painel de navegação é um `<nav>` com `aria-label`; o de detalhe é uma `<section>` ou `<main>` com `aria-labelledby` no título.

**Gerencie o foco ao abrir um item.** Em dois painéis, abrir um item atualiza o detalhe sem mover o foco; ofereça um atalho para pular ao detalhe e anuncie o título do detalhe em região viva educada. Em um painel, o detalhe é uma etapa nova: leve o foco ao título dele e, ao voltar, devolva o foco ao item da lista.

**Divisor redimensionável é um controle.** Use `role="separator"` com `aria-orientation="vertical"`, `aria-valuenow`, `aria-valuemin`, `aria-valuemax` e foco por teclado; as setas ajustam a largura. Ofereça também um botão para recolher, porque arrastar não pode ser a única forma (WCAG 2.2, 2.5.7).

**Mantenha a ordem do DOM igual à visual.** Lista antes do detalhe, para que a ordem de foco siga a leitura (WCAG 2.2, 2.4.3).

## Tokens usados

| Elemento                                                | Token                                               |
|---------------------------------------------------------|-----------------------------------------------------|
| Superfície dos painéis                                  | `--t-surface-raised` ou `--t-bg`                    |
| Painel de navegação                                     | `--t-surface-1`                                     |
| Divisor                                                 | `--t-border-subtle`, `--stroke-thin`                |
| Item selecionado                                        | `--t-brand-subtle`                                  |
| Preenchimento dos painéis                               | `--sp-400`                                          |
| Margens da página                                       | 16, 24, 32, 40 ou 48 px conforme a classe de janela |
| Camada de um painel sobreposto (drawer em janela média) | `--z-3`, `--e-5`                                    |
| Recolher e expandir                                     | `--m-slow`, `--m-ease-standard`                     |
| Divisor em foco                                         | `--t-focus`, `--stroke-thick`                       |

## Considerações por plataforma

### Web desktop

Permita redimensionar e recolher painéis, com atalho de teclado para mostrar e esconder a navegação. Em janelas grandes, até três painéis. Ao reduzir a janela, recolha a navegação automaticamente antes de cortar o detalhe ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)).

### Web móvel

Um painel por vez, sempre em largura fluida, com transição de pilha: a lista leva ao detalhe e o botão Voltar e o gesto de voltar do navegador retornam. Atualize o endereço a cada nível, para que o voltar do navegador funcione.

### Tablets e dobráveis

Use a proporção 42:58 entre 600 e 959 px, 38:62 a partir de 960 px e 50:50 em dobráveis abertos ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Em Z Fold em retrato, combine dois painéis com o rail de navegação; em tablets em paisagem, use três painéis ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Mantenha menu e conteúdo visíveis juntos ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)). Não coloque elementos interativos perto da dobra ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Veja também Postura e dobra.

## Recursos

### Relacionados

- Projetar para tablets e dobráveis
- Layout e grid
- Navegação lateral
- Listas
- Multitarefa e janelas
- Postura e dobra

### Referências

- [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views) Apple HIG
- [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) Apple HIG
- [Column views](https://developer.apple.com/design/human-interface-guidelines/column-views) Apple HIG
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Layout design for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI
- [Panel stack](https://blueprintjs.com/docs/#core/components/panel-stack) Blueprint
- [Grid](https://www.gov.br/ds/fundamentos-visuais/grid) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Empty States](https://www.gov.br/ds/padroes/design/emptystates) gov.br DS

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                                        |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Entram a largura fluida (D18), a barra de ações do painel com a principal no fim (D4), a distinção entre item atual e selecionado (D10), o foco ao abrir o detalhe (D13), a densidade entre painéis (D11) e o estado vazio no próprio painel. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                                 |
