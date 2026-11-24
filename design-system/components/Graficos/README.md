# Graficos

Um gráfico organiza um conjunto de dados em marcas visuais para destacar poucas informações importantes e ajudar as pessoas a decidir.

Gráficos comunicam tendência, comparação e proporção mais rápido do que um texto com números, e são os elementos mais proeminentes de uma tela. Acompanhe todo gráfico com um resumo em texto e com os dados acessíveis.

O Trama trata o gráfico como um componente de conteúdo com três áreas: cabeçalho, área principal e rodapé ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). A escolha do tipo de gráfico e da paleta está no padrão Visualização de dados; esta página define a anatomia, os limites de cada tipo e a acessibilidade.

## Quando usar

- Para mostrar padrões e tendências ou comparar informações ao longo de um período ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).
- Quando a mensagem principal é um padrão, como uma evolução ou uma diferença grande entre grupos ([DKFDS](https://designsystem.dk/komponenter/tables/)).
- Para dar uma visão rápida (um gráfico pequeno) que leva a uma versão detalhada em outra tela ([HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)).

## Quando não usar

- **Para entregar valores exatos que a pessoa precisa consultar, ordenar ou pesquisar.** Use uma tabela ou uma lista ([HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)).
- **Como decoração.** Gráficos que não melhoram a compreensão geram confusão ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/)).
- **Para um único número.** Mostre o número em texto, com rótulo e unidade.

## Anatomia

As áreas podem mudar de ordem conforme a necessidade, mas a área principal é obrigatória ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).

1.  **Cabeçalho: título.** Diz o que o gráfico mede, o recorte e o período.
2.  **Cabeçalho: resumo.** Uma frase com a mensagem principal. A HIG recomenda resumir a informação-chave para que as pessoas a entendam sem examinar os detalhes ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).
3.  **Área principal: plotagem.** Região que contém as marcas. Cada marca representa um valor ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).
4.  **Eixos, marcações e linhas de grade.** Dão o quadro de referência para estimar valores.
5.  **Rótulos e legenda.** Nomeiam séries e valores. Prefira rótulos diretos nas marcas; use legenda quando houver atributos sem relação com a posição, como cor ou forma.
6.  **Rodapé: descrição.** Texto que detalha o que o gráfico mostra, para quem tem dificuldade de interpretar gráficos ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).
7.  **Rodapé: fonte e data.** De onde vêm os dados e quando foram fechados, com link para os dados originais sempre que possível ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).
8.  **Alternativa em dados.** Tabela ou arquivo para baixar com os mesmos valores.

## Tipos

Cada tipo tem limites de quantidade a partir dos quais deixa de ser legível. Acima deles, divida o gráfico, filtre os dados ou use uma tabela.

| Tipo               | Use para                                                                                                                                                                    | Limites e cuidados                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Colunas e barras   | Comparar quantidades por categoria ou período; barras horizontais quando os rótulos são longos e para rankings ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). | Até 10 categorias ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/datavisualisering/)). Espaço entre barras de pelo menos metade da largura da barra; ordene por valor quando a ordem não for temporal; uma cor, com destaque só na barra que importa ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). Eixo em zero. Evite quando a diferença entre valores é pequena ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). |
| Linha e área       | Evolução contínua ao longo do tempo ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).                                                                            | No máximo 3 a 4 linhas por gráfico ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). Não use com intervalos descontínuos. Diferencie séries por traço e marcador, além da cor ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/datavisualisering/)).                                                                                                                                                                                 |
| Pizza e rosca      | Partes de um todo que somam 100%, em um único momento ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).                                                          | Evite sempre que possível. No máximo 7 categorias; não serve para zeros, valores negativos, dados ordinais ou séries temporais, nem para comparar vários conjuntos lado a lado ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). Prefira a rosca e coloque uma tabela junto ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/)).                                                                                                     |
| Histograma         | Distribuição de uma variável em faixas, sem espaço entre as barras ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).                                             | Pelo menos 50 a 100 valores para uma amostra significativa; uma cor, até três para destaque ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).                                                                                                                                                                                                                                                                                                                |
| Dispersão e bolhas | Relação entre duas variáveis; nas bolhas, uma terceira pelo tamanho ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).                                            | Desenhe a bolha pela área, nunca pelo raio; use transparência para mostrar sobreposições e limite a quantidade de bolhas ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). Garanta alvo de interação suficiente.                                                                                                                                                                                                                                             |
| Medidor            | Uma razão de 0 a 100 contra um máximo fixo, como uso de cota.                                                                                                               | Sempre com rótulo visível que nomeia a medida ([Geist](https://vercel.com/geist/gauge)). Para progresso de tarefa, use indicadores de progresso.                                                                                                                                                                                                                                                                                                                        |

## Boas práticas

**Escolha tipos comuns e mantenha o gráfico simples.** Barras e linhas são conhecidas por quase todos; excesso de dados esconde a relação que você quer mostrar, então ofereça filtros quando houver muito a mostrar ([HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)).

**Defina o limite inferior do eixo pelo tipo de marca.** Em barras, use zero para que as alturas sejam comparáveis. Em linhas longe de zero, use um limite dinâmico; use escala fixa quando mínimo e máximo têm significado, como 0% e 100% ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).

**Use sequências familiares nas marcações e dose as linhas de grade.** 0, 5, 10 se lê de relance ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Desenhe grades com `--t-border-subtle` e rótulos de eixo com `--t-fg-3`.

**Mantenha consistência entre gráficos do mesmo conjunto de dados.** Mesmo tipo e mesmas cores sinalizam os mesmos dados ([HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)).

**Use poucas cores e evite combinações problemáticas.** Use poucas famílias de cor; excesso de cores é o erro mais comum ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). Evite pares que se confundem com daltonismo: vermelho e verde, verde e marrom, verde e azul, verde e cinza, verde e preto, azul e cinza, azul e roxo ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). Teste o gráfico com um simulador de daltonismo.

**Arredonde os valores.** Mostre só as casas decimais que mudam a leitura, com o mesmo número de casas em toda a série, ponto de milhar e vírgula decimal.

**Organize gráficos em cards.** Em painéis, cada gráfico fica em um card, com o título do gráfico como título do card, a fonte no rodapé e, se necessário, ações de ampliar, filtrar e aproximar ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). Coloque o indicador mais importante no canto superior esquerdo e agrupe métricas relacionadas ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).

**Faça** rotule cada barra com o nome da categoria e o valor, para que a leitura não dependa de cor nem de legenda.

**Não faça** diferenciar séries só por cor, e evite combinações como verde e vermelho ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/tilgaengelig-grafik/)).

### Estados e comportamento

- **Carregando.** Reserve a área do gráfico com um skeleton do mesmo tamanho. Em gráficos que se atualizam, mostre carregamento enquanto os dados demoram, para que a pessoa saiba que a informação está sendo atualizada ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).
- **Ampliar.** Um botão "Ampliar gráfico" abre o mesmo gráfico maior, em diálogo ou página, com cabeçalho e rodapé ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).
- **Aproximar e filtrar.** Controles de zoom e filtros mudam a área principal sem mudar o tamanho do card, e sempre permitem voltar ao estado anterior ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).
- **Sem dados.** Mostre um estado vazio dentro da área de plotagem, com o motivo e o próximo passo. Não desenhe eixos vazios.
- **Interação.** Permita explorar valores, mas não exija interação para revelar informação crítica ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).
- **Mudança de dados.** Ao atualizar marcas ou eixos, anime com `--m-normal` e `--m-ease-standard` e anuncie a mudança em texto, porque quem usa leitor de tela ou desativa animações não percebe o movimento ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Respeite `prefers-reduced-motion` e o controle do produto para desligar animações; animações de gráfico não são essenciais ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).

## Conteúdo

- Escreva o título como descrição do que é medido: "Pedidos concluídos por canal, setembro de 2026".
- Escreva o resumo como a conclusão, com valores reais. Evite termos subjetivos como "rapidamente" ou "quase"; deixe a pessoa interpretar ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).
- Evite formatos ambíguos: "6 de junho" é mais claro que "6/6" ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Escreva unidades por extenso no título, no resumo e nos rótulos acessíveis; abreviações padronizadas (min, h, d, kB, MB) só nos eixos e em cartões compactos, com a unidade nomeada no título.
- Coloque a unidade no título ou no rótulo do eixo e mantenha os rótulos do eixo vertical curtos.
- Cite a fonte e a data de fechamento dos dados. Quando os dados forem de terceiros, informe publicação, data e direitos e, se possível, link para o original ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).

> **Divergência entre referências** A HIG pede evitar abreviações como "60m" e preferir "60 minutos" ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). O gov.br aceita abreviações como "7d" em painéis, desde que o público as entenda ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). O Trama aplica a decisão D21: por extenso em texto corrido e rótulos acessíveis, abreviações padronizadas só em eixos e cartões compactos, com a unidade nomeada no título.

## Acessibilidade

**Escreva o texto alternativo e a descrição longa.** O texto alternativo diz o tipo de gráfico e o tipo de dado em poucas palavras; muitos leitores de tela cortam textos alternativos em 125 caracteres ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). A descrição longa, visível no rodapé e ligada por `aria-describedby`, diz o tipo de gráfico, o tipo de dado e o propósito, com os valores principais ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). Agrupe gráfico, título e descrição em `<figure>` e `<figcaption>` ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).

**Entregue os dados em texto.** Gráficos acessíveis disponibilizam os dados como texto. Ofereça uma tabela ou uma descrição longa visível para quem enxerga, além do texto alternativo curto ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Prefira gráficos em HTML ou SVG com texto real a imagens rasterizadas ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/)).

**Não dependa só de cor.** Use também forma, padrão, tipo de linha ou rótulo direto (WCAG 2.2, 1.4.1). Separe áreas de cor contíguas com um divisor fino ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Marcas e linhas que carregam significado precisam de contraste de 3:1 com o fundo (WCAG 2.2, 1.4.11). Rotule os dados diretamente em vez de depender de legenda separada: a leitura fica independente da cor e exige menos idas e vindas ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). Quando as cores não bastam, use texturas, formas nos marcadores e espaço em branco entre séries ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).

> **Divergência entre referências** O gov.br sugere trabalhar com contraste a partir de 10:1 quando a preocupação é daltonismo, sem citar estudo ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). O WCAG 2.2 exige 3:1 para elementos gráficos necessários à compreensão (critério 1.4.11). O Trama mantém 3:1 como mínimo obrigatório e exige codificação redundante (rótulo direto, forma ou padrão), que resolve o daltonismo sem depender de diferença de luminosidade entre séries.

**Descreva o que os elementos representam.** Em rótulos acessíveis, nomeie a série, como "Aplicativo, 46%". Esconda dos leitores de tela rótulos de eixo redundantes ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).

**Torne a navegação previsível.** Em gráficos interativos, permita percorrer valores com as setas ao longo do eixo X ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).

**Relacione título e resumo ao gráfico.** Use `aria-labelledby` no título e `aria-describedby` no resumo, como na demonstração. Não use o atributo `longdesc`, obsoleto no HTML atual, embora o gov.br o cite como opção ao lado de `aria-describedby` ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).

**Dê controle sobre a animação.** Gráficos animados oferecem pausa, para pessoas com epilepsia, TDAH ou deficiências cognitivas ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)).

## Tokens usados

| Elemento                                         | Token                                                        |
|--------------------------------------------------|--------------------------------------------------------------|
| Marca da série principal                         | `--t-brand`                                                  |
| Trilho de barra, fundo de área                   | `--t-surface-2`                                              |
| Linhas de grade e separadores entre áreas de cor | `--t-border-subtle`, `--stroke-thin`                         |
| Título                                           | Subtitle 20/28 (`.tr-subtitle`), `--t-fg-1`                  |
| Resumo e rótulos                                 | Body small 14/20, `--t-fg-1` e `--t-fg-2`                    |
| Rótulos de eixo, fonte                           | Caption 12/16, `--t-fg-3`                                    |
| Valores numéricos em tabelas                     | `--t-font-mono` ou algarismos tabulares                      |
| Status (meta, alerta)                            | `--t-success`, `--t-warning`, `--t-danger`, sempre com texto |
| Espaço entre título, gráfico e fonte             | `--sp-300`                                                   |
| Transição de dados                               | `--m-normal`, `--m-ease-standard`                            |

## Considerações por plataforma

### Web desktop

Mostre valores ao passar o ponteiro sobre a área de plotagem e repita o mesmo conteúdo com o foco do teclado. Um tooltip de valor nunca é o único lugar onde o dado aparece.

### Web móvel

Em janelas compactas (abaixo de 600 px), maximize a largura da área de plotagem, encurte os rótulos do eixo vertical e mova a unidade para o título ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Prefira barras horizontais com rótulos acima de cada barra. Use alvos de toque de pelo menos `--c-touch`.

### Tablets e dobráveis

Em layouts de dois painéis, o gráfico pequeno no painel de lista pode abrir a versão completa no painel de detalhe, mantendo o mesmo estilo nas duas versões ([HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)).

## Recursos

### Relacionados

- Visualização de dados
- Tabelas
- Cor
- Acessibilidade
- Indicadores de progresso

### Referências

- [Gráfico](https://www.gov.br/ds/padroes/design/grafico) gov.br DS
- [Charts](https://developer.apple.com/design/human-interface-guidelines/charts) Apple HIG
- [Charting data](https://developer.apple.com/design/human-interface-guidelines/charting-data) Apple HIG
- [Datavisualisering og infografik](https://designsystem.dk/styleguide/datavisualisering-infografik/) DKFDS
- [Tilgængelig grafik](https://designsystem.dk/styleguide/datavisualisering-infografik/tilgaengelig-grafik/) DKFDS
- [Datavisualisering](https://designsystem.dk/styleguide/datavisualisering-infografik/datavisualisering/) DKFDS
- [Tabeller](https://designsystem.dk/komponenter/tables/) DKFDS
- [Images](https://design-system.service.gov.uk/styles/images/) GOV.UK Design System
- [Gauge](https://vercel.com/geist/gauge) Geist

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Entram as três áreas do gráfico, os limites por tipo, as combinações de cor a evitar, a organização em cards com ampliar, aproximar e filtrar, a descrição longa, o controle de animação (D20) e a regra de unidades (D21). |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                               |
