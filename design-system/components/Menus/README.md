# Menus

Um menu revela uma lista de ações ou opções quando a pessoa ativa um botão, economizando espaço na tela.

O menu fica oculto até que alguém interaja com o acionador. Cada item representa um comando, uma opção ou um estado que afeta a seleção ou o contexto atual ([HIG](https://developer.apple.com/design/human-interface-guidelines/menus)). O gov.br descreve esse comportamento como padrão dropdown: uma superfície flutuante e temporária que surge a partir de um acionador, com um indicador de estado ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). No Trama, o menu é um `.tr-menu` aberto por um botão visível: um botão com rótulo e indicador, um botão circular “Mais opções” ou o segmento de seta de um botão dividido.

**Quando usar.** Para reunir ações sobre um único objeto, como uma linha de tabela ([Geist](https://vercel.com/geist/menu)); para oferecer variações de uma ação ([HIG](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)); e para funções extras em pouco espaço, sem levar a pessoa a outra tela ([DKFDS](https://designsystem.dk/komponenter/overflowmenu/), [gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)).

**Quando não usar.** Para coletar um valor num formulário, use select ou combobox ([Fluent](https://fluent2.microsoft.design/components/web/react/core/menu/usage)). Para a navegação principal, use a navegação lateral ou a barra de navegação. Para uma ou duas ações, use botões visíveis; para escolher entre duas opções, use radio ou switch ([HIG](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), [gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). Para conteúdo extenso ou complexo, leve a pessoa a uma página ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)).

## Anatomia

1.  **Acionador**: botão visível com `aria-haspopup="menu"`, `aria-expanded` e `aria-controls`, os mesmos atributos que o utilitário de dropdown do gov.br gera no acionador ([gov.br DS](https://www.gov.br/ds/utilitarios/js/dropdown)). A área de clique cobre o botão inteiro, incluindo o indicador ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)).
2.  **Indicador de estado**: seta no fim do acionador, para baixo com o menu fechado e para cima com ele aberto ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). É opcional quando o acionador já representa o menu, como o botão “Mais opções”.
3.  **Superfície** (`.tr-menu`): fundo `--t-surface-raised`, raio `--r-lg`, sombra `--e-4`, camada `--z-2`, largura entre 200px e 300px ([Fluent](https://fluent2.microsoft.design/components/web/react/core/menu/usage)).
4.  **Item**: rótulo, ícone opcional à esquerda e atalho opcional à direita em `kbd`.
5.  **Cabeçalho de grupo** (`.tr-menu__group`) e **separador** (`hr`), opcionais.
6.  **Indicador de submenu ou de seleção**: seta após o rótulo para submenu; marca de verificação para opção ativa.

## Tipos

| Tipo                      | Acionador                       | Uso                                                                                                                                              |
|---------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Menu de ações             | Botão com rótulo e indicador    | Comandos relacionados à finalidade do botão ([HIG](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)).            |
| Menu “Mais opções”        | Botão circular de três pontos   | Ações secundárias quando falta espaço ([Geist](https://vercel.com/geist/dots-menu), [DKFDS](https://designsystem.dk/komponenter/overflowmenu/)). |
| Itens de seleção única    | Qualquer                        | Escolher um critério, como ordenação. Usa `menuitemradio` ([Fluent](https://fluent2.microsoft.design/components/web/react/core/menu/usage)).     |
| Itens de seleção múltipla | Qualquer                        | Ligar vários filtros ou atributos. Usa `menuitemcheckbox` ([Fluent](https://fluent2.microsoft.design/components/web/react/core/menu/usage)).     |
| Menu do botão dividido    | Segmento de seta de `.tr-split` | Variações de uma ação padrão. Veja Botões.                                                                                                       |

## Boas práticas

**Ponha primeiro os itens mais usados.** As pessoas leem o menu de cima para baixo ([HIG](https://developer.apple.com/design/human-interface-guidelines/menus)). Ações frequentes no topo, ações perigosas no fim ([Fluent](https://fluent2.microsoft.design/components/web/react/core/menu/usage)).

**Agrupe itens relacionados.** Separe grupos com `hr` e, se ajudar a varrer, com cabeçalho ([HIG](https://developer.apple.com/design/human-interface-guidelines/menus)).

**Controle o tamanho.** De 3 a 10 itens. Com menos de três, o clique extra não compensa ([HIG](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), [DKFDS](https://designsystem.dk/komponenter/overflowmenu/)). Acima de cerca de 10, agrupe ou leve ações secundárias para outra tela ([Geist](https://vercel.com/geist/menu)). Se o conteúdo faria a superfície criar barra de rolagem na tela, prefira um link para uma página ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)).

**Use no máximo um nível de submenu.** Cada submenu esconde itens e acrescenta complexidade. Crie um quando o mesmo termo se repete em vários itens, como “Ordenar por” ([HIG](https://developer.apple.com/design/human-interface-guidelines/menus), [Fluent](https://fluent2.microsoft.design/components/web/react/core/menu/usage)).

> **Divergência entre referências** O gov.br admite até três níveis de elementos dropdown em cascata, com cautela ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). A HIG e o Fluent recomendam submenus raros e rasos ([HIG](https://developer.apple.com/design/human-interface-guidelines/menus), [Fluent](https://fluent2.microsoft.design/components/web/react/core/menu/usage)). O Trama mantém um nível só, pelo critério de acessibilidade: cada nível exige um movimento preciso do ponteiro e mais um passo de teclado, e os níveis aninhados se sobrepõem na classe Compacta.

**Não esconda as ações principais.** Deixe-as visíveis como botões ([HIG](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)). Itens ocultos são sempre mais difíceis de encontrar ([DKFDS](https://designsystem.dk/komponenter/overflowmenu/)).

**Coloque o botão “Mais opções” depois das ações visíveis.** Sozinho, sem contexto, ele tende a ser ignorado ([DKFDS](https://designsystem.dk/komponenter/overflowmenu/)).

**Peça confirmação para itens destrutivos.** Mostre-os em `--t-danger` (`.tr-danger-item`), no fim, depois de um separador, e abra um diálogo de confirmação ([HIG](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons), [Geist](https://vercel.com/geist/menu)).

**Faça** Deixe as ações principais visíveis e leve só as secundárias para o menu “Mais opções”, ao lado delas.

**Não faça** Esconda todas as ações da vista, inclusive a principal, num único botão de três pontos sem contexto.

### Estados

Os itens têm repouso, hover, foco, marcado e indisponível. Hover é a camada `--o-hover` sobre a cor do item; só um item tem hover ou foco por vez. Enquanto o menu está aberto, o acionador mantém o estado ativado, para deixar claro que foi a pessoa quem abriu ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)); o kit aplica essa camada a `[aria-expanded="true"]`.

**Item indisponível.** Se o comando nunca se aplica à pessoa, por exemplo por falta de permissão que ela não pode obter, retire o item. Se ela pode torná-lo disponível, como selecionar um texto antes de “Copiar”, mostre o item esmaecido em `--t-fg-disabled` com `aria-disabled="true"`, mantenha-o focável e diga o motivo no próprio item ou numa descrição associada (`aria-describedby`). Um cadeado com explicação serve para itens que dependem de permissão ([Geist](https://vercel.com/geist/menu)).

> **Divergência entre referências** A HIG mostra itens indisponíveis esmaecidos, sem explicação, para que a pessoa saiba que o comando existe ([HIG](https://developer.apple.com/design/human-interface-guidelines/menus)). O menu de navegação do gov.br prevê o estado desabilitado sem pedir explicação ([gov.br DS](https://www.gov.br/ds/components/menu)). Pela decisão transversal D9, o Trama não tem item desabilitado sem explicação: um item esmaecido sem motivo não diz à pessoa o que fazer.

### Comportamento

**Abra com clique, toque, Enter ou Espaço.** Menus que abrem no hover atrapalham leitores de tela e a rolagem com trackpad ([Geist](https://vercel.com/geist/menu), [HDS](https://hds.hel.fi/components/header/accessibility)). O gov.br admite abertura por hover ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)); o Trama não, pelo critério de acessibilidade (WCAG 2.2, 1.4.13).

**Feche de todas as formas que fizerem sentido.** Pelo próprio acionador, ao escolher um item, com Esc e ao clicar fora ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown), [Geist](https://vercel.com/geist/menu)). Ao fechar, devolva o foco ao acionador.

**Posicione junto ao acionador, sem criar espaço.** Por padrão a superfície abre abaixo do acionador; perto da borda da janela, abre para o lado ou para cima. Ela usa só o espaço visível e nunca empurra o layout nem faz surgir barra de rolagem na página ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). Submenus abrem à direita do item e passam para a esquerda se faltar espaço ([Blueprint](https://blueprintjs.com/docs/#core/components/menu)). A entrada usa `--m-normal` com `--m-ease-enter`.

**Use véu só quando a atenção for prioritária.** O padrão é só a sombra. Se aplicar um véu `--t-overlay` por trás, bloqueie toda interação com o conteúdo sob ele, por mouse e por teclado ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)).

**Prefira um item que alterna o rótulo.** “Mostrar mapa” vira “Ocultar mapa”. Para atributos ligados, use marca de verificação ([HIG](https://developer.apple.com/design/human-interface-guidelines/menus)).

## Conteúdo

**Ações começam por verbo; opções são substantivos curtos.** “Duplicar projeto”, “Mover para pasta…”; “Data de criação”, “Nome (A a Z)” ([Fluent](https://fluent2.microsoft.design/components/web/react/core/menu/usage)). Use até duas palavras, três quando inevitável, e sem artigos ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy), [HIG](https://developer.apple.com/design/human-interface-guidelines/menus)).

**Caixa de frase, sem ponto final.** ([Fluent](https://fluent2.microsoft.design/components/web/react/core/menu/usage))

**Nunca trunque um item.** Prefira rótulos curtos; se um rótulo passar dos 300px da superfície, ele quebra a linha e o item cresce na altura. Reticências nunca cortam o texto de um item de menu (decisão D15).

**Use reticências quando o item abre um diálogo.** “Renomear…” ([HIG](https://developer.apple.com/design/human-interface-guidelines/menus)).

**Indique o sentido da ordenação.** “(A a Z)”, “(mais recentes primeiro)” ([DKFDS](https://designsystem.dk/komponenter/overflowmenu/)).

**Use ícones de forma uniforme.** Dentro de um grupo, todos os itens têm ícone ou nenhum tem ([HIG](https://developer.apple.com/design/human-interface-guidelines/menus)).

## Acessibilidade

Use o padrão de menu do WAI-ARIA: `role="menu"` na superfície, `menuitem`, `menuitemradio` ou `menuitemcheckbox` nos itens e `aria-checked` para opções marcadas.

| Tecla                                         | Função                                       |
|-----------------------------------------------|----------------------------------------------|
| Enter, Espaço ou seta para baixo no acionador | Abre o menu e foca o primeiro item           |
| Setas para cima e para baixo                  | Movem o foco entre os itens                  |
| Home e End                                    | Vão ao primeiro e ao último item             |
| Letra                                         | Salta para o próximo item que começa com ela |
| Setas para a direita e para a esquerda        | Abrem e fecham o submenu                     |
| Enter ou Espaço                               | Ativa o item                                 |
| Esc                                           | Fecha o menu e devolve o foco ao acionador   |

As setas, Home, End, salto por letra e retorno do foco seguem o Geist ([Geist](https://vercel.com/geist/menu)); Esc para fechar e Enter ou Espaço para abrir seguem também o gov.br ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). Dê ao acionador circular um `aria-label` que nomeie o conjunto, como “Mais opções do relatório”, e mostre o mesmo texto num tooltip. Para itens indisponíveis, a explicação fica em `aria-describedby`.

## Tokens usados

| Token                                           | Uso                                           |
|-------------------------------------------------|-----------------------------------------------|
| `--t-surface-raised`, `--e-4`, `--z-2`          | Superfície, sombra e camada                   |
| `--r-lg`, `--r-md`                              | Raio do menu e dos itens                      |
| `--sp-100`, `--sp-300`                          | Margem interna do menu e dos itens            |
| `--o-hover`                                     | Hover do item e estado ativado do acionador   |
| `--t-fg-1`, `--t-fg-3`, `--t-fg-disabled`       | Rótulo; cabeçalho e atalho; item indisponível |
| `--t-danger`, `--t-border-subtle`               | Item destrutivo; separador                    |
| `--t-overlay`                                   | Véu opcional                                  |
| `--m-normal`, `--m-ease-enter`, `--m-ease-exit` | Abertura e fechamento                         |

## Considerações por plataforma

### Web desktop

Mostre atalhos de teclado nos itens que os têm. A superfície não segue o grid; posicione-a em relação à janela ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). Use itens de densidade alta só em ferramentas com mouse.

### Web móvel

Use densidade baixa, com itens de no mínimo `--c-touch`. Na classe Compacta, a superfície ocupa a largura total da tela ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)); o Trama a apresenta presa à base, ao alcance do polegar, com o mesmo conteúdo e a mesma ordem. Atalhos de teclado não aparecem.

### Tablets e dobráveis

Abra o menu perto do elemento tocado, para reduzir o deslocamento do dedo e manter o contexto ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Com teclado físico conectado, todo o comportamento de teclado do desktop vale também. Ao mudar de classe de janela com o menu aberto, feche-o e devolva o foco ao acionador.

## Recursos

### Relacionados

- Menu de contexto
- Botões
- Barra de ferramentas
- Select e dropdown
- Popovers

### Referências

- [Dropdown (Elemento Flutuante)](https://www.gov.br/ds/padroes/design/dropdown) gov.br DS
- [Utilitário Dropdown](https://www.gov.br/ds/utilitarios/js/dropdown) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Menu de Navegação](https://www.gov.br/ds/components/menu) gov.br DS
- [Menus](https://developer.apple.com/design/human-interface-guidelines/menus) Apple HIG
- [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons) Apple HIG
- [Menu: usage](https://fluent2.microsoft.design/components/web/react/core/menu/usage) Fluent 2
- [Overflow menu](https://designsystem.dk/komponenter/overflowmenu/) DKFDS
- [Menu](https://vercel.com/geist/menu) Geist
- [Dots Menu](https://vercel.com/geist/dots-menu) Geist
- [Menu](https://blueprintjs.com/docs/#core/components/menu) Blueprint
- [Header: accessibility](https://hds.hel.fi/components/header/accessibility) Helsinki Design System
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o indicador de estado, a persistência do estado do acionador, a superfície que não cria espaço, o véu opcional e as formas de fechar; proíbe truncar itens (D15) e itens indisponíveis sem explicação (D9). |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                          |
