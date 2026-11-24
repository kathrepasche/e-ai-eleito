# Desenvolvimento

## Construir componentes

Regras para criar ou estender um componente do Trama: nome, variações, estados, elementos de ação, documentação e tokens.

Um componente do Trama é um conjunto de marcação, estilo, comportamento e documentação que sempre andam juntos. Esta página define as convenções de código do kit e o caminho para propor um componente novo. Ela vale para quem mantém o Trama e para equipes de produto que criam componentes próprios sobre ele.

### Antes de criar

**Confirme que o componente ainda não existe.** Procure no Trama e no histórico de propostas. Depois, veja se um componente existente atende com uma pequena mudança. Por fim, pergunte se o componente serve a outros produtos e se pode ficar mais genérico ([HDS](https://hds.hel.fi/getting-started/contributing/how-to-contribute)). Só então proponha um componente novo.

**Entregue design, documentação e código juntos.** Um componente só entra no sistema quando as três partes estão prontas e validadas ([HDS](https://hds.hel.fi/getting-started/contributing/how-to-contribute)). A documentação não é publicada antes do código ([HDS](https://hds.hel.fi/getting-started/contributing/documentation)).

### Regras de código

**Use o prefixo `tr-`.** Toda classe de componente começa com `tr-`, como todo componente do gov.br começa com `br-` ([gov.br](https://www.gov.br/ds/guias/construcao-de-componentes)). O prefixo evita colisão com o CSS do produto. Partes internas usam dois sublinhados (`.tr-header__title`) e variações usam dois hífens (`.tr-btn--primary`). Componentes criados por um produto usam o prefixo do produto, nunca `tr-`.

**Variações fixas são classes; estados são atributos.** Tipo, tamanho e ênfase, que não mudam enquanto a pessoa usa a página, são classes modificadoras: `.tr-btn--primary`, `.tr-btn--sm`, `.tr-header--sticky`. Estados que mudam com a interação usam o atributo nativo ou ARIA que já comunica o estado às tecnologias assistivas, e o CSS estiliza esse atributo: `aria-pressed`, `aria-expanded`, `aria-current`, `aria-selected`, `aria-invalid`, `disabled`. Estados visuais sem equivalente ARIA usam `data-state`, como `data-state="success"` num campo. Contextos que afetam vários componentes usam um atributo ou uma classe no contêiner: `data-density` e `.tr-inverse`.

**Comportamentos são ligados por atributo.** O script encontra o componente pela classe raiz e liga o comportamento a partir de atributos, como os que indicam qual elemento abre e qual é aberto ([gov.br](https://www.gov.br/ds/guias/construcao-de-componentes)). Veja JavaScript.

**Ações só em `<button>` e `<a>`.** Por acessibilidade e compatibilidade entre navegadores, só botões e links recebem ações ([gov.br](https://www.gov.br/ds/guias/construcao-de-componentes)). Use `<a href>` quando a ação leva a outro endereço e `<button type="button">` quando ela muda algo na página ou envia dados. Nunca ponha ação de clique em `<div>` ou `<span>`.

> **Divergência entre referências** O gov.br aplica por classe as variações de tipo, densidade, cor e estado, e reserva atributos para comportamentos ([gov.br](https://www.gov.br/ds/guias/construcao-de-componentes)). O Trama aplica estados por atributo ARIA ou nativo, para que o estado visual e o estado anunciado pelo leitor de tela venham da mesma fonte e não possam divergir (critério 2). Densidade é contexto e usa `data-density` (D11).

**Faça** um `<button>` com `aria-expanded`, que o CSS usa para o estado aberto.

**Não faça** um `<span>` com aparência de botão, sem foco por teclado e sem estado anunciado.

### Tokens de componente

**Consuma tokens alias.** Componentes usam tokens alias (`--t-*`), de espaçamento, forma, elevação e movimento. Nunca usam globais (`--g-*`) nem valores literais de cor, espaço ou fonte ([HDS](https://hds.hel.fi/getting-started/contributing/implementation), [gov.br](https://www.gov.br/ds/guias/boas-praticas-de-css)). Veja CSS e tokens no código.

**Crie um token de componente só quando o valor precisa variar.** O gov.br orienta criar tokens no componente apenas quando houver necessidade de modificar o valor; caso contrário, eles não têm utilidade ([gov.br](https://www.gov.br/ds/guias/codificacao-sass)). No Trama, um token de componente se justifica quando ao menos uma condição vale:

- o mesmo valor é trocado por uma variação ou um contexto, como os tokens `--d-*` que `data-density` redefine;
- produtos precisam ajustar o valor sem reescrever o componente;
- o valor é usado em várias propriedades do componente e precisa ficar sincronizado.

Nomeie como `--tr-<componente>-<propriedade>` e aponte sempre para um token alias. As variações redefinem só o token ([gov.br](https://www.gov.br/ds/guias/codificacao-sass)):

``` code
.tr-aviso {
  --tr-aviso-fundo: var(--t-info-subtle);
  --tr-aviso-borda: var(--t-info-border);
  background: var(--tr-aviso-fundo);
  border: var(--stroke-thin) solid var(--tr-aviso-borda);
  padding: var(--d-pad-y) var(--d-pad-x);
}
.tr-aviso--sucesso {
  --tr-aviso-fundo: var(--t-success-subtle);
  --tr-aviso-borda: var(--t-success-border);
}
```

### Documentação de cada componente

O gov.br divide a documentação de cada componente em diretriz de design, guia de desenvolvimento e acessibilidade, e registra o componente numa lista central ([gov.br](https://www.gov.br/ds/guias/construcao-de-componentes)). O Trama reúne tudo numa página, nesta ordem:

1.  Resumo, quando usar e quando não usar, com a alternativa.
2.  Demonstração ao vivo com o kit.
3.  Anatomia, com o nome de cada parte e a classe correspondente.
4.  Tipos, quando houver.
5.  Boas práticas, com estados e comportamento, e ao menos um par Faça e Não faça.
6.  Conteúdo (textos de interface).
7.  Acessibilidade: elementos, papéis, teclado e anúncios.
8.  Tokens usados.
9.  Considerações por plataforma: Web desktop, Web móvel, Tablets e dobráveis.
10. Recursos e histórico de mudanças.

Quando as referências divergem, a página registra a decisão numa nota "Divergência entre referências". Use títulos de seção em ordem hierárquica e marque links externos ([HDS](https://hds.hel.fi/getting-started/contributing/documentation)).

### Testes

**Teste cada estado.** Escreva testes de renderização, acessibilidade e comportamento, e crie um exemplo para cada estado distinto do componente, para que ele possa ser exercitado em testes automáticos ([HDS](https://hds.hel.fi/getting-started/contributing/implementation)).

**Não dependa só de ferramentas automáticas.** Um estudo do GDS de 2017 concluiu que ferramentas automáticas acham cerca de 30% dos problemas de acessibilidade ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)). Complete com teste manual por teclado, leitor de tela, ampliação e modo de alto contraste. O eMAG também pede validação automática seguida de validação manual ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)). Veja Navegadores e dispositivos suportados.

**Valide o HTML.** Código fora do padrão do kit precisa ser validado, por exemplo no validador de marcação do W3C ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/frameworks/)).

### Considerações por plataforma

#### Web desktop

Teste o componente com mouse, teclado e trackpad, e com densidade alta quando ele for usado em tabelas, listas longas ou ferramentas (D11).

#### Web móvel

Projete o componente primeiro para a classe Compacta. Toda área de ação tem `--c-touch`, e a densidade baixa é obrigatória em toque (D11, D17).

#### Tablets e dobráveis

Teste a troca de classe de janela com o componente aberto, como acontece ao abrir ou fechar um dobrável: estado, foco e conteúdo digitado devem continuar.

### Recursos

#### Relacionados

- HTML acessível e WAI-ARIA
- CSS e tokens no código
- JavaScript
- Tokens de design
- Estados de interação
- Versões e migração

#### Referências

- [Construção de componentes](https://www.gov.br/ds/guias/construcao-de-componentes) gov.br DS
- [Codificação Sass](https://www.gov.br/ds/guias/codificacao-sass) gov.br DS
- [Boas práticas de CSS](https://www.gov.br/ds/guias/boas-praticas-de-css) gov.br DS
- [Acessibilidade no código HTML](https://www.gov.br/ds/guias/acessibilidade-html) gov.br DS
- [How to contribute](https://hds.hel.fi/getting-started/contributing/how-to-contribute) Helsinki Design System
- [Contributing: implementation](https://hds.hel.fi/getting-started/contributing/implementation) Helsinki Design System
- [Contributing: documentation](https://hds.hel.fi/getting-started/contributing/documentation) Helsinki Design System
- [Accessibility strategy](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) GOV.UK Design System
- [Frameworks](https://designsystem.dk/kom-i-gang/implementering-kode/frameworks/) DKFDS

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## HTML acessível e WAI-ARIA

Marcação válida e semântica é a base da acessibilidade no Trama: elementos nativos primeiro, ARIA só para o que o HTML não expressa.

Leitores de tela, ampliadores, controle por voz e navegação por teclado dependem da árvore de acessibilidade que o navegador monta a partir do HTML. Uma estrutura semântica correta produz uma árvore organizada e precisa ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)). O eMAG, modelo de acessibilidade do governo federal brasileiro, resume o processo em três passos: seguir os padrões web, seguir as recomendações de acessibilidade e avaliar a acessibilidade ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)).

Usar o Trama não torna um produto acessível por si só: ainda é preciso pesquisa, design, desenvolvimento e teste ([GOV.UK](https://design-system.service.gov.uk/accessibility/)). Esta página trata da marcação. Para cor, contraste e conteúdo, veja Acessibilidade.

### Semântica nativa primeiro

**Escreva HTML válido.** HTML válido segue a gramática e a sintaxe da linguagem, aparece de forma previsível em qualquer navegador e tem mais chance de funcionar com tecnologias assistivas ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)). Valide o código que foge do kit ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/frameworks/)).

**Use cada elemento pelo que ele é.** Escolha o elemento pelo significado; a aparência vem do CSS ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html), [Fluent](https://fluent2.microsoft.design/accessibility)). Um botão é `<button>`, um link é `<a href>`, um campo tem `<label>`, um grupo de opções tem `<fieldset>` e `<legend>`.

**Prefira o elemento nativo ao ARIA.** Quando existe um elemento HTML com a semântica e o comportamento de que você precisa, use-o em vez de recriar o papel com ARIA ([W3C](https://www.w3.org/TR/using-aria/)). Os estados e propriedades nativos têm precedência sobre os equivalentes ARIA, e o atributo `role` sobrescreve o papel implícito do elemento ([gov.br](https://www.gov.br/ds/guias/wai-aria)), por isso um `role` errado apaga uma semântica que estava certa.

**Use ARIA para componentes que o HTML não cobre.** O WAI-ARIA dá papéis (`role`), estados e propriedades (`aria-*`) a componentes personalizados, como abas e menus. O autor associa o papel e mantém estados e propriedades atualizados durante todo o ciclo de vida do elemento ([gov.br](https://www.gov.br/ds/guias/wai-aria)). Siga os padrões de interação do guia de práticas de autoria do WAI-ARIA ([Fluent](https://fluent2.microsoft.design/accessibility)).

**Faça** `<button type="button">`: foco, Enter, Espaço e papel vêm prontos.

**Não faça** `<span role="button">` sem `tabindex` nem teclado: o papel promete um botão que não funciona.

### Estrutura da página

**Declare o idioma.** O atributo `lang` vai no `<html>` de todas as páginas: `lang="pt-BR"`. Trechos em outro idioma levam o próprio `lang`; nomes próprios e termos técnicos compreendidos no contexto não precisam ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html); WCAG 2.2, 3.1.1 e 3.1.2).

**Monte o esqueleto do documento.** `<!doctype html>`, codificação UTF-8, viewport com largura do dispositivo e escala 1 e um `<title>` por página ([gov.br](https://www.gov.br/ds/guias/boas-praticas-de-html)). O título descreve a página: assunto primeiro, produto depois (WCAG 2.2, 2.4.2). Não bloqueie o zoom no viewport.

**Marque as regiões com landmarks.** Use `<header>`, `<nav>`, `<main>` e `<footer>` ([gov.br](https://www.gov.br/ds/components/skiplink)), e `role="search"` na pesquisa ([HDS](https://hds.hel.fi/components/header/accessibility)). Tenha um só `<main>`. Quando houver dois landmarks do mesmo tipo, como duas `<nav>`, dê a cada um um `aria-label` diferente. Use landmarks com moderação: muitos geram ruído para leitores de tela e confundem a estrutura ([HDS](https://hds.hel.fi/components/header/accessibility)). Os links de pular levam a esses landmarks.

**Use um único H1 e níveis em ordem.** O H1 corresponde ao conteúdo principal, e o recomendável é um por página; H2 a H6 podem se repetir, sempre em hierarquia ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)). Não pule níveis nem use um nível pelo tamanho visual ([Fluent](https://fluent2.microsoft.design/accessibility)). A aparência vem das classes de tipografia, como `.tr-title-2`; o nível vem do conteúdo.

**Use listas para listas.** `<ul>` para itens sem ordem e `<ol>` quando a ordem importa ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)). Leitores de tela anunciam a quantidade de itens. Navegações, breadcrumbs e etapas são listas.

**Use tabelas só para dados.** Tabelas servem a dados tabulares; o layout é feito com CSS ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)). Toda tabela de dados tem `<caption>`, cabeçalhos `<th>` com `scope` e, se for ordenável, `aria-sort` na coluna ordenada. Veja Tabelas.

**Dê alternativa em texto às imagens.** Imagens informativas têm `alt` que descreve o conteúdo; imagens que são links descrevem o destino ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)). Imagens decorativas têm `alt=""`.

**Associe rótulos aos campos.** Todo campo tem `<label for>` ligado ao seu `id`; o leitor de tela lê o rótulo ao chegar ao campo ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)). Texto de ajuda e mensagem de erro se ligam ao campo com `aria-describedby`.

### Papéis usados pelos componentes do Trama

A tabela mostra o elemento ou papel e os estados que cada componente usa. Onde a coluna traz um elemento nativo, ele dispensa ARIA adicional.

| Componente                                 | Elemento ou papel                                                                 | Estados e propriedades                                                                          |
|--------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Cabeçalho `.tr-header`                     | `<header>` (banner)                                                               | `aria-current` na navegação; `aria-expanded` nos botões de menu e pesquisa                      |
| Rodapé `.tr-footer`                        | `<footer>` (contentinfo)                                                          | `<details name>` no mapa recolhível                                                             |
| Links de pular `.tr-skiplinks`             | `<a href="#id">`, sem landmark                                                    | `tabindex="-1"` no destino                                                                      |
| Navegação lateral `.tr-nav`                | `<nav aria-label>` com links                                                      | `aria-current="page"`                                                                           |
| Breadcrumb `.tr-breadcrumb`                | `<nav aria-label>` + `<ol>`                                                       | `aria-current="page"` no item atual                                                             |
| Paginação `.tr-pagination`                 | `<nav aria-label>` com links                                                      | `aria-current="page"`                                                                           |
| Campo de pesquisa `.tr-search`             | `<form role="search">` + `<input type="search">`                                  | `<label>`, visível ou oculto                                                                    |
| Botão `.tr-btn`                            | `<button>` ou `<a>`                                                               | `aria-pressed` em alternância; `aria-expanded` se abre algo                                     |
| Controle segmentado `.tr-seg`              | Grupo de `<button>`                                                               | `aria-pressed`                                                                                  |
| Checkbox e radio `.tr-check`               | `<input type="checkbox|radio">` em `<fieldset>`                                   | `checked`, `indeterminate`                                                                      |
| Switch `.tr-switch`                        | `<input type="checkbox" role="switch">`                                           | `checked`                                                                                       |
| Campo de texto `.tr-input`                 | `<input>` + `<label>`                                                             | `aria-invalid`, `aria-describedby`                                                              |
| Abas `.tr-tabs`                            | `tablist`, `tab`, `tabpanel`                                                      | `aria-selected`, `aria-controls`, `aria-labelledby`                                             |
| Acordeão `.tr-accordion`                   | `<details>` + `<summary>`                                                         | `open` (nativo)                                                                                 |
| Menu de ações `.tr-menu`                   | `menu` + `menuitem`                                                               | `aria-haspopup="menu"` e `aria-expanded` no botão que abre                                      |
| Diálogo `.tr-dialog`                       | `<dialog>` ou `role="dialog"`                                                     | `aria-modal="true"`, `aria-labelledby`                                                          |
| Drawer `.tr-drawer`                        | `role="dialog"`                                                                   | `aria-modal` quando bloqueia a página, `aria-labelledby`                                        |
| Tooltip `.tr-tooltip`                      | `role="tooltip"`                                                                  | `aria-describedby` no elemento de origem                                                        |
| Toast `.tr-toast`                          | `role="status"`                                                                   | Região viva educada                                                                             |
| Mensagem `.tr-msg`                         | `role="alert"` se inserida para um erro; `role="status"` para as demais inseridas | Nenhum papel quando já está na página ao carregar                                               |
| Resumo de erros `.tr-error-summary`        | Título + lista de links para os campos                                            | Recebe o foco ao aparecer ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)) |
| Progresso `.tr-progress`                   | `<progress>` ou `role="progressbar"`                                              | `aria-valuenow`, `aria-valuemin`, `aria-valuemax`; sem valor quando indeterminado               |
| Spinner `.tr-spinner`                      | `role="status"` com texto                                                         | `aria-busy="true"` na região que carrega                                                        |
| Indicador de etapas `.tr-steps`            | `<ol>`                                                                            | `aria-current="step"`                                                                           |
| Tabela `.tr-table`                         | `<table>` + `<caption>` + `<th scope>`                                            | `aria-sort` na coluna ordenada                                                                  |
| Lista selecionável `.tr-list--interactive` | `listbox` + `option`                                                              | `aria-selected`                                                                                 |
| Avatar `.tr-avatar`                        | Imagem com `alt`, ou `aria-hidden="true"` ao lado do nome                         | Nenhum                                                                                          |

`aria-current` marca a posição atual em navegação; `aria-selected` e `aria-checked` marcam escolhas numa coleção (D10). Numa subpágina cuja seção continua destacada, use `aria-current="true"` ([DKFDS](https://designsystem.dk/komponenter/header/)).

### eMAG para produtos públicos

Produtos para órgãos públicos brasileiros observam o eMAG, além da meta WCAG 2.2 AA (D25). O eMAG se baseia nas recomendações do WCAG e tem o compromisso de ser o norteador do desenvolvimento e da adaptação de conteúdos digitais do governo federal ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)). Na avaliação, valide o código com validadores automáticos e complete com validação manual por listas de verificação, porque nem todo problema é detectado mecanicamente ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)). Veja Legislação e normas.

> **Divergência entre referências** O guia de acessibilidade em HTML do gov.br cita o WCAG 2.1 e o WAI-ARIA 1.1 como versões vigentes ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)). O GOV.UK já entrega componentes conformes ao WCAG 2.2 AA ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)). O Trama adota o WCAG 2.2 AA como meta, que inclui os critérios do 2.1 (critério 2), e trata o eMAG como requisito adicional para produtos públicos (D25).

### Considerações por plataforma

#### Web desktop

Teste a navegação por landmarks e por títulos com leitores de tela de desktop; a ordem do foco segue a ordem visual, da esquerda para a direita e de cima para baixo ([Fluent](https://fluent2.microsoft.design/accessibility)).

#### Web móvel

Leitores de tela de celular navegam por gestos entre títulos, landmarks e links; a mesma marcação serve. Não esconda conteúdo com `aria-hidden` só porque ele está fora da área visível em telas pequenas: use CSS de layout.

#### Tablets e dobráveis

Quando dois painéis aparecem lado a lado, cada um é uma região com nome (`aria-label` ou `aria-labelledby`), e a ordem no código segue a ordem de leitura. Nenhuma outra consideração.

### Recursos

#### Relacionados

- Acessibilidade
- Legislação e normas
- Construir componentes
- JavaScript
- Links de pular
- Foco e seleção

#### Referências

- [Acessibilidade no código HTML](https://www.gov.br/ds/guias/acessibilidade-html) gov.br DS
- [Uso do WAI-ARIA](https://www.gov.br/ds/guias/wai-aria) gov.br DS
- [Boas práticas de HTML](https://www.gov.br/ds/guias/boas-praticas-de-html) gov.br DS
- [Skip Link](https://www.gov.br/ds/components/skiplink) gov.br DS
- [Accessibility](https://design-system.service.gov.uk/accessibility/) GOV.UK Design System
- [Accessibility strategy](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) GOV.UK Design System
- [Recover from validation errors](https://design-system.service.gov.uk/patterns/validation/) GOV.UK Design System
- [Header: accessibility](https://hds.hel.fi/components/header/accessibility) Helsinki Design System
- [Header](https://designsystem.dk/komponenter/header/) DKFDS
- [Frameworks](https://designsystem.dk/kom-i-gang/implementering-kode/frameworks/) DKFDS
- [Accessibility](https://fluent2.microsoft.design/accessibility) Fluent 2
- [Using ARIA](https://www.w3.org/TR/using-aria/) W3C

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## CSS e tokens no código

No código, todo valor visual vem de um token do Trama, escrito a partir da tela pequena e organizado em camadas que permitem temas, densidades e fundos invertidos.

Os tokens do Trama são propriedades personalizadas de CSS declaradas em `kit.css`. Eles são a fonte única de cor, espaço, forma, elevação, movimento e camadas. Esta página explica como consumir esses tokens no CSS do produto e dos componentes, como as camadas se organizam e como escrever folhas de estilo consistentes. Para o significado de cada token, veja Tokens de design.

### Camadas do kit

| Camada      | Prefixo                                                        | Exemplo                        | Quem usa                                           |
|-------------|----------------------------------------------------------------|--------------------------------|----------------------------------------------------|
| Globais     | `--g-*`                                                        | `--g-brand-60`                 | Só o próprio kit, para definir os alias            |
| Alias       | `--t-*`, `--sp-*`, `--r-*`, `--e-*`, `--m-*`, `--z-*`, `--o-*` | `--t-brand`, `--sp-400`        | Produtos e componentes                             |
| Contexto    | `--d-*`, `--f-*`                                               | `--d-control`, `--f-gap-field` | Componentes que mudam com a densidade; formulários |
| Componentes | `.tr-*`                                                        | `.tr-btn`                      | Marcação do produto                                |

**Use só tokens alias e de contexto.** Globais descrevem valores brutos, como um tom de cinza; alias descrevem função, como texto secundário. Quando o tema muda, só os alias são redefinidos. Um produto que usa `--g-grey-60` no lugar de `--t-fg-3` não acompanha o modo escuro.

### Boas práticas

**Não escreva valores fixos.** Use sempre tokens nos estilos de componentes e páginas; valores fixos impedem a aplicação de temas ([gov.br](https://www.gov.br/ds/guias/boas-praticas-de-css)). Em vez de especificar pixels, cores, fontes ou breakpoints, aplique os tokens ([HDS](https://hds.hel.fi/getting-started/contributing/implementation)). Valem como exceção: `0`, porcentagens de layout, `auto` e os limites das classes de janela em media queries, porque propriedades personalizadas não funcionam dentro da condição de uma media query.

``` code
/* Faça */
.resumo-pedido {
  padding: var(--sp-400);
  border: var(--stroke-thin) solid var(--t-border-subtle);
  border-radius: var(--r-lg);
  background: var(--t-surface-raised);
  color: var(--t-fg-1);
}

/* Não faça */
.resumo-pedido {
  padding: 16px;
  border: 1px solid #E1E4E8;
  border-radius: 8px;
  background: #fff;
  color: #15191E;
}
```

**Não altere o CSS do kit.** Personalize por cima, redefinindo tokens ou acrescentando regras no CSS do produto. O DKFDS pede nunca escrever direto nos arquivos de CSS distribuídos e alerta que alterar o código-fonte do sistema dificulta atualizar para novas versões ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/justering/)). Valores literais que ainda restam dentro do kit, como alguns tamanhos de fonte de componentes, são dívida registrada para versões futuras: não os copie para o produto.

**Escreva primeiro para a tela pequena.** O estilo base vale para a classe Compacta; cada media query com `min-width` acrescenta o que muda nas classes maiores ([gov.br](https://www.gov.br/ds/guias/boas-praticas-de-css), [GOV.UK](https://design-system.service.gov.uk/styles/layout/)). Use os limites das classes de janela do Trama: 600, 840, 1200 e 1600px. Escreva as media queries de cada componente no próprio arquivo do componente ([gov.br](https://www.gov.br/ds/guias/boas-praticas-de-css)).

``` code
.lista-pedidos { display: grid; gap: var(--sp-300); }

@media (min-width: 840px) {           /* Expandida */
  .lista-pedidos { grid-template-columns: 1fr 1fr; gap: var(--sp-600); }
}
@media (min-width: 1200px) {          /* Grande */
  .lista-pedidos { grid-template-columns: repeat(3, 1fr); }
}
```

### Temas, densidade e fundo invertido

**Temas claro e escuro.** Os alias têm valores claros em `:root`. O kit os redefine para o escuro em `@media (prefers-color-scheme: dark)`, protegido por `:root:not([data-theme="light"])`, e de novo em `:root[data-theme="dark"]`. Assim o produto segue a preferência do sistema e também aceita uma escolha explícita da pessoa. Não teste a cor do sistema em JavaScript para trocar classes; o CSS já resolve. Veja Modo escuro.

**Densidade com `data-density`.** `data-density="alta"` ou `"baixa"` num contêiner redefine os tokens `--d-*` para tudo o que estiver dentro: altura de controle, espaçamentos, altura de linha de lista e de célula (D11). Componentes novos que precisam responder à densidade consomem `--d-*` em vez de `--c-h-md`. Veja Densidade.

**Fundo escuro no tema claro com `.tr-inverse`.** A classe redefine os alias para os valores escuros dentro do contêiner, para rodapés e faixas escuras (D27). Os componentes de dentro continuam corretos sem regra extra.

### Escrita do CSS

**Ordene as declarações.** Em cada regra, primeiro as propriedades personalizadas (tokens locais), depois as declarações, depois as regras aninhadas e os estados. O gov.br configura essa ordem no linter: propriedades personalizadas, variáveis do pré-processador, declarações e regras ([gov.br](https://www.gov.br/ds/guias/codificacao-sass)). Dentro das declarações, o Trama segue a sequência posição e camada, caixa e layout, tipografia, cor e fundo, borda e forma, sombra, movimento.

**Estilize estados por atributo.** Use `[aria-expanded="true"]`, `[aria-current="page"]`, `[aria-invalid="true"]` e `:disabled` como seletores de estado. O foco aparece com `:focus-visible` (D12). Veja Construir componentes.

**Mantenha a especificidade baixa.** Uma classe por seletor sempre que possível. Não use `id` em seletores nem `!important`, exceto em utilitários que precisam vencer qualquer regra, como `.tr-visually-hidden`.

**Use as camadas de sobreposição.** `z-index` só com `--z-0` a `--z-4`, e a elevação acompanha a camada (D26). Nunca crie valores como `z-index: 9999`.

**Respeite a redução de movimento.** Toda transição ou animação usa os tokens `--m-*` e é anulada em `prefers-reduced-motion: reduce`, como o kit faz. Ofereça também o controle no produto (D20).

**Comente a intenção.** Cada componente ou modelo começa com um comentário sobre a finalidade do código; comentários curtos explicam propriedades que não são óbvias ([gov.br](https://www.gov.br/ds/guias/boas-praticas-de-css)).

**Garanta o conteúdo sem CSS.** O conteúdo principal precisa continuar disponível sem as folhas de estilo, o que atende folhas personalizadas e modos de cores forçadas ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)). Teste no modo de alto contraste do sistema: bordas e anéis de foco devem continuar visíveis.

### Lint

Use o stylelint, que o gov.br adota e executa no pipeline sempre que código novo entra no repositório ([gov.br](https://www.gov.br/ds/guias/boas-praticas-de-css)). No Trama, configure ao menos:

- proibição de cores hexadecimais e nomeadas fora de `kit.css` (regra `color-no-hex` e lista de valores proibidos);
- proibição de `z-index` numérico e de `!important` fora de utilitários;
- ordem das declarações descrita acima;
- uso de `var(--…)` obrigatório em `color`, `background`, `border-color`, `box-shadow`, `margin`, `padding` e `gap`.

> **Divergência entre referências** O gov.br escreve os estilos em Sass, no formato SCSS, com blocos de mixins por componente ([gov.br](https://www.gov.br/ds/guias/codificacao-sass)), e o DKFDS pede ajustes pelos arquivos SCSS distribuídos ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/justering/)). O Trama distribui CSS puro com propriedades personalizadas, que mudam em tempo de execução sem compilação; isso é o que permite `data-density`, `.tr-inverse` e a troca de tema. Pré-processadores são opcionais no produto, desde que produzam CSS que consome os tokens.

### Considerações por plataforma

#### Web desktop

Em ferramentas com apontador fino, a densidade alta pode ser o padrão da área de trabalho, mas nunca em alertas e mensagens (D11). Teste o zoom do navegador em 200% (WCAG 2.2, 1.4.4).

#### Web móvel

O estilo base é o da classe Compacta. Use unidades relativas para texto, para respeitar o tamanho de fonte escolhido pela pessoa, e garanta o refluxo sem rolagem horizontal em 320px de largura CSS (WCAG 2.2, 1.4.10).

#### Tablets e dobráveis

Os layouts reagem à largura da janela, qualquer que seja o aparelho: um dobrável aberto entra na classe Média ou Expandida e recebe o CSS dessas classes. Para a dobra, veja Postura e dobra.

### Recursos

#### Relacionados

- Tokens de design
- Modo escuro
- Densidade
- Layout e grid
- Construir componentes
- Movimento

#### Referências

- [Boas práticas de CSS](https://www.gov.br/ds/guias/boas-praticas-de-css) gov.br DS
- [Codificação Sass](https://www.gov.br/ds/guias/codificacao-sass) gov.br DS
- [Justering af tema og stylesheets](https://designsystem.dk/kom-i-gang/implementering-kode/justering/) DKFDS
- [Contributing: implementation](https://hds.hel.fi/getting-started/contributing/implementation) Helsinki Design System
- [Layout](https://design-system.service.gov.uk/styles/layout/) GOV.UK Design System
- [Accessibility strategy](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) GOV.UK Design System

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## JavaScript

O JavaScript do Trama melhora componentes que já funcionam em HTML: uma classe por componente, uma instância por ocorrência e estados acessíveis gerados pelo próprio script.

Os componentes do Trama são construídos em camadas. O HTML entrega o conteúdo e as funções essenciais; o CSS dá a aparência; o JavaScript acrescenta comportamentos que melhoram a experiência. Esta página define como escrever esse script. Ela vale para o kit e para componentes próprios dos produtos.

### Melhoria progressiva

**Faça a página funcionar sem JavaScript.** Comece pelo HTML semântico, garanta o conteúdo sem CSS e construa uma experiência que funcione bem sem JavaScript; ofereça melhorias em JavaScript acessíveis quando elas ajudam, e alternativas para os elementos interativos que dependem dele ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)). Scripts falham por rede lenta, bloqueio, erro em outro script ou navegador antigo. Com a melhoria progressiva, a pessoa ainda lê, navega e envia formulários.

**Prefira o comportamento nativo do HTML.** Acordeões e seções recolhíveis usam `<details>` e `<summary>`; o atributo `name` faz um grupo com uma seção aberta por vez, como no rodapé. Formulários enviam por `<form>` e validam no servidor. Links de navegação são `<a href>` que funcionam com o script desligado.

**Esconda só depois que o script assume.** Conteúdo que o script vai recolher fica visível no HTML. O script, ao iniciar, adiciona a classe `tr-js` ao `<html>`, oculta o conteúdo e cria os controles. O GOV.UK faz o mesmo com uma classe adicionada por script, exigida pelos componentes com comportamento em JavaScript ([GOV.UK](https://design-system.service.gov.uk/styles/page-template/)). Um botão que só funciona com script é criado pelo script, ou fica oculto até ele rodar.

> **Divergência entre referências** O gov.br avisa que, com JavaScript desligado, o site e os componentes podem não funcionar corretamente ([gov.br](https://www.gov.br/ds/guias/navegadores-suportados)). O HDS exige JavaScript para garantir a funcionalidade completa e indica um guia de alternativa sem script ([HDS](https://hds.hel.fi/getting-started/developer)), e o cabeçalho do DKFDS precisa de JavaScript para funcionar ([DKFDS](https://designsystem.dk/komponenter/header/)). O GOV.UK adota a melhoria progressiva como princípio de acessibilidade ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)). O Trama segue o GOV.UK (critério 2): conteúdo, navegação e envio funcionam sem script, e o JavaScript melhora o resto.

### Estrutura do código

**Uma classe por componente.** Cada componente é definido pela própria classe, com prefixo e nome do componente, como `BRHeader` no gov.br ([gov.br](https://www.gov.br/ds/guias/construcao-de-componentes)). No Trama, o prefixo é `Tr`: `TrHeader`, `TrTabs`. O construtor recebe o elemento raiz e, quando há muitas opções, um objeto de configuração com valores padrão ([gov.br](https://www.gov.br/ds/guias/codificacao-javascript)).

**Uma instância por ocorrência.** Procure todas as ocorrências do componente na página e crie uma instância para cada uma, para que cada cópia funcione no próprio escopo; guarde as referências para usá-las depois ([gov.br](https://www.gov.br/ds/guias/codificacao-javascript)). Não inicie a mesma ocorrência duas vezes; componentes inseridos depois do carregamento são iniciados um a um ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/hent-kodepakken/)).

**Ofereça um método para desmontar.** Em aplicações com frameworks, inicie os componentes no momento de montagem e limpe as instâncias na desmontagem, para evitar vazamento de memória ([gov.br](https://www.gov.br/ds/como-comecar/fluxo-dev)). Todo componente do Trama com script tem `destroy()`, que remove ouvintes e devolve o HTML ao estado inicial.

**Use métodos privados de verdade.** O gov.br marca métodos de uso interno com sublinhado no início, uma convenção que não impede o acesso ([gov.br](https://www.gov.br/ds/guias/codificacao-javascript)). O Trama usa campos e métodos privados da linguagem (`#nome`), que impedem o acesso externo.

**Não dependa de bibliotecas.** O kit usa JavaScript puro, sem bibliotecas de terceiros, como o DKFDS, para evitar dependência de fornecedores e dívida técnica ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/frameworks/)).

``` code
/** Exemplo fora do kit. Seção recolhível: botão que mostra e oculta um painel. */
class TrDisclosure {
  static contador = 0;
  #botao; #painel;

  constructor(raiz) {
    this.raiz = raiz;
    this.#painel = raiz.querySelector('.tr-disclosure__painel');
    this.#painel.id ||= `tr-disclosure-${++TrDisclosure.contador}`;
    this.#botao = document.createElement('button');
    this.#botao.type = 'button';
    this.#botao.className = 'tr-btn tr-btn--subtle';
    this.#botao.textContent = raiz.dataset.rotulo;
    this.#botao.setAttribute('aria-controls', this.#painel.id);
    this.#botao.setAttribute('aria-expanded', 'false');
    this.#painel.hidden = true;
    this.#botao.addEventListener('click', this.#alternar);
    raiz.prepend(this.#botao);
  }

  #alternar = () => {
    const aberto = this.#botao.getAttribute('aria-expanded') === 'true';
    this.#botao.setAttribute('aria-expanded', String(!aberto));
    this.#painel.hidden = aberto;
  };

  destroy() {
    this.#botao.removeEventListener('click', this.#alternar);
    this.#botao.remove();
    this.#painel.hidden = false;
  }
}

document.documentElement.classList.add('tr-js');
const disclosures = [...document.querySelectorAll('.tr-disclosure')]
  .map((raiz) => new TrDisclosure(raiz));
```

Sem script, o painel fica visível e não existe botão sem função. Com script, o botão é criado com os estados corretos.

### Atributos acessíveis gerados

**Gere `aria-expanded` e `aria-controls` no script.** Nos utilitários de acordeão, recolhível e dropdown do gov.br, o acionador recebe `aria-expanded` e `aria-controls`, e o alvo recebe `hidden`, todos gerados pelo JavaScript ([gov.br](https://www.gov.br/ds/utilitarios/js/collapse)). O Trama faz o mesmo: quem escreve o HTML não declara esses atributos, porque eles só são verdadeiros quando o script está ativo. Menus com submenus usam o padrão de divulgação do guia de práticas de autoria do WAI-ARIA, com `aria-expanded` e `aria-controls` ([DKFDS](https://designsystem.dk/komponenter/header/)).

**Mantenha o estado num só lugar.** O atributo ARIA é o estado: o CSS o lê para a aparência e o script o lê para decidir a próxima ação. Não guarde uma cópia em variável ou em classe que possa ficar diferente.

**Anuncie mudanças com regiões vivas.** Conteúdo que muda sem mudar de página, como resultados filtrados e confirmações, vai numa região com `role="status"` ou `aria-live="polite"` que já existe no HTML antes da mudança. Erros que exigem atenção imediata usam `role="alert"`.

### Sobreposições: foco e Esc

**Prenda o foco em sobreposições modais.** Em diálogos modais, drawers modais e menus em tela cheia, Tab e Shift+Tab circulam só dentro da sobreposição, e a página por trás fica inerte. O utilitário de véu do gov.br oferece essas duas opções, prender o Tab e fechar com Esc, desligadas por padrão ([gov.br](https://www.gov.br/ds/utilitarios/js/scrim)). No Trama, elas são sempre ligadas em sobreposições modais, sem configuração. O elemento `<dialog>` aberto com `showModal()` já torna o resto da página inerte.

**Feche com Esc.** Esc fecha a sobreposição mais recente: diálogo, drawer, menu, popover, tooltip e a pesquisa expandida do cabeçalho. Se houver alterações não salvas, Esc abre o alerta de alterações não salvas (D22).

**Ponha e devolva o foco.** Ao abrir, siga a regra de foco inicial (D13). Ao fechar, devolva o foco ao elemento que abriu a sobreposição; o foco nunca se perde depois que uma interface temporária fecha ([Fluent](https://fluent2.microsoft.design/accessibility)).

**Não abra nada por hover.** Menus e submenus abrem por clique, toque ou teclado ([HDS](https://hds.hel.fi/components/header/accessibility)). Tooltips são a exceção: aparecem com hover e com foco, e somem com Esc.

### Qualidade

Use o ESLint. O gov.br valida o código com um conjunto de regras que inclui, entre outras, proibir `console` exceto `warn` e `error`, `alert`, `eval` e `var`, e exigir `const` quando a variável não é reatribuída ([gov.br](https://www.gov.br/ds/guias/codificacao-javascript)). O Trama adota essas regras e documenta as classes com comentários JSDoc, como o gov.br ([gov.br](https://www.gov.br/ds/guias/codificacao-javascript)). Use `console.warn` para avisar sobre recursos depreciados; veja Versões e migração. Nunca use `alert()`, `confirm()` ou `prompt()` como interface: use diálogos.

### Considerações por plataforma

#### Web desktop

Trate teclado e mouse juntos: um componente que responde a clique também responde a Enter ou Espaço quando focado, o que botões e links nativos já fazem.

#### Web móvel

Use eventos de ponteiro (`pointerdown`, `pointerup`), que cobrem toque, mouse e caneta. Não dependa de gestos sem alternativa por botão (WCAG 2.2, 2.5.1). Em redes lentas, a página precisa ser útil antes de o script carregar.

#### Tablets e dobráveis

Escute mudanças de tamanho com `ResizeObserver` ou `matchMedia` nos limites das classes de janela, e preserve estado, foco e texto digitado quando o dobrável abre ou fecha.

### Recursos

#### Relacionados

- Construir componentes
- HTML acessível e WAI-ARIA
- Navegadores e dispositivos suportados
- Diálogos
- Foco e seleção
- Teclado

#### Referências

- [Codificação JavaScript](https://www.gov.br/ds/guias/codificacao-javascript) gov.br DS
- [Construção de componentes](https://www.gov.br/ds/guias/construcao-de-componentes) gov.br DS
- [Utilitário Collapse](https://www.gov.br/ds/utilitarios/js/collapse) gov.br DS
- [Utilitário Scrim](https://www.gov.br/ds/utilitarios/js/scrim) gov.br DS
- [Fluxo de desenvolvimento](https://www.gov.br/ds/como-comecar/fluxo-dev) gov.br DS
- [Navegadores suportados](https://www.gov.br/ds/guias/navegadores-suportados) gov.br DS
- [Accessibility strategy](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) GOV.UK Design System
- [Page template](https://design-system.service.gov.uk/styles/page-template/) GOV.UK Design System
- [Hent kodepakken](https://designsystem.dk/kom-i-gang/implementering-kode/hent-kodepakken/) DKFDS
- [Frameworks](https://designsystem.dk/kom-i-gang/implementering-kode/frameworks/) DKFDS
- [Header](https://designsystem.dk/komponenter/header/) DKFDS
- [Getting started as a developer](https://hds.hel.fi/getting-started/developer) Helsinki Design System
- [Header: accessibility](https://hds.hel.fi/components/header/accessibility) Helsinki Design System
- [Accessibility](https://fluent2.microsoft.design/accessibility) Fluent 2

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## Navegadores e dispositivos suportados

O Trama define o suporte por critérios: quais motores de navegador, quais recursos da plataforma web e quais combinações de dispositivo e tecnologia assistiva cada versão precisa atender.

Uma lista de versões mínimas envelhece rápido e não diz nada sobre leitores de tela, ampliação ou dobráveis. Por isso o Trama declara uma política própria, baseada em critérios verificáveis. Ela vale para o kit; cada produto pode ampliá-la conforme o público, com dados reais de uso.

### O que as referências declaram

Os números abaixo servem só como referência. Eles não são a política do Trama.

| Sistema   | O que declara                                                                                                                                                                                                                                                                                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gov.br DS | Versões mínimas: Chrome 49, Edge 14, Firefox 67 e Safari 11, com preferência pelas mais novas. Não recomenda Internet Explorer em nenhuma versão nem o Edge antigo e avisa que, com JavaScript desligado, o site e os componentes podem não funcionar ([gov.br](https://www.gov.br/ds/guias/navegadores-suportados)).                                           |
| DKFDS     | Lista navegadores por sistema, sem versões: Chrome, Edge e Firefox no Windows; Chrome, Safari e Firefox no Mac; Safari e Chrome no iOS; Chrome e Samsung Internet no Android. Diz que a lista é informativa e não é requisito; cada solução define o próprio suporte ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/browserunderstoettelse/)). |
| GOV.UK    | Testa cada componente com combinações registradas de navegador e tecnologia assistiva, incluindo leitores de tela, ampliadores, modos de alto contraste e reconhecimento de fala ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)).                                                                                        |

> **Divergência entre referências** O gov.br fixa versões mínimas; o DKFDS lista navegadores sem versões e não os trata como requisito; o GOV.UK define o suporte pelos testes com tecnologias assistivas. O Trama não publica números de versão: define critérios de motor, de recurso e de teste, que se atualizam sozinhos com o tempo (critérios 2 e 4). Quem precisa de uma lista fechada para contrato deriva-a destes critérios na data da entrega.

### Critérios do Trama

**Três motores.** O kit funciona nos três motores de renderização em uso: Blink, Gecko e WebKit. O gov.br observa que o mercado se reduziu a esses três, que ainda podem desenhar alguns elementos de forma particular, sobretudo em formulários ([gov.br](https://www.gov.br/ds/guias/boas-praticas-de-css)).

**Versões que recebem atualização.** Estão no suporte completo as versões estáveis de Chrome, Edge, Firefox, Safari e Samsung Internet que ainda recebem atualizações de segurança do fabricante, em desktop e em celular. Versões sem atualização de segurança recebem o suporte básico descrito abaixo.

**Recursos amplamente disponíveis.** O kit usa no essencial só recursos da plataforma web classificados como "amplamente disponíveis" no Baseline, a classificação que acompanha quando um recurso funciona em todos os navegadores principais ([web.dev](https://web.dev/baseline)). Recursos mais novos entram só como melhoria, com alternativa: se não houver suporte, o componente continua usável. Por exemplo, o kit usa `color-mix()` na camada de hover; sem ele, o componente perde só o realce.

**Internet Explorer fora do suporte.** Nenhuma versão do Internet Explorer nem do Edge antigo é suportada, como no gov.br ([gov.br](https://www.gov.br/ds/guias/navegadores-suportados)). O Internet Explorer não entende propriedades personalizadas de CSS, das quais todos os tokens dependem.

### Níveis de suporte

| Nível       | Para quem                                                         | O que se garante                                                                                                                                            |
|-------------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Completo    | Navegadores dos critérios acima                                   | Aparência, comportamento e acessibilidade como documentados. Defeitos são corrigidos.                                                                       |
| Básico      | Navegadores antigos, JavaScript desligado ou falho, CSS bloqueado | Conteúdo legível, links e formulários funcionando, ordem lógica. A aparência pode ser simples. Esse nível decorre da melhoria progressiva; veja JavaScript. |
| Sem suporte | Internet Explorer, Edge antigo                                    | Nenhuma garantia.                                                                                                                                           |

### Tecnologias assistivas e modos do sistema

Cada componente é testado em todas as combinações abaixo antes de entrar numa versão. As combinações seguem o uso mais comum de cada sistema; o GOV.UK também registra as combinações que testa ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)).

| Sistema      | Combinações                                                                                                                                                |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows      | NVDA com Chrome e com Firefox; JAWS com Chrome ou Edge; modo de alto contraste; reconhecimento de fala                                                     |
| macOS        | VoiceOver com Safari; ampliação do sistema                                                                                                                 |
| iOS e iPadOS | VoiceOver com Safari; tamanho de texto ampliado; teclado físico no iPad                                                                                    |
| Android      | TalkBack com Chrome; Samsung Internet em aparelhos Galaxy, incluindo dobráveis                                                                             |
| Todos        | Só teclado; zoom do navegador em 200% (WCAG 2.2, 1.4.4); refluxo em 320px de largura CSS (WCAG 2.2, 1.4.10); `prefers-reduced-motion`; tema claro e escuro |

**Teste também à mão.** Validadores automáticos não bastam: o eMAG pede validação manual depois da automática ([gov.br](https://www.gov.br/ds/guias/acessibilidade-html)), e um estudo do GDS encontrou cerca de 30% dos problemas com ferramentas automáticas ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)).

### Dispositivos

O Trama não lista modelos de aparelho. Projete para tamanhos de tela, sem supor dispositivos ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)). O suporte cobre:

- todas as classes de janela, da Compacta à Extragrande;
- entrada por toque, mouse, trackpad, caneta e teclado físico, em qualquer combinação;
- mudança de classe durante o uso, como ao girar o aparelho ou abrir um dobrável;
- janelas divididas e redimensionadas no desktop e no tablet.

### Boas práticas para produtos

**Use dados de acesso do seu público.** Antes de restringir o suporte, veja quais navegadores e aparelhos o público usa de fato. Serviços públicos atendem pessoas com aparelhos antigos e redes lentas, e o nível básico precisa funcionar para elas.

**Não bloqueie navegadores.** Não detecte o navegador para negar acesso. Detecte o recurso e ofereça a alternativa.

**Peça a versão mais recente sem exigir.** Recomende atualizar o navegador ([gov.br](https://www.gov.br/ds/guias/navegadores-suportados)), sem impedir o uso de quem não pode.

### Considerações por plataforma

#### Web desktop

Teste em Windows e macOS, nos três motores. Inclua o modo de alto contraste do Windows, que substitui cores e pode esconder bordas e anéis de foco desenhados só com sombra.

#### Web móvel

No iOS e no iPadOS, os navegadores em geral usam o WebKit; teste no Safari. No Android, teste no Chrome e, em aparelhos Samsung, no Samsung Internet, que o DKFDS também lista ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/browserunderstoettelse/)).

#### Tablets e dobráveis

Teste com teclado físico em tablets e em dobráveis Galaxy Z Fold e Z Flip, fechados e abertos, passando de uma classe de janela para outra durante uma tarefa. Veja Projetar para tablets e dobráveis.

### Recursos

#### Relacionados

- JavaScript
- CSS e tokens no código
- HTML acessível e WAI-ARIA
- Acessibilidade
- Projetar para tablets e dobráveis
- Versões e migração

#### Referências

- [Navegadores suportados](https://www.gov.br/ds/guias/navegadores-suportados) gov.br DS
- [Boas práticas de CSS](https://www.gov.br/ds/guias/boas-praticas-de-css) gov.br DS
- [Acessibilidade no código HTML](https://www.gov.br/ds/guias/acessibilidade-html) gov.br DS
- [Browserunderstøttelse](https://designsystem.dk/kom-i-gang/implementering-kode/browserunderstoettelse/) DKFDS
- [Accessibility strategy](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) GOV.UK Design System
- [Layout](https://design-system.service.gov.uk/styles/layout/) GOV.UK Design System
- [Baseline](https://web.dev/baseline) web.dev

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## Versões e migração

O Trama numera versões com versionamento semântico, avisa antes de remover qualquer coisa e publica um guia de migração para cada mudança que exige trabalho dos produtos.

Produtos que usam o Trama precisam saber, antes de atualizar, se a nova versão vai quebrar algo. Esta página define o que cada número de versão promete, como um recurso é depreciado e removido e o que mudou da versão 1.0 para a 1.1, que integra o Padrão Digital de Governo.

### Versionamento semântico

O Trama segue o versionamento semântico, no formato `MAIOR.MENOR.CORREÇÃO`, como o HDS ([HDS](https://hds.hel.fi/getting-started/versioning)). Uma versão que quebra compatibilidade aumenta o primeiro número, como na passagem de 5.x.x para 6.0.0 no GOV.UK Frontend ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)).

| Número           | Quando muda                                                                                                            | O que o produto precisa fazer                                                       |
|------------------|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Maior (2.0.0)    | Há ao menos uma mudança que quebra compatibilidade.                                                                    | Seguir o guia de migração.                                                          |
| Menor (1.1.0)    | Novos componentes, tokens, classes, variações ou diretrizes, sem quebrar o que existe. Recursos podem ser depreciados. | Nada obrigatório no código. Revisar as diretrizes novas e os avisos de depreciação. |
| Correção (1.1.1) | Correção de defeito que não muda nomes nem remove funções.                                                             | Atualizar.                                                                          |

#### O que quebra compatibilidade

O Trama adota os critérios do HDS, que separam design e implementação ([HDS](https://hds.hel.fi/getting-started/versioning)).

|        | Quebra (versão maior)                                                                                                                                                                                                | Não quebra                                                                                                                                                                  |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Design | Remover um componente; mudar a largura de um componente a ponto de levar elementos vizinhos para outra linha; mudar tipografia de estilos existentes; mudar espaço externo (margens); mudar o valor de tokens de cor | Mudar a estrutura interna sem remover partes; mudar espaçamento interno mantendo o tamanho externo; mudar raio de borda; mudar a cor dentro do componente; mudar a elevação |
| Código | Remover ou renomear classes, atributos, tokens ou parâmetros; mudar o modelo de caixa de forma que altere alinhamento ou largura; exigir versão nova de uma dependência                                              | Acrescentar classes, tokens ou opções; corrigir defeitos sem renomear nem remover; marcar algo como depreciado                                                              |

Para o Trama, também quebra compatibilidade mudar o `id` de uma página da documentação, porque produtos e outras páginas apontam para ele.

### Suporte e depreciação

**Duas versões maiores com suporte.** O Trama corrige defeitos na versão maior atual e na anterior, como o HDS ([HDS](https://hds.hel.fi/getting-started/versioning)). Versões mais antigas não recebem correções.

**Deprecie antes de remover.** Marcar um recurso como depreciado não quebra nada; a quebra só acontece quando ele é removido ([HDS](https://hds.hel.fi/getting-started/versioning)). O gov.br manteve componentes marcados como obsoletos ou depreciados, como o Accordion e o Scrim, na lista de compatíveis da migração para a versão 3 ([gov.br](https://www.gov.br/ds/guias/migracao-2x-3x)). No Trama, um recurso depreciado:

1.  recebe a marca "Depreciado" na página, com a alternativa e a versão em que sai;
2.  emite `console.warn` em ambiente de desenvolvimento, quando tem script;
3.  continua funcionando até a próxima versão maior, no mínimo;
4.  sai numa versão maior, listado no guia de migração.

### Guias de migração e notas de versão

Cada versão maior tem um guia de migração. O guia começa por um resumo do que verificar primeiro, como faz o HDS ([HDS](https://hds.hel.fi/getting-started/tutorials/migrate-to-6.0.0)), e traz, como o guia do gov.br da versão 2 para a 3 ([gov.br](https://www.gov.br/ds/guias/migracao-2x-3x)):

- dependências que mudam;
- componentes compatíveis, depreciados e removidos;
- nomes de arquivos, classes e tokens que mudaram, com o antes e o depois;
- mudanças na forma de iniciar componentes com script, com exemplo de código antes e depois.

O gov.br publica notas de versão separadas para os repositórios de design (diretrizes, modelos, kits de interface) e de desenvolvimento (núcleo, Web Components, React) ([gov.br](https://www.gov.br/ds/release-notes)). O Trama registra as mudanças em dois lugares: no histórico de cada página, para quem acompanha um componente, e nesta página, para a visão do sistema.

### Da 1.0 para a 1.1

A versão 1.1 integra o Padrão Digital de Governo (gov.br DS) a todo o sistema. Toda página foi revisada à luz do gov.br e das outras referências, e as regras em conflito foram reavaliadas por um critério de decisão em ordem: evidência, acessibilidade, contexto brasileiro e convergência. Cada decisão fica registrada na página em que se aplica, numa nota "Divergência entre referências".

A 1.1 é uma versão menor: acrescenta tokens, classes, páginas e diretrizes e não remove nem renomeia nenhuma classe, token ou `id` de página. A camada de hover dos componentes mudou de cor dentro do próprio componente, o que não quebra compatibilidade pelos critérios acima.

#### Decisões transversais

| Tema        | Decisões                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Escrita     | Caixa de frase em títulos, botões e rótulos (D1). Confirmações dizem o que mudou, sem "com sucesso" (D2). Erros nunca culpam a pessoa e não usam humor (D6). Vocabulário controlado: "Pesquisar", "Baixar", "Excluir", "Entrar", "Sair", "Continuar" (D7). Unidades por extenso em texto corrido (D21). "Você", parágrafos de até quatro linhas, rótulos de ação curtos (D24).                                    |
| Formulários | Aceitar qualquer formato digitado e nunca bloquear caracteres (D3). Ordem dos botões por contexto (D4). Regras de senha (D5). Nunca desabilitar o botão de envio (D9).                                                                                                                                                                                                                                            |
| Interação   | Chevron no fim em acordeões e no início em árvores (D8). Elemento desabilitado só quando a pessoa pode habilitá-lo, com explicação (D9). Hover e pressionado como camada de opacidade, um ativo por vez (D10). Foco só em `:focus-visible` e foco tênue para foco movido pelo sistema (D12). Regras de foco inicial (D13). Links na mesma aba e aviso de site externo (D14). Truncamento só onde permitido (D15). |
| Visual      | Três densidades (D11). Body de 16px e mínimo de 12px (D16). Alvo de toque de 44px (D17). Largura fixa e fluida (D18). Espaçamento fino restrito e margens que não se somam (D19). Controle explícito de movimento (D20). Camadas `--z-0` a `--z-4` (D26). Fundo invertido com `.tr-inverse` (D27).                                                                                                                |
| Componentes | No máximo duas ações em diálogos (D22). Só toasts informativos somem sozinhos, após no mínimo 7 segundos (D23).                                                                                                                                                                                                                                                                                                   |
| Legislação  | Meta WCAG 2.2 AA; Estatuto da Pessoa com Deficiência e LGPD para o público brasileiro; Lei nº 14.129/2021 e eMAG para órgãos públicos (D25).                                                                                                                                                                                                                                                                      |

#### Novidades no kit

Tokens de opacidade (`--o-*`), camadas (`--z-*`), ícones (`--icon-*`), densidade (`--d-*` e `[data-density]`) e espaços de formulário (`--f-gap-*`). Classes novas: `.tr-inverse`, `.tr-focus-subtle`, `.tr-header`, `.tr-footer`, `.tr-skiplinks`, `.tr-carousel`, `.tr-timepicker`, `.tr-calendar`, `.tr-table-bar`, `.tr-scroll`, `.tr-link--external`, `.tr-mark`, `.tr-truncate`, `.tr-progress-ring`, `.tr-region-busy`, entre outras, além de variações de diálogo, switch, etapas e estados de validação em campos.

#### Páginas novas e renomeadas

- **Novas**: Como começar, Padrão mínimo, Estados de interação, Densidade, Legislação e normas, Ilustração, Excesso de conteúdo, Estruturar a navegação, Modelos de página, Consentimento de cookies, Coletar feedback, Cabeçalho, Rodapé, Links de pular, Carrossel e a seção Desenvolvimento inteira.
- **Renomeadas**: "Campo de busca" passa a "Campo de pesquisa", e "Busca" passa a "Pesquisa" (D7). Os `id` continuam `campo-busca` e `busca`.
- **Conteúdo movido**: os casos de página não encontrada, serviço indisponível e problema no serviço saem de Estados vazios e vão para Modelos de página.

#### Como migrar um produto da 1.0

1.  Atualize `kit.css`. Nenhuma classe mudou de nome.
2.  Troque rótulos fora do vocabulário controlado: "Buscar" por "Pesquisar", "Fazer download" por "Baixar", "Deletar" por "Excluir" (D7).
3.  Revise títulos, botões e abas em caixa alta ou com iniciais maiúsculas e passe-os para caixa de frase (D1).
4.  Reabilite botões de envio desabilitados e valide ao enviar (D9).
5.  Tire "com sucesso" e exclamações das confirmações (D2) e revise mensagens de erro (D6).
6.  Revise máscaras de campo que bloqueiam digitação (D3).
7.  Troque `z-index` numéricos pelos tokens `--z-*` (D26) e cores fixas de rodapés escuros por `.tr-inverse` (D27).
8.  Acrescente links de pular, cabeçalho e rodapé conforme Modelos de página.

### Considerações por plataforma

#### Web desktop

Nenhuma consideração adicional para Web desktop.

#### Web móvel

Na 1.1, a densidade baixa passa a ser obrigatória em toque e na classe Compacta (D11). Confira telas de celular depois de migrar.

#### Tablets e dobráveis

Nenhuma consideração adicional para Tablets e dobráveis.

### Recursos

#### Relacionados

- Como começar: design e desenvolvimento
- Construir componentes
- CSS e tokens no código
- Navegadores e dispositivos suportados
- Legislação e normas

#### Referências

- [Migração da versão 2.x para 3.x](https://www.gov.br/ds/guias/migracao-2x-3x) gov.br DS
- [Release Notes](https://www.gov.br/ds/release-notes) gov.br DS
- [Versioning](https://hds.hel.fi/getting-started/versioning) Helsinki Design System
- [Migrate to 6.0.0](https://hds.hel.fi/getting-started/tutorials/migrate-to-6.0.0) Helsinki Design System
- [Accessibility strategy](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) GOV.UK Design System

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

