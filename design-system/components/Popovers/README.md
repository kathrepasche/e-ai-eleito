# Popovers

Um popover é uma superfície transitória que surge junto ao controle que a pessoa acionou, com pouca informação ou poucas ações ligadas a ele.

O popover aparece sobre o conteúdo quando a pessoa clica ou toca num controle e desaparece quando ela interage fora dele, fecha ou conclui a escolha ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/popovers)). Ele economiza espaço: em vez de reservar uma coluna para opções usadas de vez em quando, o Trama as mostra só quando necessárias, perto de onde a pessoa está olhando. O gov.br DS trata esse componente como o tipo popover do tooltip: fica visível até ser fechado e aceita conteúdo formatado, imagens e elementos interativos ([gov.br DS](https://www.gov.br/ds/components/tooltip)).

**Use um popover** para editar um atributo de um item sem sair da tela (mudar a data de um evento, escolher uma cor), mostrar um resumo de uma entidade, oferecer um pequeno conjunto de controles relacionados ou listar as notificações da conta.

**Não use um popover** para avisos: a pessoa pode não ver ou fechar sem querer; use um diálogo ou uma mensagem ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/popovers)). Para texto curto sem estrutura, use um tooltip. Para layouts complexos ou que precisam bloquear a página, use um diálogo ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/popover/usage)). Para uma lista de comandos, use um menu. Não coloque no popover informação essencial para concluir a tarefa; o gov.br pede que o mesmo conteúdo tenha sempre outro caminho de acesso ([gov.br DS](https://www.gov.br/ds/components/tooltip)).

## Anatomia

1.  **Gatilho**: botão ou área interativa que abre o popover e indica o estado com `aria-expanded`.
2.  **Seta**: aponta para o gatilho, centralizada no lado do balão em que aparece ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/popovers), [gov.br DS](https://www.gov.br/ds/components/tooltip)).
3.  **Superfície**: `--t-surface-raised`, raio `--r-lg`, elevação `--e-4`, preenchimento `--sp-400`, largura máxima de 280px, na camada `--z-2`.
4.  **Conteúdo**: título opcional, texto curto, controles e, se preciso, um link "Saiba mais" no fim ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/popover/usage)).
5.  **Botão Fechar**: no canto superior direito dos popovers informativos ([gov.br DS](https://www.gov.br/ds/components/tooltip)). No popover de ação, Cancelar cumpre o papel.
6.  **Ações** (opcionais): Cancelar e Salvar, alinhadas ao fim, só quando esclarecem se a alteração será mantida.

## Tipos

| Tipo                   | Abre com                                                               | Uso                                                                                |
|------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Popover de ação        | Clique, toque ou Enter no gatilho.                                     | Editar atributos, escolher opções, formulário de um ou dois campos.                |
| Popover informativo    | Clique, toque ou Enter no gatilho.                                     | Detalhe com formatação, imagem ou um link, com botão Fechar.                       |
| Cartão de contexto     | Hover ou foco no gatilho, com atraso de cerca de 150ms.                | Metadados de uma pessoa, projeto ou item numa lista densa, com no máximo uma ação. |
| Painel de notificações | Clique no acionador do cabeçalho, como um ícone ou o avatar com badge. | Lista cronológica das notificações da conta.                                       |

O cartão de contexto segue o Context Card do [Geist](https://vercel.com/geist/context-card): ele pode fechar quando o cursor sai, por isso nunca contém ações destrutivas.

### Painel de notificações

O painel agrupa os avisos do sistema em ordem cronológica, do mais recente para o mais antigo ([gov.br DS](https://www.gov.br/ds/components/notification)). Ele tem, de cima para baixo:

- **Área do usuário** (opcional): nome e e-mail, útil quando o painel abre pelo avatar, com o botão Fechar no topo à direita.
- **Abas** (opcionais): separam categorias, como "Todas" e "Não lidas".
- **Itens**: marca de não lida, título, data e hora, e o conteúdo total ou parcial, separados por divisores.

Nas classes Expandida em diante, o painel ocupa no máximo metade da largura de conteúdo e nunca passa da altura visível. Só a lista de itens rola; área do usuário e abas ficam fixas ([gov.br DS](https://www.gov.br/ds/components/notification)). Na classe Compacta, o painel ocupa a tela toda, com botão Fechar obrigatório e a rolagem nativa da página, sem rolagem interna ([gov.br DS](https://www.gov.br/ds/components/notification)).

## Boas práticas

**Abra o popover só por ação da pessoa.** Clique, toque, Enter ou foco no gatilho. O Trama não abre popovers automaticamente; para apresentar uma novidade, use o padrão de onboarding.

**Mostre um popover por vez.** Nunca abra um popover a partir de outro. Se outro precisa abrir, feche o atual; e permita trocar de um para outro com um único clique quando vários botões de uma barra abrem popovers ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/popovers), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/popover/usage)).

**Não cubra o gatilho nem o conteúdo que a pessoa precisa ver.** Posicione o popover do lado com mais espaço e inverta o lado quando a borda da janela se aproxima: abaixo do gatilho perto do topo, acima perto da base, à direita perto da borda esquerda e à esquerda perto da borda direita ([Blueprint](https://blueprintjs.com/docs/#core/components/popover), [gov.br DS](https://www.gov.br/ds/components/tooltip)).

**Dimensione pelo conteúdo.** O popover tem apenas o tamanho necessário. Se o conteúdo transborda, role só na vertical ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/popover/usage)). Se ele cresce demais, é sinal de que pertence a um drawer ou a uma página.

**Salve o trabalho ao fechar por clique fora.** A pessoa pode fechar sem querer. Descarte alterações apenas quando ela escolhe Cancelar ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/popovers)).

**Anime mudanças de tamanho.** Se o popover expande, anime a transição em `--m-normal` para não parecer que outro popover substituiu o primeiro ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/popovers)).

**Deixe a pessoa decidir se quer notificações.** Ofereça nas configurações a escolha de receber ou não cada tipo, e evite o excesso de avisos ([gov.br DS](https://www.gov.br/ds/components/notification)).

> **Divergência entre referências** O gov.br DS permite que o popover apareça automaticamente, programado pelo sistema, e alerta que esse uso pode causar problemas de acessibilidade. A Apple HIG descreve o popover como resposta ao clique ou toque num controle. Pelo critério de acessibilidade, o Trama abre popovers apenas por ação da pessoa: um balão que surge sozinho cobre conteúdo sem pedido e não tem relação clara com o foco atual de quem usa leitor de tela. Do gov.br, o Trama adota o botão Fechar nos popovers informativos, porque ele dá uma saída visível a quem usa toque ou mouse.

**Faça** mostre pouco conteúdo, com um caminho para saber mais.

**Não faça** use o popover para um aviso crítico que a pessoa pode não ver.

### Estados e comportamento

- **Fechamento**: botão Fechar, clique fora, Esc, novo clique no gatilho ou seleção de um item. Se várias seleções são possíveis, o popover só fecha com clique fora ou ação explícita ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/popovers), [gov.br DS](https://www.gov.br/ds/components/notification)).
- **Gatilho desativado**: um `<button disabled>` não recebe eventos; use `aria-disabled="true"` e explique perto do gatilho por que ele está indisponível ([Blueprint](https://blueprintjs.com/docs/#core/components/popover)).
- **Camada**: popovers, menus e o painel de notificações ficam em `--z-2`, abaixo do cabeçalho fixo. Um diálogo aberto a partir do popover fecha o popover antes.
- **Itens de notificação**: seguem os estados de item de lista, com hover, foco e marca de não lida em texto ([gov.br DS](https://www.gov.br/ds/components/notification)).
- **Movimento**: entrada em `--m-fast` com `--m-ease-enter`; sem animação com `prefers-reduced-motion` ou com as animações desligadas no produto.

## Conteúdo

**Use frases curtas ou fragmentos.** Não repita o que já está na tela ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/popover/usage)).

**Não diga "popover" em textos de ajuda.** Refira-se à tarefa: "Escolha o lembrete" em vez de "Use o popover de lembrete" ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/popovers)).

**Escreva notificações com título claro e data.** O título diz o que aconteceu; a data situa o item na linha do tempo ([gov.br DS](https://www.gov.br/ds/components/notification)). Nunca trunque o texto da notificação: quebre a linha ou mostre o resumo e leve ao detalhe.

**Leve "Saiba mais" a outro painel ou página.** Assim o popover não tira a pessoa da tarefa sem aviso ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/popover/usage)). Se abrir em nova aba, diga "(abre em nova aba)" no texto do link.

## Acessibilidade

- O gatilho é um `<button>` com `aria-expanded` e `aria-controls`. O popover com controles usa `role="dialog"` e `aria-labelledby`.
- Ao abrir pelo teclado, mova o foco para o primeiro controle. Esc fecha e devolve o foco ao gatilho ([Geist](https://vercel.com/geist/context-card)).
- Se o popover prende o foco, o resto da página fica oculto para tecnologias assistivas até o fechamento ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/popover/usage)).
- No painel de notificações, Tab e Shift+Tab percorrem os controles e Enter ou Espaço os acionam ([gov.br DS](https://www.gov.br/ds/components/notification)). A contagem de não lidas entra no nome do acionador: "Notificações, 2 não lidas".
- O cartão de contexto que abre por hover também abre por foco, e a pessoa pode mover o ponteiro até ele sem que feche (WCAG 2.2, 1.4.13).

## Tokens usados

| Elemento                 | Token                                                         |
|--------------------------|---------------------------------------------------------------|
| Superfície e seta        | `--t-surface-raised`, contorno da seta em `--t-border-subtle` |
| Raio                     | `--r-lg`                                                      |
| Elevação e camada        | `--e-4`, `--z-2`                                              |
| Preenchimento            | `--sp-400`                                                    |
| Distância do gatilho     | `--sp-200`                                                    |
| Texto                    | `--t-fg-1`, Body small 14/20                                  |
| Divisores de notificação | `--t-border-subtle`                                           |
| Movimento                | `--m-fast`, `--m-normal`, `--m-ease-enter`                    |

## Considerações por plataforma

### Web desktop

O cartão de contexto por hover existe apenas com ponteiro. Popovers de ação abrem por clique e respondem ao teclado. Mantenha o popover dentro da janela ao redimensionar, invertendo o lado quando necessário.

### Web móvel

Na classe Compacta, não use popovers de ação: apresente o mesmo conteúdo numa folha inferior, que aproveita a largura da tela ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/popovers)). O painel de notificações ocupa a tela toda, com Fechar ([gov.br DS](https://www.gov.br/ds/components/notification)). Cartões de contexto não têm equivalente por toque; leve a informação para a página de detalhe.

### Tablets e dobráveis

A partir da classe Média, prefira o popover a uma tela cheia para entradas pequenas. Faça o popover surgir perto do botão que a pessoa tocou: isso reduz o deslocamento do dedo e mantém o contexto anterior visível ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Quando o dobrável fecha e a janela cai para Compacta, converta o popover aberto em folha inferior, preservando o que foi digitado.

## Recursos

### Relacionados

- Tooltips
- Menus
- Diálogos
- Drawers e folhas laterais
- Notificações
- Oferecer ajuda

### Referências

- [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers) Apple HIG
- [Tooltip (tipo popover)](https://www.gov.br/ds/components/tooltip) gov.br DS
- [Notification](https://www.gov.br/ds/components/notification) gov.br DS
- [Popover](https://fluent2.microsoft.design/components/web/react/core/popover/usage) Fluent 2
- [Popover](https://blueprintjs.com/docs/#core/components/popover) Blueprint
- [Context Card](https://vercel.com/geist/context-card) Geist
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o popover informativo com Fechar e o painel de notificações, define a inversão de lado perto da borda, a camada e a ordem das ações, e proíbe a abertura automática. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                   |
