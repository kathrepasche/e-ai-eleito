# IndicadorDeEtapas

O indicador de etapas mostra em que ponto de um fluxo de várias etapas a pessoa está, quantas faltam e quais precisam de atenção.

Em fluxos longos, saber onde se está reduz a incerteza. O Trama oferece três formas: o indicador textual, um texto "Etapa 2 de 4" acima do título da página; a lista de etapas, que mostra todas as etapas com seus rótulos e estados, na horizontal ou na vertical; e o indicador de pontos, para sequências curtas dentro de outros componentes. O indicador textual é o padrão. Equipes do GOV.UK removeram listas de etapas sem efeito negativo nas taxas e nos tempos de conclusão, e o Ontario deixou de recomendá-las por ocuparem espaço e escalarem mal em telas pequenas ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/), [Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html)).

**Use um indicador de etapas** em fluxos com etapas sequenciais relacionadas entre si, quando ajuda a pessoa saber o tamanho do caminho e o que já concluiu ([gov.br DS](https://www.gov.br/ds/components/step), [DKFDS](https://designsystem.dk/komponenter/trinindikator/)).

**Não use um indicador de etapas** antes de testar o formulário sem ele: melhore primeiro a ordem, o tipo e o número de perguntas ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)). Se as etapas não têm relação entre si ou não há progressão, use abas ou um menu ([gov.br DS](https://www.gov.br/ds/components/step)). Quando a pessoa faz as tarefas em qualquer ordem e em várias sessões, use uma lista de tarefas com badges de status ([GOV.UK](https://design-system.service.gov.uk/components/task-list/)). Para progresso de uma operação do sistema, use uma barra de progresso. Não use como menu lateral nem junto com navegação lateral ou breadcrumb ([DKFDS](https://designsystem.dk/komponenter/trinindikator/)).

## Anatomia

### Indicador textual

1.  **Texto de posição**: "Etapa 2 de 4", Caption em `--t-fg-3`, logo acima do `h1`.
2.  **Título da etapa**: o `h1` da página, único e ligado ao que é pedido nela ([Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html)).

### Lista de etapas

1.  **Marcador**: círculo de 28px com o número, contorno `--stroke-thick`. Define o estado e serve de área interativa ([gov.br DS](https://www.gov.br/ds/components/step)).
2.  **Rótulo**: nome curto da etapa, à direita do marcador, alinhado ao início. Use uma só posição de rótulo no produto inteiro ([gov.br DS](https://www.gov.br/ds/components/step)).
3.  **Linha do tempo** (opcional): liga os marcadores e dá sentido de sequência ([gov.br DS](https://www.gov.br/ds/components/step)).
4.  **Estado**: concluída (preenchida com `--t-brand` e marca de verificação), atual (contorno `--t-brand`, texto em peso 600), futura (contorno `--t-border-control`, texto `--t-fg-3`), com erro (`data-state="error"`, `--t-danger`) e com alerta (`data-state="warning"`, `--t-warning`).

## Tipos

| Tipo                                   | Quando usar                                                                                                                                                                                                                        |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Textual                                | Padrão. Formulários em que a pessoa só avança e volta ([DKFDS](https://designsystem.dk/komponenter/trinindikator/)), e sequências longas demais para mostrar todas as etapas ([gov.br DS](https://www.gov.br/ds/components/step)). |
| Lista horizontal                       | Fluxos em que conhecer as próximas etapas ajuda a planejar, ou em que a pessoa revisita etapas anteriores, em janelas Expandida em diante. Só com evidência de pesquisa a favor.                                                   |
| Lista vertical (`.tr-steps--vertical`) | Os mesmos fluxos em janelas Compacta e Média, ou em layouts com coluna lateral para as etapas. O conteúdo da etapa atual pode ficar logo abaixo dela ou ao lado da lista ([gov.br DS](https://www.gov.br/ds/components/step)).     |
| Pontos                                 | Sequências de 4 a 5 itens dentro de outros componentes, como um carrossel ou um card, sempre com botões de avançar e voltar ([gov.br DS](https://www.gov.br/ds/components/step)). Acima disso, use o textual.                      |

## Boas práticas

**Mostre o total só se ele for confiável.** Fluxos com etapas condicionais mudam de tamanho; nesses casos, o indicador textual sem total ("Etapa 2") é mais honesto ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)).

**Divida as etapas de um jeito natural para a pessoa.** Agrupe perguntas relacionadas e evite etapas com uma pergunta só. Uma etapa reúne ao menos três componentes de formulário ([HDS](https://hds.hel.fi/components/stepper), [Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html)). Apresente as etapas numa ordem lógica ([gov.br DS](https://www.gov.br/ds/components/step)).

**Escolha a progressão pela dependência entre as etapas.** Na progressão linear, padrão do Trama, cada etapa depende da anterior: as futuras ficam indisponíveis até a anterior ser concluída, e as concluídas continuam acessíveis para revisão ([HDS](https://hds.hel.fi/components/stepper), [DKFDS](https://designsystem.dk/komponenter/trinindikator/), [gov.br DS](https://www.gov.br/ds/components/step)). Na progressão não linear, todas as etapas ficam interativas e a pessoa navega livremente; use-a quando nenhuma etapa depende de outra e o fluxo cabe numa sessão ([gov.br DS](https://www.gov.br/ds/components/step)).

**Explique por que uma etapa futura está indisponível.** No texto acessível e, se houver espaço, em texto visível: "disponível depois das etapas anteriores". Uma etapa indisponível sem explicação deixa a pessoa sem saber o que fazer.

**Sinalize erros e pendências em texto.** Uma etapa concluída com problema mostra o estado de erro ou de alerta no marcador e no rótulo ([gov.br DS](https://www.gov.br/ds/components/step)), e o detalhe aparece em texto: abaixo do rótulo na lista vertical, no texto acessível e na página da etapa, com resumo de erros ([DKFDS](https://designsystem.dk/komponenter/trinindikator/)). Quando a etapa com erro é a atual, ela mantém o destaque de etapa atual além do estado de erro ([gov.br DS](https://www.gov.br/ds/components/step)).

**Termine na revisão.** A última etapa é a revisão das respostas. A página de confirmação vem depois e não aparece no indicador, assim como páginas de introdução ([DKFDS](https://designsystem.dk/komponenter/trinindikator/), [Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html)).

**Não aninhe etapas.** Subetapas tornam o fluxo complexo; seções dentro de uma etapa não ganham indicador próprio ([DKFDS](https://designsystem.dk/komponenter/trinindikator/), [Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html)).

**Não acrescente porcentagem nem tempo.** Um indicador de progresso por etapa basta ([Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html)).

**Ofereça Voltar e Continuar em cada etapa.** "Continuar" nas etapas intermediárias e "Concluir" na última. O botão Voltar do navegador leva à etapa anterior, no estado em que a pessoa a deixou ([Ontario](https://designsystem.ontario.ca/components/detail/step-indicator.html), [GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)). O indicador de pontos depende desses controles: ele nunca é o único meio de navegar ([gov.br DS](https://www.gov.br/ds/components/step)).

**Prefira a lista vertical à rolagem horizontal.** Se a lista horizontal não cabe numa linha, encurte os rótulos ou passe para a vertical ([HDS](https://hds.hel.fi/components/stepper)). Se a horizontal for inevitável em janelas estreitas, mostre no máximo 4 etapas visíveis, deixe as demais acessíveis por rolagem e marque com sombra os lados onde há etapas ocultas ([gov.br DS](https://www.gov.br/ds/components/step)).

**Faça** comece pelo indicador textual, com título único por etapa.

**Não faça** crie muitas etapas, subetapas e rótulos genéricos que quebram linha.

### Estados e comportamento

- **Interativa**: etapas concluídas e, na progressão não linear, as não visitadas. Recebem hover, pressionado e foco; a área de ação inclui marcador e rótulo, com no mínimo 24px no mouse e `--c-touch` no toque ([gov.br DS](https://www.gov.br/ds/components/step)).
- **Atual**: uma única etapa, com `aria-current="step"`.
- **Indisponível**: etapas futuras na progressão linear, como texto fora da ordem de tabulação, com a explicação no texto acessível.
- **Erro e alerta**: erro para um impedimento, alerta para uma pendência; sempre com texto ([gov.br DS](https://www.gov.br/ds/components/step), [HDS](https://hds.hel.fi/components/stepper)).
- **Troca de etapa**: ao avançar, o foco vai para o título `h1` da nova etapa ([HDS](https://hds.hel.fi/components/stepper/accessibility)).
- **Sequência automática**: se os pontos avançam sozinhos, como num carrossel, ofereça pausar e retomar ([gov.br DS](https://www.gov.br/ds/components/step)).

> **Divergência entre referências** Forma padrão: o gov.br DS tem como forma principal o indicador com marcadores e rótulos (step complexo); o GOV.UK e o Ontario recomendam o texto simples, com relato de equipes que removeram a lista sem prejuízo. Pelo critério de evidência, o padrão do Trama é o indicador textual. Formato do texto: o gov.br escreve "etapa atual / total", como "2/4"; o Trama mantém "Etapa 2 de 4", que o leitor de tela lê sem ambiguidade (critério de acessibilidade). Detalhe do erro: o gov.br mostra o detalhe de erros e pendências em tooltip por hover, e usa tooltip para nomear etapas sem rótulo; o Trama exige o detalhe e o rótulo em texto, porque o hover não existe no toque nem no teclado (critério de acessibilidade). Telas estreitas: o gov.br aceita a lista horizontal com rolagem e até 4 etapas visíveis; o HDS trata a rolagem como último recurso. O Trama prefere a lista vertical, que acompanha o reflow (WCAG 2.2, 1.4.10), e usa o limite de 4 do gov.br quando a horizontal for inevitável. Progressão: a versão 1.0 só admitia a linear; o Trama passa a aceitar a não linear do gov.br quando as etapas são independentes, e mantém a lista de tarefas do GOV.UK para fluxos em várias sessões.

## Conteúdo

**Nomeie cada etapa pelo que ela pede.** "Imóvel", "Documentos". O ideal é uma palavra; no máximo três ([gov.br DS](https://www.gov.br/ds/components/step)). Use substantivos em caixa de frase. O rótulo é obrigatório mesmo quando fica oculto visualmente ([HDS](https://hds.hel.fi/components/stepper)).

**Escreva a posição sempre igual.** "Etapa 2 de 4" em todo o produto, sem variações como "Passo" ou "2/4".

**Descreva erros e pendências em poucas palavras.** Diga o que falta: "Comprovante ilegível", "Falta a matrícula" ([gov.br DS](https://www.gov.br/ds/components/step)). Sem culpar a pessoa.

## Acessibilidade

- A lista de etapas é uma lista ordenada (`<ol>`) dentro de um `<nav>` com rótulo. A etapa atual tem `aria-current="step"` ([HDS](https://hds.hel.fi/components/stepper/accessibility)).
- Etapas que levam a outra página são links; etapas que trocam o conteúdo na mesma página são `<button>` ([gov.br DS](https://www.gov.br/ds/components/step)). Tab e Shift+Tab percorrem as etapas interativas, e Enter ou Espaço as acionam, com foco visível em cada uma.
- O estado de cada etapa aparece em texto, mesmo oculto: "Solicitante, concluída", "Pagamento, com erro: comprovante ilegível". O ícone e a cor são reforço (WCAG 2.2, 1.4.1).
- Indicadores sem rótulo visível, como os pontos, têm nome acessível com a ação e a posição: "Ir para o item 2 de 4" ([gov.br DS](https://www.gov.br/ds/components/step)).
- Anuncie a conclusão de uma etapa e os erros numa região viva. Um som curto pode reforçar o anúncio, como sugere o [gov.br DS](https://www.gov.br/ds/components/step); no Trama, ele é opcional e desligável.
- Cada etapa tem um título de página próprio (`<title>` e `h1`), com a posição no título do documento: "Dados do imóvel, etapa 2 de 4" (WCAG 2.2, 2.4.2).

## Tokens usados

| Elemento             | Token                                          |
|----------------------|------------------------------------------------|
| Texto de posição     | `--t-fg-3`, Caption 12/16                      |
| Marcador concluído   | `--t-brand`, `--t-on-brand`                    |
| Marcador atual       | `--t-brand`, `--stroke-thick`                  |
| Marcador futuro      | `--t-border-control`, texto `--t-fg-3`         |
| Erro e alerta        | `--t-danger`, `--t-warning`                    |
| Estados de interação | `--o-hover`, `--o-pressed`, `--t-focus`        |
| Espaço entre etapas  | `--sp-200` (horizontal), `--sp-300` (vertical) |

## Considerações por plataforma

### Web desktop

A lista horizontal fica acima do título da página, alinhada à coluna do formulário. A lista vertical pode ocupar uma coluna ao lado do conteúdo da etapa ([gov.br DS](https://www.gov.br/ds/components/step)), desde que a página não tenha navegação lateral, com que concorreria.

### Web móvel

Na classe Compacta, use o indicador textual. Se o produto usa a lista de etapas, use a vertical, ou mostre no topo um botão "Etapa 2 de 4" que abre a lista completa numa folha inferior, como faz o [DKFDS](https://designsystem.dk/komponenter/trinindikator/). Com rótulos ao lado, só o número cabe em telas estreitas ([gov.br DS](https://www.gov.br/ds/components/step)); nesse caso o rótulo continua no nome acessível e aparece no título da página.

### Tablets e dobráveis

Na classe Média, prefira a lista vertical ([gov.br DS](https://www.gov.br/ds/components/step)). Na Expandida, a lista horizontal com rótulos cabe numa linha quando os rótulos são curtos. Ao abrir ou fechar um dobrável, a pessoa continua na mesma etapa, com as respostas preservadas, e a lista troca de orientação sem perder o estado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

> **Nota** A Apple HIG não tem um componente de etapas para formulários. O mais próximo é o controle de página, que representa a posição numa lista ordenada de páginas e fica difícil de contar acima de cerca de 10 pontos ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/page-controls)). A HIG também pede que tarefas modais com várias vistas tenham um caminho único ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/modality)), princípio que o Trama aplica à progressão linear.

## Recursos

### Relacionados

- Formulários em etapas e páginas de pergunta
- Revisar respostas e confirmação
- Resumo de erros
- Indicadores de progresso
- Carrossel
- Lista de resumo

### Referências

- [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls) Apple HIG
- [Modality](https://developer.apple.com/design/human-interface-guidelines/modality) Apple HIG
- [Step](https://www.gov.br/ds/components/step) gov.br DS
- [Question pages](https://design-system.service.gov.uk/patterns/question-pages/) GOV.UK
- [Task list](https://design-system.service.gov.uk/components/task-list/) GOV.UK
- [Trinindikator](https://designsystem.dk/komponenter/trinindikator/) DKFDS
- [Stepper](https://hds.hel.fi/components/stepper) Helsinki Design System
- [Stepper: accessibility](https://hds.hel.fi/components/stepper/accessibility) Helsinki Design System
- [Step indicator](https://designsystem.ontario.ca/components/detail/step-indicator.html) Ontario Design System
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                            |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a lista vertical, a progressão não linear, os estados de erro e alerta, o indicador de pontos, o limite de 4 etapas visíveis em janelas estreitas e a área de ação por densidade, e passa o último botão a "Concluir". |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                     |
