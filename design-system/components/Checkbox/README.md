# Checkbox

Um checkbox permite marcar uma ou mais opções independentes numa lista visível, ou confirmar uma única afirmação.

O checkbox do Trama (`.tr-check`) é uma caixa quadrada à esquerda do texto: vazia quando desmarcada, preenchida com `--t-brand` e marca de seleção quando marcada. Um checkbox também pode ter estado misto, mostrado com um traço, quando controla um grupo com estados diferentes ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)). O gov.br chama esse controle de caixa de seleção e o compõe com cabeçalho de opções, lista de opções e uma mensagem para o conjunto ([gov.br](https://www.gov.br/ds/components/checkbox)).

**Quando usar.**

- Para escolher várias opções numa lista ([GOV.UK](https://design-system.service.gov.uk/components/checkboxes/)), quando a pessoa precisa ver todas as escolhas de uma vez ([DKFDS](https://designsystem.dk/komponenter/tjekboks/)).
- Para uma única opção de sim ou não que só vale após o envio, como “Lembrar meu acesso neste computador” ([gov.br](https://www.gov.br/ds/components/checkbox); [Fluent](https://fluent2.microsoft.design/components/web/react/core/checkbox/usage)).
- Para confirmar uma declaração, como aceitar termos de uso ([Geist](https://vercel.com/geist/checkbox)).
- Para selecionar linhas numa tabela ou itens numa lista, inclusive sem texto visível ([gov.br](https://www.gov.br/ds/components/checkbox)).

**Quando não usar.** Se só uma opção pode ser escolhida, use radios ([GOV.UK](https://design-system.service.gov.uk/components/checkboxes/)). Se a mudança vale na hora, sem botão de enviar, use um switch ([Fluent](https://fluent2.microsoft.design/components/web/react/core/checkbox/usage)). Se a lista for muito extensa, use um combobox múltiplo ou um select múltiplo ([gov.br](https://www.gov.br/ds/components/checkbox)).

## Anatomia

1.  **Legenda do grupo** (`<legend>` em `.tr-fieldset`): a pergunta ou o nome do conjunto, no topo, alinhada à esquerda ([gov.br](https://www.gov.br/ds/components/checkbox)).
2.  **Dica do grupo** (`.tr-hint`, opcional): logo abaixo da legenda, por exemplo quantas opções escolher.
3.  **Mensagem do grupo** (condicional): uma só para todo o conjunto ([gov.br](https://www.gov.br/ds/components/checkbox)), abaixo da legenda e da dica.
4.  **Caixa**: 20 por 20px, borda de 2px `--t-border-control`, raio `--r-md`.
5.  **Texto da opção**: Body 16/24, à direita da caixa. Toda a linha é clicável.
6.  **Dica da opção** (opcional) e **conteúdo condicional** (opcional): uma pergunta que aparece quando a opção é marcada.

## Tipos

| Tipo                       | Uso                                                                                                                                                                                         |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Grupo                      | Várias opções relacionadas, dentro de `<fieldset>`                                                                                                                                          |
| Único                      | Uma afirmação de sim ou não, ou um aceite                                                                                                                                                   |
| Principal com estado misto | Checkbox que marca e desmarca um conjunto de itens vinculados, que podem ser checkboxes, switches, itens de lista ou linhas de tabela ([gov.br](https://www.gov.br/ds/components/checkbox)) |
| Em cadeia                  | Um item vinculado que também é principal de outro conjunto ([gov.br](https://www.gov.br/ds/utilitarios/js/checkgroup))                                                                      |
| Sem texto visível          | Seleção de linha em tabela, com `aria-label`, mantendo alinhamento e espaçamento ([gov.br](https://www.gov.br/ds/components/checkbox))                                                      |

## Boas práticas

**Posicione a caixa à esquerda do texto e empilhe as opções.** Isso facilita encontrar a caixa, principalmente com ampliador de tela ([GOV.UK](https://design-system.service.gov.uk/components/checkboxes/)). Prefira uma coluna; use duas só em caso de real necessidade, com a mesma largura nos itens da coluna e a mesma altura nos itens da linha ([gov.br](https://www.gov.br/ds/components/checkbox)).

**Não pré-marque opções em perguntas.** Uma resposta já marcada aumenta a chance de a pessoa não perceber a pergunta ou enviar a resposta errada ([GOV.UK](https://design-system.service.gov.uk/components/checkboxes/)). Consentimentos sempre começam desmarcados, um por finalidade ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Diga que é possível marcar várias.** Antes da lista, use legenda e uma breve descrição: “Selecione todas as opções que se aplicam” ([gov.br](https://www.gov.br/ds/components/checkbox); [GOV.UK](https://design-system.service.gov.uk/components/checkboxes/)).

**Ordene as opções.** Por padrão, em ordem alfabética; quando houver dados, da mais comum para a menos comum ([GOV.UK](https://design-system.service.gov.uk/components/checkboxes/)). Siga a ordem natural quando ela existir, como Segunda, Terça, Quarta, para que a ordem de tabulação também faça sentido ([gov.br](https://www.gov.br/ds/components/checkbox)). Com mais de cerca de sete opções, divida em grupos ou use um combobox ([Fluent](https://fluent2.microsoft.design/components/web/react/core/checkbox/usage)).

**Ofereça “nenhuma” quando for resposta válida.** Coloque-a por último, separada por um divisor com a palavra “ou”, e repita a parte principal da pergunta: “Não vou viajar para nenhum destes países” ([GOV.UK](https://design-system.service.gov.uk/components/checkboxes/)). Ao marcar “nenhuma”, desmarque as outras.

**Mantenha os checkboxes independentes e sem efeito imediato.** Marcar um não altera os outros, exceto no checkbox principal e na opção “nenhuma”, e a escolha vale ao enviar o formulário ([HDS](https://hds.hel.fi/components/checkbox)).

**Siga o ciclo do checkbox principal.** Desmarcado, ao ser clicado, marca todos os itens vinculados. Marcado, desmarca todos. Com parte dos itens marcada, mostra o estado misto e, ao ser clicado, marca todos ([gov.br](https://www.gov.br/ds/components/checkbox)). Seu rótulo pode alternar entre “Selecionar todas” e “Desselecionar todas” ([gov.br](https://www.gov.br/ds/utilitarios/js/checkgroup)). Recue os itens vinculados com `--sp-800` ([Fluent](https://fluent2.microsoft.design/components/web/react/core/checkbox/usage)) e, se ajudar, informe a contagem ao lado: “3 de 5 selecionados” ([Geist](https://vercel.com/geist/checkbox)).

**Use a cadeia com moderação.** Um item vinculado pode ser principal de outro conjunto, e o estado se propaga nos dois sentidos ([gov.br](https://www.gov.br/ds/utilitarios/js/checkgroup)). Limite a um nível de subgrupo dentro de cada grupo ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Revele só perguntas simples.** Ao marcar “Ligação telefônica”, pode aparecer o campo de telefone. Não esconda textos explicativos ou imagens dessa forma ([DKFDS](https://designsystem.dk/komponenter/tjekboks/)), e leve perguntas complexas para a próxima página ([GOV.UK](https://design-system.service.gov.uk/components/checkboxes/)).

**Faça** texto afirmativo: marcar significa sim.

**Não faça** negativa: a pessoa precisa decifrar o que acontece ao marcar.

### Estados

| Estado       | Aparência e uso                                                                                                                                                       |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Desmarcado   | Borda de 2px `--t-border-control`, fundo `--t-surface-raised`                                                                                                         |
| Hover        | Camada `--o-hover` em volta da caixa; só com ponteiro ([gov.br](https://www.gov.br/ds/components/checkbox))                                                           |
| Marcado      | Fundo e borda `--t-brand`, marca em `--t-on-brand`. Aciona com Espaço, clique ou toque na caixa ou no texto ([gov.br](https://www.gov.br/ds/components/checkbox))     |
| Misto        | Fundo `--t-brand` com traço horizontal                                                                                                                                |
| Foco         | Anel de 2px `--t-focus` em volta da caixa, em `:focus-visible`                                                                                                        |
| Inválido     | Mensagem `.tr-error-msg` no grupo, quando a escolha é obrigatória ou incorreta                                                                                        |
| Válido       | Mensagem `.tr-field-msg--success` no grupo, quando a resposta foi conferida, como num questionário com correção ([gov.br](https://www.gov.br/ds/components/checkbox)) |
| Desabilitado | Texto `--t-fg-disabled`, borda `--t-border-subtle`. Só quando a pessoa pode habilitar a opção por uma ação dela, com o motivo ao lado; caso contrário, retire a opção |

Em aceites obrigatórios, valide só no envio, para que marcar e desmarcar não pisque um erro ([Geist](https://vercel.com/geist/checkbox)).

> **Divergência entre referências** *Tamanho do texto da opção:* a HDS sugere até três palavras; o gov.br aceita até sete palavras no texto da opção e evita linhas com mais de 10 palavras ou 56 caracteres em média. Pelo critério de contexto brasileiro (textos em português são mais longos), o Trama segue o gov.br. *Posição da mensagem:* o gov.br põe a mensagem abaixo do último item; o GOV.UK, abaixo da legenda. O Trama a mantém abaixo da legenda, coerente com os campos de texto. Todos concordam em uma só mensagem por grupo. *Tamanho da caixa:* o gov.br usa 24px com borda de 1px; o Trama mantém 20px com borda de 2px, porque a área de ação é a linha inteira, com altura `--c-touch`.

## Conteúdo

**Legenda.** Normalmente uma pergunta ou um verbo no imperativo: “Como podemos entrar em contato?”, “Selecione os estados do projeto” ([gov.br](https://www.gov.br/ds/components/checkbox)). Coloque na legenda as palavras que se repetiriam em todas as opções ([Fluent](https://fluent2.microsoft.design/components/web/react/core/checkbox/usage)).

**Opções.** Até sete palavras, em caixa de frase, sem caixa alta e sem ponto final ([gov.br](https://www.gov.br/ds/components/checkbox)). Mantenha a linha abaixo de 10 palavras ou 56 caracteres; se passar, quebre a linha alinhada ao texto ([gov.br](https://www.gov.br/ds/components/checkbox)). Use linguagem afirmativa ([DKFDS](https://designsystem.dk/komponenter/tjekboks/)) e estrutura paralela.

**Aceites.** Frase completa, com ponto final: “Li e aceito os termos de uso.” ([Geist](https://vercel.com/geist/checkbox)).

**Mensagens.** Sucintas, de preferência numa linha ([gov.br](https://www.gov.br/ds/components/checkbox)), sem culpar a pessoa.

| Situação                          | Modelo                                                                                 |
|-----------------------------------|----------------------------------------------------------------------------------------|
| Nada marcado, pergunta com opções | Selecione se você é brasileiro, português ou de outra nacionalidade                    |
| Nada marcado, pergunta aberta     | Selecione sua nacionalidade ou nacionalidades                                          |
| “Nenhuma” e outra opção marcadas  | Selecione os países para onde vai viajar ou “Não vou viajar para nenhum destes países” |
| Aceite não marcado                | Aceite os termos de uso para continuar                                                 |

Os três primeiros modelos seguem a estrutura do GOV.UK ([GOV.UK](https://design-system.service.gov.uk/components/checkboxes/)).

## Acessibilidade

- Agrupe checkboxes relacionados num `<fieldset>` com `<legend>`, para que o leitor de tela anuncie o nome do grupo ([gov.br](https://www.gov.br/ds/components/checkbox)).
- Use `<input type="checkbox">` dentro de `<label>`, como faz o `.tr-check`. Sem input nativo, use `aria-checked` com `true`, `false` ou `mixed` ([gov.br](https://www.gov.br/ds/components/checkbox)).
- Tab chega a cada checkbox e Espaço marca ou desmarca. A mudança de estado é anunciada pelo leitor de tela ([gov.br](https://www.gov.br/ds/components/checkbox)).
- No checkbox principal, defina o estado misto pela propriedade `indeterminate`, que só existe em JavaScript ([HDS](https://hds.hel.fi/components/checkbox)), e use `aria-controls` com os ids dos itens vinculados ([HDS](https://hds.hel.fi/components/checkbox)).
- Na seleção de linhas de tabela, dê a cada checkbox um `aria-label` com o nome da linha: “Selecionar contrato 2026-114” ([Geist](https://vercel.com/geist/checkbox)).
- Diferencie os estados por forma (marca, traço), além da cor ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)). A borda `--t-border-control` atende a 3:1 (WCAG 2.2, 1.4.11).
- O conteúdo revelado nem sempre é anunciado pelos leitores de tela, o que falha o WCAG 2.2, 4.1.2. Mantenha-o simples ([GOV.UK](https://design-system.service.gov.uk/components/checkboxes/)).

## Tokens usados

| Elemento                   | Token                                                                      |
|----------------------------|----------------------------------------------------------------------------|
| Borda e raio da caixa      | `--stroke-thick`, `--t-border-control`, `--r-md`                           |
| Marcado e misto            | `--t-brand`, `--t-on-brand`                                                |
| Hover                      | `--o-hover`                                                                |
| Espaço entre caixa e texto | `--sp-300`                                                                 |
| Altura mínima da linha     | `--c-touch`; com mouse, em tabelas densas, área de ação de pelo menos 24px |
| Recuo de itens vinculados  | `--sp-800`                                                                 |
| Mensagens                  | `--t-danger`, `--t-success`                                                |
| Desabilitado               | `--t-fg-disabled`, `--t-border-subtle`                                     |
| Foco                       | `--t-focus`                                                                |

## Considerações por plataforma

### Web desktop

Em tabelas, permita marcar um intervalo com Shift e clique, e use o checkbox do cabeçalho como principal com estado misto ([gov.br](https://www.gov.br/ds/components/checkbox)). Não use checkboxes em barras de ferramentas; a HIG os reserva ao corpo da janela ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)).

### Web móvel

Garanta espaço em volta de cada checkbox para o toque ([DKFDS](https://designsystem.dk/komponenter/tjekboks/)); a linha inteira, com altura `--c-touch`, é a área de toque. Na classe Compacta, use sempre uma coluna. Evite grupos tão longos que não caibam bem na tela.

### Tablets e dobráveis

Em telas expandidas, grupos curtos podem ficar em duas colunas, desde que a ordem de leitura siga de cima para baixo em cada coluna. Num dobrável aberto, não divida um mesmo grupo entre os dois painéis.

## Recursos

### Relacionados

- Radio
- Switch
- Combobox
- Tabelas
- Validação e mensagens de erro

### Referências

- [Checkbox](https://www.gov.br/ds/components/checkbox) gov.br DS
- [Checkgroup](https://www.gov.br/ds/utilitarios/js/checkgroup) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles) Apple HIG
- [Checkboxes](https://design-system.service.gov.uk/components/checkboxes/) GOV.UK Design System
- [Tjekboks](https://designsystem.dk/komponenter/tjekboks/) Det Fælles Designsystem
- [Checkbox](https://hds.hel.fi/components/checkbox) Helsinki Design System
- [Checkbox](https://fluent2.microsoft.design/components/web/react/core/checkbox/usage) Fluent 2
- [Checkbox](https://vercel.com/geist/checkbox) Geist

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                     |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o ciclo do checkbox principal, a cadeia de grupos, o estado válido, uma mensagem por grupo, limites de texto do gov.br e a ordem de tabulação, e retira a opção desabilitada sem ação possível. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                              |
