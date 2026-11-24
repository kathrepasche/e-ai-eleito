# LinksDePular

Links de pular deixam quem navega pelo teclado saltar direto para o conteúdo principal e para as outras regiões da página.

Muitas pessoas usam a tecla Tab para percorrer links e campos. Sem atalho, elas passam por todo o cabeçalho e pela navegação em cada página antes de chegar ao conteúdo ([GOV.UK](https://design-system.service.gov.uk/components/skip-link/), [gov.br](https://www.gov.br/ds/templates/base)). Os links de pular resolvem isso: ficam ocultos até o primeiro Tab e levam a pessoa à região escolhida. No Trama, o componente é o `.tr-skiplinks`, um grupo de links que pode ter vários destinos.

**Quando usar.** Em todas as páginas ([gov.br](https://www.gov.br/ds/components/skiplink), [DKFDS](https://designsystem.dk/komponenter/skip-link/), [GOV.UK](https://design-system.service.gov.uk/components/skip-link/)). Eles atendem ao critério de contornar blocos repetidos (WCAG 2.2, 2.4.1).

**Quando não usar.** Para outras formas de navegação dentro do conteúdo ([DKFDS](https://designsystem.dk/komponenter/skip-link/)). Um índice de seções de uma página longa é outro componente; veja Estruturar a navegação.

## Anatomia

1.  **Superfície**: fundo `--t-fg-1`, invertido em relação à página, para se destacar sobre qualquer cabeçalho.
2.  **Links**: um elemento `<a>` por destino, com texto em `--t-bg` e sublinhado.
3.  **Anel de foco**: 2px em `--t-bg`, porque o anel padrão em `--t-focus` não teria contraste sobre a superfície escura.

## Tipos

| Tipo            | Uso                                                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Destino único   | Um link, "Pular para o conteúdo principal". Páginas com cabeçalho simples ([GOV.UK](https://design-system.service.gov.uk/components/skip-link/), [DKFDS](https://designsystem.dk/komponenter/skip-link/)).  |
| Vários destinos | De dois a quatro links, para conteúdo, navegação, pesquisa e rodapé. Páginas com navegação extensa, pesquisa no cabeçalho ou rodapé com mapa do site ([gov.br](https://www.gov.br/ds/components/skiplink)). |

## Boas práticas

**Ponha os links de pular antes de tudo.** Eles são o primeiro elemento focável da página, logo depois da abertura do `<body>`. A única exceção é o banner de cookies, que vem antes ([GOV.UK](https://design-system.service.gov.uk/components/skip-link/), [DKFDS](https://designsystem.dk/komponenter/skip-link/), [gov.br](https://www.gov.br/ds/components/skiplink)). Não os coloque dentro do cabeçalho ([GOV.UK](https://design-system.service.gov.uk/components/skip-link/)).

**O primeiro link sempre leva ao conteúdo principal.** Os demais seguem a ordem das regiões na página: navegação, pesquisa, rodapé. Cada destino é um landmark ou o início de um: `<main>`, `<nav>`, a região com `role="search"` e `<footer>` ([gov.br](https://www.gov.br/ds/components/skiplink)).

**Use no máximo quatro destinos.** O gov.br limita o tipo composto a quatro itens ([gov.br](https://www.gov.br/ds/components/skiplink)). Se a página parece pedir mais, simplifique a estrutura da página.

**Mostre todos os destinos juntos quando o grupo recebe foco.** O grupo aparece no primeiro Tab, continua visível enquanto qualquer link dele tem foco e volta a ficar oculto quando o foco sai ([gov.br](https://www.gov.br/ds/components/skiplink)). Esc também o oculta ([gov.br](https://www.gov.br/ds/components/skiplink)). Nunca use estado desabilitado num link de pular ([gov.br](https://www.gov.br/ds/components/skiplink)).

**Mova o foco para o destino.** Ao acionar o link, o foco vai para o destino, e o próximo Tab continua dali. Dê `tabindex="-1"` ao destino que não é focável por natureza, como o `<main>`. O GOV.UK passou a mover o foco por script para tornar o comportamento dos leitores de tela mais consistente ([GOV.UK](https://design-system.service.gov.uk/components/skip-link/)).

**Confira que todos os destinos existem.** Cada `href` aponta para um `id` presente na página ([gov.br](https://www.gov.br/ds/templates/base)). Se a página não tem pesquisa, o link "Pular para a pesquisa" não aparece.

> **Divergência entre referências** O gov.br atribui `accesskey` numérico a cada link e sugere agrupá-los em `<nav>` com lista ([gov.br](https://www.gov.br/ds/components/skiplink)). O próprio gov.br alerta que essas teclas podem conflitar com as combinações nativas de cada navegador, e a HIG pede respeitar os atalhos padrão ([HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards)). O GOV.UK pede não envolver o link de pular numa região `<nav>` ([GOV.UK](https://design-system.service.gov.uk/components/skip-link/)). O Trama não usa `accesskey` e não cria landmark para o grupo (critério 2). O gov.br também tem um tipo simples, que mostra um destino por vez no mesmo lugar com a contagem "(1/4)"; o Trama mostra todos os destinos de uma vez, para que a pessoa veja as opções sem precisar percorrê-las. Por fim, o HDS trata o link de pular como opcional, recomendado quando o cabeçalho tem mais que a barra de ações ([HDS](https://hds.hel.fi/components/header)); o Trama o exige em todas as páginas, como gov.br, GOV.UK e DKFDS (critério 4).

**Faça** textos curtos que dizem o destino, começando pelo conteúdo principal.

**Não faça** atalhos de tecla que conflitam com o navegador, ordem trocada e texto sem destino.

## Conteúdo

Use textos curtos e diretos ([gov.br](https://www.gov.br/ds/components/skiplink)), no formato "Pular para" seguido da região: "Pular para o conteúdo principal", "Pular para a navegação", "Pular para a pesquisa", "Pular para o rodapé". O gov.br usa "Pular para o conteúdo principal" como exemplo de linguagem clara ([gov.br](https://www.gov.br/ds/components/skiplink)). Não inclua números de tecla no texto.

## Acessibilidade

**Oculte visualmente sem remover do teclado.** Use uma técnica de ocultação que mantém o link focável, como a do `.tr-visually-hidden`, revertida em `:focus-within` no grupo. `display:none` e `visibility:hidden` tiram o link da ordem de tabulação. O GOV.UK oferece uma classe que torna visível ao receber foco um elemento oculto ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)).

**Teste com teclado e leitor de tela.** Verifique que o primeiro Tab mostra o grupo, que cada link leva ao destino certo e que Enter aciona o link ([gov.br](https://www.gov.br/ds/components/skiplink)). Ferramentas automáticas podem avisar que o link de pular está fora de um landmark; esse aviso não se aplica a ele ([GOV.UK](https://design-system.service.gov.uk/components/skip-link/)).

**Cuidado com a âncora no endereço.** Depois de usar o link de pular, o endereço ganha a âncora do destino, e páginas seguintes podem pular direto para o conteúdo sem que a pessoa espere. O GOV.UK recebeu retornos mistos sobre esse efeito ([GOV.UK](https://design-system.service.gov.uk/components/skip-link/)). O Trama não carrega a âncora para a próxima página.

**Estruture a página com landmarks.** Os links de pular dependem de uma página bem marcada: `<header>`, `<nav>`, `<main>` e `<footer>` ([gov.br](https://www.gov.br/ds/components/skiplink)). Veja HTML acessível e WAI-ARIA.

``` code
<body>
  <!-- banner de cookies, se houver -->
  <div class="tr-skiplinks">
    <a href="#conteudo">Pular para o conteúdo principal</a>
    <a href="#navegacao">Pular para a navegação</a>
    <a href="#rodape">Pular para o rodapé</a>
  </div>
  <header class="tr-header">…</header>
  <nav id="navegacao" aria-label="Principal" tabindex="-1">…</nav>
  <main id="conteudo" tabindex="-1">…</main>
  <footer id="rodape" tabindex="-1">…</footer>
</body>
```

## Tokens usados

| Token                  | Uso                                              |
|------------------------|--------------------------------------------------|
| `--t-fg-1`             | Superfície do grupo                              |
| `--t-bg`               | Texto dos links e anel de foco                   |
| `--sp-100`, `--sp-200` | Espaçamento interno dos links e do grupo         |
| `--r-md`, `--r-sm`     | Cantos do grupo e dos links                      |
| `--z-4`                | Camada do grupo visível, acima do cabeçalho fixo |

## Considerações por plataforma

### Web desktop

Mostre o grupo no canto superior inicial da página, sobre o cabeçalho, na camada `--z-4`, para que o cabeçalho fixo não o cubra. O gov.br coloca o componente na camada 4 de elevação ([gov.br](https://www.gov.br/ds/components/skiplink)).

### Web móvel

Teclados físicos e leitores de tela também são usados no celular. Mantenha os links de pular; na classe Compacta, o grupo quebra em linhas e cada link mantém área de `--c-touch`.

### Tablets e dobráveis

Tablets com teclado físico usam Tab como no desktop. Nenhuma outra consideração para dobráveis.

## Recursos

### Relacionados

- Cabeçalho
- Rodapé
- Modelos de página: base e erro
- Teclado
- Foco e seleção
- HTML acessível e WAI-ARIA

### Referências

- [Skip Link (Atalhos Acessíveis)](https://www.gov.br/ds/components/skiplink) gov.br DS
- [Template Base](https://www.gov.br/ds/templates/base) gov.br DS
- [Skip link](https://design-system.service.gov.uk/components/skip-link/) GOV.UK Design System
- [Layout](https://design-system.service.gov.uk/styles/layout/) GOV.UK Design System
- [Gå til sidens indhold (Skip-link)](https://designsystem.dk/komponenter/skip-link/) DKFDS
- [Header (Header.SkipLink)](https://hds.hel.fi/components/header) Helsinki Design System
- [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards) Apple HIG

## Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |
