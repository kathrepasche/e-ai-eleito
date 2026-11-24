# Radio

Um grupo de radios mostra todas as opções de uma vez e permite escolher exatamente uma.

Cada radio é um círculo seguido de um texto. Selecionado, mostra um círculo preenchido; não selecionado, um círculo vazio ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)). Ao escolher uma opção, a anterior é desmarcada ([DKFDS](https://designsystem.dk/komponenter/radioknap/)). No Trama, o radio usa a classe `.tr-check tr-check--radio` e vive sempre num `.tr-fieldset` com legenda. O gov.br compõe o radio com cabeçalho de opções, lista de opções e uma única mensagem para o conjunto, como no checkbox ([gov.br](https://www.gov.br/ds/components/radio)).

**Quando usar.** Para escolher uma opção entre duas e cerca de cinco, mutuamente exclusivas, quando a pessoa precisa ver e comparar todas antes de decidir ([Fluent](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage)). Os radios funcionam bem em telas de celular, desde que a lista caiba ([DKFDS](https://designsystem.dk/komponenter/radioknap/)).

**Quando não usar.**

- Várias respostas possíveis: use checkboxes ([GOV.UK](https://design-system.service.gov.uk/components/radios/)).
- Muitas opções ou pouco espaço: use select ou combobox ([gov.br](https://www.gov.br/ds/components/radio)). A HIG sugere outro componente a partir de cerca de cinco opções ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)), e o Geist, a partir de seis ([Geist](https://vercel.com/geist/radio)).
- Um ajuste que liga ou desliga na hora: use um switch ([Fluent](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage)).
- Uma única afirmação de sim ou não: prefira um checkbox, cuja marca torna o estado mais claro ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)).
- Trocar a visualização de um conteúdo: use o controle segmentado ou abas.

## Anatomia

1.  **Legenda** (`<legend>`): a pergunta ou o nome da escolha. É o primeiro elemento do fieldset ([GOV.UK](https://design-system.service.gov.uk/components/fieldset/)).
2.  **Dica do grupo** (`.tr-hint`, opcional).
3.  **Mensagem do grupo** (condicional): erro, validação ou alerta, uma só para todo o conjunto ([gov.br](https://www.gov.br/ds/components/radio)), abaixo da legenda.
4.  **Círculo**: 20px, borda de 2px `--t-border-control`; selecionado, borda e ponto em `--t-brand`.
5.  **Texto da opção** e **dica da opção** (opcional).
6.  **Divisor “ou”** (opcional): separa uma opção diferente das demais.
7.  **Pergunta condicional** (opcional): aparece abaixo da opção escolhida.

## Tipos

| Tipo               | Uso                                                                                                                                                                               |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Vertical           | Padrão. Mais fácil de escanear e de traduzir ([Fluent](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage)).                                             |
| Em linha           | Só com duas opções curtas, como Sim e Não ([GOV.UK](https://design-system.service.gov.uk/components/radios/)). Em janelas compactas, volta a empilhar.                            |
| Com dica por opção | Escolhas complexas: todas as opções recebem uma frase de apoio ([Fluent](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage)).                           |
| Cartão de escolha  | Opções que pedem descrição, preço ou ícone, como planos. Toda a área do cartão seleciona, e um indicador no canto mostra a escolha ([Geist](https://vercel.com/geist/choicebox)). |
| Pequeno            | Densidade alta, só com mouse: filtros de pesquisa e telas densas de uso recorrente ([GOV.UK](https://design-system.service.gov.uk/components/radios/)).                           |

## Boas práticas

**Não pré-selecione respostas de perguntas.** Uma opção marcada de antemão faz a pessoa não perceber que pulou a pergunta ou enviar a resposta errada ([GOV.UK](https://design-system.service.gov.uk/components/radios/)). Um padrão pode também parecer manipulação ([DKFDS](https://designsystem.dk/komponenter/radioknap/)).

**Em ajustes, pré-selecione o padrão mais seguro.** Quando o grupo configura algo, como o ciclo de cobrança, um valor inicial mostra que o campo já está configurado ([Geist](https://vercel.com/geist/radio)). Coloque o padrão em primeiro lugar ([Fluent](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage)).

**Inclua “Não sei” ou “Nenhuma” quando forem respostas válidas.** Depois de marcar um radio, não há como voltar a deixar o grupo vazio sem recarregar a página ([GOV.UK](https://design-system.service.gov.uk/components/radios/)).

**Ordene as opções com cuidado.** Use ordem alfabética por padrão. Ordenar da mais comum para a menos comum pode reforçar vieses; na dúvida, use a alfabética ([GOV.UK](https://design-system.service.gov.uk/components/radios/)). Valores com ordem natural, como faixas, vão do menor para o maior ([Fluent](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage)).

**Posicione o círculo à esquerda e empilhe as opções.** Isso facilita a leitura e o uso com ampliador de tela ([GOV.UK](https://design-system.service.gov.uk/components/radios/)). Toda a linha, círculo e texto, é clicável ([DKFDS](https://designsystem.dk/komponenter/radioknap/)). Prefira uma coluna; use duas só em caso de real necessidade, com a mesma largura nos itens da coluna e a mesma altura nos itens da linha ([gov.br](https://www.gov.br/ds/components/radio)).

**Diga que só uma opção vale, se houver dúvida.** A diferença visual entre radio e checkbox não basta; use a dica “Selecione uma opção” ([GOV.UK](https://design-system.service.gov.uk/components/radios/)).

**Revele só perguntas simples.** A opção escolhida pode revelar uma pergunta relacionada, como o número de telefone. Não revele perguntas a partir de radios em linha, e leve perguntas complexas para a próxima página ([GOV.UK](https://design-system.service.gov.uk/components/radios/)).

**No cartão de escolha, não coloque botões ou links dentro do cartão.** Eles roubariam o clique que seleciona a opção ([Geist](https://vercel.com/geist/choicebox)).

**Faça** radios em linha só para duas opções curtas, sem resposta pré-marcada.

**Não faça** opções longas lado a lado, com uma resposta já marcada.

### Estados e teclado

| Estado          | Aparência                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Não selecionado | Círculo vazio, borda `--t-border-control`                                                                                                                                                                              |
| Hover           | Camada `--o-hover` em volta do círculo; só com ponteiro ([gov.br](https://www.gov.br/ds/components/radio))                                                                                                             |
| Selecionado     | Borda `--t-brand` e ponto central `--t-brand`. Aciona com clique ou toque no círculo ou no texto, com as setas ou com Espaço ([gov.br](https://www.gov.br/ds/components/radio))                                        |
| Foco            | Anel de 2px `--t-focus` em volta do círculo, em `:focus-visible`                                                                                                                                                       |
| Inválido        | `.tr-error-msg` abaixo da legenda, para o grupo inteiro, quando a escolha é obrigatória ou incorreta                                                                                                                   |
| Válido          | `.tr-field-msg--success` no grupo, quando a resposta foi conferida, como num questionário com correção ([gov.br](https://www.gov.br/ds/components/radio))                                                              |
| Desabilitado    | Texto `--t-fg-disabled`. Só quando a pessoa pode habilitar a opção por uma ação dela, com o motivo ao lado, como “Disponível no plano anual” ([Geist](https://vercel.com/geist/radio)); caso contrário, retire a opção |

Tab entra e sai do grupo como uma única parada. Sem seleção, o foco vai para a primeira opção; com seleção, vai para a selecionada ([Fluent](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage)). As setas movem a seleção dentro do grupo e pulam opções desabilitadas ([Geist](https://vercel.com/geist/radio)). Espaço seleciona a opção em foco quando nenhuma está selecionada.

> **Divergência entre referências** *Teclado:* a página de acessibilidade do gov.br descreve o radio como navegável com Tab e acionado com Espaço; Fluent e Geist tratam o grupo como uma única parada de Tab, com setas entre as opções, que é o comportamento nativo dos navegadores. Pelo critério de acessibilidade (menos paradas de Tab e o comportamento que leitores de tela anunciam), o Trama segue o comportamento nativo. *Tamanho do texto da opção:* a HDS sugere até três palavras; o gov.br aceita até sete e evita linhas com mais de 10 palavras ou 56 caracteres em média. Pelo critério de contexto brasileiro, o Trama segue o gov.br. *Posição da mensagem:* o gov.br a põe abaixo do último item; o GOV.UK, abaixo da legenda. O Trama mantém abaixo da legenda, como no checkbox. *Opção padrão:* o gov.br prevê radio selecionado por padrão com `checked`; o GOV.UK proíbe pré-selecionar respostas. O Trama pré-seleciona só em ajustes, nunca em perguntas.

## Conteúdo

**Legenda.** Normalmente uma pergunta ou um verbo no imperativo, em caixa de frase ([gov.br](https://www.gov.br/ds/components/radio)), sem dois-pontos no fim ([Fluent](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage)). Numa página de uma pergunta, a legenda pode ser o título da página, e o leitor de tela a anuncia uma vez só ([GOV.UK](https://design-system.service.gov.uk/components/radios/)).

**Opções.** Fragmentos curtos, com só a primeira letra maiúscula e sem ponto final. Se o texto for longo, deixe quebrar a linha; nunca corte com reticências ([Fluent](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage)). Mantenha construção paralela, como “Mensal” e “Anual”; evite misturar “Mensal” com “Pagar por ano” ([Geist](https://vercel.com/geist/radio)). Cada texto diz o que acontece se for escolhido. Use até sete palavras e mantenha a linha abaixo de 10 palavras ou 56 caracteres; se passar, quebre a linha alinhada ao texto ([gov.br](https://www.gov.br/ds/components/radio)).

**Dicas por opção.** Use em todas as opções ou em nenhuma ([Fluent](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage)). Uma frase curta, sem links ([GOV.UK](https://design-system.service.gov.uk/components/radios/)).

**Erros.**

| Situação                          | Modelo                                          |
|-----------------------------------|-------------------------------------------------|
| Pergunta de sim ou não            | Selecione sim se Ana mora com você              |
| Duas opções que não são sim e não | Selecione se você é empregado ou autônomo       |
| Mais de duas opções               | Selecione o dia da semana em que paga o aluguel |

Os modelos seguem a estrutura do GOV.UK ([GOV.UK](https://design-system.service.gov.uk/components/radios/)).

## Acessibilidade

- Agrupe os radios em `<fieldset>` com `<legend>`; todos compartilham o mesmo `name`.
- Use `<input type="radio">` nativo. Não substitua o anel de foco por um estilo que remove o afastamento ([Geist](https://vercel.com/geist/radio)).
- Use `required` no grupo, não numa opção isolada ([Geist](https://vercel.com/geist/radio); [gov.br](https://www.gov.br/ds/components/radio)). Num ajuste com valor padrão, marque-o com `checked` ([gov.br](https://www.gov.br/ds/components/radio)).
- A mudança de seleção é anunciada pelo leitor de tela; não a substitua por um aviso visual sem texto ([gov.br](https://www.gov.br/ds/components/radio)).
- Mostre a seleção por forma, com o ponto central, além da cor (WCAG 2.2, 1.4.1). No cartão de escolha, a borda destacada vem acompanhada do indicador no canto ([Geist](https://vercel.com/geist/choicebox)).
- Perguntas reveladas nem sempre são anunciadas pelos leitores de tela, o que falha o WCAG 2.2, 4.1.2 ([GOV.UK](https://design-system.service.gov.uk/components/radios/)).
- Use as combinações de cor do sistema, já verificadas para WCAG AA ([HDS](https://hds.hel.fi/components/radio-button/accessibility)).

## Tokens usados

| Elemento                     | Token                                                                    |
|------------------------------|--------------------------------------------------------------------------|
| Borda do círculo             | `--stroke-thick`, `--t-border-control`                                   |
| Selecionado                  | `--t-brand` (borda e ponto), `--t-surface-raised` (anel interno)         |
| Espaço entre círculo e texto | `--sp-300`                                                               |
| Altura mínima da linha       | `--c-touch`; com mouse, em telas densas, área de ação de pelo menos 24px |
| Hover                        | `--o-hover`                                                              |
| Mensagens                    | `--t-danger`, `--t-success`                                              |
| Espaço entre opções em linha | `--sp-300`                                                               |
| Cartão de escolha            | `--r-lg`, `--t-border`; selecionado `--t-brand` e `--t-brand-subtle`     |
| Legenda                      | 16/24 semibold, `--t-fg-1`                                               |
| Foco                         | `--t-focus`                                                              |

## Considerações por plataforma

### Web desktop

Ao exibir radios na horizontal, use um espaçamento consistente, medido pela opção mais longa ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)). Não coloque radios em barras de ferramentas ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)).

### Web móvel

Radios em linha voltam a empilhar em telas pequenas ([GOV.UK](https://design-system.service.gov.uk/components/radios/)). Garanta espaço em volta de cada opção para o toque ([DKFDS](https://designsystem.dk/komponenter/radioknap/)). Cartões de escolha oferecem área de toque maior para opções com descrição ([Geist](https://vercel.com/geist/choicebox)).

### Tablets e dobráveis

Cartões de escolha podem formar uma grade de duas ou três colunas em janelas expandidas, limitada a cerca de quatro a seis cartões ([Geist](https://vercel.com/geist/choicebox)). Em dobráveis abertos, mantenha o grupo inteiro num painel.

## Recursos

### Relacionados

- Checkbox
- Select e dropdown
- Controle segmentado
- Switch
- Formulários em etapas e páginas de pergunta

### Referências

- [Radio](https://www.gov.br/ds/components/radio) gov.br DS
- [Toggles (Radio buttons)](https://developer.apple.com/design/human-interface-guidelines/toggles) Apple HIG
- [Radios](https://design-system.service.gov.uk/components/radios/) GOV.UK Design System
- [Fieldset](https://design-system.service.gov.uk/components/fieldset/) GOV.UK Design System
- [Radioknap](https://designsystem.dk/komponenter/radioknap/) Det Fælles Designsystem
- [RadioButton](https://hds.hel.fi/components/radio-button) Helsinki Design System
- [RadioButton: acessibilidade](https://hds.hel.fi/components/radio-button/accessibility) Helsinki Design System
- [Radio group](https://fluent2.microsoft.design/components/web/react/core/radiogroup/usage) Fluent 2
- [Radio](https://vercel.com/geist/radio) Geist
- [Choicebox](https://vercel.com/geist/choicebox) Geist

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                   |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta estados de hover, válido e inválido, uma mensagem por grupo, limites de texto do gov.br e a preferência por uma coluna, e registra a decisão sobre o teclado. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                            |
