# Padrões: Visualização de dados a Contas e autenticação

## Visualização de dados

Apresente dados em gráficos quando a forma visual ajuda as pessoas a entender uma tendência, um estado ou uma comparação, e garanta que a mesma informação exista em texto e em dados abertos.

Um gráfico comunica informação complexa sem exigir a leitura de muito texto. Use gráficos para três tarefas principais: analisar tendências ao longo do tempo, acompanhar o estado atual de um processo ou de uma quantidade e comparar itens em várias categorias ([HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)). Antes de escolher o tipo, responda três perguntas: qual informação o gráfico precisa transmitir, quantas variáveis ou categorias ele mostra e quem vai lê-lo ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).

Se a pessoa só precisa consultar valores, prefira uma tabela ([HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)). Nunca use gráficos como decoração ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/)). Anatomia, marcas e eixos do componente estão em Gráficos.

### Boas práticas

**Comece pela mensagem.** Escreva em uma frase o que a pessoa deve aprender com o gráfico e use essa frase como título ou subtítulo. Títulos, subtítulos e anotações destacam as conclusões acionáveis ([HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)). Um resumo visível também ajuda pessoas com algumas deficiências cognitivas e usuários de leitores de tela a decidir se vale investigar os detalhes ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).

**Prefira barras e linhas.** Elas são lidas sem aprendizado prévio ([HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)). Teste a legibilidade com pessoas do público ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).

#### Limites por tipo de gráfico

| Tipo             | Use para                                                                                     | Regras do Trama                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Colunas e barras | Comparar quantidades entre categorias, criar rankings, mostrar valores positivos e negativos | Até 10 categorias ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/datavisualisering/)). Espaço entre barras de pelo menos metade da largura da barra. Mostre o valor de cada barra, ordene de forma crescente ou decrescente, nomeie os eixos e use uma cor só, com destaque para a barra que carrega a mensagem. Use barras horizontais quando os nomes das categorias forem longos ([gov.br](https://www.gov.br/ds/padroes/design/grafico)). Evite quando a variação entre os valores for pequena. |
| Linhas e áreas   | Tendências em dados contínuos ao longo do tempo                                              | No máximo 3 a 4 séries por gráfico. Compare séries só quando os eixos usam a mesma escala. Não use para dados sem intervalo contínuo ([gov.br](https://www.gov.br/ds/padroes/design/grafico)). Some pontos sobre a linha para destacar valores individuais ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).                                                                                                                                                                                     |
| Pizza e rosca    | Partes de um todo que somam 100%                                                             | Até 7 categorias. Não use com zeros, valores negativos, dados ordinais, séries temporais ou para comparar vários conjuntos lado a lado. Se usar, prefira a rosca e escreva o percentual em cada fatia ([gov.br](https://www.gov.br/ds/padroes/design/grafico)). Acompanhe com tabela, porque fatias pequenas não comportam rótulos ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/)).                                                                                                               |
| Histograma       | Distribuição de frequências, simetria, picos e valor mais comum                              | Barras sem espaço entre si. Pelo menos 50 a 100 dados para uma amostra significativa. Uma cor, ou de duas a três quando houver destaque. Separe em dois histogramas quando houver dois picos de alta frequência ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).                                                                                                                                                                                                                                                     |
| Dispersão        | Relação entre duas variáveis quantitativas                                                   | Ajuda a identificar agrupamentos e valores fora do padrão ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Diferencie séries por forma do ponto, além da cor ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).                                                                                                                                                                                                                                                                          |
| Bolhas           | Três variáveis numéricas (x, y e tamanho)                                                    | Desenhe o tamanho pela área do círculo, nunca pelo raio ou diâmetro. Use poucas categorias, bolhas translúcidas para revelar sobreposições e variações de um mesmo tom ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).                                                                                                                                                                                                                                                                                              |

> **Divergência entre referências** O DKFDS apresenta o gráfico de setores como opção comum para partes de um todo, com tabela ao lado. O gov.br recomenda evitá-lo sempre que possível e limita o uso a 7 categorias, com dados citados: o olho compara mal ângulos e áreas, categorias abaixo de 5% somem, e 8% da população masculina tem alguma dificuldade em perceber cores. Pelo critério de evidência, o Trama segue o gov.br: prefira barras e use pizza ou rosca só nas condições da tabela. Fontes: [gov.br](https://www.gov.br/ds/padroes/design/grafico), [DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/).

#### Desenho e cor

**Mantenha o gráfico simples e revele detalhes aos poucos,** com níveis de detalhe que a pessoa escolhe ver ([HIG](https://developer.apple.com/design/human-interface-guidelines/charting-data)).

**Defina o limite do eixo de acordo com a marca.** Em barras, comece o eixo vertical em zero. Use intervalo fixo quando mínimo e máximo têm significado, como 0% e 100%, e intervalo dinâmico quando os valores variam muito. Prefira marcações familiares, como 0, 5, 10 ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).

**Use poucas famílias de cor.** O excesso de cores é o erro mais comum em gráficos. Reserve uma cor vibrante para o dado que reforça a mensagem e evite escalas monocromáticas com muitos tons ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).

**Nunca comunique significado só pela cor.** Combine cor com forma do ponto, padrão de preenchimento, tipo de linha (contínua, tracejada, pontilhada), espaço em branco entre séries ou rótulo direto. O gráfico deve continuar legível em preto e branco ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/tilgaengelig-grafik/), [gov.br](https://www.gov.br/ds/padroes/design/grafico)). Prefira rótulos diretos sobre os dados a uma legenda separada: a pessoa não precisa casar cores e reduz o vaivém do olhar ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).

**Evite pares de cor que pessoas com daltonismo confundem.** Não coloque lado a lado vermelho e verde, verde e marrom, verde e azul, verde e cinza, verde e preto, azul e cinza, azul e roxo, nem verde-claro e amarelo ([gov.br](https://www.gov.br/ds/padroes/design/grafico), [DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/tilgaengelig-grafik/)).

**Separe áreas de cor contíguas.** Em barras empilhadas, use um separador de `--stroke-thin` na cor `--t-bg` entre segmentos ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Marcas e cores adjacentes precisam de contraste de pelo menos 3:1 (WCAG 2.2, 1.4.11) e textos de 4,5:1 (WCAG 2.2, 1.4.3).

> **Divergência entre referências** O gov.br considera 4,5:1 suficiente na maioria dos casos e sugere trabalhar a partir de 10:1 quando o público inclui pessoas com daltonismo. DKFDS e HIG pedem redundância visual além da cor. O Trama exige os mínimos da WCAG (3:1 entre marcas, 4,5:1 em texto) e busca a margem extra por redundância: forma, padrão ou rótulo direto. Um contraste de 10:1 entre todas as cores vizinhas reduziria a paleta a poucos pares. Fontes: [gov.br](https://www.gov.br/ds/padroes/design/grafico), [DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/tilgaengelig-grafik/), [HIG](https://developer.apple.com/design/human-interface-guidelines/charts).

#### Interação

**Não exija interação para revelar informação crítica.** A conclusão principal fica visível sem passar o ponteiro ou tocar ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Use dicas flutuantes, filtros e ampliação para explorar detalhes.

**Sinalize atualizações em mais de uma forma.** Em gráficos dinâmicos, mostre um indicador de carregamento quando os dados demoram a atualizar ([gov.br](https://www.gov.br/ds/padroes/design/grafico)). Anuncie a mudança em uma região `aria-live="polite"`, porque quem desativa animações ou usa leitor de tela também precisa saber ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Respeite `prefers-reduced-motion` e ofereça controle para pausar animações ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).

#### Card de gráfico

**Organize cada gráfico em um card.** O título e o subtítulo do card são o título e o subtítulo do gráfico. O card pode receber estes comportamentos opcionais ([gov.br](https://www.gov.br/ds/padroes/design/grafico)):

- **Expandir:** amplia cabeçalho, área principal e rodapé juntos, centralizados, em um diálogo `.tr-dialog--lg` ou em página própria. Veja Tela cheia.
- **Ampliar e reduzir:** aproxima a área principal sem mudar o tamanho do card.
- **Filtrar:** segmenta os dados e permite voltar ao estado anterior.
- **Recolher:** fecha o conteúdo do card e mantém o título visível.
- **Rodapé:** descrição, fonte e link para os dados originais.

**Cite a fonte e ofereça os dados originais.** No rodapé, informe origem, data ou ano, local de publicação e direitos do titular, com um link para os dados em formato aberto, como CSV, que a pessoa abre no programa que preferir ([gov.br](https://www.gov.br/ds/padroes/design/grafico)). Informe formato e tamanho no texto do link, segundo Gerenciamento de arquivos.

#### Painéis de gráficos

Um painel reúne vários gráficos para comunicar os objetivos e as métricas principais. Siga as nove orientações do gov.br ([gov.br](https://www.gov.br/ds/padroes/design/grafico)):

1.  **Defina objetivo e público** antes de escolher métricas.
2.  **Inclua só o essencial.** Cada métrica tem propósito definido e é atualizada. Se for extenso, divida em mais de um painel.
3.  **Crie hierarquia por tamanho e posição.** Coloque o mais importante no canto superior inicial, onde o olhar chega primeiro. Deixe espaço vazio em vez de aumentar um gráfico para preencher.
4.  **Dê contexto aos números.** Mostre o valor do período anterior, uma linha de tendência, a meta e o progresso, e avisos quando a métrica passar de um limite.
5.  **Agrupe métricas relacionadas** por produto, região, equipe ou período, com um título por grupo.
6.  **Seja consistente.** Grupos que mostram as mesmas métricas usam as mesmas visualizações e o mesmo layout.
7.  **Use rótulos claros e curtos.**
8.  **Arredonde os números.** Valores longos distraem. Arredonde para poucas casas decimais ou para o centavo.
9.  **Evolua o painel** com o retorno de quem o usa.

> **Divergência entre referências** Para rótulos de painel, o gov.br aceita abreviações como "7d" no lugar de "7 dias". A HIG pede formatos sem ambiguidade nos rótulos de acessibilidade, como "60 minutos" e não "60m". O Trama aplica a decisão D21: abreviações padronizadas só em eixos, células e cartões compactos, com a unidade nomeada no título, e sempre por extenso no nome acessível. Fontes: [gov.br](https://www.gov.br/ds/padroes/design/grafico), [HIG](https://developer.apple.com/design/human-interface-guidelines/charts).

**Faça** escreva o valor e a conclusão junto da marca.

**Não faça** diferencie séries apenas por verde, vermelho e amarelo, sem rótulo nem forma.

### Acessibilidade

**Construa gráficos em HTML ou SVG acessível.** Eles funcionam com leitores de tela e teclado e escalam melhor. Quando só for possível usar uma imagem, o texto alternativo precisa ser cuidadosamente escrito ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/)).

**Escreva um texto alternativo curto.** Diga o tipo de gráfico e o tipo de dado. Muitos leitores de tela cortam o texto alternativo em 125 caracteres ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).

**Acrescente uma descrição longa em três partes** ([gov.br](https://www.gov.br/ds/padroes/design/grafico)):

1.  **Tipo de gráfico:** "Gráfico de linhas". Dá contexto para o resto.
2.  **Tipo de dado:** "Número de carros vendidos por mês no último ano". Os títulos dos eixos ajudam a escrevê-lo.
3.  **Propósito:** "Os meses de verão têm mais vendas". É o que o gráfico mostra de significativo.

Deixe a descrição visível e ligue-a com `aria-describedby`: ela ajuda também quem tem dificuldade de interpretar gráficos ([gov.br](https://www.gov.br/ds/padroes/design/grafico)). Agrupe gráfico, descrição, fonte e link de dados em `<figure>` e `<figcaption>` ([gov.br](https://www.gov.br/ds/padroes/design/grafico)). Quando as diferenças forem pequenas ou houver muitos valores, inclua uma tabela com os dados ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/)).

**Escreva rótulos de acessibilidade com contexto e valores reais.** Inclua data ou local ("Norte, setembro: 74%"), escreva "60 minutos" e não "60m", e descreva o que a série representa, nunca a cor ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).

**Ofereça um caminho previsível pelo teclado.** Em gráficos interativos, mova o foco ao longo do eixo X com as setas. Em conjuntos grandes, deixe a pessoa navegar por subconjuntos antes do ponto individual ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Filtros, Expandir e Ampliar são botões alcançáveis por Tab, com foco em `--t-focus`.

### Tokens usados

| Elemento                           | Token                                                         |
|------------------------------------|---------------------------------------------------------------|
| Série principal                    | `--t-brand`                                                   |
| Valor de referência ou meta        | `--t-fg-2` com linha tracejada de `--stroke-thin`             |
| Rótulos de eixo, fonte e legendas  | `--t-fg-3`, classe `.tr-caption`                              |
| Linhas de grade                    | `--t-border-subtle`                                           |
| Card e painel expandido            | `--e-2` no card; `--e-6` e `--z-4` no diálogo                 |
| Situação (acima ou abaixo da meta) | `--t-success`, `--t-warning`, `--t-danger`, sempre com rótulo |

### Considerações por plataforma

#### Web desktop

Mostre detalhes em uma dica flutuante ao passar o ponteiro e ao receber foco do teclado. Alinhe a borda inicial do gráfico com a dos demais elementos; para isso, você pode mover o eixo Y para o lado final ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)).

#### Web móvel

Na classe Compacta, use toda a largura para a área de plotagem, encurte os rótulos do eixo vertical e mova as unidades para o título ([HIG](https://developer.apple.com/design/human-interface-guidelines/charts)). Prefira barras horizontais. Não há dica flutuante por hover no toque: mostre o valor escrito em cada marca. Empilhe os cards do painel em uma coluna, na ordem de importância.

#### Tablets e dobráveis

Em layouts de dois painéis, mostre a versão pequena do gráfico na lista e a completa no detalhe, com o mesmo estilo. Com o dobrável parcialmente dobrado, mostre o gráfico na metade superior e os filtros na inferior, sem elementos interativos sobre a dobra ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Gráficos
- Tabelas
- Cards
- Cor
- Excesso de conteúdo
- Acessibilidade

#### Referências

- [Gráfico](https://www.gov.br/ds/padroes/design/grafico) gov.br DS
- [Charting data](https://developer.apple.com/design/human-interface-guidelines/charting-data) Apple HIG
- [Charts](https://developer.apple.com/design/human-interface-guidelines/charts) Apple HIG
- [Datavisualisering og infografik](https://designsystem.dk/styleguide/datavisualisering-infografik/) DKFDS
- [Tilgængelig grafik](https://designsystem.dk/styleguide/datavisualisering-infografik/tilgaengelig-grafik/) DKFDS
- [Datavisualisering](https://designsystem.dk/styleguide/datavisualisering-infografik/datavisualisering/) DKFDS
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta limites por tipo de gráfico, card de gráfico com seus comportamentos, as nove orientações para painéis, descrição longa em três partes, link para dados originais e pares de cor a evitar. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                         |

## Arrastar e soltar

Permita mover, copiar e reordenar conteúdo arrastando, com retorno contínuo durante o gesto e sempre com um caminho equivalente que dispense o arraste.

Ao arrastar e soltar, a pessoa seleciona conteúdo em um local, a origem, e o solta em outro, o destino. Origem e destino podem estar no mesmo contêiner, como uma lista, em contêineres diferentes da mesma tela, como as colunas de um quadro, ou em aplicações diferentes ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

No Trama, o padrão cobre quatro usos: reordenar itens de uma lista, mover itens entre listas ou colunas, soltar arquivos do sistema em uma área de envio e receber conteúdo vindo de outra janela. Arrastar é sempre um atalho: toda ação feita por arraste também precisa ser possível com um único clique, toque ou tecla (WCAG 2.2, 2.5.7).

### Boas práticas

**Ofereça sempre outra forma de fazer a mesma ação.** Arrastar pode ser difícil ou impossível para algumas pessoas. Disponibilize botões, itens de menu como "Mover para" ou comandos de teclado que alcancem o mesmo resultado ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)). Em envios de arquivo, a área de soltar também abre o seletor de arquivos ao ser clicada ou acionada pelo teclado ([gov.br](https://www.gov.br/ds/components/upload)), e o botão de seleção continua visível ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/), [HDS](https://hds.hel.fi/components/file-input)).

**Retire os controles que não podem agir.** O primeiro item de uma lista não mostra "Mover para cima" e o último não mostra "Mover para baixo", porque a pessoa não tem como habilitá-los. Essa é a regra do Trama para elementos desabilitados: o que não pode ser habilitado por uma ação da pessoa sai da interface.

**Informe que é possível arrastar.** Diga no texto de ajuda que a área aceita arquivos arrastados ([gov.br](https://www.gov.br/ds/components/upload)). Em listas, mostre a alça de arraste e uma instrução curta. Se um item parece arrastável e não é, a interface frustra.

**Decida com clareza quando o resultado é mover ou copiar.** Soltar no mesmo contêiner move; soltar em outro contêiner copia; soltar em outra aplicação sempre copia. Antes de mudar esse padrão, escolha o comportamento com menor risco de perda de dados ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

**Ao mover itens entre listas, mantenha as duas coerentes.** Em quadros com colunas, como "A fazer" e "Concluídas", arrastar de uma coluna para outra move o item: ele sai da origem e entra no destino na posição da linha de inserção. Atualize a contagem das duas listas e anuncie o resultado: "Enviar relatório movido para Concluídas, posição 1 de 4". O caminho alternativo é a ação "Mover para" no menu do item, com a lista de destinos.

**Permita arrastar vários itens quando fizer sentido.** Mostre a quantidade em um `.tr-badge--count` junto à imagem de arraste e atualize o número se o destino aceitar só parte dos itens ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

**Deixe desfazer.** Ofereça Desfazer logo após o soltar. Peça confirmação apenas quando a operação não puder ser desfeita ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

#### Estados do arraste

| Estado                                       | Aparência no Trama                                                                                   |
|----------------------------------------------|------------------------------------------------------------------------------------------------------|
| Arrastável em repouso                        | Alça visível; cursor `grab` sobre a alça.                                                            |
| Em arraste (imagem que acompanha o ponteiro) | `.tr-dragging`: opacidade `--o-xl`, leve rotação, `--e-4` e cursor `grabbing`.                       |
| Origem durante o arraste                     | Espaço reservado com contorno tracejado em `--t-border-control`.                                     |
| Destino válido sob o item                    | `.tr-dropzone--active`: borda em `--t-brand` e camada da marca em `--o-xs`, mais o texto do destino. |
| Linha de inserção                            | `--stroke-thick` em `--t-brand` no ponto onde o item vai entrar.                                     |
| Destino inválido                             | Sem destaque, cursor `not-allowed` e, se ajudar, texto "Não é possível soltar aqui".                 |

**Mostre a imagem de arraste assim que o movimento começar.** Use uma representação translúcida do conteúdo para diferenciá-la do original e deixar ver os destinos por baixo ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

**Destaque o destino só enquanto o conteúdo está sobre ele.** Remova o destaque quando o conteúdo sai. Se o destino não aceita o item, não mostre destaque ou mostre um indicador explícito de "não permitido" ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)). Em envios de arquivo, a borda da área muda de cor quando o arquivo passa sobre ela ([gov.br](https://www.gov.br/ds/components/upload)).

**Nunca faça a área de soltar menor que a área visível.** A área que aceita o soltar cobre pelo menos toda a superfície desenhada do destino e pode ultrapassá-la, como as áreas de ação do Trama. Uma área de soltar menor que o desenho faz a pessoa soltar sobre algo que parece aceitar e ver o item voltar.

**Mostre o que acontece quando o soltar falha.** O item volta à origem, se ela estiver visível, ou desaparece com uma transição de `--m-normal`, e uma mensagem explica o motivo ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

**Role o contêiner automaticamente perto das bordas.** Em listas longas, o conteúdo rola enquanto o item passa perto do topo ou da base, e para se o arraste sair do contêiner ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

> **Divergência entre referências** No gov.br, a borda da área de envio fica verde quando o arquivo está sobre ela. No Trama, verde é a cor de `--t-success` e sinaliza conclusão. O destino ativo usa a cor da marca e um texto, e o verde fica para "Arquivo enviado". Fontes: [gov.br](https://www.gov.br/ds/components/upload).

#### Depois de soltar

**Mostre o progresso de transferências demoradas.** Use um indicador de progresso por arquivo e, em listas, um espaço reservado no ponto de inserção ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop), [gov.br](https://www.gov.br/ds/components/upload)).

**Aproveite só a parte relevante do conteúdo recebido.** Ao soltar um contato em um campo de destinatário, use nome e e-mail e descarte o resto ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

**Em envios de arquivo, aceite os válidos e aponte os inválidos.** Se a pessoa soltar vários arquivos e um deles não cumprir os requisitos, aceite os demais e mostre uma mensagem de erro para aquele arquivo ([gov.br](https://www.gov.br/ds/components/upload)). Os detalhes estão em Gerenciamento de arquivos.

**Mantenha o conteúdo solto selecionado.** A pessoa espera poder agir sobre ele imediatamente. Retire a seleção da origem quando o conteúdo foi para outro contêiner ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

**Faça** mantenha a área de soltar visível, com um botão que abre o seletor e os requisitos escritos.

**Não faça** dependa apenas do arraste para anexar arquivos.

### Acessibilidade

**Implemente o arraste pelo teclado.** Com foco na alça, Espaço ou Enter pega o item; as setas movem; Espaço ou Enter solta; Esc cancela e devolve o item à posição original. A alça é um `<button>` com rótulo que inclui o nome do item, como "Reordenar Enviar relatório". Entre listas, as setas para os lados levam o item à coluna vizinha.

**Anuncie cada etapa.** Use uma região `aria-live="polite"` para informar quando o item foi pego, a posição atual ("posição 2 de 3") e o resultado ao soltar ou cancelar.

**Torne a área de envio acessível pelo teclado.** Ela recebe foco com Tab e abre o seletor com Enter ou Espaço. A lista de arquivos enviados é alcançável por Tab, e cada botão Excluir está associado ao nome do arquivo ([gov.br](https://www.gov.br/ds/components/upload)).

**Garanta o alvo de toque.** Alças e botões de mover têm área de ação de `--c-touch` no toque e de pelo menos 24 pixels com mouse.

**Não use cor como único indicador de destino válido.** Combine a borda com a linha de inserção e o texto do destino, como "Solte para mover para Concluídas".

### Tokens usados

| Elemento                   | Token                                           |
|----------------------------|-------------------------------------------------|
| Imagem de arraste          | `--o-xl`, `--e-4`, camada `--z-2`               |
| Destino ativo              | `--t-brand`, `--o-xs`                           |
| Linha de inserção          | `--stroke-thick`, `--t-brand`                   |
| Espaço reservado na origem | `--t-border-control`, `--stroke-thin` tracejado |
| Retorno e saída do item    | `--m-normal`, `--m-ease-standard`               |

### Considerações por plataforma

#### Web desktop

Mude o cursor para indicar o resultado: `grab` sobre a alça, `grabbing` durante o arraste, `copy` quando o soltar vai copiar e `not-allowed` sobre destinos inválidos. Respeite o modificador do sistema para forçar cópia no mesmo contêiner: Option no macOS ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)) e Ctrl no Windows. Quando possível, permita selecionar e arrastar em um único movimento ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)). Ao receber arquivos do sistema, destaque a área de envio mais próxima quando o arquivo entra na janela.

#### Web móvel

No toque, o arraste disputa o gesto com a rolagem. Inicie o arraste só a partir da alça ou após um toque longo e mostre os botões de mover como caminho principal. Em telas da classe Compacta não há arraste de arquivos: a área de envio funciona apenas com toque, que abre o seletor ([gov.br](https://www.gov.br/ds/components/upload)). Troque o texto "Solte os arquivos aqui" por "Selecionar arquivos" nessa classe.

#### Tablets e dobráveis

Em visão de várias janelas, as pessoas arrastam texto, imagens e endereços web entre aplicações. Aceite esse conteúdo nos campos e áreas de anexo, mostre retorno visual quando o arraste começa e indique onde é possível soltar ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). No iPad, as pessoas podem acrescentar itens a um arraste em andamento; aceite várias entradas soltas de uma vez ([HIG](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

### Recursos

#### Relacionados

- Gerenciamento de arquivos
- Upload de arquivo
- Desfazer e refazer
- Listas
- Mouse e trackpad
- Toque e gestos

#### Referências

- [Upload (envio de arquivos)](https://www.gov.br/ds/components/upload) gov.br DS
- [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop) Apple HIG
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [File upload](https://design-system.service.gov.uk/components/file-upload/) GOV.UK Design System
- [FileInput](https://hds.hel.fi/components/file-input) Helsinki Design System

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a tabela de estados com `.tr-dragging` e `.tr-dropzone--active`, a regra de área de soltar, mover itens entre listas, aceite parcial de arquivos e a remoção de controles que não podem agir. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                            |

## Entrada de dados

Peça só o que for necessário, explique por que pede, organize os campos numa ordem previsível e aceite as respostas no formato em que as pessoas costumam escrevê-las.

Preencher campos é trabalho para quem usa o produto. Cada pergunta custa tempo, atenção e, às vezes, a confiança de quem precisa revelar um dado pessoal. Este padrão reúne as regras do Trama para estruturar formulários e pedir nomes, endereços, documentos, datas, e-mails, telefones e senhas em produtos web, com exemplos adaptados ao Brasil e à Lei Geral de Proteção de Dados Pessoais (LGPD).

A reação a respostas que não podem ser aceitas fica em Validação e mensagens de erro. A divisão de formulários longos em páginas fica em Formulários em etapas e páginas de pergunta.

### Boas práticas

#### Peça o mínimo e diga por quê

**Pergunte só o que o serviço realmente usa.** Todo dado coletado precisa de uma finalidade clara e informada, e não pode ser pedido para armazenamento e uso futuro genéricos ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Peça nomes, telefones e documentos apenas quando forem necessários para entregar o serviço, e ofereça mais de um canal de contato ([GOV.UK](https://design-system.service.gov.uk/patterns/names/), [GOV.UK](https://design-system.service.gov.uk/patterns/phone-numbers/)).

**Explique o motivo da coleta de dados pessoais.** Diga para que o dado serve e quando você vai usá-lo, principalmente em dados pessoais e sensíveis ([gov.br](https://www.gov.br/ds/padroes/design/formulario), [GOV.UK](https://design-system.service.gov.uk/patterns/email-addresses/)). Em todo formulário que coleta dados pessoais, inclua antes das ações um link para a política de tratamento de dados. Veja Privacidade.

**Diga o que a pessoa ganha ao preencher um campo opcional.** "Avisamos por SMS quando o pedido sair para entrega" justifica o celular ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Peça consentimento desmarcado, por finalidade e reversível.** Mostre as opções de consentimento sem marcação prévia, uma para cada uso dos dados, com o checkbox ou o switch junto ao texto que descreve o uso, e explique como retirar o consentimento depois ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Obtenha do sistema o que puder e não pergunte duas vezes.** Não peça o que você já sabe ou pode obter com permissão ([HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data)). Dados vindos de um registro externo aparecem em campo somente leitura com a origem na dica e um link "Editar" quando a pessoa puder corrigi-los ([DKFDS](https://designsystem.dk/eksempler/patterns/hentet-data/)). Preencha de antemão o que a pessoa já informou na jornada ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)), o que atende ao critério WCAG 2.2, 3.3.7 (Entrada redundante).

**Identifique dados ocultados.** Quando um campo exibir um dado anonimizado ou sigiloso, diga isso numa mensagem junto ao campo ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

#### Estrutura e espaçamento

**Use uma coluna.** Formulários são preenchidos melhor na vertical. Ponha lado a lado só campos complementares, que completam o anterior, como Estado e Cidade ou Data de início e Data de término ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Quando a largura diminuir, o campo complementar desce para a linha de baixo ([gov.br](https://www.gov.br/ds/components/input)).

**Siga uma ordem lógica e mantenha o código na ordem visual.** Peça o CEP antes do restante do endereço e priorize os campos mais importantes e frequentes ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Leitores de tela seguem a ordem do código, então não reordene campos com CSS ([DKFDS](https://designsystem.dk/eksempler/patterns/formular/)).

**Agrupe por afinidade com `fieldset` e `legend`.** Use `.tr-fieldset`, sem borda, e escreva a legenda como título do grupo, com menos ênfase que o título do formulário ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Botões de opção e grupos de caixas de seleção sempre têm `fieldset` ([Ontario](https://designsystem.ontario.ca/components/detail/fieldsets.html)). Use no máximo um nível de subagrupamento, com recuo de `--sp-600` ([gov.br](https://www.gov.br/ds/padroes/design/formulario)), e evite `fieldset` aninhado no código, que confunde leitores de tela ([Ontario](https://designsystem.ontario.ca/components/detail/fieldsets.html)). Quando faltar espaço, separe grupos com divisor ou com uma superfície `--t-surface-1` ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Use os espaços de formulário por função, iguais em todo o produto.** O gov.br pede espaços constantes para cada função: maiores entre grupos e antes das ações, menores entre campos ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). O Trama define:

| Função                                 | Token             | Valor |
|----------------------------------------|-------------------|-------|
| Título ou legenda até o primeiro campo | `--f-gap-title`   | 16px  |
| Entre campos do mesmo grupo            | `--f-gap-field`   | 24px  |
| Último campo até as ações              | `--f-gap-actions` | 32px  |
| Entre grupos                           | `--f-gap-group`   | 40px  |

**Divida o que for longo.** Formulários extensos ficam mais claros em etapas ou em abas ([gov.br](https://www.gov.br/ds/padroes/design/formulario)), mas não separe em páginas campos muito relacionados, como CEP e cidade ([DKFDS](https://designsystem.dk/eksempler/patterns/formular/)).

#### Rótulos, dicas e campos obrigatórios

**Escreva rótulos visíveis, curtos e positivos.** Use até três palavras, caixa de frase e rótulo acima do campo, perto dele. Escreva no positivo: "Cancelar envio de e-mails" em vez de "Não me envie mais e-mails" ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). O Trama não usa dois-pontos no fim do rótulo. Em páginas de uma pergunta só, a pergunta é a legenda ou o título da página e pode passar de três palavras ([GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)).

**Ponha o formato e as instruções na dica.** Use `.tr-hint` para formato aceito, onde encontrar o dado ou por que ele é pedido, em texto compacto e sem links ([gov.br](https://www.gov.br/ds/padroes/design/formulario), [GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)). Não use placeholder como instrução: ele some ao digitar e pode ser confundido com um valor preenchido ([DKFDS](https://designsystem.dk/eksempler/patterns/formular/), [Fluent](https://fluent2.microsoft.design/components/web/react/core/field/usage)).

**Use o ícone de ajuda só para complementos.** Ele explica, por exemplo, a base legal da coleta, e fica na linha do rótulo. Requisitos do campo nunca ficam escondidos nele ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Veja Oferecer ajuda.

**Prefira campos obrigatórios e indique a exceção em texto.** Diga no subtítulo que todos os campos são obrigatórios e marque cada exceção com "(opcional)" no rótulo. Se a maioria for opcional, marque os obrigatórios com "(obrigatório)". Nunca marque os dois tipos no mesmo formulário ([gov.br](https://www.gov.br/ds/padroes/design/formulario), [GOV.UK](https://design-system.service.gov.uk/patterns/question-pages/)). O Trama não usa o asterisco sozinho: o texto dispensa legenda e é lido por todos.

#### Formatos de dado

**Aceite o dado no formato em que a pessoa escreve.** Aceite espaços, pontos, hífens, parênteses e barras em números e códigos, inclusive no início e no fim, e normalize o valor no sistema ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)). Nunca bloqueie caracteres durante a digitação. Ao sair do campo, você pode formatar o valor exibido; máscara que impede digitar, colar ou apagar é proibida.

**Use um campo para cada dado.** Não divida telefone, CPF ou protocolo em várias caixas ([gov.br](https://www.gov.br/ds/components/input)). A exceção é a data conhecida, em três campos ([GOV.UK](https://design-system.service.gov.uk/patterns/dates/)). Veja Entrada e seletor de data.

**Dimensione o campo pelo tamanho esperado da resposta.** A largura comunica o que se espera e não muda com o texto digitado ([gov.br](https://www.gov.br/ds/padroes/design/formulario), [GOV.UK](https://design-system.service.gov.uk/patterns/addresses/)). Campos de e-mail mostram pelo menos 30 caracteres ([GOV.UK](https://design-system.service.gov.uk/patterns/email-addresses/)).

**Declare o propósito e permita colar.** Use `autocomplete` em nome, e-mail, telefone e endereço, o que atende ao critério WCAG 2.2, 1.3.5, e `spellcheck="false"` em nomes, e-mails e documentos ([GOV.UK](https://design-system.service.gov.uk/patterns/names/)). Nunca bloqueie colar ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/)).

| Dado                 | Campo e atributos                           | Regras do Trama                                                                                                                                                               |
|----------------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome                 | "Nome completo", `autocomplete="name"`      | Campo único que aceita acentos, apóstrofos e hífens. Diga se precisa do nome social ou do nome do documento ([GOV.UK](https://design-system.service.gov.uk/patterns/names/)). |
| Telefone             | `type="tel"`, `autocomplete="tel"`          | DDD com ou sem parênteses, código do país com "+". Use "Celular" se o número receber SMS ([DKFDS](https://designsystem.dk/eksempler/patterns/angivelse-af-telefonnummer/)).   |
| CPF, CNPJ, protocolo | `inputmode="numeric"`, `spellcheck="false"` | Um campo, com ou sem pontuação. Em exemplos, use valores fictícios ([GOV.UK](https://design-system.service.gov.uk/patterns/national-insurance-numbers/)).                     |
| Endereço             | Pesquisa por CEP com opção manual           | Sempre permita digitar o endereço à mão ([GOV.UK](https://design-system.service.gov.uk/patterns/addresses/)).                                                                 |

#### Senhas e autenticação

**Siga a regra de senhas do Trama.** Mínimo de 8 caracteres, sem máximo, colar permitido, botão "Mostrar senha" e nenhum campo de confirmação ([GOV.UK](https://design-system.service.gov.uk/components/password-input/)). Ao criar a senha, mostre um medidor de força com texto (Fraca, Média, Forte) e dicas para fortalecê-la ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Use `autocomplete="new-password"` ou `"current-password"`, e não revele se o erro de acesso foi no usuário ou na senha ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/)).

**Ofereça recuperar e alterar a senha à vista.** Os links ficam junto ao campo de senha ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Agrupe os métodos de autenticação.** Quando houver mais de um, como senha e certificado digital, apresente-os juntos, cada um com rótulo claro, para que a pessoa escolha num só lugar ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Veja Contas e autenticação.

#### Editar dados já enviados

**Mostre o que pode ser editado e como sair da edição.** Ponha um identificador perto de cada informação editável; se tudo puder ser editado, não marque item por item. O acionador pode ser o próprio identificador ou um botão geral. Em modo de edição, ofereça sempre salvar e cancelar, e use o controle certo para o dado: seleção para opções predefinidas, campo de texto para texto livre ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Com muitos dados, edite por etapas ou por abas.

#### Ações do formulário

**Ponha a ação principal primeiro, alinhada ao início do conteúdo.** Secundárias vêm depois; empilhadas no celular, a principal fica em cima. Separe o último campo das ações com `--f-gap-actions`. Nunca desabilite o botão de envio: valide ao enviar. Veja Botões.

**Não ofereça "Limpar formulário" nem "Redefinir".** Esses botões apagam trabalho por engano e não ajudam a concluir a tarefa ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Faça** rótulo visível, dica de formato e campo curto que aceita o valor com ou sem separadores.

**Não faça** placeholder no lugar do rótulo, campo largo demais para o dado e botão que apaga o formulário.

> **Divergência entre referências** Máscara: o GOV.UK pede não usar máscaras em telefones; o gov.br recomenda máscara dinâmica e sugere bloquear caracteres não numéricos. O Trama aceita qualquer formato, nunca bloqueia digitação e permite formatar o valor ao sair do campo (D3). Confirmação de senha: o gov.br pede um segundo campo e níveis Baixa, Média e Alta; o GOV.UK dispensa a confirmação com base em pesquisa. Pelo critério de evidência, o Trama segue o GOV.UK e usa Fraca, Média e Forte (D5). Posição dos botões: o gov.br põe a ação principal à direita; o Trama põe a principal primeiro (D4). Placeholder: o gov.br admite placeholder com exemplos genéricos, em itálico; DKFDS e Fluent o evitam. Pelo critério de acessibilidade, o Trama leva exemplos e formatos para a dica, sem itálico. Espaço do título: o gov.br trata o espaço entre título e primeiro campo como intermediário; o Trama usa o menor valor (`--f-gap-title`) para que a legenda fique visualmente presa ao seu grupo.

### Considerações por plataforma

#### Web desktop

Garanta que a ordem de tabulação siga a ordem de leitura e que cada campo mostre o anel de foco (`--t-focus`). Mantenha o formulário numa coluna de largura confortável mesmo nas classes Grande e Extragrande; campos esticados até a borda não comunicam o tamanho esperado da resposta. Permita alternar entre teclado e mouse a qualquer momento ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

#### Web móvel

Na classe Compacta, campos ocupam a largura toda e usam densidade baixa, com área de toque maior ([gov.br](https://www.gov.br/ds/components/input)); no Trama, `data-density="baixa"`. Os atributos `type` e `inputmode` escolhem o teclado virtual ([GOV.UK](https://design-system.service.gov.uk/patterns/email-addresses/)). Campos complementares descem para linhas separadas. Prefira uma pergunta por página em jornadas longas ([DKFDS](https://designsystem.dk/eksempler/patterns/formular/)).

#### Tablets e dobráveis

Teste se a ordem de preenchimento continua lógica em retrato e paisagem ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Ao abrir ou fechar um dobrável, preserve o texto digitado, a rolagem e o teclado aberto ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Para entradas curtas em telas grandes, prefira um popover perto do controle ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

### Recursos

#### Relacionados

- Validação e mensagens de erro
- Formulários em etapas e páginas de pergunta
- Revisar respostas e confirmação
- Campos de texto
- Entrada e seletor de data
- Contas e autenticação
- Privacidade
- Espaçamento

#### Referências

- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data) Apple HIG
- [Names](https://design-system.service.gov.uk/patterns/names/) GOV.UK Design System
- [Addresses](https://design-system.service.gov.uk/patterns/addresses/) GOV.UK Design System
- [Dates](https://design-system.service.gov.uk/patterns/dates/) GOV.UK Design System
- [Email addresses](https://design-system.service.gov.uk/patterns/email-addresses/) GOV.UK Design System
- [Phone numbers](https://design-system.service.gov.uk/patterns/phone-numbers/) GOV.UK Design System
- [Passwords](https://design-system.service.gov.uk/patterns/passwords/) GOV.UK Design System
- [Password input](https://design-system.service.gov.uk/components/password-input/) GOV.UK Design System
- [National Insurance numbers](https://design-system.service.gov.uk/patterns/national-insurance-numbers/) GOV.UK Design System
- [Question pages](https://design-system.service.gov.uk/patterns/question-pages/) GOV.UK Design System
- [Recover from validation errors](https://design-system.service.gov.uk/patterns/validation/) GOV.UK Design System
- [Fieldsets](https://designsystem.ontario.ca/components/detail/fieldsets.html) Ontario Design System
- [Angivelse af telefonnummer](https://designsystem.dk/eksempler/patterns/angivelse-af-telefonnummer/) Det Fælles Designsystem
- [Formular](https://designsystem.dk/eksempler/patterns/formular/) Det Fælles Designsystem
- [Inputfelter med hentet data](https://designsystem.dk/eksempler/patterns/hentet-data/) Det Fælles Designsystem
- [Field](https://fluent2.microsoft.design/components/web/react/core/field/usage) Fluent 2
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta LGPD, estrutura em uma coluna com campos complementares, agrupamento com fieldset, espaços de formulário por função, edição de dados enviados, métodos de autenticação e a regra de formatos D3; retira o asterisco e o botão de limpar. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                                       |

## Validação e mensagens de erro

Quando uma resposta não pode ser aceita, diga exatamente o que aconteceu, onde e como corrigir, sem apagar nada do que a pessoa já preencheu.

Validação é a verificação das respostas antes de usá-las. O Trama valida para recusar três coisas: informação que não pode estar correta, informação ambígua demais para ser usada e informação obrigatória ausente ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)). Todo o resto deve ser aceito, mesmo que venha num formato diferente do esperado.

Um erro de validação aparece em dois lugares ao mesmo tempo: um resumo de erros no topo da página e uma mensagem junto a cada campo com problema. Além do erro, um campo pode mostrar os estados de sucesso, alerta e informativo, descritos abaixo. Problemas que a pessoa não consegue resolver no formulário, como falta de permissão ou falha do serviço, seguem outro caminho: estados vazios dentro da tela ou as páginas de erro de Modelos de página.

### Boas práticas

#### Evite o erro antes de precisar mostrá-lo

**Projete perguntas que não gerem erro.** Perguntas claras e aceitação de formatos variados reduzem a necessidade de mensagens ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)). Ignore espaços, pontuação e caracteres invisíveis em números e códigos, inclusive os que vêm ao colar ou ditar. Veja Entrada de dados.

**Não use validação para dizer que a pessoa não tem direito ou permissão.** Leve-a a uma página que explique o motivo e o que fazer em seguida ([GOV.UK](https://design-system.service.gov.uk/components/error-message/), [DKFDS](https://designsystem.dk/komponenter/fejlmeddelelser/)). Falhas do sistema dentro de uma área usam uma mensagem ou um estado vazio de erro. Erros de origem externa à aplicação, como endereço inexistente (404) ou falha do servidor (500), usam as páginas de erro de Modelos de página ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)).

#### Quando validar

**Valide quando a pessoa tentar avançar.** O padrão do Trama é validar ao acionar "Continuar" ou "Enviar", e não ao sair de cada campo. Validar antes de a pessoa terminar de digitar atrapalha, principalmente quem digita devagar ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)).

**Use validação durante a digitação só quando houver evidência de ganho.** HIG e gov.br recomendam verificar valores logo que são preenchidos ([HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data), [gov.br](https://www.gov.br/ds/components/input)); GOV.UK e Ontario pedem pesquisa antes de adotar esse comportamento ([Ontario](https://designsystem.ontario.ca/components/detail/error-messaging.html)). O Trama permite validação imediata em casos pontuais, como o `.tr-count` que avisa quando o texto passou do limite, e a criação de nome de usuário, em que a pessoa precisa saber se a escolha está disponível.

**Valide sempre no servidor.** A validação no navegador pode falhar ou ser contornada, então ela complementa a do servidor e nunca a substitui. Quando usar as duas, garanta que as regras não se contradigam ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)).

**Desligue a validação nativa do HTML5.** Adicione `novalidate` ao `<form>`. O estilo, a posição e o texto das mensagens nativas variam por navegador e não seguem o sistema ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/), [Ontario](https://designsystem.ontario.ca/components/detail/error-messaging.html)).

#### Como mostrar

**Mostre a página de novo com tudo o que foi preenchido.** Não limpe campos, nem os corretos nem os incorretos. Manter as respostas ajuda a ver o que deu errado e a corrigir sem redigitar ([GOV.UK](https://design-system.service.gov.uk/components/error-message/)). A exceção é a senha após tentativa de acesso incorreta, que não deve ser mantida ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/)).

**Mostre um resumo de erros, mesmo que haja um só erro.** Use `.tr-error-summary` no topo do conteúdo principal, abaixo do breadcrumb e acima do `h1`, com o título "Há um problema" e um link para cada campo com erro. Mova o foco do teclado para o resumo; essa é a exceção à regra de foco no `h1`, porque a página voltou com problemas a resolver ([GOV.UK](https://design-system.service.gov.uk/components/error-summary/), [DKFDS](https://designsystem.dk/komponenter/fejlopsummering/)).

**Ligue cada link do resumo ao campo certo.** Para um campo único, link para o campo. Para grupos com vários campos, como uma data, link para o primeiro campo com erro, ou para o primeiro do grupo se não souber qual é. Para botões de opção e caixas de seleção, link para a primeira opção ([GOV.UK](https://design-system.service.gov.uk/components/error-summary/)). Ao seguir o link, o rótulo do campo deve continuar visível ([DKFDS](https://designsystem.dk/komponenter/fejlopsummering/)).

**Ponha a mensagem junto ao campo, depois da dica e antes do controle.** Use `.tr-error-msg` e marque o controle com `aria-invalid="true"`, que aplica a borda de `--stroke-thick` em `--t-danger`. Associe a mensagem com `aria-describedby`. Inclua o prefixo oculto "Erro:" para leitores de tela ([GOV.UK](https://design-system.service.gov.uk/components/error-message/), [DKFDS](https://designsystem.dk/komponenter/fejlmeddelelser/)). Não exiba erros em tooltips, ao lado ou abaixo do campo ([Ontario](https://designsystem.ontario.ca/components/detail/error-messaging.html)). Deixe uma linha só para a mensagem e evite textos que quebrem em várias linhas ([gov.br](https://www.gov.br/ds/components/message)); se a quebra acontecer, nunca trunque a mensagem.

**Acrescente "Erro: " ao início do `<title>`.** Assim leitores de tela anunciam o problema assim que a página carrega ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)).

**Não dependa só da cor.** O erro aparece com texto, ícone de erro, borda mais grossa e no resumo. Isso atende ao critério WCAG 2.2, 1.4.1 (Uso de cor). Reserve `--t-danger` para erros e ações destrutivas ([DKFDS](https://designsystem.dk/komponenter/fejlmeddelelser/)).

**Não use toast para erro de campo.** A mensagem do campo precisa ficar visível enquanto a pessoa corrige; um toast some ([DKFDS](https://designsystem.dk/komponenter/toastbesked/), [Geist](https://vercel.com/geist/toast)).

#### Estados de campo além do erro

**Use sucesso, alerta e informativo com o mesmo lugar e a mesma estrutura do erro.** O gov.br prevê quatro objetivos para a mensagem de um campo: erro, sucesso, alerta e informativo ([gov.br](https://www.gov.br/ds/components/input)). No Trama, a mensagem fica depois da dica e antes do controle, usa `.tr-field-msg` com o modificador do estado e é ligada ao controle por `aria-describedby`.

| Estado      | Quando usar                                                                                                                                                                  | No kit                                            |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Sucesso     | Uma verificação que a pessoa espera confirmou o dado: código conferido, nome de usuário disponível, CEP encontrado. Não pinte de verde cada campo apenas preenchido.         | `data-state="success"` e `.tr-field-msg--success` |
| Alerta      | O valor foi aceito, mas pode causar um problema evitável, como um domínio de e-mail com provável erro de digitação. Nunca impede o envio.                                    | `data-state="warning"` e `.tr-field-msg--warning` |
| Informativo | Informação neutra sobre o valor que precisa de mais destaque que a dica, como o efeito do dado em outra parte do serviço ([gov.br](https://www.gov.br/ds/components/input)). | `.tr-field-msg--info`, sem mudar a borda          |
| Erro        | O valor não pode ser aceito.                                                                                                                                                 | `aria-invalid="true"` e `.tr-error-msg`           |

**Retire o estado quando o valor mudar.** Ao editar um campo em estado de sucesso ou alerta, volte ao estado padrão até a próxima verificação. Mensagens de sucesso e alerta usam `role="status"` quando surgem sem envio da página.

#### Como escrever

**Diga o que aconteceu e como corrigir, em linguagem simples.** As mensagens explicam que houve um erro, por que e como contornar ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). Reaproveite as palavras do rótulo para que a mensagem se ligue ao campo. Para o rótulo "Horas por semana", escreva "Digite quantas horas você trabalha por semana" ([GOV.UK](https://design-system.service.gov.uk/components/error-message/)).

**Escreva uma mensagem específica para cada situação.** Um campo pode estar vazio, longo demais, curto demais, com caracteres não aceitos ou no formato errado, e cada caso pede um texto. Evite mensagens genéricas como "Ocorreu um erro", "Preencha o campo" ou "Este campo é obrigatório" ([GOV.UK](https://design-system.service.gov.uk/components/error-message/), [DKFDS](https://designsystem.dk/komponenter/fejlmeddelelser/)).

**Use instruções e descrições de forma consistente.** Use instrução para campo vazio ("Digite seu nome") e descrição para limites ("O nome deve ter no máximo 35 caracteres") ([GOV.UK](https://design-system.service.gov.uk/components/error-message/)).

**Nunca culpe a pessoa, mesmo quando o erro foi dela.** Evite "você fez" e "você não fez" e diga o que fazer: "Digite um e-mail no formato nome@exemplo.com" em vez de "Você digitou seu e-mail errado" ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). Tom neutro, sem humor e sem "Ops" ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)).

**Corte jargão e enfeites.** Não use códigos técnicos, "inválido", "proibido", "você esqueceu", "por favor" nem "desculpe" ([GOV.UK](https://design-system.service.gov.uk/components/error-message/)). Não repita na mensagem um exemplo que já está na dica. Use o mesmo texto no campo e no resumo. Omita o ponto final quando a mensagem for uma frase só ([Fluent](https://fluent2.microsoft.design/components/web/react/core/field/usage)).

| Situação                                      | Mensagem do Trama                                          |
|-----------------------------------------------|------------------------------------------------------------|
| E-mail vazio                                  | Digite seu e-mail                                          |
| E-mail fora do formato, sem exemplo na tela   | Digite um e-mail no formato correto, como nome@exemplo.com |
| Telefone fora do formato, com exemplo na dica | Digite um telefone no formato correto                      |
| CPF incompleto                                | Digite o CPF completo                                      |
| Data incompleta                               | A data de nascimento precisa incluir o ano                 |
| Data no futuro                                | A data de emissão precisa estar no passado                 |
| Nenhuma opção marcada                         | Selecione como prefere receber o comprovante               |
| Arquivo grande demais                         | O arquivo deve ter menos de 2 MB                           |

> **Nota** O limite de 2 MB repete o exemplo do [DKFDS](https://designsystem.dk/komponenter/fejlmeddelelser/) e serve só para mostrar a redação. Use os limites reais do seu serviço.

**Faça** uma mensagem que repete a linguagem do rótulo e diz o que fazer.

**Não faça** mensagem vaga, com "Ops", sem instrução de correção.

#### Erros que não são de campo

**Use um diálogo só para problemas críticos que pedem decisão.** O título descreve a situação de forma específica, nunca apenas "Erro" ou um código, e os botões dizem o resultado da ação ([HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)). Mostre quando um comando não pode ser executado e explique por quê ([HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)). Para falhas de envio de um formulário inteiro, use uma mensagem de erro no topo do formulário e mova o foco para ela; erros e avisos de uma mensagem sempre trazem um botão ou link de recuperação ([Fluent](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). Essa mensagem fica até a pessoa resolver o problema e não some sozinha. Detalhes complementares, como código e data da ocorrência, ficam num estilo diferente do texto principal ([gov.br](https://www.gov.br/ds/components/message)), no Trama em `.tr-caption`.

**Nunca desabilite o botão de envio para evitar erros.** Deixe a pessoa enviar e mostre o que falta. Um botão desabilitado não explica o problema e não leva ao campo.

> **Divergência entre referências** Momento da validação: o gov.br pede feedback visual imediato, com cor de sucesso ou de erro, ao preencher o campo; GOV.UK e Ontario validam ao enviar e só adotam validação imediata com pesquisa que mostre ganho. O GOV.UK relata o uso prolongado dessa abordagem em serviços reais. Pelo critério de evidência, o Trama valida ao enviar e reserva o estado de sucesso para verificações que a pessoa espera. Posição da mensagem: o gov.br põe a mensagem contextual abaixo do campo; GOV.UK, Ontario e DKFDS a põem acima do controle, depois da dica. Pela convergência, e para que a mensagem não fique escondida sob o teclado virtual ou uma lista aberta, o Trama mantém a mensagem acima do controle. Tom: o gov.br admite "sucesso" e exclamação em confirmações; o Trama segue D2 e diz só o que mudou.

### Considerações por plataforma

#### Web desktop

O resumo de erros com links é a principal forma de navegação entre erros pelo teclado. Ao seguir um link, mova o foco para o controle e role a página para que o rótulo apareça acima dele.

#### Web móvel

Em telas pequenas o campo com erro pode estar fora da área visível. Por isso o foco vai para o resumo no topo, e cada link leva ao campo. Evite fechar o teclado virtual ao mostrar erros que surgem durante a digitação, como o contador de caracteres.

#### Tablets e dobráveis

Em layouts de dois painéis, mostre o resumo no topo do painel que contém o formulário, e não no topo da janela. Mantenha as respostas e as mensagens ao mudar de tela num dobrável ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Resumo de erros
- Entrada de dados
- Feedback
- Mensagens e banners
- Campos de texto
- Escrita e conteúdo
- Estados vazios
- Modelos de página: base e erro

#### Referências

- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Message](https://www.gov.br/ds/components/message) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Empty states](https://www.gov.br/ds/padroes/design/emptystates) gov.br DS
- [Recover from validation errors](https://design-system.service.gov.uk/patterns/validation/) GOV.UK Design System
- [Error message](https://design-system.service.gov.uk/components/error-message/) GOV.UK Design System
- [Error summary](https://design-system.service.gov.uk/components/error-summary/) GOV.UK Design System
- [Passwords](https://design-system.service.gov.uk/patterns/passwords/) GOV.UK Design System
- [Fejlmeddelelser](https://designsystem.dk/komponenter/fejlmeddelelser/) Det Fælles Designsystem
- [Fejlopsummering](https://designsystem.dk/komponenter/fejlopsummering/) Det Fælles Designsystem
- [Toastbesked](https://designsystem.dk/komponenter/toastbesked/) Det Fælles Designsystem
- [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) Apple HIG
- [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) Apple HIG
- [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data) Apple HIG
- [Field](https://fluent2.microsoft.design/components/web/react/core/field/usage) Fluent 2
- [Message bar](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage) Fluent 2
- [Error messaging](https://designsystem.ontario.ca/components/detail/error-messaging.html) Ontario Design System
- [Toast](https://vercel.com/geist/toast) Geist
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta os estados de campo sucesso, alerta e informativo, a separação entre estados vazios e páginas de erro, as regras D6 e D9 e a nota de divergência sobre momento e posição da validação. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                     |

## Feedback

Feedback informa o estado das coisas, o resultado das ações e os riscos à frente, com um nível de interrupção proporcional à importância da informação.

Toda ação gera uma pergunta implícita: "funcionou?". O feedback responde a essa pergunta e a outras: o que está acontecendo agora, o que deu certo, o que pode dar errado e como corrigir um problema ([HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)). Feedback claro e consistente faz o produto parecer previsível e encoraja a exploração.

O Trama oferece vários canais de feedback, do mais discreto ao mais interruptivo. A regra central desta página é escolher o canal pela importância e pela urgência da informação. Status pode ficar à vista para ser consultado quando a pessoa quiser; um risco de perda de dados precisa interromper ([HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)). Esta página trata do feedback que o produto dá às pessoas; para colher a opinião delas sobre o produto, veja Coletar feedback.

### Boas práticas

**Ajuste o canal à importância da informação.** Use a tabela a seguir para decidir. Quanto mais o canal interrompe, mais raro deve ser o seu uso: alertas usados com frequência ou para informação sem importância perdem o efeito ([HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)).

| Canal                                                | Use para                                                                                                                                                                                                                                                                                                     | Não use para                                                                                                        |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Status integrado (texto, badge, ícone junto ao item) | Estado atual de um objeto: salvo, sincronizando, publicado, não lido.                                                                                                                                                                                                                                        | Informação que exige ação imediata.                                                                                 |
| Mensagem do campo (`.tr-error-msg`)                  | Problemas com uma resposta específica.                                                                                                                                                                                                                                                                       | Falhas do sistema ou falta de permissão ([DKFDS](https://designsystem.dk/komponenter/fejlmeddelelser/)).            |
| Mensagem e banner (`.tr-msg`)                        | Estado de uma página, painel, card ou do produto inteiro; precisa ficar visível até ser resolvido ([Fluent](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). Também a confirmação de que um formulário foi aceito ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). | Erros de um campo específico ou decoração de texto neutro ([DKFDS](https://designsystem.dk/komponenter/beskeder/)). |
| Toast (`.tr-toast`)                                  | Confirmação não bloqueante de uma ação da pessoa, progresso de uma tarefa em segundo plano, aviso de atividade de outras pessoas ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toast/usage)).                                                                                         | Informação crítica, ações obrigatórias ou erros que precisam de triagem ([Geist](https://vercel.com/geist/toast)).  |
| Diálogo                                              | Informação crítica que pede decisão agora, como confirmar uma ação destrutiva incomum e irreversível ([HIG](https://developer.apple.com/design/human-interface-guidelines/alerts)).                                                                                                                          | Informação apenas informativa ou confirmações de sucesso.                                                           |
| Página inteira                                       | Fim de uma transação, falta de direito de acesso, serviço indisponível.                                                                                                                                                                                                                                      | Qualquer coisa que caiba no contexto atual.                                                                         |

**Integre o status à interface, perto do que ele descreve.** Status próximo do item informa sem exigir ação e sem tirar a pessoa do contexto ([HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)). Um rótulo "Salvo às 14:32" no cabeçalho do documento vale mais que um toast a cada salvamento automático.

**Confirme ações importantes e deixe as rotineiras falarem por si.** As pessoas esperam que uma ação funcione e precisam saber principalmente quando ela falha. Reserve a confirmação explícita para tarefas relevantes, como um pagamento ou um envio ([HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)). Quando confirmar, diga o que foi feito, o que foi enviado e o que acontece em seguida, sem deixar a pessoa num beco sem saída ([DKFDS](https://designsystem.dk/komponenter/beskeder/)). Não mostre confirmações de sucesso em janelas modais ([DKFDS](https://designsystem.dk/komponenter/beskeder/)).

**Avise antes de uma perda de dados inesperada e irreversível.** Não avise quando a perda é o resultado esperado da ação: quem apaga um arquivo quer apagá-lo ([HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)). Para exclusões comuns e reversíveis, prefira executar e oferecer "Desfazer". Veja Desfazer e refazer.

**Mostre quando uma ação não pode ser feita e explique por quê.** Um botão desativado sem explicação deixa a pessoa sem saída. Diga o que falta, perto do controle ou ao tentar a ação ([HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)).

**Toda mensagem de erro e de aviso traz uma saída.** Inclua um botão, um link ou os dois, com um verbo que responda ao problema, como "Renovar licença" ([Fluent](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). Se a pessoa fechar um aviso sem resolver o problema, mostre-o de novo na próxima sessão ([Fluent](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)).

**Posicione a mensagem pelo alcance do que ela comunica.** O gov.br distingue dois tipos e duas posições ([gov.br](https://www.gov.br/ds/components/message)):

| Alcance                                                          | Posição no Trama                                                                                                                                               |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Produto inteiro, como uma instabilidade ou manutenção programada | Entre o cabeçalho e o breadcrumb, com a superfície na largura total e o texto dentro das margens do grid ([gov.br](https://www.gov.br/ds/components/message)). |
| Página atual, como o resultado de uma ação na página anterior    | Imediatamente antes do `h1`, na mesma largura do conteúdo ([GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)).                    |
| Uma área, um card ou uma aba                                     | Junto ao elemento a que se refere ([gov.br](https://www.gov.br/ds/components/message)).                                                                        |
| Um campo                                                         | Mensagem contextual do campo, sem botão Fechar. Veja Validação e mensagens de erro.                                                                            |

**Evite várias mensagens ao mesmo tempo.** Pessoas deixam de ver banners usados com frequência ([GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)). Em vez de várias mensagens de página, use mensagens contextuais junto aos elementos ([gov.br](https://www.gov.br/ds/components/message)) ou junte o conteúdo numa só. Se várias forem inevitáveis no mesmo contêiner, ordene por gravidade: erro, alerta, sucesso, informação ([Fluent](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). Não mostre uma mensagem de página junto com o resumo de erros ([GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)).

**Use o ícone do estado e o botão Fechar no lugar fixo.** O ícone semântico fica à esquerda (círculo com visto para sucesso, triângulo com exclamação para alerta, círculo com X para erro, círculo com "i" para informação) e o Fechar fica no topo, à direita, e não muda de lugar quando o texto quebra ([gov.br](https://www.gov.br/ds/components/message)). Mensagens com conteúdo indispensável e mensagens de campo não têm Fechar ([gov.br](https://www.gov.br/ds/components/message)).

**Decida o tempo de exibição pelo tipo.** Só toasts informativos sem ação somem sozinhos, depois de pelo menos 7 segundos, com pausa enquanto o ponteiro ou o foco estiver sobre eles. Mensagens com ação, de erro ou de alerta ficam até a pessoa fechar ou resolver. Mensagens que somem rápido podem passar despercebidas ([gov.br](https://www.gov.br/ds/components/message)).

**Não narre um fluxo assíncrono com uma sequência de toasts.** Emita um só toast no fim, de sucesso ou de erro ([Geist](https://vercel.com/geist/toast)). Durante a espera, siga Carregamento e espera.

#### Conteúdo

**Escreva títulos específicos.** "Armazenamento quase cheio" diz mais que "Aviso" ([Fluent](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). O corpo complementa o título em uma ou duas frases curtas e não o repete.

**Confirme com substantivo e particípio.** Diga o que mudou: "Relatório arquivado", "Endereço atualizado". Sem a expressão de êxito e sem exclamação: a própria ação já diz que deu certo ([Geist](https://vercel.com/geist/toast), [Fluent](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). Use o mesmo verbo do botão que disparou a ação: o botão "Excluir projeto" gera "Projeto excluído" ([Geist](https://vercel.com/geist/toast)). Não parabenize a pessoa por tarefas rotineiras.

**Termine mensagens de erro com o passo de recuperação.** "Não foi possível verificar o domínio. Tente novamente." ([Geist](https://vercel.com/geist/toast)). Use palavras que a pessoa reconhece do produto e evite termos técnicos ([DKFDS](https://designsystem.dk/komponenter/beskeder/)). Nunca culpe a pessoa e não use humor nem "Ops" ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). Veja Escrita e conteúdo.

**Escreva curto.** Quanto mais longa a mensagem, menos provável que seja lida ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). O título, quando houver, resume a mensagem numa palavra ou frase curta ([gov.br](https://www.gov.br/ds/components/message)).

#### Acessibilidade

**Ofereça o feedback por mais de um meio.** Combine texto, cor e ícone; quem não vê a tela ou usa leitor de tela precisa receber a mesma informação ([HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)). A cor nunca é o único sinal (WCAG 2.2, 1.4.1).

**Anuncie mudanças de status que a pessoa não pediu sem mover o foco.** Use `role="status"` (polido) para informação e sucesso e `role="alert"` (assertivo) só para erros e alertas, porque anúncios assertivos interrompem o que o leitor de tela está lendo ([Fluent](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). Isso atende ao critério WCAG 2.2, 4.1.3 (Mensagens de status).

**Leve o foco ao Fechar quando a mensagem responde a uma ação na mesma página.** Se a mensagem surgir como resposta a uma ação da pessoa e tiver botão Fechar, mova o foco para ele; o botão tem nome "Fechar" e `aria-describedby` apontando para o texto da mensagem, que o leitor de tela lê junto. Ao fechar, devolva o foco ao ponto de origem no fluxo ([gov.br](https://www.gov.br/ds/components/message)). Se a ação levou a uma página nova, o foco vai para o `h1` e a mensagem, antes dele, é anunciada.

**Dê tempo para ler e não interrompa demais.** Feedback que some sozinho precisa respeitar o critério WCAG 2.2, 2.2.1 (Tempo ajustável). Interrupções frequentes prejudicam principalmente pessoas com deficiência cognitiva ou visual ([gov.br](https://www.gov.br/ds/components/message)). Um som característico pode anunciar a mensagem antes da leitura ([gov.br](https://www.gov.br/ds/components/message)), sempre combinado com texto e cor ([HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)).

> **Divergência entre referências** Foco: o Fluent anuncia mensagens sem mover o foco; o gov.br move o foco para o botão Fechar; o GOV.UK foca o banner de sucesso ao carregar a página. O Trama separa os casos: sem foco para status que a pessoa não pediu (WCAG 2.2, 4.1.3), foco no Fechar para resposta a uma ação na mesma página (gov.br) e foco no `h1` em página nova (D13). Tempo: o Fluent fecha toasts após 7 segundos; o gov.br pede evitar mensagens que somem. O Trama aplica D23. Confirmação: o microcopy do gov.br recomenda "sucesso" e exclamação; Geist e Fluent dispensam a expressão. O Trama segue D2 e diz só o que mudou.

### Considerações por plataforma

#### Web desktop

Mensagens de página ficam na área de conteúdo, abaixo da barra de comandos, e nunca acima da navegação lateral ([Fluent](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). Na classe Grande ou maior, a superfície da mensagem se estende até o limite do conteúdo e mantém altura de uma linha quando o texto cabe ([gov.br](https://www.gov.br/ds/components/message)).

#### Web móvel

Em telas pequenas, mensagens de página quebram em várias linhas, o Fechar continua no topo à direita e as ações descem para baixo do texto; nunca corte o conteúdo ([Fluent](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)). Toasts devem ocupar no máximo três linhas em qualquer idioma ([One UI](https://developer.samsung.com/one-ui/comp/toast.html)) e não podem cobrir a navegação inferior.

#### Tablets e dobráveis

Em layouts de vários painéis, mostre a mensagem no painel a que ela se refere. Mensagens de produto inteiro ficam no topo da área de conteúdo, acima dos painéis. Mantenha o feedback visível ao abrir ou fechar um dobrável.

### Recursos

#### Relacionados

- Mensagens e banners
- Toasts
- Diálogos
- Validação e mensagens de erro
- Carregamento e espera
- Notificações
- Desfazer e refazer
- Coletar feedback

#### Referências

- [Message](https://www.gov.br/ds/components/message) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Notification banner](https://design-system.service.gov.uk/components/notification-banner/) GOV.UK Design System
- [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) Apple HIG
- [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) Apple HIG
- [Message bar](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage) Fluent 2
- [Toast](https://fluent2.microsoft.design/components/web/react/core/toast/usage) Fluent 2
- [Beskeder (Alerts)](https://designsystem.dk/komponenter/beskeder/) Det Fælles Designsystem
- [Fejlmeddelelser](https://designsystem.dk/komponenter/fejlmeddelelser/) Det Fælles Designsystem
- [Toastbesked](https://designsystem.dk/komponenter/toastbesked/) Det Fælles Designsystem
- [Toast](https://vercel.com/geist/toast) Geist
- [Toasts](https://developer.samsung.com/one-ui/comp/toast.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta posição por alcance da mensagem, ícones e Fechar, foco no Fechar em resposta a uma ação, tempos de exibição de D23 e confirmações de D2. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                       |

## Gerenciamento de arquivos

Ajude as pessoas a enviar, criar, abrir, salvar e baixar arquivos com confiança, sabendo antes o que é aceito e depois o que aconteceu com cada arquivo.

Aplicações web lidam com arquivos de duas formas. Na primeira, a pessoa traz um arquivo do próprio dispositivo, como um comprovante anexado a uma solicitação. Na segunda, o produto cria e guarda documentos, como relatórios ou rascunhos, que a pessoa abre, edita, salva e exporta.

Este padrão cobre as duas situações. O controle de seleção está documentado em Upload de arquivo, e o gesto de soltar arquivos em Arrastar e soltar.

### Boas práticas

#### Enviar arquivos

**Peça um arquivo apenas quando ele for indispensável.** Enviar arquivos exige que a pessoa encontre, prepare e às vezes digitalize um documento ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/), [DKFDS](https://designsystem.dk/komponenter/fil-upload/)).

**Diga antes quais formatos e tamanhos são aceitos.** Coloque os formatos e o tamanho máximo por arquivo no texto de ajuda ([DKFDS](https://designsystem.dk/komponenter/fil-upload/), [HDS](https://hds.hel.fi/components/file-input)), e diga também se é possível arrastar arquivos para a área ([gov.br](https://www.gov.br/ds/components/upload)). Use o rótulo para dizer o que enviar, como "Anexe o laudo médico", e indique se o campo aceita um ou vários arquivos ([HDS](https://hds.hel.fi/components/file-input)).

> **Divergência entre referências** O gov.br padroniza o rótulo do componente como "Envio de arquivos" ou "Envio de documentos", em caixa alta, com placeholder em itálico. HDS e GOV.UK pedem um rótulo que diga o que enviar. O Trama segue HDS e GOV.UK no conteúdo, porque um rótulo específico evita erro de documento, e segue as decisões D1 e D16 na forma: caixa de frase, sem itálico. Fontes: [gov.br](https://www.gov.br/ds/components/upload), [HDS](https://hds.hel.fi/components/file-input), [GOV.UK](https://design-system.service.gov.uk/components/file-upload/).

**Verifique o formato antes de começar a transferência.** Assim a pessoa não espera o envio terminar para descobrir que o arquivo é inválido ([DKFDS](https://designsystem.dk/komponenter/fil-upload/)). Repita todas as validações no servidor: a verificação no navegador olha a extensão e o tipo declarado, não o conteúdo ([HDS](https://hds.hel.fi/components/file-input/security)).

**Mostre o progresso de cada arquivo.** Ao soltar ou selecionar, a transferência começa e cada arquivo mostra seu próprio indicador de carregamento ([gov.br](https://www.gov.br/ds/components/upload)). Ofereça Cancelar enquanto o arquivo está sendo enviado.

**Confirme quando o envio terminar.** Liste cada arquivo logo abaixo da área de envio, com nome, formato, tamanho e status, e permita excluir cada um antes de enviar o formulário ([gov.br](https://www.gov.br/ds/components/upload), [DKFDS](https://designsystem.dk/komponenter/fil-upload/)). O nome do arquivo pode ser um link que abre o arquivo para conferência ([gov.br](https://www.gov.br/ds/components/upload)).

**Em lote, aceite os válidos e aponte os inválidos.** Se a pessoa enviar vários arquivos e um deles não cumprir os requisitos, aceite os demais e mostre a mensagem de erro no arquivo recusado ([gov.br](https://www.gov.br/ds/components/upload)). Repita o erro no resumo de erros do topo, com o nome do arquivo.

**Em envio único, substitua e avise.** Se o campo aceita um só arquivo, o rótulo fala em "arquivo", no singular, e o seletor não permite escolher vários. Se a pessoa arrastar mais de um, recuse a ação e diga que só um arquivo é permitido. Se ela já enviou um arquivo e envia outro, o mais recente substitui o anterior, e uma mensagem de alerta informa a troca ([gov.br](https://www.gov.br/ds/components/upload)). No Trama, essa mensagem nomeia os dois arquivos e oferece Desfazer.

**Trunque nomes longos de arquivo sem esconder o nome.** Quando o nome não cabe no espaço, trunque a parte que excede e mostre o nome completo em uma dica ([gov.br](https://www.gov.br/ds/components/upload)). No Trama, o nome completo também fica no nome acessível do item e dos botões. Prefira truncar no meio, preservando a extensão, e nunca deixe menos de três caracteres de uma palavra. Veja Excesso de conteúdo.

**Agrupe arquivos relacionados e separe os que não são.** Um campo com vários arquivos funciona para itens do mesmo tipo. Para documentos diferentes, como identidade e comprovante de endereço, use um campo para cada ([HDS](https://hds.hel.fi/components/file-input)).

**Permita reutilizar um arquivo já enviado na mesma jornada** e, antes de permitir baixá-lo de volta, considere quem usa dispositivos públicos ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)).

**Escreva mensagens de erro específicas.** Use mensagens de sistema para cada tipo de erro: formato inválido, tamanho excessivo, envio não concluído ([gov.br](https://www.gov.br/ds/components/upload)). Use as formas abaixo, adaptadas do [GOV.UK](https://design-system.service.gov.uk/components/file-upload/). Diga o que aconteceu e como resolver, sem culpar a pessoa, e nunca exponha detalhes técnicos como caminhos do servidor ([HDS](https://hds.hel.fi/components/file-input/security)).

| Situação                          | Mensagem                                                                            |
|-----------------------------------|-------------------------------------------------------------------------------------|
| Nenhum arquivo escolhido          | Selecione \[o que precisa ser enviado\], por exemplo "Selecione o laudo médico"     |
| Formato não aceito                | O arquivo \[nome\] precisa ser \[lista de formatos\], por exemplo "PDF, JPG ou PNG" |
| Arquivo grande demais             | O arquivo \[nome\] precisa ter menos de \[tamanho por extenso\]                     |
| Arquivo vazio                     | O arquivo \[nome\] está vazio                                                       |
| Arquivo com vírus                 | O arquivo \[nome\] contém um vírus                                                  |
| Arquivo protegido por senha       | O arquivo \[nome\] está protegido por senha. Retire a senha e envie de novo         |
| Falha no envio                    | Não foi possível enviar o arquivo \[nome\]. Tente de novo                           |
| Mais de um arquivo em envio único | Este campo aceita um arquivo. Selecione apenas um                                   |
| Limite de quantidade              | Você pode enviar até \[número\] arquivos                                            |

#### Criar, salvar e abrir documentos

**Salve o trabalho automaticamente.** Salve periodicamente durante a edição e ao sair do documento, sem exigir ação explícita ([HIG](https://developer.apple.com/design/human-interface-guidelines/file-management)). Mostre o estado perto do título ("Salvo às 14:32") e use o padrão de feedback se o salvamento falhar.

**Deixe claro quando há alterações não salvas.** Se o salvamento automático estiver desativado ou falhar, indique as alterações pendentes e peça confirmação ao fechar, com as ações Salvar, Não salvar e Cancelar. Quando o salvamento automático funciona, não mostre esse indicador ([HIG](https://developer.apple.com/design/human-interface-guidelines/file-management)).

**Dê um nome provisório a documentos novos.** Use "Sem título" até a pessoa escolher um nome ([HIG](https://developer.apple.com/design/human-interface-guidelines/file-management)) e permita renomear direto no título.

**Ofereça "Abrir recentes" junto de "Abrir"** e permita filtrar a lista e abrir vários arquivos de uma vez ([HIG](https://developer.apple.com/design/human-interface-guidelines/file-management)).

**Nomeie o botão de confirmação pela tarefa.** Se o seletor insere o conteúdo de um arquivo no documento atual, o botão diz "Inserir" ([HIG](https://developer.apple.com/design/human-interface-guidelines/file-management)).

**Permita escolher nome, formato e local ao exportar** ([HIG](https://developer.apple.com/design/human-interface-guidelines/file-management)). Em links de download, use o verbo "Baixar" e informe formato e tamanho no texto do link, como "Baixar extrato (PDF, 240 kilobytes)".

**Ofereça pré-visualização de arquivos que o produto não edita** ([HIG](https://developer.apple.com/design/human-interface-guidelines/file-management)).

**Faça** diga o que enviar e os requisitos antes da escolha.

**Não faça** use um rótulo genérico e revele os requisitos só no erro.

### Acessibilidade

**Use o campo nativo.** Prefira `<input type="file">`, que recebe foco com Tab, abre com Enter ou Espaço e funciona com tecnologias assistivas ([gov.br](https://www.gov.br/ds/components/upload), [DKFDS](https://designsystem.dk/komponenter/fil-upload/)). Mantenha curtos os textos do botão e de "Nenhum arquivo escolhido", porque leitores de tela leem tudo ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)).

**Ligue cada ação ao seu arquivo.** O botão Excluir carrega no nome acessível o nome do arquivo, para que a pessoa saiba qual será removido ([gov.br](https://www.gov.br/ds/components/upload)). A lista é alcançável por Tab.

**Anuncie os estados.** Mensagens de informação, sucesso, alerta e erro do envio precisam ser lidas por tecnologias assistivas ([gov.br](https://www.gov.br/ds/components/upload)). Use `role="status"` para progresso e conclusão e o resumo de erros, com foco, para erros ao enviar o formulário.

**Mantenha mensagens com ação até a pessoa agir.** O alerta de substituição tem Desfazer, então fica visível até ser fechado.

### Considerações por plataforma

#### Web desktop

Aceite arquivos soltos na área de envio e mantenha o botão de seleção. A área de envio tem largura limitada ao campo do formulário, sem esticar na largura da página. Em editores de documentos, ofereça atalhos para criar e abrir sem substituir atalhos do navegador.

#### Web móvel

Na classe Compacta, a área de envio ocupa a largura disponível e funciona só pelo toque, porque não há arraste de arquivos nesse contexto ([gov.br](https://www.gov.br/ds/components/upload)). O campo abre o seletor do sistema, que pode incluir a câmera. Use `accept` para filtrar tipos e `capture` só quando a foto precisa ser tirada na hora ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)). Fotos de celular costumam ser grandes: mostre o limite e, se possível, reduza a imagem antes do envio. Ações da lista têm área de `--c-touch`.

#### Tablets e dobráveis

Em multi-janela, as pessoas arrastam imagens e documentos de outra aplicação para a sua. Aceite esses arquivos e mostre onde soltar ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Na classe Expandida, mostre a lista de arquivos em um painel e a pré-visualização no outro.

### Recursos

#### Relacionados

- Upload de arquivo
- Arrastar e soltar
- Excesso de conteúdo
- Validação e mensagens de erro
- Carregamento e espera
- Privacidade

#### Referências

- [Upload (envio de arquivos)](https://www.gov.br/ds/components/upload) gov.br DS
- [File management](https://developer.apple.com/design/human-interface-guidelines/file-management) Apple HIG
- [File upload](https://design-system.service.gov.uk/components/file-upload/) GOV.UK Design System
- [Vedhæft fil](https://designsystem.dk/komponenter/fil-upload/) DKFDS
- [FileInput](https://hds.hel.fi/components/file-input) Helsinki Design System
- [FileInput: Security](https://hds.hel.fi/components/file-input/security) Helsinki Design System
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta envio em lote com aceite dos arquivos válidos, substituição com alerta no envio único, progresso por arquivo, truncamento de nomes e unidades por extenso no texto. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                  |

## Tela cheia

Ofereça tela cheia ou visualização expandida quando o conteúdo ou uma tarefa exigente se beneficia de mais espaço e menos distração, sempre por escolha da pessoa e com saída evidente.

No modo de tela cheia, uma janela se expande para ocupar a tela inteira e esconde os controles do sistema ([HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)). Na web, isso significa pedir ao navegador que um elemento ocupe a tela, escondendo abas, barra de endereço e a interface do próprio produto.

O Trama distingue três casos:

- **Tela cheia do navegador:** modo de visualização não modal. A pessoa continua a mesma tarefa com mais espaço. É o assunto principal desta página.
- **Visualização expandida:** um elemento da página, como um gráfico, um mapa ou uma imagem, cresce para ocupar a área do produto, centralizado, sobre um véu. Funciona em todos os navegadores e não depende da API de tela cheia.
- **Apresentação modal em tela cheia:** uma forma de modalidade para tarefas complexas, como editar uma imagem, que segue as regras daquele padrão ([HIG](https://developer.apple.com/design/human-interface-guidelines/modality)). É a superfície mais elevada da hierarquia ([Geist](https://vercel.com/geist/materials)) e usa `--e-6`, `--r-2xl` e `--z-4`.

### Quando usar

Ofereça tela cheia quando a pessoa quer se concentrar ou mergulhar no conteúdo: assistir a vídeos, ver fotos ou apresentações, jogar ou executar uma tarefa aprofundada ([HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)). No Trama, os casos típicos são players de mídia, visualizadores de documentos e imagens, apresentações, painéis em telões e editores com área de trabalho extensa.

Use a visualização expandida quando um componente tem informação demais para o espaço que ocupa na página. Gráficos densos e mapas são o caso mais comum: a ação Expandir amplia cabeçalho, área principal e rodapé juntos, centralizados na tela, com melhor legibilidade ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).

Não use tela cheia para formulários, listas ou páginas de leitura comum. Para dar mais espaço a um painel, prefira recolher a navegação lateral.

### Boas práticas

**Deixe a pessoa escolher quando entrar.** Nunca ative a tela cheia ao abrir uma página. Ofereça um botão explícito ([HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)). Os navegadores só aceitam o pedido em resposta a uma ação da pessoa.

**Deixe a pessoa escolher quando sair.** Não saia sozinho quando a mídia termina ou a atividade acaba ([HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)). Esc sempre sai, porque o navegador garante isso, e um botão visível "Sair da tela cheia" oferece o mesmo caminho para quem usa toque ou não conhece a tecla.

**Retire o botão quando o modo não estiver disponível.** Se o navegador não oferece tela cheia para aquele elemento, a pessoa não tem como habilitar o botão: retire-o e ofereça a visualização expandida no lugar. Não mostre um botão Tela cheia desabilitado.

**Ajuste o layout ao espaço extra, sem mudar o que aparece.** Mantenha o conteúdo essencial em destaque e aproveite o espaço ajustando proporções. As mudanças devem ser sutis, para que a interface continue reconhecível ([HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)). Não tente redimensionar a janela do navegador por código.

**Mantenha acessíveis os controles necessários para terminar a tarefa.** Um player em tela cheia precisa ter os controles de reprodução visíveis ou fáceis de revelar ([HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)). Um gráfico expandido mantém filtros, ampliação e a fonte dos dados ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).

**Esconda barras temporariamente e permita trazê-las de volta.** Oculte barras de ferramentas e navegação quando o conteúdo é o foco, e revele-as com um toque, com o movimento do ponteiro ou com o foco do teclado. Mantenha visíveis os controles essenciais para a navegação ([HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)). As barras reaparecem com `--m-normal` e `--m-ease-enter` e somem após alguns segundos sem interação, exceto enquanto um controle dentro delas tem foco. Com `prefers-reduced-motion` ou com as animações desligadas na configuração do produto, aparecem e somem sem animação.

**Retome de onde a pessoa parou.** Se ela troca de aba ou de aplicação, pause vídeos, apresentações automáticas e jogos e retome do mesmo ponto na volta ([HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)).

**Reflita o estado no botão.** Use um botão de alternância com `aria-pressed` ou troque o rótulo entre "Tela cheia" e "Sair da tela cheia". Atualize o estado também quando a pessoa sai por Esc ou pelo próprio navegador.

#### Visualização expandida

**Centralize o conteúdo expandido sobre um véu.** Use um diálogo `.tr-dialog--lg` ou uma página própria ([gov.br](https://www.gov.br/ds/padroes/design/grafico)). O véu é um scrim de foco: escurece o resto da tela para dirigir a atenção ao elemento expandido ([gov.br](https://www.gov.br/ds/components/scrim)). No Trama, ele usa `--t-overlay`.

**Deixe uma margem entre o conteúdo expandido e a borda da tela.** Assim a pessoa percebe que a tela anterior continua por baixo ([gov.br](https://www.gov.br/ds/components/modal)). Na classe Compacta, essa margem não é possível: use a largura total e um botão Fechar fixo no topo.

**Nunca use rolagem horizontal no conteúdo expandido.** Se o conteúdo for mais alto que a tela, mantenha cabeçalho e ações fixos e role só o corpo, com a sombra de borda que indica conteúdo oculto ([gov.br](https://www.gov.br/ds/components/modal)). Mapas e gráficos que exigem duas dimensões usam ampliação e deslocamento dentro da área principal, sem mudar o tamanho do contêiner ([gov.br](https://www.gov.br/ds/padroes/design/grafico)).

**Faça** ofereça um controle explícito para entrar.

**Não faça** entre ou saia do modo sem que a pessoa peça.

### Acessibilidade

**Cuide do foco ao entrar e ao sair.** Na tela cheia do navegador, mantenha o foco no elemento ativo ou mova-o para o primeiro controle do conteúdo expandido. Na visualização expandida, que é informativa, o foco inicial vai para o botão Fechar. Ao sair, devolva o foco ao botão que abriu o modo ([gov.br](https://www.gov.br/ds/components/modal)).

**Não deixe o foco escapar.** Elementos fora do contêiner em tela cheia ficam invisíveis e não podem receber foco. Na visualização expandida, marque o resto da página com `inert`. Barras ocultas não podem ficar invisíveis e focáveis ao mesmo tempo: mostre a barra quando um de seus controles receber foco.

**Nomeie a ação de expandir.** O botão diz o que vai expandir no nome acessível, como "Expandir gráfico de pedidos no prazo", e usa `aria-haspopup="dialog"` quando abre um diálogo.

### Tokens usados

| Elemento                       | Token                                            |
|--------------------------------|--------------------------------------------------|
| Fundo de mídia em tela cheia   | `--t-bg` do tema escuro, com `.tr-inverse`       |
| Véu da visualização expandida  | `--t-overlay`                                    |
| Superfície expandida           | `--t-surface-raised`, `--e-6`, `--z-4`           |
| Barras sobrepostas ao conteúdo | `--t-surface-raised` com `--e-4`, camada `--z-3` |
| Entrada e saída das barras     | `--m-normal`, `--m-ease-enter`, `--m-ease-exit`  |
| Alvos de controle              | mínimo `--c-touch` no toque                      |

### Considerações por plataforma

#### Web desktop

Ofereça o botão na barra de ferramentas do conteúdo e o atalho F quando o foco estiver no player ou visualizador. Não interfira no atalho de tela cheia do navegador. Revele as barras quando o ponteiro se move ou se aproxima da borda superior ([HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)). A visualização expandida fecha com Esc, com o botão Fechar e com clique fora.

#### Web móvel

O suporte à tela cheia varia entre navegadores móveis; alguns só a permitem para vídeo. Quando não houver suporte, use a visualização expandida, que esconde a interface do produto. Em vídeo, permita girar para paisagem. Revele os controles com um toque no conteúdo e não capture gestos de borda que o sistema usa ([HIG](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)).

#### Tablets e dobráveis

Ao abrir ou fechar um dobrável, o conteúdo preenche a nova tela e continua no mesmo ponto, com a mesma posição de rolagem ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). No modo Flex, mostre o vídeo na metade superior e os controles na inferior, sem elementos interativos sobre a dobra ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Em tablets com várias janelas, a tela cheia do navegador ocupa só a área da janela; teste o layout nesse tamanho.

### Recursos

#### Relacionados

- Modalidade
- Visualização de dados
- Multitarefa e janelas
- Barra de ferramentas
- Postura e dobra
- Movimento

#### Referências

- [Gráfico](https://www.gov.br/ds/padroes/design/grafico) gov.br DS
- [Modal](https://www.gov.br/ds/components/modal) gov.br DS
- [Scrim](https://www.gov.br/ds/components/scrim) gov.br DS
- [Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen) Apple HIG
- [Modality](https://developer.apple.com/design/human-interface-guidelines/modality) Apple HIG
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI
- [Materials](https://vercel.com/geist/materials) Geist

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                               |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a visualização expandida de gráficos e mapas, o scrim de foco, a remoção do botão quando o modo não existe, o foco inicial em Fechar e a proibição de rolagem horizontal. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                        |

## Carregamento e espera

O melhor carregamento termina antes de a pessoa perceber; quando a espera é inevitável, mostre algo logo, diga o que está acontecendo e quanto falta.

Toda interface espera por algo: uma página, uma lista filtrada, um arquivo enviado, um relatório gerado. A forma de lidar com a espera muda a percepção de velocidade e de confiabilidade do produto. Tela em branco faz a pessoa achar que algo quebrou ([HIG](https://developer.apple.com/design/human-interface-guidelines/loading)); indicador parado faz achar que o produto travou ([HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)).

O Trama tem quatro indicadores de espera: skeleton para conteúdo com layout conhecido, spinner para esperas indeterminadas, barra de progresso para tarefas mensuráveis em linha e progresso circular determinado (`.tr-progress-ring`) para tarefas mensuráveis no corpo da página. Qualquer um deles pode, em casos raros, bloquear uma região enquanto ela processa.

### Boas práticas

**Escolha o indicador pela duração esperada.** O Trama adota os limites do Fluent ([Fluent](https://fluent2.microsoft.design/wait-ux)):

| Duração esperada                                              | O que mostrar                                                                        |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Menos de 1 segundo                                            | Nada. Um indicador que pisca e some parece um defeito.                               |
| De 1 a 3 segundos                                             | Spinner junto ao elemento afetado, ou skeleton se o conteúdo tiver layout conhecido. |
| Mais de 3 segundos                                            | Barra de progresso, ou spinner acompanhado de um texto que explique a espera.        |
| Mais de 3 segundos, com duração mensurável no corpo da página | Progresso circular determinado, com percentual e, se possível, "Cancelar".           |
| Tarefa longa em segundo plano                                 | Toast de progresso, para acompanhar sem bloquear o trabalho.                         |

Outras referências usam limites próximos: o DKFDS reserva o spinner para esperas acima de 2 segundos ([DKFDS](https://designsystem.dk/komponenter/spinner/)), e o Ontario usa indicador a partir de 1 segundo e pede texto explicativo acima de 8 segundos ([Ontario](https://designsystem.ontario.ca/components/detail/loading-indicator.html)).

**Mostre algo o quanto antes.** Exiba a estrutura da página e os dados já disponíveis enquanto o resto chega. Esperar por tudo antes de mostrar qualquer coisa faz a ausência de conteúdo parecer um problema ([HIG](https://developer.apple.com/design/human-interface-guidelines/loading)).

**Use skeleton quando o layout final for conhecido.** Linhas de tabela, grades de cards e blocos de perfil são bons casos. Dimensione cada bloco de `.tr-skeleton` como o conteúdo final, para que nada se desloque quando os dados chegarem, e use o raio do elemento real: `--r-pill` para avatares, `--r-md` para botões ([Geist](https://vercel.com/geist/skeleton)). Nunca use skeleton para representar ausência de dados; isso é um estado vazio.

**Escolha o tamanho pelo lugar.** O gov.br define um tamanho pequeno para dentro de componentes, um padrão para o corpo da página e um único tamanho para o determinado ([gov.br](https://www.gov.br/ds/components/loading)). No Trama: `.tr-spinner` dentro de botões, células, listas e campos, quando a pessoa pode continuar interagindo com o resto; `.tr-spinner--lg` ou `.tr-progress-ring` no corpo da página, num bloco que carrega ou num envio de arquivos.

**Ponha o spinner onde a atenção estará.** Para uma ação dentro da página, ligue o indicador ao elemento afetado: o botão, a célula, a área de resultados. Para uma nova página ou visão, centralize-o na área de conteúdo principal ([Ontario](https://designsystem.ontario.ca/components/detail/loading-indicator.html)). Num bloco que recarrega, coloque o spinner no topo da seção, centralizado na horizontal, para que apareça sem rolagem em telas pequenas; não cubra a página inteira com um spinner ([DKFDS](https://designsystem.dk/komponenter/spinner/)).

**Prefira o progresso determinado.** Saber quanto falta ajuda a decidir se vale esperar, fazer outra coisa ou desistir. Se uma tarefa indeterminada chegar a um ponto em que a duração pode ser medida, troque para o indicador determinado ([HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)). Não troque o formato de spinner para barra no meio da tarefa, porque os dois têm tamanhos diferentes e a troca desorganiza a interface ([HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)). Nunca mostre spinner e barra juntos ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toast/usage)).

**Mostre o progresso circular com percentual.** O círculo de `.tr-progress-ring` cresce no sentido horário a partir do topo e o rótulo ao centro vai de 0% a 100% ([gov.br](https://www.gov.br/ds/components/loading)). Ponha abaixo dele o nome da tarefa e, se a operação puder ser interrompida, um botão sutil "Cancelar envio".

**Seja honesto no ritmo.** Mostrar 90% em cinco segundos e os últimos 10% em cinco minutos parece enganoso. Distribua o avanço de forma regular e mantenha o indicador em movimento; se o processo travar, diga o que aconteceu e o que a pessoa pode fazer ([HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)).

**Não deixe ninguém preso num spinner.** Defina um tempo limite. Depois dele, troque o spinner por uma mensagem de erro ou uma página de erro com caminho de saída ([DKFDS](https://designsystem.dk/komponenter/spinner/)). Spinners também não compensam lentidão permanente: resolva o desempenho ([DKFDS](https://designsystem.dk/komponenter/spinner/)).

**Permita interromper.** Se a tarefa puder ser interrompida sem efeito colateral, ofereça "Cancelar". Se cancelar significar perder progresso, ofereça também "Pausar" e confirme antes de descartar o que já foi feito ([HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)).

**Bloqueie só a região que não pode ser usada durante o processamento.** Quando interagir com uma área durante o processamento puder gerar dados errados, como editar parcelas enquanto são recalculadas, cubra apenas essa área com `.tr-region-busy`: o véu usa `--o-lg`, o conteúdo coberto recebe `inert` e o indicador fica centralizado na largura e na altura ([gov.br](https://www.gov.br/ds/components/loading)). O bloqueio fica na camada `--z-4`. Bloquear a tela inteira é exceção, para operações das quais toda a página depende, e sempre com indicador determinado ou texto que explique a espera.

**Deixe a pessoa continuar trabalhando.** Carregue em segundo plano e mantenha disponíveis as outras ações ([HIG](https://developer.apple.com/design/human-interface-guidelines/loading)). Mantenha a pessoa na visão atual e ligue o feedback ao conteúdo afetado, sem indicadores concorrentes na mesma tela ([Fluent](https://fluent2.microsoft.design/wait-ux)).

**Identifique dados que chegaram de outro sistema.** Quando um formulário for preenchido com dados obtidos automaticamente, como um cadastro de empresa, mostre-os em campos somente leitura com uma dica que indique a origem e, se couber, um link para editar. Esses campos são salvos e validados como qualquer outro ([DKFDS](https://designsystem.dk/eksempler/patterns/hentet-data/)). Enquanto os dados chegam, use skeleton nos campos que receberão os dados.

**Informe a espera em formulários.** Ao enviar, verificar ou carregar dados de um formulário, mostre o indicador ou uma mensagem com a situação ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). O botão de envio continua focável enquanto envia: marque-o com `aria-disabled="true"`, troque o rótulo por "Enviando" e ignore novos acionamentos, para que o motivo da indisponibilidade fique à vista.

**Não use spinner em atualizações automáticas.** Use-o só no primeiro carregamento ou em resposta a uma ação da pessoa ([DKFDS](https://designsystem.dk/komponenter/spinner/)). Atualizações periódicas entram em silêncio, como em Notificações.

#### Conteúdo

**Nomeie o trabalho em andamento.** "Enviando 3 arquivos" e "Gerando relatório de setembro" dizem mais que "Carregando", termo vago que pouco acrescenta ([HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)). Use gerúndio para o estado em andamento e particípio para o fim: "Enviando arquivo", "Arquivo enviado" ([Fluent](https://fluent2.microsoft.design/wait-ux)). Quando não houver detalhe disponível, use uma frase tranquilizadora como "Preparando tudo" ([Fluent](https://fluent2.microsoft.design/wait-ux)).

**Informe o que resta no formato mais útil.** "10 minutos restantes", "65% concluído" ou "10 de 17 gigabytes", sem ponto final ([Fluent](https://fluent2.microsoft.design/components/web/react/core/toast/usage)). Agrupe processos parecidos num único indicador: "Enviando 6 arquivos".

#### Acessibilidade

**Anuncie início, progresso e fim sem mover o foco.** Dê ao indicador um texto que descreva o que acontece, como "Carregando pedidos" ([gov.br](https://www.gov.br/ds/components/loading)). Marque a região que carrega com `aria-busy="true"` e anuncie a conclusão com `aria-live="polite"` no contêiner de destino, e não no skeleton ([Geist](https://vercel.com/geist/skeleton)). Use `role="status"` para mensagens de espera ([Fluent](https://fluent2.microsoft.design/wait-ux)), atendendo ao critério WCAG 2.2, 4.1.3. O progresso circular usa `role="progressbar"` com `aria-valuenow`; anuncie só alguns marcos do avanço, para não sobrecarregar o leitor de tela.

**Mantenha o foco no botão que carrega.** Marque-o com `aria-disabled="true"` em vez de `disabled`, para que continue focável, e use um elemento separado só para a mensagem do leitor de tela, fora do botão, porque nem todo leitor anuncia mudanças no texto de um botão ([DKFDS](https://designsystem.dk/komponenter/spinner/), [Geist](https://vercel.com/geist/spinner)). Se o botão sumir quando o conteúdo chegar, mova o foco para o primeiro elemento novo.

**Ofereça cancelar esperas longas.** Se a espera for longa, dê a opção de cancelar e voltar à tarefa anterior ([gov.br](https://www.gov.br/ds/components/loading)).

**Respeite o movimento reduzido e evite clarões.** Não use variações intensas de cor ou piscadas no indicador ([gov.br](https://www.gov.br/ds/components/loading); WCAG 2.2, 2.3.1). Com `prefers-reduced-motion`, o kit para as animações de `.tr-skeleton`, `.tr-spinner` e da barra indeterminada, e o controle de animações do produto também as desliga. Garanta que o texto de status continue comunicando a espera sem a animação. Não coloque controles focáveis dentro de um skeleton ([Geist](https://vercel.com/geist/skeleton)).

> **Divergência entre referências** Bloqueio: o DKFDS pede não cobrir a página inteira com um spinner; o gov.br prevê bloquear a tela ou parte dela com véu e superfície. O Trama permite bloquear a região afetada e trata a tela inteira como exceção, porque bloquear menos mantém o restante utilizável. Anúncio: o gov.br admite `aria-live="assertive"` para o status de carregamento; Fluent e Geist usam anúncio polido. Pelo critério de acessibilidade, o Trama usa `polite`, que não interrompe a leitura em curso.

### Considerações por plataforma

#### Web desktop

Com mouse, o cursor sobre uma região bloqueada indica espera; o restante da página mantém o cursor normal. Mostre o indicador sempre no mesmo lugar para cada tipo de tarefa, para que a pessoa saiba onde procurar o status ([HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)). Toasts de progresso ficam no canto em que o produto mostra notificações.

#### Web móvel

Redes móveis variam muito; o primeiro conteúdo útil deve aparecer cedo e o resto carregar depois. Atualize listas de forma automática e periódica, sem depender de a pessoa pedir cada atualização ([HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)). Se oferecer "puxar para atualizar", use o texto do controle só para informação útil, como a hora da última atualização.

#### Tablets e dobráveis

Em layouts de dois ou três painéis, cada painel carrega e mostra seu indicador de forma independente; a lista não deve ficar bloqueada enquanto o detalhe carrega. Ao abrir ou fechar um dobrável, não reinicie carregamentos já concluídos e preserve a posição de rolagem ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Indicadores de progresso
- Spinner
- Skeleton
- Feedback
- Estados vazios
- Movimento

#### Referências

- [Loading](https://www.gov.br/ds/components/loading) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Loading](https://developer.apple.com/design/human-interface-guidelines/loading) Apple HIG
- [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators) Apple HIG
- [Wait UX](https://fluent2.microsoft.design/wait-ux) Fluent 2
- [Toast](https://fluent2.microsoft.design/components/web/react/core/toast/usage) Fluent 2
- [Loading spinner](https://designsystem.dk/komponenter/spinner/) Det Fælles Designsystem
- [Inputfelter med hentet data](https://designsystem.dk/eksempler/patterns/hentet-data/) Det Fælles Designsystem
- [Loading indicator](https://designsystem.ontario.ca/components/detail/loading-indicator.html) Ontario Design System
- [Skeleton](https://vercel.com/geist/skeleton) Geist
- [Spinner](https://vercel.com/geist/spinner) Geist
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o progresso circular determinado, os tamanhos por lugar, o bloqueio de região, o cancelamento de esperas longas e a espera em formulários. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                         |

## Contas e autenticação

Peça uma conta só quando ela traz valor real, e torne entrar, criar a conta, recuperar o acesso e excluir a conta tarefas simples e seguras.

Uma conta é útil quando as pessoas precisam voltar regularmente para acessar ou atualizar seus dados ([GOV.UK](https://design-system.service.gov.uk/patterns/create-accounts/)). Ela também é uma barreira: muitas pessoas desistem quando precisam se cadastrar antes de fazer algo útil ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)). Use autenticação para restringir conteúdo, controlar quem acessa o quê, personalizar o que a pessoa vê e proteger os dados dela ([gov.br](https://www.gov.br/ds/components/signin)).

Este padrão cobre a decisão de exigir conta, a entrada com provedor de identidade e com senha, o cadastro, a força da senha, a confirmação de e-mail e telefone, o aviso de sessão expirando, a saída e a exclusão da conta.

### Boas práticas

#### Decidir se precisa de conta

**Exija conta só quando a função principal depende dela.** Se o serviço funciona sem conta, não crie contas ([GOV.UK](https://design-system.service.gov.uk/patterns/create-accounts/), [HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)). Para acompanhar uma solicitação pontual, envie um número de referência por e-mail ou SMS ([GOV.UK](https://design-system.service.gov.uk/patterns/create-accounts/)).

**Adie a entrada o máximo possível.** Deixe a pessoa usar a maior parte do produto antes de pedir a conta ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts), [GOV.UK](https://design-system.service.gov.uk/patterns/create-accounts/)).

**Explique o benefício** em uma frase curta na tela de entrada ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)).

#### Entrar com provedor de identidade

**Ofereça um provedor de identidade quando o público já tem cadastro nele.** Entrar com uma conta existente evita um cadastro novo e facilita o acesso a vários sistemas. Ofereça também o cadastro próprio, para quem não se sente confortável com o provedor, e permita vincular contas que existiam antes ([gov.br](https://www.gov.br/ds/components/signin)). Em produtos para órgãos públicos, o provedor costuma ser o gov.br.

**Nomeie o provedor no botão.** Escreva "Entrar com" seguido do nome ou da assinatura do provedor, como "Entrar com gov.br". Use até três palavras e mantenha o ícone de pessoa à esquerda do rótulo, ou a assinatura à direita ([gov.br](https://www.gov.br/ds/components/signin)). Um "Entrar" genérico não diz qual método será usado ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)).

**Agrupe os métodos de autenticação.** Quando houver várias formas de entrar, como CPF e senha, certificado digital, certificado em nuvem, banco credenciado, validação facial ou digital, agrupe-as de forma simples e compreensível ([gov.br](https://www.gov.br/ds/padroes/design/formulario), [gov.br](https://www.gov.br/ds/components/signin)). Mostre primeiro o método que a maioria usa e reúna os demais em uma seção recolhível. Cite apenas métodos disponíveis no dispositivo atual ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)).

**Mantenha o botão de entrada perto dos campos**, mesmo quando houver métodos alternativos, e deixe visíveis os caminhos para dúvidas frequentes, criação de conta e recuperação de acesso ([gov.br](https://www.gov.br/ds/components/signin)).

**Responda imediatamente ao acionamento.** Ao acionar Entrar, mostre um indicador de carregamento no próprio botão até o retorno do provedor ou do servidor ([gov.br](https://www.gov.br/ds/components/signin)).

> **Divergência entre referências** O gov.br pede que o rótulo do botão de entrada nunca quebre linha. A decisão D15 do Trama proíbe truncar rótulos de botão e manda quebrar a linha. O Trama mantém o rótulo curto, até três palavras, para que ele caiba em uma linha nas larguras comuns; quando não couber, como com zoom de 400%, a linha quebra, porque esconder parte do rótulo falha em WCAG 2.2, 1.4.10. Fontes: [gov.br](https://www.gov.br/ds/components/signin).

#### Criar a conta

**Use "Criar conta" em todo o produto.** Não alterne com "Cadastrar" ou "Registrar". Nos campos, use "Crie uma senha" para deixar claro que a pessoa vai criar o dado agora ([GOV.UK](https://design-system.service.gov.uk/patterns/create-accounts/)).

**Separe claramente criar conta e entrar.** Colocar as duas opções lado a lado não basta: as pessoas deixam de ver uma delas. Dedique a tela de cadastro só a essa tarefa e não peça a mesma informação duas vezes ([GOV.UK](https://design-system.service.gov.uk/patterns/create-accounts/)).

**Use o e-mail ou o CPF como nome de usuário.** Peça nomes de usuário personalizados só quando o produto atribui conteúdo público, e permita mudar o dado de acesso depois ([GOV.UK](https://design-system.service.gov.uk/patterns/create-a-username/)). Aceite o CPF com ou sem pontos e hífen e normalize no sistema, sem máscara que impeça digitar ou apagar.

**Peça só os dados com finalidade clara** e explique por que cada dado pessoal é coletado ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Veja Privacidade.

**Evite CAPTCHAs.** Eles testam funções cognitivas e reconhecimento de palavras e imagens, o que exclui pessoas por deficiência, cultura ou idioma ([GOV.UK](https://design-system.service.gov.uk/patterns/create-accounts/)).

#### Senhas

**Prefira chaves de acesso e segundo fator.** Chaves de acesso dispensam criar e lembrar senhas. Se usar senha, acrescente um segundo fator ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)) em vez de regras de senha mais rígidas ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/)).

**Defina regras simples e explique-as antes.** Exija no mínimo 8 caracteres, não imponha máximo, bloqueie senhas comuns e mostre as regras junto ao campo. Use as mesmas regras em todo lugar. Não obrigue a troca periódica ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/)).

**Mostre a força da senha com texto e dicas.** Ao criar a senha, mostre um medidor com três níveis escritos, Fraca, Média e Forte, e dicas para chegar a uma senha forte ([gov.br](https://www.gov.br/ds/padroes/design/formulario)): use uma frase com várias palavras, evite seu nome, CPF, nome da empresa ou uma palavra comum, e use uma senha diferente das anteriores. As dicas orientam; só as regras acima impedem o envio.

**Esconda a senha por padrão e permita mostrá-la.** A pessoa pode não estar em um lugar privado. Um botão "Mostrar senha" dispensa o campo de confirmação ([GOV.UK](https://design-system.service.gov.uk/components/password-input/)). Permita colar, porque gerenciadores de senha dependem disso. Use `autocomplete="new-password"` ao criar e `current-password` ao entrar, desative correção e maiúscula automáticas e não use `maxlength` ([GOV.UK](https://design-system.service.gov.uk/components/password-input/)).

> **Divergência entre referências** O gov.br pede um campo de confirmação de senha, sugere senhas com "pelo menos seis a oito caracteres" e nomeia os níveis do medidor como Baixa, Média e Alta. O GOV.UK dispensa a confirmação quando há "Mostrar senha", exige no mínimo 8 caracteres e registra que falta pesquisa sobre validação durante a digitação de senhas. O Trama aplica a decisão D5: mínimo de 8, sem máximo, sem confirmação quando há "Mostrar senha" (com mais margem de acessibilidade, porque evita digitar duas vezes), e adota o medidor do gov.br com os rótulos Fraca, Média e Forte, que descrevem a senha e não um risco. Fontes: [gov.br](https://www.gov.br/ds/padroes/design/formulario), [GOV.UK](https://design-system.service.gov.uk/components/password-input/), [GOV.UK](https://design-system.service.gov.uk/patterns/passwords/).

**Não revele qual dado está errado na entrada.** Diga que o CPF ou a senha não conferem, limpe o campo de senha e permita entre 5 e 10 tentativas antes de bloquear ou pedir verificações extras ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/)).

**Deixe sempre visível como recuperar e alterar a senha** ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Envie para o e-mail ou telefone cadastrado um link ou código com prazo. Nunca envie a senha por e-mail, avise sempre que uma senha for redefinida e não use perguntas de segurança nem lembretes de senha ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/)).

#### Confirmar e-mail e telefone

**Confirme o e-mail só quando for necessário,** como quando a redefinição de senha depende dele. O link expira após um prazo, após o primeiro uso, quando um novo link é enviado ou quando o e-mail muda. Permita reenviar e mostre o endereço usado ([GOV.UK](https://design-system.service.gov.uk/patterns/confirm-an-email-address/)).

**Use códigos por SMS como segundo fator.** Envie um código de 5 dígitos válido por 15 minutos, aceite espaços e hífens na digitação, ofereça o link "Não recebeu a mensagem?" e explique o que fazer sem acesso ao telefone ([GOV.UK](https://design-system.service.gov.uk/patterns/confirm-a-phone-number/)).

#### Sessão expirando e saída

**Avise antes de encerrar a sessão por inatividade.** Mostre um diálogo cerca de 5 minutos antes, com contagem regressiva e as ações "Continuar conectado" e "Sair". Diga se alterações não salvas serão perdidas. Depois do encerramento, leve a pessoa a uma página de saída ([DKFDS](https://designsystem.dk/eksempler/patterns/session-udloeber/)). O aviso nunca dá menos de 20 segundos para a pessoa reagir (WCAG 2.2, 2.2.1). O foco inicial vai para "Continuar conectado", a ação principal de um diálogo sem campos.

**Ponha a saída no menu da conta.** Depois da entrada, a pessoa chega à página inicial já autenticada e encontra "Sair" e o acesso aos seus dados no menu do avatar, no cabeçalho, ou no menu principal no celular ([gov.br](https://www.gov.br/ds/components/signin)).

#### Excluir a conta

**Se o produto cria contas, ele também precisa excluí-las.** A desativação sozinha não atende a esse requisito. Ofereça um caminho fácil de achar, informe quando a exclusão vai terminar e explique quais dados a lei obriga a manter ([HIG](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)). A confirmação final segue o padrão de ações destrutivas em Modalidade.

### Acessibilidade

Use `<button>` para o botão de entrada. Ícones decorativos ao lado do rótulo levam `aria-hidden="true"` e nenhum `title`, para não serem lidos duas vezes. Botões só com ícone, como os de redes sociais, levam `aria-label` e uma dica visível em hover e foco ([gov.br](https://www.gov.br/ds/components/signin)). Marque a região de entrada como um `<form>` com nome acessível, para que leitores de tela cheguem direto aos campos ([gov.br](https://www.gov.br/ds/components/signin)). O botão "Mostrar senha" usa `aria-pressed` e o medidor de força anuncia o nível com `aria-live="polite"`, sem depender da cor da barra.

### Considerações por plataforma

#### Web desktop

Garanta que gerenciadores de senha reconheçam os formulários: use `<form>`, campos com `name` e `autocomplete` corretos e o identificador no mesmo formulário da senha. Mantenha o formulário em uma coluna estreita.

#### Web móvel

Na classe Compacta, o botão do provedor ocupa a largura da coluna (`.tr-btn--block-compact`) e usa a densidade baixa, com área de toque maior ([gov.br](https://www.gov.br/ds/components/signin)). Coloque a ação de entrar no meio ou na parte de baixo da tela, ao alcance do polegar ([gov.br](https://www.gov.br/ds/components/signin)). Não há dica por hover: botões só com ícone precisam de ícones muito reconhecíveis e alvo de `--c-touch` ([gov.br](https://www.gov.br/ds/components/signin)). Use `inputmode="numeric"` no CPF e `autocomplete="one-time-code"` no código de verificação.

#### Tablets e dobráveis

Ao abrir ou fechar um dobrável durante o cadastro ou a entrada, o texto digitado e o teclado permanecem ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Na classe Expandida, mantenha o formulário em uma coluna estreita e centralizada.

### Recursos

#### Relacionados

- Privacidade
- Campos de texto
- Validação e mensagens de erro
- Cabeçalho
- Modalidade
- Legislação e normas

#### Referências

- [Sign-in (autenticação)](https://www.gov.br/ds/components/signin) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts) Apple HIG
- [Create accounts](https://design-system.service.gov.uk/patterns/create-accounts/) GOV.UK Design System
- [Passwords](https://design-system.service.gov.uk/patterns/passwords/) GOV.UK Design System
- [Password input](https://design-system.service.gov.uk/components/password-input/) GOV.UK Design System
- [Create a username](https://design-system.service.gov.uk/patterns/create-a-username/) GOV.UK Design System
- [Confirm an email address](https://design-system.service.gov.uk/patterns/confirm-an-email-address/) GOV.UK Design System
- [Confirm a phone number](https://design-system.service.gov.uk/patterns/confirm-a-phone-number/) GOV.UK Design System
- [Session udløber](https://designsystem.dk/eksempler/patterns/session-udloeber/) DKFDS
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                             |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta entrada com provedor de identidade, agrupamento dos métodos de autenticação, medidor de força de senha, CPF sem máscara bloqueante, saída pelo menu da conta e unidades por extenso no aviso de sessão. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                      |

