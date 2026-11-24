# Dialogos

Um diálogo interrompe a tarefa atual para pedir uma decisão, confirmar uma ação ou entregar uma informação crítica.

O diálogo aparece sobre a página, com um véu (scrim) que escurece o fundo. Enquanto ele está aberto, a pessoa só interage com ele. Essa interrupção tem custo, por isso o Trama reserva o diálogo para momentos em que a decisão precisa acontecer agora ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/modality), [gov.br DS](https://www.gov.br/ds/components/modal)).

**Use um diálogo** para confirmar uma ação destrutiva ou irreversível, para avisar sobre um erro que impede o fluxo, como uma sessão prestes a expirar, para pedir uma escolha que a pessoa precisa fazer antes de seguir, ou para uma entrada de dados curta que não exige consultar a página de fundo ([gov.br DS](https://www.gov.br/ds/components/modal)).

**Não use um diálogo** para informar algo que não pede ação: prefira um toast para confirmar uma ação concluída e uma mensagem para um estado persistente ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)). Mensagens de sucesso também não vão em diálogo ([DKFDS](https://designsystem.dk/komponenter/beskeder/)). Se a tarefa exige pesquisar ou consultar outras fontes que o diálogo esconderia, use um popover, um drawer ou uma página ([gov.br DS](https://www.gov.br/ds/components/modal)). Para escolher uma opção entre poucas, prefira um select, que interrompe menos ([gov.br DS](https://www.gov.br/ds/components/modal)).

## Anatomia

1.  **Véu**: scrim de foco que cobre a página com `--t-overlay` e sinaliza que o fundo está bloqueado ([HDS](https://hds.hel.fi/components/dialog), [gov.br DS](https://www.gov.br/ds/components/scrim)).
2.  **Superfície**: `--t-surface-raised`, raio `--r-xl`, elevação `--e-6`, preenchimento `--sp-600`, na camada `--z-4`.
3.  **Cabeçalho com título** (obrigatório): Subtitle 20/28 semibold, ligado ao diálogo por `aria-labelledby`, com até duas linhas.
4.  **Corpo**: texto curto, lista de opções ou poucos campos.
5.  **Rodapé com ações**: no máximo duas, alinhadas ao fim da linha, com a principal por último, separadas por `--sp-200`.
6.  **Botão Fechar** (condicional): ícone no canto superior direito, em diálogos informativos e de escolha por lista.

## Tipos

| Tipo                | Quando usar                                                                                 | Ações                               | Como fecha                                                            |
|---------------------|---------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------------------------------------------------|
| Informativo         | Uma informação crítica que só pede reconhecimento.                                          | Uma: "Fechar" ou "Entendi".         | Botão, Fechar, Esc ou clique no véu.                                  |
| Confirmação         | Uma decisão sobre uma ação proposta, como continuar com campos incompletos.                 | Duas: confirmação e "Cancelar".     | Botões, Esc ou clique no véu.                                         |
| Destrutivo (alerta) | A ação pode apagar dados ou não tem volta. Usa `--t-danger` no botão principal.             | Duas: ação destrutiva e "Cancelar". | Somente pelos botões do rodapé.                                       |
| Escolha por lista   | Uma lista de itens que entram em vigor ao serem escolhidos, como trocar o órgão de lotação. | Nenhuma no rodapé.                  | Escolha de um item, Fechar, Esc ou clique no véu.                     |
| Entrada             | Um a três campos de formulário que a pessoa preenche sem perder o contexto.                 | Duas: envio e "Cancelar".           | Botões, Fechar ou Esc. O clique no véu só fecha se nada foi digitado. |
| Não modal           | Ferramenta auxiliar que convive com a página, como localizar e substituir. Sem véu.         | Conforme a tarefa.                  | Fechar ou Esc; o clique fora não fecha.                               |

Os tipos combinam o [HDS](https://hds.hel.fi/components/dialog) e o [gov.br DS](https://www.gov.br/ds/components/modal). O fechamento do destrutivo só pelos botões segue o [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/dialog/usage), o [Blueprint](https://blueprintjs.com/docs/#core/components/alert) e o [gov.br DS](https://www.gov.br/ds/components/modal).

### Tamanhos

| Classe                | Largura máxima | Uso                                                                                  |
|-----------------------|----------------|--------------------------------------------------------------------------------------|
| `.tr-dialog--sm`      | 360px          | Informativo, confirmação curta, escolha por lista.                                   |
| `.tr-dialog` (padrão) | 440px          | Confirmação, destrutivo, entrada com um ou dois campos.                              |
| `.tr-dialog--lg`      | 720px          | Entrada com campos lado a lado ou conteúdo que precisa rolar, como termos de adesão. |

O diálogo se adapta ao conteúdo dentro desses limites. Deixe sempre uma área de respiro entre o diálogo e as bordas da janela, para que a pessoa perceba que ele está sobre a tela anterior ([gov.br DS](https://www.gov.br/ds/components/modal)).

## Boas práticas

**Abra o diálogo somente a partir de uma ação da pessoa.** Um diálogo que aparece sozinho tende a ser fechado por reflexo, sem leitura. Nunca o mostre ao carregar a página ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/alerts), [gov.br DS](https://www.gov.br/ds/components/modal)). A exceção é o aviso de sessão prestes a expirar, que o próprio sistema dispara ([DKFDS](https://designsystem.dk/komponenter/modal/)).

**Não confirme ações comuns que podem ser desfeitas.** Excluir um e-mail que vai para a lixeira dispensa confirmação; ofereça Desfazer num toast. Reserve a confirmação para ações raras, destrutivas e sem volta ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)).

**Mostre um diálogo por vez.** Nunca empilhe diálogos. Se uma ação dentro do diálogo exige outro, feche o primeiro antes ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/modality), [gov.br DS](https://www.gov.br/ds/components/modal)). Só um tooltip ou um seletor de data podem cobrir parte do diálogo, por pouco tempo ([gov.br DS](https://www.gov.br/ds/components/modal)).

**Use no máximo duas ações.** Uma ação de confirmação exige uma de negação ao lado. A única exceção é o alerta de alterações não salvas, com "Salvar", "Não salvar" e "Cancelar". Nunca use "Saiba mais" como botão: ele tira a pessoa da tarefa; mostre a explicação num trecho expansível do corpo ou antes de abrir o diálogo ([gov.br DS](https://www.gov.br/ds/components/modal)).

**Mantenha o diálogo curto e evite rolagem.** Se o conteúdo cresce, ele pertence a uma página ([DKFDS](https://designsystem.dk/komponenter/modal/)). Quando a rolagem for inevitável, use `.tr-dialog--scroll`: o título fica fixo no topo, as ações fixas no rodapé, e uma sombra marca a divisão sempre que houver conteúdo oculto ([gov.br DS](https://www.gov.br/ds/components/modal), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)). Nunca use rolagem horizontal num diálogo ([gov.br DS](https://www.gov.br/ds/components/modal)).

**Use a escolha por lista com moderação.** O item escolhido entra em vigor na hora e o diálogo fecha sozinho. Como interrompe mais que um select, reserve-a para listas que precisam de espaço, como opções com descrição ([gov.br DS](https://www.gov.br/ds/components/modal)).

**Exija digitação para ações de alto impacto.** Para excluir um recurso de produção, peça que a pessoa digite o nome dele; sem a correspondência exata, mostre o erro junto ao campo ([Geist](https://vercel.com/geist/destructive-action-modal)).

**Feche automaticamente só quando o conteúdo perde o sentido.** O temporizador vale para diálogos que acompanham um processo bloqueante, como "Gerando o documento", que fecham quando o processo termina. Esses diálogos sempre trazem "Cancelar" ([gov.br DS](https://www.gov.br/ds/components/modal)). Um diálogo com texto para ler nunca fecha sozinho (WCAG 2.2, 2.2.1).

**Faça** nomeie a ação no título e repita o verbo no botão principal.

**Não faça** use título genérico, três ações, "Saiba mais" e botões que não dizem o que acontece.

### Véu e scrim

O véu do diálogo é um dos três tipos de scrim que o Trama usa, com base no [gov.br DS](https://www.gov.br/ds/components/scrim):

| Tipo         | Função                                                                                                | Token                 |
|--------------|-------------------------------------------------------------------------------------------------------|-----------------------|
| Foco         | Escurece tudo o que não é o diálogo. Pode ter uma fresta que destaca um elemento, como em onboarding. | `--t-overlay`         |
| Legibilidade | Garante contraste de texto sobre imagem.                                                              | `--t-overlay-text`    |
| Inibição     | Cobre uma área grande ainda indisponível, como uma região em carregamento (`.tr-region-busy`).        | `--t-bg` com `--o-lg` |

O scrim de inibição só esconde visualmente: os elementos abaixo continuam ativos. Marque a área com `inert` ou desative os controles, e prefira o estado desativado do próprio componente em áreas pequenas. Nunca cubra a pesquisa nem os recursos de acessibilidade do produto ([gov.br DS](https://www.gov.br/ds/components/scrim)).

### Estados e comportamento

- **Abertura**: o véu e a superfície entram em `--m-normal` com `--m-ease-enter`; a saída usa `--m-fast` com `--m-ease-exit`. Com `prefers-reduced-motion` ou com o controle de animações do produto desligado, o diálogo aparece sem transição.
- **Posição**: centralizado, ou próximo ao elemento que o abriu ([gov.br DS](https://www.gov.br/ds/components/modal)).
- **Camada**: diálogo e véu ficam em `--z-4`, acima do cabeçalho fixo (`--z-3`), camada que só tooltips e o carregamento bloqueante dividem.
- **Envio em andamento**: o botão principal mostra um spinner com `aria-disabled="true"`, e o diálogo continua aberto até a resposta.
- **Erro**: mostre a mensagem dentro do diálogo e mantenha o foco nele ([Geist](https://vercel.com/geist/destructive-action-modal)).
- **Fechamento com dados**: se fechar pode descartar algo digitado, use o alerta de alterações não salvas ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/modality)).

> **Divergência entre referências** Número de ações: o Fluent 2 aceita até três ações no rodapé; o gov.br DS recomenda no máximo duas e desaconselha "Saiba mais". O Trama segue o gov.br (decisão D22), com a exceção de alterações não salvas. Título: o gov.br torna o título opcional no modal de alerta e corta com reticências o que passa de duas linhas, mostrando o resto em tooltip; o HDS liga o título ao diálogo por `aria-labelledby`. Pelo critério de acessibilidade, o Trama exige o título, que dá nome acessível ao diálogo, e nunca o trunca: reescreva até caber em duas linhas (decisão D15). Botões desativados: o gov.br sugere desativar a confirmação até preencher os campos obrigatórios ou até rolar o conteúdo até o fim. O Trama mantém as ações sempre ativas e valida ao enviar, porque um botão desativado sem explicação não diz o que falta (decisão D9). Botão Fechar: o gov.br recomenda oferecê-lo sempre; o HDS e o Fluent 2 o evitam quando já existe Cancelar. O Trama segue a maioria: nos tipos com Cancelar, ele cumpre a mesma função. Véu: o gov.br usa preto a 40%; sem critério que separe os valores, o Trama mantém `--t-overlay`, ajustado aos dois temas.

## Conteúdo

**Escreva um título específico que descreva a situação.** Uma afirmação ou pergunta breve e clara. Evite "Erro", "Aviso!", "Desculpe a interrupção" e "Você tem certeza?"; prefira "Sua sessão terminou" ou "Excluir foto" ([gov.br DS](https://www.gov.br/ds/components/modal), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)). Use caixa de frase, sem ponto final, em até duas linhas.

**Combine o título com o botão principal.** Título "Excluir foto", botão "Excluir" ([gov.br DS](https://www.gov.br/ds/components/modal)). Rótulos de ação com até duas palavras, sem artigo. A recusa se chama "Cancelar". Prefira "Cancelar" e "Excluir" a "Não" e "Sim" ([gov.br DS](https://www.gov.br/ds/components/modal)).

**Comece o corpo pela consequência.** Diga o que vai acontecer e a quem afeta, sem repetir o título. Feche com "Não é possível desfazer esta ação" somente quando isso for verdade ([Geist](https://vercel.com/geist/modal)).

## Acessibilidade

- Use o elemento `<dialog>` aberto com `showModal()`, que torna o resto da página inerte. Sem ele, use `role="dialog"` com `aria-modal="true"` e o atributo `inert` no fundo. No tipo destrutivo, use `role="alertdialog"`. Só declare o diálogo como modal quando o fundo de fato estiver bloqueado para todas as pessoas ([gov.br DS](https://www.gov.br/ds/components/modal)).
- Ligue o título com `aria-labelledby` e um corpo curto com `aria-describedby` ([HDS](https://hds.hel.fi/components/dialog)).
- Foco inicial conforme o tipo: no informativo, no botão Fechar; na confirmação e na entrada, no primeiro campo ou, sem campos, na ação principal; no destrutivo, em Cancelar ([gov.br DS](https://www.gov.br/ds/components/modal)). Na escolha por lista, no item selecionado.
- Tab e Shift+Tab percorrem só o diálogo ([gov.br DS](https://www.gov.br/ds/components/modal)).
- Ao fechar, devolva o foco ao elemento que abriu o diálogo ([HDS](https://hds.hel.fi/components/dialog/accessibility), [gov.br DS](https://www.gov.br/ds/components/modal)).
- O corpo que rola recebe `tabindex="0"` e um nome, para que quem usa teclado consiga rolar (WCAG 2.2, 2.1.1).
- Garanta sempre um botão para sair, para quem não usa Esc nem clique no véu ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)). Os botões têm alvo de `--c-touch` em telas de toque.

## Tokens usados

| Elemento                        | Token                                                       |
|---------------------------------|-------------------------------------------------------------|
| Véu (scrim de foco)             | `--t-overlay`                                               |
| Superfície                      | `--t-surface-raised`, `--r-xl`, `--e-6`                     |
| Camada                          | `--z-4`                                                     |
| Preenchimento e espaço interno  | `--sp-600`, `--sp-400`, `--sp-300` (corpo com rolagem)      |
| Sombra de rolagem               | `--t-shadow-key`                                            |
| Espaço entre botões             | `--sp-200`                                                  |
| Título, corpo e ação destrutiva | `--t-fg-1`, `--t-fg-2`, `--t-danger`                        |
| Movimento                       | `--m-normal`, `--m-fast`, `--m-ease-enter`, `--m-ease-exit` |

## Considerações por plataforma

### Web desktop

Comece pelo tamanho padrão de 440px. Esc fecha todos os tipos, exceto o destrutivo. Um diálogo não modal pode ficar perto da ferramenta que o abriu.

### Web móvel

Na classe Compacta, o diálogo ocupa a largura da tela menos as margens de `--sp-400`, em qualquer tamanho, e os botões se empilham com a ação principal em cima e Cancelar embaixo ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)). Diálogos de escolha e confirmação podem se ancorar na parte inferior, onde o polegar alcança ([One UI](https://developer.samsung.com/one-ui/comp/dialog.html)). Evite diálogos de entrada no celular, onde funcionam mal ([DKFDS](https://designsystem.dk/komponenter/modal/)). Respeite o gesto Voltar do navegador como forma de fechar.

### Tablets e dobráveis

Nas classes Média e Expandida, use as larguras do desktop, sem esticar. Num dobrável parcialmente dobrado, não posicione botões sobre a dobra ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Ao abrir ou fechar o aparelho, o diálogo continua aberto com o que foi digitado.

## Recursos

### Relacionados

- Modalidade
- Drawers e folhas laterais
- Popovers
- Toasts
- Botões
- Desfazer e refazer
- Elevação

### Referências

- [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) Apple HIG
- [Modality](https://developer.apple.com/design/human-interface-guidelines/modality) Apple HIG
- [Modal](https://www.gov.br/ds/components/modal) gov.br DS
- [Scrim](https://www.gov.br/ds/components/scrim) gov.br DS
- [Utilitário Scrim](https://www.gov.br/ds/utilitarios/js/scrim) gov.br DS
- [Dialog](https://fluent2.microsoft.design/components/web/react/core/dialog/usage) Fluent 2
- [Dialog](https://hds.hel.fi/components/dialog) Helsinki Design System
- [Dialog: accessibility](https://hds.hel.fi/components/dialog/accessibility) Helsinki Design System
- [Modal](https://designsystem.dk/komponenter/modal/) DKFDS
- [Beskeder](https://designsystem.dk/komponenter/beskeder/) DKFDS
- [Modal](https://vercel.com/geist/modal) Geist
- [Destructive Action Modal](https://vercel.com/geist/destructive-action-modal) Geist
- [Alert](https://blueprintjs.com/docs/#core/components/alert) Blueprint
- [Dialog](https://developer.samsung.com/one-ui/comp/dialog.html) One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta tamanhos, rolagem com cabeçalho e rodapé fixos, tipos de escolha por lista e entrada, temporizador, tipos de scrim, camada e foco inicial por tipo, e limita o rodapé a duas ações. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                  |
