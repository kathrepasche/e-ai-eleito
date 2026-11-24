# EntradaESeletorDeData

A entrada de data recebe dia, mês e ano em três campos; o seletor de data e hora mostra um calendário e um seletor de horário para escolher datas e horas próximas.

O Trama oferece duas formas de pedir datas, e a escolha depende do tipo de data. Três campos separados para dia, mês e ano são a forma mais fácil de digitar uma data conhecida ([DKFDS](https://designsystem.dk/komponenter/datofelter/)). O calendário ajuda quando a pessoa precisa ver a data em relação a outras ou saber o dia da semana ([GOV.UK](https://design-system.service.gov.uk/patterns/dates/)). O gov.br divide o seletor em calendário e seletor de horário, que funcionam juntos ou separados ([gov.br](https://www.gov.br/ds/components/datetimepicker)).

| Tipo de data                                     | Exemplo                         | Componente                                                                                            |
|--------------------------------------------------|---------------------------------|-------------------------------------------------------------------------------------------------------|
| Data que a pessoa sabe ou consulta num documento | Nascimento, emissão do RG       | Entrada de data (três campos)                                                                         |
| Data de documento ou cartão                      | Validade do cartão (mês e ano)  | Campos no mesmo formato do documento ([GOV.UK](https://design-system.service.gov.uk/patterns/dates/)) |
| Data aproximada                                  | “Dezembro de 2023”              | Mês e ano, sem o dia ([GOV.UK](https://design-system.service.gov.uk/patterns/dates/))                 |
| Data escolhida entre opções disponíveis          | Agendamento, audiência, entrega | Seletor de data com digitação                                                                         |
| Data e hora de um compromisso                    | Início da audiência             | Seletor de data e seletor de horário                                                                  |
| Período                                          | Início e término de férias      | Duas entradas com o intervalo destacado no calendário                                                 |

**Quando não usar.** Não use o calendário para datas fáceis de lembrar ou muito distantes, como a data de nascimento ([HDS](https://hds.hel.fi/components/date-input)): para datas a mais de um ano de hoje, ele obriga a muitos cliques ([DKFDS](https://designsystem.dk/komponenter/datovaelger/)). Não use a entrada de data se a pessoa provavelmente não sabe a data exata ([GOV.UK](https://design-system.service.gov.uk/components/date-input/)). Não use três selects para dia, mês e ano.

## Anatomia

### Entrada de data

1.  **Legenda**: a pergunta, num `<fieldset>` que agrupa os três campos ([GOV.UK](https://design-system.service.gov.uk/components/date-input/)).
2.  **Dica**: um exemplo de data válida para a pergunta.
3.  **Campos Dia, Mês e Ano** (`.tr-date`): cada um com rótulo próprio.
4.  **Mensagem de erro**: abaixo da legenda, para a data inteira ou para um campo.

### Seletor de data e hora

1.  **Campo de texto** com a data no formato dia/mês/ano e, quando houver, a hora no formato hora:minuto ([gov.br](https://www.gov.br/ds/components/datetimepicker)), sempre editável à mão.
2.  **Botão de calendário**: ação interna que abre o calendário (`.tr-calendar`) num popover na camada `--z-2`.
3.  **Cabeçalho** (`.tr-calendar__head`): mês por extenso e ano, com botões de mês anterior e seguinte ([gov.br](https://www.gov.br/ds/components/datetimepicker)).
4.  **Grade de dias**: dias da semana abreviados com três letras, domingo primeiro; hoje em destaque, dia escolhido, intervalo e dias bloqueados ([gov.br](https://www.gov.br/ds/components/datetimepicker)).
5.  **Seletor de horário** (`.tr-timepicker`): campos de hora e minuto em 24 horas ([gov.br](https://www.gov.br/ds/components/datetimepicker)).
6.  **Ações**: Cancelar e Confirmar, alinhadas ao fim, com a principal por último.

## Boas práticas

**Ordene os campos como no Brasil: dia, mês e ano.** Use a ordem de data do país do serviço ([DKFDS](https://designsystem.dk/komponenter/datofelter/)). Em produtos traduzidos, a ordem segue o idioma. Veja Internacionalização.

**Mostre um exemplo que deixe a ordem óbvia.** Use um dia de 13 ou mais e um mês de 9 ou menos, como “27 3 1985” ([GOV.UK](https://design-system.service.gov.uk/patterns/dates/)), válido para a pergunta ([GOV.UK](https://design-system.service.gov.uk/components/date-input/)).

**Aceite a data em qualquer formato digitado.** Nos três campos, aceite zero à esquerda ou não e o mês escrito, como “março” ou “mar”: o GOV.UK viu os erros caírem muito depois de aceitar nomes de mês ([GOV.UK](https://design-system.service.gov.uk/components/date-input/)). No seletor, aceite barras, pontos, hífens ou espaços e normalize para dia/mês/ano ao sair do campo ([DKFDS](https://designsystem.dk/komponenter/datovaelger/)). Nunca bloqueie a digitação com máscara.

**Nunca mova o foco sozinho entre os campos.** Pular do dia para o mês confunde e conflita com os controles normais do teclado ([GOV.UK](https://design-system.service.gov.uk/components/date-input/)).

**Escreva o calendário em português e comece no domingo.** Mês por extenso, dias da semana com três letras e domingo como primeiro dia ([gov.br](https://www.gov.br/ds/components/datetimepicker)). Destaque o dia de hoje ([gov.br](https://www.gov.br/ds/components/datetimepicker)).

**Ofereça navegação rápida entre meses e anos.** Além das setas de mês, permita escolher o mês numa lista e digitar o ano ([gov.br](https://www.gov.br/ds/components/datetimepicker)).

**Limite as datas possíveis e explique por quê.** Defina mínimo e máximo ([DKFDS](https://designsystem.dk/komponenter/datovaelger/)) e diga o motivo dos bloqueios na dica: “Dias úteis entre 16 e 30 de outubro” ([HDS](https://hds.hel.fi/components/date-input/accessibility)).

**Peça períodos com duas entradas e destaque o intervalo.** Use um campo de início e outro de término ([HDS](https://hds.hel.fi/components/date-input)). No calendário, os dias entre as duas datas ficam destacados, e os dias anteriores à data inicial ficam bloqueados para evitar uma escolha inválida por descuido ([gov.br](https://www.gov.br/ds/components/datetimepicker)). Ao reabrir, preserve o intervalo ([Geist](https://vercel.com/geist/calendar)).

**Peça confirmação no calendário em serviços para o público.** A HDS considera que fechar o calendário assim que a pessoa toca num dia fere o critério WCAG 2.2, 3.2.2, e dispensa a confirmação só em ferramentas internas em que se escolhem muitas datas seguidas ([HDS](https://hds.hel.fi/components/date-input)).

**Use 24 horas e deixe o campo de hora vazio até a escolha.** O seletor de horário usa o formato de 24 horas e abre em 00:00 ([gov.br](https://www.gov.br/ds/components/datetimepicker)), mas o campo só recebe a hora quando a pessoa confirma. Considere intervalos de minuto maiores que um, como de 15 em 15 ([Apple](https://developer.apple.com/design/human-interface-guidelines/pickers)). Respeite o fuso da pessoa e nunca mostre a hora em UTC sem avisar ([Geist](https://vercel.com/geist/calendar)).

**Faça** campos no mesmo formato do documento.

**Não faça** calendário para a data de nascimento: a pessoa navega décadas mês a mês.

### Estados e teclado

| Estado      | Aparência                                                                                                                                                      |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hover       | Nos campos e nos dias, camada `--o-hover`                                                                                                                      |
| Foco        | Anel `--t-focus` nos campos, nos botões e no dia em foco                                                                                                       |
| Hoje        | `aria-current="date"`, contorno `--t-brand`; independe da ação da pessoa                                                                                       |
| Selecionado | `aria-pressed="true"`, fundo `--t-brand`                                                                                                                       |
| Intervalo   | Dias entre início e término em `--t-brand-subtle`                                                                                                              |
| Bloqueado   | `--t-fg-disabled`, com o motivo na dica                                                                                                                        |
| Erro        | Na data inteira, destaque os três campos; em um campo, só ele, e diga qual na mensagem ([GOV.UK](https://design-system.service.gov.uk/components/date-input/)) |

Com vários erros, mostre o mais prioritário: primeiro informação faltando, depois informação impossível, depois as demais regras ([GOV.UK](https://design-system.service.gov.uk/components/date-input/)).

**Teclado.** Tab percorre os campos e as ações internas na ordem. Enter ou Espaço no botão abre o calendário; Esc fecha e devolve o foco ao botão ([gov.br](https://www.gov.br/ds/components/datetimepicker)). No calendário, as setas movem entre dias, Shift com seta salta uma semana, Page Up e Page Down mudam de mês ([Geist](https://vercel.com/geist/calendar)), e Enter escolhe o dia.

> **Divergência entre referências** *Três campos ou campo único:* o gov.br pede não dividir campos e usa um campo único com máscara e calendário; GOV.UK e DKFDS usam três campos para datas conhecidas, e o DKFDS cita literatura de pesquisa (Silver, 2018; Enders, 2016) para isso. Pelo critério de evidência, o Trama mantém três campos para datas conhecidas e usa o campo único só no seletor. *Fechar ao escolher:* no gov.br, escolher o dia preenche o campo e fecha o calendário; a HDS exige confirmação por acessibilidade. Pelo critério de acessibilidade, o Trama pede confirmação em serviços para o público. *Abertura:* o gov.br abre o calendário ao clicar no campo; o DKFDS descreve o seletor como um campo com botão, e a HDS recomenda a digitação manual como uso principal. Por convergência, o Trama abre pelo botão, para que clicar no campo sirva para digitar. *Horário padrão:* o gov.br indica 00:00 nos campos; o Trama abre o seletor em 00:00, mas não grava esse valor sem a escolha da pessoa, pelo mesmo motivo que proíbe pré-selecionar respostas ([GOV.UK](https://design-system.service.gov.uk/components/radios/)).

## Conteúdo

**Legenda e rótulo.** Diga qual data se espera: “Data de chegada”, “Quando o documento foi emitido?” ([HDS](https://hds.hel.fi/components/date-input)).

**Formato.** No seletor, mostre o formato na dica, em linguagem humana, e não só no placeholder ([HDS](https://hds.hel.fi/components/date-input)): “No formato dia/mês/ano, como 27/03/2026”. Para hora: “Formato de 24 horas, como 14:30”.

**Erros.**

| Situação                        | Modelo                                                                                        |
|---------------------------------|-----------------------------------------------------------------------------------------------|
| Nada preenchido                 | Digite sua data de nascimento                                                                 |
| Incompleta                      | A data de nascimento deve incluir um mês                                                      |
| Ano incompleto                  | O ano deve ter 4 números                                                                      |
| Impossível                      | A data de nascimento deve ser uma data real                                                   |
| Futura, quando deve ser passada | A data de nascimento deve ser no passado                                                      |
| Antes de outra data             | A data de término deve ser igual ou posterior a 1 de setembro de 2026, quando o curso começou |
| Hora impossível                 | A hora deve ser entre 00:00 e 23:59                                                           |

Os modelos de data seguem a estrutura do GOV.UK ([GOV.UK](https://design-system.service.gov.uk/components/date-input/)).

## Acessibilidade

- Agrupe os três campos num `<fieldset>` com `<legend>`; cada campo tem seu `<label>` ([GOV.UK](https://design-system.service.gov.uk/components/date-input/)).
- Para data de nascimento, use `autocomplete="bday-day"`, `"bday-month"` e `"bday-year"` ([GOV.UK](https://design-system.service.gov.uk/components/date-input/); WCAG 2.2, 1.3.5). Use `inputmode="numeric"` e evite `type="number"`.
- Use `<input type="date">` ou `type="text"` no seletor ([gov.br](https://www.gov.br/ds/components/datetimepicker)). Cada dia é um botão com a data completa no nome acessível: “Quarta-feira, 21 de outubro de 2026”, e não só “21” ([gov.br](https://www.gov.br/ds/components/datetimepicker)).
- Prenda o foco no calendário enquanto ele estiver aberto ([Geist](https://vercel.com/geist/calendar)) e anuncie a troca de mês e de intervalo numa região `aria-live="polite"`.
- Diferencie hoje, selecionado e bloqueado por mais de uma pista além da cor, e verifique o contraste dos fundos ([HDS](https://hds.hel.fi/components/date-input/accessibility)).
- Em toque, cada elemento interativo do calendário tem área mínima de 44px ([gov.br](https://www.gov.br/ds/components/datetimepicker)), igual a `--c-touch`.

## Tokens usados

| Elemento                        | Token                                                                       |
|---------------------------------|-----------------------------------------------------------------------------|
| Campos                          | Tokens de `.tr-input`; altura `--d-control`; espaço entre campos `--sp-300` |
| Calendário e seletor de horário | `--t-surface-raised`, `--e-4`, `--z-2`, `--r-lg`, preenchimento `--sp-300`  |
| Dia                             | 36px com mouse; `--c-touch` em toque                                        |
| Dia selecionado                 | `--t-brand` com texto `--t-on-brand`                                        |
| Hoje                            | Contorno `--stroke-thin` em `--t-brand`                                     |
| Intervalo                       | `--t-brand-subtle`                                                          |
| Dia bloqueado                   | `--t-fg-disabled`                                                           |
| Horas e minutos                 | `--t-font-mono`, 18px                                                       |

## Considerações por plataforma

### Web desktop

O calendário abre num popover abaixo do campo e muda de direção perto da borda da tela. Em painéis de análise, mostre o calendário ao lado dos resultados e ofereça atalhos para os períodos comuns ([Geist](https://vercel.com/geist/calendar)).

### Web móvel

O seletor funciona em qualquer largura até a grade de quatro colunas ([gov.br](https://www.gov.br/ds/components/datetimepicker)). Na classe Compacta, prefira o `<input type="date">` nativo, que abre o seletor do sistema; a HIG mostra a data num botão e abre o calendário numa camada modal perto do campo ([Apple](https://developer.apple.com/design/human-interface-guidelines/pickers)). Num calendário próprio, cada dia tem `--c-touch` de alvo.

### Tablets e dobráveis

Em janelas expandidas, o seletor de intervalo pode mostrar dois meses lado a lado; em espaços estreitos, empilhe os meses ([Geist](https://vercel.com/geist/calendar)). Num dobrável aberto, não deixe o calendário cruzar a dobra.

## Recursos

### Relacionados

- Campos de texto
- Popovers
- Validação e mensagens de erro
- Internacionalização e direita para esquerda
- Entrada de dados

### Referências

- [DateTimePicker](https://www.gov.br/ds/components/datetimepicker) gov.br DS
- [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) Apple HIG
- [Date input](https://design-system.service.gov.uk/components/date-input/) GOV.UK Design System
- [Dates](https://design-system.service.gov.uk/patterns/dates/) GOV.UK Design System
- [Radios](https://design-system.service.gov.uk/components/radios/) GOV.UK Design System
- [Datofelter](https://designsystem.dk/komponenter/datofelter/) Det Fælles Designsystem
- [Datovælger](https://designsystem.dk/komponenter/datovaelger/) Det Fælles Designsystem
- [DateInput](https://hds.hel.fi/components/date-input) Helsinki Design System
- [DateInput: acessibilidade](https://hds.hel.fi/components/date-input/accessibility) Helsinki Design System
- [Calendar](https://vercel.com/geist/calendar) Geist
- [DatePicker](https://blueprintjs.com/docs/#datetime/date-picker) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o seletor de horário em 24 horas, o calendário em português com domingo primeiro, o intervalo com dias anteriores bloqueados, a abertura com Enter e o fechamento com Esc, e a regra de formatos digitados. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                          |
