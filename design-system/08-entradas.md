# Entradas

## Teclado

Tudo o que a pessoa faz com mouse ou toque precisa estar disponível pelo teclado, e os comandos frequentes ganham atalhos previsíveis.

O teclado físico é a entrada principal de muita gente no desktop e é comum em tablets com capa-teclado. Algumas pessoas navegam só com o teclado, por preferência ou necessidade; outras usam tecnologias assistivas que simulam o teclado. O gov.br cita teclados alternativos, usados por pessoas com deficiência física que têm dificuldade com o teclado convencional, e programas de reconhecimento de voz ([gov.br DS](https://www.gov.br/ds/acessibilidade)). Os atalhos aceleram quem usa o produto todos os dias.

O Trama trata o teclado em duas camadas. A primeira é obrigatória: navegação e operação completas com Tab, setas, Enter, Espaço e Esc, conforme as Diretrizes de Acessibilidade para Conteúdo Web (WCAG) 2.2, critério 2.1.1. A segunda é opcional: atalhos para comandos frequentes, que nunca são o único caminho para uma ação.

### Boas práticas

#### Navegação

**Torne todo controle alcançável e operável pelo teclado.** A HIG pede suporte ao Acesso Total pelo Teclado, que permite navegar e ativar janelas, menus e controles usando só o teclado ([HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards)). O gov.br pede que a pessoa consiga acessar todo o conteúdo e as funcionalidades só pelo teclado, acompanhe onde está o foco e navegue até todos os elementos interativos ([gov.br DS](https://www.gov.br/ds/templates/base)). Use elementos nativos (`<button>`, `<a href>`, `<input>`), que já recebem foco e respondem às teclas certas.

**Deixe a pessoa alternar entre teclado e mouse.** O gov.br pede que a pessoa decida como navegar entre os campos de um formulário, pelo teclado ou pelo mouse, e possa trocar quando quiser ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). Nada no Trama muda de comportamento por causa da entrada usada antes.

**Ofereça links de pular em toda página.** O link de pular fica oculto até o primeiro Tab e leva o foco direto ao conteúdo principal ([GOV.UK](https://design-system.service.gov.uk/components/skip-link/), [DKFDS](https://designsystem.dk/komponenter/skip-link/)). Coloque-o logo após a abertura do `<body>`, depois do banner de cookies se houver, e fora do cabeçalho ([GOV.UK](https://design-system.service.gov.uk/components/skip-link/)). O gov.br pede que ele seja o primeiro elemento a receber foco, que Esc o recolha e que ofereça âncoras para o conteúdo, o menu principal e áreas de apoio como ajuda, acessibilidade e pesquisa ([gov.br DS](https://www.gov.br/ds/components/skiplink)). No Trama, o primeiro link vai sempre para o conteúdo principal, e outros destinos são opcionais (`.tr-skiplinks`). Veja Links de pular.

**Use Tab entre grupos e setas dentro de um grupo.** Em listas de opções, abas, radios, menus, barras de ferramentas e grades, Tab entra e sai do grupo e as setas movem entre os itens. A HIG descreve o mesmo modelo de grupos de foco ([HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)), e o gov.br pede as setas esquerda e direita entre abas ([gov.br DS](https://www.gov.br/ds/components/tab)). Em painéis suspensos que contêm campos e botões variados, Tab percorre os elementos, como o gov.br define para o dropdown ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). Veja Foco e seleção.

**Nunca prenda o foco sem saída.** Diálogos modais contêm o foco enquanto estão abertos e o devolvem ao elemento de origem ao fechar, como pedem o gov.br ([gov.br DS](https://www.gov.br/ds/components/modal)) e o Geist ([Geist](https://vercel.com/geist/command-menu)). Fora disso, a pessoa sempre consegue sair de um componente com Tab ou Esc (WCAG 2.2, 2.1.2).

**Deixe o texto digitado se comportar como texto.** Depois que o campo recebe foco, a pessoa digita sem nenhum passo extra, navega entre palavras com Ctrl e setas no Windows ou Option e setas no Mac, e alcança com Tab os controles internos do campo, como Mostrar senha ([gov.br DS](https://www.gov.br/ds/components/input)).

#### Teclas padrão do Trama

| Tecla           | Ação                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tab e Shift Tab | Movem o foco para o próximo ou o anterior elemento ou grupo interativo.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Enter           | Ativa links e botões; envia formulários de um campo; abre o item em foco numa lista.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Espaço          | Ativa botões; marca e desmarca checkbox e switch; rola a página quando o foco está num link ou fora de um controle.                                                                                                                                                                                                                                                                                                                                                                                               |
| Esc             | Fecha menu, popover, tooltip, diálogo e links de pular e cancela a operação em curso. A HIG associa Esc a cancelar a ação atual ([HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards)), e o gov.br usa Esc para fechar dropdown ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)), menu ([gov.br DS](https://www.gov.br/ds/components/menu)), modal ([gov.br DS](https://www.gov.br/ds/components/modal)) e tooltip ([gov.br DS](https://www.gov.br/ds/components/tooltip)). |
| Setas           | Movem entre itens de um grupo: abas, opções de radio, itens de menu e de lista, células de tabela.                                                                                                                                                                                                                                                                                                                                                                                                                |
| Home e End      | Vão ao primeiro ou ao último item do grupo. O gov.br as trata como opcionais nas abas ([gov.br DS](https://www.gov.br/ds/components/tab)); o Trama as exige em todo grupo com setas.                                                                                                                                                                                                                                                                                                                              |
| Mod K           | Abre o menu de comandos global, quando o produto tiver um.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ?               | Abre a lista de atalhos do produto, quando o foco não está num campo de texto.                                                                                                                                                                                                                                                                                                                                                                                                                                    |

Mod significa ⌘ no macOS e no iPadOS e Ctrl no Windows, Linux, ChromeOS e Android. O Blueprint usa o mesmo modificador, que escolhe a tecla preferida de cada sistema ([Blueprint](https://blueprintjs.com/docs/#core/hooks/use-hotkeys)), e o Geist associa o menu de comandos a ⌘K no macOS e Ctrl+K nos demais sistemas ([Geist](https://vercel.com/geist/command-menu)).

> **Divergência entre referências** A página de acessibilidade do rodapé do gov.br pede acionar links com Espaço ou Enter ([gov.br DS](https://www.gov.br/ds/components/footer)), enquanto a do breadcrumb usa Enter ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)). No HTML, o link nativo responde só a Enter, e Espaço rola a página. Mudar isso quebraria o comportamento que leitores de tela e navegadores já oferecem, e o próprio gov.br recomenda os elementos nativos por seus recursos de acessibilidade ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)). Pelo critério de acessibilidade, o Trama decide: links com Enter, botões com Enter e Espaço. A página do link de pular do gov.br cita Ctrl+Tab para voltar ([gov.br DS](https://www.gov.br/ds/components/skiplink)), enquanto as demais páginas do gov.br e a HIG usam Shift+Tab ([HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards)). Por convergência, o Trama usa Shift+Tab.

#### Atalhos

**Respeite os atalhos padrão do navegador e do sistema.** Não redefina um atalho padrão para outra ação ([HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards)). Na web, isso inclui atalhos do navegador como Mod+F, Mod+P, Mod+L e Mod+T. O gov.br lembra que cada navegador combina teclas de um jeito e pede atenção a essas combinações ao criar atalhos ([gov.br DS](https://www.gov.br/ds/components/skiplink)). Por isso o Trama não usa o atributo `accesskey`.

**Crie atalhos só para os comandos mais frequentes.** Atalhos demais tornam o produto difícil de aprender. Comece por desfazer, refazer, pesquisar e criar novo item.

**Use os modificadores como as pessoas esperam.** Prefira Mod como modificador principal e Shift como secundário, para uma variação do mesmo comando. Use Alt (Option) com moderação ([HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards)). Alguns idiomas precisam de modificadores para gerar certos caracteres. Teste com o layout ABNT2.

**Associe letras pelo caractere digitado.** O Blueprint identifica letras pelo caractere que a tecla produz, para respeitar layouts como QWERTY e AZERTY, e números pela posição física ([Blueprint](https://blueprintjs.com/docs/#core/hooks/use-hotkeys)). Na web, use `event.key` para letras.

**Controle os atalhos de tecla única.** Atalhos sem modificador, como ? ou J, disparam por engano com software de voz e com digitação. Desative-os enquanto o foco estiver num campo de texto e ofereça, nas configurações, uma forma de desligá-los ou remapeá-los, conforme WCAG 2.2, 2.1.4.

**Torne os atalhos fáceis de descobrir.** Mostre o atalho ao lado do comando em menus e no tooltip do botão. Ofereça uma lista de todos os atalhos: o Blueprint abre essa lista com a tecla ? ([Blueprint](https://blueprintjs.com/docs/#core/context/hotkeys-provider)).

**Nunca dependa só de um atalho.** Teclados virtuais não oferecem atalhos ([HIG](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards)). Toda ação com atalho também existe como botão ou item de menu.

### Conteúdo

**Escreva atalhos com o símbolo certo para cada sistema.** O componente de tecla do Geist troca ⌘ por Ctrl no Windows e no Linux ([Geist](https://vercel.com/geist/keyboard-input)). No Trama, detecte o sistema e exiba ⌘, ⌥, ⇧ no macOS e Ctrl, Alt, Shift nos demais.

**Use um elemento `<kbd>` por tecla e deixe a pontuação fora.** Cada elemento contém uma tecla; pontuação e conectivos ficam no texto ao redor, para que leitores de tela não os anunciem como teclas ([Geist](https://vercel.com/geist/keyboard-input)). Exemplo: "Pressione Ctrl K para abrir o menu de comandos."

**Liste modificadores numa ordem fixa.** No macOS, siga a ordem Control, Option, Shift, Command ([HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards)). Nos demais sistemas, o Trama usa Ctrl, Alt, Shift.

**Faça** uma tecla por elemento e pontuação no texto ao redor.

**Não faça** combine várias teclas e pontuação num só elemento, nem fixe o símbolo de um sistema.

### Acessibilidade

Mantenha a ordem de foco igual à ordem de leitura (WCAG 2.2, 2.4.3) e o foco sempre visível (WCAG 2.2, 2.4.7). O gov.br pede manter sempre habilitado o estado de foco do navegador ([gov.br DS](https://www.gov.br/ds/components/button)): nunca remova o contorno sem substituto. Tooltips aparecem quando o gatilho recebe foco, somem com Esc ou quando o foco sai, e não recebem foco ([gov.br DS](https://www.gov.br/ds/components/tooltip)). Teste cada tela só com o teclado, do primeiro Tab até concluir a tarefa, e também com leitor de tela, porque leitores interceptam várias teclas e atalhos de tecla única podem não chegar à página.

### Considerações por plataforma

#### Web desktop

É a plataforma em que atalhos fazem mais diferença. A HIG recomenda atalhos de teclado para acelerar ações e permitir trabalhar só com o teclado ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos)).

#### Web móvel

O teclado é virtual na maior parte do tempo. Concentre-se em pedir o teclado certo para cada campo (veja Projetar para web móvel). Teclados Bluetooth e acesso por varredura continuam exigindo navegação completa por Tab.

#### Tablets e dobráveis

Com capa-teclado, a pessoa alterna entre toque e teclado o tempo todo. Mostre o anel de foco assim que uma tecla de navegação for pressionada e mantenha os atalhos disponíveis. A HIG lembra que pessoas com iPad usam com frequência teclado físico ([HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards)).

### Recursos

#### Relacionados

- Foco e seleção
- Links de pular
- Mouse e trackpad
- Menus
- Diálogos
- Acessibilidade

#### Referências

- [Template base](https://www.gov.br/ds/templates/base) gov.br DS
- [Skip link](https://www.gov.br/ds/components/skiplink) gov.br DS
- [Tab](https://www.gov.br/ds/components/tab) gov.br DS
- [Modal](https://www.gov.br/ds/components/modal) gov.br DS
- [Menu](https://www.gov.br/ds/components/menu) gov.br DS
- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Button](https://www.gov.br/ds/components/button) gov.br DS
- [Footer](https://www.gov.br/ds/components/footer) gov.br DS
- [Breadcrumb](https://www.gov.br/ds/components/breadcrumb) gov.br DS
- [Tooltip](https://www.gov.br/ds/components/tooltip) gov.br DS
- [Dropdown](https://www.gov.br/ds/padroes/design/dropdown) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Movimento](https://www.gov.br/ds/fundamentos-visuais/movimento) gov.br DS
- [Acessibilidade](https://www.gov.br/ds/acessibilidade) gov.br DS
- [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards) Apple HIG
- [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) Apple HIG
- [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards) Apple HIG
- [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) Apple HIG
- [Skip link](https://design-system.service.gov.uk/components/skip-link/) GOV.UK Design System
- [Gå til sidens indhold (skip-link)](https://designsystem.dk/komponenter/skip-link/) DKFDS
- [useHotkeys](https://blueprintjs.com/docs/#core/hooks/use-hotkeys) Blueprint
- [HotkeysProvider](https://blueprintjs.com/docs/#core/context/hotkeys-provider) Blueprint
- [Keyboard Input](https://vercel.com/geist/keyboard-input) Geist
- [Command Menu](https://vercel.com/geist/command-menu) Geist

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                           |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta links de pular com vários destinos, alternância livre entre teclado e mouse, comportamento de texto em campos, Home e End obrigatórias em grupos e as divergências sobre Espaço em links e Shift+Tab. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                    |

## Mouse e trackpad

Mouse e trackpad dão precisão e permitem hover, clique secundário e arrastar, sempre como caminhos adicionais a toque e teclado.

As pessoas valorizam a precisão e a flexibilidade dos dispositivos apontadores. No computador, elas costumam combinar o apontador com o teclado; no tablet, o apontador se soma ao toque como forma adicional de interagir ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)). Algumas pessoas usam apontadores alternativos, que simulam o mouse e são acionados com os olhos, os pés ou as mãos ([gov.br DS](https://www.gov.br/ds/acessibilidade)). Na web, o mesmo layout pode receber mouse, trackpad, caneta e dedo, às vezes na mesma sessão.

O Trama projeta cada interação para funcionar primeiro com toque e teclado e acrescenta recursos de apontador por cima: estados de hover, menu de contexto, seleção por arraste, cursores, densidade alta e atalhos com modificadores.

### Boas práticas

#### Interação

**Ofereça a mesma experiência com qualquer entrada.** As pessoas esperam alternar entre gestos, apontador e teclado sem aprender interações diferentes para cada modo ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)). O gov.br pede que a pessoa possa escolher entre teclado e mouse e alternar quando quiser ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)).

**Use hover só para revelar e reforçar.** Hover não existe em telas de toque, e o gov.br observa que ele pode não fazer sentido em dispositivos sem mouse ([gov.br DS](https://www.gov.br/ds/components/checkbox)). Use-o para destacar a linha ou o card sob o cursor, mostrar um tooltip ou revelar controles que se minimizam ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)). Mantenha as ações principais fora do hover, porque quem usa toque não alcança um controle revelado só por hover ([Geist](https://vercel.com/geist/tooltip)). Não abra menus só por hover: abra com clique, toque, Enter ou Espaço.

**Desenhe o hover como camada sobre o próprio elemento.** O gov.br aplica o hover como uma camada semitransparente na cor do primeiro plano do elemento, com opacidade menor em fundo claro e maior em fundo escuro, e pede o feedback no próprio objeto ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). No Trama, a camada usa `--o-hover` (0,16 no claro, 0,30 no escuro) e o pressionado usa `--o-pressed`; a marca usa `--t-brand-hover` e `--t-brand-pressed`. No pressionado, retire ou reduza sombras de elevação ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Veja Estados de interação.

**Mantenha um hover por vez.** Só um elemento fica em hover na tela, e elementos desabilitados não recebem hover. Se o hover abriu um painel suspenso, o acionador pode manter o estilo até o painel fechar ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Num campo de texto em foco, dispense o hover da superfície e mantenha a mudança do cursor ([gov.br DS](https://www.gov.br/ds/components/input)).

**Siga as regras de conteúdo exibido no hover.** Conteúdo que aparece no hover ou no foco precisa poder ser dispensado com Esc, permanecer visível enquanto o ponteiro estiver sobre ele e não sumir sozinho, conforme as Diretrizes de Acessibilidade para Conteúdo Web (WCAG) 2.2, critério 1.4.13. O Geist recomenda um pequeno atraso de entrada para que o tooltip não pisque quando o mouse passa por cima ([Geist](https://vercel.com/geist/tooltip)). O gov.br pede não depender só do hover para acionar tooltips ([gov.br DS](https://www.gov.br/ds/components/tooltip)): o mesmo conteúdo aparece no foco.

**Espelhe o menu de contexto num controle visível.** O clique secundário revela menus de contexto ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)). O menu de contexto nunca pode ser a única entrada para uma ação: repita cada item num menu visível ou num botão da linha ([Geist](https://vercel.com/geist/context-menu)). Suprima o menu nativo do navegador só na área do gatilho e posicione o menu no ponteiro ([Geist](https://vercel.com/geist/context-menu)). Veja Menu de contexto.

#### Áreas de clique e densidade

**Dê áreas de clique de pelo menos 24 px.** O gov.br define 24 por 24 px como área mínima de clique em interfaces operadas por mouse ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)) e permite que a área de ação ultrapasse a superfície visível do elemento ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). O valor coincide com o mínimo de WCAG 2.2, 2.5.8. A HIG sugere cerca de 12 pontos de folga ao redor de elementos com borda e cerca de 24 pontos ao redor de elementos sem borda ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)). Quando o toque for possível, o mínimo passa a `--c-touch`.

**Use densidade alta só com apontador fino.** Aplique `data-density="alta"` em tabelas, listas longas e ferramentas apenas quando `(pointer: fine)` for verdadeira e nenhuma entrada de toque estiver disponível. Nunca use densidade alta em alertas e mensagens, como pede o gov.br ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). Veja Densidade.

**Faça áreas de clique contíguas em barras.** Entre botões vizinhos de uma barra de ferramentas, evite espaços sem área de clique, que fazem o realce saltar quando o ponteiro passa de um botão a outro ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)).

#### Cursores

**Use o cursor para indicar o que vai acontecer.** A HIG define cursores padrão para link, texto, arrastar, redimensionar e operação não permitida ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)), e o gov.br associa um cursor a cada estado ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O Trama usa os valores da propriedade CSS `cursor`:

| Situação                                                        | Valor de `cursor`                                                                                                                    |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Link, botão e outro elemento interativo em hover ou pressionado | `pointer`                                                                                                                            |
| Campo de texto                                                  | `text` ([gov.br DS](https://www.gov.br/ds/components/input))                                                                         |
| Elemento desabilitado                                           | `not-allowed`                                                                                                                        |
| Elemento que pode ser arrastado                                 | `grab`, junto com o ícone de alça à esquerda ou no topo do elemento ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)) |
| Elemento sendo arrastado                                        | `grabbing`, com `.tr-dragging`                                                                                                       |
| Área de soltura ativa                                           | `copy`, com `.tr-dropzone--active`                                                                                                   |
| Divisor de painel                                               | `col-resize` ou `row-resize`                                                                                                         |

**Evite efeitos de ponteiro gratuitos.** Mudanças de aparência que não informam nada distraem ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)). O gov.br pede estados funcionais, sem transições elaboradas que criem ruído ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Não aumente a escala de linhas de tabela no hover ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)).

**Não coloque instruções no ponteiro.** Texto instrutivo junto ao ponteiro faz o produto parecer complicado ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)). Anotações úteis, como coordenadas num gráfico ou largura e altura ao redimensionar, são bem-vindas.

#### Modificadores e arraste

**Use modificadores como as pessoas esperam.** Shift ao redimensionar mantém a proporção ([HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards)); Mod com clique adiciona itens à seleção; Shift com clique seleciona um intervalo. Veja Foco e seleção.

**Ofereça alternativa a arrastar.** Toda ação feita arrastando também precisa de um caminho com um único clique ou toque, como os botões "Subir" e "Descer" ou um menu "Mover para" (WCAG 2.2, 2.5.7). Veja Arrastar e soltar.

**Ative ações no fim do clique.** Dispare a ação quando o botão é solto, para que a pessoa possa desistir afastando o ponteiro (WCAG 2.2, 2.5.2). Elementos nativos já fazem isso.

**Não redefina gestos do sistema.** As pessoas esperam que gestos do trackpad, como deslizar entre páginas, funcionem igual em todos os programas ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)). Na web, não intercepte a rolagem nem o gesto de voltar do navegador.

#### Foco ao usar o apontador

O clique em botões, links e controles não mostra o anel de foco; campos de texto mostram, porque sempre importa saber onde se está digitando ([Blueprint](https://blueprintjs.com/docs/#core/accessibility)). O gov.br define o mesmo padrão: clicar ou tocar não gera foco visual, salvo quando a diretriz do elemento disser o contrário ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O Trama obtém esse comportamento com `:focus-visible`, que todos os componentes do kit usam. Não remova o contorno de foco com `outline: none` sem substituto.

**Faça** mantenha um botão visível para as ações da linha, além do menu de contexto.

**Não faça** deixe ações acessíveis só pelo clique secundário ou pelo hover.

> **Divergência entre referências** No estado arrastando, o gov.br gira o objeto 5 graus e aplica contorno e sombra na cor do estado interativo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). A HIG pede evitar efeitos de ponteiro que não informam nada ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)). Nenhuma fonte cita pesquisa. O Trama adota do gov.br a combinação de opacidade, sombra e leve rotação, que diferencia o objeto em movimento sem depender só da cor, e usa a rotação menor de `.tr-dragging`, que reduz o movimento na tela.

### Considerações por plataforma

#### Web desktop

É a plataforma principal do apontador. Suporte seleção precisa e edição fina, como a HIG recomenda para entradas de alta precisão ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos)). A densidade alta é aceitável em tabelas e barras de ferramentas quando `(pointer: fine)` é verdadeira.

#### Web móvel

Não há hover. Projete supondo `(hover: none)` e `(pointer: coarse)`. O menu de contexto abre com toque longo ([Geist](https://vercel.com/geist/context-menu)).

#### Tablets e dobráveis

Um trackpad pode estar conectado ou não, e a pessoa alterna entre ele e o dedo. Use `any-pointer` e `any-hover` para acrescentar recursos de apontador sem reduzir alvos de toque nem passar para a densidade alta. Diferencie ponteiro e dedo só quando isso agrega valor, como permitir clique preciso numa linha do tempo de vídeo ([HIG](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)).

### Recursos

#### Relacionados

- Estados de interação
- Densidade
- Teclado
- Toque e gestos
- Menu de contexto
- Arrastar e soltar

#### Referências

- [Estados](https://www.gov.br/ds/fundamentos-visuais/estados) gov.br DS
- [Iconografia](https://www.gov.br/ds/fundamentos-visuais/iconografia) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Checkbox](https://www.gov.br/ds/components/checkbox) gov.br DS
- [Tooltip](https://www.gov.br/ds/components/tooltip) gov.br DS
- [Acessibilidade](https://www.gov.br/ds/acessibilidade) gov.br DS
- [Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices) Apple HIG
- [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards) Apple HIG
- [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) Apple HIG
- [Context Menu](https://vercel.com/geist/context-menu) Geist
- [Tooltip](https://vercel.com/geist/tooltip) Geist
- [Accessibility](https://blueprintjs.com/docs/#core/accessibility) Blueprint

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. O hover passa a ser camada na cor do primeiro plano com `--o-hover`, a área mínima de clique passa a 24 px, a densidade alta fica restrita ao apontador fino e entra a tabela de cursores por estado. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                         |

## Toque e gestos

Em telas de toque, a pessoa age diretamente sobre o conteúdo com gestos conhecidos, e cada gesto tem um caminho alternativo visível.

Gesto é um movimento físico que a pessoa faz para agir diretamente sobre um objeto. Todas as plataformas suportam gestos básicos, como tocar, deslizar e arrastar, e as pessoas esperam usá-los em todo lugar ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)). O gov.br lista como gestos mais comuns deslizar na horizontal e na vertical, tocar em elementos interativos e ampliar ou reduzir com dois dedos ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). Na web, o navegador já reserva vários gestos: rolar, ampliar com pinça, voltar deslizando da borda e atualizar puxando para baixo. A aplicação convive com eles.

O Trama usa toque como entrada de primeira classe em web móvel, tablets e dobráveis. Os componentes do kit têm alvo mínimo de `--c-touch` (44 px), a densidade é baixa em toda tela operada por toque e nenhuma função depende só de um gesto.

### Boas práticas

**Ofereça mais de uma forma de agir.** Muitas pessoas preferem ou precisam de outras entradas, como voz, teclado ou acesso por varredura. Não suponha que alguém consiga fazer um gesto específico ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)). O One UI pede alternativas para ações complexas como arrastar e soltar e gestos com vários dedos ([One UI](https://developer.samsung.com/one-ui/accessibility/interaction-and-control.html)), e o gov.br pede considerar mouse, toque, teclado, voz e leitores de tela ao projetar cada componente ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Toda função que usa gesto com trajeto ou com vários dedos também funciona com um único toque, conforme as Diretrizes de Acessibilidade para Conteúdo Web (WCAG) 2.2, critério 2.5.1.

**Use gestos para conteúdo em sequência.** O gov.br recomenda a navegação por gestos para itens relacionados e em ordem natural, como páginas em sequência, para visualizações com poucos itens e para conteúdos semelhantes, como carrosséis e galerias de imagens ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). Fora desses casos, prefira controles visíveis.

**Responda aos gestos como as pessoas esperam.** Tocar ativa ou seleciona. Não use um gesto conhecido, como tocar ou deslizar, para uma ação exclusiva do seu produto, e não crie um gesto novo para uma ação padrão, como ativar um botão ou rolar ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)).

**Use gestos de atalho como complemento.** Um gesto pode acelerar uma ação, e a pessoa continua precisando de um caminho simples e conhecido, mesmo que custe um ou dois toques a mais. A HIG cita o botão Voltar, que continua presente mesmo quando deslizar da borda também volta ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)).

**Dê feedback imediato ao toque e durante o gesto.** Sem hover, o estado pressionado é o primeiro sinal de que o toque funcionou. Aplique a camada `--o-pressed` no elemento tocado, como o gov.br define para o pressionado por toque ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Enquanto a pessoa arrasta ou desliza, mostre o que vai acontecer e quanto movimento falta ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)). Ao deslizar uma linha, revele a ação e sua cor semântica, como `--t-danger` para excluir. Respeite `prefers-reduced-motion` e o controle de animações do produto.

**Mostre quando um gesto não está disponível.** Se um gesto não funciona e nada explica o motivo, a pessoa pensa que o produto travou ou que errou o gesto ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)). Deixe claro, por exemplo, que um objeto está bloqueado e não pode ser arrastado.

**Crie gestos próprios só quando forem necessários.** Gestos personalizados fazem sentido para tarefas especializadas e frequentes, como em editores de desenho. Eles precisam ser fáceis de descobrir e de fazer, distintos de outros gestos e nunca o único caminho para uma ação importante ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)).

**Não entre em conflito com gestos do sistema e do navegador.** As pessoas esperam que os gestos de acesso ao sistema funcionem sempre ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)). Na web, não capture o deslizar a partir das bordas da tela, não bloqueie a pinça com `user-scalable=no` e não impeça a rolagem da página fora de áreas como mapas e telas de desenho.

**Prefira a rolagem da página e deixe áreas seguras para arrastar.** No celular, o gov.br pede preferir a rolagem da tela à rolagem interna de elementos e prever áreas onde a pessoa arraste a tela sem risco de toque acidental ([gov.br DS](https://www.gov.br/ds/padroes/design/contentoverflow)). Uma lista em que cada linha inteira é um alvo de deslizar precisa de margem livre para rolar.

#### Alvos de toque

**Use alvos de pelo menos 44 por 44 px.** Todo controle tocável tem área de `--c-touch` nas duas dimensões. O elemento visível pode ser menor, como um ícone de 20 px, desde que a área tocável tenha 44 px; o gov.br também permite que a área de ação ultrapasse a superfície do elemento ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). Use densidade baixa (`data-density="baixa"`) em toda tela operada por toque, como o gov.br faz com o botão de entrar no celular, para compensar a menor precisão das mãos ([gov.br DS](https://www.gov.br/ds/components/signin)), e com o campo de texto na grade de 4 colunas ([gov.br DS](https://www.gov.br/ds/components/input)).

**Separe os alvos.** Alvos vizinhos colados causam toques errados. Mantenha pelo menos `--sp-200` entre controles independentes. O gov.br conta a área mínima de interação do ícone como espaço útil para medir a distância até o elemento vizinho ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)).

**Afaste controles das bordas curvas e da área de apoio da mão.** O One UI coloca informação e componentes interativos com margem das bordas laterais para evitar conflito com telas curvas e toques acidentais da palma ([One UI](https://developer.samsung.com/one-ui/layout/grid.html)). No Trama, as margens da classe Compacta (16 px) mais `env(safe-area-inset-*)` mantêm os alvos longe das bordas.

> **Divergência entre referências** O gov.br traz três valores: 40 px como área mínima de ação no toque ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)), 44 px nas páginas de acessibilidade de botões, abas e outros componentes ([gov.br DS](https://www.gov.br/ds/components/button)) e 48 por 48 px como área de toque de ícones ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)). O Fluent define 44 por 44 na web e no iOS e 48 por 48 no Android ([Fluent 2](https://fluent2.microsoft.design/layout)). Nenhuma fonte cita pesquisa própria. Os três valores ficam acima dos 24 px de WCAG 2.2, 2.5.8; 44 px é o valor de WCAG 2.2, 2.5.5, e é o valor em que as fontes mais convergem para a web. O Trama mantém 44 px para todo alvo de toque e descarta os 40 px.

**Faça** use alvos de 44 px com espaço entre eles.

**Não faça** encoste alvos pequenos, sobretudo ao lado de uma ação destrutiva.

#### Gestos padrão no Trama

| Gesto           | Ação comum                                                                                                                                                          | Alternativa obrigatória                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Tocar           | Ativar um controle; selecionar um item ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)).                                             | Enter ou Espaço no teclado.                                                             |
| Deslizar        | Rolar; revelar ações numa linha; passar itens de um carrossel; dispensar uma folha ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)). | Botão visível na linha ou menu ⋯; botões Anterior e Próximo no carrossel; botão Fechar. |
| Arrastar        | Mover um elemento ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)).                                                                  | Comandos "Mover para" ou botões Subir e Descer (WCAG 2.2, 2.5.7).                       |
| Tocar e segurar | Revelar controles ou funções adicionais, como o menu de contexto ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)).                   | Botão ⋯ visível.                                                                        |
| Pinça           | Ampliar o conteúdo ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)).                                                                 | Botões + e − em mapas e imagens; zoom do navegador preservado.                          |
| Toque duplo     | Ampliar ou reduzir ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)).                                                                 | Não use para outras ações.                                                              |

> **Divergência entre referências** Para o carrossel, o gov.br diz que, com navegação por gestos, os botões de navegação não são necessários, desde que haja uma alternativa acessível verificada com tecnologias assistivas ([gov.br DS](https://www.gov.br/ds/components/carousel)). A HIG pede que gestos de atalho complementem os controles padrão, sem substituí-los ([HIG](https://developer.apple.com/design/human-interface-guidelines/gestures)). Pelo critério de acessibilidade, o Trama decide: os botões Anterior e Próximo ficam sempre visíveis, porque atendem WCAG 2.2, 2.5.1 sem depender de leitor de tela.

### Acessibilidade

Leitores de tela em celulares mudam o significado dos gestos: um toque move o foco e um toque duplo ativa. Por isso, um gesto personalizado pode ficar inacessível com o leitor ligado. Garanta que cada ação tenha um controle nomeado. Tooltips, sem hover, abrem por toque ou foco ([gov.br DS](https://www.gov.br/ds/components/tooltip)). Não acione funções por movimento do aparelho, como sacudir, sem alternativa na interface e sem permitir desligar (WCAG 2.2, 2.5.4). Não feche nem oculte recursos automaticamente sem dar tempo suficiente para a pessoa agir ([One UI](https://developer.samsung.com/one-ui/accessibility/interaction-and-control.html)).

### Considerações por plataforma

#### Web desktop

Notebooks com tela de toque recebem os mesmos gestos. Não suponha que um desktop não tem toque: use `(any-pointer: coarse)` para detectar e, quando ela for verdadeira, mantenha densidade padrão ou baixa.

#### Web móvel

Coloque as ações frequentes no meio e na parte de baixo da tela, onde o polegar alcança com conforto ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)). Não use reprodução automática em carrosséis no celular ([gov.br DS](https://www.gov.br/ds/components/carousel)). Use `touch-action` para declarar quais gestos um componente trata, sem bloquear a rolagem da página.

#### Tablets e dobráveis

A pessoa pode usar as duas mãos, caneta e trackpad. Em telas grandes, mantenha controles ao alcance, inclusive nas laterais, e evite alvos sobre o vinco dos dobráveis. Veja Projetar para tablets e dobráveis e Postura e dobra.

### Recursos

#### Relacionados

- Densidade
- Mouse e trackpad
- Arrastar e soltar
- Carrossel
- Projetar para web móvel
- Listas

#### Referências

- [Navegação](https://www.gov.br/ds/padroes/design/navegacao) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Content overflow](https://www.gov.br/ds/padroes/design/contentoverflow) gov.br DS
- [Estados](https://www.gov.br/ds/fundamentos-visuais/estados) gov.br DS
- [Iconografia](https://www.gov.br/ds/fundamentos-visuais/iconografia) gov.br DS
- [Button](https://www.gov.br/ds/components/button) gov.br DS
- [Sign-in](https://www.gov.br/ds/components/signin) gov.br DS
- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Carousel](https://www.gov.br/ds/components/carousel) gov.br DS
- [Tooltip](https://www.gov.br/ds/components/tooltip) gov.br DS
- [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures) Apple HIG
- [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios) Apple HIG
- [Layout](https://fluent2.microsoft.design/layout) Fluent 2
- [Interaction and control](https://developer.samsung.com/one-ui/accessibility/interaction-and-control.html) Samsung One UI
- [Grid system](https://developer.samsung.com/one-ui/layout/grid.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta quando usar navegação por gestos, feedback de pressionado, densidade baixa no toque, áreas seguras para arrastar e as divergências sobre tamanho de alvo e botões do carrossel. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                              |

## Foco e seleção

O foco mostra qual elemento vai receber a próxima ação; o item ativo mostra onde a pessoa está; a seleção mostra sobre quais itens uma ação posterior vai agir.

Foco ajuda a pessoa a confirmar visualmente o objeto que a interação vai atingir ([HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)). O gov.br descreve o foco como o estado que surge quando a pessoa destaca um elemento interativo pelo teclado ou por voz, e por isso pede alta ênfase sobre os demais elementos da interface ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Quem navega com teclado, controle por varredura ou leitor de tela depende dele para saber onde está.

Ativo e selecionado são estados diferentes do foco e diferentes entre si. O gov.br resume a diferença: no ativo, a ação acontece logo após a escolha e só um item do conjunto fica ativo; no selecionado, a ação acontece depois, com outro controle, e a pessoa pode escolher um ou mais itens ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O Trama dá a cada estado uma aparência própria, para que os três possam aparecer juntos sem ambiguidade.

### Boas práticas

#### Indicador de foco

**Mostre sempre onde está o foco.** O Trama desenha um anel sólido de `--stroke-thick` (2 px) na cor `--t-focus`, afastado 2 px do elemento. O afastamento segue o gov.br, que pede um espaçamento de segurança para que a borda de foco não se confunda com outras propriedades do elemento nem com outros estados ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O token tem contraste acima de 3:1 contra todas as superfícies do Trama nos temas claro e escuro, conforme as Diretrizes de Acessibilidade para Conteúdo Web (WCAG) 2.2, critério 1.4.11. Dentro de `.tr-inverse`, o token troca para o valor do tema escuro, como o gov.br pede uma cor de foco diferente em fundo escuro ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

**Mostre o anel com teclado e voz, sem mostrá-lo no clique.** O gov.br define que clicar ou tocar não gera foco visual por padrão, enquanto o foco por teclado ou voz continua visível ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O Blueprint faz o mesmo e mantém a indicação em campos de texto, porque sempre importa saber onde se digita ([Blueprint](https://blueprintjs.com/docs/#core/accessibility)). O Trama usa `:focus-visible`: botões, links e controles não mostram o anel num clique, e campos de texto o mostram, como o gov.br define para o campo que recebe foco após o clique ([gov.br DS](https://www.gov.br/ds/components/input)).

**Use o foco tênue quando o sistema move o foco.** O gov.br define um foco de menor ênfase, sem espaçamento de segurança, para quando o elemento recebe foco de forma indireta, como ao focar automaticamente o campo de pesquisa ao abrir uma página de pesquisa, e para quando o foco padrão chamaria mais atenção do que deveria ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). No Trama, aplique `.tr-focus-subtle` (1 px, afastado 1 px) só nesses casos, e só com foco movido pelo sistema sem ação de teclado. Assim que a pessoa usar o teclado, o anel padrão volta.

**Use um único foco e um único estilo por vez.** Só pode existir um elemento com foco na tela, e cada elemento tem um só tipo de foco ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Componentes estendidos ou criados pelo produto usam o mesmo anel do kit. O GOV.UK dá orientação equivalente: usar os valores de foco do sistema em vez de valores numéricos próprios ([GOV.UK](https://design-system.service.gov.uk/get-started/focus-states/)).

**Não deixe o foco escondido.** Cabeçalhos fixos, barras inferiores e banners de cookies não podem cobrir o elemento em foco (WCAG 2.2, 2.4.11). Use `scroll-padding` com a altura das barras fixas e não deixe containers com `overflow: hidden` cortarem o anel.

> **Divergência entre referências** O gov.br desenha o foco como borda tracejada dourada, com cor diferente em fundo escuro ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O GOV.UK combina amarelo e preto com uma borda inferior grossa, para atender WCAG 2.2, 1.4.11 em qualquer fundo usado no GOV.UK ([GOV.UK](https://design-system.service.gov.uk/get-started/focus-states/)). A HIG descreve um anel ao redor do item ([HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)). Nenhuma fonte cita pesquisa sobre o estilo; as três cumprem 1.4.11 em seus fundos. O Trama mantém o anel sólido em `--t-focus`, que tem contraste acima de 3:1 em todas as suas superfícies, e adota do gov.br o afastamento de segurança e o foco tênue.

#### Ordem de foco

**Siga a ordem de leitura.** O Fluent pede que o foco siga um padrão em Z, da esquerda para a direita e de cima para baixo ([Fluent 2](https://fluent2.microsoft.design/accessibility)). A HIG descreve o mesmo percurso, do início ao fim da linha e de cima para baixo ([HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)). O gov.br pede, num card, que cada elemento receba foco em ordem lógica antes de passar ao card seguinte ([gov.br DS](https://www.gov.br/ds/components/card)). Em idiomas da direita para a esquerda, o Z se espelha. Veja Internacionalização e direita para esquerda.

**Mantenha o código na ordem visual.** Classes que reordenam só visualmente geram ordem de tabulação e de leitura incorretas ([Ontario](https://designsystem.ontario.ca/components/detail/grid.html)). Evite `order`, `flex-direction: row-reverse` e `tabindex` positivo para mudar a sequência.

**Não foque o que não é interativo.** Elementos decorativos e espaços vazios não precisam de foco ([One UI](https://developer.samsung.com/one-ui/accessibility/focus-order.html)). O gov.br pede que o foco não passe por divisores ([gov.br DS](https://www.gov.br/ds/components/divider)) nem pelos ícones decorativos do breadcrumb ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)). Um card inteiro clicável recebe um único foco.

**Use um ponto de Tab por grupo composto.** Em abas, radios, menus, barras de ferramentas, listas de opções e grades, Tab entra no grupo e as setas movem entre os itens ([HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)). Ao entrar no grupo, foque o item ativo ou selecionado e, se não houver, o primeiro. A navegação por setas para no último item, como no One UI ([One UI](https://developer.samsung.com/one-ui/accessibility/focus-order.html)), exceto em menus, onde ela dá a volta.

**Deixe o desabilitado fora do percurso, a menos que ele precise explicar algo.** O gov.br não deixa elementos desabilitados receberem foco ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). No Trama, controles com o atributo `disabled` ficam fora do percurso. Quando a pessoa pode habilitar o controle e a explicação está num tooltip, use `aria-disabled="true"`, que mantém o controle focável para que a explicação seja alcançada. Veja Estados de interação.

#### Foco inicial e gerenciamento

**Coloque o foco inicial no lugar certo.** O Trama define o foco inicial assim:

| Situação                                   | Foco inicial                                                                                                                  |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Página nova ou etapa nova de um fluxo      | Título `<h1>`, com `tabindex="-1"` e `.tr-focus-subtle`.                                                                      |
| Diálogo informativo                        | Botão Fechar, como no gov.br ([gov.br DS](https://www.gov.br/ds/components/modal)).                                           |
| Diálogo de ação                            | Primeiro campo; se não houver campo, a ação principal.                                                                        |
| Diálogo destrutivo                         | Ação segura (Cancelar), como no gov.br ([gov.br DS](https://www.gov.br/ds/components/modal)).                                 |
| Menu de navegação lateral aberto por botão | Botão Fechar, se houver, como no gov.br ([gov.br DS](https://www.gov.br/ds/components/menu)); se não houver, o primeiro item. |
| Formulário enviado com erros               | Resumo de erros.                                                                                                              |

**Não mova o foco sem uma ação da pessoa.** Mudar o foco sozinho obriga a pessoa a procurar onde ele foi parar ([HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)). Toasts e mensagens de status nunca roubam o foco; o Blueprint, por padrão, não move o foco para um toast ([Blueprint](https://blueprintjs.com/docs/#core/components/toast)). Use regiões `aria-live` para anunciar, conforme WCAG 2.2, 4.1.3.

**Devolva o foco ao fechar.** Ao fechar um diálogo, um drawer, um popover ou uma mensagem, devolva o foco ao elemento que estava focado antes, como pede o gov.br ([gov.br DS](https://www.gov.br/ds/components/modal)). O Fluent alerta que o foco não pode se perder quando uma interface temporária fecha ([Fluent 2](https://fluent2.microsoft.design/accessibility)).

**Quando o item em foco some, foque um vizinho.** Se a pessoa navega por teclado e o item em foco desaparece, mova o foco para um item próximo ([HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)). Depois de excluir uma linha, foque a linha seguinte ou, se era a última, a anterior.

> **Divergência entre referências** O gov.br pede foco no primeiro campo obrigatório de um formulário ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)), foco na ação principal de um diálogo de ação ([gov.br DS](https://www.gov.br/ds/components/modal)) e foco no botão Fechar de uma mensagem quando ela aparece ([gov.br DS](https://www.gov.br/ds/components/message)). A HIG pede não mover o foco sem ação da pessoa ([HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)), e o Blueprint não move o foco para toasts ([Blueprint](https://blueprintjs.com/docs/#core/components/toast)). Pelo critério de acessibilidade, o Trama decide: página e etapa novas focam o título, para que o leitor de tela anuncie o contexto antes da primeira pergunta; diálogos de ação focam o primeiro campo, porque a pessoa abriu o diálogo para preenchê-lo; mensagens de status são anunciadas sem mover o foco, conforme WCAG 2.2, 4.1.3. Uma mensagem só recebe foco quando resume erros de um envio.

#### Ativo e selecionado

**Use ativo para navegação e ação imediata.** Marque com `aria-current` a página atual, a aba visível e o item cujo conteúdo aparece no painel ao lado. Só um item ativo por conjunto, e o estado não vale para componentes em que vários itens podem estar abertos ao mesmo tempo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O ativo combina cor de fundo e primeiro plano com uma borda, para não depender só da cor; uma borda costuma bastar ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). No kit, é a barra de 3 px em `--t-brand` da navegação lateral e das abas.

**Use selecionado para coleções e ação posterior.** Marque com `aria-selected` ou `aria-checked` os itens sobre os quais a pessoa vai agir depois. O gov.br pede cor de fundo mais um elemento gráfico de seleção, como ícone de confirmação, checkbox ou radio ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). No kit, o item selecionado usa `--t-brand-subtle` e o rótulo "Selecionado". O gov.br não aplica o estado selecionado a navegação, diálogos, tooltips, botões, mensagens e divisores ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)); o Trama segue essa lista. As abas usam o atributo `aria-selected` exigido pelo padrão de abas, com a aparência de item ativo.

**Mantenha os estados exclusivos e respeite a interação direta.** Só pode haver um elemento com hover, um com foco e um pressionado por vez na tela, e um ativo por conjunto. Quando vários estados ocorrem juntos, todos aparecem, e o estado produzido pela interação direta da pessoa tem prioridade: num item de menu, o hover prevalece sobre o ativo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

**Ofereça seleção múltipla com controles visíveis.** Use checkboxes para selecionar várias linhas. Com teclado, Espaço marca o item em foco; com apontador, aceite também Shift com clique para intervalos e Mod com clique para itens avulsos. Em tabelas densas, o Blueprint permite navegar por células com as setas e expandir o intervalo com Shift e setas ([Blueprint](https://blueprintjs.com/docs/#table/features)), e o gov.br aceita setas entre caixas de seleção dentro de células ([gov.br DS](https://www.gov.br/ds/components/table)).

**Mostre quantos itens estão selecionados e o que se pode fazer.** Exiba a contagem e as ações da seleção numa barra de ferramentas e ofereça "Selecionar tudo" e "Limpar seleção". Preserve a seleção ao rolar e ao paginar, ou avise quando ela for perdida.

**Faça** combine fundo e barra lateral para marcar o item atual, sem depender só da cor.

**Não faça** indique o item atual ou a seleção só trocando a cor do texto.

### Considerações por plataforma

#### Web desktop

Seleção com Shift e Mod, seleção por arraste e atalhos como Mod+A são esperados em listas e tabelas. Veja Teclado e Mouse e trackpad.

#### Web móvel

Sem teclado físico, o foco aparece com leitores de tela, entrada por voz e teclados externos. Entre no modo de seleção múltipla com um botão "Selecionar" visível; o toque longo pode ser um atalho adicional.

#### Tablets e dobráveis

Mantenha foco, item ativo e seleção ao abrir, fechar ou redimensionar a tela. Ao passar de um para dois painéis, o item ativo na lista continua marcado e seu detalhe aparece no segundo painel. Veja Projetar para tablets e dobráveis.

### Recursos

#### Relacionados

- Estados de interação
- Teclado
- Mouse e trackpad
- Diálogos
- Tabelas
- Listas

#### Referências

- [Estados](https://www.gov.br/ds/fundamentos-visuais/estados) gov.br DS
- [Modal](https://www.gov.br/ds/components/modal) gov.br DS
- [Menu](https://www.gov.br/ds/components/menu) gov.br DS
- [Message](https://www.gov.br/ds/components/message) gov.br DS
- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Card](https://www.gov.br/ds/components/card) gov.br DS
- [Divider](https://www.gov.br/ds/components/divider) gov.br DS
- [Breadcrumb](https://www.gov.br/ds/components/breadcrumb) gov.br DS
- [Table](https://www.gov.br/ds/components/table) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) Apple HIG
- [Accessibility](https://fluent2.microsoft.design/accessibility) Fluent 2
- [Understanding focus state styles](https://design-system.service.gov.uk/get-started/focus-states/) GOV.UK Design System
- [Accessibility](https://blueprintjs.com/docs/#core/accessibility) Blueprint
- [Toast](https://blueprintjs.com/docs/#core/components/toast) Blueprint
- [Table features](https://blueprintjs.com/docs/#table/features) Blueprint
- [Focus order](https://developer.samsung.com/one-ui/accessibility/focus-order.html) Samsung One UI
- [Grid](https://designsystem.ontario.ca/components/detail/grid.html) Ontario Design System

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta foco tênue, foco só por teclado e voz, tabela de foco inicial, distinção entre ativo e selecionado, exclusividade de estados e as divergências sobre estilo de foco e foco inicial. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                  |

## Postura e dobra

Abrir, fechar e dobrar parcialmente um aparelho são entradas: a pessoa muda a forma da tela e espera que a interface acompanhe sem perder o contexto.

Dispositivos dobráveis podem ser usados fechados, abertos, parcialmente dobrados sobre uma mesa ou segurados como um livro. A HIG lista posturas como dobrado parcialmente como um livro, apoiado numa superfície ou em pé sobre as bordas, e lembra que a dobradiça também afeta o espaço disponível para o conteúdo ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)). O One UI pede que os apps funcionem bem com o aparelho aberto, fechado e parcialmente dobrado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

Para uma aplicação web, cada mudança de postura chega como um redimensionamento da janela e, em navegadores compatíveis, como uma mudança de segmentos da tela e de postura do aparelho. O Trama trata postura como entrada: a interface responde a ela, mantém o estado e nunca exige uma postura específica para concluir uma tarefa.

O Padrão Digital de Governo não tem orientação específica para dobráveis. Duas regras dele valem aqui: um ponto de quebra não indica o aparelho, e a interface precisa funcionar quando a pessoa gira o tablet ou muda a área útil do navegador ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)); e movimentos abruptos podem causar confusão e sobrecarga cognitiva ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)). As demais regras desta página vêm do One UI e da HIG.

### Posturas

| Postura                                   | Como a pessoa usa                                      | Comportamento no Trama                                                           |
|-------------------------------------------|--------------------------------------------------------|----------------------------------------------------------------------------------|
| Fechado                                   | Tela externa, uma mão, tarefas rápidas.                | Classe Compacta, um painel, barra inferior.                                      |
| Aberto plano                              | Tela interna, duas mãos, leitura e produtividade.      | Classe Média ou Expandida, dois painéis em 50:50, rail lateral, densidade baixa. |
| Meio dobrado na horizontal (sobre a mesa) | Aparelho apoiado, mãos livres: vídeo, chamada, câmera. | Conteúdo na metade superior, controles na metade inferior.                       |
| Meio dobrado na vertical (livro)          | Segurado com as duas mãos: leitura, comparação.        | Um painel de cada lado da dobra.                                                 |

### Boas práticas

**Adapte o layout ao espaço, sem criar um layout por postura.** Apoiar várias posturas não significa projetar um layout para cada uma. Use classes de tamanho para que o app se adapte naturalmente: um layout de largura compacta para a tela externa e um de largura regular para a interna cobrem o essencial de todas as posturas ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)). No Trama, as classes de janela fazem esse papel; a postura só refina a distribuição do conteúdo.

**Ajuste automaticamente ao dobrar.** Os apps devem se ajustar sozinhos quando o aparelho é parcialmente dobrado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Nunca peça que a pessoa toque num botão para trocar de modo.

**No modo sobre a mesa, conteúdo em cima e controles embaixo.** No modo Flex, a parte de cima, inclinada para a pessoa, mostra o conteúdo, e a parte de baixo, apoiada na mesa, mostra os controles e botões ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Aplique a regra a players de vídeo, chamadas, câmera, apresentação de slides e leitura de receitas.

**Mantenha elementos interativos longe da dobra.** Evite posicionar elementos interativos perto do vinco no meio da tela ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Com o aparelho parcialmente aberto, a região da dobra divide a tela em áreas utilizáveis e fica excluída ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)). Reserve uma faixa sem texto nem controles sobre a dobra, e não deixe diálogos, menus ou popovers atravessarem a dobra: posicione-os inteiros numa das metades.

**Divida grades e painéis de forma simétrica.** Em layouts de grade, prefira número par de colunas para que o conteúdo se divida bem; prefira containers que ajustam a largura de cada painel para continuar visível quando o aparelho dobra ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)). Use `.tr-panes--50` com o aparelho aberto.

**Escolha a divisão pela forma da área.** A HIG descreve um arranjo em que dois conteúdos se dividem lado a lado quando a área é mais larga que alta e um sobre o outro quando é mais alta que larga; e outro em que, com o aparelho parcialmente dobrado, cada conteúdo ocupa um lado da dobra ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)). No Trama, uma lista e seu detalhe ficam lado a lado no modo livro e um acima do outro no modo sobre a mesa.

**Evite mudanças bruscas.** Mova só o necessário para manter os elementos visíveis e fáceis de tocar; prefira pequenos ajustes a rearranjos ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)). Mantenha as posições relativas dos controles parecidas entre posturas, para que a pessoa não precise reaprender onde ficam as ações ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)).

**Mostre uma transição curta ao entrar e sair do modo dobrado.** O One UI pede um efeito visual de transição ao mudar para o modo Flex e ao sair dele ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). O gov.br pede considerar movimentos simplificados ou reduzidos em celulares e tablets e oferecer uma opção explícita para ativar ou desativar animações ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)). Use `--m-slow` com `--m-ease-standard` e troque por mudança instantânea quando `prefers-reduced-motion` estiver ativo ou quando a pessoa desligar as animações no produto.

**Nem toda tela precisa mudar.** Algumas telas não precisam de outro layout com o aparelho parcialmente dobrado, como uma lista de configurações ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Reserve o layout dividido para telas em que a pessoa assiste ou opera algo com as mãos livres.

**Mantenha os controles tocáveis em qualquer postura.** No modo sobre a mesa, a pessoa toca a metade de baixo com o aparelho apoiado e, às vezes, de longe. Use densidade baixa (`data-density="baixa"`) e alvos de `--c-touch` na área de controles, e mantenha o estado pressionado visível com `--o-pressed`, porque não há hover para confirmar o alvo. Veja Densidade.

**Preserve o estado em qualquer mudança de postura.** Mantenha posição de rolagem, texto digitado, teclado aberto e item selecionado ao trocar de tela ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Mantenha as mesmas funções em todas as posturas ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)). Não reproduza nem pause mídia por causa de uma mudança de postura. Mantenha o mesmo item em foco e o mesmo item ativo; se o elemento em foco saiu da tela, foque o vizinho mais próximo. Veja Foco e seleção.

**Faça** deixe uma faixa livre sobre a dobra e posicione controles inteiros numa metade.

**Não faça** coloque um botão ou campo cortado pela dobra.

### Acessibilidade

Postura nunca pode ser o único jeito de acessar uma função: tudo o que o modo dobrado oferece também está disponível com o aparelho aberto ou fechado. Mudanças de layout não podem mover o foco nem disparar anúncios desnecessários no leitor de tela. Não trave a orientação da tela, conforme as Diretrizes de Acessibilidade para Conteúdo Web (WCAG) 2.2, critério 1.3.4. O gov.br lembra que a acessibilidade de serviços públicos digitais inclui dispositivos móveis, por força da Lei nº 14.129/2021 ([gov.br DS](https://www.gov.br/ds/acessibilidade)).

### Considerações por plataforma

#### Web desktop

Nenhuma consideração adicional para Web desktop.

#### Web móvel

Celulares comuns não mudam de postura. A tela externa dos dobráveis e os Flip fechados seguem web móvel.

#### Tablets e dobráveis

Detecte o espaço com as classes de janela e refine pela postura quando o navegador oferecer suporte. Navegadores baseados em Chromium expõem a Device Posture API (media query `device-posture`, com os valores `continuous` e `folded`) e as media queries de segmentos de tela (`horizontal-viewport-segments` e `vertical-viewport-segments`). Use-as como aprimoramento progressivo e confira o suporte atual antes de depender delas.

``` code
/* Meio dobrado sobre a mesa: dois segmentos, um acima do outro */
@media (device-posture: folded) and (vertical-viewport-segments: 2) {
  .player {
    grid-template-rows:
      env(viewport-segment-height 0 0)
      env(viewport-segment-height 0 1);
    row-gap: calc(env(viewport-segment-top 0 1) - env(viewport-segment-bottom 0 0));
  }
}
```

### Recursos

#### Relacionados

- Projetar para tablets e dobráveis
- Painéis e split view
- Toque e gestos
- Movimento
- Densidade
- Layout e grid

#### Referências

- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI
- [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) Apple HIG
- [Grid](https://www.gov.br/ds/fundamentos-visuais/grid) gov.br DS
- [Movimento](https://www.gov.br/ds/fundamentos-visuais/movimento) gov.br DS
- [Acessibilidade](https://www.gov.br/ds/acessibilidade) gov.br DS

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                            |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta controle explícito de animações na transição de postura, densidade baixa e estado pressionado na área de controles e preservação de foco e item ativo. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                     |

