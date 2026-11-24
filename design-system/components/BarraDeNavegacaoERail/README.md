# BarraDeNavegacaoERail

A barra de navegação e o rail levam às seções de primeiro nível da aplicação e mudam de forma conforme a classe de janela.

A barra de navegação ajuda a entender que tipos de informação a aplicação oferece e permite trocar de seção mantendo o estado de navegação dentro de cada uma ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)). O Trama tem três formas do mesmo destino de navegação: a **barra inferior** (`.tr-bottom-nav`), o **rail** (`.tr-rail`) e a navegação lateral (`.tr-nav`). Em sites de serviço, há também a **barra superior**, com o nome do serviço e links para as seções. O gov.br não tem barra inferior nem rail; dele vêm as regras de navegação lateral entre níveis irmãos: os componentes que levam aos níveis principais ficam sempre visíveis, com poucos itens ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)).

**Quando usar.** Em aplicações que as pessoas usam com frequência, com várias tarefas e sem uma ordem fixa entre elas ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)), para dar acesso permanente a três a cinco seções principais.

**Quando não usar.** Para executar ações sobre o conteúdo, use a barra de ferramentas ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)). Para alternar entre vistas da mesma página, use abas ([DKFDS](https://designsystem.dk/komponenter/header/)). Para serviços com uma jornada clara de começo ao fim, simplifique a jornada e use uma lista de tarefas ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)).

## Anatomia

1.  **Contêiner**: `<nav>` com nome. A barra inferior tem 64px de altura, borda superior `--t-border-subtle` e camada `--z-3`, porque fica fixa sobre o conteúdo; o rail tem 80px de largura e fundo `--t-surface-1`.
2.  **Destino**: ícone e rótulo, empilhados.
3.  **Indicador de seleção**: na barra inferior, ícone e rótulo em `--t-brand`; no rail, cápsula `--t-brand-subtle` atrás do ícone.
4.  **Badge** (opcional): número ou ponto sobre o ícone para informação crítica. Veja Badges.
5.  **Botão de menu** (opcional): botão circular que abre o drawer modal com destinos extras. Na classe Compacta, dê a ele ênfase visual suficiente para a pessoa saber onde está a navegação completa ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)).

## Tipos

O Trama escolhe a forma pela classe de janela, como recomenda o One UI: barra de navegação na base em telas pequenas, rail na lateral em telas médias e drawer de navegação completo em telas grandes ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

| Classe de janela              | Forma                            | Destinos extras      |
|-------------------------------|----------------------------------|----------------------|
| Compacta (\< 600)             | Barra inferior `.tr-bottom-nav`  | Drawer modal         |
| Média (600 a 839)             | Rail `.tr-rail`                  | Drawer modal         |
| Expandida (840 a 1199)        | Rail ou navegação lateral fixa   | Drawer modal ou fixo |
| Grande e Extragrande (≥ 1200) | Navegação lateral fixa `.tr-nav` | Na própria navegação |

**Barra superior de serviço.** Em sites de serviço público e portais, a barra superior mostra o nome do serviço como link para a página inicial, os links das seções principais e ferramentas do serviço, como a pesquisa ([GOV.UK](https://design-system.service.gov.uk/components/service-navigation/)). Ela fica abaixo do cabeçalho geral e acima de elementos da página, como o breadcrumb: do mais geral para o mais específico ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)). Em telas estreitas, os links dela se recolhem num menu ([DKFDS](https://designsystem.dk/komponenter/header/), [HDS](https://hds.hel.fi/components/header)).

## Boas práticas

**Use a barra para navegar.** Ações sobre o conteúdo vão para a barra de ferramentas ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)).

**Mantenha a barra visível em todas as seções.** Se ela some, a pessoa esquece em que área está. A exceção é uma vista modal que cobre a barra ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)). O gov.br pede o mesmo para os componentes que levam aos níveis principais ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)).

**Tenha de três a cinco destinos na barra inferior.** O One UI recomenda menos de quatro abas na base da tela e, se necessário, no máximo cinco ([One UI](https://developer.samsung.com/one-ui/comp/bottom-navigation.html)). Para destinos extras, use o drawer; a HIG desaconselha abas de excedente “Mais”, porque escondem conteúdo ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)).

**Liste só as seções mais importantes.** Evite menus com muitos itens e ofereça o que realmente importa ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). Os links levam às seções de primeiro nível mais úteis, sem tentar listar todas as páginas do serviço ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)). Links para fora do serviço ficam agrupados depois dos internos, ou no corpo da página, com `.tr-link--external`.

**Não desabilite nem esconda destinos dinamicamente.** Destinos que aparecem e somem deixam a interface instável. Se uma seção está vazia, explique por quê dentro dela ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)). Veja Estados vazios.

**Reserve badges para informação crítica.** O excesso dilui o significado ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)).

**Preserve o estado de cada seção.** Ao voltar a uma seção, a pessoa encontra a rolagem e a vista em que estava ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)).

**Faça** Use poucos destinos, cada um com ícone e um rótulo de uma palavra.

**Não faça** Use só ícones, ultrapasse cinco destinos e esconda seções num item “Mais”.

### Comportamento

Tocar no destino atual leva ao topo da seção. A troca de forma entre barra, rail e navegação lateral acontece na mudança de classe de janela, sem animação de deslocamento do conteúdo e mantendo o destino ativo. No One UI, não se troca de aba deslizando o dedo na barra inferior ([One UI](https://developer.samsung.com/one-ui/comp/bottom-navigation.html)); o Trama segue essa regra, para não conflitar com a rolagem horizontal do conteúdo. Uma barra superior fixa ao topo da janela cobre o conteúdo se a página não reservar um espaço igual à altura dela ([Blueprint](https://blueprintjs.com/docs/#core/components/navbar)). Os menus suspensos da barra superior abrem só com clique ([HDS](https://hds.hel.fi/components/header/accessibility)).

## Conteúdo

> **Divergência entre referências** O gov.br prefere iniciais maiúsculas em todas as palavras de componentes de navegação, exceto artigos e preposições ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Fluent, GOV.UK e DKFDS usam caixa de frase. Pela decisão D1, o Trama usa caixa de frase: “Meus pedidos”, não “Meus Pedidos”.

Inclua rótulo em todos os destinos e use uma palavra sempre que possível ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)). Nunca trunque um rótulo: escolha um sinônimo mais curto ([gov.br DS](https://www.gov.br/ds/components/menu)) e, se ainda assim não couber, deixe quebrar em duas linhas (decisão D15). Na barra superior, prefira rótulos de uma ou duas palavras e evite começar vários com a mesma palavra ([HDS](https://hds.hel.fi/components/header)). Use substantivos que nomeiam a seção, como “Pedidos” ou “Agenda”, em caixa de frase. Quando há barra de navegação, o título no topo da tela pode ser omitido; o nome da seção principal pode servir de título ([One UI](https://developer.samsung.com/one-ui/comp/bottom-navigation.html)).

## Acessibilidade

**Use `<nav>` com nome e links.** Cada destino é um `<a href>`; o atual leva `aria-current="page"`. Não use o padrão de abas (`role="tablist"`), porque cada destino muda a página.

**Não dependa só da cor para o estado atual.** Na barra inferior, o destino atual muda a cor do ícone e do rótulo; combine com peso de fonte ou com o fundo do ícone, como no rail (WCAG 2.2, 1.4.1).

**Pense na ordem do teclado.** Itens de uso frequente não ficam no fim ([HDS](https://hds.hel.fi/components/header/accessibility)). Na barra superior, ofereça “Pular para o conteúdo” antes dos links.

**Garanta alvos de toque.** Cada destino tem no mínimo `--c-touch` de altura e largura.

**Estados.** Hover é a camada `--o-hover`; o foco aparece só em `:focus-visible`; só um destino é atual por vez.

**Anuncie badges.** Inclua o valor no nome acessível, como “Pedidos, 3 novos”.

## Tokens usados

| Token                                     | Uso                                 |
|-------------------------------------------|-------------------------------------|
| `--t-surface-raised`, `--t-border-subtle` | Fundo e borda da barra inferior     |
| `--t-surface-1`                           | Fundo do rail                       |
| `--t-brand`                               | Destino atual na barra inferior     |
| `--t-brand-subtle`                        | Cápsula do destino atual no rail    |
| `--t-fg-1`, `--t-fg-2`                    | Rótulo atual e comum                |
| `--r-pill`, `--r-lg`                      | Cápsula do ícone; contêiner do rail |
| `--t-danger`                              | Badge de contagem                   |

## Considerações por plataforma

### Web desktop

Nas classes Grande e Extragrande, use a navegação lateral fixa, com a barra superior de serviço quando o produto for um site público. Mantenha a navegação visível junto ao conteúdo ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)).

### Web móvel

Na classe Compacta, use a barra inferior com três a cinco destinos e o drawer modal para o resto ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Reserve a área segura da base da tela. A barra superior de serviço recolhe os links num botão de menu. O DKFDS faz essa troca abaixo de 992px ([DKFDS](https://designsystem.dk/komponenter/header/)), e o HDS a partir de 768px para baixo ([HDS](https://hds.hel.fi/components/header)); o Trama faz a troca na classe Compacta.

### Tablets e dobráveis

Use o rail em dobráveis do tipo Z Fold na vertical ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Num tablet na horizontal, a classe costuma ser Expandida ou Grande, com navegação lateral fixa. Ao abrir ou fechar o dobrável, a forma muda e o destino ativo, a rolagem e o texto digitado permanecem ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Estruturar a navegação
- Navegação lateral
- Abas
- Drawers e folhas laterais
- Projetar para tablets e dobráveis
- Layout e grid

### Referências

- [Navegação](https://www.gov.br/ds/padroes/design/navegacao) gov.br DS
- [Menu de Navegação](https://www.gov.br/ds/components/menu) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) Apple HIG
- [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) Apple HIG
- [Service navigation](https://design-system.service.gov.uk/components/service-navigation/) GOV.UK Design System
- [Navigate a service](https://design-system.service.gov.uk/patterns/navigate-a-service/) GOV.UK Design System
- [Header](https://designsystem.dk/komponenter/header/) DKFDS
- [Header](https://hds.hel.fi/components/header) Helsinki Design System
- [Header: accessibility](https://hds.hel.fi/components/header/accessibility) Helsinki Design System
- [Navbar](https://blueprintjs.com/docs/#core/components/navbar) Blueprint
- [Bottom navigation](https://developer.samsung.com/one-ui/comp/bottom-navigation.html) Samsung One UI
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Layout design for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta as regras de navegação lateral do gov.br, a ênfase do botão de menu no celular, a camada da barra fixa, a caixa de frase D1 e a proibição de truncar rótulos (D15). |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                  |
