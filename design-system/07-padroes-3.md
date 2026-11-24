# Padrões: Estados vazios a Coletar feedback

## Estados vazios

Quando não há nada para mostrar, ocupe o lugar do conteúdo ausente com uma explicação curta e o próximo passo, para que a área vazia nunca pareça um defeito.

Uma área fica vazia por motivos muito diferentes: a pessoa ainda não criou nada, um filtro não encontrou resultados, todo o trabalho foi concluído, falta uma configuração ou permissão, a ação não é suportada ou o carregamento falhou. Cada caso pede uma mensagem e uma ação diferentes ([Geist](https://vercel.com/geist/empty-state), [gov.br](https://www.gov.br/ds/padroes/design/emptystates)). Projete esses estados desde o início do projeto, e não como acréscimo tardio ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)).

Estados vazios também são um bom lugar para orientar quem chega pela primeira vez, sem interromper ([Fluent](https://fluent2.microsoft.design/onboarding)). Erros que vêm de fora da aplicação, como endereço inexistente ou serviço fora do ar, não são estados vazios: usam as páginas de erro de Modelos de página.

### Anatomia

| Elemento | Uso                                                                     | No kit                        |
|----------|-------------------------------------------------------------------------|-------------------------------|
| Imagem   | Opcional e decorativa, coerente com a mensagem e proporcional ao espaço | `.tr-empty__art`              |
| Título   | Obrigatório. Frase curta que resume a situação                          | Cabeçalho real (`h2` ou `h3`) |
| Corpo    | Obrigatório. Explica o contexto e sugere a ação                         | Parágrafo                     |
| Ações    | Opcionais. Só quando houver algo a fazer agora                          | `.tr-btn` e `.tr-link`        |

A anatomia segue o gov.br ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)).

### Boas práticas

#### Tipos

**Escolha o tipo de estado vazio pela causa.** O Trama combina os tipos do Geist com os erros do gov.br ([Geist](https://vercel.com/geist/empty-state), [gov.br](https://www.gov.br/ds/padroes/design/emptystates)):

| Tipo                    | Quando                                                                                      | Conteúdo                                                                             |
|-------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Primeiro uso            | Ainda não há dados.                                                                         | Que dado vai aparecer ali e como inserir o primeiro.                                 |
| Conteúdo de exemplo     | Aprender mexendo é mais fácil que ler.                                                      | Dados iniciais que a pessoa pode editar ou excluir.                                  |
| Sem resultados          | Uma pesquisa ou filtro não encontrou nada.                                                  | O termo pesquisado, "Limpar filtros" e, se houver, link para a ajuda. Veja Pesquisa. |
| Etapa indisponível      | Uma etapa seguinte não pode ser exibida ainda.                                              | O que falta para liberá-la.                                                          |
| Concluído               | Todo o trabalho foi feito, como uma fila zerada.                                            | Confirmação neutra, sem ação obrigatória.                                            |
| Problema no sistema     | Um impedimento técnico impede exibir os dados.                                              | O que aconteceu, "Tentar novamente" e um código da ocorrência que possa ser copiado. |
| Ação não suportada      | A pessoa tentou algo que o serviço não aceita, como enviar um tipo de arquivo incompatível. | O que é aceito, no lugar onde o resultado apareceria.                                |
| Sem permissão           | A pessoa não pode ver o conteúdo.                                                           | Motivo e como solicitar acesso.                                                      |
| Configuração necessária | Falta um ajuste para os dados aparecerem.                                                   | Qual configuração fazer e um link para começá-la.                                    |

#### Conteúdo

**Escreva um título orientado à ação.** Prefira "Insira dados para visualizar o painel" a "Você não tem dados" ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)). Comece pelo objetivo e evite negar. Em erros e sem resultados, o título pode descrever o estado, desde que o corpo diga o que fazer.

**Acrescente informação nova no corpo.** O corpo não repete o título ([Geist](https://vercel.com/geist/empty-state)). Diga que tipo de dado aparecerá quando a área for preenchida, com poucas palavras, sem termos técnicos e sem tratar de outras áreas do produto ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)).

**Oriente sobre um problema por vez.** Não peça para resolver vários problemas: aponte o mais importante. Se houver várias etapas, leve a pessoa à primeira ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)).

**Nunca deixe a pessoa sem saída.** Se houver ação possível, inclua um botão ou link para ela ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)). Use uma ação e, só quando houver um caminho complementar, um link, posicionados logo abaixo do corpo. Três ações indicam um problema ([Geist](https://vercel.com/geist/empty-state)). Rótulos usam verbo e substantivo, como "Cadastrar contrato", e não "Começar" ou "OK".

**Mantenha o tom respeitoso e consistente.** Evite linguagem petulante e trate situações semelhantes com o mesmo padrão de imagem e texto ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)). Erros seguem a regra D6: nunca culpar a pessoa, sem humor e sem "Ops".

#### Posição e layout

**Substitua a estrutura inteira do conteúdo ausente.** Mostre o estado vazio no mesmo lugar onde os dados apareceriam: página, painel lateral, tabela, card. Numa tabela vazia, o estado vazio substitui cabeçalho, linhas, colunas e rodapé, para que a pessoa não perca tempo lendo estrutura sem conteúdo ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)).

**Faça** o estado vazio ocupar o lugar da tabela inteira.

**Não faça** cabeçalho de colunas sem linhas e um "Sem dados" sem explicação nem ação.

**Alinhe pelo espaço disponível.** Em espaços pequenos, como cards, células e painéis estreitos, alinhe tudo à esquerda; se o espaço for muito pequeno, centralize só a ilustração, com o texto à esquerda, ou use apenas texto. Em espaços amplos, use um bloco centralizado na horizontal e na vertical, ou uma margem lateral maior, para chamar a atenção ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)). O `.tr-empty` vem centralizado para áreas amplas.

**Dimensione a imagem pelo espaço e pelo texto.** Imagens horizontais ficam acima do texto; imagens verticais, à esquerda dele ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)). Nunca deixe a imagem chamar mais atenção que a mensagem.

**Com vários estados vazios na mesma tela, seja discreto.** Em painéis com muitos blocos, evite várias ilustrações coloridas e muitos botões. Use só texto ou imagens sóbrias, com links ou botões sutis ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)).

#### O que não é estado vazio

**Não use skeleton nem spinner para representar ausência de dados.** O skeleton promete conteúdo que vai chegar; quando não há nada a carregar, mostre o estado vazio ([Geist](https://vercel.com/geist/skeleton)). A tela sem nada faz a pessoa achar que o produto falhou ([HIG](https://developer.apple.com/design/human-interface-guidelines/loading)).

**Não guarde avisos permanentes num estado vazio.** Ele some quando a área se preenche. Avisos que precisam continuar visíveis vão para uma mensagem ([Geist](https://vercel.com/geist/empty-state)).

**Escolha a escala certa para falta de permissão.** Se a pessoa chega a uma página que não pode ver, use a página inteira; se só um bloco estiver bloqueado, use o estado vazio nesse bloco ([Geist](https://vercel.com/geist/empty-state)). Não use erro de validação para falta de permissão ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)).

**Separe estados vazios de páginas de erro.** Erros de protocolo, como página não encontrada (404), acesso proibido (403), tempo esgotado (408) ou falha do servidor (500), têm origem fora da aplicação e seguem o modelo de página de erro ([gov.br](https://www.gov.br/ds/padroes/design/emptystates), [gov.br](https://www.gov.br/ds/templates/erro)), com regras próprias para página não encontrada, serviço indisponível e problema no serviço ([GOV.UK](https://design-system.service.gov.uk/patterns/page-not-found-pages/)). Veja Modelos de página: base e erro.

**Faça** explicar o que aconteceu, tranquilizar sobre os dados e oferecer a recuperação.

**Não faça** jargão técnico, tom informal e nenhuma saída.

#### Acessibilidade

Toda a informação está no título e no corpo; a ilustração é decorativa. Use `alt=""` em imagens decorativas e não confie em `role="presentation"`, pouco reconhecido por navegadores ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)); a forma CSS de `.tr-empty__art` leva `aria-hidden="true"`. Quando um filtro muda e a lista fica vazia, envolva a região em `aria-live="polite"` para que leitores de tela anunciem o novo estado ([Geist](https://vercel.com/geist/empty-state)). O título é um cabeçalho real na hierarquia da página, e a ação entra na ordem de tabulação.

> **Divergência entre referências** Título: o Geist pede um título que descreva o estado; o gov.br pede um título positivo, orientado à ação. Pelo contexto brasileiro e pela regra D24 (comece pelo objetivo, não negue), o Trama orienta o título à ação e aceita a descrição do estado em erros e sem resultados. Ênfase da ação: o Geist usa ação principal; o gov.br usa botão de ênfase secundária e link. O Trama usa `.tr-btn--primary` só quando o estado vazio ocupa a área principal da página e a ação é a tarefa da tela; em cards, painéis e telas com vários estados vazios, usa `.tr-btn`, `.tr-btn--subtle` ou link. Alinhamento: o 1.0 centralizava sempre; o gov.br alinha à esquerda em espaços pequenos. O Trama passa a alinhar pelo espaço.

### Considerações por plataforma

#### Web desktop

Na área principal de uma página, centralize o bloco na largura e na altura disponíveis, mantendo a navegação e os filtros visíveis. Em cards, células e painéis laterais, alinhe à esquerda.

#### Web móvel

Mantenha o estado vazio curto: título, uma frase e uma ação. Posicione-o no topo da área de conteúdo, para que apareça sem rolagem. Em espaços muito reduzidos, use só texto, que evita problemas de legibilidade e de responsividade ([gov.br](https://www.gov.br/ds/padroes/design/emptystates)).

#### Tablets e dobráveis

Em dois painéis, cada painel tem o seu estado vazio, alinhado conforme a largura do painel. Um painel de detalhe sem seleção mostra uma instrução curta, como "Selecione um contrato para ver os detalhes", em vez de ficar em branco.

### Recursos

#### Relacionados

- Modelos de página: base e erro
- Onboarding
- Pesquisa
- Carregamento e espera
- Feedback
- Validação e mensagens de erro
- Skeleton
- Ilustração

#### Referências

- [Empty states](https://www.gov.br/ds/padroes/design/emptystates) gov.br DS
- [Template de erro](https://www.gov.br/ds/templates/erro) gov.br DS
- [Empty State](https://vercel.com/geist/empty-state) Geist
- [Skeleton](https://vercel.com/geist/skeleton) Geist
- [Onboarding](https://fluent2.microsoft.design/onboarding) Fluent 2
- [Page not found pages](https://design-system.service.gov.uk/patterns/page-not-found-pages/) GOV.UK Design System
- [Recover from validation errors](https://design-system.service.gov.uk/patterns/validation/) GOV.UK Design System
- [Loading](https://developer.apple.com/design/human-interface-guidelines/loading) Apple HIG

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                                                                               |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta anatomia, os tipos "Ação não suportada", "Configuração necessária" e "Etapa indisponível", títulos orientados à ação, substituição da estrutura inteira, alinhamento pelo espaço e vários estados vazios na mesma tela; as páginas de erro passam para Modelos de página. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                                                                        |

## Excesso de conteúdo

Quando o conteúdo não cabe no espaço, organize-o por prioridade e escolha entre rolar, revelar sob demanda, truncar ou levar a outro lugar, sem nunca esconder o que é essencial.

Excesso de conteúdo, também chamado de densidade informacional, reúne as técnicas que mostram ou ocultam partes do conteúdo conforme a prioridade da informação. Elas ajudam a acomodar o conteúdo no espaço da tela ou do componente, acrescentar informação complementar, ocultar o que é menos relevante e deixar o layout mais fácil de assimilar ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)).

Antes de aplicar qualquer técnica, revise o conteúdo. Se for possível simplificá-lo para caber no espaço, simplifique. As técnicas desta página não substituem um bom planejamento de conteúdo ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)).

### Três camadas de informação

Hierarquize o conteúdo antes de escolher a técnica. Mostrar tudo de uma vez gera sobrecarga cognitiva e afasta a pessoa, que chegou à página para resolver um problema específico. Agrupe o conteúdo em blocos por função e semelhança ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)).

| Camada       | O que é                                                                       | Onde fica                                                  | Técnicas                                                        |
|--------------|-------------------------------------------------------------------------------|------------------------------------------------------------|-----------------------------------------------------------------|
| Essencial    | Indispensável para executar a tarefa                                          | Visível na tela, de forma direta                           | Posição, agrupamento e rolagem. Nunca oculte nem trunque.       |
| Complementar | Apoia o essencial; para algumas pessoas é eventual, para outras é fundamental | Oculta ou parcialmente oculta, revelada por ação da pessoa | Expansão (acordeão), tooltip, menu, "Mostrar mais", truncamento |
| Adicional    | Menos importante; não precisa estar na tela de origem                         | Fora da tela, indicada por link ou botão                   | Diálogo, página interna, página externa                         |

Camadas e técnicas seguem o gov.br ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). As técnicas podem ser combinadas, e situações semelhantes usam a mesma técnica em todo o produto ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)).

### Boas práticas

#### Onde nunca ocultar nem truncar

**Quebre a linha em vez de truncar estes elementos:** títulos e cabeçalhos de página, itens de menu e de navegação, rótulos de botão, mensagens de erro, mensagens de validação e notificações ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). Também nunca oculte conteúdo essencial.

**Trunque só onde o Trama permite:** células de tabela, breadcrumb, nomes de arquivo, chips e parágrafos com "Mostrar mais". Em todos os casos, o texto completo continua acessível.

> **Divergência entre referências** O gov.br lista links longos e paginação entre os elementos que podem ser truncados, e o componente Modal do gov.br trunca títulos acima de duas linhas. O próprio padrão de excesso de conteúdo do gov.br proíbe truncar títulos. O Trama aplica a decisão D15: títulos quebram linha, links longos são reescritos com um texto mais curto, e a paginação resume páginas com reticências entre números, sem cortar texto. Fontes: [gov.br](https://www.gov.br/ds/padroes/design/contentoverflow), [gov.br](https://www.gov.br/ds/components/modal).

#### Rolagem

**Use a rolagem da página como forma padrão.** As pessoas conhecem a rolagem do navegador; não altere seu comportamento nem sua aparência ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). Suporte os gestos e atalhos de rolagem que as pessoas esperam ([HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views)).

**Use rolagem interna com bordas elevadas.** Em componentes como cards, painéis e diálogos, só o conteúdo interno rola, sob as margens do componente, e a página fica parada. Enquanto houver conteúdo oculto, a borda que o esconde sobe um nível de elevação e mostra a sombra correspondente ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). No Trama, use `.tr-scroll` com `header`, `div` e `footer`, e aplique `is-overflow-top` e `is-overflow-bottom` enquanto houver conteúdo acima ou abaixo. As bordas ficam na camada `--z-1`.

**Deixe parte do conteúdo seguinte visível.** Um item cortado na borda insinua que há mais para ver ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow), [HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views)). Ajuste a altura da área para que a borda não coincida com o fim de um item.

**Siga estas práticas para barras de rolagem** ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)):

- Oculte a barra quando todo o conteúdo estiver visível. Quem vê uma barra espera rolar. Use `overflow: auto`, nunca `scroll`.
- Use barras que se parecem com barras de rolagem. Não personalize a ponto de descaracterizá-las.
- Não exagere na quantidade de áreas com rolagem na mesma tela.
- Não coloque uma área rolável dentro de outra com a mesma orientação ([HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views)).
- Evite rolagens muito longas e mantenha o que é importante na área visível inicial.
- Considere pessoas com deficiência motora, pessoas com baixo letramento, que perdem a posição quando o conteúdo se move, e pessoas idosas, que têm dificuldade com itens pequenos que rolam.

**Evite rolagem horizontal.** Em testes, as pessoas desaprovam a rolagem horizontal. Na web, elas esperam rolar na vertical, e mover a visão em dois eixos é especialmente difícil para quem tem pouca habilidade de visualização espacial ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). Nunca use rolagem horizontal em páginas nem em diálogos ([gov.br](https://www.gov.br/ds/components/modal)). Em componentes, minimize-a: só tabelas de dados, mapas, gráficos e código, que dependem de duas dimensões, podem rolar na horizontal dentro do próprio contêiner (WCAG 2.2, 1.4.10).

#### Conteúdo oculto e parcialmente oculto

**Use expansão para blocos inteiros.** Um acordeão revela o conteúdo de uma vez e empurra o conteúdo seguinte para baixo ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)).

**Use tooltip para descrições curtas** de um elemento que pode não ser entendido, e menus suspensos para agrupar ações que não precisam estar visíveis, como as ações de uma linha de tabela ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). Indique visualmente que há algo para revelar.

**Use "Mostrar mais" para textos longos.** O botão mostra o conteúdo em partes mais fáceis de absorver e é mais visível que uma rolagem. Depois de expandido, ofereça "Mostrar menos" para recolher ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). Em listas longas, quando o desempenho importa, use "Carregar mais"; ao carregar, mova o foco para o primeiro item novo.

> **Divergência entre referências** O gov.br mostra variações de "Mostrar mais" que usam só um ícone. O GOV.UK registra evidência de que algumas pessoas evitam acionar o link que revela detalhes porque acham que ele as leva para fora da página. O Trama exige o texto "Mostrar mais" ou "Mostrar menos", em caixa de frase, em um botão com `aria-expanded`, e nunca um link. Fontes: [gov.br](https://www.gov.br/ds/padroes/design/contentoverflow), [GOV.UK](https://design-system.service.gov.uk/components/details/).

#### Truncamento

**Trunque com reticências e escolha a posição pelo conteúdo** ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)):

| Tipo          | Quando usar                                                                                                              | Exemplo                           |
|---------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Inicial       | O início da sequência se repete e o fim é o que distingue os itens, como caminhos de pasta                               | …/2026/contratos/aditivo-03.pdf   |
| Intermediário | Vários textos têm inícios e fins diferentes e o mesmo meio, ou o fim não pode ser cortado, como a extensão de um arquivo | relatorio-anual-secr…-v03.pdf     |
| Final         | O texto continua e o início basta para identificá-lo                                                                     | Rua das Acácias, 120, apartament… |

**Nunca deixe menos de três caracteres de uma palavra.** Conte só letras e números ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). Se o corte deixaria uma ou duas letras, corte antes da palavra.

**Use as classes do kit para o truncamento final.** `.tr-truncate` limita o texto a uma linha com reticências no fim; `.tr-clamp-2` e `.tr-clamp-3` limitam um bloco a duas ou três linhas. O CSS corta no ponto em que o espaço acaba e não garante os três caracteres; quando isso importar, ou para truncamento inicial e intermediário, corte o texto no código e mantenha o texto completo no nome acessível.

**Sempre dê acesso ao texto completo.** Mostre o texto inteiro em um tooltip que apareça em hover e em foco ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow), [HIG](https://developer.apple.com/design/human-interface-guidelines/entering-data)), ou use `title` mais o texto completo no nome acessível. Parágrafos com "Mostrar mais" dispensam o tooltip ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). Evite truncar dentro de áreas roláveis, a menos que a pessoa possa abrir o conteúdo completo em outra vista ([HIG](https://developer.apple.com/design/human-interface-guidelines/typography)).

**Não trunque o valor de campos editáveis.** Dimensione o campo para a entrada esperada: a pessoa erra mais quando não vê o que digitou ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Para textos longos, use uma área de texto.

#### Informações adicionais

**Escolha o destino pelo vínculo com a tarefa** ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)):

- **Diálogo:** quando a informação está ligada ao conteúdo de origem, mas é extensa demais para a mesma tela. Use com moderação.
- **Página interna:** quando a informação é extensa ou tem pouco vínculo com o conteúdo de origem. Evite quando interromper o fluxo prejudicar a tarefa.
- **Página externa:** só quando traz valor real, como uma legislação. Sinalize com o ícone de link externo (`.tr-link--external`) e o texto acessível "(site externo)". Se abrir em nova aba, diga "(abre em nova aba)" no texto do link.

**Faça** deixe o rótulo do botão quebrar a linha quando não couber, e reescreva-o mais curto se puder.

**Não faça** trunque o rótulo de um botão.

### Reflow e zoom de 400%

**Projete para que o conteúdo reflua sem perder nada.** Com 320 pixels CSS de largura, o conteúdo precisa caber sem rolagem em duas direções, exceto o que depende de duas dimensões (WCAG 2.2, 1.4.10). Essa largura equivale a uma janela de 1.280 pixels com zoom de 400%, e cai na classe Compacta do Trama. Por isso, com zoom alto, valem as regras da Web móvel: uma coluna, rolagem da página no lugar de rolagens internas e nada de rolagem horizontal.

**Teste nas bordas das classes de janela e com o zoom do navegador** ([HDS](https://hds.hel.fi/foundation/design-tokens/breakpoints)). Com ampliação de 400%, uma pessoa que usa ampliador pode não ver um botão alinhado à direita ([Ontario](https://designsystem.ontario.ca/components/detail/buttons.html)): alinhe as ações ao início.

**Reduza o truncamento quando o texto cresce.** Mostre tanto texto útil no maior tamanho de fonte quanto no tamanho padrão. Com fonte grande, empilhe itens que ficavam lado a lado e reduza o número de colunas ([HIG](https://developer.apple.com/design/human-interface-guidelines/typography)). Texto ampliado em 200% não pode perder conteúdo (WCAG 2.2, 1.4.4).

**Não use alturas fixas em contêineres de texto.** Quando a pessoa aumenta o espaçamento entre linhas, letras e palavras, o texto precisa continuar visível (WCAG 2.2, 1.4.12). Use `min-height` e, em `.tr-scroll`, troque a altura máxima por fluxo normal na classe Compacta.

### Acessibilidade

**Torne a área rolável alcançável pelo teclado.** Uma área com rolagem interna sem elementos focáveis precisa de `tabindex="0"`, `role="region"` e um nome acessível, para que a pessoa role com as setas (WCAG 2.2, 2.1.1). O foco usa o anel padrão de `--t-focus`.

**Ligue o botão expansor ao conteúdo.** "Mostrar mais" usa `aria-expanded` e `aria-controls`, e o foco permanece no botão depois de expandir. Com `.tr-clamp-*`, o texto completo continua no documento e é lido por leitores de tela; o botão serve a quem vê a tela.

**Ofereça o texto completo de elementos truncados** no nome acessível e em um tooltip que apareça também com o foco do teclado. Um texto truncado que não é focável, como o de uma célula de tabela, precisa de outro caminho até o texto completo, como abrir o detalhe da linha.

### Tokens usados

| Elemento                       | Token                                               |
|--------------------------------|-----------------------------------------------------|
| Borda de rolagem elevada       | `--t-shadow-key`, camada `--z-1`                    |
| Superfície da área rolável     | `--t-surface-raised`, `--t-border-subtle`, `--r-lg` |
| Espaço interno da área rolável | `--sp-300` na vertical, `--sp-400` na horizontal    |
| Expansão e recolhimento        | `--m-normal`, `--m-ease-standard`                   |

### Considerações por plataforma

#### Web desktop

Mostre o tooltip do texto truncado em hover e em foco. Barras de rolagem do sistema podem ficar ocultas até a pessoa rolar; por isso, a sombra das bordas e o item cortado são as pistas principais ([HIG](https://developer.apple.com/design/human-interface-guidelines/scroll-views)).

#### Web móvel

No celular, espera-se mais rolagem, e a da tela é preferível às rolagens internas. A barra de rolagem costuma ser dispensável, mas deixe pistas de que há mais conteúdo, e mostre parte do conteúdo antes da dobra para motivar a rolagem. Deixe áreas seguras, sem elementos interativos, onde a pessoa possa arrastar a tela sem toques acidentais ([gov.br](https://www.gov.br/ds/padroes/design/contentoverflow)). Não há hover: dê acesso ao texto completo por toque, abrindo o detalhe do item.

#### Tablets e dobráveis

Em telas grandes, use o espaço extra para mostrar mais conteúdo em painéis, em vez de truncar, e reduza a necessidade de "Mostrar mais". Ao abrir ou fechar um dobrável, mantenha a posição de rolagem e o estado de expansão ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Acordeão
- Tooltips
- Tabelas
- Modalidade
- Layout e grid
- Escrita e conteúdo

#### Referências

- [Content overflow](https://www.gov.br/ds/padroes/design/contentoverflow) gov.br DS
- [Modal (janela de exibição)](https://www.gov.br/ds/components/modal) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views) Apple HIG
- [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) Apple HIG
- [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data) Apple HIG
- [Details](https://design-system.service.gov.uk/components/details/) GOV.UK Design System
- [Buttons](https://designsystem.ontario.ca/components/detail/buttons.html) Ontario Design System
- [Breakpoints](https://hds.hel.fi/foundation/design-tokens/breakpoints) Helsinki Design System
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## Estruturar a navegação

Uma boa navegação nasce da lista de tarefas das pessoas, organizada em hierarquia, e usa o componente certo para cada movimento entre telas.

Navegação é o processo pelo qual as pessoas acessam as telas e funcionalidades de um produto, realizam tarefas, percorrem fluxos de etapas e chegam à informação que procuram ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). Esta página trata da estrutura: como decidir o que entra na navegação, em que ordem e com quais componentes. Os componentes em si estão em Navegação lateral, Barra de navegação e rail, Breadcrumb, Paginação e Campo de pesquisa.

Uma boa navegação é fácil, intuitiva e previsível, tanto para quem chega pela primeira vez quanto para quem usa o produto todo dia; oferece opções relacionadas; guia a pessoa sem deixar dúvida sobre o próximo passo; e dá destaque ao que leva às tarefas mais importantes ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)).

### Estruturar o processo

Antes de escolher componentes, percorra cinco passos ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)):

1.  **Inventário.** Identifique quem usa o produto e quais funcionalidades, tarefas e conteúdos são mais comuns para cada perfil.
2.  **Priorização.** Classifique essas atividades em prioridade alta, média e baixa para cada perfil e revise quando as necessidades mudarem. Dê destaque na interface ao que é prioritário ou mais acessado.
3.  **Sequência.** Descubra os caminhos que as pessoas percorrem, use-os para estruturar a navegação, dê ênfase aos destinos frequentes e agrupe tarefas relacionadas.
4.  **Desconstrução.** Divida tarefas complexas em atividades menores, como um formulário longo em etapas. Partes menores são mais fáceis de aprender e podem ser usadas separadamente.
5.  **Hierarquia.** Organize o conteúdo em níveis, com o mais relevante no topo, dando acesso às camadas de baixo.

**Simplifique a jornada antes de criar navegação.** Serviços com uma jornada clara de começo ao fim não precisam de links de navegação; use uma lista de tarefas ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)). Navegação faz sentido em produtos usados com frequência, com várias tarefas e sem ordem fixa entre elas.

#### Elementos da hierarquia

| Elemento      | O que é                                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------------------------|
| Início        | Entrada principal: apresenta o produto e traz o componente principal de navegação, que leva às outras camadas.    |
| Pais e filhos | O nível de cima é o pai; os de baixo, filhos. Mantenha sempre o acesso entre eles.                                |
| Irmãos        | Níveis com o mesmo pai, em geral de mesma prioridade e contexto parecido.                                         |
| Fluxo         | O caminho entre níveis; ele define o tipo de navegação, como descer de pai para filho ou subir de filho para pai. |
| Hiperlinks    | Atalhos para qualquer nível, mesmo não adjacente, ou para fora do produto.                                        |

Os cinco elementos vêm do gov.br ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). O Trama limita a dois os níveis visíveis numa mesma navegação lateral; níveis mais profundos usam uma lista intermediária numa split view ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)).

### Tipos de navegação e componentes

O gov.br classifica o movimento entre telas em três tipos: lateral, progressiva e reversa ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). A tabela aponta o componente do Trama para cada um.

| Tipo                    | Movimento                                              | Componentes do Trama                                                                                                                      |
|-------------------------|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Lateral                 | Entre irmãos do mesmo nível                            | Navegação lateral e barra de navegação e rail (nível superior); abas e listas (qualquer nível); carrossel (conteúdos irmãos em sequência) |
| Progressiva descendente | De pai para filho                                      | Cards interativos, listas com link, categorias da navegação lateral                                                                       |
| Progressiva sequencial  | Por etapas ordenadas de um fluxo ou por lotes de itens | Indicador de etapas com formulários em etapas; paginação                                                                                  |
| Progressiva direta      | De qualquer tela para qualquer outra                   | Links, tags de link, campo de pesquisa, botão Entrar                                                                                      |
| Reversa cronológica     | Volta pelo histórico recente                           | Botão Voltar do navegador; link de voltar (Breadcrumb)                                                                                    |
| Reversa ascendente      | Sobe pela hierarquia até o Início                      | Breadcrumb; link “Voltar para \[página pai\]”                                                                                             |

> **Divergência entre referências** O gov.br lista janelas modais e o Magic Button entre os componentes de navegação descendente e recomenda um botão “Voltar” dentro da aplicação para a navegação cronológica ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). O GOV.UK usa um link de voltar no topo da página ([GOV.UK](https://design-system.service.gov.uk/components/back-link/)). O Trama usa diálogos só para tarefas curtas que não mudam de lugar, sem tratá-los como nível da hierarquia, e mantém o link de voltar, porque voltar é navegação e navegação usa link, regra do Trama em Botões e Links. A palavra continua “Voltar” (vocabulário D7).

### Boas práticas

#### Navegação lateral

**Deixe sempre visíveis os componentes que levam aos níveis principais.** A pessoa precisa ter acesso imediato às telas principais de qualquer lugar ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao), [HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)).

**Evite listas extensas.** Menus, abas e listas com muitos itens dificultam a escolha; ofereça o que realmente importa ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). Liste só as seções principais, sem tentar reproduzir o mapa do site ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)).

**No celular, destaque o botão que abre a navegação recolhida.** A pessoa precisa ter certeza de onde está a navegação principal ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)).

#### Navegação progressiva

**Sinalize a descida.** Use pistas visuais, como um chevron no fim do card ou da linha, para mostrar que o item leva a um nível inferior ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)).

**Em fluxos sequenciais, reforce o botão que avança.** Use a ação primária “Continuar” em cada etapa e “Concluir” na última ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao); vocabulário D7).

**Depois de uma navegação direta, mostre onde a pessoa está.** Quem chega por pesquisa ou por link cai no meio da hierarquia; mantenha breadcrumb e navegação visíveis para ela entender o caminho e voltar ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)).

#### Navegação reversa

**Volte ao estado e à rolagem anteriores.** Sempre que possível, a tela anterior reaparece como a pessoa a deixou: filtros, página da lista, abas, campos preenchidos e posição de rolagem ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao), [GOV.UK](https://design-system.service.gov.uk/components/back-link/)). Cada seção da barra de navegação guarda o próprio estado ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)). Use endereços próprios para cada estado relevante, para que o botão Voltar do navegador funcione.

**Avise quando a tela anterior não existe mais.** Se o item foi excluído ou o prazo expirou, mostre uma mensagem clara que diga o que aconteceu e para onde ir, usando um estado vazio, uma página de erro ou uma mensagem ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). Sem culpar a pessoa: “Este processo foi arquivado em 3 de outubro. Veja os processos arquivados.”

**Deixe clara a relação entre pai e filho.** A pessoa precisa encontrar o acesso à tela pai com facilidade ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)).

**Faça** Quando a pessoa volta para uma tela que não existe mais, diga o que aconteceu e ofereça um caminho.

**Não faça** Mostre um erro genérico, sem contexto e sem saída.

### Padrões de navegação

Padrões combinam componentes para atender necessidades diferentes; hierarquias profundas pedem padrões diferentes dos de produtos simples ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)).

| Padrão                            | Como funciona                                                                      | Quando usar                                                                                                   |
|-----------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Embutida                          | Os controles de navegação fazem parte do próprio conteúdo                          | Poucos níveis, uma visualização principal forte que reúne as tarefas comuns, uso pouco frequente              |
| Aninhada                          | Filhos agrupados abaixo dos pais, deixando os níveis evidentes                     | Navegação lateral, estruturas profundas, acesso a itens de primeiro nível a partir de vistas não relacionadas |
| Aninhada com expansão ou dropdown | O mesmo, com filhos que abrem e fecham                                             | Pouco espaço: responsividade, celular, desktop com tela cheia de conteúdo                                     |
| Em cascata                        | Filhos ao lado dos pais, em colunas; no celular, uma coluna por vez                | Os mesmos casos da aninhada, quando a largura permite colunas                                                 |
| Combinada                         | Dois ou mais padrões juntos, como navegação lateral entre pais e abas entre filhos | Necessidades específicas, com cautela                                                                         |

Os padrões e seus usos vêm do gov.br ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). No Trama, a cascata corresponde à split view: lista de pais, lista de filhos e detalhe, que na classe Compacta se mostram uma tela por vez. Ao combinar, evite que a mesma coisa apareça em dois lugares: não repita itens entre a navegação principal e a da página ([gov.br DS](https://www.gov.br/ds/components/menu)).

**Ofereça um controle visível para cada gesto.** O gov.br descreve a navegação gestual, como deslizar entre itens irmãos ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). No Trama, todo gesto tem um controle visível equivalente (WCAG 2.2, 2.5.1); veja Toque e gestos.

### Considerações por plataforma

A forma da navegação principal muda com a classe de janela, como recomenda o One UI: barra na base em telas pequenas, rail na lateral em telas médias e navegação completa visível em telas grandes ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

| Classe de janela              | Painéis | Navegação principal            | Breadcrumb      |
|-------------------------------|---------|--------------------------------|-----------------|
| Compacta (\< 600)             | 1       | Barra inferior e drawer modal  | Especial        |
| Média (600 a 839)             | 1 ou 2  | Rail e drawer modal            | Padrão truncado |
| Expandida (840 a 1199)        | 2       | Rail ou navegação lateral fixa | Padrão          |
| Grande e Extragrande (≥ 1200) | 2 ou 3  | Navegação lateral fixa         | Padrão          |

#### Web desktop

Mostre a navegação junto ao conteúdo; menus não ficam ocultos quando há espaço ([gov.br DS](https://www.gov.br/ds/components/menu), [One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)). A HIG pede no máximo dois níveis numa barra lateral e uma lista intermediária para hierarquias maiores ([HIG](https://developer.apple.com/design/human-interface-guidelines/sidebars)).

#### Web móvel

Na classe Compacta, a hierarquia achata: um painel por vez, barra inferior para três a cinco seções e drawer para o resto. A navegação em cascata vira uma sequência de telas, cada uma com caminho de volta ao pai. Sem hover, todo destino precisa de rótulo visível ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)).

#### Tablets e dobráveis

Telas grandes permitem achatar a navegação com vários painéis, para a pessoa chegar ao conteúdo sem trocar a tela inteira ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Para tarefas curtas, use um popover junto ao elemento tocado em vez de outra tela ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)). Ao abrir ou fechar o dobrável, a navegação muda de forma e a pessoa continua no mesmo ponto, com a mesma rolagem e o texto digitado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Navegação lateral
- Barra de navegação e rail
- Breadcrumb
- Paginação
- Pesquisa
- Painéis e split view
- Layout e grid

#### Referências

- [Navegação](https://www.gov.br/ds/padroes/design/navegacao) gov.br DS
- [Menu de Navegação](https://www.gov.br/ds/components/menu) gov.br DS
- [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) Apple HIG
- [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) Apple HIG
- [Navigate a service](https://design-system.service.gov.uk/patterns/navigate-a-service/) GOV.UK Design System
- [Back link](https://design-system.service.gov.uk/components/back-link/) GOV.UK Design System
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Layout design for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## Modelos de página: base e erro

Os modelos de página definem onde fica cada área da tela, como ela se comporta em cada largura e o que muda quando algo dá errado.

Um modelo de página é uma estrutura pronta que define a organização, o comportamento e a localização das áreas do layout, e as variações de cada área em cada classe de janela ([gov.br](https://www.gov.br/ds/templates/base)). Começar de um modelo poupa tempo e mantém as páginas consistentes ([gov.br](https://www.gov.br/ds/templates/visao-geral), [GOV.UK](https://design-system.service.gov.uk/styles/page-template/)). O Trama oferece dois: a **página base**, ponto de partida de todas as páginas, e a **página de erro**, com três casos: página não encontrada, serviço indisponível e problema no serviço.

### Página base

A página base tem cinco áreas ([gov.br](https://www.gov.br/ds/templates/base)):

| Área        | Uso         | Conteúdo                                                                                                                                               |
|-------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cabeçalho   | Obrigatória | Só o cabeçalho e suas variações. A altura varia com o tipo usado.                                                                                      |
| Navegação   | Opcional    | Só a navegação lateral, à esquerda do conteúdo.                                                                                                        |
| Localização | Opcional    | O breadcrumb, primeiro item da área de conteúdo. Dispensável na página inicial e em telas de celular ([gov.br](https://www.gov.br/ds/templates/base)). |
| Conteúdo    | Obrigatória | O `<main>`, com o H1 e todo o conteúdo específico da página.                                                                                           |
| Rodapé      | Obrigatória | Só o rodapé e suas variações.                                                                                                                          |

#### Boas práticas da página base

**Use a rolagem do navegador para a página.** A área de conteúdo cresce com o que contém, e a pessoa rola a página inteira. A área de navegação é a única que pode ter barra de rolagem própria ([gov.br](https://www.gov.br/ds/templates/base)). Rolagens internas na área de conteúdo dificultam o uso com teclado e com zoom.

**Escolha largura fixa ou fluida pelo tipo de produto.** Largura fixa centraliza o conteúdo com `max-width` e serve a portais e conteúdo informativo, em que o texto não deve mudar de forma com a largura da tela. Largura fluida aproveita toda a tela e serve a sistemas e ferramentas ([gov.br](https://www.gov.br/ds/templates/base); D18). Na classe Compacta, a página é sempre fluida. Em qualquer caso, o fundo do cabeçalho e do rodapé vai de ponta a ponta, e o conteúdo deles se alinha ao grid ([gov.br](https://www.gov.br/ds/templates/base)). O GOV.UK usa largura máxima padrão de 1020px e permite ampliá-la quando o conteúdo pede ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)).

**Limite a largura do texto corrido.** Em páginas de texto, mantenha o conteúdo principal numa coluna de dois terços, para que as linhas não passem de cerca de 75 caracteres ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)). Veja Layout e grid.

**Projete primeiro para a tela pequena.** Comece com uma coluna e acrescente colunas conforme a largura aumenta. Projete para classes de janela, sem supor dispositivos ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)).

**Esconda a navegação quando faltar espaço.** Na classe Compacta, a navegação fica oculta até ser pedida pelo botão Menu do cabeçalho e aparece como gaveta flutuante à esquerda ou como barra inferior. Quando ela precisa de atenção total, ocupa toda a altura e usa véu sobre o resto da página. A navegação persistente, que empurra o conteúdo, serve à classe Expandida e maiores ([gov.br](https://www.gov.br/ds/templates/base)). Veja Drawers e Barra de navegação e rail.

**Ofereça links de pular para as áreas principais.** Quem usa teclado precisa saber onde está o foco, alcançar todos os elementos interativos e saltar a navegação quando há muitos links ([gov.br](https://www.gov.br/ds/templates/base)). Crie destinos para o conteúdo principal, a navegação e as áreas de suporte, como a pesquisa. Veja Links de pular.

**Respeite os espaços mínimos entre áreas.** O Trama define: `--sp-600` abaixo do cabeçalho, à direita da navegação e abaixo do breadcrumb, e `--sp-1000` acima do rodapé. O gov.br define os mesmos quatro espaços mínimos com tokens próprios ([gov.br](https://www.gov.br/ds/templates/base)). Margens vizinhas não se somam: vale a maior (D19).

``` code
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Meus pedidos | Licenças e alvarás</title>
</head>
<body>
  <div class="tr-skiplinks">…</div>
  <header class="tr-header">…</header>
  <div class="pagina">
    <nav id="navegacao" class="tr-nav" aria-label="Seções">…</nav>
    <div class="coluna">
      <nav class="tr-breadcrumb" aria-label="Breadcrumb">…</nav>
      <main id="conteudo" tabindex="-1">
        <h1>Meus pedidos</h1>
        …
      </main>
    </div>
  </div>
  <div class="tr-inverse"><footer id="rodape" class="tr-footer">…</footer></div>
</body>
</html>
```

O `<title>` começa pelo assunto da página e termina no nome do produto. As classes `pagina` e `coluna` são o layout do produto, fora do kit. O breadcrumb fica no topo da coluna de conteúdo, antes do `<main>`, para que "Pular para o conteúdo principal" salte também o breadcrumb ([GOV.UK](https://design-system.service.gov.uk/patterns/navigate-a-service/)). O gov.br trata o breadcrumb como o primeiro item da área de conteúdo ([gov.br](https://www.gov.br/ds/templates/base)); a posição visual é a mesma, e o Trama adota a marcação do GOV.UK.

### Página de erro

A página de erro usa a mesma estrutura da base, com mudanças no cabeçalho e no rodapé e com a área de conteúdo dividida em área informativa e área de suporte ([gov.br](https://www.gov.br/ds/templates/erro)).

#### Anatomia da página de erro

1.  **Cabeçalho compacto** (obrigatório): mostra que a pessoa ainda está no produto certo, para que ela não se sinta abandonada. Só a marca e os links necessários ([gov.br](https://www.gov.br/ds/templates/erro)).
2.  **Área informativa** (obrigatória): até três níveis de texto, nesta ordem ([gov.br](https://www.gov.br/ds/templates/erro)):
    - **Texto principal**: o H1, que diz o que aconteceu.
    - **Texto secundário**: complementa o principal e diz o que fazer.
    - **Texto de apoio** (opcional): explica a causa provável ou pede um relato.

    Uma imagem de apoio é opcional e nunca chama mais atenção que o texto ([gov.br](https://www.gov.br/ds/templates/erro)); quando usada, é decorativa.
3.  **Área de suporte** (opcional): pesquisa, sugestões e links de saída ([gov.br](https://www.gov.br/ds/templates/erro)).
4.  **Rodapé compacto** (obrigatório): informação legal e contato; quanto mais simples, melhor ([gov.br](https://www.gov.br/ds/templates/erro)).

#### Boas práticas da página de erro

**Diga o que aconteceu sem culpar a pessoa.** Os textos nunca dão a entender que o erro foi da pessoa, mesmo que tenha sido; são específicos sobre o que aconteceu e sugerem passos para resolver ([gov.br](https://www.gov.br/ds/templates/erro); D6). Use linguagem simples, compreensível para quem não é técnico.

**Mantenha o tom neutro.** Sem humor, sem "Ops", sem jargão como "404", "500" ou "requisição inválida" e sem texto vermelho de alerta ([GOV.UK](https://design-system.service.gov.uk/patterns/page-not-found-pages/); D6). Não use breadcrumb ([GOV.UK](https://design-system.service.gov.uk/patterns/page-not-found-pages/)).

**Ponha a pesquisa no conteúdo.** Quem chega a uma página de erro está perdido. Um campo de pesquisa na área de conteúdo ganha mais destaque do que o do cabeçalho, e sugestões de termos válidos ajudam a recomeçar ([gov.br](https://www.gov.br/ds/templates/erro)). Use a pesquisa na página não encontrada; nas páginas de serviço indisponível e de problema no serviço, ela não resolve a necessidade.

**Ofereça saídas como links.** Página inicial, página anterior e um canal para relatar o problema ([gov.br](https://www.gov.br/ds/templates/erro)). Como levam a outras páginas, são elementos `<a>`, mesmo com aparência de botão. Com três ou mais, empilhe-os na vertical ([gov.br](https://www.gov.br/ds/templates/erro)).

**Corrija a causa.** Registre todos os erros e corrija-os o quanto antes ([GOV.UK](https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/)). Teste todos os links e mantenha redirecionamentos para endereços antigos que aparecem em cartas, formulários e outros sites ([GOV.UK](https://design-system.service.gov.uk/patterns/page-not-found-pages/)).

> **Divergência entre referências** O gov.br sugere linguagem "leve e descontraída", mensagem otimista e imagem com tom humanizado e até engraçado na página de erro ([gov.br](https://www.gov.br/ds/templates/erro)). O GOV.UK proíbe palavras informais ou humorísticas ([GOV.UK](https://design-system.service.gov.uk/patterns/page-not-found-pages/)), e o DKFDS usa tom neutro no exemplo de página não encontrada ([DKFDS](https://designsystem.dk/pages/eksempler/siden-kunne-ikke-findes-1/)). O Trama mantém tom neutro (D6). O DKFDS cita o código entre parênteses, "fejl 404"; o Trama segue o GOV.UK e deixa o código fora do texto. O gov.br usa botões para "Ir para Página Anterior" e "Ir para Página Principal"; o Trama usa links, porque são navegação (veja Construir componentes).

#### Casos de erro

| Caso                  | Quando                                                                                                                                                                                                                                | Conteúdo obrigatório                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Página não encontrada | O endereço não existe: link quebrado, endereço digitado ou copiado errado, página movida ou excluída ([GOV.UK](https://design-system.service.gov.uk/patterns/page-not-found-pages/), [gov.br](https://www.gov.br/ds/templates/erro)). | H1 "Página não encontrada", pesquisa, links de saída e contato, se houver e ajudar ([GOV.UK](https://design-system.service.gov.uk/patterns/page-not-found-pages/)).                                                                                                                                                                                                                   |
| Serviço indisponível  | O serviço foi fechado de propósito, por um período ou para sempre ([GOV.UK](https://design-system.service.gov.uk/patterns/service-unavailable-pages/)).                                                                               | H1 "O serviço está indisponível"; dia, data e hora da volta, ou o que fazer se fechou para sempre; o que aconteceu com as respostas de quem estava no meio do processo; contato; link para outro serviço que resolva a mesma necessidade ([GOV.UK](https://design-system.service.gov.uk/patterns/service-unavailable-pages/)). Evite palavras vagas como "manutenção" ou "melhorias". |
| Problema no serviço   | Qualquer erro inesperado. Use a mesma página para todos ([GOV.UK](https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/)).                                                                                    | H1 "Houve um problema no serviço"; "Tente novamente mais tarde." como parágrafo; o que aconteceu com as respostas; contato; link para outro serviço. Evite "Estamos com dificuldades técnicas" ([GOV.UK](https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/)).                                                                                             |

**Tenha uma página de indisponibilidade genérica pronta.** Use-a quando precisar fechar o serviço sem tempo de redigir, e atualize-a assim que souber quando ele volta ([GOV.UK](https://design-system.service.gov.uk/patterns/service-unavailable-pages/)). Antes de um serviço sazonal abrir, não mostre contato ([GOV.UK](https://design-system.service.gov.uk/patterns/service-unavailable-pages/)).

**Guarde o que a pessoa já preencheu.** Num problema no serviço, mantenha as respostas por um tempo razoável para que ela retome a jornada quando o serviço voltar. Mostre a página de problema só por pouco tempo; se o problema não se resolve logo, feche o serviço e use a página de indisponível ([GOV.UK](https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/)).

**Dê o contato completo ou um link para ele.** Mostre telefones e horários de atendimento na própria página, ou um link para uma página que os traga ([GOV.UK](https://design-system.service.gov.uk/patterns/service-unavailable-pages/)). Num problema no serviço, um código de ocorrência que a pessoa possa copiar ajuda o atendimento; ponha-o no texto de apoio, em `.tr-mono`.

> **Nota** Os títulos do GOV.UK para indisponível e problema no serviço começam com "Sorry" (desculpe). O próprio GOV.UK lista como pesquisa pendente se as pessoas esperam "por favor" e "desculpe" nessas páginas ([GOV.UK](https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/)). O Trama usa títulos diretos, que dizem o estado, e deixa o pedido de desculpas para o texto secundário quando a falha é do produto. Estados vazios dentro de uma página continuam em Estados vazios; o gov.br também separa os dois temas ([gov.br](https://www.gov.br/ds/templates/erro)).

#### Acessibilidade

O `<title>` de uma página de erro começa pelo problema: "Página não encontrada \| Licenças e alvarás" ([GOV.UK](https://design-system.service.gov.uk/patterns/page-not-found-pages/)). O texto principal é o único H1 e recebe o foco ao carregar (D13). A página de erro também tem links de pular, landmarks e o atributo `lang`. O servidor devolve o código de status correto, para que buscadores e ferramentas entendam o erro sem que ele apareça no texto.

### Considerações por plataforma

#### Web desktop

Use a navegação persistente à esquerda na classe Expandida e maiores. Em portais, use largura fixa; em sistemas, fluida. Na página de erro, os links de saída podem ficar em linha quando forem dois.

#### Web móvel

A página é fluida, em uma coluna. A navegação abre por um botão no cabeçalho, como gaveta ou barra inferior ([gov.br](https://www.gov.br/ds/templates/base)). O breadcrumb pode sair ou virar um link para o nível acima. Na página de erro, os links de saída ocupam a largura toda, empilhados.

#### Tablets e dobráveis

Na classe Média, a navegação fica recolhida por padrão. O gov.br admite largura fixa num tablet em paisagem quando o conteúdo pede ([gov.br](https://www.gov.br/ds/templates/base)). Num dobrável aberto, a navegação persistente pode ocupar um lado da dobra e o conteúdo o outro; veja Postura e dobra.

### Recursos

#### Relacionados

- Cabeçalho
- Rodapé
- Links de pular
- Layout e grid
- Estruturar a navegação
- Estados vazios
- Validação e mensagens de erro

#### Referências

- [Templates: visão geral](https://www.gov.br/ds/templates/visao-geral) gov.br DS
- [Template Base](https://www.gov.br/ds/templates/base) gov.br DS
- [Template de Erro](https://www.gov.br/ds/templates/erro) gov.br DS
- [Page template](https://design-system.service.gov.uk/styles/page-template/) GOV.UK Design System
- [Layout](https://design-system.service.gov.uk/styles/layout/) GOV.UK Design System
- [Navigate a service](https://design-system.service.gov.uk/patterns/navigate-a-service/) GOV.UK Design System
- [Page not found pages](https://design-system.service.gov.uk/patterns/page-not-found-pages/) GOV.UK Design System
- [Service unavailable pages](https://design-system.service.gov.uk/patterns/service-unavailable-pages/) GOV.UK Design System
- [There is a problem with the service pages](https://design-system.service.gov.uk/patterns/problem-with-the-service-pages/) GOV.UK Design System
- [Siden kunne ikke findes (exemplo)](https://designsystem.dk/pages/eksempler/siden-kunne-ikke-findes-1/) DKFDS

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. Recebe os casos de página não encontrada, serviço indisponível e problema no serviço, antes em Estados vazios. |

## Consentimento de cookies

Informe quais cookies o produto usa e deixe a pessoa aceitar ou recusar os não essenciais com o mesmo esforço, sem bloquear a página e sem gravar nada antes da escolha.

Use este padrão sempre que o produto gravar no dispositivo da pessoa qualquer coisa que não seja essencial para o serviço funcionar. Além de cookies, isso inclui armazenamento local do HTML5, service workers e outras tecnologias que guardam arquivos no dispositivo ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)). No Padrão Digital de Governo, o componente de cookies é obrigatório quando o produto trata dados pessoais por meio de cookies, e deve permitir ver a finalidade, a duração e os dados de cada cookie, consentir e revogar o consentimento, conforme a LGPD ([gov.br DS](https://www.gov.br/ds/components/cookiebar)).

O padrão tem três partes: o **aviso** no topo da página, a **confirmação** que o substitui depois da escolha e a **página de cookies**, com a lista detalhada e as preferências. Se o produto só usa cookies essenciais, dispense o aviso, mas publique a página de cookies e linke-a no rodapé ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/), [DKFDS](https://designsystem.dk/komponenter/cookiemeddelelse/)). Este padrão é uma decisão de design e não substitui orientação jurídica; veja Legislação e normas.

### Anatomia

| Parte                         | Conteúdo                                                                                                                             | Obrigatório |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------|
| Título do aviso               | "Cookies no" e o nome do serviço                                                                                                     | Sim         |
| Texto do aviso                | Quais cookies o serviço usa, para quê e o que acontece se a pessoa recusar                                                           | Sim         |
| Ações                         | "Aceitar cookies" e "Recusar cookies", no mesmo estilo                                                                               | Sim         |
| Link para a página de cookies | "Definir cookies" quando há mais de uma categoria; "Ver cookies" quando há uma só                                                    | Sim         |
| Confirmação                   | A escolha feita, onde mudar e o botão "Ocultar"                                                                                      | Sim         |
| Página de cookies             | Data da última atualização, texto introdutório, categorias com preferências, lista de cookies, perguntas frequentes, links e contato | Sim         |

A página de cookies reúne as áreas que o gov.br prevê para o cookiebar aberto: título, informação sobre atualização, texto introdutório, classes de cookies, cards com os detalhes de cada cookie, aviso em formato de perguntas e respostas e links para conteúdo complementar ([gov.br DS](https://www.gov.br/ds/components/cookiebar)).

### Boas práticas

#### Antes de desenhar

**Liste e classifique tudo o que o produto grava.** Separe em essenciais, sem os quais o serviço não funciona; funcionais, que lembram preferências; de análise; e outros. Registre se cada um é gravado no servidor ou no navegador ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)). O gov.br chama esses grupos de classes e mostra quantos cookies cada classe contém ([gov.br DS](https://www.gov.br/ds/components/cookiebar)).

**Não grave nada não essencial antes do consentimento.** Cookies de estatística só podem ser gravados depois de aceitação ativa ([DKFDS](https://designsystem.dk/komponenter/cookiemeddelelse/)). Essenciais não pedem consentimento, mas precisam ser informados ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)).

#### Aviso

**Dê o mesmo peso a aceitar e recusar.** Use dois botões do mesmo estilo, lado a lado, com rótulos paralelos. Nenhum dos dois é primário. Recusar nunca fica escondido na página de detalhes.

> **Divergência entre referências** No cookiebar do gov.br, o aviso inicial tem só "Aceitar" e "Definir Cookies" ou "Ver Política de Cookies", e só pode ser fechado com a aceitação dos termos ([gov.br DS](https://www.gov.br/ds/components/cookiebar)). A orientação de acessibilidade do mesmo componente pede uma opção fácil e clara para não aceitar cookies ([gov.br DS](https://www.gov.br/ds/components/cookiebar)). O GOV.UK coloca aceitar e recusar no próprio aviso ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)), e o site do DKFDS oferece "Accepter cookies" e "Nej tak til cookies" lado a lado ([DKFDS](https://designsystem.dk/privatlivspolitik-cookies/)). A Apple considera manipulação usar rótulos e peso visual que levem a pessoa a permitir sem querer ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)). Pela convergência e pela orientação de acessibilidade do próprio gov.br, o Trama mantém a regra da versão 1.0: aceitar e recusar no aviso, com o mesmo peso.

**Mostre o aviso no fluxo da página, sem modal, sem véu e sem posição fixa.** Um modal impede a pessoa de ver a página antes de decidir e a distrai da tarefa; o DKFDS cita pesquisas de Friedman (2019) e Fessenden (2017) para essa regra ([DKFDS](https://designsystem.dk/komponenter/cookiemeddelelse/)). Um aviso fixo pode cobrir o elemento com foco e violar a WCAG 2.2, 2.4.11 ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)). O aviso fica na camada `--z-0`, sem sombra.

> **Divergência entre referências** O gov.br permite bloquear a página com um scrim até a pessoa concordar, e coloca o cookiebar na camada 4 ([gov.br DS](https://www.gov.br/ds/components/cookiebar), [gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)). O DKFDS sugere deixar o aviso acompanhar a rolagem quando a escolha for importante ([DKFDS](https://designsystem.dk/komponenter/cookiemeddelelse/)). O critério de evidência favorece o aviso sem modal, apoiado em pesquisa pelo DKFDS, e o de acessibilidade favorece o aviso sem posição fixa, pelo critério 2.4.11. O Trama não bloqueia a página e não fixa o aviso.

**Posicione o aviso como primeiro elemento da página.** Coloque-o logo após a abertura do `body`, antes dos links de pular e do cabeçalho ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/), [DKFDS](https://designsystem.dk/komponenter/cookiemeddelelse/)). Use um elemento com nome acessível, como `<section aria-labelledby>` ou um `form` com `aria-label`.

**Funcione sem JavaScript quando o servidor grava cookies.** Ponha o aviso dentro de um formulário que envia a escolha; com JavaScript, envie sem recarregar para a pessoa não perder o lugar num formulário ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)).

**Mostre o aviso até a pessoa decidir.** O aviso aparece em toda visita até a pessoa aceitar ou recusar, no aviso ou na página de cookies; depois, não aparece mais enquanto a preferência estiver salva ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)). Se a política mudar, mostre o aviso de novo com o motivo ([gov.br DS](https://www.gov.br/ds/components/cookiebar)).

#### Confirmação

**Substitua o aviso por uma confirmação e mova o foco para ela.** A confirmação diz o que foi escolhido, onde mudar e tem o botão "Ocultar". Guarde a preferência por um ano. Dê à confirmação `tabindex="-1"` e `role="alert"` e mova o foco para ela ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)). Como o foco foi movido pelo sistema, use o foco tênue `.tr-focus-subtle`.

#### Página de cookies

**Publique uma página de cookies própria do serviço.** Linke-a no rodapé e no aviso, e não esconda a política em termos e condições ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)). O gov.br pede um item de menu no cabeçalho ou em outro local de destaque para redefinir os cookies ([gov.br DS](https://www.gov.br/ds/components/cookiebar)); no Trama, o link "Cookies" fica no rodapé de todas as páginas e, em produtos com área de conta, também em Configurações.

**Descreva cada cookie.** Para cada um, informe nome, finalidade, quem o grava, domínio e validade ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/), [gov.br DS](https://www.gov.br/ds/components/cookiebar)). Mostre a data da última atualização no topo ([gov.br DS](https://www.gov.br/ds/components/cookiebar)).

**Carregue as preferências não essenciais desmarcadas na primeira visita.** Na volta, mostre a escolha já feita ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)). O gov.br pede que opções de consentimento apareçam sem marcação prévia nos formulários ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)).

**Use radio por categoria e um botão para salvar.** O GOV.UK usa radios e um botão ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)). O gov.br usa checkbox por classe, com estado intermediário, e switch por cookie ([gov.br DS](https://www.gov.br/ds/components/cookiebar)). O Trama usa radio quando há poucas categorias. Se o produto precisar de escolha por cookie, use checkbox por categoria com estado misto e checkbox por cookie, todos confirmados pelo botão "Salvar preferências"; switch fica para mudanças com efeito imediato. Veja Switch.

**Marque essenciais como "Sempre ativos", sem controle.** O gov.br identifica classes que não podem ser desligadas com o texto "Sempre ativos", sem checkbox ([gov.br DS](https://www.gov.br/ds/components/cookiebar)). O gov.br mostra esse texto em verde; o Trama usa um badge com símbolo e texto, para não depender de cor.

**Avise antes de a pessoa desligar algo que afeta o serviço.** Se uma escolha comprometer uma função, mostre uma mensagem logo abaixo do controle correspondente, para que a pessoa decida se mantém a escolha ([gov.br DS](https://www.gov.br/ds/components/cookiebar)).

**Confirme a gravação no topo da página.** Ao salvar, mostre uma mensagem de sucesso que leve de volta à página onde a pessoa estava ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)). Se a pessoa sair da página sem salvar, as escolhas feitas ali não valem; diga isso numa mensagem e explique como voltar ([gov.br DS](https://www.gov.br/ds/components/cookiebar)).

**Peça consentimento de novo quando o uso mudar.** Peça de novo ao começar a usar um tipo de cookie não essencial novo, cookies que coletam informação sensível ou ao usar os dados de forma diferente da consentida; até lá, não grave os cookies novos ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)).

### Conteúdo

**Ponha o nome do serviço no título.** Assim a pessoa entende de quais cookies se trata ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)).

**Escreva para leigos.** Mesmo num tema técnico, use vocabulário simples; a pessoa não é obrigada a entender termos restritos a áreas técnicas ([gov.br DS](https://www.gov.br/ds/components/cookiebar)). Mantenha o texto curto e fiel ao uso real dos cookies ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)). Não use "opt in" nem "opt out" na interface: são estrangeirismos com equivalente comum.

**Diga o que acontece se a pessoa recusar.** Se recusar não muda nada, diga. Se alguma função deixar de funcionar ou algum dado continuar sendo gravado, diga isso de forma explícita no aviso ([gov.br DS](https://www.gov.br/ds/components/cookiebar)).

**Use perguntas e respostas para as explicações gerais.** O gov.br recomenda esse formato no aviso sobre cookies, com links para detalhes legais e um canal de contato para dúvidas ([gov.br DS](https://www.gov.br/ds/components/cookiebar)).

| Elemento                   | Texto do Trama                                            |
|----------------------------|-----------------------------------------------------------|
| Título do aviso            | Cookies no \[nome do serviço\]                            |
| Botões do aviso            | Aceitar cookies · Recusar cookies                         |
| Link do aviso              | Definir cookies                                           |
| Confirmação                | Cookies de análise aceitos · Cookies de análise recusados |
| Botão da confirmação       | Ocultar                                                   |
| Botão da página de cookies | Salvar preferências                                       |
| Essenciais                 | Sempre ativos                                             |

### Acessibilidade

**Garanta o uso por teclado e leitor de tela.** Os botões do aviso são alcançados com Tab e acionados com Enter ou Espaço; o propósito do aviso fica claro para quem usa leitor de tela ([gov.br DS](https://www.gov.br/ds/components/cookiebar)). Use `button` e `a` nativos.

**Mantenha a página navegável.** O aviso não pode interferir no conteúdo principal nem prejudicar a navegação ([gov.br DS](https://www.gov.br/ds/components/cookiebar)). Sem modal e sem posição fixa, o foco nunca fica coberto.

**Use alvos de 44px em toque.** O gov.br pede área mínima de 44px nos elementos interativos do cookiebar em dispositivos móveis ([gov.br DS](https://www.gov.br/ds/components/cookiebar)), o mesmo `--c-touch` do Trama.

**Não dependa de cor.** "Sempre ativos" e a confirmação levam texto e símbolo além da cor.

### Considerações por plataforma

#### Web desktop

O aviso ocupa a largura do conteúdo, com o texto limitado à coluna de leitura e os botões em linha, no início do conteúdo.

#### Web móvel

O aviso ocupa boa parte da primeira tela; mantenha o texto curto. Use `.tr-btn--block-compact` para empilhar os botões em largura total na classe Compacta, na ordem do texto: "Aceitar cookies" e depois "Recusar cookies", ambos com o mesmo estilo. Todo o conteúdo do padrão deve se adaptar a qualquer resolução, inclusive à grade de 4 colunas ([gov.br DS](https://www.gov.br/ds/components/cookiebar)).

#### Tablets e dobráveis

Ao abrir ou fechar o aparelho, preserve a escolha em andamento e a posição do foco. Na página de cookies, use uma coluna mesmo em telas largas, para que categoria e controle fiquem juntos.

### Recursos

#### Relacionados

- Privacidade
- Legislação e normas
- Mensagens e banners
- Rodapé
- Radio
- Configurações

#### Referências

- [Cookiebar](https://www.gov.br/ds/components/cookiebar) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Elevação](https://www.gov.br/ds/fundamentos-visuais/elevacao) gov.br DS
- [Cookie banner](https://design-system.service.gov.uk/components/cookie-banner/) GOV.UK Design System
- [Cookies page](https://design-system.service.gov.uk/patterns/cookies-page/) GOV.UK Design System
- [Cookiemeddelelse](https://designsystem.dk/komponenter/cookiemeddelelse/) Det Fælles Designsystem
- [Privatlivspolitik og cookies](https://designsystem.dk/privatlivspolitik-cookies/) Det Fælles Designsystem
- [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) Apple HIG

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## Coletar feedback

Dê às pessoas um caminho simples e sempre voluntário para dizer o que acham do produto, diga o que será coletado e use o que elas disserem.

O feedback das pessoas é a forma mais direta de saber como o produto funciona na prática. Ele serve para avaliar o lançamento de um produto, uma mudança de layout, um novo fluxo ou um novo recurso ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Esta página trata de colher a opinião das pessoas. As respostas que o produto dá às ações delas estão em Feedback, e a avaliação de resultados gerados por IA, em IA generativa.

### Boas práticas

#### Tipos de feedback

**Saiba que tipo de opinião você quer receber.** O gov.br classifica o feedback em cinco tipos ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Use-os como opções do motivo no formulário:

| Tipo                       | O que costuma indicar                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------|
| Sugestão de melhoria       | Vem muito de quem usa o produto com frequência; aponta evoluções.                             |
| Crítica                    | Negativa ou construtiva, dá insumos para análise e próximas versões.                          |
| Elogio                     | Menos comum; indica satisfação com a interface ou um recurso.                                 |
| Dúvida de uso              | A pessoa tentou resolver sozinha e não conseguiu; sinal de problema na interface ou na ajuda. |
| Relato de problema ou erro | Alimenta as correções futuras.                                                                |

**Combine feedback explícito e implícito.** O explícito é o que a pessoa diz em resposta a um pedido; o implícito vem do uso, como a escolha entre duas versões. Peça feedback explícito só quando necessário, porque ele exige trabalho da pessoa, e não dependa só do implícito, que mostra apenas o que a pessoa já consegue ver e fazer ([HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning)).

#### Formas de coleta

**Deixe alternar entre a versão nova e a antiga.** Ao lançar um recurso ou um novo layout, ofereça um switch ou um checkbox no menu de opções para usar a versão nova. O sistema conta quantas pessoas escolhem cada versão e mostra a preferência do público ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Diga que é possível voltar e mantenha a escolha entre sessões.

**Ofereça um formulário aberto com motivo e e-mail opcional.** Uma caixa de texto recebe dúvidas, sugestões e críticas, numa página própria ou num painel flutuante. Peça o motivo do contato numa seleção e, de forma opcional, o e-mail para uma resposta personalizada ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Diga para que o e-mail será usado ([gov.br](https://www.gov.br/ds/padroes/design/formulario)).

**Use questionários para opinião detalhada.** Um questionário com perguntas específicas dá respostas mais ricas, mas exige mais tempo e costuma ter menos adesão ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Diga antes quanto tempo leva ([GOV.UK](https://design-system.service.gov.uk/components/feedback/)) e organize-o como em Formulários em etapas.

**Use a escala de satisfação para uma medida rápida.** A escala vai de "Muito insatisfeito" a "Muito satisfeito" e fica junto do recurso avaliado ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). No Trama, ela é um grupo de botões de opção com texto visível em `.tr-scale`, dentro de um `fieldset` cuja legenda é a pergunta. Depois da nota, ofereça um campo opcional para explicar.

**Avalie resultados de IA no próprio resultado.** Ofereça um jeito rápido de avaliar positivo e negativo e um caminho para detalhar problemas complexos ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). As categorias, os rótulos e os dados enviados estão em IA generativa.

#### Quando e onde pedir

**Deixe o acesso ao formulário em todas as telas.** Ponha o caminho para enviar opinião no cabeçalho, ao lado da ajuda, ou no rodapé ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)), e repita-o ao fim de cada página, antes do rodapé, para que a pessoa opine a qualquer momento sem se distrair ([GOV.UK](https://design-system.service.gov.uk/components/feedback/)). Páginas de erro também oferecem esse caminho ([gov.br](https://www.gov.br/ds/templates/erro)).

**Use o ícone de balão simples.** O balão de comentário único representa o envio de opinião, uma comunicação de mão única. Não use o balão duplo, que sugere conversa ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). Acompanhe o ícone do texto "Enviar opinião".

**Peça depois que a pessoa usou o produto, numa pausa natural.** Não peça avaliação no primeiro acesso nem durante o onboarding, e não interrompa uma tarefa; prefira o fim de uma etapa ou tarefa ([HIG](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews)). O Trama não abre pedidos de opinião em diálogo modal.

**Não insista.** Pedidos repetidos irritam e podem piorar a opinião sobre o produto; espere novo uso antes de pedir de novo ([HIG](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews)). Quem respondeu ou dispensou não vê o mesmo pedido de novo na mesma versão.

**Torne o feedback sempre voluntário.** Diga que a opinião ajuda sem dar a impressão de que é obrigatória ([HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning)). Nenhum fluxo depende de a pessoa avaliar.

#### Conteúdo

**Diga por que pede, o que fará e quanto tempo leva.** Explique a diferença entre dar uma opinião e pedir atendimento ([GOV.UK](https://design-system.service.gov.uk/components/feedback/)), e leve quem precisa de atendimento à ajuda e aos canais de contato.

**Descreva cada opção pelas consequências.** Evite termos vagos como "não gostei"; prefira opções que digam o que acontece, como "Mostrar menos sugestões deste tipo" ([HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning)).

**Confirme dizendo o que aconteceu.** Depois do envio, mostre "Opinião enviada" e, se houver e-mail, quando a pessoa pode esperar resposta. Sem exclamação e sem a expressão de êxito (D2).

#### Privacidade e LGPD

**Diga o que é coletado antes do envio.** Liste o que vai junto com a opinião, como página, data, versão do produto, navegador ou, na IA, o pedido e a resposta, e ligue a política de tratamento de dados. Todo dado coletado precisa de finalidade clara e informada, e o e-mail opcional diz o benefício de preenchê-lo ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Veja Privacidade e Legislação e normas.

**Proteja o feedback implícito.** A escolha entre versões e outros sinais de uso podem revelar informação sensível. Mantenha controles rígidos de privacidade, diga como o produto obtém essas informações e dê meios de restringi-las ([HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning)).

**Desestimule dados pessoais no texto livre.** Avise na dica do campo que a opinião não deve conter CPF, senha ou dados de terceiros, e remova esses dados antes de compartilhar as respostas com a equipe.

#### Use o que receber

**Leve o feedback a sério e mostre o efeito.** Resolva rápido os problemas relatados ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Quando a opinião mudar algo na experiência da pessoa, como ocultar um tipo de sugestão, aja na hora e mantenha a mudança ([HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning)). Dúvidas de uso recorrentes indicam onde melhorar a interface ou a ajuda ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)).

**Faça** pergunta curta no fim do conteúdo, com opções em texto.

**Não faça** diálogo modal ao abrir o produto, estrelas sem texto e nenhuma forma de dispensar.

#### Acessibilidade

A escala é um `fieldset` com `legend` e botões de opção nativos: o leitor de tela anuncia a pergunta, cada opção tem texto visível e as setas do teclado percorrem as opções. Não represente a escala só com ícones ou cores (WCAG 2.2, 1.4.1). Cada opção de `.tr-scale` mantém alvo de pelo menos 24 por 24 pixels CSS (WCAG 2.2, 2.5.8) e, no toque, `--c-touch`. A confirmação de envio usa `role="status"`. Ao abrir o drawer do formulário, o foco vai para o primeiro campo; ao fechar, volta ao botão "Enviar opinião".

> **Divergência entre referências** Escala: os exemplos do gov.br usam slider, percentual e estrelas. O Trama usa botões de opção com texto, pelo critério de acessibilidade: cada nível tem nome visível, a escolha é feita por teclado sem precisão de arraste e não depende de ícones. Momento: o gov.br sugere posicionar a escala junto ao recurso avaliado; a HIG pede não interromper e esperar o uso. O Trama mostra a escala junto ao recurso, no fim da tarefa, sem diálogo. Lugar: o gov.br sugere cabeçalho, rodapé ou menu; o GOV.UK testa, em fase de avaliação, o acesso antes do rodapé de cada página. O Trama adota os dois, pela convergência com a regra de ajuda acessível em todas as telas.

### Considerações por plataforma

#### Web desktop

Abra o formulário aberto num drawer, para que a pessoa veja a tela sobre a qual está opinando. Ações do drawer ficam alinhadas ao fim, com "Enviar" por último.

#### Web móvel

O formulário abre em página própria ou em tela cheia, com rótulos acima dos campos. As opções da escala quebram em várias linhas sem perder o texto; nunca abrevie "Muito insatisfeito". O acesso para opinar pode ficar no menu do cabeçalho compacto, junto da ajuda ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)).

#### Tablets e dobráveis

Em telas grandes, o drawer de opinião ocupa a lateral sem cobrir a tarefa. Ao abrir ou fechar um dobrável, preserve o texto já digitado no formulário ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Feedback
- Oferecer ajuda
- IA generativa
- Privacidade
- Entrada de dados
- Radio
- Drawers e folhas laterais

#### Referências

- [Ajuda e comunicação](https://www.gov.br/ds/padroes/design/ajuda-comunicacao) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Template de erro](https://www.gov.br/ds/templates/erro) gov.br DS
- [Feedback](https://design-system.service.gov.uk/components/feedback/) GOV.UK Design System
- [Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai) Apple HIG
- [Machine learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning) Apple HIG
- [Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews) Apple HIG
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

