# DrawersEFolhasLaterais

Um drawer é uma superfície secundária que desliza de uma borda da tela para mostrar detalhes, filtros ou uma tarefa curta ligada à página atual.

O drawer mantém a página principal à vista. Você inspeciona uma linha da tabela, ajusta filtros ou edita um item e volta ao ponto onde estava. No Trama, ele pode se sobrepor à página (com ou sem véu) ou ocupar espaço ao lado dela, como uma coluna que se abre. No celular, a mesma função aparece como folha inferior.

**Use um drawer** para detalhes de um item selecionado (inspetor), filtros de uma lista, configurações que afetam o conteúdo visível e tarefas de uma ou duas etapas que dependem do contexto da página ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/drawer/usage), [Geist](https://vercel.com/geist/sheet)).

**Não use um drawer** para confirmar ações destrutivas: sem um bloqueio completo da página, o sinal de gravidade fica fraco; use um diálogo ([Geist](https://vercel.com/geist/drawer)). Para uma informação breve, use tooltip ou popover. Para a lista de notificações aberta a partir do cabeçalho, use o painel de notificações descrito em Popovers. Para fluxos longos, use uma página. Para navegação principal permanente, use a navegação lateral.

## Anatomia

1.  **Cabeçalho** (obrigatório): título e botão Fechar, com ações rápidas opcionais. Divisor em `--t-border-subtle`.
2.  **Corpo** (obrigatório): listas, resumos ou campos. É a única área que rola, sempre na vertical.
3.  **Rodapé** (opcional): até duas ações, alinhadas ao fim, com a principal por último, à direita.
4.  **Véu** (apenas no modo modal): scrim de foco em `--t-overlay`.

Cabeçalho e rodapé ficam fixos quando o corpo rola, e uma sombra marca a divisão sempre que há conteúdo oculto acima ou abaixo, como no diálogo com rolagem ([gov.br DS](https://www.gov.br/ds/components/modal)). Em zoom alto ou viewport pequena, deixam de ser fixos para liberar espaço de leitura ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/drawer/usage)).

## Tipos

| Tipo                 | Comportamento                                                 | Camada  | Quando usar                                                                         |
|----------------------|---------------------------------------------------------------|---------|-------------------------------------------------------------------------------------|
| Sobreposto não modal | Cobre parte da página, sem véu. A página continua interativa. | `--z-3` | Inspetor de itens, carrinho.                                                        |
| Sobreposto modal     | Cobre a página com véu e prende o foco.                       | `--z-4` | Tarefa curta que precisa de atenção total, como um formulário de filtro no celular. |
| Em linha             | Abre ao lado do conteúdo e reduz a largura da área principal. | `--z-0` | Quando a pessoa precisa ver e usar as duas áreas ao mesmo tempo.                    |
| Folha inferior       | Sobe da borda inferior na classe Compacta.                    | `--z-4` | Filtros, escolha de opções e ações curtas no celular.                               |

A divisão entre em linha e sobreposto segue o [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/drawer/usage). A folha inferior restrita a telas pequenas segue o [Geist](https://vercel.com/geist/drawer). As camadas seguem a escala do Trama: o drawer não modal se comporta como navegação flutuante e o modal divide a camada dos diálogos, com a elevação `--e-5`.

O Trama define três larguras para drawers laterais: pequena (360px, padrão), média (50% da janela) e grande (90%). Os valores vêm das constantes do [Blueprint](https://blueprintjs.com/docs/#core/components/drawer). Evite a largura de tela cheia quando a pessoa precisa consultar a página ao lado.

## Boas práticas

**Escolha a borda pela origem da ação e mantenha-a.** Inspetores de linha entram pela direita; filtros globais e navegação, pela esquerda. Não troque de lado durante a sessão ([Geist](https://vercel.com/geist/sheet), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/drawer/usage)).

**Prefira o modo não modal para conteúdo de consulta.** Reserve o véu para tarefas importantes, claras e rápidas ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/drawer/usage)). Um inspetor que atualiza o conteúdo conforme a seleção muda é mais útil quando a lista continua clicável ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/panels)).

**Abra um drawer por vez.** Fechar um drawer devolve a pessoa à página, nunca a outro drawer. Se uma ação exige outra superfície, feche o primeiro ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/sheets)).

**Limite tarefas a duas ou três etapas.** Fluxos maiores pedem uma superfície mais focada, como uma página ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/drawer/usage)).

**Alinhe as ações ao fim, com a principal por último.** Na barra de ações do drawer, como nos diálogos, a ação secundária vem primeiro e a principal fica à direita. No celular, com os botões empilhados, a principal fica em cima.

**Ofereça sempre uma saída explícita.** No modo não modal, o clique fora não fecha o drawer; por isso o botão Fechar é obrigatório e Esc também fecha ([Geist](https://vercel.com/geist/sheet)). Se houver uma ação de envio, acompanhe-a de Cancelar ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/sheets)).

**Nunca role na horizontal.** O corpo do drawer rola só na vertical. Tabelas largas dentro dele indicam que o conteúdo pertence a uma página ([gov.br DS](https://www.gov.br/ds/components/modal)).

> **Divergência entre referências** O Fluent 2 coloca o botão primário primeiro, à esquerda, no rodapé do drawer. O gov.br DS alinha os botões do modal à direita. Nenhum critério de evidência ou acessibilidade separa as duas posições; o Trama trata o drawer como os diálogos, para que a pessoa encontre a ação principal sempre no mesmo lugar nas superfícies sobrepostas: ações ao fim, principal por último (decisão D4). A versão 1.0 seguia o Fluent 2.

**Faça** use o drawer para uma tarefa curta ligada à lista que continua visível.

**Não faça** confirme uma ação destrutiva num drawer, sem saída e sem bloqueio da página.

### Estados e comportamento

- **Abertura e fechamento**: desliza da borda em `--m-slow` com `--m-ease-enter` e sai em `--m-normal` com `--m-ease-exit`. Com `prefers-reduced-motion` ou com as animações desligadas no produto, aparece sem deslizar.
- **Gatilho**: o mesmo botão que abre também fecha o drawer em linha ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/drawer/usage)).
- **Alterações não salvas**: ao fechar com dados digitados, abra o alerta de alterações não salvas, com "Salvar", "Não salvar" e "Cancelar" ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/modality)).
- **Erros**: mostre uma mensagem no topo do corpo para vários erros, ou um estado vazio quando o conteúdo inteiro falha ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/drawer/usage)).
- **Carregamento**: enquanto o detalhe carrega, use skeleton no corpo; mantenha cabeçalho e Fechar utilizáveis.
- **Rolagem**: o corpo rola dentro do drawer; a página de fundo não rola junto ([Geist](https://vercel.com/geist/drawer)).

## Conteúdo

**Nomeie a entidade ou a tarefa no título.** "Detalhes do pedido 4821", "Filtrar pedidos". Não repita o título da página ([Geist](https://vercel.com/geist/sheet)). Use caixa de frase, sem ponto final, e quebre a linha em vez de truncar.

**Vá direto ao ponto no corpo.** Conteúdo escaneável, sem textos longos como termos de uso ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/drawer/usage)).

**Rotule ações com até duas palavras, sem artigo.** "Aplicar filtros", "Editar pedido". A recusa é "Cancelar".

## Acessibilidade

- O drawer sobreposto usa `role="dialog"` com `aria-labelledby` apontando para o título ([Geist](https://vercel.com/geist/sheet)). No modo modal, use `<dialog>` com `showModal()` ou `aria-modal="true"` com o fundo inerte, e prenda o foco.
- O drawer em linha é uma região (`<aside>` com rótulo) e não prende o foco.
- Ao abrir, mova o foco para o primeiro campo; sem campos, para o título com `tabindex="-1"` e o foco tênue `.tr-focus-subtle`. Ao fechar, devolva o foco ao gatilho, para que a pessoa mantenha seu lugar na lista ([Geist](https://vercel.com/geist/sheet)).
- O botão Fechar com ícone tem `aria-label="Fechar"` seguido do objeto.
- O corpo que rola recebe `tabindex="0"` quando não tem elementos focáveis, para que o teclado consiga rolar (WCAG 2.2, 2.1.1).
- A folha inferior com alça de arraste também precisa de um botão Fechar; o arraste não pode ser o único caminho (WCAG 2.2, 2.5.7).

## Tokens usados

| Elemento                      | Token                                                       |
|-------------------------------|-------------------------------------------------------------|
| Superfície                    | `--t-surface-raised`                                        |
| Elevação (sobreposto)         | `--e-5`                                                     |
| Camada                        | `--z-3` (não modal), `--z-4` (modal e folha inferior)       |
| Véu (modal)                   | `--t-overlay`                                               |
| Divisores e sombra de rolagem | `--t-border-subtle`, `--stroke-thin`, `--t-shadow-key`      |
| Preenchimento                 | `--sp-400`                                                  |
| Espaço entre botões           | `--sp-200`                                                  |
| Raio da folha inferior        | `--r-2xl` nos cantos superiores                             |
| Movimento                     | `--m-slow`, `--m-normal`, `--m-ease-enter`, `--m-ease-exit` |

## Considerações por plataforma

### Web desktop

Use o drawer lateral. Comece pela largura pequena e só aumente se o conteúdo exigir. O modo em linha funciona bem a partir da classe Grande, quando sobra espaço para a área principal. Com cabeçalho fixo na página, o drawer não modal começa abaixo dele ou o cobre, nunca fica por trás.

### Web móvel

Na classe Compacta, o drawer vira folha inferior com cantos superiores arredondados. Toque fora e deslize para baixo fecham a folha, a menos que haja dados não salvos ([Geist](https://vercel.com/geist/drawer)). Mantenha a ação principal e Cancelar visíveis sem rolar, empilhados com a principal em cima e com alvo de `--c-touch`. Respeite o gesto Voltar do navegador.

### Tablets e dobráveis

Nas classes Média e Expandida, use o drawer lateral sobreposto. Em telas a partir de 600px, avalie se o conteúdo não fica melhor como segundo painel de um split view, que mostra lista e detalhe juntos sem sobreposição ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Ao abrir ou fechar um dobrável, mantenha o drawer aberto e preserve a posição de rolagem e o texto digitado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Diálogos
- Painéis e split view
- Navegação lateral
- Modalidade
- Multitarefa e janelas
- Elevação

### Referências

- [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) Apple HIG
- [Panels](https://developer.apple.com/design/human-interface-guidelines/panels) Apple HIG
- [Modality](https://developer.apple.com/design/human-interface-guidelines/modality) Apple HIG
- [Modal](https://www.gov.br/ds/components/modal) gov.br DS
- [Scrim](https://www.gov.br/ds/components/scrim) gov.br DS
- [Drawer](https://fluent2.microsoft.design/components/web/react/core/drawer/usage) Fluent 2
- [Drawer](https://vercel.com/geist/drawer) Geist
- [Sheet](https://vercel.com/geist/sheet) Geist
- [Drawer](https://blueprintjs.com/docs/#core/components/drawer) Blueprint
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Move as ações do rodapé para o fim com a principal por último, define camadas por tipo, sombra de rolagem e proíbe rolagem horizontal. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                          |
