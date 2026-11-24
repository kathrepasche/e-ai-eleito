# Padrões: Notificações a Revisar respostas e confirmação

## Notificações

Uma notificação entrega informação oportuna e valiosa, compreensível num relance, e respeita o direito de cada pessoa de decidir quando ser interrompida.

Notificações avisam sobre algo que aconteceu fora da tela que a pessoa está vendo: uma menção, uma aprovação, um prazo, a conclusão de uma tarefa longa. No Trama, elas chegam por três vias: um toast de comunicação enquanto o produto está aberto, a central de notificações dentro do produto e, com permissão, notificações do navegador ou por e-mail.

Toda notificação compete pela atenção da pessoa. Se o produto interromper com pouca coisa, a pessoa desliga todas as notificações e perde também as importantes ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)).

### Boas práticas

#### Permissão e controle

**Peça permissão antes de enviar notificações fora do produto.** Explique que tipo de informação você vai enviar e dê um jeito claro de aceitar ou recusar ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications)). Peça no momento em que o benefício está claro, por exemplo ao acompanhar um processo pela primeira vez, e nunca ao abrir o produto. O pedido nativo do navegador só aparece depois de uma ação da pessoa numa explicação do próprio produto. Veja Onboarding.

**Não envie marketing sem consentimento explícito.** Ofertas e novidades só são enviadas a quem aceitou recebê-las, e nunca com nível de urgência alto ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications)).

**Deixe a pessoa mudar a escolha dentro do produto.** Notificações são opcionais ([gov.br](https://www.gov.br/ds/components/notification)). Ofereça uma tela de configurações onde cada tipo de notificação possa ser ligado ou desligado, por canal ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications)). Veja Configurações.

#### Central de notificações

**Agrupe as notificações numa central aberta por um acionador.** A central é um painel flutuante que aparece quando a pessoa aciona um elemento que indica a existência de notificações, como um botão com contagem no cabeçalho. Ela fecha pelo botão Fechar, ao clicar fora ou ao acionar de novo o mesmo elemento ([gov.br](https://www.gov.br/ds/components/notification)), e com Esc, que devolve o foco ao acionador.

**Monte a central com as partes do gov.br.** Área de cabeçalho com o título e o botão Fechar; abas opcionais em densidade alta, como "Todas" e "Não lidas"; itens obrigatórios separados por divisores; e uma superfície flutuante ([gov.br](https://www.gov.br/ds/components/notification)). No Trama, a central fica na camada `--z-2`, com a elevação `--e-4` dos flutuantes.

**Escreva cada item com etiqueta de estado, título, data e conteúdo.** Uma etiqueta marca o item novo ou não lido; o título identifica o evento; a informação de data e hora localiza o item no tempo; o conteúdo traz o texto total ou parcial ([gov.br](https://www.gov.br/ds/components/notification)). Não dependa só da cor para marcar o não lido.

**Ordene da mais recente para a mais antiga.** A lista funciona como uma linha do tempo contínua, com as novas empilhadas sobre as antigas ([gov.br](https://www.gov.br/ds/components/notification)).

**Role só os itens.** A altura máxima da central não muda e não ultrapassa a área visível; a rolagem interna afeta só a lista, com cabeçalho e abas parados ([gov.br](https://www.gov.br/ds/components/notification)). Use `.tr-scroll`, que eleva a borda quando há conteúdo escondido. Na classe Compacta, sem rolagem interna (veja abaixo).

#### Urgência

**Classifique cada notificação pela urgência real.** O Trama usa quatro níveis, adaptados dos níveis de interrupção da HIG ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications)):

| Nível             | Para quê                                                                                                                         | Como o Trama entrega                                                   |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Passivo           | Informação para ver quando quiser, como uma recomendação.                                                                        | Só na central, sem contagem na badge.                                  |
| Ativo (padrão)    | Algo que a pessoa gosta de saber quando acontece, como uma resposta a um comentário.                                             | Central e badge; toast se o produto estiver aberto.                    |
| Sensível ao tempo | Algo que afeta a pessoa diretamente e pede atenção agora, como um problema de segurança na conta ou um prazo que vence em breve. | Central, toast e, com permissão, notificação do navegador ou e-mail.   |
| Crítico           | Informação urgente sobre saúde ou segurança. Extremamente rara.                                                                  | Todos os canais permitidos. Exige aprovação de produto para ser usada. |

Use o nível sensível ao tempo só para eventos que acontecem agora ou dentro de uma hora ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications)). Exagerar a urgência quebra a confiança.

#### Conteúdo e comportamento

**Seja conciso e informativo.** A pessoa liga notificações para receber atualizações rápidas. O título traz o dado mais útil, como o nome do evento ou o assunto, e o corpo é escrito em frases completas ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)). Use palavras que a pessoa reconhece do produto ([DKFDS](https://designsystem.dk/komponenter/toastbesked/)).

**Não envie várias notificações sobre a mesma coisa.** Mesmo que a pessoa não responda, uma notificação basta. Repetições enchem a central e levam a pessoa a desligar tudo ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)). Agrupe eventos parecidos: "3 novos comentários em Contrato 112/2026".

**Não use notificação para dar instruções.** Instruções são esquecidas assim que a notificação é dispensada. Se a tarefa for simples, ofereça a ação na própria notificação ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)).

**Ofereça ações que poupam tempo.** "Responder", "Aprovar", "Adiar". Evite uma ação que só abre o produto, porque selecionar a notificação já faz isso. Prefira ações não destrutivas; se precisar de uma destrutiva, dê contexto suficiente para evitar engano ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)). Rótulos têm uma ou duas palavras e respondem ao título, como "Abrir contrato" para "Um contrato foi compartilhado com você" ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toast/usage)).

**Não exponha dados sensíveis.** Você não sabe quem mais vê a tela quando a notificação chega. Notificações do navegador e e-mails não trazem dados pessoais ou confidenciais ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)). Escreva um texto genérico e descritivo, como "Novo comentário" ou "Lembrete de prazo", para quando a pré-visualização estiver oculta ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)).

**Mostre erros com alertas e mensagens.** Um erro numa tarefa da pessoa aparece onde a tarefa está ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)). Veja Feedback.

**Com o produto aberto, seja discreto.** Se a pessoa já está vendo a lista em que o item novo entra, insira o item na lista e atualize a contagem, sem toast ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)).

#### Toasts de comunicação

**Use toast para atividade de outras pessoas e mensagens do sistema.** Menções, lembretes de eventos e respostas cabem num toast de comunicação, com uma chamada para o conteúdo. Ele só pode ser dispensado se a informação também estiver na central ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toast/usage)). Não use toast para informação crítica ou ação obrigatória; nesse caso, use uma mensagem ou um diálogo ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toast/usage), [DKFDS](https://designsystem.dk/komponenter/toastbesked/)).

**Siga os limites de tempo e quantidade.** Só o toast informativo sem ação some sozinho, depois de pelo menos 7 segundos, com pausa enquanto o ponteiro ou o foco estiver sobre ele; toasts com ação ficam até a pessoa fechar. Mostre no máximo quatro toasts ao mesmo tempo, com `--sp-400` entre eles, e mantenha o corpo com até 60 caracteres ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toast/usage)). O mais novo aparece na borda e empurra os anteriores; se a ordem importar, mostre a hora em cada um ([DKFDS](https://designsystem.dk/komponenter/toastbesked/)). O tempo de exibição precisa respeitar o critério WCAG 2.2, 2.2.1.

**Mantenha os toasts num lugar fixo.** Use o canto em que a central de notificações abre, normalmente no alto ou embaixo à direita, sem cobrir o conteúdo principal ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toast/usage)).

#### Badges

**Use a badge de contagem só para notificações não lidas.** Não use `.tr-badge--count` para outros números, como saldos ou datas. Atualize a contagem assim que a pessoa ler as notificações e não crie elementos que imitem uma badge ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)). Nunca dependa só da badge para comunicar algo essencial: a informação importante aparece de forma clara quando a pessoa abre o produto ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)).

**Faça** título com o fato principal, contexto curto e uma ação específica.

**Não faça** título vago, urgência falsa, instrução no corpo e ação que só abre o produto.

#### Acessibilidade

A central funciona inteiramente pelo teclado: Tab e Shift+Tab percorrem os controles, Enter ou Espaço os acionam ([gov.br](https://www.gov.br/ds/components/notification)). Ao abrir, o foco vai para o título da central, que recebe `tabindex="-1"`; ao fechar, volta ao acionador. Escreva descrições claras e garanta o contraste do texto, inclusive na etiqueta "Nova" (WCAG 2.2, 1.4.3). Evite sobrecarregar a pessoa com excesso de notificações ([gov.br](https://www.gov.br/ds/components/notification)).

Toasts de informação e sucesso usam `aria-live="polite"`; reserve o anúncio assertivo para erros e avisos que interrompem um fluxo, porque anúncios assertivos frequentes atrapalham ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toast/usage), [Geist](https://vercel.com/geist/toast)). Não ponha navegação principal dentro de um toast: ele some antes que pessoas que usam teclado consigam alcançá-lo ([Geist](https://vercel.com/geist/toast)). A central de notificações é sempre alcançável pelo teclado e o botão que a abre informa a quantidade de não lidas no nome acessível.

Som pode complementar uma notificação, mas nunca carrega sozinho uma informação importante, porque a pessoa pode não ouvi-lo ([HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)).

> **Divergência entre referências** Tempo do toast: o Fluent fecha toasts sem ação após sete segundos; o gov.br pede evitar mensagens que somem sozinhas. O Trama aplica D23: só o toast informativo sem ação some, com no mínimo 7 segundos e pausa em hover e foco. Opcionalidade: a HIG pede consentimento para notificações fora do produto; o gov.br pede que todas as notificações sejam configuráveis. O Trama aplica as duas: permissão para os canais externos e configuração por tipo e canal dentro do produto.

### Considerações por plataforma

#### Web desktop

A central abre como popover ou drawer a partir do botão no cabeçalho, com largura de no máximo metade da área de conteúdo e altura limitada à área visível ([gov.br](https://www.gov.br/ds/components/notification)). Notificações do navegador aparecem fora da aba; ao selecionar uma, leve a pessoa direto ao conteúdo, na aba já aberta do produto quando houver.

#### Web móvel

Toasts devem ter cerca de uma linha e nunca passar de três, em qualquer idioma ([One UI](https://developer.samsung.com/one-ui/comp/toast.html)). Posicione-os acima da navegação inferior. Na classe Compacta, a central ocupa a tela toda, com o botão Fechar obrigatório, e a altura acompanha o conteúdo: use a rolagem nativa da página, sem rolagem interna ([gov.br](https://www.gov.br/ds/components/notification)). Não dependa só de notificações do navegador: ofereça também o e-mail para avisos sensíveis ao tempo.

#### Tablets e dobráveis

Na classe Média, a central segue a regra do desktop: até metade da largura, com rolagem interna. Em telas grandes, ela pode ocupar um painel lateral sem tirar a pessoa da tarefa. Ao selecionar uma notificação num layout de dois painéis, abra o conteúdo no painel de detalhe e mantenha a lista visível.

### Recursos

#### Relacionados

- Toasts
- Badges
- Feedback
- Configurações
- Privacidade
- Onboarding

#### Referências

- [Notification](https://www.gov.br/ds/components/notification) gov.br DS
- [Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications) Apple HIG
- [Managing notifications](https://developer.apple.com/design/human-interface-guidelines/managing-notifications) Apple HIG
- [Toast](https://fluent2.microsoft.design/components/web/react/core/toast/usage) Fluent 2
- [Toastbesked](https://designsystem.dk/komponenter/toastbesked/) Det Fælles Designsystem
- [Toast](https://vercel.com/geist/toast) Geist
- [Toasts](https://developer.samsung.com/one-ui/comp/toast.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a anatomia e o comportamento da central de notificações (abertura, ordem cronológica, rolagem só nos itens, tela cheia na classe Compacta), o acesso por teclado e os tempos de toast de D23. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                            |

## Modalidade

Use apresentações modais só quando interromper a tarefa atual traz um benefício claro, e torne evidente o que a pessoa precisa fazer e como sair.

Modalidade apresenta conteúdo em um modo separado, que impede a interação com a tela de origem e exige uma ação explícita para ser encerrado ([HIG](https://developer.apple.com/design/human-interface-guidelines/modality)). Use-a para informar erros que impedem o fluxo, pedir uma escolha ou decisão sobre algo crítico, ou coletar uma entrada curta sem perder o contexto da tela ([gov.br](https://www.gov.br/ds/components/modal), [HIG](https://developer.apple.com/design/human-interface-guidelines/modality)).

Toda interrupção tem custo. Diálogos modais aumentam a carga cognitiva e quebram o fluxo, por isso o Trama os reserva para ações importantes ([Fluent](https://fluent2.microsoft.design/components/web/react/core/dialog/usage), [Ontario](https://designsystem.ontario.ca/components/detail/modals.html)). Mostre um modal só em resposta a uma ação da pessoa, nunca ao carregar a página: modais exibidos por eventos do sistema tendem a ser fechados sem leitura ([gov.br](https://www.gov.br/ds/components/modal)).

### Escolher a apresentação

Comece pela forma menos intrusiva que resolve o problema.

| Situação                                              | Use                                                              | Modal?        |
|-------------------------------------------------------|------------------------------------------------------------------|---------------|
| Informar o resultado de uma ação, sem pedir resposta  | Toast                                                            | Não           |
| Dar contexto extra ou exigir consulta a outras fontes | Popover ou tooltip                                               | Não           |
| Ferramenta auxiliar usada enquanto se edita a página  | Diálogo não modal ou drawer                                      | Não           |
| Escolher uma opção que vale de imediato               | Menu ou select; modal de opção por lista só se o menu não couber | Às vezes      |
| Tarefa curta e focada, como renomear                  | Modal de entrada                                                 | Sim           |
| Decisão sobre perda de dados ou ação destrutiva       | Modal de alerta                                                  | Sim           |
| Tarefa complexa ou em várias etapas                   | Página própria ou apresentação modal em tela cheia               | Sim           |
| Aviso dentro de um fluxo de páginas                   | Página de interrupção                                            | Não se aplica |

Os critérios vêm do Fluent para toast, popover e diálogos ([Fluent](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)), do gov.br para popover em consultas e menu no lugar do modal de lista ([gov.br](https://www.gov.br/ds/components/modal)), da HIG para tela cheia modal ([HIG](https://developer.apple.com/design/human-interface-guidelines/modality)) e do GOV.UK para páginas de interrupção ([GOV.UK](https://design-system.service.gov.uk/patterns/interruption-pages/)).

### Tipos

| Tipo              | Uso                                                                         | Ações no rodapé             | Fecha com                                                        | Foco inicial                    |
|-------------------|-----------------------------------------------------------------------------|-----------------------------|------------------------------------------------------------------|---------------------------------|
| Informativo       | Informação que exige ciência                                                | Uma: Fechar ou "Entendi"    | Botão, Fechar no canto, Esc                                      | Botão Fechar                    |
| Alerta            | Ação urgente ou destrutiva; título opcional no gov.br, obrigatório no Trama | Duas: confirmação e negação | Botões e Esc, que equivale a Cancelar                            | Ação segura (Cancelar)          |
| Opção por lista   | Escolha que vale assim que selecionada                                      | Nenhuma                     | Fechar no canto, clique fora, Esc ou a própria escolha           | Opção selecionada ou a primeira |
| Opção por seleção | Escolha que a pessoa confirma antes de valer                                | Duas: confirmação e negação | Botões, Fechar no canto, clique fora, Esc                        | Opção selecionada ou a primeira |
| Entrada           | Campos de formulário curtos                                                 | Duas: confirmação e negação | Botões, Fechar no canto, Esc; clique fora só sem dados digitados | Primeiro campo                  |

Tipos e formas de fechar seguem o gov.br ([gov.br](https://www.gov.br/ds/components/modal)). O modal de opção por lista é disruptivo: prefira um menu suspenso ([gov.br](https://www.gov.br/ds/components/modal)). O foco inicial segue a decisão D13 do Trama.

### Boas práticas

**Não use alertas para ações comuns que podem ser desfeitas.** Reserve o alerta para ações destrutivas incomuns e irreversíveis ([HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)). Nas demais, ofereça Desfazer.

**Não use alertas só para informar.** Mostre a informação no contexto, com uma mensagem ([HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)). A exceção é o aviso de sessão expirando, que alerta sobre uma mudança que a pessoa não iniciou ([DKFDS](https://designsystem.dk/komponenter/modal/)).

**Mantenha a tarefa modal simples e curta.** Evite hierarquias de telas dentro do modal ([HIG](https://developer.apple.com/design/human-interface-guidelines/modality)). Formulários em diálogos são curtos ([Fluent](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)). Se a tarefa exige consultar outras fontes que o modal bloquearia, ele é o componente errado ([gov.br](https://www.gov.br/ds/components/modal)).

**Mostre um modal por vez.** Não empilhe nem encadeie diálogos ([gov.br](https://www.gov.br/ds/components/modal), [HIG](https://developer.apple.com/design/human-interface-guidelines/modality), [Fluent](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)). Só componentes de maior prioridade, como um tooltip ou um seletor de data, podem cobrir parte do modal por um momento ([gov.br](https://www.gov.br/ds/components/modal)).

**Evite perda de dados ao fechar.** Se fechar o modal descartaria conteúdo criado pela pessoa, explique e ofereça como resolver ([HIG](https://developer.apple.com/design/human-interface-guidelines/modality)). Por isso, um modal de entrada com dados digitados não fecha com clique fora.

**Nunca feche um modal com temporizador fixo.** O fechamento automático só vale quando o conteúdo perde o sentido ao fim de um processo, como um modal de carregamento que fecha quando o processo termina, e sempre com uma ação de negação disponível ([gov.br](https://www.gov.br/ds/components/modal)). Conteúdo para ler não some sozinho (WCAG 2.2, 2.2.1).

#### Tamanho e rolagem

**Escolha o tamanho pelo conteúdo.** Use `.tr-dialog--sm` para alertas e confirmações, o tamanho padrão para modais de entrada e opção, e `.tr-dialog--lg` para conteúdo extenso, como um gráfico expandido. O modal se adapta ao conteúdo, mas não ocupa quase toda a tela: deixe uma área de respiro para a pessoa perceber que a tela anterior continua por baixo ([gov.br](https://www.gov.br/ds/components/modal), [DKFDS](https://designsystem.dk/komponenter/modal/)).

**Evite rolagem; se for inevitável, fixe cabeçalho e rodapé.** Com `.tr-dialog--scroll`, o título fica fixo no topo, as ações na base e só o corpo rola. Mostre uma sombra na divisa enquanto houver conteúdo oculto daquele lado ([gov.br](https://www.gov.br/ds/components/modal), [Fluent](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)). Nunca use rolagem horizontal em modais ([gov.br](https://www.gov.br/ds/components/modal)).

#### Conteúdo e ações

**Escreva um título que diga a situação ou a tarefa.** Seja específico e evite títulos alarmantes ou vagos, como "Aviso", "Desculpe a interrupção" ou "Tem certeza?" ([gov.br](https://www.gov.br/ds/components/modal), [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)). Use caixa de frase ([Fluent](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)). Combine o título com o botão principal: título "Excluir foto", botão "Excluir" ([gov.br](https://www.gov.br/ds/components/modal)).

**Use no máximo duas ações no rodapé.** Com uma ação, ela é de ciência ou de negação. Com duas, uma confirma e a outra nega; toda confirmação tem uma negação ao lado ([gov.br](https://www.gov.br/ds/components/modal)). A única exceção é o alerta de alterações não salvas, com Salvar, Não salvar e Cancelar. Nunca use "Saiba mais" como botão: ele afasta a pessoa da tarefa. Use um conteúdo expansível no corpo ou dê a informação antes de abrir o modal ([gov.br](https://www.gov.br/ds/components/modal)).

**Alinhe as ações ao fim, com a principal por último.** A ação principal usa ênfase primária e a negação, secundária ([gov.br](https://www.gov.br/ds/components/modal)). Na classe Compacta, empilhe os botões com a principal em cima.

**Rotule os botões com o resultado.** "Cancelar" e "Excluir" dizem mais que "Não" e "Sim" ([gov.br](https://www.gov.br/ds/components/modal), [HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)). Evite "OK" quando a pessoa confirma uma ação. Aplique `.tr-btn--danger` à ação destrutiva, com texto que diga o que vai acontecer ([GOV.UK](https://design-system.service.gov.uk/components/button/)).

**Mantenha a ação principal sempre habilitada.** Valide ao confirmar: se faltar um campo obrigatório, mostre o erro no campo e mova o foco para ele ([Ontario](https://designsystem.ontario.ca/components/detail/buttons.html)).

> **Divergência entre referências** O gov.br sugere desativar a confirmação até que os campos obrigatórios estejam preenchidos, ou até que a pessoa role todo o conteúdo, e limitar o título a duas linhas com reticências e tooltip. O Ontario pede botões sempre habilitados, com tratamento de erro. O Trama aplica as decisões D9 e D15: a confirmação fica habilitada e valida ao ser acionada, porque um botão desativado não diz o que falta, e o título quebra linha sem truncar. O gov.br também põe o foco inicial do modal de ação no botão primário; pela decisão D13, o Trama o põe no primeiro campo e usa a ação principal só quando não há campo. Fontes: [gov.br](https://www.gov.br/ds/components/modal), [Ontario](https://designsystem.ontario.ca/components/detail/buttons.html).

### Scrim e bloqueio

Um scrim é uma camada semitransparente que torna uma área menos proeminente. Há três tipos ([gov.br](https://www.gov.br/ds/components/scrim)):

| Tipo         | Uso                                                                                    | No Trama                                                                                        |
|--------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Foco         | Escurece a tela atrás de um elemento que exige atenção, como um modal                  | `--t-overlay`, com `inert` no restante da página                                                |
| Legibilidade | Garante contraste de texto sobre imagem                                                | `--t-overlay-text`                                                                              |
| Inibição     | Bloqueia uma área grande enquanto ela não pode ser usada, como durante um carregamento | `.tr-region-busy`, com `--o-lg` sobre a cor de fundo da área, mais `aria-busy="true"` e `inert` |

**Bloqueie de verdade o que o scrim cobre.** Elementos sob um scrim de inibição continuam ativos se nada mais for feito ([gov.br](https://www.gov.br/ds/components/scrim)). Aplique `inert` à área coberta. Em componentes pequenos, prefira o estado desabilitado do próprio componente ([gov.br](https://www.gov.br/ds/components/scrim)), com a explicação exigida para elementos desabilitados.

**Não bloqueie a pesquisa nem os recursos de acessibilidade** sem uma justificativa forte ([gov.br](https://www.gov.br/ds/components/scrim)). Vários scrims podem coexistir na tela, mas nunca dois modais.

> **Divergência entre referências** O gov.br define o scrim de foco como preto com 40% de opacidade. O Trama mantém `--t-overlay`, com 48% no tema claro e 64% no escuro, porque o véu é ajustado a cada tema e separa mais o modal do fundo. Fontes: [gov.br](https://www.gov.br/ds/components/scrim).

#### Páginas de interrupção

**Use páginas de interrupção com moderação em fluxos de páginas.** Elas avisam antes de a pessoa fazer algo incomum, irreversível ou que conflita com dados existentes, e ficam menos eficazes quanto mais aparecem. Mostre a informação com um botão para continuar e um link Voltar no topo ([GOV.UK](https://design-system.service.gov.uk/patterns/interruption-pages/)).

### Acessibilidade

**Prenda o foco e devolva-o.** Com o modal aberto, Tab e Shift+Tab percorrem só os elementos dele. Ao fechar, o foco volta ao último elemento focado na página ([gov.br](https://www.gov.br/ds/components/modal), [Fluent](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)).

**Posicione o foco inicial pelo tipo.** Informativo: no botão Fechar. Ação: no primeiro campo, ou na ação principal se não houver campo. Destrutivo: na ação segura, para que Enter nunca execute a destruição por acidente ([gov.br](https://www.gov.br/ds/components/modal), [Geist](https://vercel.com/geist/modal)).

**Ofereça sempre uma saída que dispense Esc e clique fora.** O botão Fechar faz parte da ordem de navegação ([gov.br](https://www.gov.br/ds/components/modal), [Fluent](https://fluent2.microsoft.design/components/web/react/core/dialog/usage)).

**Identifique o modal.** Use `role="dialog"` ou `role="alertdialog"`, `aria-labelledby` apontando para o título e `aria-modal="true"` quando o modal de fato bloqueia a página, com `inert` no restante ([gov.br](https://www.gov.br/ds/components/modal), [DKFDS](https://designsystem.dk/komponenter/modal/)). Um corpo com rolagem recebe `tabindex="0"` e nome acessível, para rolar pelo teclado.

> **Divergência entre referências** O Fluent fecha diálogos de alerta só pelos botões. O gov.br inclui Esc entre as formas de fechar o modal. Pelo critério de acessibilidade, o Trama permite Esc em todos os tipos; no alerta, Esc equivale à ação segura, Cancelar. Fontes: [Fluent](https://fluent2.microsoft.design/components/web/react/core/dialog/usage), [gov.br](https://www.gov.br/ds/components/modal).

### Tokens usados

| Elemento                     | Token                                                             |
|------------------------------|-------------------------------------------------------------------|
| Scrim de foco                | `--t-overlay`                                                     |
| Superfície do modal          | `--t-surface-raised`, `--r-xl`, `--e-6`, camada `--z-4`           |
| Sombra da divisa com rolagem | `--t-shadow-key`, camada `--z-1` dentro do modal                  |
| Drawer modal                 | `--e-5`                                                           |
| Espaçamento interno          | `--sp-600`, com `--sp-400` entre blocos                           |
| Entrada e saída              | `--m-normal` com `--m-ease-enter`; `--m-fast` com `--m-ease-exit` |

### Considerações por plataforma

#### Web desktop

Centralize o modal sobre o scrim ou mostre-o perto do elemento que o abriu ([gov.br](https://www.gov.br/ds/components/modal)). Em diálogos não modais, a pessoa continua interagindo com a página; não aplique scrim nem `inert`.

#### Web móvel

Diálogos centrados funcionam mal em telas pequenas ([DKFDS](https://designsystem.dk/komponenter/modal/)), e a área de respiro deixa de ser possível ([gov.br](https://www.gov.br/ds/components/modal)). Na classe Compacta, mantenha alertas curtos e centrados; apresente tarefas modais como folha que sobe da base ou como página inteira, com Fechar visível no topo. Permita fechar a folha arrastando para baixo e confirme antes se houver alterações não salvas ([HIG](https://developer.apple.com/design/human-interface-guidelines/sheets)). Empilhe os botões com a ação principal em cima.

#### Tablets e dobráveis

Em telas grandes, use um pop-up pequeno para tarefas breves, perto do controle que o abriu, mantendo a tela anterior visível ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Não ocupe a tela inteira com uma tarefa que pede pouca informação ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)).

### Recursos

#### Relacionados

- Diálogos
- Drawers e folhas laterais
- Popovers
- Desfazer e refazer
- Excesso de conteúdo
- Foco e seleção

#### Referências

- [Modal (janela de exibição)](https://www.gov.br/ds/components/modal) gov.br DS
- [Scrim](https://www.gov.br/ds/components/scrim) gov.br DS
- [Modality](https://developer.apple.com/design/human-interface-guidelines/modality) Apple HIG
- [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) Apple HIG
- [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) Apple HIG
- [Dialog](https://fluent2.microsoft.design/components/web/react/core/dialog/usage) Fluent 2
- [Interruption pages](https://design-system.service.gov.uk/patterns/interruption-pages/) GOV.UK Design System
- [Button](https://design-system.service.gov.uk/components/button/) GOV.UK Design System
- [Modal](https://designsystem.dk/komponenter/modal/) DKFDS
- [Modals](https://designsystem.ontario.ca/components/detail/modals.html) Ontario Design System
- [Buttons](https://designsystem.ontario.ca/components/detail/buttons.html) Ontario Design System
- [Modal](https://vercel.com/geist/modal) Geist
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Layout design for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                       |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta os tipos de modal com formas de fechar e foco inicial, tamanhos, cabeçalho e rodapé fixos com sombra de rolagem, limite de duas ações, scrims de foco, legibilidade e inibição, e Esc em alertas. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                |

## Multitarefa e janelas

Prepare o produto para ser usado em várias abas, janelas e telas divididas ao mesmo tempo, preservando o contexto de cada uma e se adaptando a qualquer tamanho.

As pessoas alternam entre tarefas o tempo todo: abrem o produto em várias abas, dividem a tela com outra aplicação no tablet, mantêm uma janela estreita ao lado de uma planilha. Elas esperam que isso funcione e podem achar que há algo errado quando não funciona ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)).

Na web, o produto não controla a configuração escolhida pela pessoa nem é avisado dela ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)). Ele só sabe o tamanho da área disponível e se está visível. Por isso, o Trama trata multitarefa como três obrigações: adaptar o layout a qualquer largura, salvar e restaurar o contexto a qualquer momento e coordenar várias instâncias abertas do mesmo produto.

### Boas práticas

#### Adaptar o layout

**Adapte o layout fluidamente a qualquer tamanho de janela** ([HIG](https://developer.apple.com/design/human-interface-guidelines/windows)). Escolha o layout pela largura disponível, nunca pelo tipo de dispositivo: um tablet em tela dividida pode entregar ao produto a largura da classe Compacta. Use as classes de janela do Trama e reorganize painéis e navegação a cada mudança, conforme Layout e grid. Na classe Compacta, use sempre largura fluida.

**Não crie rolagem horizontal em janelas estreitas.** Pessoas desaprovam a rolagem horizontal em testes, esperam rolar na vertical e têm dificuldade de se mover em dois eixos ao mesmo tempo ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). Reorganize o conteúdo em uma coluna. A exceção são conteúdos que exigem duas dimensões, como tabelas de dados e mapas, que rolam dentro do próprio contêiner (WCAG 2.2, 1.4.10). Veja Excesso de conteúdo.

**Em janelas estreitas, prefira a rolagem da página.** Áreas com rolagem interna ficam pequenas e difíceis de usar; deixe a página rolar e mostre parte do conteúdo seguinte como pista de que há mais ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)).

**Não estique o conteúdo em janelas largas.** Aplicações esticadas são mais difíceis de ler. Use vários painéis para mostrar mais informação ao mesmo tempo ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

**Evite trocar de contexto para tarefas breves.** Em janelas grandes, use um pop-up pequeno perto do controle que o abriu e mantenha a tela anterior visível ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)).

#### Preservar o contexto

**Esteja sempre pronto para salvar e restaurar o contexto.** Você não sabe quando a pessoa vai trocar de tarefa ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)). Salve rascunhos, filtros, a aba ativa e a posição de rolagem continuamente, e reflita o estado principal na URL para que recarregar ou compartilhar o link leve ao mesmo lugar. Para pessoas sem conta, guarde o progresso temporário em `sessionStorage`, que é apagado quando o navegador fecha, e não guarde dados sensíveis em `localStorage`. Para pessoas com conta, salve no servidor ([Ontario](https://designsystem.ontario.ca/components/detail/task-list.html)).

**Pause o que exige atenção quando a pessoa sai.** Vídeos, apresentações automáticas e cronômetros pausam quando a aba fica oculta e retomam do mesmo ponto na volta ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)). Use o evento de visibilidade da página. Áudio que a pessoa iniciou de propósito continua tocando.

**Termine em segundo plano as tarefas que a pessoa iniciou.** Envios de arquivo, exportações e processamentos continuam enquanto ela navega para outra parte do produto ou para outra aba ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)). Mostre o andamento em um lugar persistente, como um indicador no cabeçalho. Não bloqueie a página inteira com um scrim enquanto a tarefa roda: bloqueie só a região afetada com `.tr-region-busy` ([gov.br](https://www.gov.br/ds/components/scrim)).

**Notifique com moderação.** Avise quando uma tarefa importante ou com prazo termina enquanto a pessoa está em outro lugar; para tarefas rotineiras, deixe que ela confira ao voltar ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)). Siga Notificações.

#### Várias janelas e instâncias

**Escolha bem o momento de abrir uma nova janela.** Uma janela nova ajuda a comparar conteúdos ou preservar o contexto. Abrir janelas por padrão gera bagunça e confunde a navegação ([HIG](https://developer.apple.com/design/human-interface-guidelines/windows)). No Trama, links abrem na mesma aba por padrão.

**Ofereça a opção de abrir em nova aba.** Coloque "Abrir em nova aba" no menu de contexto do item ([HIG](https://developer.apple.com/design/human-interface-guidelines/windows)). Use links reais (`<a href>`) para itens navegáveis, para que o clique do meio e o menu do navegador funcionem. Quando um link abrir em nova aba por decisão do produto, diga isso no texto: "Regulamento do programa (abre em nova aba)".

**Use as palavras "janela" e "aba" na interface.** Outros termos técnicos confundem ([HIG](https://developer.apple.com/design/human-interface-guidelines/windows)).

**Mantenha cada instância independente e os dados sincronizados.** Duas abas podem mostrar telas diferentes; o estado de navegação de uma não muda a outra. Os dados são compartilhados: quando um item muda em uma aba, atualize as outras ou avise que há uma versão mais recente. Se a mesma pessoa edita o mesmo documento em duas janelas, avise antes de sobrescrever. Esse aviso tem ação, então fica visível até a pessoa agir ou fechar.

**Não abra modais sobre modais entre instâncias.** Cada aba mostra no máximo um modal por vez ([gov.br](https://www.gov.br/ds/components/modal)). Se um evento de outra aba exigir decisão enquanto um modal está aberto, espere o modal fechar e use uma mensagem na página.

**Não imite janelas do sistema.** Molduras e controles personalizados que não reproduzem o comportamento do sistema fazem o produto parecer quebrado ([HIG](https://developer.apple.com/design/human-interface-guidelines/windows)). Prefira painéis, drawers e abas reais do navegador.

**Permita arrastar conteúdo entre janelas.** Em multi-janela, as pessoas movem texto, imagens e endereços web de uma aplicação para outra ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Siga Arrastar e soltar.

**Faça** avise quando os dados mudaram em outra instância e deixe a pessoa decidir quando atualizar.

**Não faça** bloqueie o uso em mais de uma aba.

### Acessibilidade

Ao restaurar o contexto, devolva o foco ao elemento que a pessoa usava, ou ao título H1 se a página foi recarregada, sem anunciar a página inteira de novo. Avisos de mudança vinda de outra instância usam `role="status"` e não roubam o foco. Teste o produto com zoom de 400% em uma janela de 1.280 pixels, que equivale à largura de 320 pixels CSS da classe Compacta: o conteúdo precisa caber sem rolagem nas duas direções (WCAG 2.2, 1.4.10).

### Considerações por plataforma

#### Web desktop

No desktop, multitarefa é o modo normal de trabalho ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)). Teste o produto em janelas ocupando metade ou um terço do monitor. Não coloque ações críticas apenas na borda inferior da janela, que pode ficar fora da tela quando a pessoa reposiciona a janela ([HIG](https://developer.apple.com/design/human-interface-guidelines/windows)).

#### Web móvel

O navegador pode descarregar abas em segundo plano. Ao voltar, a página recarrega: restaure rascunhos e posição a partir do que foi salvo. Vídeos podem continuar em uma janela flutuante (picture-in-picture) enquanto a pessoa usa outra aplicação ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)); não desative esse recurso sem motivo.

#### Tablets e dobráveis

Telas grandes permitem até 3 aplicações em tela dividida e 5 em pop-up ao mesmo tempo, com janelas redimensionáveis ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). No iPad em modo de janelas, as pessoas redimensionam e reposicionam janelas livremente ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)). O produto precisa funcionar em qualquer uma dessas larguras. Em dobráveis, ao abrir ou fechar o aparelho, mantenha a posição de rolagem e o texto em edição ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Layout e grid
- Painéis e split view
- Excesso de conteúdo
- Projetar para tablets e dobráveis
- Tela cheia
- Links

#### Referências

- [Content overflow](https://www.gov.br/ds/padroes/design/contentoverflow) gov.br DS
- [Modal (janela de exibição)](https://www.gov.br/ds/components/modal) gov.br DS
- [Scrim](https://www.gov.br/ds/components/scrim) gov.br DS
- [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking) Apple HIG
- [Windows](https://developer.apple.com/design/human-interface-guidelines/windows) Apple HIG
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Layout design for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI
- [Task list](https://designsystem.ontario.ca/components/detail/task-list.html) Ontario Design System

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a proibição de rolagem horizontal em janelas estreitas, a preferência pela rolagem da página, o bloqueio só da região afetada, um modal por aba, links na mesma aba por padrão e o teste com zoom de 400%. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                         |

## Oferecer ajuda

Ajuda boa aparece onde a dúvida surge, trata da tarefa em curso e sai do caminho de quem não precisa dela.

Um produto claro reduz a necessidade de ajuda, mas não a elimina. Quando for preciso orientar, relacione a ajuda à ação exata que a pessoa está fazendo e facilite dispensá-la ([HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help)). Tarefas simples pedem uma explicação curta na própria tela; tarefas complexas e com várias etapas podem pedir um tutorial.

O Trama organiza a ajuda em três tipos, como o gov.br: global, a seção de ajuda do produto; contextual, o trecho de ajuda junto ao elemento em uso; e não solicitada, que aparece sem pedido, como num onboarding ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Dentro da ajuda contextual vale uma escala: quanto mais pessoas precisam da informação, mais visível ela fica, e informação essencial nunca vai para dentro de um elemento que precisa ser aberto.

### Boas práticas

#### Acesso em todas as telas

**Ofereça acesso à ajuda em todas as telas.** Nunca se sabe quando a pessoa vai precisar dela. Ponha o acesso num lugar visível e fácil de achar, no cabeçalho, no rodapé ou no menu de navegação ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). No Trama, o padrão é um botão "Ajuda" nas ações do cabeçalho, repetido no rodapé.

**Leve direto ao conteúdo de ajuda.** Ao acionar "Ajuda", mostre o conteúdo, sem um menu intermediário com tópicos alheios à ajuda ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Se a pessoa estiver numa tarefa, abra o tópico dessa tarefa.

**Use o ícone de interrogação para ajuda e o de informação para ajuda contextual.** A interrogação é a referência que as pessoas reconhecem para ajuda; o "i" serve como alternativa junto a campos e elementos ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Acompanhe o ícone de texto, ou de nome acessível quando estiver sozinho. Veja Iconografia.

#### Ajuda global

**Organize a seção de ajuda por tarefas e assuntos.** Use tópicos e categorias, uma navegação própria e uma pesquisa com sugestões. Trate só do assunto de cada tópico, em linguagem simples e sem termos técnicos, com títulos, listas, tabelas e imagens. Ofereça vídeos com legenda quando ajudarem a entender ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Veja Pesquisa.

**Atenda diferentes níveis de experiência.** Quando possível, ofereça caminhos para quem começa e para quem já domina o produto ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)), como um tópico "Primeiros passos" separado de atalhos e recursos avançados.

**Trate o assistente de conversa como mais um canal.** Um assistente pode ajudar a encontrar informação ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)), mas a seção de ajuda continua acessível sem ele. Se usar IA, siga IA generativa.

#### Ajuda contextual

**Escolha o nível de ajuda pela quantidade de pessoas que precisa dela.**

| Quem precisa                                          | Onde colocar                                                      | Componente do Trama                              |
|-------------------------------------------------------|-------------------------------------------------------------------|--------------------------------------------------|
| Quase todos                                           | Sempre visível: rótulo, dica do campo, texto introdutório         | `.tr-hint`, parágrafo                            |
| Alguns                                                | Expansível, logo abaixo do conteúdo relacionado                   | Acordeão com uma única seção (`details`)         |
| Poucos, com dúvida pontual                            | Popover aberto por um botão de informação ao lado do rótulo       | Popover (`.tr-popover`)                          |
| Quem precisa de explicação longa, com imagem ou vídeo | Janela com rolagem interna, aberta por um botão junto ao elemento | Diálogo (`.tr-dialog--scroll`) ou drawer         |
| Quem não reconhece um ícone                           | Ao passar o ponteiro ou focar                                     | Tooltip (`.tr-tooltip`)                          |
| Quem quer aprender um recurso novo                    | Dica contextual, uma vez                                          | Popover ou mensagem dispensável; veja Onboarding |
| Quem ficou sem saída                                  | Seção de ajuda, canais de contato e envio de opinião              | Bloco de contato; veja Coletar feedback          |

**Não esconda o que é essencial.** Informação necessária para concluir a tarefa fica visível, como dica ou texto da página. Popovers e tooltips guardam só complementos ([Fluent](https://fluent2.microsoft.design/components/web/react/core/infolabel/usage), [DKFDS](https://designsystem.dk/komponenter/tooltip/)). Requisitos de formato, por exemplo, nunca ficam escondidos ([DKFDS](https://designsystem.dk/komponenter/tooltip/)).

**Use dicas de campo curtas.** Use a dica para o que ajuda a maioria a responder, como onde encontrar o dado ou como ele será usado. Mantenha-a numa frase curta e sem links. Se a explicação for longa, ponha-a na página, antes da pergunta, porque leitores de tela leem a dica inteira a cada interação com o campo ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)).

**Use o detalhe expansível para conteúdo que só alguns precisam.** Ele deixa a página fácil de escanear. Escreva o texto do controle curto e descritivo, para que a pessoa saiba se precisa abri-lo ([GOV.UK](https://design-system.service.gov.uk/components/details/)). Algumas pessoas evitam abrir esse tipo de controle por achar que sairão da página ([GOV.UK](https://design-system.service.gov.uk/components/details/)), mais um motivo para não guardar ali o essencial.

**Ponha o acionador junto ao elemento e termine com um caminho para a ajuda global.** O ícone de ajuda contextual fica perto do elemento a que se refere; o texto é curto e direto; quando houver mais a dizer, um link no fim leva ao tópico da ajuda global ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Use a ajuda contextual para complementos, como a justificativa legal da coleta de um dado ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Use popover de informação com moderação.** O botão de informação fica ao lado do rótulo; o popover abre ao selecionar e fecha com Esc ou ao selecionar outra coisa. Limite a dois ou três por área: mais do que isso indica um problema de design. O conteúdo tem uma ou duas frases curtas, sem listas, e no máximo um link com texto específico ([Fluent](https://fluent2.microsoft.design/components/web/react/core/infolabel/usage)). Não aninhe popovers ([Fluent](https://fluent2.microsoft.design/components/web/react/core/popover/usage)).

**Use diálogo ou drawer para ajuda rica.** Conteúdo com formatação, imagens ou vídeo precisa de espaço e rolagem interna ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Prefira o drawer quando a pessoa precisar ver o formulário enquanto lê; num diálogo informativo, o foco inicial vai para o botão Fechar (D13).

**Escreva tooltips que expliquem a ação.** Descreva só o controle em questão, comece com um verbo ("Restaurar configurações padrão"), não repita o nome do controle e limite o texto a 60 a 75 caracteres, lembrando que traduções mudam o tamanho ([HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help)). Não ponha botões nem links dentro de tooltips ([DKFDS](https://designsystem.dk/komponenter/tooltip/)). Tooltips não aparecem na impressão; se o conteúdo precisa ser impresso, deixe-o visível ([DKFDS](https://designsystem.dk/komponenter/tooltip/)).

**Não repita na ajuda o que já está na tela.** Tooltips e popovers trazem informação nova ([DKFDS](https://designsystem.dk/komponenter/tooltip/), [Fluent](https://fluent2.microsoft.design/components/web/react/core/infolabel/usage)). Também não explique como funcionam componentes padrão; explique o que eles fazem no seu produto ([HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help)).

**Use a linguagem certa para o contexto.** Termos e imagens da ajuda acompanham o dispositivo e a entrada em uso. Escreva "selecione" em vez de "clique" ou "toque" quando a mesma tela servir a mouse e toque ([HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help)). Veja Escrita e conteúdo.

**Destaque exemplos e informações adicionais com texto recuado, sem exagero.** Um bloco destacado diferencia citações, exemplos e informações extras. Usado demais, perde o efeito, e em páginas complexas pode passar despercebido; para avisos importantes, use uma mensagem ([GOV.UK](https://design-system.service.gov.uk/components/inset-text/)).

#### Dicas de recursos

**Use dicas só para recursos simples.** Se o recurso exige mais de três ações, ele é complexo demais para uma dica ([HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help)). Escreva uma ou duas frases diretas, sem conteúdo promocional nem assunto de outro fluxo.

**Defina quem vê cada dica e com que frequência.** Não mostre a dica a quem já usa o recurso. Quando houver várias dicas, espace-as, por exemplo uma a cada 24 horas ([HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help)). Uma dica pode ter um botão que leve às configurações do recurso ou a mais informações.

#### Contato e opinião

**Ofereça um caminho para quando a ajuda não bastar.** Ao lado da ajuda, permita enviar dúvidas, sugestões e relatos de problema ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Dúvidas frequentes que chegam por esse canal indicam onde a interface ou a ajuda precisam melhorar. Veja Coletar feedback.

**Mostre os canais na mesma ordem em todo o produto.** Ordene-os pelo que as pessoas mais precisam e pelo que a equipe consegue atender. Redes sociais vêm por último, com o aviso para não publicar dados pessoais ([GOV.UK](https://design-system.service.gov.uk/patterns/contact-a-department-or-service-team/)).

**Informe horários, exceções, custos e prazos.** Diga quando cada canal funciona, quais dias são exceção (feriados, por exemplo), se há custo e quanto tempo leva a resposta. Isso ajuda a escolher o canal ([GOV.UK](https://design-system.service.gov.uk/patterns/contact-a-department-or-service-team/)).

**Ajuste o destaque do contato à importância.** Use texto recuado para diferenciar o contato do conteúdo ao redor. Se o contato for secundário e longo, ponha-o num detalhe expansível ao fim do formulário; se tiver uma ou duas linhas, deixe-o no corpo da página ([GOV.UK](https://design-system.service.gov.uk/patterns/contact-a-department-or-service-team/)).

**Faça** deixar visível a ajuda que a maioria precisa para responder.

**Não faça** esconder em tooltip uma instrução longa que quase todos precisam.

#### Acessibilidade

O acesso à ajuda fica na mesma posição em todas as telas, o que atende ao critério WCAG 2.2, 3.2.6 (Ajuda consistente). O botão de informação entra na ordem de tabulação e tem nome acessível que combina o rótulo e "mais informações" ([Fluent](https://fluent2.microsoft.design/components/web/react/core/infolabel/usage)). Conteúdo que aparece ao passar o ponteiro ou focar precisa poder ser dispensado, permanecer visível enquanto o ponteiro estiver sobre ele e não sumir sozinho (WCAG 2.2, 1.4.13). Garanta o alvo mínimo de 24 por 24 pixels CSS do critério WCAG 2.2, 2.5.8; no Trama, prefira `--c-touch`.

> **Divergência entre referências** O gov.br recomenda tooltip para ajuda contextual curta e modal para ajuda rica; DKFDS e Fluent abrem a ajuda contextual por clique, porque o passar do ponteiro não existe em telas de toque. Pelo critério de acessibilidade, o Trama usa popover aberto por botão para ajuda curta e reserva o tooltip para nomear controles. Para ajuda rica, o Trama aceita o diálogo do gov.br e prefere o drawer quando a pessoa precisa ver a tarefa enquanto lê.

### Considerações por plataforma

#### Web desktop

Tooltips aparecem quando o ponteiro repousa sobre o elemento e também no foco do teclado ([HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help)). Ofereça texto diferente para estados diferentes de um mesmo controle, quando isso ajudar. Use tooltip de expansão para mostrar o valor completo de um campo truncado ([HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data)).

#### Web móvel

Ajuda e envio de opinião podem ficar num menu flutuante ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)); no Trama, no menu do cabeçalho compacto, sempre alcançável. Não há passar o ponteiro em telas de toque. Toda informação de tooltip precisa estar disponível de outro jeito: rótulo visível, botão de informação que abre por toque ou texto na página. O DKFDS abre tooltips de ajuda com clique num ícone por esse motivo ([DKFDS](https://designsystem.dk/komponenter/tooltip/)). Tooltips longos causam problemas em telas pequenas, onde podem não caber ([DKFDS](https://designsystem.dk/komponenter/tooltip/)).

#### Tablets e dobráveis

Em telas grandes, o popover de ajuda aparece perto do elemento tocado, para reduzir o deslocamento do dedo ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Uma página de ajuda extensa pode abrir num painel lateral, ao lado da tarefa, em vez de substituí-la.

### Recursos

#### Relacionados

- Onboarding
- Tooltips
- Popovers
- Acordeão
- Entrada de dados
- Escrita e conteúdo
- Coletar feedback
- Cabeçalho

#### Referências

- [Ajuda e comunicação](https://www.gov.br/ds/padroes/design/ajuda-comunicacao) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help) Apple HIG
- [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data) Apple HIG
- [Info label](https://fluent2.microsoft.design/components/web/react/core/infolabel/usage) Fluent 2
- [Popover](https://fluent2.microsoft.design/components/web/react/core/popover/usage) Fluent 2
- [Details](https://design-system.service.gov.uk/components/details/) GOV.UK Design System
- [Inset text](https://design-system.service.gov.uk/components/inset-text/) GOV.UK Design System
- [Contact a department or service team](https://design-system.service.gov.uk/patterns/contact-a-department-or-service-team/) GOV.UK Design System
- [Question pages](https://design-system.service.gov.uk/patterns/question-pages/) GOV.UK Design System
- [Tooltip](https://designsystem.dk/komponenter/tooltip/) Det Fælles Designsystem
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta os tipos global, contextual e não solicitada, o acesso à ajuda em todas as telas, a iconografia de ajuda, a ajuda rica em diálogo ou drawer e o caminho para enviar opinião. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                           |

## Onboarding

Onboarding ajuda as pessoas a começar; no Trama ele é curto, opcional e distribuído ao longo do uso, perto das tarefas que ensina.

O ideal é que o produto se explique pelo próprio uso. Quando for preciso orientar, o fluxo deve ser rápido e opcional ([HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)). O Fluent trata onboarding como momentos de aprendizado espalhados pela jornada, em vez de um evento único no primeiro acesso ([Fluent](https://fluent2.microsoft.design/onboarding)). O Trama segue essa visão.

Quando um tour for a melhor forma de ensinar, como ao apresentar novidades de uma versão, o Trama usa a estrutura do gov.br: tela de boas-vindas, poucas etapas, opção de pular em todas elas e tela de conclusão ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)). Onboarding começa depois que a primeira tela está pronta e não faz parte do carregamento inicial ([HIG](https://developer.apple.com/design/human-interface-guidelines/launching)). As regras de espera estão em Carregamento e espera.

### Boas práticas

**Siga os cinco princípios.** Todo momento de onboarding do Trama é ([Fluent](https://fluent2.microsoft.design/onboarding)):

- **Relevante:** aparece dentro de uma tarefa relacionada ao que ensina.
- **Discreto:** não bloqueia o objetivo principal da pessoa.
- **Opcional:** pode ser dispensado e reaberto depois.
- **Focado no benefício:** diz logo o que a pessoa ganha, para merecer atenção.
- **Coerente:** usa componentes padrão do sistema.

**Ensine pela interação.** As pessoas aprendem e lembram mais quando executam a tarefa do que quando só leem sobre ela. Sempre que possível, ofereça um jeito seguro de testar a ação ([HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)). Conteúdo inicial de exemplo, com o qual a pessoa pode mexer, é uma forma de fazer isso ([Geist](https://vercel.com/geist/empty-state)).

**Prefira dicas contextuais a um fluxo único.** Uma dica junto à área que descreve ajuda a pessoa a se concentrar numa tarefa por vez e a aprender enquanto avança ([HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)). As regras de redação e frequência de dicas estão em Oferecer ajuda.

**Não use onboarding para tarefas do negócio nem para fluxos longos.** Envio de formulários e funcionalidades do serviço ficam fora do tour. Se o conteúdo for longo ou complexo, ponha-o na ajuda ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)).

**Escolha o formato pelo objetivo.**

| Objetivo                                                     | Formatos do Trama                                                             |
|--------------------------------------------------------------|-------------------------------------------------------------------------------|
| Dar boas-vindas e confirmar que a pessoa está no lugar certo | Tela curta, banner ou diálogo, mostrados uma única vez                        |
| Orientar sobre onde as coisas estão                          | Estado vazio ou popover de dica                                               |
| Anunciar um recurso novo ou alterado                         | Banner, estado vazio, popover de dica ou toast                                |
| Evitar que a pessoa fique travada                            | Dica na própria interface e estado vazio                                      |
| Guiar uma configuração obrigatória                           | Experiência de primeiro uso, assistente em etapas ou drawer com várias etapas |

A tabela adapta os cenários do Fluent ([Fluent](https://fluent2.microsoft.design/onboarding)).

#### Tours

**Escolha entre os dois tipos de tour.** O tour com ênfase na interface destaca elementos reais da tela, um por etapa, com um popover ancorado ao elemento. O tour com ênfase textual usa só texto e imagem, num diálogo com etapas, para novidades e vantagens. Os dois usam o véu `--t-overlay` para levar a atenção ao conteúdo do tour ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)).

**Comece com boas-vindas que digam o que vem.** A tela de boas-vindas resume o conteúdo do tour para que a pessoa decida rápido se quer seguir ou sair. Evite boas-vindas só por cortesia; combine a saudação com algo útil, como o acesso ao cadastro ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)). As etapas só começam quando a pessoa escolhe começar.

**Use poucas etapas e permita voltar.** Pessoas tendem a desistir diante de muitas etapas. Ofereça "Voltar" e "Próximo" em todas elas ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)) e mostre o progresso com o indicador de etapas, que também pode servir para ir direto a uma etapa. "Próximo" vale aqui porque o tour é leitura passiva; na última etapa, use "Concluir".

**Mantenha "Pular" visível do início ao fim.** Use um link "Pular tour" no mesmo lugar em todas as telas, da boas-vindas à conclusão ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)). Esc também encerra o tour.

**Termine com uma tela de conclusão.** Feche o tour com um texto curto e o próximo passo, como um botão para o recurso apresentado ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)). Diga onde reencontrar o tour.

**Ofereça não mostrar o tour novamente.** Quando um tour de novidades aparece por um período, inclua um checkbox para ocultá-lo nas próximas visitas ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)). Escreva o rótulo no positivo, "Ocultar este tour nas próximas visitas" ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). Pular ou concluir também conta como tour visto.

**Posicione os controles na base.** No tour com ênfase na interface, os controles ficam na base da tela; quando o elemento destacado estiver na base, eles sobem para o centro ou o topo. O popover acompanha o elemento destacado ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)).

**Ligue o tour à ajuda.** Inclua em cada etapa complexa um link para a seção de ajuda correspondente ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)).

**Quando um fluxo prévio for indispensável, faça-o curto.** Não peça que a pessoa memorize muita coisa. Quem tenta ensinar demais sobrecarrega e reduz o que se lembra depois ([HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)). Priorize a ação principal do produto ou a que gera mais engajamento ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)).

**Torne tutoriais opcionais e fáceis de reencontrar.** Se a pessoa pular o tutorial, não o mostre de novo nos acessos seguintes. Deixe-o disponível na ajuda, na conta ou nas configurações ([HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)).

**Não inicie as etapas automaticamente.** Um botão "Iniciar tour" sempre vem acompanhado de "Pular" ([Geist](https://vercel.com/geist/empty-state)).

**Ensine apenas o seu produto.** A pessoa veio aprender o que o produto faz. Não explique como usar o sistema operacional ou componentes padrão ([HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)).

**Adie configurações que não são essenciais.** Ofereça padrões razoáveis para que a maioria comece a usar o produto sem configurar nada ([HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)). Veja Configurações.

**Peça permissões no momento em que fazem sentido.** Se o produto não funcionar sem um acesso, como notificações ou localização, o onboarding é a chance de explicar o motivo e o benefício. Caso contrário, peça a permissão quando a pessoa usar pela primeira vez o recurso que depende dela ([HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)). Veja Notificações e Privacidade.

**Deixe a pessoa usar o produto antes de pedir avaliação ou compra.** Pedidos assim têm resposta melhor depois que a pessoa se envolveu com o produto ([HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)). Não ponha termos de licença no meio do fluxo de boas-vindas; se forem obrigatórios, integre-os sem interromper a experiência ([HIG](https://developer.apple.com/design/human-interface-guidelines/onboarding)).

**Não use telas de abertura como vitrine.** Se houver uma tela de marca, mostre-a apenas o tempo de ser compreendida de relance, no início do onboarding ([HIG](https://developer.apple.com/design/human-interface-guidelines/launching)). Na web, a primeira tela útil é a melhor apresentação.

**Volte para onde a pessoa parou.** Ao retornar, restaure o estado anterior com o máximo de detalhe, incluindo a posição de rolagem, para que ninguém refaça o caminho ([HIG](https://developer.apple.com/design/human-interface-guidelines/launching)).

#### Conteúdo

**Escreva para a ação.** Use voz ativa e verbos fortes, e coloque o texto onde a pessoa precisa dele. Diga o que vai acontecer e quanto tempo leva, sem surpresas desagradáveis. Ofereça ajuda no momento certo ([Fluent](https://fluent2.microsoft.design/onboarding)), com links que nomeiam o destino em vez de "Saiba mais" ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)).

**Ajuste o tom ao objetivo.** O tom pode ser de ensino, de divulgação ou técnico, conforme o conteúdo ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)), sempre dentro da voz do produto.

**Comece pelo benefício.** "Salve os filtros que você mais usa" explica o ganho; "Novo: filtros salvos" só anuncia o recurso. O botão principal nomeia a ação, como "Experimentar" ou "Configurar agora", e o secundário dispensa: "Agora não".

**Faça** um convite dispensável, com benefício, tempo esperado e uma ação clara.

**Não faça** tour modal longo, obrigatório e sem opção de pular.

#### Acessibilidade

O tour textual é um diálogo modal: ao abrir uma etapa, o foco vai para a ação principal, "Próximo" (D13), e Esc encerra o tour devolvendo o foco ao elemento de onde ele partiu. O texto de "Etapa 2 de 3" é lido junto com o título. No tour com ênfase na interface, o popover recebe nome pelo título e a área destacada continua alcançável pelo teclado. Em telas pequenas, os botões circulares de navegação (`.tr-btn--circle`) têm `aria-label` "Voltar" e "Próximo".

> **Divergência entre referências** Formato: HIG e Fluent preferem dicas espalhadas pela jornada, e o Geist pede não iniciar tours sozinhos; o gov.br estrutura o onboarding como tour com boas-vindas e véu. O Trama mantém as dicas contextuais como padrão e adota a estrutura do gov.br quando um tour for necessário, com as etapas iniciadas só pela pessoa. Desativação: a HIG pede não mostrar de novo o tutorial pulado; o gov.br oferece um checkbox para não ver mais o tour. O Trama aplica os dois: pular ou concluir marca o tour como visto, e o checkbox atende tours de novidades exibidos por um período.

### Considerações por plataforma

#### Web desktop

Popovers de dica ficam ancorados no controle descrito e não cobrem o conteúdo de que a pessoa precisa ao mesmo tempo ([Fluent](https://fluent2.microsoft.design/components/web/react/core/popover/usage)). Esc fecha a dica e devolve o foco ao controle.

#### Web móvel

Em telas compactas, um popover ancorado pode cobrir boa parte da tela. Prefira dicas na própria interface ou um banner no topo do conteúdo. No grid de 4 colunas e no tour textual, use botões circulares para voltar e avançar ([gov.br](https://www.gov.br/ds/padroes/design/onboarding)), com alvo de `--c-touch`. Fluxos de várias etapas usam uma etapa por tela, com o botão principal ao alcance do polegar.

#### Tablets e dobráveis

Em telas grandes, mostre etapas de configuração curtas como um painel ou pop-up perto do que a pessoa tocou, mantendo a tela anterior visível ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Se a pessoa abrir ou fechar o dobrável durante o onboarding, mantenha a etapa atual e o que já foi digitado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Oferecer ajuda
- Estados vazios
- Carregamento e espera
- Configurações
- Popovers
- Indicador de etapas
- Diálogos

#### Referências

- [Onboarding](https://www.gov.br/ds/padroes/design/onboarding) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding) Apple HIG
- [Launching](https://developer.apple.com/design/human-interface-guidelines/launching) Apple HIG
- [Onboarding](https://fluent2.microsoft.design/onboarding) Fluent 2
- [Popover](https://fluent2.microsoft.design/components/web/react/core/popover/usage) Fluent 2
- [Empty State](https://vercel.com/geist/empty-state) Geist
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a estrutura de tour (boas-vindas, etapas, pular, conclusão), os dois tipos de tour, a opção de não mostrar novamente e as regras de foco. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                        |

## Pesquisa

A pesquisa leva a pessoa direto ao que procura quando ela sabe o nome do que quer ou não encontra o caminho pela navegação.

Pesquisa e navegação se complementam. A pesquisa atende quem conhece as palavras certas e quem não consegue ou não quer usar menus ([DKFDS](https://designsystem.dk/komponenter/search/)). Produtos muito pequenos, de uma página só, não precisam dela.

Esta página trata da experiência completa: onde a pesquisa fica, o que acontece enquanto a pessoa digita, como os resultados aparecem, como filtrá-los e o que mostrar quando nada é encontrado. O componente em si está em Campo de pesquisa. O Trama usa o verbo "Pesquisar" em botões, rótulos e textos.

### Boas práticas

#### Posição e escopo

**Se a pesquisa é importante, dê a ela uma posição de destaque.** Mostre o campo completo na página inicial do produto, sem reduzi-lo a um link ou ícone ([HIG](https://developer.apple.com/design/human-interface-guidelines/searching), [DKFDS](https://designsystem.dk/komponenter/search/)). Quando a pesquisa for a tarefa principal da página, use o campo em destaque, `.tr-input--feature`, mais alto e com raio maior ([gov.br](https://www.gov.br/ds/components/input)). Na web, o canto superior direito do cabeçalho é onde as pessoas procuram a pesquisa global ([DKFDS](https://designsystem.dk/komponenter/search/)).

**Ofereça um único lugar para pesquisar tudo.** As pessoas gostam de ter um ponto identificado para achar qualquer coisa. Seções muito distintas podem ter uma pesquisa local que funciona como filtro da visão atual ([HIG](https://developer.apple.com/design/human-interface-guidelines/searching)). Posicione a pesquisa local logo acima da lista que ela filtra, para mostrar a relação ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)).

**Deixe claro o escopo atual.** Use um rótulo, um título ou filtros visíveis para dizer onde a pesquisa acontece, por exemplo "Pesquisar processos" ([HIG](https://developer.apple.com/design/human-interface-guidelines/searching)). O rótulo acessível é obrigatório, porque um placeholder some ao digitar. Se a pesquisa precisar de instruções, ponha-as acima do campo ([DKFDS](https://designsystem.dk/komponenter/search/)).

**Comece com o escopo mais amplo.** O escopo amplo mostra o conjunto completo de resultados e orienta a pessoa quando ela decidir estreitar ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)). Ofereça a pesquisa avançada como opção; a principal é sempre a simples ([DKFDS](https://designsystem.dk/komponenter/search/)).

#### O campo

**Faça o campo parecer um campo de pesquisa e largo o bastante.** Use `.tr-search`, com ícone de lupa e largura para pelo menos 27 caracteres, já que a maioria das pesquisas tem duas palavras ou mais ([DKFDS](https://designsystem.dk/komponenter/search/)).

**Mostre o botão de limpar só quando houver texto.** ([Fluent](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage)). Esc também limpa o campo quando ele está em foco. Ações internas do campo, como limpar e pesquisar, são alcançáveis pelo teclado ([gov.br](https://www.gov.br/ds/components/input)).

**Escreva "Pesquisar" no botão ou no nome acessível.** Se o botão mostrar só a lupa, o nome acessível diz "Pesquisar". O botão de envio é um `submit` real e o campo tem rótulo, mesmo que visualmente oculto ([DKFDS](https://designsystem.dk/komponenter/search/)). Envolva o formulário em `role="search"`.

**Ofereça um atalho de teclado para a pesquisa global e mostre-o no campo.** O Geist exibe o atalho ⌘K e a tecla Esc dentro do próprio campo ([Geist](https://vercel.com/geist/search-input)). No Trama, use Ctrl+K no Windows e no Linux e ⌘K no macOS, e Esc para fechar.

#### Enquanto a pessoa digita

**Mostre pesquisas recentes e sugestões.** Ao focar o campo, mostre pesquisas recentes; ao digitar, troque-as por sugestões que antecipam o termo ([Fluent](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage), [HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)). Sugestões que toleram erros de digitação e incluem termos relacionados ajudam quem não sabe o termo exato ([One UI](https://developer.samsung.com/one-ui/comp/search.html)); associe assuntos relacionados ao termo, inclusive quando não houver sugestão direta ([gov.br](https://www.gov.br/ds/components/input)). Use o padrão de combobox para a lista.

**Ordene as sugestões de forma previsível.** Para listas de nomes, como cidades, órgãos ou pessoas, use ordem alfabética ([gov.br](https://www.gov.br/ds/components/input)). Para termos de pesquisa livres, ponha primeiro o que tem mais chance de levar ao resultado.

**Diga quando não houver sugestão.** Mostre o aviso no lugar da lista, como "Nenhuma sugestão para “licensa”", em vez de fechá-la sem explicação ([gov.br](https://www.gov.br/ds/components/input)).

**Proteja o histórico de pesquisa.** Antes de exibir pesquisas anteriores, pense em quem mais pode ver a tela. Se mostrar o histórico, ofereça um jeito de apagá-lo ([HIG](https://developer.apple.com/design/human-interface-guidelines/searching)). Veja Privacidade.

**Pesquise enquanto a pessoa digita quando os resultados forem rápidos.** Resultados que se refinam a cada letra dão sensação de resposta imediata ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)); atualize as sugestões o mais rápido possível e mostre um indicador de carregamento se houver espera ([gov.br](https://www.gov.br/ds/components/input)). Quando a pesquisa for lenta ou cara, espere o envio. Durante a espera, mostre o indicador dentro do campo, onde o texto do resultado vai aparecer ([Ontario](https://designsystem.ontario.ca/components/detail/loading-indicator.html)), ou na área de resultados, seguindo Carregamento e espera.

#### Resultados

**Mantenha o termo visível na página de resultados.** O campo continua preenchido com o que a pessoa pesquisou, para que ela possa ajustar sem redigitar ([DKFDS](https://designsystem.dk/komponenter/search/)).

**Ponha os resultados mais relevantes primeiro.** Minimize a rolagem até o que a pessoa procura e considere agrupar resultados por categoria ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields), [Fluent](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage)). Cada resultado mostra título, tipo e um dado que ajude a decidir, como data ou situação.

**Permita filtrar e mostre os filtros ativos.** Filtros por categoria ajudam a ir do amplo ao específico ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)). No Trama, cada filtro ativo vira um chip removível, equivalente aos tokens da HIG, que representam um termo como item único editável. Combine filtros com sugestões para que a pessoa descubra quais existem ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)).

**Anuncie a quantidade de resultados.** Mostre "24 processos encontrados" num elemento com `role="status"`, para que leitores de tela saibam que a lista mudou (WCAG 2.2, 4.1.3).

#### Nenhum resultado

**Trate a pesquisa sem resultados como um estado vazio por ação da pessoa.** Substitua a lista inteira pelo estado vazio, no lugar onde os resultados apareceriam ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)). Repita o termo pesquisado entre aspas e diga o que fazer: "Nenhum processo encontrado para “licença ambental”. Confira a grafia ou remova filtros." ([Geist](https://vercel.com/geist/empty-state)). Ofereça "Limpar filtros" como ação e, se houver, um link para a ajuda sobre como pesquisar ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)). Veja Estados vazios.

**Ofereça a pesquisa também nas páginas de erro.** Numa página não encontrada, um campo de pesquisa na área de conteúdo ajuda a pessoa a se orientar ([gov.br](https://www.gov.br/ds/templates/erro)). Veja Modelos de página.

**Faça** campo largo, com rótulo que define o escopo.

**Não faça** campo estreito demais para ver o termo e instrução genérica dentro do campo.

> **Divergência entre referências** Ordem das sugestões: o gov.br pede ordem alfabética nas sugestões do autocompletar; HIG e Fluent priorizam a relevância nos resultados. O Trama usa ordem alfabética em listas de nomes, em que a pessoa sabe o que procura e a ordem previsível ajuda a localizar, e relevância em termos livres. Vocabulário: as referências em inglês usam "search"; o gov.br alterna entre "busca" e "pesquisa". O Trama padroniza "Pesquisar" (D7).

### Considerações por plataforma

#### Web desktop

Coloque a pesquisa global no cabeçalho, à direita, como campo aberto a partir da classe Expandida, de 12 colunas ([gov.br](https://www.gov.br/ds/components/header)). Em produtos com vários painéis, a pesquisa na barra de ferramentas permite navegar pelos resultados mantendo a seleção visível no detalhe; a pesquisa no topo da navegação lateral filtra a própria navegação ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)).

#### Web móvel

Em telas compactas, o campo recolhe para um botão com lupa. Ao acioná-lo, o campo ocupa a largura do cabeçalho, recebe o foco e ganha um botão circular para fechar; fechar devolve o cabeçalho ao estado anterior ([gov.br](https://www.gov.br/ds/components/header), [Fluent](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage)). Use `type="search"` para que o teclado virtual mostre a tecla de pesquisa. Planeje o comportamento do campo com zoom de 400% ([Fluent](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage)).

#### Tablets e dobráveis

Na classe Média, de 8 colunas, o cabeçalho usa o mesmo comportamento de lupa que expande ([gov.br](https://www.gov.br/ds/components/header)). Numa área dedicada à pesquisa, dê foco ao campo ao chegar, exceto quando só houver teclado virtual: nesse caso o teclado cobriria a tela sem aviso ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)). Quando a janela encolher, mantenha a pesquisa acima da coluna de lista. Em dois painéis, os resultados ficam no painel da lista e o item escolhido abre no painel de detalhe.

### Recursos

#### Relacionados

- Campo de pesquisa
- Combobox
- Tags e chips
- Estados vazios
- Carregamento e espera
- Paginação
- Cabeçalho

#### Referências

- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Header](https://www.gov.br/ds/components/header) gov.br DS
- [Empty states](https://www.gov.br/ds/padroes/design/emptystates) gov.br DS
- [Template de erro](https://www.gov.br/ds/templates/erro) gov.br DS
- [Searching](https://developer.apple.com/design/human-interface-guidelines/searching) Apple HIG
- [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields) Apple HIG
- [Search box](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage) Fluent 2
- [Søgefelt](https://designsystem.dk/komponenter/search/) Det Fælles Designsystem
- [Search Input](https://vercel.com/geist/search-input) Geist
- [Empty State](https://vercel.com/geist/empty-state) Geist
- [Search](https://developer.samsung.com/one-ui/comp/search.html) Samsung One UI
- [Loading indicator](https://designsystem.ontario.ca/components/detail/loading-indicator.html) Ontario Design System

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                           |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. A página passa a se chamar "Pesquisa" (D7) e acrescenta o campo em destaque, a pesquisa que expande no cabeçalho, a ordem e o aviso de sugestões, o estado vazio sem resultados e a pesquisa em páginas de erro. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                    |

## Configurações

Configurações permitem ajustar o produto às necessidades de cada pessoa; os bons padrões fazem com que a maioria nunca precise abri-las.

As pessoas esperam que o produto funcione bem desde o início e gostam de poder personalizá-lo. O Trama separa as configurações em dois lugares: uma área de configurações para opções gerais, raramente alteradas, e controles dentro da própria tarefa para opções que afetam só aquela tela ([HIG](https://developer.apple.com/design/human-interface-guidelines/settings)).

Em produtos web, a área de configurações também concentra escolhas que envolvem privacidade e consentimento, como notificações e cookies. Essas escolhas seguem regras próprias, descritas mais abaixo.

### Boas práticas

**Escolha padrões que sirvam à maioria.** Bons padrões permitem começar sem ajustar nada ([HIG](https://developer.apple.com/design/human-interface-guidelines/settings)). Antes de criar uma opção, pergunte se um padrão melhor resolveria o problema para todos.

**Ofereça poucas configurações.** Configurações demais deixam o produto menos acessível e tornam difícil achar a opção certa ([HIG](https://developer.apple.com/design/human-interface-guidelines/settings)).

**Não pergunte o que dá para detectar.** O produto pode detectar, por exemplo, se o sistema está no modo escuro ([HIG](https://developer.apple.com/design/human-interface-guidelines/settings)). O Trama estende a regra ao idioma do navegador e à preferência de movimento reduzido. Veja Modo escuro e Movimento.

**Respeite as preferências do sistema e do navegador.** Não crie versões próprias de ajustes globais, como tamanho de texto, contraste ou leitura de tela. Uma cópia local sugere que o ajuste do sistema não vale para o seu produto e confunde ([HIG](https://developer.apple.com/design/human-interface-guidelines/settings)). Quando o produto oferecer o tema como opção, inclua "Usar o tema do sistema" e deixe-o como padrão.

**Ponha na área de configurações só o que é geral e raro.** Abrir as configurações interrompe o trabalho, então ali ficam opções que não mudam toda hora, como conta, idioma e notificações ([HIG](https://developer.apple.com/design/human-interface-guidelines/settings)).

**Deixe opções de uma tarefa na própria tarefa.** Mostrar ou ocultar colunas, reordenar uma lista ou filtrar resultados são ajustes que ficam na tela que afetam, onde são fáceis de achar e o efeito aparece na hora ([HIG](https://developer.apple.com/design/human-interface-guidelines/settings)). Use a barra de ferramentas ou um menu de exibição.

**Abra as configurações do jeito que as pessoas esperam.** O acesso fica no menu da conta, no canto superior direito, e no rodapé da navegação lateral. Em produtos de uso intenso, ofereça um atalho de teclado; a HIG cita Command-vírgula como o atalho que as pessoas usam para abrir configurações ([HIG](https://developer.apple.com/design/human-interface-guidelines/settings)). Verifique se o atalho não conflita com o do navegador.

#### Organização

**Agrupe por assunto e mantenha a estrutura estável.** Cada grupo vira uma seção com título que nomeia a área, como "Notificações" ou "Privacidade". A navegação entre seções fica sempre visível e indica a seção atual ([HIG](https://developer.apple.com/design/human-interface-guidelines/settings)). Atualize o título da página para refletir a seção aberta e, ao voltar, reabra a última seção usada ([HIG](https://developer.apple.com/design/human-interface-guidelines/settings)).

**Ofereça pesquisa quando houver muitas configurações.** Uma pesquisa no topo da navegação lateral filtra as seções e leva direto à opção, mesmo que ela esteja vários níveis abaixo ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)). Veja Pesquisa.

**Retire o que a pessoa não pode mudar.** Se uma opção depende de algo fora do alcance da pessoa, como uma permissão que ela não tem, não a mostre. Se depende de uma ação dela, como confirmar o e-mail, mostre a opção desabilitada e diga ao lado o que fazer para habilitá-la.

**Mantenha a ajuda à mão.** O acesso à ajuda continua no cabeçalho, como em todas as telas, e opções de efeito pouco óbvio trazem uma dica ou um link para o tópico de ajuda correspondente ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Veja Oferecer ajuda.

#### Salvar mudanças

**Aplique na hora as escolhas independentes.** Um switch liga ou desliga algo imediatamente, sem botão de salvar. Mostre "Salvo" perto do controle quando o salvamento depender de rede, e desfaça a mudança com uma mensagem de erro se ela falhar.

**Use um botão "Salvar alterações" para mudanças em grupo.** Quando várias respostas só fazem sentido juntas, como um endereço ou uma troca de e-mail, mostre os dados com um acionador "Alterar" e, em modo de edição, ofereça salvar e cancelar ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Veja Entrada de dados. Avise antes de sair da página com alterações não salvas. Depois de salvar, confirme com uma mensagem de sucesso no topo, para que a pessoa possa voltar ao que fazia ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)). A confirmação diz o que mudou, como "Endereço atualizado".

**Ofereça "Restaurar padrões" longe do botão de salvar.** Quando uma seção tiver muitas opções, permita voltar aos valores padrão com um link no fim da seção, separado das ações de salvar. Como a ação desfaz várias escolhas de uma vez, ofereça desfazer logo depois. Veja Desfazer e refazer.

#### Notificações e consentimento

**Deixe a pessoa gerenciar as notificações dentro do produto.** Notificações são opcionais: cada pessoa decide se quer recebê-las ([gov.br](https://www.gov.br/ds/components/notification)). Ao pedir permissão para enviar notificações, informativas ou de marketing, ofereça também uma tela de configurações onde a escolha possa ser mudada ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-notifications)). Descreva os tipos de mensagem e dê um jeito claro de aceitar ou recusar cada um. Veja Notificações.

**Comece o consentimento desmarcado.** Na primeira visita, as opções de cookies não essenciais começam em "não". Se a pessoa já escolheu, mostre a escolha salva ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)). O Trama aplica a mesma regra a comunicações de marketing e a todo consentimento previsto na LGPD ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Peça consentimento por finalidade, com o controle junto ao texto.** Ofereça uma opção para cada uso dos dados, com o checkbox ou o switch imediatamente junto à descrição do uso. Explique como retirar o consentimento e permita retirá-lo no mesmo lugar onde foi dado ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Veja Privacidade.

**Escreva a política de privacidade em linguagem simples.** Evite termos técnicos e jurídicos e divida o conteúdo por assunto, para que seja fácil de escanear ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Mantenha uma página de cookies própria e clara.** Liste cada cookie na sua categoria (essenciais, funcionais, de análise) com nome, finalidade, quem o define, se for de terceiros, e quando expira. Não esconda a política em termos de uso. Ligue a página no rodapé e no banner de cookies ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)). Veja Consentimento de cookies. Peça consentimento de novo quando passar a usar um novo tipo de cookie não essencial ou mudar o uso dos dados ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)). Produtos para o público brasileiro seguem a Lei nº 13.709/2018 (LGPD); envolva a área responsável por privacidade na redação. Veja Legislação e normas.

**Funcione sem JavaScript quando o consentimento depender dele.** Se o controle de cookies exigir JavaScript, mostre uma versão alternativa da página com instruções em texto ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)).

#### Conteúdo

Rótulos de switches descrevem o estado ligado em termos do que a pessoa ganha ("Avisar quando um processo mudar de situação"), em frase positiva e nunca com negação dupla ("Não desativar avisos") ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). Se uma opção tiver consequência pouco óbvia, explique-a numa dica abaixo do controle. Use caixa de frase, com maiúscula só na primeira palavra e em nomes próprios. Títulos de seção nomeiam a área, como "Notificações", e botões têm até duas palavras, sem artigo: "Salvar alterações".

> **Divergência entre referências** O gov.br pede evitar botões "Redefinir" e "Limpar formulário" em formulários; a versão 1.0 do Trama oferecia "Restaurar padrões" com confirmação, sem apoio explícito das outras referências. Reavaliada, a regra fica restrita a seções de configuração com muitas opções, como link afastado do botão de salvar e com desfazer, porque voltar aos padrões é uma necessidade real em configurações extensas; "Limpar formulário" fica proibido em formulários de tarefa. Consentimento: o 1.0 usava botões de opção "Quero receber" e "Não quero receber"; o gov.br recomenda checkbox ou switch junto ao texto e rótulos positivos. O Trama passa a usar um switch desligado por finalidade.

**Faça** rótulo afirmativo que descreve o efeito do estado ligado.

**Não faça** rótulo com negação que obriga a pessoa a decifrar o que ligar significa.

### Considerações por plataforma

#### Web desktop

Use dois painéis: seções à esquerda, opções à direita. A navegação de seções não muda de lugar nem de ordem. Separe grupos de opções com `--f-gap-group` e opções do mesmo grupo com `--f-gap-field`. Configurações que valem só para um documento ficam no próprio documento.

#### Web móvel

Em telas compactas, mostre primeiro a lista de seções e abra cada seção numa nova tela, com o link de voltar no topo. Mantenha cada linha de switch com altura mínima de `--c-touch` e o rótulo inteiro clicável.

#### Tablets e dobráveis

A partir da classe Média, use dois painéis com a lista de seções sempre visível, na proporção de painéis do Trama ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Uma lista de configurações não precisa mudar de layout em postura de mesa (Flex) ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Ao abrir ou fechar o dobrável, mantenha a seção aberta e a posição de rolagem.

### Recursos

#### Relacionados

- Switch
- Navegação lateral
- Painéis e split view
- Notificações
- Privacidade
- Contas e autenticação
- Onboarding
- Consentimento de cookies

#### Referências

- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Notification](https://www.gov.br/ds/components/notification) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Ajuda e comunicação](https://www.gov.br/ds/padroes/design/ajuda-comunicacao) gov.br DS
- [Settings](https://developer.apple.com/design/human-interface-guidelines/settings) Apple HIG
- [Managing notifications](https://developer.apple.com/design/human-interface-guidelines/managing-notifications) Apple HIG
- [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields) Apple HIG
- [Cookies page](https://design-system.service.gov.uk/patterns/cookies-page/) GOV.UK Design System
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta consentimento por finalidade com switch desligado, retirada de consentimento, política em linguagem simples, edição com salvar e cancelar, a regra D9 para opções indisponíveis e a nova posição de "Restaurar padrões". |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                       |

## Desfazer e refazer

Permita reverter ações recentes de forma previsível, para que as pessoas possam explorar e corrigir enganos sem medo, e reserve confirmações para o que não pode ser desfeito.

Desfazer e refazer dão às pessoas um jeito fácil de reverter muitos tipos de ação e as ajudam a explorar uma interface com segurança ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)). As pessoas costumam desfazer várias vezes seguidas e nem sempre lembram qual ação está sendo revertida. Por isso, o resultado de cada desfazer precisa ser previsível e visível ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)).

No Trama, desfazer aparece em três formatos: o **histórico de edição**, em editores, com atalhos de teclado e botões na barra de ferramentas; o **desfazer pontual**, em um toast ou em uma mensagem logo após uma ação como arquivar, mover, excluir ou substituir um arquivo; e o **cancelamento de edição**, que descarta alterações ainda não salvas.

### Boas práticas

**Prefira desfazer a pedir confirmação.** Não interrompa com alertas ações comuns que podem ser desfeitas, mesmo destrutivas, como excluir uma mensagem ([HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)). Confirmar toda ação treina as pessoas a clicar sem ler.

**Ajude a prever o resultado.** Nomeie a ação no rótulo ou na dica do controle: "Desfazer digitação", "Refazer negrito" ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)). Use uma ou duas palavras depois de "Desfazer" ou "Refazer".

**Mostre o resultado.** Se a ação desfeita afetou uma área fora da tela, role até ela e destaque o conteúdo restaurado ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)). O destaque usa `--t-brand-subtle`, que se dissipa em `--m-slower`; com `prefers-reduced-motion` ou com as animações desligadas no produto, aparece e some sem transição.

**Permita desfazer várias vezes** desde um marco lógico, como abrir o documento ou salvar ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)).

**Agrupe ajustes pequenos e relacionados,** como arrastar um controle deslizante, em um único passo, e ofereça "Reverter para a última versão salva" quando fizer sentido ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)).

**Mostre botões de desfazer e refazer só quando necessários.** As pessoas esperam usar os atalhos de teclado. Se o produto precisar de botões, coloque-os na barra de ferramentas ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)). Em celulares, sem teclado físico, os botões são necessários em editores. Quando não houver nada a refazer, a pessoa pode habilitar Refazer desfazendo algo: mostre o botão desabilitado e explique por quê.

**Ofereça desfazer depois de arrastar e soltar,** porque é comum soltar no lugar errado ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

#### Desfazer pontual

**Use o desfazer pontual só quando a reversão for segura.** Escreva a mensagem dizendo o que mudou, no particípio, como "Projeto arquivado", e ofereça uma única ação com o rótulo "Desfazer" ([Geist](https://vercel.com/geist/toast)). Não use "Restaurar" ou "Cancelar" nesse lugar.

**Mantenha o aviso com Desfazer até a pessoa fechar.** Um toast com ação não some sozinho. Ele sai quando a pessoa fecha, quando aciona Desfazer ou quando uma nova ação do mesmo tipo o substitui. Enquanto estiver aberto, aceite também Ctrl+Z (Cmd+Z no macOS).

**Não dependa só do toast.** Elementos temporários somem antes que pessoas que usam teclado ou leitor de tela os alcancem ([Geist](https://vercel.com/geist/toast)). Mantenha outro caminho de recuperação, como uma lixeira com "Restaurar".

> **Divergência entre referências** O Geist mantém o toast com Desfazer visível por 5 a 10 segundos. O Trama aplica a decisão D23: só toasts informativos sem ação somem sozinhos. Pelo critério de acessibilidade, uma ação que some com o tempo falha para quem precisa de mais tempo (WCAG 2.2, 2.2.1). Fontes: [Geist](https://vercel.com/geist/toast).

**Ao substituir um arquivo, avise e ofereça Desfazer.** Em campos que aceitam um só arquivo, um novo envio substitui o anterior, e uma mensagem de alerta informa a troca ([gov.br](https://www.gov.br/ds/components/upload)). Nomeie os dois arquivos e ofereça Desfazer, que restaura o anterior.

#### Cancelar uma edição

**Em modo de edição, ofereça Salvar e Cancelar.** Quando a pessoa edita dados já enviados, sinalize o que pode ser editado e, durante a edição, dê as opções de salvar e de cancelar as alterações ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Cancelar descarta só o que não foi salvo e volta ao valor anterior.

**Avise antes de perder dados em fluxos longos.** Em um assistente em etapas, Cancelar volta à tela anterior ao fluxo; avise que os dados preenchidos até ali serão perdidos ([gov.br](https://www.gov.br/ds/components/wizard)). Se houver alterações não salvas, use o único alerta do Trama com três ações: Salvar, Não salvar e Cancelar.

#### Quando não é possível desfazer

**Peça confirmação para ações destrutivas e irreversíveis.** Exiba um alerta quando a ação for incomum e não puder ser desfeita ([HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)). Use o botão de aviso só no passo final da confirmação, depois de um primeiro botão de outro estilo ([GOV.UK](https://design-system.service.gov.uk/components/button/)). Siga Modalidade.

**Escreva título e botões com o verbo da ação.** Use "Excluir projeto?" com os botões "Cancelar" e "Excluir", e nunca "Tem certeza?" com "Não" e "Sim" ([gov.br](https://www.gov.br/ds/components/modal)).

**Diga exatamente o que não poderá ser desfeito.** Escreva "Excluir o projeto Orçamento 2026 não pode ser desfeito." Se só parte da ação for irreversível, diga "Alguns efeitos não podem ser desfeitos." ([Geist](https://vercel.com/geist/destructive-action-modal)).

**Peça digitação para ações de alto impacto.** Para excluir um recurso de produção ou uma conta, peça que a pessoa digite o nome do recurso ([Geist](https://vercel.com/geist/destructive-action-modal)). Mantenha o botão Excluir habilitado: se o nome não conferir, mostre o erro no campo. Não use essa fricção em confirmações rotineiras.

> **Divergência entre referências** O Geist habilita o botão destrutivo só depois que o nome é digitado, e o gov.br aceita desativar a confirmação de modais até que os campos estejam preenchidos. O Ontario pede botões sempre habilitados, com tratamento de erro. O Trama aplica a decisão D9: o botão fica habilitado e a verificação acontece ao acionar, com uma mensagem que diz o que digitar. Fontes: [Geist](https://vercel.com/geist/destructive-action-modal), [gov.br](https://www.gov.br/ds/components/modal), [Ontario](https://designsystem.ontario.ca/components/detail/buttons.html).

**Ofereça reversão quando desfazer não for possível.** Algumas ações sem desfazer ainda têm um caminho de reversão, como cancelar um compartilhamento já enviado ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)). Diga como.

### Conteúdo

Escolha o rótulo pelo efeito sobre o trabalho da pessoa ([Fluent](https://fluent2.microsoft.design/components/web/react/core/button/usage), [Geist](https://vercel.com/geist/toast)):

| Rótulo     | Efeito                                                                   | Onde usar                                                        |
|------------|--------------------------------------------------------------------------|------------------------------------------------------------------|
| Desfazer   | Reverte a última ação já concluída                                       | Toast ou mensagem após a ação, barra de ferramentas, menu Editar |
| Refazer    | Reaplica a ação desfeita                                                 | Barra de ferramentas, menu Editar                                |
| Cancelar   | Interrompe uma tarefa em andamento e volta ao estado anterior sem salvar | Diálogos, drawers, modo de edição, assistentes                   |
| Não salvar | Sai e descarta as alterações                                             | Só no alerta de alterações não salvas                            |
| Fechar     | Fecha a superfície sem afetar o estado da tarefa                         | Mensagens informativas, diálogos sem ação, painéis               |

Não combine um botão X com um botão Fechar na mesma superfície ([Fluent](https://fluent2.microsoft.design/components/web/react/core/button/usage)). Use o mesmo verbo na ação e na confirmação: o botão "Arquivar" gera a mensagem "Projeto arquivado" ([Geist](https://vercel.com/geist/toast)). Não escreva "com sucesso" nem use exclamação.

**Faça** conclua a ação, diga o que mudou e ofereça Desfazer.

**Não faça** peça confirmação para uma ação comum e reversível, com título vago e "Sim" e "Não".

### Acessibilidade

Anuncie o resultado de cada desfazer e refazer em uma região `aria-live="polite"`, por exemplo "Negrito desfeito". Declare atalhos com `aria-keyshortcuts` e mostre-os na dica do botão. Quando não houver nada a refazer, mantenha o botão focável com `aria-disabled="true"` e uma dica focável que explique o motivo. O toast com Desfazer usa `role="status"`, é alcançável pelo teclado e não some enquanto a pessoa não fechar. No alerta destrutivo e no de alterações não salvas, o foco inicial vai para Cancelar.

### Considerações por plataforma

#### Web desktop

Suporte os atalhos padrão. No Windows, Ctrl+Z desfaz e Ctrl+Shift+Z ou Ctrl+Y refazem. No macOS, Cmd+Z desfaz e Shift+Cmd+Z refaz ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)). Se o produto tiver um menu Editar, coloque Desfazer e Refazer no topo dele ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)). Dentro de campos de texto, deixe o navegador cuidar do desfazer da digitação.

#### Web móvel

Sem teclado físico, o toast com Desfazer e os botões na barra de ferramentas são o principal caminho. Não redefina gestos padrão do sistema para desfazer ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)). Posicione o toast acima da barra de navegação inferior e garanta área de toque de `--c-touch` em Desfazer e Fechar. No alerta de alterações não salvas, empilhe os botões com Salvar em cima.

#### Tablets e dobráveis

Com teclado conectado, suporte os mesmos atalhos do desktop. No iPad, as pessoas também desfazem com o gesto de deslizar com três dedos, que é do sistema ([HIG](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)); não capture esse gesto para outras funções.

### Recursos

#### Relacionados

- Toasts
- Modalidade
- Feedback
- Gerenciamento de arquivos
- Barra de ferramentas
- Teclado

#### Referências

- [Modal (janela de exibição)](https://www.gov.br/ds/components/modal) gov.br DS
- [Upload (envio de arquivos)](https://www.gov.br/ds/components/upload) gov.br DS
- [Wizard (assistente)](https://www.gov.br/ds/components/wizard) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo) Apple HIG
- [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) Apple HIG
- [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop) Apple HIG
- [Button](https://fluent2.microsoft.design/components/web/react/core/button/usage) Fluent 2
- [Toast](https://vercel.com/geist/toast) Geist
- [Destructive Action Modal](https://vercel.com/geist/destructive-action-modal) Geist
- [Button](https://design-system.service.gov.uk/components/button/) GOV.UK Design System
- [Buttons](https://designsystem.ontario.ca/components/detail/buttons.html) Ontario Design System

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. O toast com Desfazer passa a ficar até a pessoa fechar, a confirmação por digitação mantém o botão habilitado e a página acrescenta cancelamento de edição, alerta de alterações não salvas e substituição de arquivo com Desfazer. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                       |

## Formulários em etapas e páginas de pergunta

Divida transações longas em páginas curtas, com uma pergunta clara por vez, e mostre o caminho apenas quando isso ajuda a pessoa a avançar.

Dividir um formulário longo em etapas mostra menos informação por vez, reduz o esforço cognitivo, facilita adaptar o layout a telas pequenas e diminui os erros. Em troca, aumenta o número de cliques, então nem todo formulário deve ser dividido ([HDS](https://hds.hel.fi/patterns/forms/form-multi-page)).

O Trama tem duas formas de etapas. As **páginas de pergunta** servem a transações públicas, como pedir um benefício: uma pergunta por página, link Voltar no topo e, se preciso, o texto "Etapa 2 de 4". O **assistente** serve a tarefas complexas dentro do produto, em ordem obrigatória, em que etapas seguintes dependem das anteriores: ele tem painel de etapas, área de conteúdo e barra de navegação ([gov.br](https://www.gov.br/ds/components/wizard)). A revisão final e a confirmação estão em Revisar respostas e confirmação.

### Quando dividir em etapas

Divida quando o formulário tiver temas distintos, for longo a ponto de exigir rolagem em uma tela de desktop ou quando as pessoas erram muito. Mantenha em uma página quando houver poucos campos, quando a pessoa precisar comparar partes ou quando uma etapa puder invalidar outra ([HDS](https://hds.hel.fi/patterns/forms/form-multi-page)). Use o assistente só para navegação linear; se a pessoa puder visitar as partes em qualquer ordem, use abas ou uma lista de tarefas ([gov.br](https://www.gov.br/ds/components/wizard)).

### Boas práticas

#### Início e elegibilidade

**Comece com uma página de início.** Diga o que o serviço faz, para quem é, quanto custa e quanto tempo leva, liste os documentos necessários e indique outras formas de acesso. Use um botão com verbo, como "Começar agora" ([GOV.UK](https://design-system.service.gov.uk/patterns/start-using-a-service/)). Titule o formulário com o que a pessoa quer fazer, como "Inscreva seu filho na creche" ([DKFDS](https://designsystem.dk/eksempler/patterns/formular/), [gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Verifique a elegibilidade cedo, com perguntas simples,** e mostre o resultado: se a pessoa pode usar o serviço e, se não puder, por quê e o que fazer. Não repita depois as perguntas já feitas ([GOV.UK](https://design-system.service.gov.uk/patterns/check-a-service-is-suitable/)).

#### Páginas de pergunta

**Pergunte só o que for necessário e diga por quê.** Todo dado coletado tem uma finalidade clara e informada, principalmente dados pessoais ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Ofereça "Não sei" quando for uma resposta válida ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)).

**Comece com uma pergunta por página.** Isso ajuda a pessoa a focar, funciona bem no celular e ajuda pessoas idosas e com pouca experiência digital ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/), [DKFDS](https://designsystem.dk/eksempler/patterns/formular/)). Mantenha juntos os campos complementares, como data de início e de término, estado e cidade ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Use a pergunta como título da página.** Coloque o `<label>` ou a `<legend>` dentro do `<h1>`, com título único por página, e indique a seção em uma legenda acima ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)).

**Escreva dicas curtas e diga o formato esperado.** Uma frase, sem links ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)). Explique exatamente o formato quando houver um, como em telefone ou CEP ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Aceite qualquer formato digitado, com espaços, pontos, hífens ou barras, e normalize no sistema. Você pode formatar o valor ao sair do campo; nunca bloqueie a digitação nem impeça apagar. Não divida um mesmo dado em vários campos ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

> **Divergência entre referências** O gov.br recomenda máscara dinâmica durante a digitação e ao colar. O GOV.UK pede aceitar formatos diferentes, com espaços e hífens, sem máscara. O Trama aplica a decisão D3: aceita qualquer formato e normaliza; formatar ao sair do campo é permitido, máscara que bloqueia digitar ou apagar é proibida. Fontes: [gov.br](https://www.gov.br/ds/padroes/design/formulario), [GOV.UK](https://design-system.service.gov.uk/patterns/payment-card-details/).

**Marque os campos opcionais com "(opcional)".** Prefira formulários com todos os campos obrigatórios e nunca sinalize obrigatórios e opcionais ao mesmo tempo ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Não use asterisco em páginas de pergunta ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)).

**Não peça a mesma informação duas vezes** e preencha com respostas anteriores ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)). Repita instruções importantes em cada etapa ([HDS](https://hds.hel.fi/patterns/forms/form-multi-page)).

**Espace por função.** Use `--f-gap-field` entre campos, `--f-gap-title` entre o título e o primeiro campo, `--f-gap-group` entre grupos e `--f-gap-actions` antes dos botões, sempre os mesmos em todo o produto ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Agrupe com `<fieldset>` e `<legend>`, com no máximo um nível de subagrupamento ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Evite controles deslizantes** ou ofereça outra forma de responder sem arrastar ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/), WCAG 2.2, 2.5.7). Não ofereça botões "Limpar formulário" ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

#### Navegação entre etapas

**Inclua o link Voltar e preserve o botão voltar do navegador.** O botão do navegador volta à página anterior no estado em que a pessoa a deixou; ações que só acontecem uma vez, como um pagamento, mostram uma mensagem sem repetir a ação ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/), [Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html)). Na primeira etapa não há Voltar ([gov.br](https://www.gov.br/ds/components/wizard)).

**Rotule o botão de avanço "Continuar" e, na última etapa, "Concluir".** Coloque a ação principal primeiro, alinhada ao início do conteúdo, onde a pessoa não deixa de vê-la ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/), [Ontario](https://designsystem.ontario.ca/components/detail/buttons.html)). Se a última etapa envia algo, nomeie o envio, como "Enviar solicitação". Ofereça "Salvar rascunho" como ação secundária quando houver como continuar depois ([HDS](https://hds.hel.fi/patterns/forms/form-multi-page)).

**Não ponha Cancelar em páginas de pergunta** ([Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html)). No assistente, Cancelar é uma ação terciária, depois das outras, que volta à tela anterior ao fluxo e avisa que os dados preenchidos serão perdidos ([gov.br](https://www.gov.br/ds/components/wizard)).

> **Divergência entre referências** No gov.br, o botão primário fica à direita dos secundários, e o assistente usa o rótulo "Avançar". GOV.UK e Ontario alinham a ação principal à esquerda; o Ontario mostra que, com zoom de 400%, um botão à direita sai da área visível. O Trama aplica as decisões D4 (principal primeiro, no início) e D7 ("Continuar" em fluxos de tarefa, "Concluir" na última etapa). Fontes: [gov.br](https://www.gov.br/ds/padroes/design/formulario), [gov.br](https://www.gov.br/ds/components/wizard), [GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/), [Ontario](https://designsystem.ontario.ca/components/detail/buttons.html).

**Valide cada etapa ao sair dela.** Mantenha Continuar sempre habilitado; ao acionar, mostre o resumo de erros e as mensagens nos campos ([HDS](https://hds.hel.fi/patterns/forms/form-multi-page), [DKFDS](https://designsystem.dk/komponenter/trinindikator/)).

**Ao mudar de etapa, mova o foco para o título H1 da etapa** ([HDS](https://hds.hel.fi/patterns/forms/form-multi-page)). Avise por texto, e não só por cor, quando uma etapa foi concluída ou tem erro ([gov.br](https://www.gov.br/ds/components/wizard)).

> **Divergência entre referências** O gov.br põe o foco no primeiro campo obrigatório do formulário. O HDS o põe no título da etapa. O Trama aplica a decisão D13: foco no H1, para que leitores de tela anunciem a pergunta e a etapa antes do campo. Fontes: [gov.br](https://www.gov.br/ds/padroes/design/formulario), [HDS](https://hds.hel.fi/patterns/forms/form-multi-page).

#### Indicador de etapa

**Em páginas de pergunta, teste primeiro sem indicador.** Melhore a ordem, o tipo ou a quantidade de perguntas antes. Se ainda for necessário, use "Etapa 2 de 4" acima do título, e só mostre o total se ele for confiável ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/), [DKFDS](https://designsystem.dk/komponenter/trinindikator/)). Indicadores horizontais com todas as etapas rotuladas passam despercebidos, ocupam espaço e não se adaptam a telas pequenas; serviços do GOV.UK os removeram sem efeito negativo, inclusive um de 12 etapas sem mudança na taxa nem no tempo de conclusão ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/), [Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html)).

**No assistente, use o painel de etapas.** O Trama reserva esse painel a tarefas dentro do produto, como faz o assistente do gov.br, e segue a evidência do GOV.UK nas transações públicas. Use o componente Indicador de etapas com número em cada etapa e rótulos de uma palavra, no máximo três ([gov.br](https://www.gov.br/ds/components/step)). Etapas concluídas usam `data-state="done"`, a atual `aria-current="step"`, e etapas com pendência ou erro `data-state="warning"` ou `"error"`, com a explicação em texto ([gov.br](https://www.gov.br/ds/components/step)). Na progressão linear, etapas ainda não liberadas aparecem sem link e com a explicação "Disponível depois da etapa anterior".

**Não aninhe indicadores e não os mostre em páginas sem entrada de dados,** como introdução e confirmação; não conte percentuais ou tempo ([Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html), [DKFDS](https://designsystem.dk/komponenter/trinindikator/)).

#### Transações longas: lista de tarefas

**Use uma lista de tarefas quando a transação tem muitas partes e pode levar várias sessões.** Mostre-a no início e a cada retorno, com tarefas nomeadas por verbo, como "Informe sua renda" ([GOV.UK](https://design-system.service.gov.uk/patterns/complete-multiple-tasks/), [Ontario](https://designsystem.ontario.ca/components/detail/task-list.html)).

| Status                 | Uso                                                   | Aparência no Trama  |
|------------------------|-------------------------------------------------------|---------------------|
| Não iniciada           | Pronta para começar                                   | Não iniciada        |
| Em andamento           | Começada e não concluída                              | Em andamento        |
| Concluída              | Terminada; texto sem fundo, para destacar o que falta | Texto em `--t-fg-1` |
| Não pode começar ainda | Depende de outra tarefa; linha sem link               | Texto em `--t-fg-3` |
| Há um problema         | Salva com erro; único status com cor de erro          | Há um problema      |

Fontes dos status: [GOV.UK](https://design-system.service.gov.uk/patterns/complete-multiple-tasks/) e [Ontario](https://designsystem.ontario.ca/components/detail/task-list.html). Permita concluir tarefas em qualquer ordem quando possível e salve as respostas automaticamente ([Ontario](https://designsystem.ontario.ca/components/detail/task-list.html)).

**Faça** indique a posição em texto simples e o formato aceito na dica.

**Não faça** mostre uma fileira de etapas rotuladas em um formulário público longo.

### Considerações por plataforma

#### Web desktop

Limite o formulário a cerca de dois terços da largura do conteúdo, em uma coluna, exceto campos complementares ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). No assistente, o painel de etapas ocupa a largura do conteúdo, com espaços iguais entre etapas, na orientação horizontal ou vertical ([gov.br](https://www.gov.br/ds/components/wizard)). Garanta que Enter envie a etapa pelo botão Continuar.

#### Web móvel

Uma pergunta por página funciona especialmente bem em telas pequenas ([DKFDS](https://designsystem.dk/eksempler/patterns/formular/)). Use o teclado adequado a cada campo e mantenha Continuar logo após o último campo, em largura total, com Voltar e Cancelar empilhados abaixo. No assistente, use a orientação vertical (`.tr-steps--vertical`) ou mostre só "Etapa 2 de 4" com o nome da etapa atual e abra a lista ao tocar ([gov.br](https://www.gov.br/ds/components/step), [DKFDS](https://designsystem.dk/komponenter/trinindikator/)). Na orientação horizontal, mostre no máximo 4 etapas visíveis ([gov.br](https://www.gov.br/ds/components/step)). Prefira a rolagem da página a uma área de conteúdo com rolagem interna.

> **Divergência entre referências** No celular, o gov.br troca Voltar e Avançar por botões circulares só com ícone, fixa a barra de navegação na base da tela e esconde os rótulos das etapas. O Trama mantém botões com texto, no fluxo da página, e o nome da etapa atual visível: rótulos escritos são mais claros que ícones, e uma barra fixa cobre conteúdo quando o zoom aumenta. Fontes: [gov.br](https://www.gov.br/ds/components/wizard).

#### Tablets e dobráveis

Não estique campos à largura da tela ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Na classe Expandida, a lista de tarefas ou o painel de etapas vertical pode ficar ao lado da etapa atual. Ao abrir ou fechar o dobrável, preserve respostas, foco e teclado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Revisar respostas e confirmação
- Entrada de dados
- Validação e mensagens de erro
- Indicador de etapas
- Resumo de erros
- Abas

#### Referências

- [Wizard (assistente)](https://www.gov.br/ds/components/wizard) gov.br DS
- [Steps (navegação passo a passo)](https://www.gov.br/ds/components/step) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Question pages](https://design-system.service.gov.uk/patterns/question-pages/) GOV.UK Design System
- [Payment card details](https://design-system.service.gov.uk/patterns/payment-card-details/) GOV.UK Design System
- [Complete multiple tasks](https://design-system.service.gov.uk/patterns/complete-multiple-tasks/) GOV.UK Design System
- [Start using a service](https://design-system.service.gov.uk/patterns/start-using-a-service/) GOV.UK Design System
- [Check a service is suitable](https://design-system.service.gov.uk/patterns/check-a-service-is-suitable/) GOV.UK Design System
- [Trinindikator](https://designsystem.dk/komponenter/trinindikator/) DKFDS
- [Formular](https://designsystem.dk/eksempler/patterns/formular/) DKFDS
- [Step indicator](https://designsystem.ontario.ca/components/detail/step-indicator.html) Ontario Design System
- [Buttons](https://designsystem.ontario.ca/components/detail/buttons.html) Ontario Design System
- [Task list](https://designsystem.ontario.ca/components/detail/task-list.html) Ontario Design System
- [Multi-page forms](https://hds.hel.fi/patterns/forms/form-multi-page) Helsinki Design System
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o assistente com painel de etapas e estados, Voltar ausente na primeira etapa e Concluir na última, formatos sem máscara bloqueante, espaços de formulário por função e foco no H1 da etapa. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                           |

## Revisar respostas e confirmação

Antes do envio, mostre todas as respostas com um caminho direto para corrigir cada uma; depois do envio, confirme o que aconteceu e o que vem a seguir.

A página de revisão aumenta a confiança da pessoa, porque ela vê que completou todas as seções e que os dados foram registrados, e reduz erros, porque oferece uma segunda chance de corrigir algo antes do envio ([GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/), [Ontario](https://designsystem.ontario.ca/components/detail/form-review.html)). No assistente, o resumo das escolhas feitas aparece na etapa final, antes do botão Concluir ([gov.br](https://www.gov.br/ds/components/wizard)).

A página de confirmação encerra a transação. Ela tranquiliza a pessoa de que terminou e explica o que esperar depois ([GOV.UK](https://design-system.service.gov.uk/patterns/confirmation-pages/)). As duas páginas fecham o fluxo descrito em Formulários em etapas e páginas de pergunta.

### Boas práticas

#### Página de revisão

**Mostre a revisão imediatamente antes do envio.** Em transações pequenas e médias, use uma única página de revisão. Em transações grandes, considere uma revisão ao fim de cada seção e uma final, principalmente quando pessoas diferentes preenchem seções diferentes ([GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/), [Ontario](https://designsystem.ontario.ca/components/detail/form-review.html)). Considere a revisão sempre que o envio tiver impacto significativo ou o formulário tiver muitas etapas ([Ontario](https://designsystem.ontario.ca/components/detail/form-review.html), [gov.br](https://www.gov.br/ds/components/wizard)).

**Use o título para dizer o que a pessoa precisa fazer** e deixe claro que a transação só termina depois que ela confirma ([GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/), [Ontario](https://designsystem.ontario.ca/components/detail/form-review.html)).

**Organize em seções e mostre só o que se aplica.** Divida as respostas em seções com títulos na hierarquia correta e não mostre seções que a pessoa não precisou responder ([GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/), [Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)).

**Reescreva as perguntas quando necessário.** Use um único rótulo "Endereço" para todas as linhas do endereço e transforme perguntas longas em afirmações curtas ([GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/), [Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)).

**Mostre respostas opcionais vazias.** Escreva "Não informado" para que a pessoa saiba que pulou a pergunta ([GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/)). Quando faltar uma informação obrigatória, coloque no lugar do valor um link para a pergunta, como "Informe o telefone" ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)).

**Proteja dados sensíveis e diga que estão protegidos.** Mostre dados pessoais sensíveis parcialmente ocultos e informe, em texto junto ao campo, que o dado foi anonimizado ou ocultado ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). A forma de ocultar segue a Privacidade do produto.

**Não trunque respostas.** Valores da revisão quebram linha. A exceção são nomes de arquivo longos, que podem ser truncados com o nome completo disponível em dica e no nome acessível. Veja Excesso de conteúdo.

**Não use acordeões na revisão.** Todas as respostas ficam visíveis ([Ontario](https://designsystem.ontario.ca/components/detail/form-review.html)).

**Mostre erros de etapas anteriores no topo,** em um resumo de erros com links para as etapas onde corrigir ([DKFDS](https://designsystem.dk/komponenter/trinindikator/), [HDS](https://hds.hel.fi/patterns/forms/form-multi-page)).

**Use cartões de resumo para vários itens do mesmo tipo,** como várias pessoas ou documentos, cada um com título único e poucas ações no cabeçalho. Se uma ação do cartão for difícil de desfazer, avise ou peça confirmação ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)).

#### Nomear o envio

**Nomeie a ação no botão.** Quando a última etapa envia algo, use o verbo e o objeto, como "Enviar solicitação" ([GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/)), com até duas palavras. Quando a última etapa de um assistente só encerra o fluxo, sem envio a terceiros, use "Concluir" ([gov.br](https://www.gov.br/ds/components/wizard)).

> **Divergência entre referências** O gov.br troca o rótulo do avanço por "Concluir" em toda última etapa. O GOV.UK pede um rótulo que diga o que acontece ao enviar. O Trama usa "Concluir" como regra de vocabulário (decisão D7) e, quando a etapa final envia dados, prefere o rótulo que nomeia o envio, porque "Concluir" sozinho não diz que algo será enviado. Fontes: [gov.br](https://www.gov.br/ds/components/wizard), [GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/).

#### Alterar uma resposta

**Ofereça um link Alterar por linha ou por seção.** Se várias linhas levam ao mesmo lugar, use um único link no título da seção ([Ontario](https://designsystem.ontario.ca/components/detail/form-review.html)). Se nem todas as respostas podem ser alteradas, o link indica quais podem; se todas podem, a presença do link em cada linha basta ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Linhas que não podem ser alteradas ficam sem link.

**Leve direto ao dado que será alterado.** O link abre a página ou a etapa onde o dado foi informado, com o campo em foco, e não o início do fluxo. Em assistentes com mais de seis etapas, esses links diretos são indispensáveis ([gov.br](https://www.gov.br/ds/components/wizard)).

> **Divergência entre referências** O gov.br recomenda links diretos para editar quando o assistente tem mais de seis etapas; com menos, a pessoa volta pelas etapas. GOV.UK e Ontario oferecem o link Alterar em toda revisão. Pela convergência e porque voltar etapa por etapa exige mais navegação pelo teclado, o Trama oferece links diretos em qualquer revisão. Fontes: [gov.br](https://www.gov.br/ds/components/wizard), [GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/), [Ontario](https://designsystem.ontario.ca/components/detail/form-review.html).

**Leve de volta à revisão depois da alteração.** A página de alteração abre com as respostas preenchidas, com o botão "Salvar alterações" primeiro e o link "Voltar à revisão" depois. Ao salvar, a pessoa volta à revisão com a lista atualizada, sem repetir o restante do formulário. Se a nova resposta exigir perguntas extras, faça-as antes de voltar ([Ontario](https://designsystem.ontario.ca/components/detail/form-review.html), [GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/)). O modo de edição sempre oferece salvar e cancelar ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

#### Página de confirmação

**Inclua o que a pessoa precisa depois de enviar** ([GOV.UK](https://design-system.service.gov.uk/patterns/confirmation-pages/)):

- o número de referência, se houver;
- o que acontece a seguir e quando;
- os contatos do serviço;
- links para o que a pessoa provavelmente vai precisar em seguida;
- um link para dar opinião sobre o serviço;
- uma forma de guardar o registro, como baixar o comprovante em PDF.

**Ofereça o comprovante e os próximos caminhos.** Os exemplos de recibo do DKFDS trazem o número de referência, o comprovante em PDF, uma seção "O que acontece agora", os contatos e ações para começar outra solicitação ou ir à página inicial ([DKFDS](https://designsystem.dk/pages/eksempler/kvittering/kvittering-2/)).

**Destaque o resultado em um painel curto.** O painel traz o resultado como título, dizendo o que mudou, como "Solicitação enviada", sem "com sucesso" e sem exclamação. Textos curtos quebram menos linhas com zoom ([GOV.UK](https://design-system.service.gov.uk/components/panel/)). Não coloque links nem botões dentro do painel ([GOV.UK](https://design-system.service.gov.uk/patterns/confirmation-pages/)).

**Permita voltar à confirmação**, que algumas pessoas salvam como recibo, e **impeça o envio duplicado** se a pessoa usar o botão voltar do navegador ([GOV.UK](https://design-system.service.gov.uk/patterns/confirmation-pages/), [GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)).

**Faça** agrupe linhas relacionadas sob um rótulo curto, com link de alteração descritivo.

**Não faça** copie a pergunta longa nem use "Alterar" sem dizer o quê.

### Acessibilidade

Use a lista de resumo (`<dl>`) só para pares de chave e valor; dados tabulares vão em tabela ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)). Os links Alterar contêm texto visualmente oculto com o nome da resposta, para que o leitor de tela anuncie "Alterar endereço" ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/), [Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)). Mantenha as bordas entre linhas: elas ligam cada ação à informação certa e ajudam quem usa ampliação de tela ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)). Ao carregar a revisão ou a confirmação, mova o foco para o título principal da página. Informe a conclusão também em texto, e não só pela cor do painel ([gov.br](https://www.gov.br/ds/components/wizard)). Elementos interativos sobre fundo colorido precisam de contraste de pelo menos 3:1 no indicador de foco (WCAG 2.2, 1.4.11).

### Considerações por plataforma

#### Web desktop

Use cerca de dois terços da largura para respostas curtas: linhas menores são mais fáceis de ler e os links Alterar ficam perto do conteúdo, o que ajuda quem usa ampliação de tela. Para respostas longas, use a largura total ([GOV.UK](https://design-system.service.gov.uk/patterns/check-answers/), [Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)).

#### Web móvel

Na classe Compacta, empilhe chave, valor e ação em cada linha, com a ação alinhada à borda inicial e área de toque de `--c-touch`. O botão de envio ocupa a largura total (`.tr-btn--block-compact`). Mantenha o painel de confirmação com texto curto, para que não quebre em muitas linhas com zoom ([GOV.UK](https://design-system.service.gov.uk/components/panel/)).

#### Tablets e dobráveis

Mantenha a revisão em uma coluna de largura legível ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Na classe Expandida, a página de alteração pode abrir em um painel ao lado da revisão, para que a pessoa veja a lista atualizar ao salvar.

### Recursos

#### Relacionados

- Formulários em etapas e páginas de pergunta
- Lista de resumo
- Resumo de erros
- Mensagens e banners
- Privacidade
- Excesso de conteúdo

#### Referências

- [Wizard (assistente)](https://www.gov.br/ds/components/wizard) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Check answers](https://design-system.service.gov.uk/patterns/check-answers/) GOV.UK Design System
- [Confirmation pages](https://design-system.service.gov.uk/patterns/confirmation-pages/) GOV.UK Design System
- [Summary list](https://design-system.service.gov.uk/components/summary-list/) GOV.UK Design System
- [Panel](https://design-system.service.gov.uk/components/panel/) GOV.UK Design System
- [Question pages](https://design-system.service.gov.uk/patterns/question-pages/) GOV.UK Design System
- [Form review](https://designsystem.ontario.ca/components/detail/form-review.html) Ontario Design System
- [Summary list](https://designsystem.ontario.ca/components/detail/summary-list.html) Ontario Design System
- [Trinindikator](https://designsystem.dk/komponenter/trinindikator/) DKFDS
- [Eksempel: Kvittering](https://designsystem.dk/pages/eksempler/kvittering/kvittering-2/) DKFDS
- [Multi-page forms](https://hds.hel.fi/patterns/forms/form-multi-page) Helsinki Design System
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o resumo antes de Concluir no assistente, links diretos para editar em qualquer revisão, dados sensíveis ocultos com explicação, regra para nomear o envio e confirmação que diz o que mudou. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                            |

