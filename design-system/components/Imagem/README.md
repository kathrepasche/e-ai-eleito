# Imagem

O componente de imagem exibe uma foto, ilustração ou gráfico estático com proporção, recorte, legenda e texto alternativo controlados.

Uma imagem só entra na interface quando ajuda a entender algo ou a concluir uma tarefa. O texto da página precisa conter toda a informação necessária; a imagem é um apoio visual ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Esta página trata do componente que exibe a imagem. Para direção de arte, fotografia e formatos de arquivo, veja o fundamento Imagens.

Imagens do componente não são interativas. Se a imagem precisa disparar uma ação, coloque-a dentro de um botão ou de um link e dê ao controle um nome acessível ([HIG](https://developer.apple.com/design/human-interface-guidelines/image-views)).

## Quando usar

- Para mostrar algo concreto de forma realista, como a prévia de um documento enviado ([GOV.UK](https://design-system.service.gov.uk/styles/images/)).
- Para simplificar algo complexo com uma ilustração, como onde achar um número de referência em um documento ([GOV.UK](https://design-system.service.gov.uk/styles/images/)).
- Como mídia de um card ou de um cabeçalho de página de entrada.

## Quando não usar

- **Para decorar.** Evite imagens sem necessidade real ([GOV.UK](https://design-system.service.gov.uk/styles/images/)).
- **Para representar conceitos abstratos**, como "sinergia" ou "confiança", e para fotos genéricas de banco de imagens ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).
- **Para mostrar texto.** Escreva o texto na página. Imagens de texto não se ajustam a zoom, cor ou leitura em voz alta (WCAG 2.2, 1.4.5).
- **Para ícones de interface.** Use a biblioteca de ícones, que acompanha cor e tamanho do texto ([HIG](https://developer.apple.com/design/human-interface-guidelines/image-views)).

## Anatomia

1.  **Contêiner.** Define a proporção e reserva o espaço antes do carregamento.
2.  **Imagem.** O arquivo, ajustado ao contêiner por preenchimento ou contenção.
3.  **Texto alternativo.** Atributo `alt`, presente em toda imagem, mesmo vazio.
4.  **Legenda (opcional).** Texto visível abaixo da imagem em `<figcaption>`.
5.  **Crédito (opcional).** Autoria ou licença, junto da legenda.

## Tipos

| Tipo                        | Uso                                                                                                                                                                                         |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fotografia                  | Representação fiel de algo real: um documento, um local, um produto.                                                                                                                        |
| Ilustração                  | Simplificação de algo complexo, com poucos elementos, cores chapadas e traços consistentes entre as ilustrações do produto ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). |
| Miniatura                   | Versão reduzida em listas e cards, com recorte fixo.                                                                                                                                        |
| Imagem com texto sobreposto | Faixas de página de entrada e páginas de carrossel. Exige a camada de legibilidade descrita abaixo.                                                                                         |
| Placeholder                 | Substitui uma imagem ausente em listagens ou a prévia de uma imagem ainda não enviada ([HDS](https://hds.hel.fi/foundation/visual-assets/placeholders)).                                    |

O Trama define quatro proporções: 1:1 (miniaturas e perfis), 4:3 (uso geral), 16:9 (fotos amplas) e 2:1 (faixas e cabeçalhos). Todas estão entre as proporções recomendadas pelo Ontario para imagens ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

## Boas práticas

**Reserve o espaço da imagem.** Declare largura e altura (ou a proporção do contêiner) para que o conteúdo não salte quando a imagem carregar. Enquanto carrega, mostre `--t-surface-2` ou um skeleton no mesmo tamanho.

**Escolha entre preencher e conter.** Preencha (recortando as bordas) em fotos decorativas de cards e cabeçalhos. Contenha (sem recorte) em documentos, diagramas e qualquer imagem em que perder a borda significa perder informação.

**Adapte a imagem a cada classe de janela.** Crie variações da mesma imagem para cada resolução, com recortes que mantêm a informação principal, e entregue-as com `<picture>` e `<source>` ([gov.br DS](https://www.gov.br/ds/components/carousel)).

**Entregue a resolução certa.** Forneça versões em alta densidade para telas de alta resolução e teste em dispositivos reais, porque uma imagem que parece boa no projeto pode ficar pixelada ou esticada ([HIG](https://developer.apple.com/design/human-interface-guidelines/images)). Use `srcset` e `sizes` para que o navegador escolha o arquivo.

**Use vetores para ilustrações e diagramas.** SVG mantém linhas e textos nítidos com zoom ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Fotos vão em JPEG ou formatos modernos equivalentes, comprimidos antes da publicação ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

**Evite texto sobre imagem.** Texto sobre foto perde legibilidade e a foto perde clareza. Se for inevitável, use texto HTML, nunca texto gravado na imagem, e garanta contraste de 4,5:1 com todas as partes da imagem que ficam sob o texto, em todos os tamanhos de tela ([HIG](https://developer.apple.com/design/human-interface-guidelines/image-views), [GOV.UK](https://design-system.service.gov.uk/styles/images/)).

### Camada de legibilidade

**Ponha uma camada escura entre a imagem e o texto.** O gov.br chama essa sobreposição de scrim de legibilidade e a aplica parcial ou totalmente sobre o elemento ([gov.br DS](https://www.gov.br/ds/components/scrim)). No Trama, a camada é o token `--t-overlay-text`: um gradiente transparente no topo que chega a preto opaco na base. O texto fica na parte inferior, sobre a região mais escura, em branco e com pelo menos Body (16 px). Quando o texto precisa ficar em outra posição ou ocupar a imagem inteira, use uma camada uniforme de `--t-overlay` e meça o contraste no ponto mais claro sob o texto.

> **Divergência entre referências** O gov.br especifica o scrim de legibilidade como preto com 64% de opacidade uniforme ([gov.br DS](https://www.gov.br/ds/components/scrim)). A HIG e o GOV.UK pedem só que o contraste seja garantido em toda a área sob o texto ([HIG](https://developer.apple.com/design/human-interface-guidelines/image-views), [GOV.UK](https://design-system.service.gov.uk/styles/images/)). Pelo critério de acessibilidade, o Trama usa o gradiente `--t-overlay-text`, que escurece até o preto opaco sob o texto e dá mais margem de contraste que 64% uniformes, deixando o resto da foto visível. A regra que vale é a medição: 4,5:1 no ponto mais claro sob o texto.

### Outros usos de scrim

O gov.br descreve mais dois tipos de scrim ([gov.br DS](https://www.gov.br/ds/components/scrim)). O **scrim de foco** escurece o restante da tela para destacar um elemento novo, como um diálogo; no Trama, ele é o véu `--t-overlay` de diálogos e drawers, na camada abaixo de `--z-4`. O **scrim de inibição** cobre uma área para simular que ela está desativada; o Trama não adota esse uso, porque os elementos sob a camada continuam ativos para teclado e leitor de tela, como o próprio gov.br alerta. Para áreas que carregam, use `.tr-region-busy` com `aria-busy`; para controles indisponíveis, siga as regras de desabilitado.

**Use o raio do contêiner.** Imagens soltas usam `--r-lg`. Dentro de um card, a imagem herda o raio superior do card. Avatares são circulares e têm componente próprio, o avatar.

**Faça** descreva o que a imagem informa no contexto: a rampa de acesso importa para quem vai ao local.

**Não faça** começar com "Imagem de" nem repetir o título que já está na página ([GOV.UK](https://design-system.service.gov.uk/styles/images/)).

### Estados e comportamento

- **Carregando.** Contêiner com `--t-surface-2` e proporção final. Carregue sob demanda (`loading="lazy"`) imagens fora da primeira dobra.
- **Erro ou ausente.** Mostre um placeholder neutro do mesmo tamanho. Não amplie um placeholder pequeno; use o tamanho mais próximo acima ([HDS](https://hds.hel.fi/foundation/visual-assets/placeholders)).
- **Ampliação.** Quando a pessoa precisar ver detalhes, ofereça um botão "Ampliar imagem" que abre a versão completa em tela cheia.

## Conteúdo

- Escreva o texto alternativo com a informação que a imagem dá, de forma específica e concisa, em no máximo duas frases, com pontuação normal ([GOV.UK](https://design-system.service.gov.uk/styles/images/), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/image/usage)).
- Não inclua o nome do fotógrafo nem informação que não está na imagem.
- Se a imagem representa uma função, descreva a função ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/image/usage)).
- Use a legenda para contexto que todos devem ver, como a fonte de um mapa ou a data de uma foto.

## Acessibilidade

**Toda imagem tem atributo `alt`.** Deixe-o vazio (`alt=""`) em imagens decorativas, em ícones ao lado de um rótulo de texto e em imagens dentro de links cujo texto já explica o destino ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Atende ao WCAG 2.2, 1.1.1.

**Não repita texto da página no `alt`.** O leitor de tela anunciaria a mesma informação duas vezes ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/image/usage)).

**Imagens complexas pedem descrição longa visível.** Para diagramas e mapas, escreva um `alt` curto e uma descrição completa na página ou atrás de um link visível ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Para dados, veja Gráficos.

**Agrupe imagem e legenda.** Use `<figure>` e `<figcaption>` para que a relação seja exposta às tecnologias assistivas.

**Animações respeitam a preferência de movimento.** GIFs e sequências animadas param com `prefers-reduced-motion` e oferecem controle de pausa quando duram mais de cinco segundos (WCAG 2.2, 2.2.2).

## Tokens usados

| Elemento                                              | Token                                       |
|-------------------------------------------------------|---------------------------------------------|
| Fundo de carregamento e placeholder                   | `--t-surface-2`                             |
| Raio de imagem solta                                  | `--r-lg`                                    |
| Contorno opcional em imagens claras sobre fundo claro | `--t-border-subtle`, `--stroke-thin`        |
| Legenda                                               | Caption 12/16, `--t-fg-3`                   |
| Espaço entre imagem e legenda                         | `--sp-200`                                  |
| Camada de legibilidade sob texto                      | `--t-overlay-text`; uniforme: `--t-overlay` |
| Foco em imagem dentro de link                         | `--t-focus`, `--stroke-thick`               |

## Considerações por plataforma

### Web desktop

Dimensione imagens pela grade: em 12 colunas, imagens 4:3 ocupam em geral 4 colunas e imagens 2:1, 6 colunas ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)). Telas de alta densidade são comuns em notebooks; entregue a versão 2x.

### Web móvel

Imagens ocupam a largura útil da coluna. Evite imagens pequenas demais para mostrar detalhes importantes em celular ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)) e imagens altas que empurram o conteúdo principal para baixo. Sirva arquivos menores para economizar dados.

### Tablets e dobráveis

Ao abrir ou fechar um dobrável, mantenha a posição de rolagem e não recarregue as imagens ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Recalcule `sizes` para cada classe de janela, porque a mesma imagem pode passar de 4 para 8 colunas.

## Recursos

### Relacionados

- Imagens
- Cards
- Carrossel
- Avatar
- Iconografia
- Acessibilidade

### Referências

- [Image views](https://developer.apple.com/design/human-interface-guidelines/image-views) Apple HIG
- [Images](https://developer.apple.com/design/human-interface-guidelines/images) Apple HIG
- [Images](https://design-system.service.gov.uk/styles/images/) GOV.UK Design System
- [Image](https://fluent2.microsoft.design/components/web/react/core/image/usage) Fluent 2
- [Images and photography](https://designsystem.ontario.ca/components/detail/images.html) Ontario Design System
- [Placeholders](https://hds.hel.fi/foundation/visual-assets/placeholders) Helsinki Design System
- [Scrim](https://www.gov.br/ds/components/scrim) gov.br DS
- [Carousel](https://www.gov.br/ds/components/carousel) gov.br DS
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                        |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Entram a camada de legibilidade para texto sobre imagem, os usos de scrim (foco adotado, inibição não adotada) e as variações de imagem por classe de janela. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                 |
