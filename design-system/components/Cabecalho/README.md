# Cabecalho

O cabeçalho identifica o produto no topo de todas as páginas e reúne a navegação principal, a pesquisa e o acesso à conta.

O cabeçalho é a primeira área que a pessoa vê e a referência que se repete em todas as etapas e subpáginas ([DKFDS](https://designsystem.dk/komponenter/header/)). Ele agrupa a identificação do produto, a navegação, as funcionalidades e o suporte ([gov.br](https://www.gov.br/ds/components/header)). No Trama, o componente é o `.tr-header`, com uma linha superior (`__top`) e uma linha opcional de navegação (`__nav`).

**Quando usar.** Em todas as páginas do produto, no topo, acima do conteúdo principal ([HDS](https://hds.hel.fi/components/header), [GOV.UK](https://design-system.service.gov.uk/components/header/)). Em páginas de erro, use a versão simplificada descrita em Modelos de página.

**Quando não usar.** Não repita o cabeçalho no meio da página ([DKFDS](https://designsystem.dk/komponenter/header/)). Para alternar entre visões do mesmo conteúdo, use abas; a navegação do cabeçalho leva a outras seções ([DKFDS](https://designsystem.dk/komponenter/header/)). Em fluxos lineares, com uma ordem clara de tarefas, evite links de navegação no cabeçalho e use uma lista de tarefas ou o indicador de etapas ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)).

## Anatomia

1.  **Superfície**: ocupa a largura total da janela, mesmo quando o conteúdo tem largura fixa ([gov.br](https://www.gov.br/ds/components/header)). Fundo `--t-surface-raised`, borda inferior `--t-border-subtle` e sombra `--e-1`, na camada `--z-1`.
2.  **Logo** (opcional): `.tr-header__logo`, link para a página inicial da organização.
3.  **Separador** (condicional): `.tr-header__sep`, sempre que outro elemento fica ao lado do logo ([gov.br](https://www.gov.br/ds/components/header)).
4.  **Título** (obrigatório): nome do produto, link para a página inicial do produto. É o único elemento obrigatório ([gov.br](https://www.gov.br/ds/components/header)).
5.  **Subtítulo** (opcional): categoria ou órgão responsável, logo abaixo do título.
6.  **Ações** (opcional): `.tr-header__actions`, com pesquisa, funcionalidades, idioma, Entrar ou avatar, nesta ordem.
7.  **Navegação** (opcional): `.tr-header__nav`, com as seções de primeiro nível.

## Tipos

| Tipo              | Uso                                                                                                                                                                    |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Padrão            | Portais e sites informativos, quando a marca precisa de destaque e há mais informação para mostrar ([gov.br](https://www.gov.br/ds/components/header)).                |
| Compacto          | Sistemas e ferramentas, quando o conteúdo precisa de mais espaço vertical ([gov.br](https://www.gov.br/ds/components/header)). Use `data-density="alta"` no cabeçalho. |
| Fixo simplificado | `.tr-header--sticky`: fica preso ao topo durante a rolagem, com conteúdo reduzido. Veja Comportamento.                                                                 |
| Mínimo            | Só logo e título, para páginas de erro e para o início de fluxos de autenticação.                                                                                      |

## Boas práticas

**Mostre só o essencial.** Um cabeçalho com muitas funcionalidades fica difícil de percorrer com o teclado; priorize as essenciais ([gov.br](https://www.gov.br/ds/components/header), [HDS](https://hds.hel.fi/components/header/accessibility)). Agrupe as ações por função e use no máximo três grupos ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)).

**Mantenha a ordem dos elementos em todas as páginas.** Link de pular, logo e título, ações e navegação, sempre nessa ordem. Dentro das ações, idioma, pesquisa e entrar não mudam de posição sem um bom motivo ([HDS](https://hds.hel.fi/components/header)). Comece pelos elementos mais gerais e termine nos mais específicos do serviço ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)).

**Escreva um título que caiba em até duas linhas.** O título cresce para duas linhas e a altura do cabeçalho acompanha ([gov.br](https://www.gov.br/ds/components/header)). O HDS recomenda no máximo 22 caracteres, contando espaços ([HDS](https://hds.hel.fi/components/header)). Não trunque o título: se ele passar de duas linhas, reescreva-o (D15).

**Use a navegação para as seções mais importantes.** A navegação do cabeçalho mostra as seções de primeiro nível mais úteis e não precisa listar todas as páginas: ela não é um mapa do site ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)). Links para fora do produto ficam agrupados depois dos internos e levam o ícone de link externo (D14).

**Troque Entrar pelo avatar depois da autenticação.** O botão Entrar aparece só para quem não entrou; depois, o avatar o substitui e abre um menu com as opções da conta, com Sair por último ([gov.br](https://www.gov.br/ds/components/header), [HDS](https://hds.hel.fi/components/header)). Veja Contas e autenticação.

**Use rótulo de texto nas funcionalidades.** Botões só com ícone ficam restritos a convenções universais, como pesquisar e menu, sempre com nome acessível. Em telas de toque não há tooltip por hover, então prefira ícones de sentido imediato ou texto ([gov.br](https://www.gov.br/ds/components/header)). Se um item tem ícone, todos os itens do grupo têm ícone ([HDS](https://hds.hel.fi/components/header)).

**Leve o excedente para um menu.** Quando links ou funcionalidades não cabem na largura, reúna-os num menu "Mais" ([gov.br](https://www.gov.br/ds/components/header), [DKFDS](https://designsystem.dk/komponenter/header/)). Defina antes quais itens saem primeiro ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)).

> **Divergência entre referências** O GOV.UK tirou o nome do serviço e a navegação do cabeçalho e os levou para um componente separado, a navegação do serviço ([GOV.UK](https://design-system.service.gov.uk/components/service-navigation/)). O gov.br, o DKFDS e o HDS mantêm título e navegação dentro do cabeçalho. O Trama segue a maioria (critério 4): título e navegação ficam no `.tr-header`, em linhas distintas. O gov.br também trunca títulos com mais de duas linhas e usa título em caixa alta na especificação; o Trama não trunca títulos (D15) e usa caixa de frase (D1, D16).

**Faça** um título curto em caixa de frase e poucas ações, cada uma com nome claro.

**Não faça** título em caixa alta truncado e uma fileira de ícones sem rótulo.

### Comportamento

**Pesquisa expansível em telas estreitas.** Na classe Expandida e maiores, o cabeçalho padrão mostra o campo de pesquisa aberto. Nas classes Compacta e Média, e no cabeçalho fixo, mostre só o botão Pesquisar. Ao acioná-lo, os outros elementos do cabeçalho somem, o campo ocupa toda a largura e recebe o foco, e um botão circular Fechar aparece; Fechar devolve o cabeçalho ao estado anterior ([gov.br](https://www.gov.br/ds/components/header)). Ao fechar, devolva o foco ao botão Pesquisar. Se a pesquisa cobre só o produto, diga isso no rótulo, como "Pesquisar em Licenças e alvarás" ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)).

**Versão fixa simplificada.** Se o cabeçalho acompanha a rolagem, ele sobe para a camada `--z-3` e usa a sombra `--e-3`, mais pronunciada ([gov.br](https://www.gov.br/ds/components/header); D26). Nessa versão, mostre só o estritamente necessário: logo, título sem subtítulo, botão Pesquisar e Entrar ou avatar. O gov.br fixa o cabeçalho quando a pessoa rola a página para cima e o devolve ao estado normal ao chegar ao topo ([gov.br](https://www.gov.br/ds/components/header)). O cabeçalho compacto já é enxuto e não muda de formato quando fica fixo.

**Menus abrem por clique.** Submenus da navegação e o menu do avatar abrem com clique, toque ou teclado, nunca por hover, que é difícil para pessoas com limitações motoras ou visuais ([HDS](https://hds.hel.fi/components/header/accessibility)). Fecham com um segundo clique no mesmo botão, com clique fora ou com Esc ([gov.br](https://www.gov.br/ds/components/header)). Na classe Compacta, a lista ocupa toda a largura e flutua sobre o conteúdo.

**Densidades.** O cabeçalho aceita os três níveis de densidade, que mudam o espaçamento vertical da superfície: alta para ocupar menos espaço, padrão para a maioria dos layouts e baixa quando o cabeçalho precisa de destaque ([gov.br](https://www.gov.br/ds/components/header)). Aplique com `data-density` no `.tr-header`. Na classe Compacta e em toque, use a densidade padrão ou baixa, para que cada ação tenha `--c-touch` (D11).

## Conteúdo

Use o nome do produto no título. A página atual fica no H1. Em celulares, o gov.br permite que o título indique a página atual ([gov.br](https://www.gov.br/ds/components/header)); o Trama mantém o nome do produto e deixa a página atual para o H1. Rótulos de navegação têm uma ou duas palavras e não começam todos pela mesma palavra ([HDS](https://hds.hel.fi/components/header)). Use o vocabulário controlado: "Pesquisar", "Entrar" e "Sair" (D7).

## Acessibilidade

**Use o elemento `<header>`.** Filho direto do `<body>`, ele vira o landmark `banner` ([gov.br](https://www.gov.br/ds/components/header)). A navegação usa `<nav aria-label="Principal">` e a pesquisa usa `role="search"` ([HDS](https://hds.hel.fi/components/header/accessibility)). Não crie outros landmarks dentro do cabeçalho sem necessidade: o excesso gera ruído para leitores de tela ([HDS](https://hds.hel.fi/components/header/accessibility)).

**Marque a página atual.** Use `aria-current="page"` no link da página atual. Numa subpágina cuja seção continua destacada no cabeçalho, use `aria-current="true"` ([DKFDS](https://designsystem.dk/komponenter/header/)).

**Descreva cada botão que abre algo.** Botões de menu e de pesquisa levam `aria-expanded` e `aria-controls`, gerados pelo script ([DKFDS](https://designsystem.dk/komponenter/header/); veja JavaScript). O logo tem nome acessível que diz o destino. Teste a navegação só com teclado: Tab e Shift+Tab percorrem, Enter e Espaço acionam, e a ordem segue a ordem visual ([gov.br](https://www.gov.br/ds/components/header)).

**O cabeçalho fixo não pode cobrir o foco.** Reserve espaço com `scroll-padding-top` para que o elemento focado nunca fique escondido atrás dele (WCAG 2.2, 2.4.11).

## Tokens usados

| Token                              | Uso                                                   |
|------------------------------------|-------------------------------------------------------|
| `--t-surface-raised`               | Superfície                                            |
| `--t-border-subtle`                | Borda inferior e divisão da linha de navegação        |
| `--e-1` / `--e-3`                  | Sombra do cabeçalho normal e do fixo                  |
| `--z-1` / `--z-3`                  | Camada do cabeçalho normal e do fixo                  |
| `--t-brand`                        | Indicador da página atual na navegação                |
| `--t-fg-1`, `--t-fg-2`, `--t-fg-3` | Título, links de navegação e subtítulo                |
| `--sp-200`, `--sp-300`, `--sp-400` | Espaçamentos internos e entre elementos               |
| `--c-touch`                        | Altura dos links de navegação e área mínima das ações |

## Considerações por plataforma

### Web desktop

Use o cabeçalho padrão em portais e o compacto em sistemas. Com largura fixa, o conteúdo do cabeçalho se alinha ao contêiner da página e a superfície continua de ponta a ponta (D18).

### Web móvel

Na classe Compacta, oculte o subtítulo ([gov.br](https://www.gov.br/ds/components/header)), leve a navegação para um botão Menu e mostre a pesquisa como botão expansível. O DKFDS e o HDS fazem essa troca só quando o conteúdo deixa de caber ([DKFDS](https://designsystem.dk/komponenter/header/), [HDS](https://hds.hel.fi/components/header)). Mantenha no máximo dois itens fixos à direita, como pesquisa e conta, para não sobrecarregar o menu ([HDS](https://hds.hel.fi/components/header)).

### Tablets e dobráveis

Na classe Média, use o mesmo comportamento da Compacta para pesquisa e navegação. Ao abrir o dobrável e passar para a Expandida, mostre a navegação e o campo de pesquisa abertos. Ao mudar de classe, preserve o termo digitado na pesquisa.

## Recursos

### Relacionados

- Links de pular
- Rodapé
- Estruturar a navegação
- Campo de pesquisa
- Modelos de página: base e erro
- Avatar
- Densidade

### Referências

- [Header (Cabeçalho)](https://www.gov.br/ds/components/header) gov.br DS
- [GOV.UK header](https://design-system.service.gov.uk/components/header/) GOV.UK Design System
- [Service navigation](https://design-system.service.gov.uk/components/service-navigation/) GOV.UK Design System
- [Navigate a service](https://design-system.service.gov.uk/patterns/navigate-a-service/) GOV.UK Design System
- [Header](https://designsystem.dk/komponenter/header/) DKFDS
- [Header](https://hds.hel.fi/components/header) Helsinki Design System
- [Header: accessibility](https://hds.hel.fi/components/header/accessibility) Helsinki Design System
- [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) Apple HIG

## Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |
