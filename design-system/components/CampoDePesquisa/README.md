# CampoDePesquisa

O campo de pesquisa recebe os termos que a pessoa digita para encontrar conteúdo numa coleção.

O campo de pesquisa é um campo de texto editável com ícone de lupa, botão de limpar e texto de exemplo ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)). No gov.br, ele é uma aplicação do componente input, que prevê a requisição de pesquisa por palavra-chave, um tipo destaque para chamar atenção e o recurso de autocompletar ([gov.br DS](https://www.gov.br/ds/components/input)). É o componente da navegação direta, que leva a qualquer ponto da hierarquia ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). No Trama, há duas formas: o `.tr-search`, cápsula de altura `--c-h-md` para cabeçalhos e filtros, e o campo destaque, `.tr-input--feature`. Para resultados e filtros, veja o padrão Pesquisa.

**Quando usar.** Quando a pessoa conhece os termos ou não encontra o conteúdo pela navegação; a pesquisa também é alternativa para quem não consegue usar os menus ([DKFDS](https://designsystem.dk/komponenter/search/)). Também para filtrar uma lista longa ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)).

**Quando não usar.** Em soluções muito pequenas ([DKFDS](https://designsystem.dk/komponenter/search/)). Para escolher um valor de uma lista conhecida num formulário, use select ou combobox ([HDS](https://hds.hel.fi/components/search)).

## Anatomia

1.  **Rótulo**: visível acima do campo, ou oculto com `.tr-visually-hidden` quando a pesquisa fica no cabeçalho.
2.  **Campo**: `input type="search"` com texto de exemplo.
3.  **Ícone de lupa**: decorativo, à esquerda, com `aria-hidden="true"` ([gov.br DS](https://www.gov.br/ds/components/input)).
4.  **Ações internas**: botão circular de limpar, que aparece só quando há texto ([Fluent](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage)), e, no campo destaque, o botão Pesquisar (`.tr-input-action`) ([gov.br DS](https://www.gov.br/ds/components/input)).
5.  **Botão Pesquisar externo** (alternativa): botão de envio ao lado do campo ([DKFDS](https://designsystem.dk/komponenter/search/)).
6.  **Lista de sugestões** (opcional): superfície flutuante abaixo do campo.

## Tipos

| Tipo                | Uso                                                                                                                                                                                                                                                  |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Destaque            | `.tr-input--feature` (48px, texto de 18px, raio `--r-lg`): pesquisa principal de páginas iniciais e portais, ocupando grande espaço ([gov.br DS](https://www.gov.br/ds/components/input)).                                                           |
| Pesquisa do serviço | No cabeçalho, pesquisa em todo o produto. Texto de exemplo “Pesquisar em \[nome do serviço\]” ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)).                                                                         |
| Expansível          | Nas classes Compacta e Média, um botão circular de lupa no cabeçalho que abre o campo em largura total ([gov.br DS](https://www.gov.br/ds/components/header), [Fluent](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage)). |
| Filtro em linha     | Acima da lista que filtra, para deixar claro que vale só para ela ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)).                                                                                              |
| Com sugestões       | Mostra sugestões enquanto a pessoa digita e pesquisas recentes ao receber foco ([gov.br DS](https://www.gov.br/ds/components/input), [HDS](https://hds.hel.fi/components/search)).                                                                   |

## Boas práticas

**Deixe o campo largo.** A maioria das pesquisas tem duas ou mais palavras; o DKFDS recomenda pelo menos 27 caracteres (`27ch`) ([DKFDS](https://designsystem.dk/komponenter/search/)), e o gov.br pede campos do tamanho aproximado da entrada esperada ([gov.br DS](https://www.gov.br/ds/components/input)). O Trama adota o mínimo de `27ch`.

**Mostre o campo inteiro onde ele importa.** Na página inicial, use o campo destaque, pronto para digitar. Mantenha o campo, com os termos, na página de resultados ([DKFDS](https://designsystem.dk/komponenter/search/)).

**Posicione onde as pessoas esperam.** No cabeçalho, no canto superior direito ([DKFDS](https://designsystem.dk/komponenter/search/)); na barra de ferramentas, na borda final ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)); num filtro, logo acima da lista.

**Tenha uma pesquisa por página.** Se precisar de duas, dê a cada uma um rótulo que diga o que ela pesquisa ([HDS](https://hds.hel.fi/components/search-input)).

**Aceite o termo em qualquer formato.** Números de processo, CPF e protocolos podem chegar com ou sem pontos, hífens, barras e espaços; normalize no sistema e nunca bloqueie caracteres (decisão D3).

**Faça** Use um campo largo, com texto de exemplo curto que diga o escopo da pesquisa.

**Não faça** Use um campo estreito, que esconde o que a pessoa digitou, com instruções longas dentro dele.

### Estados

Repouso, hover, foco, preenchido e carregando. No hover o cursor vira o cursor de texto; com o campo focado, o hover não muda a superfície ([gov.br DS](https://www.gov.br/ds/components/input)). O campo de pesquisa não fica desabilitado: se a pesquisa não está disponível, retire-a.

### Comportamento

**Pesquisa expansível.** Ao acionar a lupa no cabeçalho estreito, os outros elementos do cabeçalho se ocultam, o campo ocupa toda a largura e recebe o foco, e um botão circular Fechar aparece. Fechar devolve o cabeçalho ao estado anterior ([gov.br DS](https://www.gov.br/ds/components/header)) e o foco ao botão de lupa. Esc tem o mesmo efeito com o campo vazio.

**Sugira enquanto a pessoa digita.** Atualize as sugestões o mais rápido possível; se houver espera, mostre um indicador de carregamento na lista ([gov.br DS](https://www.gov.br/ds/components/input)). Antes de digitar, mostre pesquisas recentes; com a consulta, as sugestões tomam o lugar delas ([Fluent](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage)). O HDS guarda até 10 pesquisas, só depois do consentimento de cookies de preferência ([HDS](https://hds.hel.fi/components/search)); veja Privacidade.

**Ordene as sugestões por relevância.** Mostre primeiro as mais prováveis ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields), [Fluent](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage)). Quando o sistema não tem critério de relevância, como numa lista de municípios, use ordem alfabética.

> **Divergência entre referências** O gov.br recomenda ordem alfabética nas sugestões do autocompletar ([gov.br DS](https://www.gov.br/ds/components/input)). A HIG e o Fluent põem primeiro os resultados mais relevantes ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields), [Fluent](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage)). Sem pesquisa citada de nenhum lado, o Trama segue a convergência (relevância) e usa a ordem alfabética do gov.br quando todas as sugestões têm a mesma relevância.

**Diga quando não há sugestão.** Mostre a mensagem no lugar da lista, como “Nenhum resultado para ‘prazo recrusal’”, e, se possível, assuntos relacionados ao termo ([gov.br DS](https://www.gov.br/ds/components/input)). Tolere erros de digitação com texto preditivo ([One UI](https://developer.samsung.com/one-ui/comp/search.html)).

**A lista segue o padrão dropdown.** Abre abaixo do campo, não cria espaço extra e ocupa a largura total na classe Compacta ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). O botão de limpar apaga o texto e devolve o foco ao campo.

## Conteúdo

Use o texto de exemplo para dizer o que se pode pesquisar, como “Número, parte ou assunto” ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)). Ele some quando a pessoa digita, por isso não serve para instruções; se forem necessárias, coloque-as acima do campo ([DKFDS](https://designsystem.dk/komponenter/search/)). O texto de exemplo não usa itálico. O botão de envio diz “Pesquisar”, nunca “Buscar” (vocabulário D7). Na mensagem sem resultado, diga quais termos foram pesquisados e o que tentar; veja Estados vazios.

## Acessibilidade

**Dê um rótulo ao campo.** Visível sempre que possível; oculto apenas no cabeçalho ([HDS](https://hds.hel.fi/components/search-input)). Associe com `for` e `id`, e use `aria-describedby` para instruções ([gov.br DS](https://www.gov.br/ds/components/input)).

**Nomeie as ações internas e alcance-as pelo teclado.** “Pesquisar”, “Limpar pesquisa”, “Fechar pesquisa”. Elas recebem foco com Tab, depois do campo, e ativam com Espaço ou Enter ([gov.br DS](https://www.gov.br/ds/components/input)).

**Marque o formulário como região de pesquisa.** Use `role="search"` ou o elemento `<search>` ([HDS](https://hds.hel.fi/components/header/accessibility)).

**Com sugestões, siga o padrão combobox.** O campo tem `role="combobox"`, `aria-expanded` e `aria-controls`; o destaque usa `aria-activedescendant`, mantendo o foco no campo. Sem sugestões, o papel é `searchbox` ([HDS](https://hds.hel.fi/components/search/accessibility)).

| Tecla           | Função                                                                     |
|-----------------|----------------------------------------------------------------------------|
| Seta para baixo | Abre as pesquisas recentes com o campo vazio; move para a próxima sugestão |
| Seta para cima  | Move para a sugestão anterior                                              |
| Enter           | Escolhe a sugestão destacada; sem destaque, envia a pesquisa               |
| Esc             | Fecha as sugestões e mantém o foco no campo                                |

O mapa de teclas segue o HDS ([HDS](https://hds.hel.fi/components/search/accessibility)). Anuncie a contagem de resultados e a ausência deles numa região `aria-live`, como “5 sugestões para ‘prazo’” (WCAG 2.2, 4.1.3).

## Tokens usados

| Token                                      | Uso                                                             |
|--------------------------------------------|-----------------------------------------------------------------|
| `--t-surface-raised`, `--t-border-control` | Fundo e borda (3:1)                                             |
| `--r-pill`, `--r-lg`                       | Cápsula do campo padrão; raio do campo destaque                 |
| `--c-h-md`, `--c-h-lg`, `--d-control`      | Altura padrão; destaque e densidade baixa; altura por densidade |
| `--t-fg-1`, `--t-fg-3`                     | Texto digitado; ícone e texto de exemplo                        |
| `--e-4`, `--z-2`                           | Lista de sugestões                                              |
| `--t-focus`                                | Anel de foco no contêiner                                       |

## Considerações por plataforma

### Web desktop

Nas classes Grande e Extragrande, o campo fica aberto no cabeçalho ([gov.br DS](https://www.gov.br/ds/components/header)), em densidade alta quando o cabeçalho é compacto ([gov.br DS](https://www.gov.br/ds/components/input)). Ofereça um atalho de teclado para focar a pesquisa global; não reutilize o atalho de uma paleta de comandos ([Geist](https://vercel.com/geist/command-menu)).

### Web móvel

Na classe Compacta, use a pesquisa expansível no cabeçalho e, no conteúdo, o campo em largura total com densidade baixa ([gov.br DS](https://www.gov.br/ds/components/input)). Use `type="search"` e `enterkeyhint="search"` para o teclado virtual mostrar a tecla de pesquisa. Mantenha a fonte em 16px ou mais para o navegador não ampliar a página ao focar.

### Tablets e dobráveis

Na classe Média, a pesquisa do cabeçalho também é expansível ([gov.br DS](https://www.gov.br/ds/components/header)). Ao chegar a uma área dedicada à pesquisa, foque o campo; se só houver teclado virtual, deixe sem foco para o teclado não cobrir a vista sem aviso ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)). Ao abrir ou fechar o dobrável, preserve o texto digitado e o teclado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Pesquisa
- Campos de texto
- Combobox
- Cabeçalho
- Estados vazios

### Referências

- [Input (Campo de Entrada de Texto)](https://www.gov.br/ds/components/input) gov.br DS
- [Header](https://www.gov.br/ds/components/header) gov.br DS
- [Dropdown (Elemento Flutuante)](https://www.gov.br/ds/padroes/design/dropdown) gov.br DS
- [Navegação](https://www.gov.br/ds/padroes/design/navegacao) gov.br DS
- [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields) Apple HIG
- [SearchBox: usage](https://fluent2.microsoft.design/components/web/react/core/searchbox/usage) Fluent 2
- [Navigate a service](https://design-system.service.gov.uk/patterns/navigate-a-service/) GOV.UK Design System
- [Søgefelt](https://designsystem.dk/komponenter/search/) DKFDS
- [Search](https://hds.hel.fi/components/search) Helsinki Design System
- [Search: accessibility](https://hds.hel.fi/components/search/accessibility) Helsinki Design System
- [SearchInput](https://hds.hel.fi/components/search-input) Helsinki Design System
- [Header: accessibility](https://hds.hel.fi/components/header/accessibility) Helsinki Design System
- [Command Menu](https://vercel.com/geist/command-menu) Geist
- [Search](https://developer.samsung.com/one-ui/comp/search.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                              |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. O componente passa a se chamar Campo de pesquisa (D7) e ganha o tipo destaque, a pesquisa expansível do cabeçalho, regras de sugestões e de ausência de resultado, densidades e aceitação de qualquer formato (D3). |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                       |
