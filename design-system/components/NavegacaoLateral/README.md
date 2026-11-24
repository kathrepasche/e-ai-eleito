# NavegacaoLateral

A navegação lateral é uma lista vertical de links, na borda inicial da tela, que leva às áreas da aplicação ou às seções de um nível da hierarquia.

A navegação lateral ocupa bastante espaço horizontal e vertical; quando o espaço é curto, uma barra de navegação mais compacta funciona melhor ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)). No gov.br, o equivalente é o menu de navegação principal, que dá acesso a todas as áreas do site ou sistema por links organizados pela arquitetura da informação ([gov.br DS](https://www.gov.br/ds/components/menu)). No Trama, o componente é o `.tr-nav`: fundo `--t-surface-1`, itens de 40px na densidade padrão e indicador de página atual em `--t-brand`. Em janelas menores, ele vira um drawer modal; veja Barra de navegação e rail.

**Quando usar.** Em aplicações com muitas áreas ou com hierarquia de dois níveis; quando a pessoa alterna entre páginas de um mesmo nível, como em painéis administrativos e documentação; e quando o número de itens deve crescer ([HDS](https://hds.hel.fi/components/side-navigation)). Também como navegação contextual dentro de uma página longa ([gov.br DS](https://www.gov.br/ds/components/menu)).

**Quando não usar.** Em soluções pequenas: o DKFDS desaconselha com menos de cinco páginas ([DKFDS](https://designsystem.dk/komponenter/venstremenu/)); use a barra de navegação. Em fluxos lineares, use o indicador de etapas. Para hierarquias com mais de dois níveis, use uma split view com uma lista intermediária ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)).

## Anatomia

1.  **Contêiner** (`nav.tr-nav`): 240px de largura, fundo `--t-surface-1`, raio `--r-lg`.
2.  **Cabeçalho** (opcional): identifica o produto e, no modo drawer, traz o botão Fechar ([gov.br DS](https://www.gov.br/ds/components/menu)).
3.  **Item de primeiro nível**: link com ícone opcional e rótulo. A área de clique cobre o item inteiro ([gov.br DS](https://www.gov.br/ds/components/menu)).
4.  **Indicador de página atual**: fundo `--t-brand-subtle`, texto em peso 600 e barra vertical de 3px em `--t-brand`.
5.  **Agrupador** (opcional): título de grupo (`.tr-nav__heading`), separador ou categoria expansível. A categoria não é link e mostra o chevron no fim do rótulo ([gov.br DS](https://www.gov.br/ds/components/menu), [Fluent](https://fluent2.microsoft.design/components/web/react/core/nav/usage)).
6.  **Item de segundo nível**: recuo maior que o primeiro nível e sem separadores entre os itens ([gov.br DS](https://www.gov.br/ds/components/menu)).
7.  **Rodapé** (opcional): links de apoio, como sites externos com `.tr-link--external` ([gov.br DS](https://www.gov.br/ds/components/menu)).

## Tipos

| Tipo                     | Uso                                                                                                                                                                                                                                                                                               |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fixa ao lado do conteúdo | Classes Expandida em diante. Desloca o conteúdo, sem sobrepor, com elevação `--e-1` e camada `--z-1` ([gov.br DS](https://www.gov.br/ds/components/menu)). O Fluent usa 260px nessa variante ([Fluent](https://fluent2.microsoft.design/components/web/react/core/nav/usage)); o Trama usa 240px. |
| Drawer modal             | Classes Compacta e Média. Abre por um botão de menu no cabeçalho, sobre o conteúdo, com véu `--t-overlay`, elevação `--e-5` e camada `--z-3`. Na Compacta ocupa a largura toda ([gov.br DS](https://www.gov.br/ds/components/menu)). Veja Drawers.                                                |
| Navegação da página      | Versão enxuta para âncoras de uma página longa, na borda final, sem subníveis e sem links para outras telas ([gov.br DS](https://www.gov.br/ds/components/menu)). Nas classes Compacta e Média vira uma barra fixa na base que abre a lista de baixo para cima.                                   |

Agrupe os itens de três formas: por rótulo, por separador ou por expansão. Na navegação da página, evite grupos; se forem necessários, use rótulo ou separador ([gov.br DS](https://www.gov.br/ds/components/menu)).

## Boas práticas

**Marque sempre onde a pessoa está.** “Onde estou?” é uma pergunta fundamental, e deixar de indicar a localização é o erro mais comum em menus de sites, porque muitas pessoas chegam por páginas internas ([gov.br DS](https://www.gov.br/ds/components/menu)). Se o subitem ativo está numa categoria recolhida, o indicador passa para a categoria ([Fluent](https://fluent2.microsoft.design/components/web/react/core/nav/usage)).

**Mostre no máximo dois níveis.** Hierarquias mais profundas pedem outra estrutura ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)).

> **Divergência entre referências** O gov.br permite subníveis dentro de subníveis, com painéis que deslizam e um item para retornar ao nível anterior ([gov.br DS](https://www.gov.br/ds/components/menu)). O DKFDS aceita até três níveis e recomenda um ou dois ([DKFDS](https://designsystem.dk/komponenter/venstremenu/)); a HIG recomenda até dois ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)); o Fluent fala em um ou dois e indica outro componente para hierarquias maiores ([Fluent](https://fluent2.microsoft.design/components/web/react/core/nav/usage)). O Trama mantém dois níveis, pela convergência das referências. Do gov.br, adota a regra de reabrir o drawer sempre no primeiro nível.

**Mantenha a navegação visível quando houver espaço.** Menus não devem ser ocultados quando há espaço para exibi-los ([gov.br DS](https://www.gov.br/ds/components/menu)). Deixe a pessoa recolher a navegação para ler melhor, mas não comece recolhida ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)). No Trama, a versão recolhida é o rail, com ícone e rótulo.

**Posicione na borda inicial e mantenha no mesmo lugar.** As pessoas procuram a navegação onde a viram em outros sites ([gov.br DS](https://www.gov.br/ds/components/menu), [HDS](https://hds.hel.fi/components/side-navigation)).

**Não repita itens entre navegações.** A navegação principal e a da página funcionam de modo independente; deixe claro o nível de cada uma ([gov.br DS](https://www.gov.br/ds/components/menu), [HDS](https://hds.hel.fi/components/side-navigation)).

**Padronize os ícones.** Use ícones em todos os itens de um bloco ou em nenhum, e só no primeiro nível ([gov.br DS](https://www.gov.br/ds/components/menu), [HDS](https://hds.hel.fi/components/side-navigation)).

**Ofereça pesquisa junto da navegação.** Dê às pessoas outra forma de chegar ao conteúdo ([gov.br DS](https://www.gov.br/ds/components/menu)). Uma pesquisa no topo pode filtrar os itens quando há muitas seções ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)).

**Evite ações críticas no pé da navegação.** O fim da lista pode ficar fora da tela ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)).

**Faça** Use rótulos de uma ou duas palavras, que comecem de forma diferente e coincidam com o título das páginas.

**Não faça** Comece vários itens com a mesma palavra, trunque os rótulos e deixe de marcar a página atual.

### Estados

Repouso, hover, foco, ativo (página atual) e expandido. Hover é a camada `--o-hover` sobre a cor do item; o ativo usa `aria-current="page"` e só um item é ativo por vez. Navegação não tem item desabilitado: se a pessoa não tem acesso a uma área, retire o item; se a área está vazia, explique dentro dela (decisão D9).

### Comportamento

**Feche o drawer de várias formas.** Pelo botão Fechar, pelo próprio acionador, com Esc e com clique fora; ofereça as duas primeiras ao mesmo tempo ([gov.br DS](https://www.gov.br/ds/components/menu)). Ao fechar, devolva o foco ao botão de menu.

**Role com a página no celular.** Em telas maiores, a navegação pode ter rolagem interna; na classe Compacta, evite rolagem interna e deixe o conteúdo do drawer rolar com o navegador ([gov.br DS](https://www.gov.br/ds/components/menu)).

**Preserve o estado.** Categorias abrem e fecham sem navegar. Ao trocar de página, a navegação fixa mantém a rolagem e as categorias abertas. Ao passar da classe Expandida para a Média, ela vira rail ou drawer, preservando o item ativo ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

## Conteúdo

Use rótulos curtos e familiares, de uma ou duas palavras, sem jargão técnico ([gov.br DS](https://www.gov.br/ds/components/menu), [HDS](https://hds.hel.fi/components/side-navigation)), e evite começar vários itens pela mesma palavra. O rótulo coincide com o título da página de destino ([DKFDS](https://designsystem.dk/komponenter/venstremenu/)). Use caixa de frase.

**Nunca trunque um item.** Prefira um sinônimo mais curto ([gov.br DS](https://www.gov.br/ds/components/menu)); se o rótulo ainda não couber, ele quebra a linha, que é o comportamento padrão do Fluent ([Fluent](https://fluent2.microsoft.design/components/web/react/core/nav/usage)).

> **Divergência entre referências** O Fluent admite truncar rótulos com tooltip ao lado do item ([Fluent](https://fluent2.microsoft.design/components/web/react/core/nav/usage)), e a versão 1.0 do Trama seguia essa opção. O gov.br pede textos curtos que não quebrem a linha ([gov.br DS](https://www.gov.br/ds/components/menu)). Pela decisão D15, o Trama nunca trunca itens de navegação: o texto completo continua legível com zoom e tradução, que é a opção com mais margem de acessibilidade.

## Acessibilidade

**Use `<nav>` com lista e nome próprio.** Estruture os itens em `ul` e `li` ([gov.br DS](https://www.gov.br/ds/components/menu)). Se há mais de uma navegação na página, cada uma tem um `aria-label` distinto, como “Navegação” e “Nesta página” ([HDS](https://hds.hel.fi/components/side-navigation/accessibility)).

**Marque a página atual com `aria-current="page"`.** O destaque visual não chega ao leitor de tela.

**Teclado no drawer.** Enter ou Espaço no acionador abre; ao abrir, o foco vai para o botão Fechar, se houver, para a pessoa poder desistir; Tab e Shift+Tab percorrem os itens; Esc fecha ([gov.br DS](https://www.gov.br/ds/components/menu)). O foco fica preso no drawer enquanto ele estiver aberto.

**Categorias usam `aria-expanded`.** O botão da categoria informa se está aberta; o chevron fica no fim e aponta para baixo quando fechada e para cima quando aberta (decisão D8).

**Pense na ordem.** Itens muito usados no fim custam caro para quem usa teclado ([HDS](https://hds.hel.fi/components/side-navigation/accessibility)). Ofereça “Pular para o conteúdo” antes da navegação.

## Tokens usados

| Token                                 | Uso                                          |
|---------------------------------------|----------------------------------------------|
| `--t-surface-1`                       | Fundo da navegação                           |
| `--o-hover`                           | Camada de hover do item                      |
| `--t-brand-subtle`, `--t-brand`       | Fundo e barra do item atual                  |
| `--t-fg-1`, `--t-fg-2`, `--t-fg-3`    | Item atual, item comum, título de grupo      |
| `--d-control`, `--sp-200`, `--sp-300` | Altura do item por densidade; espaço interno |
| `--e-1`, `--z-1`                      | Navegação fixa                               |
| `--e-5`, `--z-3`, `--t-overlay`       | Drawer modal e véu                           |

## Considerações por plataforma

### Web desktop

Nas classes Expandida, Grande e Extragrande, mantenha a navegação fixa junto ao conteúdo ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)), com a navegação da página na borda final quando houver. Densidade padrão; alta só em ferramentas com muitos itens.

### Web móvel

Na classe Compacta, a navegação vira drawer modal em largura total, aberto por um botão de menu bem destacado no cabeçalho ([gov.br DS](https://www.gov.br/ds/components/menu), [gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)), combinado com a barra inferior para as áreas principais ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Use densidade baixa.

### Tablets e dobráveis

Na classe Média, use o rail com drawer modal para os itens extras; na Expandida, a navegação pode ficar fixa ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Ao abrir o dobrável, mantenha o item ativo e a posição de rolagem ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Estruturar a navegação
- Barra de navegação e rail
- Drawers e folhas laterais
- Painéis e split view
- Breadcrumb

### Referências

- [Menu de Navegação](https://www.gov.br/ds/components/menu) gov.br DS
- [Navegação](https://www.gov.br/ds/padroes/design/navegacao) gov.br DS
- [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) Apple HIG
- [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields) Apple HIG
- [Nav: usage](https://fluent2.microsoft.design/components/web/react/core/nav/usage) Fluent 2
- [Venstremenu](https://designsystem.dk/komponenter/venstremenu/) DKFDS
- [SideNavigation](https://hds.hel.fi/components/side-navigation) Helsinki Design System
- [SideNavigation: accessibility](https://hds.hel.fi/components/side-navigation/accessibility) Helsinki Design System
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Layout design for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                       |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta cabeçalho, rodapé, formas de agrupar, navegação da página, regras do drawer (fechamento, foco inicial, rolagem no celular) e camadas; troca o truncamento com tooltip pela quebra de linha (D15). |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                |
