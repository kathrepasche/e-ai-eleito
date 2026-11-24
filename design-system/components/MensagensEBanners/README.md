# MensagensEBanners

Uma mensagem destaca, dentro da própria página, uma informação de estado que a pessoa precisa ver e que continua ali até deixar de ser verdade.

Mensagens fazem parte do conteúdo. Diferentes de toasts, não somem com o tempo; diferentes de diálogos, não bloqueiam a tarefa. Elas dão retorno sobre o que acontece no sistema, em resposta a uma ação da pessoa ou a um evento programado: uma manutenção, um prazo que se aproxima, um limite de uso atingido, o resultado de uma ação feita na página anterior ([gov.br DS](https://www.gov.br/ds/components/message), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage), [GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)).

**Use uma mensagem** para informação importante e atual: estado do serviço, mudanças automáticas nos dados da pessoa, avisos que podem levar a problemas e confirmações quando a jornada ainda continua ([DKFDS](https://designsystem.dk/komponenter/beskeder/)).

**Não use uma mensagem** para erros de validação de formulário: use as mensagens contextuais junto aos campos e o resumo de erros, e nunca mostre um banner e um resumo de erros na mesma página ([GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)). Não use mensagens para enfeitar conteúdo neutro e estático; use texto comum ([DKFDS](https://designsystem.dk/komponenter/beskeder/), [Ontario](https://designsystem.ontario.ca/components/detail/page-alerts.html)). Para confirmar uma ação destrutiva, use um diálogo. Para status de um item numa lista, use um badge.

## Anatomia

1.  **Superfície**: cor suave da intenção, que define o tipo da mensagem.
2.  **Ícone** (obrigatório no Trama): à esquerda, reforça a intenção com forma própria: círculo com "i" para informação, círculo com marca de verificação para sucesso, triângulo com exclamação para aviso e círculo com X para erro ([gov.br DS](https://www.gov.br/ds/components/message)). Cor e ícone nunca são o único sinal.
3.  **Título**: resume a situação em uma linha, acima do corpo ou no início dele. Pode ser omitido em mensagens de uma frase só.
4.  **Corpo** (obrigatório): uma ou duas frases.
5.  **Dados complementares** (opcional, em erros do sistema): código, data e hora ou protocolo, num formato diferente do texto principal ([gov.br DS](https://www.gov.br/ds/components/message)). O Trama usa `.tr-mono` em `--t-fg-2`.
6.  **Ações** (opcionais em informação e sucesso, obrigatórias em aviso e erro): um botão, um link ou os dois ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)).
7.  **Fechar** (opcional): no topo à direita, apenas em informação e sucesso e nunca na mensagem contextual ([gov.br DS](https://www.gov.br/ds/components/message)).

## Tipos

### Por intenção

| Intenção   | Quando usar                                                                                                                                                                                                                                                        |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Informação | Estado padrão, para informação neutra. Algo mudou e pode afetar o que a pessoa faz, como campos preenchidos automaticamente que ela deve conferir ([gov.br DS](https://www.gov.br/ds/components/message), [DKFDS](https://designsystem.dk/komponenter/beskeder/)). |
| Sucesso    | Uma tarefa ou etapa foi concluída e a pessoa ainda não terminou a jornada ([gov.br DS](https://www.gov.br/ds/components/message), [GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)).                                                 |
| Aviso      | Uma situação que pode levar a erros, como uma manutenção planejada ou prazos de análise maiores ([DKFDS](https://designsystem.dk/komponenter/beskeder/)). Não bloqueia o avanço.                                                                                   |
| Erro       | Um problema do sistema ou da operação impede continuar ([gov.br DS](https://www.gov.br/ds/components/message), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)).                                                           |

### Por alcance e posição

- **Banner crítico**: acima do cabeçalho, para uma situação que afeta todo o serviço, como uma interrupção. Fica no ar só enquanto a situação durar, com até 140 caracteres e um único link ([Ontario](https://designsystem.ontario.ca/components/detail/critical-alerts.html)).
- **Mensagem global**: resposta que vale para a página ou o sistema inteiro. Fica entre o cabeçalho e o breadcrumb. A superfície ocupa a largura toda da janela, sem raio, e o conteúdo respeita as margens da grade ([gov.br DS](https://www.gov.br/ds/components/message)).
- **Mensagem direcionada**: resposta a uma função específica. Fica dentro do card, aba, formulário ou drawer afetado, logo abaixo do título dele e o mais perto possível do conteúdo ([gov.br DS](https://www.gov.br/ds/components/message), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage), [HDS](https://hds.hel.fi/components/notification)).
- **Mensagem contextual**: retorno sobre um componente, como a mensagem de validação de um campo. Usa `.tr-error-msg` ou `.tr-field-msg--success`, `--warning` e `--info`, sem botão Fechar, com largura limitada à do componente ([gov.br DS](https://www.gov.br/ds/components/message)). Detalhes em Validação e mensagens de erro.

> **Nota** Para destacar uma citação ou um exemplo sem carga de estado, use texto recuado com borda à esquerda, como o inset text do [GOV.UK](https://design-system.service.gov.uk/components/inset-text/). Para consequências legais de uma ação, use texto de aviso em negrito com ícone ([GOV.UK](https://design-system.service.gov.uk/components/warning-text/)).

## Boas práticas

**Use com parcimônia.** Há evidência de que as pessoas não percebem banners, e o excesso agrava o problema ([GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)). Interrupções frequentes prejudicam principalmente pessoas com deficiência cognitiva e visual ([gov.br DS](https://www.gov.br/ds/components/message)). Informação que pode ficar em contexto, como um indicador discreto de conexão, dispensa mensagem ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)).

**Mostre uma mensagem global ou direcionada por área.** Combine mensagens relacionadas numa só. Se forem diferentes demais, mostre a mais prioritária ([GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)). Quando vários elementos precisam de atenção, use mensagens contextuais em cada um, em vez de várias mensagens empilhadas no topo ([gov.br DS](https://www.gov.br/ds/components/message)). Se várias precisarem coexistir, ordene por gravidade: erro, aviso, sucesso, informação ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)).

**Ofereça a saída em avisos e erros.** Uma mensagem sem caminho é um beco sem saída. A ação resolve o estado: "Atualizar cartão", "Liberar espaço" ([Geist](https://vercel.com/geist/project-banner)).

**Mantenha avisos e erros até o problema ser resolvido.** Se a mensagem pode ser fechada sem resolver nada, ela não merece ser um aviso ([Geist](https://vercel.com/geist/project-banner)). Conteúdo importante fica sempre visível, sem Fechar ([gov.br DS](https://www.gov.br/ds/components/message)). Mensagens de sucesso somem quando a pessoa vai para outra página ([GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)). Nenhuma mensagem some por tempo.

**Faça** diga o impacto e ofereça a ação que resolve.

**Não faça** use cor de erro e título vago para destacar conteúdo promocional.

### Estados e comportamento

- **Exibida em resposta a uma ação**: o foco vai para o contêiner da mensagem (`tabindex="-1"`, com o foco tênue `.tr-focus-subtle`), para que o leitor de tela leia tudo de uma vez; o botão Fechar, quando houver, é o próximo na ordem de tabulação.
- **Fechada pela pessoa**: some com `--m-normal`, e o foco volta ao ponto do fluxo de navegação em que a pessoa estava antes de ir à mensagem ([gov.br DS](https://www.gov.br/ds/components/message)).
- **Resolvida pelo sistema**: quando a condição deixa de existir, a mensagem sai sozinha ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)).
- **Texto longo**: a superfície cresce em altura e o texto quebra, nunca trunca; o botão Fechar fica no topo ([gov.br DS](https://www.gov.br/ds/components/message)). Acima de duas linhas, as ações descem para baixo do corpo ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)).
- **Densidade**: mensagens não usam a densidade alta, mesmo em ferramentas densas.

> **Divergência entre referências** Posição: o GOV.UK põe o banner logo antes do `h1`, com a largura do conteúdo; o gov.br DS põe a mensagem global entre o cabeçalho e o breadcrumb, sangrando a grade. Nenhuma das duas tem evidência ou vantagem de acessibilidade sobre a outra; pelo critério de contexto brasileiro, o Trama segue o gov.br, que é a convenção que o público dos serviços públicos brasileiros encontra. Foco: o gov.br move o foco para o botão Fechar quando a mensagem aparece; o GOV.UK faz o banner de sucesso receber o foco ao carregar a página. Pelo critério de acessibilidade, o Trama move o foco para o contêiner, que faz o leitor de tela anunciar a mensagem inteira, e não só o nome do botão. Fechamento: a versão 1.0 levava o foco ao próximo elemento lógico; sem referência que apoiasse essa regra, o Trama passa a seguir o gov.br e devolve o foco ao ponto de origem.

## Conteúdo

**Ponha o essencial no título.** Uma palavra ou frase curta que sintetize a mensagem: "Armazenamento quase cheio" ([gov.br DS](https://www.gov.br/ds/components/message), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). Corte aberturas como "Atenção" ou "Importante"; a intenção já carrega esse sinal ([Geist](https://vercel.com/geist/note)).

**Escreva o corpo em uma ou duas frases, na voz ativa, com o impacto.** Texto curto, claro e objetivo, sem jargão; evite mensagens que quebram em muitas linhas ([gov.br DS](https://www.gov.br/ds/components/message)). Não repita o título. Fique abaixo de 280 caracteres no total ([Ontario](https://designsystem.ontario.ca/components/detail/page-alerts.html)).

**Em erros, diga o que aconteceu e como resolver.** Tom neutro, sem "Ops" e sem culpar a pessoa. Separe os dados técnicos, como código e horário, do texto que explica ([gov.br DS](https://www.gov.br/ds/components/message)).

**Em sucesso, diga o que mudou.** Evite "com sucesso" e parabéns por tarefas rotineiras ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). Se o título for apenas um rótulo de tipo, use sempre a mesma palavra no serviço inteiro (WCAG 2.2, 3.2.4, como orienta o [GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)).

**Escreva links com verbo e destino.** "Ver o calendário de manutenção", nunca "Clique aqui".

## Acessibilidade

- Mensagens presentes no carregamento usam `role="region"` com `aria-labelledby` apontando para o título, para que leitores de tela as encontrem ([GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)).
- Mensagens que aparecem ou mudam depois do carregamento são lidas imediatamente: `role="alert"` em aviso e erro, `role="status"` nos demais casos ([gov.br DS](https://www.gov.br/ds/components/message), [DKFDS](https://designsystem.dk/komponenter/beskeder/), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)).
- O produto pode tocar um som curto e característico ao exibir uma mensagem, para que quem usa tecnologia assistiva perceba o retorno antes da leitura ([gov.br DS](https://www.gov.br/ds/components/message)). No Trama, o som é opcional, desligável e nunca o único sinal.
- O ícone é decorativo (`aria-hidden="true"`); o título ou um prefixo oculto ("Aviso:") transmite a intenção, porque a cor não atende a todos os públicos ([gov.br DS](https://www.gov.br/ds/components/message); WCAG 2.2, 1.4.1).
- O botão Fechar tem nome acessível e alvo de `--c-touch` em telas de toque.

## Tokens usados

| Intenção   | Fundo                | Borda                | Ícone              |
|------------|----------------------|----------------------|--------------------|
| Informação | `--t-info-subtle`    | `--t-info-border`    | `--t-info`         |
| Sucesso    | `--t-success-subtle` | `--t-success-border` | `--t-success`      |
| Aviso      | `--t-warning-subtle` | `--t-warning-border` | `--t-warning-fill` |
| Erro       | `--t-danger-subtle`  | `--t-danger-border`  | `--t-danger`       |

Todas usam texto em `--t-fg-1`, raio `--r-lg`, contorno `--stroke-thin`, preenchimento `--sp-300` por `--sp-400` e espaço interno `--sp-300`. A mensagem global e o banner crítico ocupam a largura toda e dispensam o raio. Dados complementares usam `--t-font-mono` em `--t-fg-2`. A mensagem contextual usa as cores fortes de cada intenção sobre o fundo da página.

## Considerações por plataforma

### Web desktop

Limite a largura do texto à coluna de leitura, mesmo quando a superfície da mensagem global ocupa a janela toda. A mensagem direcionada acompanha a largura do elemento a que se refere.

### Web móvel

Mensagens no topo empurram o conteúdo para baixo. Avalie a altura do banner crítico e da mensagem global na tela do celular e mantenha o texto curto ([Ontario](https://designsystem.ontario.ca/components/detail/critical-alerts.html)). Na grade de 4 colunas, a superfície vai até as bordas da tela e cresce em altura com o texto ([gov.br DS](https://www.gov.br/ds/components/message)). As ações descem para baixo do corpo e podem ocupar a largura toda.

### Tablets e dobráveis

Em layouts de dois painéis, coloque a mensagem direcionada no painel a que ela se refere. Mensagens que afetam o produto inteiro ficam acima dos dois painéis, nunca acima da navegação lateral ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)).

## Recursos

### Relacionados

- Toasts
- Resumo de erros
- Feedback
- Validação e mensagens de erro
- Cabeçalho
- Badges

### Referências

- [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) Apple HIG
- [Message](https://www.gov.br/ds/components/message) gov.br DS
- [Message bar](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage) Fluent 2
- [Notification banner](https://design-system.service.gov.uk/components/notification-banner/) GOV.UK
- [Inset text](https://design-system.service.gov.uk/components/inset-text/) GOV.UK
- [Warning text](https://design-system.service.gov.uk/components/warning-text/) GOV.UK
- [Beskeder](https://designsystem.dk/komponenter/beskeder/) DKFDS
- [Notification](https://hds.hel.fi/components/notification) Helsinki Design System
- [Note](https://vercel.com/geist/note) Geist
- [Project Banner](https://vercel.com/geist/project-banner) Geist
- [Page alerts](https://designsystem.ontario.ca/components/detail/page-alerts.html) Ontario Design System
- [Critical alerts](https://designsystem.ontario.ca/components/detail/critical-alerts.html) Ontario Design System
- [Callout](https://blueprintjs.com/docs/#core/components/callout) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta as mensagens global e contextual, a posição da mensagem global entre cabeçalho e breadcrumb, os dados complementares de erro, o foco ao exibir e ao fechar e o som opcional. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                           |
