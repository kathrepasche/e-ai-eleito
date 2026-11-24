# Slider

Um slider é um trilho com um controle deslizante que ajusta um valor entre um mínimo e um máximo.

Conforme o valor muda, a parte do trilho entre o mínimo e o controle se preenche de cor ([Apple](https://developer.apple.com/design/human-interface-guidelines/sliders)). Para ajustar, a pessoa arrasta o controle, clica num ponto do trilho para levar o controle até ali ou usa as setas do teclado ([Blueprint](https://blueprintjs.com/docs/#core/components/sliders)). No Trama, o slider (`.tr-slider`) usa o `<input type="range">` nativo, com `accent-color` em `--t-brand`.

O Padrão Digital de Governo não tem um componente de slider; ele aparece só como exemplo de escala de satisfação no padrão de ajuda e comunicação ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Por isso, o Trama aplica ao slider as regras transversais do gov.br: densidade e área mínima de ação, estados e formato de números.

**Quando usar.** Para valores aproximados num intervalo, em que a posição relativa importa mais que a precisão: opacidade, zoom, volume, faixa de preço num filtro ([Geist](https://vercel.com/geist/slider)). O efeito pode ser imediato, como num ajuste de brilho, ou valer só ao enviar o formulário ([Fluent](https://fluent2.microsoft.design/components/web/react/core/slider/usage)).

**Quando não usar.** Para valores exatos, como um valor em reais ou uma quantidade, use o campo numérico ([Fluent](https://fluent2.microsoft.design/components/web/react/core/slider/usage)). Evite sliders para intervalos muito pequenos, em que radios ou um controle segmentado mostram todas as opções, ou muito grandes, em que cada pixel salta muitos valores ([Fluent](https://fluent2.microsoft.design/components/web/react/core/slider/usage)).

## Anatomia

1.  **Rótulo** (`.tr-label`): diz o que o intervalo representa.
2.  **Trilho**: a faixa do mínimo ao máximo. A parte já percorrida fica em `--t-brand`.
3.  **Controle**: o ponto que a pessoa arrasta.
4.  **Valor atual**: texto ao lado do trilho, em números tabulares.
5.  **Marcas e rótulos de limite** (opcionais): pontos fixos ao longo do trilho e os valores das extremidades.
6.  **Ícones de extremidade** (opcionais): imagens que ilustram o mínimo e o máximo, como uma imagem pequena e uma grande num controle de tamanho ([Apple](https://developer.apple.com/design/human-interface-guidelines/sliders)).
7.  **Campo numérico** (opcional): para digitar o valor exato.

## Tipos

| Tipo      | Uso                                                                                                                                                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Contínuo  | Qualquer valor aproximado num trilho sem marcas, como brilho ([Fluent](https://fluent2.microsoft.design/components/web/react/core/slider/usage)). Mesmo assim, tem um passo que evita valores com muitas casas decimais. |
| Em passos | O trilho é dividido em valores discretos e o controle se encaixa no mais próximo ([Fluent](https://fluent2.microsoft.design/components/web/react/core/slider/usage)).                                                    |
| Intervalo | Dois controles definem um mínimo e um máximo, como faixa de preço ([Blueprint](https://blueprintjs.com/docs/#core/components/sliders)).                                                                                  |
| Com campo | Slider mais campo numérico, para quem prefere digitar ([Geist](https://vercel.com/geist/slider)).                                                                                                                        |

## Boas práticas

**Siga a direção esperada.** No slider horizontal, o mínimo fica na borda inicial e o máximo na final; no vertical, o mínimo embaixo e o máximo em cima ([Apple](https://developer.apple.com/design/human-interface-guidelines/sliders)). Em idiomas da direita para a esquerda, a borda inicial é a direita. Veja Internacionalização.

**Prefira o slider horizontal.** É o formato que as pessoas reconhecem para um ponto inicial e final fixos ([Apple](https://developer.apple.com/design/human-interface-guidelines/sliders)). Use o vertical só quando o valor tiver leitura vertical natural, como nível.

**Mostre o valor atual o tempo todo.** O trilho sozinho não diz o número; exiba-o ao lado, em números tabulares, com a unidade ([Geist](https://vercel.com/geist/slider)). Um tooltip com o valor durante o arraste é aceitável se também chegar ao leitor de tela ([Fluent](https://fluent2.microsoft.design/components/web/react/core/slider/usage)).

**Ofereça um campo para valores exatos.** Quando o intervalo é amplo, as pessoas querem ver o número e poder digitá-lo ([Apple](https://developer.apple.com/design/human-interface-guidelines/sliders)). Quem usa teclado tende a digitar ([Geist](https://vercel.com/geist/slider)). Sincronize os dois: mover o slider atualiza o campo, e digitar move o slider ao sair do campo.

**Use um passo sensato e limites reais.** Encaixe em passos como 1, 5 ou 10% para que o arraste nunca gere valores como 47,83291, e limite mínimo e máximo ao que o produto suporta ([Geist](https://vercel.com/geist/slider)).

**Use marcas para dar escala.** Marcas ajudam a entender a medida e a localizar valores. Rotule só o mínimo e o máximo na maioria dos casos; em escalas não lineares, rotule pontos intermediários ([Apple](https://developer.apple.com/design/human-interface-guidelines/sliders)).

**Dê retorno ao vivo quando o efeito for visível.** Ver o resultado durante o arraste ajuda a acertar o valor ([Apple](https://developer.apple.com/design/human-interface-guidelines/sliders)). Se o efeito for caro, como uma consulta ao servidor, aplique quando a pessoa soltar o controle ([Blueprint](https://blueprintjs.com/docs/#core/components/sliders)).

**Garanta área de ação suficiente.** O controle deslizante tem área de ação de pelo menos 24px com mouse e `--c-touch` em toque; a área pode ultrapassar o círculo visível ([gov.br](https://www.gov.br/ds/padroes/design/densidade)). Em toque e na classe Compacta, use a densidade baixa para o campo numérico acompanhante e deixe o trilho com a largura do contêiner.

**Formate os números como no Brasil.** Use vírgula decimal e ponto como separador de milhar no valor exibido, como “1.250,5” ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). No campo acompanhante, aceite o número com ou sem separadores e com a unidade digitada, e normalize ao sair do campo, sem bloquear caracteres.

**Use as mesmas faixas de alerta do resto do produto.** Se o slider muda de cor acima de um limite, use o mesmo limite que aparece em outras partes da interface ([Geist](https://vercel.com/geist/slider)).

**Faça** slider para um ajuste aproximado, com o valor visível.

**Não faça** slider para valor exato num intervalo enorme, sem mostrar o número.

### Estados e teclado

| Tecla                              | Efeito                            |
|------------------------------------|-----------------------------------|
| Seta para a direita ou para cima   | Aumenta um passo                  |
| Seta para a esquerda ou para baixo | Diminui um passo                  |
| Page Up e Page Down                | Aumenta ou diminui um passo maior |
| Home e End                         | Vai ao mínimo ou ao máximo        |

Deixe o comportamento nativo do teclado funcionar e não intercepte essas teclas ([Geist](https://vercel.com/geist/slider)).

| Estado        | Aparência                                                                                                                                            |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hover         | Camada `--o-hover` em volta do controle, só com ponteiro                                                                                             |
| Foco          | Anel de 2px `--t-focus` no controle, em `:focus-visible`                                                                                             |
| Arrastando    | Valor visível acima do controle ou ao lado do trilho                                                                                                 |
| Erro e alerta | No campo acompanhante, com a mensagem acima dele, como no campo de texto; o slider não tem estado de erro próprio                                    |
| Desabilitado  | Trilho e controle em `--t-fg-disabled`. Só quando a pessoa pode habilitá-lo por uma ação dela, com o motivo ao lado; caso contrário, retire o slider |

> **Divergência entre referências** *Escala de satisfação:* o gov.br mostra sliders como exemplo de escala de satisfação; o Fluent desaconselha sliders para intervalos muito pequenos, em que radios mostram todas as opções. Pelo critério de convergência e de acessibilidade (cada nota da escala tem um rótulo próprio e visível), o Trama usa radios em linha (`.tr-scale`) para escalas de satisfação e reserva o slider para valores aproximados num intervalo contínuo.

## Conteúdo

**Rótulo.** Curto, dizendo o que o intervalo representa ([Fluent](https://fluent2.microsoft.design/components/web/react/core/slider/usage)). Inclua a unidade por extenso no rótulo: “Raio da pesquisa, em quilômetros”. No valor ao lado do trilho, uma abreviação curta é aceitável quando o rótulo já nomeia a unidade.

**Escalas não numéricas.** Use termos paralelos nas extremidades, como “Baixo” e “Alto” ou “Mínimo” e “Máximo” ([Fluent](https://fluent2.microsoft.design/components/web/react/core/slider/usage)).

**Formato.** Formate o valor conforme o idioma, com vírgula decimal e ponto de milhar em português ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). Use `aria-valuetext` com a unidade por extenso: “2,5 gigabytes”.

## Acessibilidade

- Todo slider tem rótulo, mesmo quando visualmente oculto ([Fluent](https://fluent2.microsoft.design/components/web/react/core/slider/usage)). Use `<label for>` ou `aria-label` ([Geist](https://vercel.com/geist/slider)).
- Garanta que rótulo e valor atual sejam anunciados ([Fluent](https://fluent2.microsoft.design/components/web/react/core/slider/usage)). Use `aria-valuetext` quando o número sozinho não fizer sentido, como “60 por cento” ou “Médio”.
- No slider de intervalo, dê a cada controle um nome próprio: “Preço mínimo” e “Preço máximo”.
- Arrastar não pode ser a única forma de ajustar: o teclado e o clique no trilho também funcionam, e o campo numérico oferece uma alternativa de um só ponto de contato (WCAG 2.2, 2.5.7).
- O controle precisa de contraste de 3:1 com o trilho e o fundo (WCAG 2.2, 1.4.11).

## Tokens usados

| Elemento                     | Token                                          |
|------------------------------|------------------------------------------------|
| Trilho preenchido e controle | `--t-brand`                                    |
| Trilho vazio                 | `--t-surface-2` com borda `--t-border-control` |
| Largura máxima               | 320px no `.tr-slider`                          |
| Valor atual                  | `.tr-mono`, `--t-fg-1`                         |
| Rótulos de limite            | Caption 12/16, `--t-fg-3`                      |
| Espaço entre slider e valor  | `--sp-300`                                     |
| Foco                         | `--t-focus`                                    |
| Área de ação do controle     | 24px com mouse; `--c-touch` em toque           |
| Hover                        | `--o-hover`                                    |

## Considerações por plataforma

### Web desktop

Mostre o valor do controle num tooltip quando o ponteiro estiver sobre ele ([Apple](https://developer.apple.com/design/human-interface-guidelines/sliders)). Permita clicar no trilho para saltar ao ponto clicado. A rolagem da roda do mouse não deve alterar o valor, para evitar mudanças acidentais ao rolar a página.

### Web móvel

Com o dedo sobre o controle, o valor fica escondido; mostre-o acima do controle durante o arraste ou ao lado do trilho. Garanta área de toque de `--c-touch` no controle e deixe o trilho com a largura do contêiner. Prefira o slider horizontal: o gesto lateral não conflita com a rolagem vertical da página.

### Tablets e dobráveis

Em janelas expandidas, limite a largura do trilho para que o arraste não exija atravessar a tela. Num dobrável aberto, não deixe o trilho cruzar a dobra.

## Recursos

### Relacionados

- Campo numérico e stepper
- Controle segmentado
- Indicadores de progresso
- Toque e gestos
- Coletar feedback
- Densidade

### Referências

- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Ajuda e comunicação](https://www.gov.br/ds/padroes/design/ajuda-comunicacao) gov.br DS
- [Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders) Apple HIG
- [Slider](https://fluent2.microsoft.design/components/web/react/core/slider/usage) Fluent 2
- [Slider](https://vercel.com/geist/slider) Geist
- [Sliders](https://blueprintjs.com/docs/#core/components/sliders) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo, que não tem componente de slider. Acrescenta área mínima de ação, estados, formato brasileiro de números, unidades por extenso e a decisão de usar radios em escalas de satisfação. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                       |
