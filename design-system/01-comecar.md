# Começar

## Princípios de design

Sete princípios orientam cada decisão do Trama e ajudam a escolher entre prioridades que competem.

Os princípios do Trama descrevem o que o sistema valoriza. Eles servem como ferramenta de decisão: quando uma regra deste site não cobre o seu caso, ou quando duas regras parecem se contradizer, volte a eles. A HIG apresenta seus princípios da mesma forma, como ferramentas para pesar prioridades concorrentes e tomar decisões ao longo do projeto ([HIG](https://developer.apple.com/design/human-interface-guidelines/design-principles)). O Padrão Digital de Governo pede que seus princípios guiem decisões de design, sejam específicos e fáceis de lembrar no dia a dia ([gov.br DS](https://www.gov.br/ds/introducao/principios)). O Ontario Design System pede que, quando um elemento não existe no sistema, a equipe use os princípios para guiar o trabalho ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)).

Na versão 1.1, os princípios incorporam os cinco princípios do gov.br (Experiência única, Eficiência e clareza, Acessibilidade, Reutilização e Colaboração) e as boas práticas que o acompanham. Cada princípio abaixo tem um enunciado curto, uma explicação e o que ele significa na prática. Os componentes, padrões e fundamentos do Trama já seguem esses princípios. Produtos que estendem o sistema também devem segui-los.

### Os princípios do Trama

#### 1. A necessidade da pessoa vem antes da tecnologia

**Entenda o problema antes de escolher a solução.** O gov.br pede atenção à pessoa usuária no lugar do foco na tecnologia: entender a necessidade primeiro e só depois pensar em como atendê-la, com a tecnologia se adequando ao objetivo ([gov.br DS](https://www.gov.br/ds/introducao/principios)). O Ontario pede que limitações do sistema interno não ditem uma interface pouco intuitiva ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)). A HIG pede que cada etapa do projeto pergunte para que o produto serve ([HIG](https://developer.apple.com/design/human-interface-guidelines/design-principles)).

- Pense em mais de uma forma de resolver o problema antes de escolher uma, como recomenda o gov.br ([gov.br DS](https://www.gov.br/ds/introducao/principios)).
- Parta da boa-fé das pessoas. Não sacrifique a solução mais simples por causa de uma possível má-fé; use mecanismos de controle de forma racional, para reduzir o dano à experiência ([gov.br DS](https://www.gov.br/ds/introducao/principios)). Peça um comprovante só quando a regra do serviço exigir, e não peça de novo um dado que o sistema já tem.
- Converse e teste com quem vive o problema. Veja Inclusão.

#### 2. Clareza em cada elemento e em cada etapa

**Inclua só o que ajuda a pessoa a concluir a tarefa, na ordem em que ela precisa.** O Ontario pede que todo elemento tenha propósito funcional ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)), e a HIG pede que cada elemento conquiste seu lugar ([HIG](https://developer.apple.com/design/human-interface-guidelines/design-principles)). O gov.br pede processos simples, informações organizadas e prioridade para o que é essencial, sem que a eficiência prejudique a compreensão: um número maior de etapas pode ser mais adequado se o processo ficar mais claro ([gov.br DS](https://www.gov.br/ds/introducao/principios)).

- Antes de criar uma função nova, responda às perguntas que o DKFDS propõe: a função é necessária, gera valor, pode ser acessível e existe uma solução mais simples e já testada ([DKFDS](https://designsystem.dk/kom-i-gang/designressourcer/)).
- Divida tarefas longas em etapas com uma pergunta ou decisão cada. Veja Formulários em etapas e páginas de pergunta.
- Use divulgação progressiva: mostre primeiro o essencial e deixe detalhes em acordeões ou páginas seguintes.
- Escreva com as palavras exatas de que o rótulo precisa. Veja Escrita e conteúdo.

#### 3. Acessível desde o primeiro rascunho

**Projete para a maior diversidade possível de pessoas, capacidades e contextos.** O Trama adota como meta mínima as Diretrizes de Acessibilidade para Conteúdo Web (WCAG) 2.2, nível AA. O gov.br pede que o sistema atenda às diferentes necessidades de acessibilidade, siga o Modelo de Acessibilidade em Governo Eletrônico (eMAG) e considere os diferentes usos e acessos ([gov.br DS](https://www.gov.br/ds/introducao/principios)). O GOV.UK observa que usar um design system não torna um serviço acessível por si só ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)), e a HIG pede tratar acessibilidade como prioridade desde o início ([HIG](https://developer.apple.com/design/human-interface-guidelines/design-principles)).

- Produtos para o público brasileiro observam a Lei nº 13.146/2015, art. 63, e a Lei nº 13.709/2018. Produtos para órgãos públicos também observam a Lei nº 14.129/2021 e o eMAG. Veja Legislação e normas.
- Use os tokens de cor do Trama, que já respeitam WCAG 2.2, 1.4.3 e 1.4.11. Veja Cor.
- Garanta que tudo funcione por teclado, com foco visível. Veja Teclado e Foco e seleção.
- Teste com pessoas com deficiência e com tecnologias assistivas reais, além de ferramentas automáticas. O gov.br lembra que avaliadores automáticos não bastam para garantir acessibilidade em nenhum nível ([gov.br DS](https://www.gov.br/ds/acessibilidade)).

#### 4. Resiliente e compreensível por máquinas

**Construa em camadas, a partir de HTML semântico.** O Trama adota o aprimoramento progressivo descrito pelo GOV.UK: comece com HTML semântico e ofereça melhorias acessíveis por cima ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)). O gov.br pede que os serviços sejam compreensíveis tanto para pessoas quanto para máquinas e compatíveis com assistentes virtuais ([gov.br DS](https://www.gov.br/ds/introducao/principios)). O Ontario lembra que muitas pessoas têm internet lenta ou instável e aparelhos antigos ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)).

- Use o elemento nativo certo: `<button>` para ações, `<a>` para navegação, `<label>` ligado a cada campo, títulos em ordem. A mesma estrutura serve ao leitor de tela, ao mecanismo de pesquisa e ao assistente virtual. Veja HTML acessível e WAI-ARIA.
- Mantenha a ordem visual igual à ordem do código. O Ontario alerta que reordenar só visualmente gera ordem de tabulação e de leitura incorretas ([Ontario](https://designsystem.ontario.ca/components/detail/grid.html)).
- Ofereça estados de carregamento e de erro para toda chamada de rede.
- Respeite preferências do sistema: modo escuro, `prefers-reduced-motion`, cores forçadas e zoom de texto.

#### 5. Uma experiência única

**Reutilize os componentes do sistema e aplique-os da mesma forma em todo lugar.** O gov.br descreve os serviços digitais do governo como um balcão único que compartilha os mesmos padrões estruturais e visuais, para dar confiança e reduzir a curva de aprendizado, com uma interface consistente, flexível e adaptável ao contexto de quem a usa ([gov.br DS](https://www.gov.br/ds/introducao/principios)). O princípio de Reutilização do gov.br pede usar componentes existentes sempre que possível e, ao criar um novo, respeitar os padrões visuais e funcionais ([gov.br DS](https://www.gov.br/ds/introducao/principios)). O DKFDS pede que componentes se comportem sempre como descrito ([DKFDS](https://designsystem.dk/kom-i-gang/tjekliste/)).

- Use os componentes do Trama para a finalidade descrita em cada página e cumpra o Padrão mínimo.
- Mantenha posição, nome e ícone de uma ação iguais em todas as telas do produto.
- Ao criar um componente, use os tokens alias e os estados do Trama. Veja Construir componentes.
- Quando precisar quebrar uma regra, registre o motivo e a evidência. O gov.br aceita alterações que respeitem princípios e fundamentos e tenham uma boa razão, como melhorar a experiência ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-criacao)).

#### 6. Adaptável a cada tela e entrada

**Projete para o espaço disponível e para qualquer forma de interação.** A HIG recomenda considerar vários métodos de entrada, incluindo voz, toque e teclado, e preservar o contexto da pessoa quando o design se adapta ([HIG](https://developer.apple.com/design/human-interface-guidelines/design-principles)). O gov.br lista mouse, toque, teclado, voz, controle de videogame e leitores de tela entre as entradas a considerar em cada componente ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)), e lembra que focar num modo de interação não significa esquecer o outro ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

- Decida o layout pelas classes de janela do Trama, sem detectar o tipo de aparelho. Veja Layout e grid.
- Comece pela tela pequena e amplie a partir dela ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)).
- Garanta alvo de `--c-touch` no toque e ofereça alternativas a gestos. Veja Toque e gestos.
- Preserve rolagem, seleção e texto digitado quando a janela muda de tamanho. Veja Postura e dobra.

#### 7. As pessoas no controle

**Deixe a pessoa agir do seu jeito, informe o que acontece e facilite desfazer.** A HIG pede liberdade para explorar sem ficar presa a fluxos, feedback claro e recuperação fácil de erros, além de transparência sobre o que o produto faz com os dados ([HIG](https://developer.apple.com/design/human-interface-guidelines/design-principles)). O HDS orienta não pedir dados "por precaução" e explicar por que cada dado é pedido ([HDS](https://hds.hel.fi/foundation/guidelines/inclusivity)).

- Prefira desfazer a pedir confirmação para ações reversíveis.
- Dê feedback visível para cada ação. Veja Feedback.
- Peça só os dados necessários e diga como serão usados. Veja Privacidade.
- Identifique conteúdo gerado por inteligência artificial e permita revisar antes de aplicar. Veja IA generativa.

### Boas práticas

**Use os princípios como critério de decisão.** Em revisões de design, cite o princípio que justifica cada escolha. Se nenhum se aplica, questione a escolha.

**Resolva conflitos pela ordem de impacto nas pessoas.** Quando consistência e facilidade de uso entram em conflito, a facilidade de uso vence ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)). Acessibilidade fica fora da negociação: uma solução que exclui alguém não é aceita no Trama. Quando as referências do Trama divergem entre si, o sistema decide nesta ordem: evidência de pesquisa, acessibilidade com mais margem, contexto brasileiro e convergência entre as referências. Cada decisão aparece na página em que foi tomada.

**Comece simples e teste cedo.** Designs simples são mais fáceis de mudar. Crie e teste a versão mais simples primeiro, e continue testando depois do lançamento ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)). O DKFDS lembra que, mesmo com componentes validados, cada solução precisa envolver as pessoas usuárias no desenvolvimento ([DKFDS](https://designsystem.dk/kom-i-gang/brugerinddragelse/)).

**Evolua o sistema junto com quem o usa.** O princípio de Colaboração do gov.br pede que os padrões melhorem de forma incremental, colaborativa e contínua, com base nas necessidades dos cidadãos e na experiência de aplicação ([gov.br DS](https://www.gov.br/ds/introducao/principios)). Quando um produto resolver um problema que o Trama não cobre, proponha a solução ao sistema com a pesquisa que a sustenta. Veja Como começar.

**Trate a qualidade como trabalho contínuo.** Lançar não encerra o design. Mantenha a interface atualizada e o nível de qualidade alto ([HIG](https://developer.apple.com/design/human-interface-guidelines/design-principles)).

| Princípio do Trama                              | Origem principal                                 | Pergunta para a revisão                                                                    |
|-------------------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------------------------|
| A necessidade da pessoa vem antes da tecnologia | Boas práticas do gov.br, Ontario                 | Que problema da pessoa esta tela resolve? O controle pedido parte da boa-fé?               |
| Clareza em cada elemento e em cada etapa        | Eficiência e clareza (gov.br), Ontario, HIG      | O que acontece se removermos este elemento? Uma etapa a mais deixaria a tarefa mais clara? |
| Acessível desde o primeiro rascunho             | Acessibilidade (gov.br), GOV.UK, HIG             | Alguém com leitor de tela, só teclado ou zoom de 400% conclui a tarefa?                    |
| Resiliente e compreensível por máquinas         | Compreensão e compatibilidade (gov.br), GOV.UK   | A página funciona com rede lenta e sem estilos? Um assistente virtual entende a estrutura? |
| Uma experiência única                           | Experiência única e Reutilização (gov.br), DKFDS | Este padrão já existe no Trama? Ele se comporta como descrito?                             |
| Adaptável a cada tela e entrada                 | HIG, gov.br                                      | A tarefa funciona em todas as classes de janela, com toque, mouse, teclado e voz?          |
| As pessoas no controle                          | HIG, HDS                                         | A pessoa entende o que vai acontecer e consegue voltar atrás?                              |

> **Divergência entre referências** O gov.br aceita mais etapas quando elas deixam o processo mais claro ([gov.br DS](https://www.gov.br/ds/introducao/principios)). A HIG pede levar a pessoa direto à tarefa e sair do caminho ([HIG](https://developer.apple.com/design/human-interface-guidelines/design-principles)). O GOV.UK recomenda dividir formulários em várias páginas com uma coisa por página, para ajudar a pessoa a se concentrar e entender o que se pede ([GOV.UK](https://design-system.service.gov.uk/get-started/labels-legends-headings/)). Nenhuma das fontes traz dado de pesquisa sobre o tema, e a maioria favorece a clareza. O Trama decide: clareza vence a contagem de etapas. Acrescente uma etapa quando ela separa decisões diferentes; remova a etapa que não acrescenta compreensão.

### Considerações por plataforma

#### Web desktop

Os princípios valem sem mudança. Em desktop, "adaptável" inclui janelas redimensionadas a qualquer largura e uso intenso de teclado. Veja Projetar para web desktop.

#### Web móvel

Em telas pequenas, a clareza pesa mais: o espaço é limitado e a rede pode ser instável. Veja Projetar para web móvel.

#### Tablets e dobráveis

"Adaptável" inclui continuidade quando o aparelho abre, fecha ou dobra parcialmente. Veja Projetar para tablets e dobráveis.

### Recursos

#### Relacionados

- Como começar: design e desenvolvimento
- Padrão mínimo
- Acessibilidade
- Legislação e normas
- Inclusão
- Escrita e conteúdo

#### Referências

- [Princípios do Design System](https://www.gov.br/ds/introducao/principios) gov.br DS
- [Fluxo de trabalho de criação](https://www.gov.br/ds/como-comecar/fluxo-criacao) gov.br DS
- [Acessibilidade](https://www.gov.br/ds/acessibilidade) gov.br DS
- [Estados](https://www.gov.br/ds/fundamentos-visuais/estados) gov.br DS
- [Grid](https://www.gov.br/ds/fundamentos-visuais/grid) gov.br DS
- [Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles) Apple HIG
- [Accessibility strategy](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) GOV.UK Design System
- [Making labels and legends headings](https://design-system.service.gov.uk/get-started/labels-legends-headings/) GOV.UK Design System
- [Design og ressourcer](https://designsystem.dk/kom-i-gang/designressourcer/) DKFDS
- [Tjekliste](https://designsystem.dk/kom-i-gang/tjekliste/) DKFDS
- [Brugerinddragelse](https://designsystem.dk/kom-i-gang/brugerinddragelse/) DKFDS
- [Ontario Government design principles](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html) Ontario Design System
- [Grid](https://designsystem.ontario.ca/components/detail/grid.html) Ontario Design System
- [Inclusivity](https://hds.hel.fi/foundation/guidelines/inclusivity) Helsinki Design System

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Os princípios passam de seis para sete, com a necessidade da pessoa antes da tecnologia, a boa-fé, a clareza acima da contagem de etapas, a compatibilidade com assistentes virtuais e a reutilização de componentes. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                         |

## Como começar

O caminho para projetar e construir com o Trama: o que estudar antes, como prototipar e validar, como incluir o kit no código e como contribuir de volta.

O Trama tem três partes que trabalham juntas. As páginas deste site são a fonte única das regras. Os tokens de design guardam as decisões visuais com nome. O arquivo `kit.css` entrega tokens e componentes prontos para o navegador. O gov.br descreve um design system como uma coleção de padrões e componentes reutilizáveis que serve de fonte única de verdade para designers, desenvolvedores e todas as pessoas envolvidas no produto ([gov.br DS](https://www.gov.br/ds/como-comecar/introducao)). O DKFDS define o site de documentação como fonte de verdade, acima do arquivo de design ([DKFDS](https://designsystem.dk/kom-i-gang/designressourcer/)). O Trama segue a mesma regra: quando um protótipo, um arquivo de código e uma página divergem, a página vale.

Esta página segue a estrutura que o gov.br usa para começar: o que saber antes e um fluxo para quem cria e outro para quem desenvolve ([gov.br DS](https://www.gov.br/ds/como-comecar/introducao)). O GOV.UK, o Ontario e o HDS também separam o começo por papel ([GOV.UK](https://design-system.service.gov.uk/get-started/), [Ontario](https://designsystem.ontario.ca/docs/documentation/explore/getting-started.html), [HDS](https://hds.hel.fi/getting-started/designer)).

### Antes de começar

**Leia os princípios.** O gov.br pede compreender os princípios antes de qualquer projeto, porque eles são a base de todo o trabalho ([gov.br DS](https://www.gov.br/ds/como-comecar/introducao)). Veja Princípios de design.

**Conheça os fundamentos.** Cor, tipografia, espaçamento, estados, layout e movimento formam a linguagem visual comum. O gov.br indica os fundamentos visuais como o passo seguinte aos princípios ([gov.br DS](https://www.gov.br/ds/como-comecar/introducao)). Comece por Tokens de design, Estados de interação e Layout e grid.

**Confira o padrão mínimo.** O Padrão mínimo lista o que todo produto feito com o Trama precisa cumprir antes de ser publicado.

**Escolha a plataforma.** Leia Projetar para web desktop, Projetar para web móvel ou Projetar para tablets e dobráveis, conforme onde o produto vai ser usado.

### Fluxo de design

Este fluxo vale para quem projeta interfaces, pesquisa com pessoas ou escreve conteúdo. Ele adapta as quatro etapas do fluxo de criação do gov.br: estudo preliminar, prototipagem, usabilidade e acessibilidade, e notas de versão ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-criacao)).

**1. Estude os componentes e padrões antes de desenhar.** O gov.br pede entender em detalhe como funciona cada componente e cada padrão, porque isso é a base das decisões de design ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-criacao)). Cada página de componente do Trama diz quando usar, quando não usar e qual alternativa escolher.

**2. Conheça as pessoas e esboce.** Pesquise, converse e descubra o que as pessoas precisam, o que as frustra e o que buscam; depois, esboce no papel antes de passar ao digital ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-criacao)). Antes de criar uma função, responda às perguntas do DKFDS: ela é necessária, gera valor, pode ser acessível e existe uma solução mais simples e já testada ([DKFDS](https://designsystem.dk/kom-i-gang/designressourcer/)).

**3. Prototipe com o kit.** O gov.br e o Ontario oferecem kits de interface em ferramentas de design para acelerar protótipos ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-criacao), [Ontario](https://designsystem.ontario.ca/docs/documentation/design/prototyping-kit.html)), e o GOV.UK oferece um kit de protótipos em código ([GOV.UK](https://design-system.service.gov.uk/get-started/prototyping/)). O Trama distribui o kit como CSS: protótipos de alta fidelidade são páginas HTML que carregam `kit.css` e copiam o markup das demonstrações deste site. Assim, o protótipo testado com pessoas já tem os estados, o foco e o contraste reais.

**4. Escreva o conteúdo junto com o layout.** Use as regras de Escrita e conteúdo e o vocabulário controlado do Trama desde o primeiro esboço. O gov.br mantém um dicionário de vocabulário controlado alimentado pela comunidade ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-criacao)).

**5. Valide usabilidade e acessibilidade.** Os componentes nascem acessíveis, e o produto montado com eles também precisa ser testado. O gov.br recomenda que quem não é designer busque um especialista antes de decisões que afetam a qualidade ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-criacao)). O Ontario pede que cada produto faça seus próprios testes de usabilidade e de acessibilidade ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/about-the-ods.html)). Veja Acessibilidade.

**6. Mude uma regra só com motivo registrado.** O gov.br aceita alterações que respeitem princípios e fundamentos e tenham uma boa razão, como melhorar a experiência ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-criacao)). No Trama, registre a evidência e proponha a mudança ao sistema.

### Fluxo de desenvolvimento

O Trama é distribuído como um único arquivo, `kit.css`, com tokens globais, tokens alias e as classes `.tr-*` dos componentes. Não há JavaScript no kit: o comportamento de cada componente é construído pelo produto, sobre HTML semântico. Veja CSS e tokens no código e JavaScript.

**1. Hospede o kit junto com o produto.** O gov.br recomenda evitar o CDN do próprio design system e instalar o pacote ou baixar os arquivos para o projeto, por segurança, atualização e controle das dependências ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-dev)). O Ontario sugere guardar os arquivos numa pasta própria, separada do resto do projeto, para trocar de versão com facilidade ([Ontario](https://designsystem.ontario.ca/docs/documentation/develop/for-developers.html)). Fixe a versão do kit e atualize de forma planejada. Veja Versões e migração.

**2. Carregue as fontes antes do kit.** O gov.br pede carregar fontes e bibliotecas externas antes dos arquivos do design system, para que estejam disponíveis quando os componentes forem desenhados ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-dev)). O Trama usa Inter para texto e JetBrains Mono para código e dados. Veja Tipografia.

``` code
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/vendor/fontes/figtree.css">
  <link rel="stylesheet" href="/vendor/trama/kit.css">
  <link rel="stylesheet" href="/css/app.css">
</head>
<body>
  <a class="app-skip" href="#conteudo">Ir para o conteúdo</a>
  <main id="conteudo">
    <h1 tabindex="-1">Título da página</h1>
    <button class="tr-btn tr-btn--primary" type="submit">Continuar</button>
  </main>
</body>
</html>
```

**3. Use só tokens alias no produto.** Os tokens globais (`--g-*`) guardam valores brutos; os alias (`--t-*`, `--sp-*`, `--r-*` e afins) guardam significado e trocam sozinhos no modo escuro, em `.tr-inverse` e nas densidades. Escreva `--t-danger`, nunca o valor hexadecimal. O GOV.UK pede não atribuir novos significados às cores nem mudar o estilo de botões ou a espessura das bordas de campos ([GOV.UK](https://design-system.service.gov.uk/styles/)). Veja Tokens de design.

**4. Nunca edite o kit e nunca sobrescreva uma classe `.tr-*`.** O DKFDS pede nunca escrever direto nos arquivos CSS do sistema ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/justering/)). O GOV.UK explica que sobrescrever uma classe do sistema funciona no curto prazo e quebra na próxima atualização ([GOV.UK](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/)). Ponha o código do produto num arquivo próprio, carregado depois do kit.

**5. Use um prefixo próprio.** O GOV.UK usa o prefixo `govuk-` e pede que cada aplicação use outro, como `app-` ([GOV.UK](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/)). O prefixo `tr-` é reservado ao Trama. Para uma pequena mudança, crie um modificador com o seu prefixo; para uma grande, crie um componente novo com outro nome ([GOV.UK](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/)). Veja Construir componentes.

**6. Ligue tema e densidade com atributos.** O tema segue `prefers-color-scheme` e pode ser fixado com `data-theme="light"` ou `data-theme="dark"` no elemento raiz. A densidade muda com `data-density="alta"` ou `data-density="baixa"` num contêiner. Faixas escuras dentro do tema claro usam `.tr-inverse`. Veja Modo escuro e Densidade.

**7. Escreva o comportamento sobre HTML que funciona sozinho.** O gov.br pede inicializar os componentes depois que a página carrega e, em frameworks, criar as instâncias na montagem e limpá-las na desmontagem para evitar vazamento de memória ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-dev)). No Trama, comece pelo elemento nativo e acrescente JavaScript só para o que o HTML não faz. Veja HTML acessível e WAI-ARIA.

**8. Teste nos navegadores suportados.** Veja a lista em Navegadores e dispositivos suportados.

| Camada               | Exemplo                              | Quem usa                                 |
|----------------------|--------------------------------------|------------------------------------------|
| Token global         | `--g-brand-60`                       | Só o próprio kit, para definir os alias. |
| Token alias          | `--t-brand`, `--sp-400`, `--o-hover` | Produtos e componentes novos.            |
| Classe de componente | `.tr-btn--primary`                   | Markup do produto, sem sobrescrever.     |
| Classe do produto    | `.app-resumo`                        | Código do produto, com prefixo próprio.  |

**Faça** crie classes com prefixo próprio que usam tokens alias.

**Não faça** sobrescreva uma classe do Trama nem escreva valores brutos.

> **Divergência entre referências** O gov.br recomenda como caminho principal sua biblioteca de web components, que encapsula estilo e comportamento ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-dev)). O GOV.UK recomenda instalar o pacote de front-end e usar HTML ou macros de template, com classes de CSS ([GOV.UK](https://design-system.service.gov.uk/get-started/production/)). O Ontario oferece as duas opções ([Ontario](https://designsystem.ontario.ca/docs/documentation/develop/for-developers.html)). Nenhuma fonte cita pesquisa. O Trama decide pela convergência com GOV.UK e DKFDS e pelo princípio de resiliência: o kit é CSS sobre HTML semântico, que funciona antes de qualquer script carregar e em qualquer framework.

### Contribuir com o Trama

**Devolva ao sistema o que funcionou no produto.** O gov.br pede que a evolução seja incremental, colaborativa e contínua ([gov.br DS](https://www.gov.br/ds/introducao/principios)) e convida a comunidade a contribuir com soluções de design e de front-end que atenderam bem um projeto ([gov.br DS](https://www.gov.br/ds/introducao/comunidade)). O GOV.UK lembra que ideias discutidas abertamente podem não ter sido testadas e pede pesquisa antes de usá-las ([GOV.UK](https://design-system.service.gov.uk/get-started/)). Ao propor um componente ou uma mudança, envie o problema, a solução, a pesquisa feita e o resultado de acessibilidade.

**Acompanhe o histórico de mudanças.** O gov.br trata as notas de versão como a comunicação transparente entre o time do design system e quem o usa ([gov.br DS](https://www.gov.br/ds/como-comecar/fluxo-criacao)). No Trama, cada página termina com seu histórico, e as mudanças de cada versão ficam em Versões e migração.

### Considerações por plataforma

#### Web desktop

Prototipe e teste nas três classes de desktop e com zoom de 200% e 400%. Veja Projetar para web desktop.

#### Web móvel

Escreva o CSS do produto a partir da classe Compacta, com densidade baixa, e teste em aparelhos reais. Veja Projetar para web móvel.

#### Tablets e dobráveis

Inclua no protótipo as mudanças de orientação e de postura e verifique que o estado se mantém. Veja Projetar para tablets e dobráveis.

### Recursos

#### Relacionados

- Princípios de design
- Padrão mínimo
- Tokens de design
- CSS e tokens no código
- Construir componentes
- Versões e migração

#### Referências

- [Como começar](https://www.gov.br/ds/como-comecar/introducao) gov.br DS
- [Fluxo de trabalho de criação](https://www.gov.br/ds/como-comecar/fluxo-criacao) gov.br DS
- [Fluxo de trabalho de desenvolvimento](https://www.gov.br/ds/como-comecar/fluxo-dev) gov.br DS
- [Princípios do Design System](https://www.gov.br/ds/introducao/principios) gov.br DS
- [Comunidade](https://www.gov.br/ds/introducao/comunidade) gov.br DS
- [Get started](https://design-system.service.gov.uk/get-started/) GOV.UK Design System
- [Production](https://design-system.service.gov.uk/get-started/production/) GOV.UK Design System
- [Prototyping](https://design-system.service.gov.uk/get-started/prototyping/) GOV.UK Design System
- [Extending and modifying components in production](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/) GOV.UK Design System
- [Styles](https://design-system.service.gov.uk/styles/) GOV.UK Design System
- [Design og ressourcer](https://designsystem.dk/kom-i-gang/designressourcer/) DKFDS
- [Justering af tema og stylesheets](https://designsystem.dk/kom-i-gang/implementering-kode/justering/) DKFDS
- [Getting started](https://designsystem.ontario.ca/docs/documentation/explore/getting-started.html) Ontario Design System
- [About the Ontario Design System](https://designsystem.ontario.ca/docs/documentation/explore/about-the-ods.html) Ontario Design System
- [Prototyping kit](https://designsystem.ontario.ca/docs/documentation/design/prototyping-kit.html) Ontario Design System
- [Getting started for developers](https://designsystem.ontario.ca/docs/documentation/develop/for-developers.html) Ontario Design System
- [Getting started as a Designer](https://hds.hel.fi/getting-started/designer) Helsinki Design System

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## Padrão mínimo

A lista do que todo produto feito com o Trama precisa cumprir antes de ser publicado, com um jeito de verificar cada item.

O padrão mínimo é o piso de aderência ao Trama. Ele reúne os itens que dão identidade, consistência e acessibilidade a um produto, e cada item pode ser verificado por quem revisa a interface ou o código. O resto do sistema continua valendo como recomendação; o padrão mínimo é o que não se negocia.

O modelo vem de duas referências. O gov.br publica um padrão mínimo para adequar soluções ao Padrão Digital de Governo, organizado em identidade visual (cabeçalho, marca, rodapé, tipografia, cores e botões), boas práticas de formulário, fundamentos visuais mínimos e componentes essenciais ([gov.br DS](https://www.gov.br/ds/introducao/padrao-minimo)). O DKFDS publica uma lista de verificação que cobre estrutura de página, estilo visual, ícones, responsividade, layout, divisão de fluxos longos, comportamento dos componentes, extensões e acessibilidade ([DKFDS](https://designsystem.dk/kom-i-gang/tjekliste/)).

### Quem precisa cumprir

Todo produto que usa o Trama cumpre o padrão mínimo, inclusive extensões e componentes criados pelo produto. O Ontario aplica sua obrigação a sites, aplicações web e serviços entregues por plataformas de fornecedores, sem exceção para plataformas compradas prontas ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/getting-started.html)). O Trama faz o mesmo: componente de terceiros dentro do produto também precisa cumprir a lista. O DKFDS pede que extensões e plugins se ajustem visualmente ao sistema e atendam aos requisitos de acessibilidade ([DKFDS](https://designsystem.dk/kom-i-gang/tjekliste/)).

### Lista de verificação

#### Estrutura e identidade

| Requisito                                                                                                                                                                                                                                                                             | Como verificar                                                         | Página                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|-----------------------|
| Toda página tem cabeçalho, conteúdo principal e rodapé. O DKFDS exige essa divisão em todas as páginas ([DKFDS](https://designsystem.dk/kom-i-gang/tjekliste/)), e o gov.br inclui cabeçalho e rodapé no padrão mínimo ([gov.br DS](https://www.gov.br/ds/introducao/padrao-minimo)). | Cada página tem `<header>`, `<main>` e `<footer>`, um de cada.         | Cabeçalho, Rodapé     |
| O cabeçalho identifica o produto e o responsável por ele.                                                                                                                                                                                                                             | Marca e nome do produto aparecem em todas as classes de janela.        | Marca                 |
| Toda página começa com um link de pular para o conteúdo principal.                                                                                                                                                                                                                    | O primeiro Tab da página mostra o link, e ele leva o foco ao `<main>`. | Links de pular        |
| Toda página tem um único título `<h1>` e um `<title>` que o repete.                                                                                                                                                                                                                   | Inspeção do código.                                                    | Texto e títulos       |
| Fluxos longos são divididos em etapas menores ([DKFDS](https://designsystem.dk/kom-i-gang/tjekliste/)).                                                                                                                                                                               | Cada etapa pede uma decisão ou um grupo de dados relacionados.         | Formulários em etapas |

#### Fundamentos visuais

| Requisito                                                                                                                                                                                                                                                                                                                | Como verificar                                                                                        | Página                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-----------------------|
| Cores vêm dos tokens alias e são usadas pela função: superfície, leitura, interação e aviso. O gov.br pede usar as cores pelas suas funções ([gov.br DS](https://www.gov.br/ds/introducao/padrao-minimo)), e o GOV.UK pede não dar novos significados às cores ([GOV.UK](https://design-system.service.gov.uk/styles/)). | Nenhum valor hexadecimal ou `rgb()` no CSS do produto; `--g-*` não aparece fora do kit.               | Cor, Tokens de design |
| Texto usa Inter, com corpo base de 16 px e nunca abaixo de 12 px.                                                                                                                                                                                                                                                      | Inspeção do CSS calculado nas classes de texto.                                                       | Tipografia            |
| Espaços seguem a escala de 4 px dos tokens `--sp-*`.                                                                                                                                                                                                                                                                     | Nenhum valor de `margin`, `padding` ou `gap` fora da escala.                                          | Espaçamento           |
| Ícones têm o significado convencional e um nome acessível. O gov.br lista significados mínimos, como lupa para pesquisar, lixeira para excluir, "x" para fechar, impressora para imprimir e casa para ir à tela inicial ([gov.br DS](https://www.gov.br/ds/introducao/padrao-minimo)).                                   | Nenhum ícone usado com dois significados no produto; todo botão só de ícone tem `aria-label`.         | Iconografia           |
| O produto funciona nos temas claro e escuro.                                                                                                                                                                                                                                                                             | Teste com `data-theme="light"` e `data-theme="dark"`.                                                 | Modo escuro           |
| O layout funciona em todas as classes de janela, da Compacta à Extragrande. O DKFDS exige solução responsiva ([DKFDS](https://designsystem.dk/kom-i-gang/tjekliste/)).                                                                                                                                                   | Sem rolagem horizontal da página de 320 px de largura (WCAG 2.2, 1.4.10) até o maior monitor testado. | Layout e grid         |

#### Componentes e interação

| Requisito                                                                                                                                                                                                                                                           | Como verificar                                                                    | Página                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------|
| Os componentes do Trama são usados para a finalidade descrita e se comportam como descrito. O DKFDS exige que componentes funcionem como descrito, para que a pessoa não estranhe um componente conhecido ([DKFDS](https://designsystem.dk/kom-i-gang/tjekliste/)). | Nenhuma regra `.tr-*` no CSS do produto; classes próprias têm prefixo do produto. | Como começar              |
| Botões seguem a hierarquia e a ordem do Trama: em páginas, a ação principal primeiro; em diálogos, a principal por último, à direita. O gov.br inclui botões e ordem das ações no padrão mínimo ([gov.br DS](https://www.gov.br/ds/introducao/padrao-minimo)).      | Uma só ação principal por tela ou diálogo; ordem conferida em cada formulário.    | Botões                    |
| Estados de hover, foco, pressionado, ativo e selecionado usam os tokens do Trama e aparecem um por vez.                                                                                                                                                             | Navegação por mouse e por teclado em cada componente.                             | Estados de interação      |
| Toda a tarefa pode ser feita só com o teclado, com o anel de foco visível.                                                                                                                                                                                          | Percorrer cada fluxo do primeiro Tab até a confirmação.                           | Teclado, Foco e seleção   |
| Alvos de toque têm 44 por 44 px e a densidade é baixa em telas de toque.                                                                                                                                                                                            | Medição na classe Compacta e em tablet.                                           | Toque e gestos, Densidade |
| Entrar e sair da conta seguem o padrão de autenticação do Trama. O gov.br inclui o componente de autenticação entre os essenciais ([gov.br DS](https://www.gov.br/ds/introducao/padrao-minimo)).                                                                    | Rótulos "Entrar" e "Sair"; o mesmo lugar em todas as páginas.                     | Contas e autenticação     |

#### Formulários e conteúdo

| Requisito                                                                                                                                                                                                                    | Como verificar                                    | Página                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------|
| Formulários têm semântica completa: todo campo com `<label>`, grupos com `<fieldset>` e `<legend>`. O gov.br pede trabalhar a semântica e organizar os campos ([gov.br DS](https://www.gov.br/ds/introducao/padrao-minimo)). | Inspeção do código e leitura com leitor de tela.  | Entrada de dados              |
| O botão de envio nunca fica desabilitado; o formulário valida ao enviar e mostra o resumo de erros.                                                                                                                          | Enviar o formulário vazio.                        | Validação e mensagens de erro |
| Campos aceitam o dado em qualquer formato digitado, sem máscara que impeça digitar ou apagar.                                                                                                                                | Digitar CPF, telefone e data com e sem pontuação. | Entrada de dados              |
| O conteúdo segue o vocabulário controlado e a caixa de frase do Trama.                                                                                                                                                       | Revisão de rótulos, títulos e mensagens.          | Escrita e conteúdo            |
| Mensagens de erro dizem o que aconteceu e como resolver, sem culpar a pessoa.                                                                                                                                                | Revisão de cada mensagem de erro.                 | Validação e mensagens de erro |

#### Acessibilidade e legislação

| Requisito                                                                                                                                                                                                                                                                        | Como verificar                                                                                                                                                                  | Página                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| O produto atende à WCAG 2.2, nível AA.                                                                                                                                                                                                                                           | Ferramenta automática e teste com pessoas e tecnologias assistivas. O gov.br lembra que avaliadores automáticos não bastam ([gov.br DS](https://www.gov.br/ds/acessibilidade)). | Acessibilidade                   |
| Produtos para o público brasileiro observam a Lei nº 13.146/2015, art. 63, e a Lei nº 13.709/2018, Lei Geral de Proteção de Dados Pessoais (LGPD). Produtos para órgãos públicos também observam a Lei nº 14.129/2021 e o Modelo de Acessibilidade em Governo Eletrônico (eMAG). | Declaração de acessibilidade e aviso de privacidade publicados.                                                                                                                 | Legislação e normas, Privacidade |
| Animações respeitam `prefers-reduced-motion` e o produto oferece um controle para desligá-las.                                                                                                                                                                                   | Ativar a preferência do sistema e o controle do produto.                                                                                                                        | Movimento                        |

**Faça** use os botões do kit, com a ação principal primeiro na página e o envio sempre habilitado.

**Não faça** desabilite o envio até o formulário ficar válido, nem dê à ação principal a mesma aparência da secundária.

> **Divergência entre referências** O gov.br inclui no padrão mínimo a identidade visual do governo: a marca, a tipografia Rawline e a paleta própria ([gov.br DS](https://www.gov.br/ds/introducao/padrao-minimo)), e o DKFDS exige o layout com conteúdo alinhado à esquerda numa coluna ([DKFDS](https://designsystem.dk/kom-i-gang/tjekliste/)). O Trama é um sistema de marca neutra: o padrão mínimo exige os tokens, a tipografia e a estrutura do Trama, e a identidade de cada órgão entra pelos tokens alias do produto. O gov.br afirma que aplicações de governo precisam estar adequadas ao Padrão Digital ([gov.br DS](https://www.gov.br/ds/home)): um produto de governo que use o Trama aplica essa identidade por meio de tokens alias próprios. A coluna única com alinhamento ao início vale para texto corrido e formulários; ferramentas e painéis seguem Layout e grid.

### Boas práticas

**Revise o padrão mínimo antes de cada publicação.** Inclua a lista na definição de pronto do time e registre quem verificou cada item.

**Trate um item reprovado como defeito.** Itens do padrão mínimo não entram em fila de melhorias; um item reprovado impede a publicação da tela afetada.

**Vá além do mínimo.** O padrão mínimo garante consistência e acessibilidade básicas. A qualidade de um produto depende também de pesquisa com as pessoas e do restante das orientações. O DKFDS lembra que, mesmo com componentes validados, cada solução precisa envolver as pessoas usuárias ([DKFDS](https://designsystem.dk/kom-i-gang/brugerinddragelse/)).

### Considerações por plataforma

#### Web desktop

Verifique os itens nas classes Expandida, Grande e Extragrande e com zoom de 400%. Veja Projetar para web desktop.

#### Web móvel

Verifique alvos de toque, densidade baixa, teclado virtual adequado a cada campo e ausência de rolagem horizontal na classe Compacta. Veja Projetar para web móvel.

#### Tablets e dobráveis

Verifique que o estado se mantém ao girar, abrir e fechar o aparelho. Veja Projetar para tablets e dobráveis.

### Recursos

#### Relacionados

- Princípios de design
- Como começar: design e desenvolvimento
- Acessibilidade
- Legislação e normas
- Cabeçalho
- Rodapé

#### Referências

- [Padrão mínimo](https://www.gov.br/ds/introducao/padrao-minimo) gov.br DS
- [Página inicial](https://www.gov.br/ds/home) gov.br DS
- [Acessibilidade](https://www.gov.br/ds/acessibilidade) gov.br DS
- [Tjekliste](https://designsystem.dk/kom-i-gang/tjekliste/) DKFDS
- [Brugerinddragelse](https://designsystem.dk/kom-i-gang/brugerinddragelse/) DKFDS
- [Styles](https://design-system.service.gov.uk/styles/) GOV.UK Design System
- [Getting started](https://designsystem.ontario.ca/docs/documentation/explore/getting-started.html) Ontario Design System

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## Projetar para web desktop

Em telas grandes, com mouse e teclado, a pessoa espera ver mais conteúdo com menos navegação, agir com precisão e trabalhar em várias janelas ao mesmo tempo.

Web desktop, no Trama, é toda aplicação web exibida em janela de navegador nas classes Expandida (840 a 1199 px), Grande (1200 a 1599 px) e Extragrande (a partir de 1600 px), operada principalmente com mouse ou trackpad e teclado físico. A janela pode ter qualquer tamanho: a pessoa redimensiona, divide a tela com outro programa ou usa vários monitores. Por isso o Trama decide o layout apenas pela largura disponível. O gov.br faz a mesma ressalva: um ponto de quebra não indica o aparelho, porque a pessoa pode ter reduzido a área útil do navegador, e a interface deve funcionar independentemente do dispositivo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

A HIG descreve o uso típico de um computador: a pessoa costuma estar parada, com o aparelho sobre a mesa; as sessões vão de poucos minutos a horas de concentração; e é comum ter vários programas abertos e alternar entre eles ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos)). Essas características valem também para a web no desktop.

### Boas práticas

#### Layout

**Use o espaço para mostrar mais conteúdo com menos níveis.** Em telas grandes, apresente mais conteúdo em menos níveis aninhados e com menos modalidade, mantendo uma densidade confortável ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos)). A partir da classe Expandida, use dois painéis (proporção 38:62 a partir de 960 px) e, na classe Grande, até três. Veja Painéis e split view.

**Escolha largura fixa ou fluida pelo tipo de produto.** O gov.br recomenda grid fluida para sistemas que precisam aproveitar o espaço útil da tela e grid fixa para portais e conteúdo informativo, que não deve sofrer distorção ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). O Trama adota as duas larguras. Em sites e portais, centralize o conteúdo com `max-width` e distribua a sobra nas margens, como o Ontario faz nas larguras grandes ([Ontario](https://designsystem.ontario.ca/components/detail/grid.html)). Em sistemas e ferramentas, ocupe a largura da janela e respeite as margens mínimas de cada classe (32, 40 e 48 px). Veja Layout e grid.

**Limite a largura das linhas de texto.** O GOV.UK recomenda layouts de dois terços ou de dois terços e um terço, o que normalmente significa no máximo 75 caracteres por linha ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)). Mesmo em largura fluida, mantenha texto corrido e formulários numa coluna de no máximo 8 das 12 colunas. Na classe Extragrande, o gov.br recomenda largura fixa por causa de problemas de legibilidade e de hierarquia numa área útil muito extensa ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

**Suporte qualquer largura de janela.** A pessoa pode reduzir o navegador para metade da tela e cair na classe Média ou Compacta. A HIG recomenda decidir o layout pelo espaço disponível e manter as mesmas funções quando o espaço muda ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)). Revise a navegação em cada ponto de quebra, como pede o gov.br ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

**Decida se painéis temporários empurram ou flutuam.** O gov.br separa objetos temporários persistentes, que comprimem a grid e o conteúdo ao aparecer, de flutuantes, que ficam sobre o conteúdo sem alterá-lo, e pede que fiquem perto da área de conteúdo mesmo quando a margem é larga ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). Use painel persistente para navegação e filtros que a pessoa consulta enquanto trabalha; use drawer flutuante para tarefas curtas.

#### Densidade e entrada

**Use densidade alta só onde ela ajuda.** O desktop permite densidade alta (`data-density="alta"`) em tabelas, listas longas e ferramentas, porque o apontador é preciso. O gov.br pede não usar densidade alta em elementos de interação frequente ou de leitura rápida, nem em alertas e mensagens que precisam de destaque ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). Mantenha área de ação de pelo menos 24 px, o mínimo que o gov.br define para o cursor do mouse ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). Veja Densidade.

**Ofereça atalhos de teclado para as ações frequentes.** No desktop, atalhos aceleram o trabalho e permitem usar só o teclado ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos)). Mostre o atalho ao lado do comando em menus. Veja Teclado.

**Aproveite a precisão do ponteiro sem depender dele.** Mouse e trackpad permitem seleção precisa, menus de contexto, arrastar e soltar e estados de hover. O gov.br pede que a pessoa escolha entre teclado e mouse para navegar e possa alternar quando quiser ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). Ofereça sempre um caminho equivalente por teclado e por botão visível. Veja Mouse e trackpad.

**Mantenha a ação perto do conteúdo que ela afeta.** A HIG observa que as pessoas movem janelas de forma que a borda inferior fica fora da tela ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)). Coloque ações principais no início do conteúdo ou junto ao que elas afetam, com a principal primeiro. Barras fixas no rodapé ficam reservadas para web móvel.

#### Janelas, abas e multitarefa

**Abra links na mesma aba.** Abrir novas janelas em excesso cria desordem; deixe a pessoa escolher ([HIG](https://developer.apple.com/design/human-interface-guidelines/windows)). Respeite clique do meio e Ctrl ou ⌘ com clique. Link que sai do domínio do produto leva o ícone de link externo (`.tr-link--external`) e o texto acessível "(site externo)". Se um link precisar abrir em nova aba, diga "(abre em nova aba)" no texto. Veja Links.

**Prepare a aplicação para multitarefa.** No desktop, usar vários programas ao mesmo tempo é o padrão ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)). Salve rascunhos automaticamente, mantenha o estado ao trocar de aba e conclua em segundo plano tarefas iniciadas pela pessoa, como envios de arquivo. Veja Multitarefa e janelas.

#### Comportamento por classe de janela

| Classe      | Largura             | Colunas | Margem mínima | Gutter | Painéis | Navegação                 |
|-------------|---------------------|---------|---------------|--------|---------|---------------------------|
| Expandida   | 840 a 1199 px       | 12      | 32 px         | 24 px  | 2       | Rail ou navegação lateral |
| Grande      | 1200 a 1599 px      | 12      | 40 px         | 24 px  | 2 ou 3  | Navegação lateral fixa    |
| Extragrande | a partir de 1600 px | 12      | 48 px         | 24 px  | 2 ou 3  | Navegação lateral fixa    |

Ao mudar de classe, use as técnicas responsivas que o Fluent descreve: reposicionar, redimensionar, refluir, mostrar ou ocultar e rearquitetar, como exibir lista e detalhe lado a lado em telas grandes ([Fluent 2](https://fluent2.microsoft.design/layout)).

> **Divergência entre referências** O gov.br usa os pontos de quebra 992, 1280 e 1600 px para tablet em paisagem, desktop e TV, com 8 colunas até 1279 px, gutter de 24 px no desktop e de 40 px a partir de 1600 px ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). O One UI define as classes Compacta, Média e Expandida que o Trama adota ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Nenhuma das duas fontes cita pesquisa para seus valores, e nenhuma opção tem vantagem de acessibilidade. O Trama mantém suas classes de janela e seus gutters, e adota do gov.br a escolha entre largura fixa e fluida.

**Faça** use dois painéis quando a janela tiver espaço para lista e detalhe.

**Não faça** estique uma única coluna de lista por toda a largura de uma tela grande.

### Considerações por plataforma

#### Web desktop

Esta página trata da própria plataforma. Teste em pelo menos três larguras: o limite inferior da Expandida (840 px), uma janela típica de notebook na classe Grande e um monitor na Extragrande. Teste também com zoom de 200% e de 400%: o zoom reduz a largura em px CSS e pode levar a página para a classe Compacta. O Fluent lembra que suportar zoom de 400% sem rolagem horizontal significa projetar até a largura de 320 px ([Fluent 2](https://fluent2.microsoft.design/accessibility)), em linha com as Diretrizes de Acessibilidade para Conteúdo Web (WCAG) 2.2, critério 1.4.10. Veja os navegadores que o Trama suporta em Navegadores e dispositivos suportados.

#### Web móvel

Veja Projetar para web móvel.

#### Tablets e dobráveis

Tablets com teclado e trackpad em modo paisagem caem nas classes Expandida e Grande e recebem o layout de desktop, com alvos de toque preservados e densidade padrão. Veja Projetar para tablets e dobráveis.

### Recursos

#### Relacionados

- Layout e grid
- Densidade
- Painéis e split view
- Multitarefa e janelas
- Teclado
- Mouse e trackpad

#### Referências

- [Grid](https://www.gov.br/ds/fundamentos-visuais/grid) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) Apple HIG
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) Apple HIG
- [Windows](https://developer.apple.com/design/human-interface-guidelines/windows) Apple HIG
- [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking) Apple HIG
- [Layout](https://fluent2.microsoft.design/layout) Fluent 2
- [Accessibility](https://fluent2.microsoft.design/accessibility) Fluent 2
- [Layout](https://design-system.service.gov.uk/styles/layout/) GOV.UK Design System
- [Grid](https://designsystem.ontario.ca/components/detail/grid.html) Ontario Design System
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta largura fixa e fluida, densidade alta restrita ao apontador fino, painéis persistentes e flutuantes, regra de links na mesma aba e a divergência sobre pontos de quebra. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                       |

## Projetar para web móvel

No celular, a pessoa segura o aparelho com uma ou duas mãos, interage por toque e teclado virtual e alterna rapidamente entre tarefas curtas.

Web móvel, no Trama, é a aplicação web exibida na classe de janela Compacta (abaixo de 600 px), em geral num celular em modo retrato, ou na classe Média quando o celular está em paisagem. Na Compacta, a grade tem 4 colunas, margens de 16 px e gutters de 16 px, a largura é sempre fluida, o layout usa um único painel e a densidade é baixa.

A HIG resume o contexto: as pessoas seguram o celular com uma ou as duas mãos, trocam entre retrato e paisagem e usam gestos, teclado virtual e voz; às vezes passam um ou dois minutos conferindo algo, às vezes uma hora lendo, e alternam com frequência entre aplicativos ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)). Muitas pessoas usam a internet só pelo celular, às vezes com rede lenta ou instável ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)). Para serviços públicos no Brasil, o gov.br lembra que a Lei nº 14.129/2021 estende a obrigação de acessibilidade aos dispositivos móveis ([gov.br DS](https://www.gov.br/ds/acessibilidade)).

### Boas práticas

#### Layout

**Comece pela tela pequena.** Projete primeiro para telas pequenas, com layout de uma coluna, e amplie a partir daí, para tamanhos de tela e sem supor qual aparelho a pessoa usa ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)). Escreva o CSS base para a classe Compacta e use media queries de largura mínima para as classes maiores.

**Use largura fluida e campos de largura total.** Na grade de 4 colunas, o gov.br recomenda grid fluida e pede evitar a fixa ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)), e recomenda que campos de texto ocupem toda a largura, com densidade baixa para aumentar a área de toque ([gov.br DS](https://www.gov.br/ds/components/input)). Aplique `data-density="baixa"` na Compacta. Veja Densidade.

**Empilhe os botões com a principal em cima.** O gov.br recomenda o botão em bloco em dispositivos de toque, porque facilita alcançar as ações importantes ([gov.br DS](https://www.gov.br/ds/components/button)). Use `.tr-btn--block-compact`, que ocupa a largura total só na classe Compacta e volta ao tamanho do conteúdo a partir de 600 px. Empilhados, a ação principal fica em cima. Veja Botões.

**Mostre só o essencial e deixe o resto a um toque.** Limite o número de controles na tela e torne detalhes e ações secundárias fáceis de descobrir ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)). Exiba menos metadados em janelas pequenas ([Fluent 2](https://fluent2.microsoft.design/layout)). Mova ações secundárias para um menu de excesso, sem remover funções.

**Prefira a rolagem da página.** No celular, o gov.br pede preferir a rolagem da tela à rolagem interna de elementos, mostrar parte do conteúdo antes da primeira rolagem para indicar que há mais e deixar áreas seguras onde a pessoa possa arrastar a tela sem tocar em algo por engano ([gov.br DS](https://www.gov.br/ds/padroes/design/contentoverflow)). Evite rolagem horizontal na página. Veja Excesso de conteúdo.

#### Toque e alcance

**Coloque os controles onde o polegar alcança.** Controles no meio ou na parte de baixo da tela são mais fáceis de alcançar ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)). O One UI separa a tela em área de visualização, no topo, e área de interação, abaixo ([One UI](https://developer.samsung.com/one-ui/layout/basic.html)). Use a barra de navegação inferior para os destinos principais na classe Compacta, como o One UI recomenda para telas pequenas ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

**Use alvos de toque de 44 por 44 px.** Todo controle interativo tem área de toque de pelo menos `--c-touch` nas duas dimensões. A área de toque pode ultrapassar a superfície visível do controle ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). Veja Toque e gestos.

**Não dependa de hover.** O celular não tem hover. O gov.br restringe o tooltip ao toque e ao foco na grade de 4 colunas ([gov.br DS](https://www.gov.br/ds/components/tooltip)) e pede ícones de significado imediato em botões só de ícone, porque o tooltip por hover não existe no celular ([gov.br DS](https://www.gov.br/ds/components/button)). Prefira botão com texto. Veja Tooltips.

#### Teclado virtual e contexto

**Peça o teclado virtual certo para cada campo.** Escolha um teclado que corresponda ao tipo de conteúdo, como o numérico para números ou o de e-mail com "@" e ponto ([HIG](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards)). Na web, use `type`, `inputmode` e `autocomplete` corretos e ajuste a tecla Enter com `enterkeyhint`. Aceite o dado em qualquer formato digitado e mostre o formato esperado no texto de ajuda, sem máscara que impeça digitar ou apagar. Veja Entrada de dados.

**Mantenha o campo ativo visível com o teclado aberto.** O teclado virtual cobre parte da tela. Garanta que o campo em foco, sua mensagem de erro e a ação principal continuem visíveis. Evite barras fixas no rodapé que fiquem presas acima do teclado e cubram o conteúdo.

**Adapte-se a orientação, tema e tamanho de texto.** Responda a mudanças de orientação, modo escuro e tamanho de texto ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)). Com texto maior, elementos lado a lado precisam empilhar ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)). Nunca bloqueie o zoom do navegador.

**Respeite as áreas seguras.** Recortes de câmera e cantos arredondados podem cobrir conteúdo ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)). O One UI evita informação e controles junto às bordas curvas e ao recorte da câmera ([One UI](https://developer.samsung.com/one-ui/layout/grid.html)). Na web, some `env(safe-area-inset-*)` às margens de barras fixas.

**Reduza movimento e peso.** O gov.br pede considerar movimentos simplificados ou reduzidos em celulares e tablets ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)) e desaconselha reprodução automática de carrossel no celular, porque deixa a página mais lenta e a pessoa provavelmente já rolou para baixo ([gov.br DS](https://www.gov.br/ds/components/carousel)). Respeite `prefers-reduced-motion` e ofereça um controle para desligar animações não essenciais. Veja Movimento.

**Prepare-se para interrupções.** A pessoa troca de aplicativo no meio da tarefa. Salve o progresso, preserve o texto digitado e retome no mesmo ponto ([HIG](https://developer.apple.com/design/human-interface-guidelines/multitasking)).

### Fundamentos do Trama e recursos nativos

O gov.br separa o que segue o design system do que segue a plataforma nativa. Na web e na web responsiva, todos os fundamentos visuais seguem o design system; em aplicativos Android e iOS, grid, superfície e elevação seguem a plataforma, e iconografia e movimento são opcionais, para evitar quebra de expectativa e procurar equilíbrio entre os padrões nativos e a identidade visual ([gov.br DS](https://www.gov.br/ds/padroes/mobile/android-e-ios)). O Trama não tem aplicativos nativos. A mesma lógica vale para o que o navegador e o sistema desenham:

| Elemento                                                                            | Quem define | Regra no Trama                                                                                                                                             |
|-------------------------------------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cor, tipografia, espaçamento, estados, grid, elevação, ícones e movimento da página | Trama       | Use os tokens e classes do kit em qualquer classe de janela.                                                                                               |
| Teclado virtual, corretor e preenchimento automático                                | Sistema     | Configure com atributos HTML; não recrie.                                                                                                                  |
| Seletores nativos de arquivo, câmera e compartilhamento                             | Sistema     | Chame o seletor do sistema a partir do botão do Trama.                                                                                                     |
| Barras de rolagem                                                                   | Navegador   | Não personalize. O gov.br pede barras de rolagem que se pareçam com barras de rolagem ([gov.br DS](https://www.gov.br/ds/padroes/design/contentoverflow)). |
| Gestos do sistema e do navegador                                                    | Sistema     | Não capture. Veja Toque e gestos.                                                                                                                          |
| Diálogo de impressão e de compartilhamento                                          | Navegador   | Abra o diálogo nativo. Veja Impressão.                                                                                                                     |

O gov.br também recomenda optar pelos componentes nativos sempre que possível, porque eles trazem recursos de acessibilidade integrados ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

> **Divergência entre referências** Para a grade do celular em retrato, o gov.br usa margem de 8 px e gutter de 16 px ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). O Trama usa 16 px nos dois. Nenhuma fonte traz pesquisa sobre o valor. A margem maior afasta conteúdo e alvos de toque das bordas, o que o One UI recomenda por causa de telas curvas e de toques acidentais da palma ([One UI](https://developer.samsung.com/one-ui/layout/grid.html)). O Trama mantém 16 px. Sobre o tamanho do alvo de toque, veja a divergência registrada em Toque e gestos.

**Faça** use botões de largura total na classe Compacta, com a ação principal em cima.

**Não faça** enfileire várias ações pequenas e de peso igual numa tela de celular.

### Considerações por plataforma

#### Web desktop

Uma janela de navegador estreita no desktop também cai na classe Compacta. O layout deve funcionar com mouse e teclado nessa largura. Veja Projetar para web desktop.

#### Web móvel

Esta página trata da própria plataforma. Teste em aparelhos reais, com rede lenta, com o leitor de tela do sistema e com o maior tamanho de texto disponível. O gov.br pede validar a interface em cada ponto de quebra e no maior número possível de cenários ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

#### Tablets e dobráveis

A tela externa de um dobrável e a tela de um Flip aberto ficam na classe Compacta e recebem o layout móvel. Veja Projetar para tablets e dobráveis.

### Recursos

#### Relacionados

- Layout e grid
- Densidade
- Toque e gestos
- Barra de navegação e rail
- Campos de texto
- Excesso de conteúdo

#### Referências

- [Padrões para Android e iOS](https://www.gov.br/ds/padroes/mobile/android-e-ios) gov.br DS
- [Grid](https://www.gov.br/ds/fundamentos-visuais/grid) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Content overflow](https://www.gov.br/ds/padroes/design/contentoverflow) gov.br DS
- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Button](https://www.gov.br/ds/components/button) gov.br DS
- [Tooltip](https://www.gov.br/ds/components/tooltip) gov.br DS
- [Carousel](https://www.gov.br/ds/components/carousel) gov.br DS
- [Movimento](https://www.gov.br/ds/fundamentos-visuais/movimento) gov.br DS
- [Acessibilidade](https://www.gov.br/ds/acessibilidade) gov.br DS
- [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios) Apple HIG
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) Apple HIG
- [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards) Apple HIG
- [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking) Apple HIG
- [Layout](https://fluent2.microsoft.design/layout) Fluent 2
- [Layout](https://design-system.service.gov.uk/styles/layout/) GOV.UK Design System
- [Ontario Government design principles](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html) Ontario Design System
- [Basic layout](https://developer.samsung.com/one-ui/layout/basic.html) Samsung One UI
- [Grid system](https://developer.samsung.com/one-ui/layout/grid.html) Samsung One UI
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta densidade baixa obrigatória, botões em bloco empilhados, preferência pela rolagem da página, a tabela de fundamentos do Trama e recursos nativos e a divergência sobre margens. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                              |

## Projetar para tablets e dobráveis

Tablets e dobráveis mudam de tamanho, orientação e postura durante o uso, e a aplicação precisa acompanhar cada mudança sem perder o que a pessoa estava fazendo.

Esta página cobre aplicações web exibidas em tablets e em dispositivos dobráveis, como Galaxy Z Fold e Z Flip. Esses aparelhos passam por várias classes de janela do Trama: a tela externa de um Fold fica na classe Compacta; a tela interna aberta fica na Média ou Expandida; um tablet em paisagem chega à Expandida ou à Grande. O One UI faz o mesmo mapeamento: Z Fold em retrato e paisagem e tablets pequenos em retrato na classe Média, tablets em retrato e paisagem na classe Expandida ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)).

O gov.br lembra que girar um tablet entre retrato e paisagem muda o ponto de quebra sem mudar o aparelho, e que a interface precisa funcionar em qualquer caso, principalmente nos elementos interativos, por toque ou clique ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). A HIG descreve o tablet como uma tela grande que a pessoa segura, apoia numa superfície ou num suporte, com entrada por toque, teclado virtual, teclado e apontador físicos, caneta ou voz, muitas vezes combinados ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados)). Nos dobráveis, a pessoa abre e fecha o aparelho com frequência, e a continuidade entre as telas é essencial ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Boas práticas

#### Layout em vários painéis

**Use vários painéis em telas grandes.** Um layout em vários painéis mostra mais informação ao mesmo tempo e achata a navegação, porque a pessoa acessa o conteúdo sem trocar a tela inteira. Aplicativos esticados são mais difíceis de ler e desperdiçam espaço ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). O Trama adota as proporções que o One UI recomenda:

| Largura da janela  | Painel 1 | Painel 2 |
|--------------------|----------|----------|
| 600 a 959 px       | 42%      | 58%      |
| A partir de 960 px | 38%      | 62%      |
| Dobrável aberto    | 50%      | 50%      |

Use o componente `.tr-panes` (38:62) e `.tr-panes--50` no dobrável aberto. Em tablets em paisagem, considere três painéis ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Veja Painéis e split view.

**Mostre um nível a mais de hierarquia quando houver espaço.** Mantenha a mesma hierarquia de informação nas duas telas e acrescente um nível na tela maior. No exemplo da HIG, o Mail mostra a lista ou o e-mail com o aparelho fechado, e os dois lado a lado com ele aberto ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)).

**Prefira largura fluida.** O gov.br recomenda grid fluida na grade de 8 colunas e pede cautela com a fixa, que reserva em geral para tablet em paisagem ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). O One UI pede que o aplicativo preencha a tela sem faixas vazias nas laterais ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Use largura fluida em sistemas e ferramentas; em portais de leitura, limite só a coluna de texto.

**Decida se a navegação empurra o conteúdo ou flutua sobre ele.** O gov.br chama de persistente o painel que comprime a grid ao aparecer e de flutuante o que fica por cima sem alterá-la, e pede rever o comportamento do flutuante em cada grade ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). Na classe Média, abra a navegação completa como gaveta flutuante sobre o conteúdo; a partir da Expandida, mantenha-a persistente ao lado.

#### Navegação por classe de janela

**Ajuste o controle de navegação ao tamanho da tela.** O One UI recomenda barra de navegação inferior em telas pequenas, rail lateral em telas médias e gaveta de navegação visível em telas grandes, e pede rail para o Z Fold em retrato ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). O Trama segue esse modelo:

| Classe                 | Painéis | Navegação                             | Exemplo de aparelho                             |
|------------------------|---------|---------------------------------------|-------------------------------------------------|
| Compacta (\< 600)      | 1       | Barra inferior, gaveta flutuante      | Tela externa do Fold, Flip aberto               |
| Média (600 a 839)      | 1 ou 2  | Rail, gaveta flutuante                | Tela interna do Fold, tablet pequeno em retrato |
| Expandida (840 a 1199) | 2       | Rail ou navegação lateral persistente | Tablet em retrato ou paisagem                   |
| Grande (≥ 1200)        | 2 ou 3  | Navegação lateral persistente         | Tablet grande em paisagem                       |

#### Continuidade

**Retome exatamente de onde a pessoa parou.** Quando a pessoa abre o aparelho, o aplicativo deve aparecer na tela principal no mesmo ponto. Ao trocar de tela, mantenha a posição de rolagem e preserve o texto digitado e o teclado aberto ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Na web, abrir ou fechar o aparelho dispara um redimensionamento da janela: guarde seleção, foco e rascunhos no estado da aplicação e evite recarregar a página.

**Mantenha as mesmas funções em qualquer postura.** Controles podem ir para um menu de excesso e o conteúdo pode mudar de posição; a pessoa continua com acesso aos mesmos controles e conteúdos em qualquer forma de segurar o aparelho ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)).

**Evite mudanças bruscas de layout.** Mova só o necessário para manter os elementos visíveis e fáceis de tocar. Controles que somem ou mudam muito de lugar são mais difíceis de achar ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)). O gov.br observa que movimentos abruptos podem causar confusão e sobrecarga cognitiva ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

#### O vinco

**Mantenha elementos interativos longe do vinco.** Evite posicionar elementos interativos perto do vinco no meio da tela ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Quando o aparelho está parcialmente dobrado, a região da dobra divide a tela em áreas utilizáveis e fica de fora ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)). Em grades, prefira número par de colunas para que o conteúdo se divida bem dos dois lados ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo)). Veja Postura e dobra.

#### Entrada e densidade

**Use densidade baixa no toque.** Tablets e dobráveis são operados principalmente com os dedos. Aplique `data-density="baixa"` e mantenha alvos de `--c-touch` mesmo quando um trackpad estiver conectado. Passe para a densidade padrão só quando a media query `(any-pointer: coarse)` for falsa. Veja Densidade.

**Suporte várias entradas ao mesmo tempo.** Deixe a pessoa usar toque, teclado, trackpad e caneta, e use a distância de visualização e o modo de entrada para decidir tamanho e densidade do conteúdo ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados)). O gov.br pede aproveitar o ponto forte de cada interação, como gestos em interfaces de toque, sem esquecer as outras ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

**Use popovers perto do controle que os abriu.** Para entradas curtas, use um popover pequeno em vez de ocupar a tela inteira, perto do elemento tocado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Aproveite a tela grande para reduzir interfaces modais e transições de tela cheia ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados)). Veja Popovers.

**Considere como a pessoa segura o aparelho.** Em telas grandes, controles na parte de baixo podem ficar longe das mãos. O aplicativo Câmera do One UI coloca os controles na lateral ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)).

**Funcione bem em tela dividida.** Em telas grandes, a pessoa pode ter até 3 aplicativos em tela dividida e 5 em janelas pop-up, e redimensiona as janelas ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Em tela dividida, a aplicação pode cair na classe Compacta mesmo num tablet. Ofereça arrastar e soltar entre janelas com feedback visual claro. Veja Arrastar e soltar.

> **Divergência entre referências** O gov.br usa a grade de 8 colunas, com gutter de 24 px e margem de 40 px, de 576 a 1279 px, cobrindo celular em paisagem e tablet em retrato e em paisagem ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)), e trata a densidade média como padrão de campos de texto em tablet e desktop ([gov.br DS](https://www.gov.br/ds/components/input)). O Trama usa 8 colunas só na classe Média (600 a 839 px), com margem de 24 px e gutter de 16 px, e 12 colunas a partir de 840 px, seguindo as classes do One UI. Nenhuma fonte traz pesquisa sobre os valores, e o Trama mantém suas classes. Na densidade, o Trama decide pelo critério de acessibilidade: densidade baixa em toda tela operada por toque, porque ela dá mais margem ao alvo de toque.

### Considerações por plataforma

#### Web desktop

Nenhuma consideração adicional para Web desktop.

#### Web móvel

A tela externa dos dobráveis segue as regras de web móvel.

#### Tablets e dobráveis

Detecte o espaço disponível com media queries de largura. Navegadores baseados em Chromium oferecem APIs específicas para telas segmentadas: a media query `horizontal-viewport-segments` (e `vertical-viewport-segments`), as variáveis de ambiente `env(viewport-segment-left 0 0)` e afins, e a Device Posture API, com a media query `device-posture`. Trate essas APIs como aprimoramento progressivo: o layout precisa funcionar só com as classes de janela, e o suporte dos navegadores deve ser conferido antes de usar.

``` code
/* Dobrável aberto com dois segmentos lado a lado */
@media (horizontal-viewport-segments: 2) {
  .app-panes {
    grid-template-columns:
      env(viewport-segment-width 0 0)
      env(viewport-segment-width 1 0);
    column-gap: calc(env(viewport-segment-left 1 0) - env(viewport-segment-right 0 0));
  }
}
```

### Recursos

#### Relacionados

- Postura e dobra
- Painéis e split view
- Layout e grid
- Densidade
- Multitarefa e janelas
- Barra de navegação e rail

#### Referências

- [Grid](https://www.gov.br/ds/fundamentos-visuais/grid) gov.br DS
- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Movimento](https://www.gov.br/ds/fundamentos-visuais/movimento) gov.br DS
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI
- [Layout design for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html) Samsung One UI
- [Designing for iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados) Apple HIG
- [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) Apple HIG

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta largura fluida, navegação persistente ou flutuante por classe, densidade baixa no toque e a divergência sobre a grade de 8 colunas. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                  |

