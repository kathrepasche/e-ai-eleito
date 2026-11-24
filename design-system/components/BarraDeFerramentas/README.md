# BarraDeFerramentas

Uma barra de ferramentas reúne, numa linha, os comandos mais usados sobre o conteúdo da vista atual.

A barra de ferramentas age sobre o conteúdo da vista, ajuda a navegar e orienta a pessoa. Ela pode conter o título da vista, controles de navegação e pesquisa, e ações como botões e menus ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)). No Trama, a barra é um `.tr-toolbar` com botões sutis, separadores `.tr-toolbar__sep` e, quando necessário, um botão “Mais opções” no fim. O gov.br não tem um componente de barra de ferramentas; o Trama aplica aqui as regras do botão circular, do comportamento de alternância e das densidades do botão do gov.br ([gov.br DS](https://www.gov.br/ds/components/button)) e o padrão dropdown para o menu de excedentes ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)).

**Quando usar.** Em editores, listas com seleção, tabelas e visualizadores, para dar acesso rápido a ações frequentes relacionadas à tarefa atual ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage)). Também como barra de ações que aparece depois que a pessoa seleciona itens, para mover, editar ou excluir ([One UI](https://developer.samsung.com/one-ui/comp/bottom-bar.html)).

**Quando não usar.** Para navegar entre áreas da aplicação, use a barra de navegação ou a navegação lateral ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)). Para alternar entre vistas irmãs de uma página, use abas. Para uma ou duas ações no fim de um formulário, use um grupo de botões.

## Anatomia

1.  **Contêiner** (`.tr-toolbar`): linha com fundo `--t-surface-raised`, borda `--t-border-subtle`, raio `--r-lg` e espaço interno `--sp-100`.
2.  **Grupos**: conjuntos de comandos relacionados por função.
3.  **Separador** (`.tr-toolbar__sep`): linha vertical de 1px entre grupos.
4.  **Itens**: botões sutis, de ícone (`.tr-btn--icon`, quadrados para alinhar o grupo) ou com rótulo; botões de alternância com `aria-pressed`; botões que abrem menus. Na barra da vista, ações isoladas no fim, como pesquisar ou mais opções, usam o botão circular `.tr-btn--circle`.
5.  **Menu de excedentes**: botão “Mais opções” no fim, que recebe os itens que não cabem.
6.  **Ação primária** (opcional): uma só, na borda final.

## Tipos

| Tipo             | Posição                         | Uso                                                                                                                                                                                 |
|------------------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Barra da vista   | Topo do conteúdo, fixa          | Título, navegação e ações da vista. Equivale à barra de aplicativo do One UI, com título, ações e “Mais opções” ([One UI](https://developer.samsung.com/one-ui/comp/app-bar.html)). |
| Barra de edição  | Fixa acima de um editor         | Formatação e inserção, agrupadas por função ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage)).                                                   |
| Barra de seleção | Topo da lista ou base da tela   | Aparece quando há itens selecionados e mostra quantos são.                                                                                                                          |
| Barra inferior   | Base da tela na classe Compacta | Até cinco ações com ícone e texto. Não use com uma ação só ([One UI](https://developer.samsung.com/one-ui/comp/bottom-bar.html)).                                                   |

## Boas práticas

**Escolha os itens com cuidado.** Cada item precisa ser distinguível e fácil de acionar. Priorize os comandos que as pessoas mais usam ou os que agem sobre os objetos mais importantes ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage)).

**Agrupe por função e frequência e limite os grupos.** Coloque negrito, itálico e sublinhado juntos e separe-os de recuo e listas ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage)). Procure ter no máximo três grupos ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)).

**Organize em três regiões.** No início, voltar, mostrar ou ocultar a barra lateral e o título. No centro, os comandos comuns, que são os primeiros a ir para o menu de excedentes. No fim, os itens que precisam ficar sempre visíveis, a pesquisa, o “Mais opções” e a ação primária ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)).

**Tenha no máximo uma ação primária, na borda final.** Use `.tr-btn--primary` para ações como Publicar ou Concluir; todo o resto usa `.tr-btn--subtle` ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)). Botões sem fundo evitam camadas desnecessárias dentro da barra ([One UI](https://developer.samsung.com/one-ui/comp/button.html)).

**Separe ações destrutivas ou que mudam o status.** Mantenha-as afastadas das outras opções, com um separador ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage)).

**Separe botões com texto de botões com ícone.** Um botão com rótulo encostado num botão de ícone parece uma ação só, e rótulos vizinhos parecem se juntar. Use separador ou espaço ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)).

**Use texto para ações difíceis de representar com ícone.** Ícones economizam espaço quando são familiares. Para ações como “Inserir tabela”, prefira texto ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars), [Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage)).

**Não torne a barra o único lugar de um comando.** Se a pessoa pode ocultar a barra, os comandos dela precisam existir em outro lugar, como num menu ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)).

**Faça** Use poucos itens com rótulos claros e isole a ação destrutiva com um separador.

**Não faça** Encha a barra de botões com contorno, use mais de um primário e deixe a ação destrutiva colada às demais.

### Estados

Os itens herdam os estados do botão: hover e pressionado são camadas `--o-hover` e `--o-pressed` sobre a cor do item. Botões de alternância, como Negrito, mantêm o rótulo fixo e informam o estado com `aria-pressed` ([gov.br DS](https://www.gov.br/ds/components/button)); o estado ligado mantém a camada de hover e precisa de uma mudança visível além da cor ([Fluent](https://fluent2.microsoft.design/components/web/react/core/button/usage)). O botão que abriu o menu de excedentes também mantém essa camada enquanto o menu está aberto ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)).

**Comandos que dependem da seleção.** Se a pessoa pode habilitar o comando por uma ação dela, como selecionar um trecho antes de “Inserir link”, mostre o item com `aria-disabled="true"`, no mesmo lugar, para a barra não mudar de forma, e explique o motivo no tooltip focável, como “Selecione um trecho para inserir link”. Comandos que a pessoa nunca poderá usar, por falta de permissão, saem da barra (decisão D9).

### Comportamento

**Não quebre a barra em duas linhas nem trunque rótulos.** A barra cresce até a largura do contêiner. Quando faltar espaço, os últimos itens do centro vão para o menu “Mais opções”, cada um com ícone e rótulo de texto ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage)). Defina de antemão a ordem em que os itens saem ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)). Evite layouts em que itens já começam no menu de excedentes na largura padrão. Rótulos nunca recebem reticências: o item inteiro vai para o menu (decisão D15). O menu de excedentes segue as regras de Menus.

**Permita ocultar quando a barra não apoia a tarefa principal.** Ofereça uma forma confiável de trazê-la de volta ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage), [HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)).

**Considere permitir personalização.** Em aplicações de uso longo e com muitos comandos, deixe a pessoa escolher os itens da barra ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)).

## Conteúdo

Rótulos e tooltips curtos, que dizem o resultado da ação, com verbo no infinitivo, até duas palavras e sem artigo ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)), em caixa de frase e sem ponto final ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage)). O título da vista é uma palavra ou expressão curta; a HIG recomenda menos de 15 caracteres para deixar espaço aos controles e pede para não usar o nome da aplicação como título ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)). Use o ícone padrão de voltar e de fechar, sem escrever “Voltar” ao lado ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)); o nome acessível desses botões é “Voltar” e “Fechar”.

## Acessibilidade

**Use o padrão de barra de ferramentas do WAI-ARIA.** `role="toolbar"` no contêiner e um nome com `aria-label` ou `aria-labelledby`, obrigatório quando há mais de uma barra na página ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage)).

**Uma parada de Tab para a barra inteira.** Tab entra na barra e foca o último item usado; setas para a esquerda e para a direita movem entre os itens; Home e End vão ao primeiro e ao último; Tab sai da barra.

**Nomeie cada botão de ícone.** Ofereça tooltip com o texto no hover e no foco e `aria-label` para leitores de tela ([gov.br DS](https://www.gov.br/ds/components/button), [Fluent](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage)). Ícones ao lado de rótulos levam `aria-hidden="true"` ([gov.br DS](https://www.gov.br/ds/components/button)).

**Anuncie mudanças de estado.** Botões de alternância comunicam o estado atual e o resultado da ação, com texto e uma mudança visível como ícone ou cor ([Fluent](https://fluent2.microsoft.design/components/web/react/core/button/usage)).

## Tokens usados

| Token                      | Uso                                 |
|----------------------------|-------------------------------------|
| `--t-surface-raised`       | Fundo da barra                      |
| `--t-border-subtle`        | Borda da barra e separadores        |
| `--r-lg`                   | Raio da barra                       |
| `--sp-100`                 | Espaço interno e espaço entre itens |
| `--c-h-sm`, `--d-control`  | Altura dos itens por densidade      |
| `--o-hover`, `--o-pressed` | Hover, pressionado e estado ligado  |
| `--t-brand`                | Ação primária                       |

## Considerações por plataforma

### Web desktop

Use densidade alta (`data-density="alta"`, itens de `--c-h-sm`) em barras de editores e tabelas operadas com mouse. Mostre tooltips em todos os botões de ícone. A barra pode ficar fixa no topo enquanto o conteúdo rola.

### Web móvel

Mantenha só os itens essenciais visíveis e leve o resto para o “Mais opções” ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)). Na barra do topo, use no máximo três botões de ação ([One UI](https://developer.samsung.com/one-ui/comp/app-bar.html)). Ações sobre itens selecionados podem ir para uma barra na base da tela, ao alcance do polegar, com até cinco ações com ícone e texto; com mais, mostre as quatro mais usadas e ponha o resto no “Mais opções” ([One UI](https://developer.samsung.com/one-ui/comp/bottom-bar.html)). Use densidade baixa, com área de ação de `--c-touch`, e ícones fortemente reconhecíveis, já que não há tooltip por hover ([gov.br DS](https://www.gov.br/ds/components/button)).

### Tablets e dobráveis

Com mais largura, mais itens cabem fora do menu de excedentes; recalcule a distribuição a cada mudança de classe de janela, incluindo ao abrir e fechar um dobrável. Em dobráveis parcialmente dobrados, posicione a barra na metade de baixo e o conteúdo na de cima ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). A barra pode dividir o espaço horizontal com a navegação por abas no topo ([HIG](https://developer.apple.com/design/human-interface-guidelines/toolbars)).

## Recursos

### Relacionados

- Botões
- Menus
- Campo de pesquisa
- Tooltips
- Barra de navegação e rail

### Referências

- [Button (Botão)](https://www.gov.br/ds/components/button) gov.br DS
- [Dropdown (Elemento Flutuante)](https://www.gov.br/ds/padroes/design/dropdown) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) Apple HIG
- [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) Apple HIG
- [Toolbar: usage](https://fluent2.microsoft.design/components/web/react/core/toolbar/usage) Fluent 2
- [Button: usage](https://fluent2.microsoft.design/components/web/react/core/button/usage) Fluent 2
- [Button group](https://blueprintjs.com/docs/#core/components/button-group) Blueprint
- [App bar](https://developer.samsung.com/one-ui/comp/app-bar.html) Samsung One UI
- [Bottom bar](https://developer.samsung.com/one-ui/comp/bottom-bar.html) Samsung One UI
- [Buttons](https://developer.samsung.com/one-ui/comp/button.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                           |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta densidades, botão circular na barra da vista, alternância com rótulo fixo e `aria-pressed`, comandos dependentes da seleção com explicação (D9) e proibição de truncar rótulos (D15). |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                    |
