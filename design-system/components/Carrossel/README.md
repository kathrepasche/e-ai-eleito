# Carrossel

Um carrossel mostra vários conteúdos no mesmo espaço da tela, um de cada vez, e a pessoa avança e volta por eles em sequência e no ritmo dela.

O carrossel economiza espaço quando há uma sequência de itens e a pessoa só precisa se concentrar em um ou poucos por vez ([gov.br DS](https://www.gov.br/ds/components/carousel)). Ele pode ficar numa página, num drawer ou num diálogo, e sua navegação é independente do resto da página ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/carousel/usage)).

O componente também é polêmico. O gov.br lembra que testes do Nielsen Norman Group mostram que as pessoas desenvolvem "cegueira" para conteúdo rotativo e que carrosséis são frequentemente ignorados ([gov.br DS](https://www.gov.br/ds/components/carousel)). Por isso, o Trama trata o carrossel como um recurso de apoio: nenhuma informação necessária para a tarefa fica só dentro dele.

## Quando usar

- Para uma sequência curta de itens do mesmo tipo em um espaço reduzido, como destaques de serviços, depoimentos ou fotos de um local ([gov.br DS](https://www.gov.br/ds/components/carousel), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/carousel/usage)).
- Para uma galeria de imagens ou vídeos que a pessoa folheia ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/carousel/usage)).
- Para conteúdo de leitura passiva em sequência, como as telas de um onboarding.

## Quando evitar

- **Para um único conteúdo.** Use uma imagem estática ([gov.br DS](https://www.gov.br/ds/components/carousel)).
- **Para informação que todos precisam ver.** Muitas pessoas não chegam às últimas páginas ([gov.br DS](https://www.gov.br/ds/components/carousel)). Deixe a informação visível na página, em cards ou em uma lista.
- **Para mais de cinco itens.** É improvável que a pessoa veja mais de cinco páginas ([gov.br DS](https://www.gov.br/ds/components/carousel)). Use uma grade, que deixa navegar em qualquer ordem ([HIG](https://developer.apple.com/design/human-interface-guidelines/page-controls)).
- **Para conteúdo que a pessoa precisa comparar.** Mostre lado a lado ou em uma tabela.
- **Para etapas de um formulário.** Use formulários em etapas, com "Continuar".
- **Dentro de um card ou de um item de lista.** Componentes de navegação, como carrossel, não vão na área de conteúdo de cards e itens ([gov.br DS](https://www.gov.br/ds/components/card)).

## Anatomia

1.  **Palco (obrigatório).** Área que mostra o conteúdo. Cada conteúdo é uma página ([gov.br DS](https://www.gov.br/ds/components/carousel)). Use `.tr-carousel__viewport`.
2.  **Botões de navegação (obrigatórios).** Anterior e Próximo, circulares, com seta na direção da navegação ([gov.br DS](https://www.gov.br/ds/components/carousel)). Use `.tr-btn--circle`.
3.  **Botão de pausa (obrigatório com reprodução automática).** Alterna entre "Pausar" e "Continuar".
4.  **Indicador de páginas (obrigatório).** Diz quantas páginas existem e qual está à vista ([gov.br DS](https://www.gov.br/ds/components/carousel)). Pode ser simples (pontos, `.tr-carousel__dots`) ou textual ("2 de 5"); o Trama usa os dois juntos.
5.  **Barra de controles.** `.tr-carousel__controls`, abaixo do palco: indicador no início, botões no fim.

> **Divergência entre referências** O gov.br põe os botões de navegação nas laterais, centralizados na altura do palco, de preferência fora dele, e permite colocá-los dentro do palco para economizar espaço ([gov.br DS](https://www.gov.br/ds/components/carousel)). A HIG centraliza o indicador abaixo do conteúdo ([HIG](https://developer.apple.com/design/human-interface-guidelines/page-controls)). O Trama reúne indicador e botões numa barra abaixo do palco. Pelo critério de acessibilidade, os controles nunca ficam sobre a imagem, o que garante o contraste em qualquer conteúdo, e a barra mantém a mesma posição em todas as classes de janela, sem tirar largura do palco na Compacta.

## Tipos

| Tipo                      | Uso                                                                                                                                                                                                                                                                                                      |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simples                   | Uma página por vez. Padrão.                                                                                                                                                                                                                                                                              |
| Múltiplas páginas         | Um bloco de páginas à vista, como cards de produtos. Até três páginas por bloco, com o mesmo espaço entre elas; a navegação avança por bloco ou por página, e cada passo corresponde a um ponto do indicador ([gov.br DS](https://www.gov.br/ds/components/carousel)). Na classe Compacta, vira simples. |
| Galeria                   | Miniaturas no lugar dos pontos, para coleções de imagens ou vídeos ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/carousel/usage)). As miniaturas são botões com alvo de pelo menos 24 px.                                                                                       |
| Com reprodução automática | Avança sozinho em intervalos. Só na web desktop, com botão de pausa sempre visível e navegação circular.                                                                                                                                                                                                 |

## Boas práticas

**Use no máximo cinco páginas.** Mais do que isso cansa e é pouco provável que seja visto ([gov.br DS](https://www.gov.br/ds/components/carousel)). A HIG observa que mais de dez pontos já não se contam de relance ([HIG](https://developer.apple.com/design/human-interface-guidelines/page-controls)); o limite do Trama é menor porque o problema do carrossel é a atenção, antes da contagem.

**Ponha o mais importante na primeira página.** E repita qualquer informação importante em outro lugar do produto, para quem não interage com o carrossel ([gov.br DS](https://www.gov.br/ds/components/carousel)).

**Mantenha as páginas consistentes.** Mesmo tipo de conteúdo e mesmas dimensões em todas as páginas de um carrossel ([gov.br DS](https://www.gov.br/ds/components/carousel)).

**Mostre sempre o indicador.** Saber quantas páginas há e em qual está ajuda a pessoa a se sentir no controle ([gov.br DS](https://www.gov.br/ds/components/carousel)). O indicador textual fica abaixo do palco, nunca dentro dele ([gov.br DS](https://www.gov.br/ds/components/carousel)).

**Ponha texto sobre imagem só com a camada de legibilidade.** Use `--t-overlay-text` e garanta 4,5:1 sob o texto (veja Imagem). O gov.br recomenda essa sobreposição para reforçar o contraste ([gov.br DS](https://www.gov.br/ds/components/carousel)).

### Reprodução automática

**Prefira não usar reprodução automática.** Não use quando não houver certeza de que o tempo basta para a maioria ler e entender, nem quando o conteúdo se parece com anúncio, porque as pessoas tendem a ignorá-lo ([gov.br DS](https://www.gov.br/ds/components/carousel)).

**Ofereça sempre um botão de pausa visível.** A pessoa precisa sempre poder pausar ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/carousel/usage)). No Trama, o botão "Pausar" fica visível o tempo todo, é o primeiro controle do carrossel na ordem de foco e muda para "Continuar" quando pausado. Conteúdo que se move sozinho por mais de cinco segundos exige um mecanismo de pausa (WCAG 2.2, 2.2.2).

**Pause sozinho no hover e no foco.** Enquanto o ponteiro estiver sobre o carrossel ou o foco estiver dentro dele, a rotação para, e volta só quando ele sair, se a pessoa não tiver pausado.

**Não use reprodução automática no celular.** Ela torna a página mais lenta e a troca acontece quando a pessoa já rolou para baixo e não vê ([gov.br DS](https://www.gov.br/ds/components/carousel)). No Trama, a reprodução automática fica desligada na classe Compacta, em qualquer dispositivo de toque, com `prefers-reduced-motion` e quando a pessoa desliga as animações no produto.

**Calcule o tempo de exibição pela quantidade de palavras.** Use três palavras por segundo como base e acrescente o tempo de ver imagens e controles ([gov.br DS](https://www.gov.br/ds/components/carousel)). Uma página com 24 palavras fica pelo menos 8 segundos, mais o tempo da imagem. Páginas com textos diferentes têm tempos diferentes.

**Use navegação circular na reprodução automática.** Não pare na última página; volte à primeira ([gov.br DS](https://www.gov.br/ds/components/carousel)).

> **Divergência entre referências** O gov.br deixa os botões de reprodução invisíveis até que o ponteiro passe sobre o conteúdo ([gov.br DS](https://www.gov.br/ds/components/carousel)). O Fluent exige que a opção de pausar esteja sempre disponível ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/carousel/usage)). Pelo critério de acessibilidade, o Trama mantém o botão de pausa sempre visível: quem usa teclado, toque ou ampliação de tela não passa o ponteiro sobre o palco e não descobriria o controle.

### Navegação e estados

**Use "Anterior" e "Próximo".** O carrossel é um fluxo de leitura passiva, em que o Trama usa "Próximo"; em fluxos de tarefa, o rótulo é "Continuar".

**Sinalize o início e o fim.** Sem reprodução automática, a navegação não é circular: na primeira página, "Anterior" fica com `aria-disabled="true"`, e na última, "Próximo" ([gov.br DS](https://www.gov.br/ds/components/carousel)). Os botões continuam focáveis, e o indicador "1 de 5" ou "5 de 5" explica por que não há para onde ir.

**Aceite gestos no toque, sem depender deles.** No toque, a pessoa desliza o palco para os lados ([gov.br DS](https://www.gov.br/ds/components/carousel)). Os botões continuam visíveis, porque nem todas as pessoas conseguem fazer o gesto, e arrastar não pode ser a única forma de navegar (WCAG 2.2, 2.5.7).

> **Divergência entre referências** No código do gov.br, os botões de navegação ficam ocultos no layout móvel por padrão, e a diretriz diz que com gestos os botões não são necessários, desde que haja alternativa acessível ([gov.br DS](https://www.gov.br/ds/components/carousel)). O Trama mantém os botões em todas as classes de janela, pelo critério de acessibilidade: o gesto de deslizar não está disponível para todas as pessoas nem é descoberto por todas.

**Anime a troca com deslizamento rápido.** A página entra e sai deslizando, em duração rápida ([gov.br DS](https://www.gov.br/ds/components/carousel)): `--m-normal` com `--m-ease-standard`. Com movimento reduzido, a troca é instantânea.

| Estado                    | Regra                                                                     |
|---------------------------|---------------------------------------------------------------------------|
| Página atual              | Ponto em `--t-brand` com `aria-current="true"` e texto "2 de 5".          |
| Hover e foco nos botões   | Camada `--o-hover`; anel `--t-focus` em `:focus-visible`.                 |
| Primeira ou última página | Botão correspondente com `aria-disabled="true"`, focável.                 |
| Reproduzindo, pausado     | Botão "Pausar" ou "Continuar"; pausa por hover e foco não troca o rótulo. |
| Carregando                | Palco com skeleton na proporção final.                                    |

**Faça** deixe o botão de pausa sempre visível e diga quantas páginas há.

**Não faça** reprodução automática sem pausa, com oito páginas e só pontos como indicador.

## Conteúdo

- Escreva frases curtas em cada página: quanto menos palavras, menos tempo a pessoa precisa e mais fácil é calcular a duração.
- Dê ao carrossel um título visível que diga o que reúne, como "Novidades dos serviços".
- Use texto HTML sobre a imagem, nunca texto gravado na imagem.
- Crie variações da imagem para cada classe de janela, com recortes que mantêm a informação principal, e entregue-as com `<picture>` e `<source>` ([gov.br DS](https://www.gov.br/ds/components/carousel)).
- Rótulos de controle: "Anterior", "Próximo", "Pausar" e "Continuar". Ações dentro de uma página têm verbo e objeto, com até duas palavras.

## Acessibilidade

**Estruture o carrossel com WAI-ARIA.** O contêiner é uma `<section>` com `aria-roledescription="carrossel"` e nome pelo título (`aria-labelledby`). Cada página é um elemento com `role="group"`, `aria-roledescription="página"` e `aria-label="2 de 5"`. Os botões têm nome em texto ("Anterior", "Próximo") e `aria-controls` apontando para o palco.

``` code
<section aria-roledescription="carrossel" aria-labelledby="tit">
  <h2 id="tit">Novidades dos serviços</h2>
  <button type="button">Pausar</button>
  <div id="palco" aria-live="off">
    <div role="group" aria-roledescription="página" aria-label="2 de 5">…</div>
  </div>
  <button type="button" aria-controls="palco">Anterior</button>
  <button type="button" aria-controls="palco">Próximo</button>
</section>
```

**Anuncie a troca só quando a pessoa a provocou.** O palco tem `aria-live="polite"` enquanto a navegação é manual e `aria-live="off"` durante a reprodução automática, para não interromper o leitor de tela a cada troca. Avisos sem texto visível ajudam quem usa leitor de tela a perceber mudanças que os demais veem pela animação ([HDS](https://hds.hel.fi/components/notification)).

**Teclado.** Tab e Shift+Tab percorrem os controles e os elementos interativos da página visível; Enter e Espaço acionam ([gov.br DS](https://www.gov.br/ds/components/carousel)). Páginas ocultas ficam fora da ordem de foco e da árvore de acessibilidade (`hidden` ou `inert`). Ao trocar de página, o foco fica no botão acionado.

**Movimento.** Respeite `prefers-reduced-motion` e o controle de animações do produto: sem reprodução automática e com troca instantânea (WCAG 2.2, 2.3.3). Tenha cuidado com a velocidade da transição ([gov.br DS](https://www.gov.br/ds/components/carousel)).

**Alvos e indicadores.** Botões têm alvo de `--c-touch` no toque ([gov.br DS](https://www.gov.br/ds/components/carousel)). Os pontos do indicador são pequenos demais para serem alvos; no Trama, eles são decorativos (`aria-hidden="true"`), e a mesma função existe nos botões e no indicador textual, o que atende à exceção de controle equivalente do WCAG 2.2, 2.5.8.

**Mídia acessível.** Imagens têm texto alternativo e vídeos têm legendas ([gov.br DS](https://www.gov.br/ds/components/carousel)). O carrossel se ajusta ao zoom de 400% sem perder conteúdo ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/carousel/usage)).

## Tokens usados

| Elemento                          | Token                                             |
|-----------------------------------|---------------------------------------------------|
| Raio do palco                     | `--r-lg`                                          |
| Camada de legibilidade            | `--t-overlay-text`                                |
| Texto sobre a imagem              | 16/22, peso 600, branco; preenchimento `--sp-400` |
| Espaço entre palco e controles    | `--sp-300`                                        |
| Pontos: inativo, atual            | `--t-border-control`, `--t-brand`                 |
| Espaço entre pontos, entre botões | `--sp-200`                                        |
| Botões circulares                 | `--c-h-md`; no toque, alvo `--c-touch`            |
| Transição                         | `--m-normal`, `--m-ease-standard`                 |
| Foco                              | `--t-focus`, `--stroke-thick`                     |

## Considerações por plataforma

### Web desktop

É a única plataforma em que a reprodução automática é permitida, com pausa visível e pausa no hover e no foco. Os controles não aparecem só no hover. Carrosséis de múltiplas páginas mostram até três páginas por bloco.

### Web móvel

Sem reprodução automática ([gov.br DS](https://www.gov.br/ds/components/carousel)). Na classe Compacta, o carrossel ocupa a largura total, o conteúdo se ajusta de 600 a 320 px e imagens e vídeos mantêm a proporção ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/carousel/usage)). Gesto de deslizar e botões convivem. Carrosséis de múltiplas páginas viram simples ([gov.br DS](https://www.gov.br/ds/components/carousel)).

### Tablets e dobráveis

Sem reprodução automática, porque são dispositivos de toque. Em janelas médias, use blocos de até duas páginas; em expandidas, até três. Em dobráveis abertos, não deixe os botões sobre a dobra ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)), e ao abrir ou fechar o aparelho mantenha a página atual.

## Recursos

### Relacionados

- Imagem
- Cards
- Onboarding
- Movimento
- Toque e gestos
- Paginação

### Referências

- [Carousel](https://www.gov.br/ds/components/carousel) gov.br DS
- [Card](https://www.gov.br/ds/components/card) gov.br DS
- [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls) Apple HIG
- [Carousel](https://fluent2.microsoft.design/components/web/react/core/carousel/usage) Fluent 2
- [Notification](https://hds.hel.fi/components/notification) Helsinki Design System
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |
