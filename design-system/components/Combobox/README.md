# Combobox

Um combobox combina um campo de texto com uma lista de opções que se filtra enquanto a pessoa digita.

A HIG define o combo box como um campo de texto unido a um botão que abre uma lista de valores predefinidos; a pessoa pode digitar um valor próprio ou escolher da lista ([Apple](https://developer.apple.com/design/human-interface-guidelines/combo-boxes)). No Trama, o combobox é o controle para listas longas: em vez de rolar centenas de opções, a pessoa digita algumas letras e escolhe entre as que restam. O gov.br trata o mesmo comportamento como o filtro do select e como o autocompletar do campo de entrada, com sugestões carregadas numa lista enquanto a pessoa digita ([gov.br](https://www.gov.br/ds/components/select); [gov.br](https://www.gov.br/ds/components/input)).

**Quando usar.**

- Listas longas, acima de 15 opções, como países, municípios, órgãos ou classificações ([DKFDS](https://designsystem.dk/komponenter/dropdown/); [HDS](https://hds.hel.fi/components/select)).
- Quando a pessoa já sabe o que procura e digitar é mais rápido que percorrer a lista ([Geist](https://vercel.com/geist/combobox)).
- Quando, além das opções sugeridas, a resposta livre é aceita ([Fluent](https://fluent2.microsoft.design/components/web/react/core/combobox/usage)).

**Quando não usar.** Para listas curtas e fixas, use select ou radios ([Geist](https://vercel.com/geist/combobox)). Para termos que não resultam numa única opção, use o campo de pesquisa ([Geist](https://vercel.com/geist/combobox)). Para ações e comandos, use um menu.

## Anatomia

1.  **Rótulo** (`.tr-label`) e **dica** (`.tr-hint`, opcional).
2.  **Campo** (`.tr-input`): recebe o texto digitado e mostra o valor escolhido.
3.  **Ícone de pesquisa** (opcional): ilustrativo, no início do campo; pode ser retirado quando falta espaço ([gov.br](https://www.gov.br/ds/components/select)).
4.  **Botão de abrir** (opcional): ação interna no fim do campo que abre a lista completa sem digitar, com seta para baixo ou para cima conforme o estado ([gov.br](https://www.gov.br/ds/components/select)).
5.  **Botão de limpar** (opcional): aparece quando há valor ([Geist](https://vercel.com/geist/combobox)).
6.  **Lista de opções**: superfície `--t-surface-raised`, sombra `--e-4`, camada `--z-2`, com o trecho digitado destacado em `.tr-mark`.
7.  **Mensagem de lista vazia** e **carregamento**, no lugar da lista.
8.  **Seleções** (múltiplo): chips fora da lista, com botão de remover.

## Tipos

| Tipo       | Comportamento                                                                                                                                                                                                                                                                                      |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Restrito   | Aceita só valores da lista; o texto digitado serve para filtrar. Padrão do Trama.                                                                                                                                                                                                                  |
| Livre      | Aceita também um valor fora da lista ([Fluent](https://fluent2.microsoft.design/components/web/react/core/combobox/usage)), que não entra na lista de opções ([Apple](https://developer.apple.com/design/human-interface-guidelines/combo-boxes)).                                                 |
| Múltiplo   | Cada opção tem um checkbox; a lista fica aberta até a pessoa clicar fora ou pressionar Esc ([Fluent](https://fluent2.microsoft.design/components/web/react/core/combobox/usage)). Pode começar com “Selecionar todos”, como o select múltiplo ([gov.br](https://www.gov.br/ds/components/select)). |
| Assíncrono | Consulta opções no servidor a cada termo e mostra carregamento sem fechar a lista ([Geist](https://vercel.com/geist/combobox); [gov.br](https://www.gov.br/ds/components/input)).                                                                                                                  |

## Boas práticas

**Atualize as sugestões na hora.** Os resultados mudam enquanto a pessoa digita, de preferência sem espera. Se houver espera, mostre um indicador de carregamento na lista ([gov.br](https://www.gov.br/ds/components/input)).

**Ordene os resultados em ordem alfabética.** A ordem previsível ajuda a achar o item ([gov.br](https://www.gov.br/ds/components/input)). Coloque primeiro os valores mais prováveis só quando houver dados de uso que justifiquem ([Apple](https://developer.apple.com/design/human-interface-guidelines/combo-boxes)).

**Filtre por qualquer parte do texto e ignore acentos e maiúsculas.** Quem digita “sao” encontra “São Paulo”. Considere espaços parte do filtro, para que opções com várias palavras funcionem ([Fluent](https://fluent2.microsoft.design/components/web/react/core/combobox/usage)).

**Mostre até dez opções por vez.** O restante fica na rolagem interna da lista ([gov.br](https://www.gov.br/ds/components/select)). A lista abre abaixo do campo e vira para cima perto da borda da tela, sem criar rolagem na página ([gov.br](https://www.gov.br/ds/padroes/design/dropdown)).

**Quebre a linha em vez de cortar opções longas.** Opções mais largas que o campo ficam difíceis de ler ([Apple](https://developer.apple.com/design/human-interface-guidelines/combo-boxes)). Se a opção precisa de duas linhas, como nome e estado, permita altura variável ([Geist](https://vercel.com/geist/combobox)).

**Mostre as seleções fora da lista.** No múltiplo, as escolhas aparecem como chips para que a pessoa as veja sem reabrir a lista ([Fluent](https://fluent2.microsoft.design/components/web/react/core/combobox/usage)). Ofereça remover cada uma e, quando forem muitas, remover todas ([HDS](https://hds.hel.fi/components/select)).

**Escreva a lista vazia com o termo digitado e uma saída.** Use “Nenhum país corresponde a ‘Arg’” em vez de “Sem resultados” ([Geist](https://vercel.com/geist/combobox)). Quando houver, sugira assuntos relacionados ao termo ([gov.br](https://www.gov.br/ds/components/input)). No combobox livre, ofereça usar o texto digitado.

**Não envie o formulário com Enter enquanto a lista estiver aberta.** Com a lista aberta, Enter escolhe a opção em destaque ([Geist](https://vercel.com/geist/combobox)).

**Ao sair do campo com texto sem correspondência, decida de forma explícita.** No restrito, mantenha o texto e mostre erro ao validar; não apague o que a pessoa digitou. No livre, aceite o texto como valor.

**Faça** combobox para centenas de municípios: a pessoa digita e escolhe.

**Não faça** combobox para duas opções: use radios.

### Estados e teclado

| Ação            | Resultado                                                                    |
|-----------------|------------------------------------------------------------------------------|
| Digitar         | Abre a lista e filtra as opções                                              |
| Seta para baixo | Abre a lista ou move o destaque para a próxima opção                         |
| Seta para cima  | Move o destaque para a opção anterior                                        |
| Enter           | Escolhe a opção em destaque e fecha (no múltiplo, marca e mantém aberta)     |
| Esc             | Fecha a lista sem escolher; um segundo Esc limpa o campo                     |
| Tab             | Fecha a lista e segue para as ações internas e, depois, para o próximo campo |

Os estados visuais do campo (hover, foco, erro, sucesso, alerta e desabilitado) e as densidades são os mesmos do campo de texto. A opção sob o ponteiro recebe a camada `--o-hover`; a opção em destaque pelo teclado, fundo `--t-surface-2`; a selecionada, fundo `--t-brand-subtle` e marca de seleção. Um único destaque por vez: a última interação da pessoa, de teclado ou de ponteiro, define qual.

> **Divergência entre referências** *Ordem das sugestões:* a HIG pede listar os valores mais prováveis; o gov.br pede ordem alfabética. Não há evidência citada nem diferença de acessibilidade; por convergência com GOV.UK, que também usa a ordem alfabética como padrão em listas de opções, o Trama ordena em ordem alfabética e só prioriza por uso com dados. *Resumo da seleção múltipla:* o Geist mostra a contagem (“3 áreas selecionadas”); o gov.br mostra o primeiro item e a quantidade restante. O Trama segue o gov.br, como no select. *Altura da lista:* a versão 1.0 limitava a cerca de oito opções; o Trama adota as dez do gov.br.

## Conteúdo

**Rótulo.** Curto e descritivo, dizendo o que há na lista ([Fluent](https://fluent2.microsoft.design/components/web/react/core/combobox/usage)). Em listas grandes, explique na dica que é possível digitar para filtrar.

**Placeholder.** Em formulários, não use. Em filtros fora de formulário, ele pode nomear o escopo, como “Pesquisar municípios”, nunca só “Pesquisar” e nunca repetindo o rótulo ([Geist](https://vercel.com/geist/combobox)). Sem itálico.

**Opções.** Paralelas, em caixa de frase e sem repetir a mesma palavra no início ([Fluent](https://fluent2.microsoft.design/components/web/react/core/combobox/usage)). Respeite a grafia oficial de nomes próprios.

**Resumo da seleção múltipla.** Quando o campo precisa resumir as escolhas, mostre o primeiro item e a quantidade restante: “Direito civil + (2)” ([gov.br](https://www.gov.br/ds/components/select)).

**Carregamento e erro.** “Carregando municípios”. Erro: “Escolha um país da lista”. Sem “Ops” e sem humor.

## Acessibilidade

- Use o padrão ARIA de combobox: campo com `role="combobox"`, `aria-expanded`, `aria-controls` e `aria-autocomplete="list"`; lista com `role="listbox"`; destaque comunicado por `aria-activedescendant`, com o foco real no campo.
- Associe um rótulo visível com `<label for>`. O placeholder não substitui o nome acessível ([Geist](https://vercel.com/geist/multi-select)).
- Anuncie o número de resultados numa região `aria-live="polite"`, como “4 resultados” ([Geist](https://vercel.com/geist/command-menu)), e anuncie também o carregamento e a lista vazia.
- As ações internas, como abrir e limpar, recebem foco com Tab depois do campo e são acionadas com Espaço ou Enter ([gov.br](https://www.gov.br/ds/components/input)).
- Coloque a lista logo após o campo no DOM. O Safari não suporta `aria-owns`, e a ordem do DOM permite navegar por gesto no iOS ([Fluent](https://fluent2.microsoft.design/components/web/react/core/combobox/usage)).
- No múltiplo, nomeie cada checkbox com o item e cada botão de remover chip com “Remover” mais o item ([Geist](https://vercel.com/geist/multi-select)).
- O destaque do trecho digitado não pode ser o único sinal da correspondência; o texto completo continua legível com contraste de 4,5:1 (WCAG 2.2, 1.4.3).

## Tokens usados

| Elemento              | Token                                                                |
|-----------------------|----------------------------------------------------------------------|
| Campo                 | Tokens de `.tr-input`: `--d-control`, `--t-border-control`, `--r-md` |
| Lista                 | `--t-surface-raised`, `--e-4`, `--z-2`, `--r-lg`                     |
| Opção                 | Altura mínima `--d-row`; em toque, nunca menos que `--c-touch`       |
| Hover e destaque      | Camada `--o-hover`; destaque de teclado `--t-surface-2`              |
| Trecho correspondente | `.tr-mark`: `--t-mark`, `--t-mark-fg`                                |
| Selecionada           | `--t-brand-subtle`, marca em `--t-brand`                             |
| Chips de seleção      | `.tr-chip`, intervalo `--sp-200`                                     |
| Abertura              | `--m-fast`, `--m-ease-enter`                                         |

## Considerações por plataforma

### Web desktop

A lista abre abaixo do campo, com a mesma largura ou mais. Em interfaces densas, com mouse, campo e opções podem usar densidade alta. Um atalho de teclado pode focar o combobox de filtro, mas nunca reutilize o atalho global da paleta de comandos ([Geist](https://vercel.com/geist/command-menu)).

### Web móvel

Na classe Compacta, campo e lista ocupam a largura toda ([gov.br](https://www.gov.br/ds/padroes/design/dropdown)), com densidade baixa. Com o teclado virtual aberto, sobra pouco espaço: role o campo até o topo da área visível ao receber foco. Dentro de diálogos, abra a pesquisa numa folha de tela cheia, como faz o Geist no celular ([Geist](https://vercel.com/geist/combobox)).

### Tablets e dobráveis

Em janelas expandidas, a lista pode abrir como popover ancorado. Num dobrável aberto, posicione a lista no mesmo painel do campo, sem cruzar a dobra.

## Recursos

### Relacionados

- Select e dropdown
- Campos de texto
- Campo de pesquisa
- Tags e chips
- Pesquisa

### Referências

- [Input (autocomplete)](https://www.gov.br/ds/components/input) gov.br DS
- [Select](https://www.gov.br/ds/components/select) gov.br DS
- [Dropdown](https://www.gov.br/ds/padroes/design/dropdown) gov.br DS
- [Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes) Apple HIG
- [Combobox](https://fluent2.microsoft.design/components/web/react/core/combobox/usage) Fluent 2
- [Combobox](https://vercel.com/geist/combobox) Geist
- [Multi Select](https://vercel.com/geist/multi-select) Geist
- [Command Menu](https://vercel.com/geist/command-menu) Geist
- [Select](https://hds.hel.fi/components/select) Helsinki Design System
- [Dropdown](https://designsystem.dk/komponenter/dropdown/) Det Fælles Designsystem
- [Radios](https://design-system.service.gov.uk/components/radios/) GOV.UK Design System
- [Suggest](https://blueprintjs.com/docs/#select/suggest) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                     |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta ordem alfabética das sugestões, até dez opções visíveis, carregamento, sugestões relacionadas na lista vazia, resumo “primeiro item + (n)”, densidades e ordem de tabulação das ações internas. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                              |
