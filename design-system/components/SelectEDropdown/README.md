# SelectEDropdown

Um select mostra a opção escolhida e esconde as demais numa lista que abre sob demanda.

O Trama oferece o select nativo (`.tr-select`, sobre o elemento `<select>`) como padrão. O dropdown personalizado, com lista desenhada pelo produto, é reservado para opções com formatação própria e para a seleção múltipla em espaço reduzido. A HIG chama esse controle de pop-up button: um botão que abre um menu de opções mutuamente exclusivas e passa a exibir a escolhida ([Apple](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons)). O gov.br define dois tipos, select para escolha única e multiselect para várias, e trata a lista como um elemento flutuante que segue o padrão dropdown ([gov.br](https://www.gov.br/ds/components/select)). Quando a lista precisa de filtro por digitação, use o combobox.

**Quando usar.** Para escolher uma opção numa lista média, de 7 a 15 itens, ou quando falta espaço vertical para mostrar todas ([HDS](https://hds.hel.fi/components/select)). Também serve para ajustes de visualização, como ordenação e quantidade de itens por página.

**Quando não usar.**

- Duas opções: use radios, um switch ou um controle segmentado, que deixam a escolha direta na interface ([gov.br](https://www.gov.br/ds/padroes/design/dropdown)). Até cerca de cinco opções, com espaço, radios também são melhores ([HDS](https://hds.hel.fi/components/select)).
- Mais de 15 opções: use um combobox ([DKFDS](https://designsystem.dk/komponenter/dropdown/)).
- Várias escolhas numa lista curta: use checkboxes visíveis. O `<select multiple>` tem histórico de baixa usabilidade e pouco suporte de tecnologias assistivas ([GOV.UK](https://design-system.service.gov.uk/components/select/)).
- Ações ou navegação: use um menu. O select não pode conter links nem botões ([HDS](https://hds.hel.fi/components/select/accessibility)).
- Datas: use a entrada de data.

Em serviços para o público geral, trate o select como último recurso: pesquisas do GOV.UK mostram pessoas que não conseguem fechá-lo, tentam digitar nele, confundem a opção em foco com a selecionada e não percebem que podem rolar a lista ([GOV.UK](https://design-system.service.gov.uk/components/select/)). Antes de usá-lo, tente reformular a pergunta para reduzir as opções.

## Anatomia

1.  **Rótulo** (`.tr-label`): descreve o que há na lista.
2.  **Dica** e **mensagem** (opcionais), acima do controle, como nos demais campos.
3.  **Acionador** (`.tr-select` ou botão): mostra o valor atual ou o texto inicial. Toda a sua área abre a lista, incluindo o indicador ([gov.br](https://www.gov.br/ds/components/select)).
4.  **Indicador de estado**: seta para baixo com a lista fechada e para cima com ela aberta, no fim do acionador ([gov.br](https://www.gov.br/ds/padroes/design/dropdown)).
5.  **Lista**: no select nativo, desenhada pelo sistema. No personalizado, superfície `--t-surface-raised` com sombra `--e-4` na camada `--z-2`.
6.  **Selecionar todos** (só no múltiplo): primeiro item da lista, destacado.
7.  **Grupos** (opcionais): `<optgroup>` com título não selecionável.

## Tipos

| Tipo                   | Uso                                                                                                                                                                         |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select nativo          | Padrão em formulários. Acessível por natureza e adequado ao celular ([Fluent](https://fluent2.microsoft.design/components/web/react/core/select/usage)).                    |
| Dropdown personalizado | Opções com ícone ou descrição, ou filtros e ordenações da interface ([Fluent](https://fluent2.microsoft.design/components/web/react/core/dropdown/usage)).                  |
| Múltiplo               | Várias escolhas numa lista longa, quando não há espaço para checkboxes visíveis. Cada opção leva um checkbox ([gov.br](https://www.gov.br/ds/components/select)).           |
| Com grupos             | Listas acima de cerca de dez itens com categorias naturais ([Geist](https://vercel.com/geist/select)), cada grupo com título ([HDS](https://hds.hel.fi/components/select)). |

## Boas práticas

**Não pré-selecione respostas de perguntas.** Num formulário, comece sem opção escolhida para não influenciar a resposta; em ajustes, como ordenação, pré-selecione o padrão ([GOV.UK](https://design-system.service.gov.uk/components/select/)). Em perguntas, a primeira opção é um texto inicial com valor vazio, como “Selecione o estado”. Consentimentos nunca vêm marcados ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Ordene as opções de forma previsível.** Use ordem alfabética, numérica ou cronológica ([gov.br](https://www.gov.br/ds/components/select); [Apple](https://developer.apple.com/design/human-interface-guidelines/pickers)). Opções como “Nenhum” e “Outro” também entram na ordem alfabética, salvo quando ficam separadas no fim.

**Limite a altura da lista e a largura do acionador.** A lista mostra até dez opções no select e nove no múltiplo, contando o “Selecionar todos”; o restante fica na rolagem ([gov.br](https://www.gov.br/ds/components/select)). O acionador tem no mínimo 100px no select e 200px no múltiplo, e no máximo 400px; na classe Compacta, ocupa a largura toda ([gov.br](https://www.gov.br/ds/components/select)).

**Posicione a lista sem criar rolagem.** A lista abre abaixo do acionador e muda de direção perto da borda da tela, sem criar espaço extra nem barra de rolagem na página ([gov.br](https://www.gov.br/ds/padroes/design/dropdown)). Enquanto ela está aberta, o acionador mantém o estado pressionado. Feche com o próprio acionador, com Esc, com clique fora ou ao concluir a escolha ([gov.br](https://www.gov.br/ds/padroes/design/dropdown)).

**No múltiplo, ofereça “Selecionar todos” e resuma a seleção.** O primeiro item marca ou desmarca todas as opções, e o rótulo alterna entre “Selecionar todos” e “Desselecionar todos”. Com parte das opções marcadas, ele mostra o estado misto ([gov.br](https://www.gov.br/ds/components/select)). A lista fica aberta enquanto a pessoa marca ([Fluent](https://fluent2.microsoft.design/components/web/react/core/dropdown/usage)). Fechada, o acionador mostra o primeiro item e a quantidade restante: “Direito civil + (2)” ([gov.br](https://www.gov.br/ds/components/select)).

**Quebre a linha das opções e trunque só o resumo.** Opções longas quebram a linha dentro da lista, embora seja melhor evitá-las ([gov.br](https://www.gov.br/ds/components/select)). No acionador, o valor pode terminar em reticências se não couber, com o texto completo no nome acessível e num tooltip focável.

**Não dispare ações ao escolher.** A pessoa pode estar só percorrendo a lista com o teclado. Coloque um botão ao lado para aplicar a escolha ([DKFDS](https://designsystem.dk/komponenter/dropdown/)). A exceção é um ajuste de visualização sem perda de dados, aplicado após o fechamento da lista.

**Evite listas que mudam o conteúdo de outras listas.** Selects encadeados confundem muitas pessoas ([DKFDS](https://designsystem.dk/komponenter/dropdown/)). Quando for inevitável, como estado e cidade, use uma página por pergunta ou um combobox. Não aninhe mais de três níveis de elementos flutuantes ([gov.br](https://www.gov.br/ds/padroes/design/dropdown)).

**Faça** radios para poucas opções: tudo fica visível e comparável.

**Não faça** três opções escondidas num select, com a primeira já escolhida.

### Estados e teclado

| Estado         | Aparência                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------|
| Padrão e hover | Borda `--t-border-control`; no hover, `--t-fg-2`. Na lista, a opção sob o ponteiro recebe a camada `--o-hover` |
| Foco           | Anel `--t-focus` de 2px afastado 2px, em `:focus-visible`                                                      |
| Aberto         | `aria-expanded="true"`, indicador para cima e acionador em estado pressionado                                  |
| Selecionado    | Opção com marca e fundo `--t-brand-subtle`; no múltiplo, checkbox marcado                                      |
| Misto          | “Selecionar todos” com traço quando parte das opções está marcada                                              |
| Erro e sucesso | Borda de 2px `--t-danger` ou `--t-success` (`data-state="success"`), com a mensagem acima                      |
| Desabilitado   | Só quando a pessoa pode habilitá-lo por uma ação dela, com o motivo ao lado; caso contrário, retire o controle |

**Teclado no dropdown personalizado.** Tab leva ao acionador. Enter, Espaço ou Seta para baixo abrem a lista; a lista não abre só por receber foco. As setas movem o destaque, digitar uma letra leva à primeira opção que começa com ela, Home e End vão ao primeiro e ao último item ([HDS](https://hds.hel.fi/components/select)). Enter ou Espaço escolhem e fecham; no múltiplo, Espaço marca e a lista continua aberta. Esc fecha sem escolher e devolve o foco ao acionador ([gov.br](https://www.gov.br/ds/components/select)).

> **Divergência entre referências** *Seleção múltipla:* o gov.br oferece o multiselect como tipo regular; GOV.UK e HDS o desaconselham, e o GOV.UK cita histórico de baixa usabilidade e pouco suporte de tecnologias assistivas. Pelo critério de evidência, o Trama prefere checkboxes visíveis e usa o dropdown múltiplo só em listas longas sem espaço, seguindo as regras do gov.br. *Pré-seleção:* o gov.br sugere tornar padrão a opção mais escolhida; GOV.UK e DKFDS pré-selecionam só em ajustes. Por convergência, o Trama pré-seleciona só em ajustes. *Abertura ao receber foco:* a página de acessibilidade do gov.br abre a lista quando o select recebe foco; HDS e Fluent abrem por tecla. Pelo critério de acessibilidade, o Trama abre só por ação da pessoa, para que quem percorre a página com Tab não esbarre em listas abertas. *Resumo da seleção:* Fluent e Geist mostram só a quantidade; o gov.br mostra o primeiro item e a quantidade restante. Pelo critério de contexto brasileiro, o Trama segue o gov.br. *Filtro:* o select do gov.br filtra por digitação; no Trama, o filtro é o que define o combobox.

## Conteúdo

**Rótulo.** Uma palavra ou frase curta que diga o que há na lista: “Estado”, “Vínculo com a empresa” ([Fluent](https://fluent2.microsoft.design/components/web/react/core/select/usage)).

**Texto inicial.** Comece com o verbo e o objeto: “Selecione o estado”. Evite “Escolha um” ou a repetição do rótulo ([Geist](https://vercel.com/geist/select)). O texto inicial complementa o rótulo e nunca o substitui ([Fluent](https://fluent2.microsoft.design/components/web/react/core/dropdown/usage)).

**Opções.** Curtas e objetivas ([gov.br](https://www.gov.br/ds/components/select)), com construção paralela e sem repetir a mesma palavra no início de cada uma ([Fluent](https://fluent2.microsoft.design/components/web/react/core/select/usage)). Caixa de frase, exceto nomes próprios.

**Lista vazia.** Quando não há opções disponíveis, diga isso no lugar da lista e como resolver: “Nenhum município disponível para este estado”. Não use “Ops”.

**Erro.** Diga o que fazer: “Selecione seu vínculo com a empresa”, quando a pessoa enviar sem escolher ([GOV.UK](https://design-system.service.gov.uk/components/select/)).

## Acessibilidade

- Prefira o `<select>` nativo: ele já tem papel, estado e teclado corretos. Associe-o a um `<label>`; sem rótulo visível, use `aria-label` ([gov.br](https://www.gov.br/ds/components/select)).
- Marque o obrigatório com `required` e ligue dica e mensagem com `aria-describedby` ([gov.br](https://www.gov.br/ds/components/select)).
- No personalizado de escolha única, use o padrão de combobox somente leitura: acionador com `role="combobox"`, `aria-expanded` e `aria-controls`, lista com `role="listbox"` e opções com `aria-selected`. No múltiplo, use um botão com `aria-expanded` que revela um `<fieldset>` de checkboxes.
- O nome acessível do acionador múltiplo lista todas as escolhas, não só o resumo visível.
- Diferencie a opção em foco da selecionada com marca, além de cor, porque as pessoas confundem os dois estados ([GOV.UK](https://design-system.service.gov.uk/components/select/)).
- Se a lista personalizada usar um véu para dar contraste, bloqueie mouse e teclado no conteúdo por baixo ([gov.br](https://www.gov.br/ds/padroes/design/dropdown)).

## Tokens usados

| Elemento            | Token                                              |
|---------------------|----------------------------------------------------|
| Altura do acionador | `--d-control`: 32, 40 ou 48px conforme a densidade |
| Borda e raio        | `--stroke-thin`, `--t-border-control`, `--r-md`    |
| Lista personalizada | `--t-surface-raised`, `--e-4`, `--z-2`, `--r-lg`   |
| Altura da opção     | `--d-row` (56px na padrão)                         |
| Hover da opção      | Camada `--o-hover`                                 |
| Opção selecionada   | `--t-brand-subtle` com marca em `--t-brand`        |
| Estados             | `--t-danger`, `--t-success`, `--stroke-thick`      |
| Abertura da lista   | `--m-fast`, `--m-ease-enter`                       |

## Considerações por plataforma

### Web desktop

A lista abre logo abaixo do acionador e não fica mais estreita que ele. Permita digitar letras com o select fechado para pular até a opção. Em barras de ferramentas e cabeçalhos de tabela, use densidade alta.

### Web móvel

O select nativo abre o seletor do sistema, familiar e acessível; por isso o Trama não o troca por listas personalizadas em formulários móveis ([Fluent](https://fluent2.microsoft.design/components/web/react/core/dropdown/usage)). Na classe Compacta, acionador e lista personalizada ocupam a largura toda, com densidade baixa ([gov.br](https://www.gov.br/ds/padroes/design/dropdown)). Algumas pessoas tentam ampliar as opções com pinça em telas pequenas ([GOV.UK](https://design-system.service.gov.uk/components/select/)): mantenha as opções curtas.

### Tablets e dobráveis

Em tablets, o sistema pode exibir a lista como popover ancorado ao campo. Em toque, use densidade baixa mesmo em janelas Expandidas. Em dobráveis abertos, garanta que a lista personalizada não atravesse a dobra.

## Recursos

### Relacionados

- Radio
- Combobox
- Checkbox
- Menus
- Controle segmentado
- Densidade

### Referências

- [Select](https://www.gov.br/ds/components/select) gov.br DS
- [Dropdown](https://www.gov.br/ds/padroes/design/dropdown) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons) Apple HIG
- [Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) Apple HIG
- [Select](https://design-system.service.gov.uk/components/select/) GOV.UK Design System
- [Dropdown](https://designsystem.dk/komponenter/dropdown/) Det Fælles Designsystem
- [Select](https://hds.hel.fi/components/select) Helsinki Design System
- [Select: acessibilidade](https://hds.hel.fi/components/select/accessibility) Helsinki Design System
- [Select](https://fluent2.microsoft.design/components/web/react/core/select/usage) Fluent 2
- [Dropdown](https://fluent2.microsoft.design/components/web/react/core/dropdown/usage) Fluent 2
- [Select](https://vercel.com/geist/select) Geist

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o dropdown múltiplo com “Selecionar todos” e resumo “primeiro item + (n)”, limites de opções visíveis e de largura, posicionamento e fechamento da lista, estados aberto, misto e sucesso, e a mensagem de lista vazia. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                      |
