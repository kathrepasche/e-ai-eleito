# Fundamentos: Iconografia a Internacionalização e direita para esquerda

## Iconografia

Um bom ícone expressa um único conceito de forma que as pessoas entendam na hora, quase sempre acompanha um texto e significa a mesma coisa em todo produto.

Ícones de interface usam formas simplificadas e pouca cor para comunicar uma ideia direta: um objeto, uma ação ou um modo ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/icons)). Eles reforçam uma ação ou informação e tornam a página mais fácil de escanear, mas raramente substituem o texto ([DKFDS](https://designsystem.dk/styleguide/ikoner/)). O Padrão Digital de Governo acrescenta um objetivo: com um padrão gráfico e um significado fixo para cada ícone, a pessoa reconhece e memoriza as funções em todos os sistemas do governo federal ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)).

O Trama adota o **Material Symbols** no estilo **Outlined**, com peso 400 e tamanho óptico 24, a configuração indicada pelo DKFDS ([DKFDS](https://designsystem.dk/styleguide/ikoner/)). O Ontario também usa a biblioteca do Material, em versão preenchida ([Ontario](https://designsystem.ontario.ca/components/detail/icons-primary.html)). Ícones próprios de um produto seguem a mesma grade, o mesmo traço e os mesmos tamanhos.

### Boas práticas

#### Quando usar

**Use ícones como complemento do texto.** Sempre que possível, mostre um rótulo ao lado do ícone ([DKFDS](https://designsystem.dk/styleguide/ikoner/), [gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)). A mesma imagem pode significar coisas diferentes para pessoas diferentes; o texto desfaz a ambiguidade ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Na dúvida, use só o texto ([DKFDS](https://designsystem.dk/styleguide/ikoner/)).

**Não use ícones como enfeite.** Ícones decorativos viram ruído visual e aumentam a carga cognitiva ([DKFDS](https://designsystem.dk/styleguide/ikoner/)). Todo ícone precisa ajudar a pessoa a concluir a tarefa ([Ontario](https://designsystem.ontario.ca/components/detail/icons-primary.html)).

**Reserve botões só com ícone para ações conhecidas e espaço curto.** Ordenação em tabelas, fechar, mais ações e excluir em listas compactas são exemplos ([DKFDS](https://designsystem.dk/komponenter/knapper/)). Sem texto, o ícone precisa expressar bem a ação, com tooltip para reforçar ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Passe para ilustração quando a ideia for complexa.** Ícones representam um único objeto, ação ou ideia; conceitos mais complicados pedem ilustração ou infográfico ([Ontario](https://designsystem.ontario.ca/components/detail/icons-primary.html)). O gov.br compara ilustrações a parágrafos e ícones a marcadores ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Veja Ilustração.

#### Significado

**Dê um único significado a cada ícone, o do catálogo.** A lupa serve só para pesquisa e nunca para ampliar a tela ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Atribuir significados diferentes ao mesmo ícone confunde ([DKFDS](https://designsystem.dk/styleguide/ikoner/), [gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)).

**Num elemento interativo, o ícone representa a ação que será executada.** Num elemento não interativo, ele pode representar um estado ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)). Um cadeado num botão quer dizer "Bloquear"; ao lado de um campo, quer dizer "bloqueado".

**Escolha metáforas reconhecíveis no contexto cultural do Brasil.** O gov.br pede ícones alinhados ao contexto cultural brasileiro, de fácil reconhecimento público ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)). Busque reconhecimento universal mais do que representação completa: a cadeira de rodas representa acessibilidade, mesmo sem representar todas as deficiências ([Ontario](https://designsystem.ontario.ca/components/detail/icons-primary.html)). Prefira figuras humanas sem gênero ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/icons)).

**Evite letras dentro de ícones.** Use texto só quando for essencial, como num ícone de negrito, e localize os caracteres ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/icons)). Veja Internacionalização.

### Catálogo de ações

O catálogo associa cada ação a um único ícone, com os verbos do vocabulário controlado. A coluna gov.br mostra a classe do Font Awesome que o Padrão Digital de Governo atribui à mesma ação ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)), para facilitar a convivência com produtos do governo federal.

| Ação ou estado                           | Desenho                                                                         | Material Symbols                                | gov.br                                                                            |
|------------------------------------------|---------------------------------------------------------------------------------|-------------------------------------------------|-----------------------------------------------------------------------------------|
| Pesquisar                                | Lupa                                                                            | `search`                                        | `fa-search`                                                                       |
| Filtrar                                  | Linhas decrescentes                                                             | `filter_list`                                   | `fa-sliders-h`                                                                    |
| Adicionar, criar                         | Sinal de mais                                                                   | `add`                                           | `fa-plus`                                                                         |
| Subtrair (em campo numérico)             | Sinal de menos                                                                  | `remove`                                        | `fa-minus`                                                                        |
| Editar                                   | Lápis                                                                           | `edit`                                          | `fa-edit`                                                                         |
| Excluir                                  | Lixeira                                                                         | `delete`                                        | `fa-trash-alt`                                                                    |
| Limpar                                   | Borracha                                                                        | `ink_eraser`                                    | `fa-eraser`                                                                       |
| Fechar                                   | X                                                                               | `close`                                         | `fa-times`                                                                        |
| Confirmar                                | Visto                                                                           | `check`                                         | `fa-check`                                                                        |
| Baixar                                   | Seta para baixo sobre linha                                                     | `download`                                      | `fa-download`                                                                     |
| Enviar arquivo                           | Seta para cima sobre linha                                                      | `upload`                                        | `fa-upload`                                                                       |
| Anexar                                   | Clipe                                                                           | `attach_file`                                   | `fa-paperclip`                                                                    |
| Enviar mensagem                          | Avião de papel                                                                  | `send`                                          | `fa-share`                                                                        |
| Compartilhar                             | Três nós ligados                                                                | `share`                                         | `fa-share-square`                                                                 |
| Copiar, cortar                           | Duas folhas; tesoura                                                            | `content_copy`, `content_cut`                   | `fa-copy`, `fa-cut`                                                               |
| Imprimir                                 | Impressora                                                                      | `print`                                         | `fa-print`                                                                        |
| Atualizar                                | Setas em círculo                                                                | `refresh`                                       | `fa-sync`                                                                         |
| Mostrar, ocultar                         | Olho; olho cortado                                                              | `visibility`, `visibility_off`                  | `fa-eye`, `fa-eye-slash`                                                          |
| Bloquear, desbloquear                    | Cadeado fechado; aberto                                                         | `lock`, `lock_open`                             | `fa-lock`, `fa-unlock`                                                            |
| Selecionar data; hora                    | Calendário; relógio                                                             | `calendar_month`, `schedule`                    | `fa-calendar-alt`, `fa-clock`                                                     |
| Ordenar (padrão, crescente, decrescente) | Setas                                                                           | `unfold_more`, `arrow_upward`, `arrow_downward` | `fa-sort`, `fa-sort-up`, `fa-sort-down`                                           |
| Voltar, avançar (direcionais)            | Chevrons laterais                                                               | `chevron_left`, `chevron_right`                 | `fa-chevron-left`, `fa-chevron-right`                                             |
| Expandir, recolher                       | Chevron para baixo; para cima                                                   | `expand_more`, `expand_less`                    | `fa-chevron-down`, `fa-chevron-up`                                                |
| Abrir lista de opções (select, menu)     | Chevron para baixo                                                              | `expand_more`                                   | `fa-caret-down`                                                                   |
| Menu principal                           | Três linhas                                                                     | `menu`                                          | `fa-bars`                                                                         |
| Mais ações                               | Três pontos (vertical em linhas, horizontal em barras)                          | `more_vert`, `more_horiz`                       | `fa-ellipsis-v`                                                                   |
| Página inicial                           | Casa                                                                            | `home`                                          | `fa-home`                                                                         |
| Configurações                            | Engrenagem                                                                      | `settings`                                      | `fa-cog`                                                                          |
| Entrar, conta                            | Pessoa                                                                          | `person`                                        | `fa-user`                                                                         |
| Mensagens; mensagem lida                 | Envelope; envelope aberto                                                       | `mail`, `drafts`                                | `fa-envelope`, `fa-envelope-open`                                                 |
| Notificações; desativar notificações     | Sino; sino cortado                                                              | `notifications`, `notifications_off`            | `fa-bell`, `fa-bell-slash`                                                        |
| Pasta; pasta atual                       | Pasta fechada; aberta                                                           | `folder`, `folder_open`                         | `fa-folder`, `fa-folder-open`                                                     |
| Incluir imagem                           | Paisagem                                                                        | `image`                                         | `fa-image`                                                                        |
| Áudio ligado; mudo                       | Alto-falante                                                                    | `volume_up`, `volume_off`                       | `fa-volume-up`, `fa-volume-mute`                                                  |
| Ativar Libras; alto contraste            | Mãos; círculo meio preenchido                                                   | `sign_language`, `contrast`                     | `fa-deaf`, `fa-adjust`                                                            |
| Densidade alta; baixa                    | Linhas juntas; espaçadas                                                        | `density_small`, `density_large`                | `fa-th`, `fa-th-large`                                                            |
| Ajuda                                    | Interrogação em círculo                                                         | `help`                                          | `fa-question`                                                                     |
| Abre em nova aba, site externo           | Seta saindo de quadrado                                                         | `open_in_new`                                   | Não definido                                                                      |
| Informação, sucesso, alerta, erro        | i em círculo, visto em círculo, triângulo com exclamação, exclamação em círculo | `info`, `check_circle`, `warning`, `error`      | `fa-info-circle`, `fa-check-circle`, `fa-exclamation-triangle`, `fa-times-circle` |

> **Divergência entre referências** O gov.br usa X em círculo para mensagem de erro e X para fechar ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)); o DKFDS usa o ícone `error`, de exclamação em círculo ([DKFDS](https://designsystem.dk/styleguide/ikoner/)). Pela regra de um significado por ícone, que gov.br, GOV.UK e DKFDS compartilham, o Trama mantém o X só para fechar e usa exclamação em círculo para erro. O gov.br usa caret para abrir dropdown e chevron para expandir; o Trama usa um único chevron para os dois, coerente com a regra de indicador de expansão. Para filtrar, o Trama mantém as linhas decrescentes, que coincidem com o símbolo padrão da HIG ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/icons)), e reserva os controles deslizantes do gov.br para "Ajustar exibição", com `tune`.

**Consulte o catálogo antes de criar um ícone.** Verifique se a função já tem ícone atribuído; se a biblioteca não tiver o ícone, desenhe um novo seguindo o estilo dela e valide com a equipe de design ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)) e com pessoas ([DKFDS](https://designsystem.dk/styleguide/ikoner/)).

### Grade e estilo

**Desenhe na grade de 24 × 24px.** O Trama define a grade de 24 × 24px com área útil de 20 × 20px, traço de 2px e as mesmas junções e terminais da biblioteca. O HDS também usa 24 × 24px como tamanho padrão ([HDS](https://hds.hel.fi/foundation/visual-assets/icons)). Ícones assimétricos, como o de baixar, recebem ajuste óptico como margem interna do próprio arquivo ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/icons)).

**Mantenha consistência visual.** Todos os ícones de um produto usam o mesmo tamanho, nível de detalhe, espessura de traço e perspectiva ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/icons)). Não misture bibliotecas.

**Use contorno por padrão e preenchido para o item atual.** O contorno combina com texto em barras e listas; a variante preenchida dá ênfase e marca seleção ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols), [Fluent 2](https://fluent2.microsoft.design/iconography)). No Trama, só a navegação (`.tr-nav`, `.tr-rail`, `.tr-bottom-nav`) troca para a variante preenchida no item atual.

> **Divergência entre referências** O gov.br usa o Font Awesome 5.10.2 no estilo Solid, preenchido, numa grade de 20 × 16px, entregue como fonte de ícones ou SVG com JavaScript ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)). HIG e Fluent usam contorno como padrão e preenchido para seleção, o DKFDS usa contorno com tamanho óptico 24 e o HDS adota 24 × 24px. Pela convergência, o Trama mantém contorno, grade de 24px e SVG. A escolha de SVG também atende ao critério de acessibilidade: uma fonte de ícones pode falhar quando a pessoa força uma fonte própria no navegador, e um SVG em linha não depende disso.

**Use uma única cor.** Ícones herdam `currentColor` do texto ao lado, normalmente `--t-fg-1` ou `--t-fg-2`. Cor extra só para status, com os tokens semânticos ([HDS](https://hds.hel.fi/foundation/visual-assets/icons), [Fluent 2](https://fluent2.microsoft.design/iconography)).

### Tamanhos

| Token                      | Tamanho    | Uso                                                           |
|----------------------------|------------|---------------------------------------------------------------|
| `--icon-xs`                | 12px       | Só informativo, junto a Caption. Nunca interativo.            |
| `--icon-sm`                | 16px       | Junto a Body small, em badges e metadados; botões `--c-h-sm`. |
| `--icon-md`                | 20px       | Botões `--c-h-md`, itens de menu, ícone de mensagens.         |
| `--icon-lg`                | 24px       | Padrão: navegação, barras de ferramentas, botões `--c-h-lg`.  |
| `--icon-xl`                | 32px       | Destaques em cards e listas.                                  |
| `--icon-2xl`, `--icon-3xl` | 48px, 64px | Estados vazios. Nunca acima de 64px.                          |

O HDS usa 24px como padrão, pede atenção à legibilidade em 16px e desaconselha passar de 64px ([HDS](https://hds.hel.fi/foundation/visual-assets/icons)). O Fluent reserva 12px para informação, nunca para interação ([Fluent 2](https://fluent2.microsoft.design/iconography)). Acima de 64px, use ilustração: o gov.br troca ilustração por ícone quando o espaço tem menos de 80px de largura ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)).

> **Divergência entre referências** O gov.br usa 16px como tamanho base e uma escala de 8px a 160px ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)). O Trama não usa ícones abaixo de 12px, o mesmo mínimo do texto, e limita a escala a 64px, como o HDS. O padrão de 24px segue HDS e DKFDS. A versão 1.0 proibia ícones abaixo de 16px; o Trama passou a aceitar 12px só para ícones informativos, como o Fluent.

**Separe tamanho do ícone e área de ação.** Ícones interativos têm área mínima mesmo quando o desenho é menor, e essa área conta no espaçamento entre elementos ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)). No Trama, a área é de 24 × 24px com mouse e de `--c-touch` (44px) em toque. O gov.br pede 48px de toque para ícones; a decisão do Trama por 44px está em Acessibilidade.

### Acessibilidade

**Oculte ícones decorativos.** Ícone decorativo é o que, removido, não muda o entendimento da página, como um ícone ao lado do rótulo. Use `aria-hidden="true"` e `focusable="false"` no SVG ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia), [Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

**Dê nome a ícones semânticos.** Ícone semântico transmite significado sem texto ao lado. Em controle interativo, ponha `aria-label` no próprio botão ou link; fora de controle, use texto visualmente oculto ou `role="img"` com nome no SVG ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)). Descreva a ação, como "Excluir item", e não a forma, como "Lixeira".

**Mostre o nome de botões só com ícone num tooltip focável.** Exiba o tooltip no hover e no foco de teclado e, em toque, ao manter pressionado ([One UI](https://developer.samsung.com/one-ui/accessibility/layout-and-typo.html)). O gov.br aceita o atributo `title` ou um tooltip próprio ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)); o Trama usa o componente Tooltip, porque o `title` não aparece no foco de teclado.

**Garanta 3:1 de contraste para ícones informativos.** Ícones que transmitem informação seguem a WCAG 2.2, 1.4.11 ([Fluent 2](https://fluent2.microsoft.design/accessibility)). O gov.br aplica a ícones as mesmas regras de contraste de texto grande ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). `--t-fg-3` e as cores semânticas atendem nos dois temas.

### Considerações por plataforma

#### Web desktop

Barras de ferramentas em densidade alta podem usar botões só com ícone de `--c-h-sm` e ícone `--icon-sm`, sempre com tooltip e atalho de teclado no tooltip, quando houver.

#### Web móvel

Na barra de navegação inferior (`.tr-bottom-nav`), todo ícone tem rótulo de texto visível. Ícones em telas pequenas podem precisar ser maiores para oferecer alvos maiores ([Fluent 2](https://fluent2.microsoft.design/iconography)); a área de toque é sempre de pelo menos `--c-touch`.

#### Tablets e dobráveis

No rail de navegação (`.tr-rail`), mantenha o rótulo abaixo do ícone. Ao abrir um dobrável, o mesmo destino mantém o mesmo ícone entre a barra inferior da tela externa e o rail da tela interna. Em RTL, espelhe só os ícones marcados como direcionais.

### Recursos

#### Relacionados

- Ilustração
- Imagens
- Escrita e conteúdo
- Botões
- Tooltips
- Tokens de design
- Internacionalização e direita para esquerda

#### Referências

- [Iconografia](https://www.gov.br/ds/fundamentos-visuais/iconografia) gov.br DS
- [Ilustração](https://www.gov.br/ds/fundamentos-visuais/ilustracao) gov.br DS
- [Cores](https://www.gov.br/ds/fundamentos-visuais/cores) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Icons](https://developer.apple.com/design/human-interface-guidelines/icons) Apple HIG
- [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) Apple HIG
- [Iconography](https://fluent2.microsoft.design/iconography) Fluent 2
- [Accessibility](https://fluent2.microsoft.design/accessibility) Fluent 2
- [Ikoner](https://designsystem.dk/styleguide/ikoner/) Det Fælles Designsystem
- [Knapper](https://designsystem.dk/komponenter/knapper/) Det Fælles Designsystem
- [Images](https://design-system.service.gov.uk/styles/images/) GOV.UK Design System
- [Primary icons](https://designsystem.ontario.ca/components/detail/icons-primary.html) Ontario Design System
- [Images and photography](https://designsystem.ontario.ca/components/detail/images.html) Ontario Design System
- [Icons](https://hds.hel.fi/foundation/visual-assets/icons) Helsinki Design System
- [Layout and typography](https://developer.samsung.com/one-ui/accessibility/layout-and-typo.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Amplia o catálogo de ações com a correspondência do gov.br, cria os tokens `--icon-*` e a grade de 24px, acrescenta a distinção entre ação e estado e entre ícones decorativos e semânticos, corrige o estilo usado pelo Ontario (preenchido) e registra as divergências sobre estilo, tamanhos, erro e área de toque. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                                                                                                          |

## Imagens

Use fotos e ilustrações só quando elas ajudam a entender algo ou a concluir uma tarefa, e garanta que a informação delas chegue também a quem não pode vê-las.

Serviços costumam funcionar melhor sem depender de imagens. Comece pelo texto claro; acrescente uma imagem quando ela tornar uma instrução mais fácil de entender, e mantenha no texto toda a informação necessária para concluir a tarefa ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). O Ontario resume a mesma regra no princípio de incluir apenas elementos com propósito ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

Esta página cobre quando usar fotografia e ilustração, como escrever texto alternativo e como preparar arquivos para web desktop, web móvel e tablets. Para o componente que exibe imagens, veja Imagem; para ilustrações, Ilustração; para ícones, Iconografia.

### Boas práticas

#### Quando usar

**Use imagens só quando houver necessidade real.** Evite imagens decorativas ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Não use imagens sem relação com o assunto da página nem imagens pequenas demais para mostrar os detalhes importantes, sobretudo em celulares ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

**Use imagens para coisas concretas.** Documentos, objetos e telas funcionam; conceitos abstratos, como "sinergia" ou "confiança", não ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

**Escolha entre foto e ilustração pela natureza do assunto.** Representações que precisam ser realistas funcionam melhor com fotografia; assuntos abstratos, processos, diagramas e fluxos pedem ilustração ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). O GOV.UK traça a mesma linha: foto para mostrar algo como é, ilustração para simplificar algo complexo ([GOV.UK](https://design-system.service.gov.uk/styles/images/)).

#### Fotografia

**Use fotografia quando for importante mostrar algo como ele é.** Por exemplo, a prévia de um documento que a pessoa enviou ou um produto cujos detalhes importam ([GOV.UK](https://design-system.service.gov.uk/styles/images/), [gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Não use fotos para transmitir emoção ou impressão abstrata e evite fotos genéricas de banco de imagens ([GOV.UK](https://design-system.service.gov.uk/styles/images/)).

> **Divergência entre referências** O gov.br também indica fotografia para criar uma "experiência visual" que transporte a pessoa a um lugar ou desperte nostalgia, e para mostrar um rosto conhecido que endosse o conteúdo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). O GOV.UK proíbe fotos para transmitir emoção ([GOV.UK](https://design-system.service.gov.uk/styles/images/)), e o Ontario restringe imagens a coisas concretas e a usos com propósito ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)). Pela convergência, o Trama não usa foto para criar clima. Uma pessoa real aparece só quando o conteúdo é sobre ela, como numa notícia, nunca como endosso implícito.

**Escolha fotos autênticas e representativas.** Pessoas reais em situações reais, com diversidade de idade, corpo, origem e capacidade ([Ontario](https://designsystem.ontario.ca/components/detail/images.html), [HDS](https://hds.hel.fi/foundation/guidelines/inclusivity)). Veja Inclusão.

**Confirme a licença de toda imagem.** Não use fotos cuja origem, autoria ou direitos você não conhece, nem imagens com marca d'água; obtenha permissão do fotógrafo para fotos pessoais ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

#### Ilustração

**Use ilustrações para simplificar algo complexo.** Mostrar uma interação física, como fotografar um documento, ou indicar onde fica um número num formulário ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Anatomia, paleta, personagens, estilos e tamanhos estão em Ilustração.

#### Texto em imagens

**Não coloque texto dentro de imagens.** Texto em imagem não pode ser lido por leitor de tela, copiado, destacado, ampliado ou recolorido ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Também cria barreiras para quem usa celular ou tem baixa visão ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)). Publique postagens, trechos de documentos e dados de apresentações como texto (WCAG 2.2, 1.4.5).

**Aceite texto só quando ele for essencial ou incidental.** Logotipos e assinaturas são essenciais; letreiros ao fundo de uma foto são incidentais ([GOV.UK](https://design-system.service.gov.uk/styles/images/)).

**Se precisar sobrepor texto, use HTML sobre a imagem com overlay.** Garanta 4.5:1 entre o texto e todas as partes da imagem por trás dele, em todos os tamanhos de tela e níveis de zoom ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Aplique `--t-overlay-text`, o degradê de legibilidade que o gov.br recomenda quando o contraste entre texto e imagem não basta ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)), e meça o contraste mesmo assim. Diagramas com texto devem ser SVG, para continuar nítidos com zoom.

#### Gráficos e imagens complexas

**Ofereça os dados em texto.** Escreva um texto alternativo curto com o significado da imagem e uma descrição longa, visível para todos, com os dados ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Para infográficos, ofereça a descrição no próprio contexto ou por um link, e os dados também em tabela ou planilha ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Uma tabela ou um resumo textual ajudam a pessoa a chegar à conclusão ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/tilgaengelig-grafik/)).

**Não comunique só com cor.** Use também padrões, formas e tipos de linha. A visualização deve continuar legível em preto e branco ([DKFDS](https://designsystem.dk/styleguide/datavisualisering-infografik/tilgaengelig-grafik/)). Veja Visualização de dados.

### Texto alternativo

O texto alternativo é lido por leitores de tela e aparece quando a imagem não carrega ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Toda imagem tem o atributo `alt`, mesmo que vazio ([GOV.UK](https://design-system.service.gov.uk/styles/images/), [Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

| Situação                                               | Atributo                                                    |
|--------------------------------------------------------|-------------------------------------------------------------|
| Imagem decorativa, sem informação                      | `alt=""`                                                    |
| Ícone ao lado de um rótulo de texto                    | `alt=""` ou `aria-hidden="true"` no SVG                     |
| Imagem dentro de link cujo texto já descreve o destino | `alt=""`                                                    |
| Imagem com informação que não está no texto            | `alt` descritivo, até 125 caracteres e duas frases          |
| Descrição longa ou contexto necessário a todos         | Legenda visível (`figcaption`); `alt` sem repetir a legenda |
| Gráfico ou diagrama                                    | `alt` curto com a conclusão, mais descrição longa visível   |
| SVG informativo                                        | `role="img"` e `aria-label`                                 |

A tabela reúne regras do GOV.UK e do Ontario ([GOV.UK](https://design-system.service.gov.uk/styles/images/), [Ontario](https://designsystem.ontario.ca/components/detail/images.html)). Um teste prático: escreva o texto alternativo e veja se ele acrescenta algo para quem ouve; se não acrescentar, a imagem é decorativa ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

**Descreva conteúdo e função em até 125 caracteres.** O gov.br recomenda descrições de no máximo 125 caracteres, flexíveis conforme a complexidade do conteúdo ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)); GOV.UK e Ontario limitam a duas frases ([GOV.UK](https://design-system.service.gov.uk/styles/images/), [Ontario](https://designsystem.ontario.ca/components/detail/images.html)). O Trama adota os dois limites: até 125 caracteres e até duas frases, com pontuação normal. Se a informação essencial não couber, ela vai para a legenda ou para uma descrição longa. Inclua no `alt` o texto essencial que estiver dentro da imagem ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). O texto deve fazer sentido sem referência visual ([One UI](https://developer.samsung.com/one-ui/accessibility/screen-reader.html)).

**Escreva frases, não listas de palavras-chave.** "Ponte no Central Park, em Nova York, cercada por árvores e flores" descreve; "ponte flores árvores parque verde" não ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Não repita a legenda no texto alternativo.** Legenda e texto alternativo têm papéis diferentes. Use legenda para descrições longas, que ficam disponíveis para todos; repetir o mesmo conteúdo no `alt` cansa quem usa leitor de tela ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing), [Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

**Não comece com "Imagem de" ou "Foto de".** O leitor de tela já anuncia que é uma imagem. Não repita o texto da página, não inclua o nome do autor e não acrescente o que a imagem não mostra ([GOV.UK](https://design-system.service.gov.uk/styles/images/), [Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

**Faça** Descreva o que importa para a tarefa.

**Não faça** Anuncie o tipo de mídia ou dê crédito no texto alternativo.

### Vídeo e áudio

**Ofereça legendas e transcrição em todo vídeo e áudio.** Legendas e transcrições devem estar disponíveis em qualquer dispositivo, sem atrapalhar a experiência, e a informação do vídeo também deve existir em outro formato ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing), [gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Para conteúdo audiovisual com informação visual importante, ofereça audiodescrição (WCAG 2.2, 1.2.5). Não reproduza mídia automaticamente.

### Arquivos e desempenho

| Tipo de imagem                       | Formato                                  |
|--------------------------------------|------------------------------------------|
| Fotografias e imagens complexas      | JPEG, ou WebP e AVIF com JPEG de reserva |
| Ilustrações com áreas de cor chapada | SVG; PNG se não houver vetor             |
| Imagens com transparência            | PNG ou SVG                               |
| Ícones e ilustrações icônicas        | SVG                                      |

A escolha de formatos segue as recomendações do Ontario e da HIG ([Ontario](https://designsystem.ontario.ca/components/detail/images.html), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/images)).

**Forneça versões para telas de alta densidade.** Telas de alta resolução exigem imagens com mais pixels ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/images)). Na web, use `srcset` com descritores de largura e `sizes` coerente com as colunas do grid, para que o navegador escolha o arquivo certo.

**Comprima toda foto antes de publicar.** Arquivos menores carregam mais rápido em conexões lentas. O Ontario recomenda qualidade JPEG de pelo menos 84% ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

**Reserve o espaço da imagem.** Declare `width` e `height` ou `aspect-ratio` para evitar saltos de layout. Use `loading="lazy"` em imagens fora da primeira dobra e `.tr-skeleton` enquanto carregam. O Trama usa as proporções 1:1, 4:3, 3:2, 16:9 e 2:1, um subconjunto das proporções do Ontario ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

**Inclua perfil de cor e teste em aparelhos reais.** Uma imagem bonita na ferramenta de design pode aparecer pixelada, esticada ou comprimida em outros dispositivos ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/images)).

**Prepare imagens para o tema escuro.** Evite ilustrações com fundo branco embutido. Use SVG com `currentColor` e tokens, ou forneça uma versão escura com `<picture>` e `prefers-color-scheme`. Veja Modo escuro.

### Considerações por plataforma

#### Web desktop

Limite imagens de conteúdo à largura da coluna de texto. Banners largos ficam reservados a páginas de entrada; páginas internas e de artigo dispensam banner ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)).

#### Web móvel

Envie arquivos proporcionais à largura da classe Compacta, nunca a versão de desktop reduzida por CSS. Verifique se detalhes importantes continuam visíveis em telas pequenas ([Ontario](https://designsystem.ontario.ca/components/detail/images.html)). Imagens de documentos devem poder ser ampliadas com o gesto de pinça.

#### Tablets e dobráveis

A mesma imagem aparece em larguras muito diferentes quando o dobrável abre ou fecha. Use `srcset` para que o navegador troque o arquivo e recorte com `object-fit` mantendo o assunto ao centro. A Samsung pede para evitar elementos interativos perto da dobra ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)); pelo mesmo motivo, o Trama evita deixar o assunto principal de uma imagem sobre ela.

### Recursos

#### Relacionados

- Imagem
- Ilustração
- Iconografia
- Acessibilidade
- Inclusão
- Visualização de dados
- Modo escuro

#### Referências

- [Princípios de UX writing](https://www.gov.br/ds/padroes/writing/principios-writing) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Ilustração](https://www.gov.br/ds/fundamentos-visuais/ilustracao) gov.br DS
- [Superfície](https://www.gov.br/ds/fundamentos-visuais/superficie) gov.br DS
- [Images](https://developer.apple.com/design/human-interface-guidelines/images) Apple HIG
- [Images](https://design-system.service.gov.uk/styles/images/) GOV.UK Design System
- [Images and photography](https://designsystem.ontario.ca/components/detail/images.html) Ontario Design System
- [Tilgængelig grafik](https://designsystem.dk/styleguide/datavisualisering-infografik/tilgaengelig-grafik/) Det Fælles Designsystem
- [Inclusivity](https://hds.hel.fi/foundation/guidelines/inclusivity) Helsinki Design System
- [Screen reader](https://developer.samsung.com/one-ui/accessibility/screen-reader.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                                                                                       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Fixa o texto alternativo em até 125 caracteres e duas frases, acrescenta regras de legenda, descrição de contexto, vídeo e áudio, critério entre foto e ilustração e overlay de legibilidade, move a ilustração para página própria e registra a divergência sobre fotos de clima e endosso. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                                                                                |

## Inclusão

Produtos inclusivos tratam as pessoas com respeito, representam a diversidade humana e evitam suposições sobre quem está do outro lado da tela.

Inclusão começa antes do primeiro rascunho. Cada pessoa combina características como idade, gênero e identidade de gênero, raça e etnia, sexualidade, atributos físicos e cognitivos, deficiências permanentes, temporárias ou situacionais, idioma e cultura, religião, escolaridade e contexto socioeconômico ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). Um produto feito com o Trama precisa funcionar para todas essas combinações. Um produto apenas inofensivo ainda pode excluir: procurar conteúdo ofensivo é necessário e insuficiente ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)).

O Padrão Digital de Governo define linguagem inclusiva como falar e escrever com palavras que demonstrem respeito a todas as pessoas, sem privilegiar umas em detrimento de outras. A proposta é usar a riqueza que o português já tem, sem provocar modificações no idioma ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). O Trama adota essa abordagem em todos os textos de interface.

Esta página trata de linguagem, representação e coleta de dados pessoais. Os requisitos técnicos para pessoas com deficiência estão em Acessibilidade; as regras gerais de texto, em Escrita e conteúdo.

### Boas práticas

#### Processo e equipe

**Forme equipes multidisciplinares e reconheça os limites delas.** A composição do time molda as decisões. Quando a equipe é pouco diversa, compense testando com um grupo de participantes mais diverso ([HDS](https://hds.hel.fi/foundation/guidelines/inclusivity)).

**Aprenda como o seu público se comunica.** Aproxime-se das pessoas que usam o produto, entenda como elas falam e valide os textos com elas; atualize os textos à medida que a linguagem muda ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Recrute participantes de origens variadas, incluindo pessoas com deficiência ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)).

**Projete para quem tem conexão lenta, aparelho antigo ou só usa celular.** O Ontario lista essas pessoas, ao lado de quem usa tecnologia assistiva e de quem tem dificuldade com o idioma, como público de todo serviço ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)).

#### Linguagem inclusiva em português

**Fale diretamente com a pessoa, no singular.** Use "você" e evite chamar alguém de "o usuário" ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). Escrever para uma pessoa no singular traz proximidade ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Reserve "nós" para a organização e use com moderação.

**Use os recursos do português para evitar o masculino genérico.** O gov.br aponta que o masculino plural, como "os usuários", exclui outros grupos, e propõe quatro recursos ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)):

| Recurso                         | Evite                                           | Prefira                                      |
|---------------------------------|-------------------------------------------------|----------------------------------------------|
| Substantivos coletivos          | Os alunos matriculados devem concluir o curso.  | A turma matriculada deve concluir o curso.   |
| Ocultar artigos e pronomes      | Adicione os participantes para criar uma turma. | Adicione participantes para criar uma turma. |
| A palavra "pessoas"             | Tenha 10 usuários na sua rede.                  | Tenha 10 pessoas na sua rede.                |
| Palavras comuns de dois gêneros | Você foi fantástico nesse desafio.              | Você foi fenomenal nesse desafio.            |
| Saudações sem gênero            | Bem-vindo ao sistema.                           | Boas-vindas ao sistema.                      |
| Reescrita com "quem"            | Os usuários cadastrados podem editar.           | Quem tem cadastro pode editar.               |

**Use "(a)" só quando não houver forma neutra.** Se o termo precisar marcar gênero, use a forma que abrange feminino e masculino segundo a norma culta, como "dono(a) de negócio" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Não use "@", "x" ou "e" como desinência neutra, porque o Trama segue a proposta de não modificar o idioma.

> **Divergência entre referências** A Apple recomenda reescrever a frase com um substantivo neutro, o que também facilita a localização ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). O gov.br aceita a forma com parênteses, "dono(a)", quando o termo de gênero é necessário ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Em linguagem para o público brasileiro, o gov.br pesa mais. O Trama decide: primeiro reescreva com recursos neutros, nos quais as duas referências concordam; use "(a)" só quando a reescrita não for possível. A versão 1.0 proibia "(a)" em qualquer caso; a regra mudou.

**Troque expressões coloquiais, regionais e gírias por linguagem simples.** Escreva em português neutro, sem expressões típicas de uma região e sem abreviações populares, como "wpp" ou "valeu" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Expressões coloquiais são difíceis de traduzir e podem ter origem excludente ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)).

**Não use palavras de cunho racista ou ofensivo.** O gov.br lista "denegrir", "judiar", "blacklist" e "whitelist" entre as palavras a evitar, junto com palavrões e gírias de grupos restritos ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Use "difamar", "maltratar", "lista de bloqueio" e "lista de permissão".

**Use humor com cautela.** Humor é subjetivo, se perde na tradução e cansa quando se repete ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion), [gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Nunca use humor em mensagens de erro.

#### Deficiência

**Mencione a deficiência só quando for relevante.** Se precisar mencionar, enfatize a pessoa e o que ela faz, não a incapacidade ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Descreva realizações e objetivos antes de citar uma deficiência ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)).

**Não use "sofre de", "vítima" ou "deficiente".** Esses termos geram dúvida sobre o tipo de deficiência e podem soar pejorativos ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Use "pessoa com deficiência", "pessoa surda", "pessoa cega" e "pessoa com baixa visão", e pergunte como a pessoa ou a comunidade se identifica ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)).

**Faça** Descreva a pessoa e o que ela faz.

**Não faça** Trate a deficiência como sofrimento ou incapacidade.

**Não use uma deficiência para expressar algo negativo.** Evite "cego" no sentido de "ignorante" ou "surdo" no sentido de "indiferente" ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)).

#### Representação

**Mostre a diversidade brasileira com intenção.** Retrate pessoas de diferentes origens, corpos, idades e capacidades e evite estereótipos de ocupação, como só médicos homens e só enfermeiras mulheres ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). O gov.br pede atenção à pluralidade racial e cultural do Brasil, usando como referência as categorias de cor ou raça do IBGE (brancos, pardos, pretos, amarelos e indígenas), sem cair em estereótipos ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Mostrar só um tipo de pessoa reforça estereótipos ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Veja Ilustração.

**Prefira figuras sem gênero em ícones e avatares genéricos.** Para representar "uma pessoa", use uma silhueta neutra e deixe cada pessoa personalizar o próprio avatar ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). O avatar padrão do Trama mostra iniciais sobre `--t-brand-subtle`.

**Não assuma um modelo de família, renda ou experiência.** Uma tela de "família" que presume duas pessoas adultas de gêneros diferentes e filhos biológicos exclui as outras famílias. Perguntas de segurança como "marca do seu primeiro carro" presumem experiências que nem todos tiveram ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)).

#### Nomes

**Peça o nome só se precisar dele para prestar o serviço, num único campo.** Nem todo nome cabe no formato nome e sobrenome; um campo "Nome completo" acomoda a maior variedade ([GOV.UK](https://design-system.service.gov.uk/patterns/names/)). Aceite acentos, apóstrofos e hífens, desligue a correção ortográfica (`spellcheck="false"`) e use `autocomplete="name"` ([GOV.UK](https://design-system.service.gov.uk/patterns/names/)).

**Pergunte e respeite o nome social.** Deixe claro se você precisa do nome usado no dia a dia ou do nome de um documento oficial, use o nome social em toda comunicação e permita alterá-lo a qualquer momento ([GOV.UK](https://design-system.service.gov.uk/patterns/names/)). Não peça pronome de tratamento, como "Sr." ou "Sra.", que obriga a revelar gênero e estado civil ([GOV.UK](https://design-system.service.gov.uk/patterns/names/)).

#### Gênero e dados sensíveis

**Não pergunte o que não precisa.** Se o dado não é necessário, a pergunta sai do formulário. Todo dado coletado precisa de uma finalidade clara e informada; explique por que ele é pedido, sobretudo dados pessoais e sensíveis ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario), [HDS](https://hds.hel.fi/foundation/guidelines/inclusivity)).

**Quando o gênero for necessário, ofereça opções inclusivas.** Inclua "Não binário", "Prefiro descrever" com campo livre e "Prefiro não informar" ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). Se não houver um conjunto inclusivo de opções, use texto livre ([HDS](https://hds.hel.fi/foundation/guidelines/inclusivity)). Se precisar de cor ou raça, use as categorias do IBGE, com "Prefiro não informar".

**Separe perguntas de diversidade do fluxo principal.** O GOV.UK coloca as perguntas de igualdade entre a revisão das respostas e a confirmação, deixa claro que são opcionais e que não afetam o pedido, e oferece "Prefiro não informar" em cada pergunta ([GOV.UK](https://design-system.service.gov.uk/patterns/equality-information/)).

> **Importante** Dados sobre origem racial ou étnica, convicção religiosa, saúde e vida sexual são dados pessoais sensíveis na Lei nº 13.709/2018 (LGPD). Consulte a pessoa encarregada de dados antes de coletá-los. Veja Privacidade e Legislação e normas.

#### Cor e cultura

**Confira o significado das cores em cada mercado.** Em alguns lugares o branco está associado ao luto; em outros, à paz ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). Os tokens semânticos do Trama, como `--t-danger` e `--t-success`, sempre vêm acompanhados de texto ou ícone.

### Considerações por plataforma

#### Web desktop

Nenhuma consideração adicional para Web desktop.

#### Web móvel

Muitas pessoas acessam serviços só pelo celular, às vezes com plano de dados limitado. Mantenha páginas leves, evite imagens decorativas pesadas e garanta que nenhuma tarefa exija desktop ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)).

#### Tablets e dobráveis

Tablets costumam ser compartilhados em casa ou no trabalho. Não presuma que a pessoa diante da tela é a dona da conta: mostre de quem é a sessão e facilite a troca de conta.

### Recursos

#### Relacionados

- Acessibilidade
- Escrita e conteúdo
- Ilustração
- Imagens
- Privacidade
- Internacionalização e direita para esquerda
- Entrada de dados

#### Referências

- [Princípios de UX writing](https://www.gov.br/ds/padroes/writing/principios-writing) gov.br DS
- [Ilustração](https://www.gov.br/ds/fundamentos-visuais/ilustracao) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) Apple HIG
- [Names](https://design-system.service.gov.uk/patterns/names/) GOV.UK Design System
- [Equality information](https://design-system.service.gov.uk/patterns/equality-information/) GOV.UK Design System
- [Images](https://design-system.service.gov.uk/styles/images/) GOV.UK Design System
- [Accessibility strategy](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) GOV.UK Design System
- [Inclusivity](https://hds.hel.fi/foundation/guidelines/inclusivity) Helsinki Design System
- [Ontario Government design principles](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html) Ontario Design System

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta os recursos do português para linguagem inclusiva, regras sobre deficiência sem "sofre de", palavras a evitar, diversidade com as categorias do IBGE e LGPD, e passa a aceitar "(a)" quando não houver forma neutra. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                   |

## Layout e grid

Um layout consistente, que se adapta ao espaço disponível em cada janela, ajuda as pessoas a entender e usar o conteúdo em qualquer tela.

O layout do Trama parte do espaço real que a página recebe. Uma janela de navegador estreita num monitor grande, um celular deitado e um dobrável aberto podem ter a mesma largura e, portanto, o mesmo layout. A Apple orienta decidir o layout pelo espaço disponível, porque o tipo de dispositivo e a orientação não dizem quanto espaço existe ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)). O gov.br faz o mesmo alerta: uma resolução não indica qual aparelho a pessoa usa, e a interface precisa funcionar em qualquer um ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

O Trama define cinco classes de janela. As três primeiras (Compacta, Média e Expandida) e as proporções de painel vêm das diretrizes de telas grandes e dobráveis do One UI ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Grande e Extragrande atendem monitores de desktop.

### Classes de janela

| Classe      | Largura (px CSS) | Colunas | Margem mínima | Gutter | Painéis  | Navegação principal                               |
|-------------|------------------|---------|---------------|--------|----------|---------------------------------------------------|
| Compacta    | \< 600           | 4       | 16            | 16     | 1        | Barra inferior (`.tr-bottom-nav`) ou drawer modal |
| Média       | 600 a 839        | 8       | 24            | 16     | 1 ou 2   | Rail (`.tr-rail`) ou drawer modal                 |
| Expandida   | 840 a 1199       | 12      | 32            | 24     | 2        | Rail ou navegação lateral (`.tr-nav`)             |
| Grande      | 1200 a 1599      | 12      | 40            | 24     | 2, até 3 | Navegação lateral fixa                            |
| Extragrande | ≥ 1600           | 12      | 48            | 24     | 2, até 3 | Navegação lateral fixa                            |

Margens e gutters usam tokens de espaçamento: 16 é `--sp-400`, 24 é `--sp-600`, 32 é `--sp-800`, 40 é `--sp-1000` e 48 é `--sp-1200`. A progressão de navegação segue o One UI: barra inferior em telas pequenas, rail em telas médias e drawer visível em telas grandes ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

> **Divergência entre referências** O gov.br usa cinco pontos de quebra (0, 576, 992, 1280 e 1600px), margem de 8px no celular em retrato e 40px nas demais grids, e gutters de 16, 24 e 40px ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). O Trama mantém as suas classes, que acompanham as diretrizes de dobráveis do One UI. Mantém também a margem de 16px na Compacta: o One UI bloqueia toques nas margens da tela para evitar acionamentos acidentais ([One UI](https://developer.samsung.com/one-ui/layout/grid.html)), e 8px deixaria controles perto demais da borda física. As duas referências concordam em 4, 8 e 12 colunas.

### Grid

O grid tem colunas, gutters e margens, e as colunas se agrupam em regiões. O conteúdo mais importante ocupa as regiões maiores ([Fluent](https://fluent2.microsoft.design/layout)). O Trama usa 12 colunas a partir da classe Expandida e as reduz para 8 e 4 nas classes menores, como o DKFDS ([DKFDS](https://designsystem.dk/styleguide/grid/)) e o gov.br ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). Com 12 colunas, você combina metades, terços, quartos e sextos.

#### Largura fixa e largura fluida

O grid tem dois comportamentos de largura. Na **largura fluida**, margens e gutters são fixos e as colunas crescem até ocupar toda a janela. Na **largura fixa**, colunas e gutters têm uma largura máxima, o conteúdo fica centralizado e as margens crescem com a janela, sem nunca ficar abaixo da margem mínima da classe ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

| Comportamento | Use em                                                                                                       | Classes                                                                          |
|---------------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Fluida        | Sistemas, ferramentas de trabalho, painéis, tabelas e telas de lista e detalhe, que aproveitam todo o espaço | Todas. Na Compacta, sempre fluida                                                |
| Fixa          | Conteúdo informativo, portais, páginas de serviço e textos longos, em que a leitura não pode se distorcer    | A partir da Expandida. Área de conteúdo de até 1200px, o início da classe Grande |

A divisão segue o gov.br, que recomenda a grid fluida para sistemas e a fixa para portais e conteúdos informativos, e evita a fixa no celular ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

``` code
.pagina {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  column-gap: var(--sp-400);
  padding-inline: var(--sp-400);           /* margem mínima */
}
@media (min-width: 600px)  { .pagina { grid-template-columns: repeat(8, 1fr); padding-inline: var(--sp-600); } }
@media (min-width: 840px)  { .pagina { grid-template-columns: repeat(12, 1fr); column-gap: var(--sp-600); padding-inline: var(--sp-800); } }
@media (min-width: 1200px) { .pagina { padding-inline: var(--sp-1000); } }
@media (min-width: 1600px) { .pagina { padding-inline: var(--sp-1200); } }

/* Largura fixa: centraliza e limita a área de conteúdo */
.pagina--fixa {
  box-sizing: content-box;   /* a margem mínima fica fora dos 1200px */
  max-width: 1200px;
  margin-inline: auto;
}
```

#### Elementos adaptativos e estáveis

Defina como cada componente responde ao grid. Um elemento **adaptativo** tem a largura presa às colunas e cresce ou encolhe com elas. Um elemento **estável** só se alinha ao grid: mantém a largura e, se não couber, passa para a linha seguinte ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). O mesmo componente pode mudar de comportamento entre classes.

**Documente a largura e a altura de cada componente.** Para cada um, diga se a largura acompanha as colunas, o conteúdo ou nenhum dos dois, e faça o mesmo com a altura. Um card pode ter largura adaptativa ao grid e altura adaptativa ao conteúdo.

#### Sangria

**Deixe só o fundo sangrar.** Por padrão, nada ultrapassa as margens. Um elemento pode ocupar a margem, como uma faixa de fundo ou uma imagem de capa, mas o conteúdo informativo dentro dele continua alinhado às colunas ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). Texto, controles e links nunca encostam na borda da janela. Elementos flutuantes não seguem o grid.

#### Objetos temporários

Regiões que aparecem e somem com uma interação se dividem em dois tipos. As **flutuantes** ficam por cima e não mexem no grid: menus, popovers, drawers modais. As **persistentes** empurram o conteúdo e comprimem o grid quando aparecem: a navegação lateral fixa, um painel de detalhes que abre ao lado da lista ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

**Use objetos persistentes quando a pessoa trabalha com eles abertos.** Um filtro consultado o tempo todo pode empurrar a tabela. Um menu de ações usado por um instante flutua. Em grid fixa, abra objetos temporários junto da área de conteúdo, e não no canto de uma margem larga ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

### Painéis

Em telas largas, mostre a hierarquia do app lado a lado em vez de esticar uma coluna única. Apps esticados são difíceis de ler e desperdiçam espaço ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). O componente `.tr-panes` aplica as proporções do Trama.

| Situação                        | Proporção                       | Classe                            |
|---------------------------------|---------------------------------|-----------------------------------|
| Largura de 600 a 959            | 42:58                           | `.tr-panes` com colunas ajustadas |
| Largura ≥ 960                   | 38:62                           | `.tr-panes` (padrão do kit)       |
| Dobrável aberto                 | 50:50                           | `.tr-panes--50`                   |
| Três painéis (Grande em diante) | Navegação fixa, lista e detalhe | `.tr-panes--3`                    |

### Boas práticas

**Comece pela coluna única.** Projete primeiro para a classe Compacta e acrescente colunas conforme o espaço cresce ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)).

**Ordene o conteúdo por importância.** Coloque o mais importante no topo e no lado inicial ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)).

**Alinhe formulários e fluxos ao início, em uma coluna.** Rótulos, campos, texto e botão primário alinhados criam um único movimento vertical do olhar ([DKFDS](https://designsystem.dk/styleguide/layout/)).

**Limite a largura de leitura.** Blocos de texto corrido não passam de cerca de 75 caracteres por linha (`max-width: 75ch`), mesmo em grid fluida ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)).

**Mantenha a funcionalidade igual em todas as classes.** Varie apenas a quantidade de recursos visíveis ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)).

**Revise a navegação em cada classe.** Telas menores pedem áreas de toque e textos maiores, e a navegação muda de forma entre classes. O gov.br pede validar os componentes de navegação em cada ponto de quebra ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)).

**Escolha a técnica responsiva certa.** Reposicione, redimensione, reorganize em mais colunas, mostre ou oculte informações secundárias e, em telas grandes, rearquitete em lista e detalhe ([Fluent](https://fluent2.microsoft.design/layout)).

**Respeite as áreas seguras.** Em telas com recortes ou cantos arredondados, use `env(safe-area-inset-*)` no preenchimento de barras fixas ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)).

**Teste os extremos.** Teste o menor e o maior layout, com textos maiores e outros idiomas ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)), e valide a interface em cada classe ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). O layout precisa funcionar com 320px CSS de largura, sem rolagem horizontal (WCAG 2.2, 1.4.10).

### Estrutura da página

Toda página do Trama tem cabeçalho, conteúdo principal e rodapé, e começa com links para pular ao conteúdo. O modelo de página do GOV.UK inclui o link de pular, o cabeçalho e o rodapé, com o conteúdo num contêiner de largura limitada dentro de `<main>` ([GOV.UK](https://design-system.service.gov.uk/styles/page-template/)).

``` code
<nav class="tr-skiplinks" aria-label="Links de pular">…</nav>
<header class="tr-header">…</header>
<div class="pagina">
  <nav aria-label="Você está aqui" class="tr-breadcrumb">…</nav>
  <main id="conteudo">…</main>
</div>
<div class="tr-inverse"><footer class="tr-footer">…</footer></div>
```

### Considerações por plataforma

#### Web desktop

Monitores largos convidam a esticar o conteúdo. Em portais, use a largura fixa; em sistemas, use a fluida com painéis e limite blocos de texto pela largura de leitura. Janelas de navegador são redimensionadas a qualquer momento: o layout muda de classe sem perder o que a pessoa estava fazendo. Veja Projetar para web desktop.

#### Web móvel

Use uma coluna fluida, margem de `--sp-400` e navegação na barra inferior. O One UI separa a parte superior da tela, para visualizar conteúdo, da área de interação abaixo, onde ficam os componentes acionáveis ([One UI](https://developer.samsung.com/one-ui/layout/basic.html)). Na Compacta, botões de ação de formulário passam a adaptativos. Veja Projetar para web móvel.

#### Tablets e dobráveis

A partir de 600px de largura, use um layout de tela grande ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)). Num dobrável aberto, prefira dois painéis em 50:50 e use um rail em vez da barra inferior. Quando a pessoa abre ou fecha o aparelho, preserve a posição de rolagem, o texto digitado e o foco, e não coloque elementos interativos sobre a dobra ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Lembre que a mesma largura pode vir de um tablet girado ou de uma janela redimensionada ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/grid)). Veja Postura e dobra.

### Recursos

#### Relacionados

- Espaçamento
- Densidade
- Painéis e split view
- Barra de navegação e rail
- Navegação lateral
- Projetar para tablets e dobráveis
- Postura e dobra

#### Referências

- [Grid](https://www.gov.br/ds/fundamentos-visuais/grid) gov.br DS
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) Apple HIG
- [Layout](https://fluent2.microsoft.design/layout) Fluent 2
- [Layout](https://design-system.service.gov.uk/styles/layout/) GOV.UK Design System
- [Page template](https://design-system.service.gov.uk/styles/page-template/) GOV.UK Design System
- [Layout](https://designsystem.dk/styleguide/layout/) Det Fælles Designsystem
- [Grid og baseline grid](https://designsystem.dk/styleguide/grid/) Det Fælles Designsystem
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Layout design for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI
- [Basic layout](https://developer.samsung.com/one-ui/layout/basic.html) Samsung One UI
- [Grid system](https://developer.samsung.com/one-ui/layout/grid.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta largura fixa e fluida, elementos adaptativos e estáveis, sangria, objetos temporários flutuantes e persistentes, e registra a divergência de pontos de quebra e margens. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                       |

## Espaçamento

Uma escala única de espaçamento, baseada em 4px, mostra o que está relacionado, dá ritmo à página e mantém os componentes consistentes entre si.

Espaço é a ferramenta de agrupamento mais barata da interface. Elementos próximos parecem relacionados, e mais espaço enfraquece essa relação a ponto de separar grupos sem precisar de divisores ([Fluent](https://fluent2.microsoft.design/layout)). O gov.br descreve o espaço em branco da mesma forma: ele cria hierarquia, aproxima o que é semelhante, afasta o que é diferente e dá ao olhar pontos de descanso durante a leitura ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)).

O Trama define 14 tokens de espaçamento, todos múltiplos ou frações de 4px. Use-os em margens, preenchimentos e `gap`. Por padrão, todo componente começa com espaço zero e recebe só os tokens que a sua especificação define.

### Escala

| Token       | Valor | Faixa                                               | Uso típico                                                         |
|-------------|-------|-----------------------------------------------------|--------------------------------------------------------------------|
| `--sp-0`    | 0     | Padrão                                              | Ponto de partida de todo componente                                |
| `--sp-50`   | 2px   | Ajuste fino, só texto e ícone                       | Entre título e texto de uma mensagem, entre rótulo e valor curto   |
| `--sp-150`  | 6px   |                                                     | Compensação óptica de ícones, preenchimento de badge de contagem   |
| `--sp-100`  | 4px   | Dentro do componente e entre elementos relacionados | Rótulo e campo, ícone e badge, área mínima de leitura              |
| `--sp-200`  | 8px   |                                                     | Ícone e rótulo do botão, botões de um grupo                        |
| `--sp-300`  | 12px  |                                                     | Preenchimento horizontal de campos, padding vertical de mensagens  |
| `--sp-400`  | 16px  |                                                     | Preenchimento de cards e botões, margem da Compacta, gutter padrão |
| `--sp-500`  | 20px  | Entre grupos                                        | Recuo de listas                                                    |
| `--sp-600`  | 24px  |                                                     | Preenchimento de diálogos, distância entre campos, margem da Média |
| `--sp-800`  | 32px  |                                                     | Entre blocos de conteúdo, margem da Expandida                      |
| `--sp-1000` | 40px  | Entre seções                                        | Seções de uma página, grupos de formulário, margem da Grande       |
| `--sp-1200` | 48px  |                                                     | Seções principais, margem da Extragrande                           |
| `--sp-1600` | 64px  |                                                     | Regiões de páginas longas                                          |
| `--sp-2000` | 80px  |                                                     | Respiro de páginas de entrada e estados vazios grandes             |

**Use `--sp-50` e `--sp-150` só em ajustes internos de texto e ícone.** Os dois valores saem da grade de 4px e servem para alinhar opticamente um ícone a uma linha de texto ou aproximar duas linhas de texto do mesmo bloco. Nunca os use entre componentes. O gov.br tem a mesma restrição para a sua escala de ajuste, reservada a textos e ícones ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)).

> **Divergência entre referências** O gov.br usa uma escala de layout em passos de 8px e reserva todos os valores intermediários de 4px (4, 12, 20, 28) a textos e ícones ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)). O Fluent usa uma rampa de base 4px para todos os elementos ([Fluent](https://fluent2.microsoft.design/layout)), o Blueprint multiplica uma unidade base de 4px para chegar às medidas dos componentes ([Blueprint](https://blueprintjs.com/docs/)) e o DKFDS usa uma unidade de 8px com metades ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/hjaelpeklasser/)). Pela convergência, o Trama mantém 4px como base para qualquer elemento e restringe só os valores de 2px e 6px.

#### Espaços de formulário

Formulários têm tokens próprios, que apontam para a escala e mantêm a mesma distância em todo o produto.

| Token             | Valor              | Onde                                       |
|-------------------|--------------------|--------------------------------------------|
| `--f-gap-field`   | `--sp-600` (24px)  | Entre um campo e o próximo                 |
| `--f-gap-group`   | `--sp-1000` (40px) | Entre grupos ou fieldsets                  |
| `--f-gap-title`   | `--sp-400` (16px)  | Entre o título do grupo e o primeiro campo |
| `--f-gap-actions` | `--sp-800` (32px)  | Entre o último campo e os botões de ação   |

### Box model

Todo elemento é uma caixa com conteúdo, preenchimento (`padding`), borda e margem. O preenchimento é o espaço **interno**, entre o conteúdo e a borda; a margem é o espaço **externo**, que separa o elemento dos vizinhos e forma a sua área de segurança ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)).

**Use `box-sizing: border-box` em todo componente.** Assim, largura e altura incluem preenchimento e borda, e um botão de 40px tem 40px com a borda. O kit aplica a regra dentro de `.tr-demo`, e o gov.br adota o mesmo comportamento ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)).

**Configure o traço interno na ferramenta de design.** A borda ocupa espaço no navegador, mas a maioria das ferramentas de design a ignora ao medir distâncias. Desenhe bordas com traço interno, que reproduz o `border-box`, e lembre que a distância medida pela ferramenta pode não contar a borda ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)).

**Especifique a sangria de cada componente.** Por padrão, nada invade o preenchimento de outro elemento. Quando um componente precisa disso, como a imagem do card (`.tr-card__media`), que encosta nas bordas do card, a documentação do componente diz que há sangria e o componente pai precisa permitir ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)).

### Boas práticas

**Use a proximidade para mostrar relação.** O espaço entre um rótulo e seu campo (`--sp-100`) é menor que o espaço entre dois campos (`--f-gap-field`), que é menor que o espaço entre dois grupos (`--f-gap-group`). Dois degraus de distância na escala é um bom mínimo entre níveis. Agrupe itens relacionados com espaço vazio, contêineres ou linhas separadoras ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)).

**Não some margens de segurança vizinhas.** Quando dois elementos ficam lado a lado ou um sobre o outro, vale a maior das duas margens; se forem iguais, vale uma só ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)). Em fluxo de bloco, o colapso de margens verticais do CSS já faz isso. Em `flex` e `grid`, use `gap` com o maior valor e tire as margens dos filhos.

**Use `gap` no contêiner em vez de margem nos filhos.** `gap` distribui o espaço sem sobras no primeiro ou no último item. Os utilitários do kit (`.tr-stack` e `.tr-row`) usam `--sp-300`.

**Prefira espaço a linhas.** Antes de acrescentar um divisor, tente separar os grupos com mais espaço ([DKFDS](https://designsystem.dk/styleguide/borders/)).

**Prefira regras nos filhos a dimensões fixas no pai.** Um componente com vários elementos internos não tem largura nem altura fixas: as medidas vêm do conteúdo e do preenchimento. Quando uma medida fixa for necessária, defina também mínimo e máximo, e use valores da escala. Se o componente se apoia no grid, diga quantas colunas ocupa em cada classe de janela ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)).

**Alinhe pelo início por padrão.** Dentro de um componente, o conteúdo começa no topo e no início da linha. Centralize só quando a especificação pedir. O gov.br usa o mesmo padrão de alinhamento ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)).

**Use propriedades lógicas.** Escreva `padding-inline-start` e `margin-block-end` em vez de `padding-left` e `margin-bottom`. O espaçamento se espelha sozinho em idiomas da direita para a esquerda.

**Mantenha o ritmo vertical em múltiplos de 4px.** As alturas de linha da escala tipográfica e as alturas de controle (`--c-h-sm` 32, `--c-h-md` 40, `--c-h-lg` 48) são múltiplos de 4px. O espaço entre blocos de texto tem tokens próprios, descritos em Tipografia.

**Garanta alvos de toque com espaço suficiente.** Todo controle de toque tem área mínima de `--c-touch` (44px). A Apple considera o espaço entre controles tão importante quanto o tamanho e sugere cerca de 12 pontos em volta de elementos com contorno e 24 pontos em volta de elementos sem contorno ([HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)). A WCAG 2.2, 2.5.8, aceita alvos menores que 24px somente com espaçamento suficiente em volta. Veja Densidade.

**Faça** deixe rótulo, dica e campo próximos (`--sp-100`) e separe um campo do outro com mais espaço.

**Não faça** use o mesmo espaço entre todos os elementos. Fica impossível saber a qual campo cada rótulo pertence.

### Espaçamento dentro dos componentes

Os componentes do kit já aplicam a escala. Use estes valores como referência ao criar componentes novos. Os valores marcados mudam com a densidade.

| Componente                       | Preenchimento                                                            | Distância interna               |
|----------------------------------|--------------------------------------------------------------------------|---------------------------------|
| Botão (`.tr-btn`)                | Horizontal `--sp-400`; com densidade, `--d-pad-x`                        | Ícone e rótulo `--sp-200`       |
| Campo (`.tr-field`, `.tr-input`) | Horizontal `--sp-300`                                                    | Rótulo, dica e campo `--sp-100` |
| Card (`.tr-card`)                | `--sp-400`                                                               | `--sp-300`                      |
| Mensagem (`.tr-msg`)             | `--sp-300` vertical, `--sp-400` horizontal                               | `--sp-300`                      |
| Diálogo (`.tr-dialog`)           | `--sp-600`                                                               | `--sp-400`                      |
| Menu (`.tr-menu`)                | `--sp-100`                                                               | Item com `--sp-300` horizontal  |
| Célula de tabela (`.tr-table`)   | Vertical `--sp-300` (com densidade, `--d-cell-y`), horizontal `--sp-400` | Não se aplica                   |

### Considerações por plataforma

#### Web desktop

Telas grandes acomodam densidade maior em ferramentas de trabalho, como tabelas e painéis. Reduza a densidade com `data-density="alta"` na região e mantenha os espaços entre seções. Não reduza o espaço entre grupos para caber mais: isso apaga a estrutura da página.

#### Web móvel

Os tokens são fixos. A adaptação ao tamanho da tela acontece na escolha do token: margens de página caem para `--sp-400` e distâncias entre seções podem descer um degrau. O GOV.UK formaliza essa ideia com uma escala responsiva, cujos valores maiores encolhem abaixo de 640px ([GOV.UK](https://design-system.service.gov.uk/styles/spacing/)). Nunca reduza a área de toque abaixo de `--c-touch`.

#### Tablets e dobráveis

Use as margens e gutters da classe de janela ativa (veja Layout e grid). Entre painéis, use um divisor de `--stroke-thin` e preenchimento de `--sp-400` em cada painel, como o `.tr-panes` do kit. Com toque e caneta, mantenha o espaçamento entre alvos do celular.

### Recursos

#### Relacionados

- Layout e grid
- Densidade
- Tipografia
- Formas e bordas
- Tokens de design
- Toque e gestos

#### Referências

- [Espaçamento](https://www.gov.br/ds/fundamentos-visuais/espacamento) gov.br DS
- [Layout](https://fluent2.microsoft.design/layout) Fluent 2
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) Apple HIG
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) Apple HIG
- [Design tokens](https://blueprintjs.com/docs/) Blueprint
- [Spacing](https://design-system.service.gov.uk/styles/spacing/) GOV.UK Design System
- [Hjælpeklasser](https://designsystem.dk/kom-i-gang/implementering-kode/hjaelpeklasser/) Det Fælles Designsystem
- [Hjørner, streger, skygger](https://designsystem.dk/styleguide/borders/) Det Fælles Designsystem

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Restringe `--sp-50` e `--sp-150` a texto e ícone, acrescenta box model, traço interno, sangria, otimização de margens, tokens de formulário e densidade. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                            |

## Materiais

Materiais definem como uma superfície se comporta em relação ao que está atrás dela: se bloqueia, se deixa transparecer, se escurece o fundo ou se garante a leitura sobre uma imagem.

Um material é um efeito visual que cria profundidade, camadas e hierarquia entre o primeiro plano e o fundo ([HIG](https://developer.apple.com/design/human-interface-guidelines/materials)). O Trama define três materiais, **sólido**, **translúcido** e **véu**, e duas camadas de apoio: a **camada de legibilidade**, que escurece uma imagem sob texto, e o **bloqueio de região**, que cobre uma área enquanto ela carrega.

O conjunto corresponde aos materiais do Fluent: sólido, o mais comum; acrílico, semitransparente, para superfícies transitórias; e smoke, um preto translúcido que faz a interface de baixo recuar ([Fluent](https://fluent2.microsoft.design/material)). Corresponde também aos dois usos de overlay do gov.br: foco, para destacar um elemento e inibir a interação com o resto, e legibilidade, para dar contraste a texto sobre imagem ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)).

| Material               | Tokens                                                           | Aplique em                                                   |
|------------------------|------------------------------------------------------------------|--------------------------------------------------------------|
| Sólido                 | `--t-bg`, `--t-surface-1`, `--t-surface-2`, `--t-surface-raised` | Páginas, painéis, cards, menus, diálogos, drawers, toasts    |
| Translúcido            | `--t-surface-raised` em `--o-xl`, com desfoque                   | Cabeçalho fixo e barra inferior fixa sobre conteúdo que rola |
| Véu                    | `--t-overlay`                                                    | Atrás de diálogos e drawers modais                           |
| Camada de legibilidade | `--t-overlay-text`                                               | Sob texto aplicado sobre fotos                               |
| Bloqueio de região     | `--t-bg` em `--o-lg` (`.tr-region-busy`)                         | Área que carrega e não aceita interação                      |

### Escala de opacidade

Toda transparência do Trama sai de uma escala de sete valores. A escala é a mesma do gov.br, que a usa em superfícies, estados e sombras ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)).

| Token      | Valor | Uso no Trama                                           |
|------------|-------|--------------------------------------------------------|
| `--o-none` | 0     | Totalmente transparente                                |
| `--o-xs`   | 0,16  | Hover no tema claro, camada da área de soltar ativa    |
| `--o-sm`   | 0,30  | Hover no tema escuro e em `.tr-inverse`                |
| `--o-md`   | 0,45  | Pressionado no tema claro                              |
| `--o-lg`   | 0,65  | Pressionado no tema escuro, bloqueio de região         |
| `--o-xl`   | 0,85  | Elemento sendo arrastado, base do material translúcido |
| `--o-full` | 1     | Opaco                                                  |

**Use só valores da escala.** Opacidades soltas tornam o contraste imprevisível. Os usos de estado estão em Estados de interação.

**Não crie matizes por sobreposição.** Uma camada colorida translúcida sobre outra cor gera um tom que não existe na paleta e distorce a identidade visual. O gov.br pede para evitar isso e, quando precisar, mexer só no brilho ou na saturação, reservando camadas coloridas a casos específicos, como o retorno a uma ação da pessoa ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)). No Trama, a única camada colorida é a da área de soltar ativa, que usa a marca em `--o-xs`.

### Sólido

O material sólido usa cor e elevação para separar regiões ([Fluent](https://fluent2.microsoft.design/material)). A hierarquia de superfícies sólidas é fixa: `--t-bg` é a base, `--t-surface-1` marca regiões secundárias, `--t-surface-2` serve a trilhos e fundos de controles, e `--t-surface-raised` recebe tudo o que fica acima da base.

**Use o material sólido como padrão.** Ele garante o contraste calculado em Cor sem depender do que está atrás. Prefira o sólido sempre que a superfície tiver muito texto.

**Não empilhe dois materiais no mesmo elemento.** Se um elemento filho precisa de mais destaque, leve-o para a sua própria superfície, com elevação maior ([Geist](https://vercel.com/geist/materials)).

### Translúcido

O material translúcido mantém um lembrete do conteúdo que passa por trás de uma barra fixa. Materiais mais finos ajudam a manter o contexto; materiais mais espessos dão mais contraste a texto e detalhes finos ([HIG](https://developer.apple.com/design/human-interface-guidelines/materials)). O Trama usa o translúcido só na camada de controles e navegação, nunca no conteúdo ([HIG](https://developer.apple.com/design/human-interface-guidelines/materials)).

**Use `--t-surface-raised` em `--o-xl` como base.** Com 85% de opacidade, o pior caso calculado sobre conteúdo preto, branco, azul-tinta, vermelho e amarelo deixa `--t-fg-1` com pelo menos 12,51:1 no claro e 9,07:1 no escuro, e `--t-fg-2` com pelo menos 6,77:1 e 6,22:1. `--t-fg-3` cai para 4,32:1 e 4,02:1 e fica proibido sobre o translúcido.

**Use o translúcido com parcimônia.** Aplique-o em, no máximo, uma barra superior e uma inferior por tela ([HIG](https://developer.apple.com/design/human-interface-guidelines/materials)).

**Ofereça um sólido como alternativa sempre.** O translúcido recai no sólido quando o navegador não suporta `backdrop-filter`, quando a pessoa pede menos transparência e quando o modo de cores forçadas está ativo.

``` code
.barra-fixa {
  background: var(--t-surface-raised);          /* sólido: padrão e alternativa */
  border-bottom: var(--stroke-thin) solid var(--t-border-subtle);
}
@supports (backdrop-filter: blur(1px)) {
  .barra-fixa--translucida {
    background: color-mix(in srgb, var(--t-surface-raised) calc(var(--o-xl) * 100%), transparent);
    backdrop-filter: blur(12px);
  }
}
@media (prefers-reduced-transparency: reduce), (forced-colors: active) {
  .barra-fixa--translucida { background: var(--t-surface-raised); backdrop-filter: none; }
}
```

> **Nota** O desfoque não tem token na versão 1.1; o valor do exemplo é ilustrativo. A opacidade da base agora vem de `--o-xl`. Teste o desempenho em celulares de entrada, porque o desfoque de fundo custa processamento ([Fluent](https://fluent2.microsoft.design/material)).

### Véu

O véu é uma camada escura sobre a página que destaca uma superfície modal e indica que o resto da interface está bloqueado. O One UI usa o escurecimento para concentrar a atenção no elemento do nível mais alto ([One UI](https://developer.samsung.com/one-ui/structure/visual-depth.html)).

**Use o véu só atrás de camadas modais.** Diálogos e drawers modais recebem o véu. Menus, popovers, toasts e drawers não modais ficam sem véu, porque a página continua utilizável ([One UI](https://developer.samsung.com/one-ui/structure/visual-depth.html)).

**Adapte o véu ao tema.** `--t-overlay` é rgba(15,18,21,.48) no claro e rgba(0,0,0,.64) no escuro, porque um véu leve quase não se percebe sobre fundo escuro. O gov.br usa preto puro em 0,45 ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)) e o DKFDS usa rgba(0, 0, 0, 0.4) ([DKFDS](https://designsystem.dk/styleguide/farver/)), valores próximos ao do Trama no claro.

**Faça o véu se comportar como a camada modal.** Torne o conteúdo atrás inerte (`inert` ou o elemento `<dialog>` aberto com `showModal()`) e devolva o foco ao controle de origem ao fechar. Em diálogos com dados digitados ou ações destrutivas, um clique no véu não fecha nada.

**Não desfoque a página atrás do véu e não empilhe véus.** Desfoque de página inteira pesa no desempenho, e a Apple recomenda evitar animações de desfoque quando a pessoa pede menos movimento ([HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)). Uma segunda camada modal escurece demais a página ([One UI](https://developer.samsung.com/one-ui/structure/visual-depth.html)).

### Camada de legibilidade

Texto sobre foto não tem contraste garantido. A camada de legibilidade é um gradiente vertical, transparente no topo e escuro na base, aplicado entre a imagem e o texto. O gov.br define o mesmo gradiente, de 180 graus, para esse uso ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)). No Trama, o token é `--t-overlay-text`, de transparente a preto opaco, e o texto sobre ele é branco.

**Meça o contraste no ponto onde o texto está.** Sobre uma imagem branca, o pior caso, o texto branco passa de 4,5:1 a partir de 54% da altura do gradiente e chega a 21:1 na base. Coloque o texto na metade inferior da área coberta. No `.tr-carousel__slide`, o preenchimento superior maior empurra a legenda para essa metade.

> **Divergência entre referências** O gradiente do gov.br termina em preto opaco ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)). Com ele, o texto branco sobre imagem branca passa de 4,5:1 a partir de 54% da altura, contra 75% no gradiente de 72% da versão 1.0. Pelo critério de acessibilidade, a opção do gov.br tem mais margem, e o Trama a adotou na versão 1.1.

### Bloqueio de região

**Cubra só a região que está carregando.** O resto da página continua utilizável. Marque a região com `aria-busy="true"` e anuncie o andamento com `role="status"`. Para bloquear a tela inteira, use um diálogo de carregamento na camada `--z-4` (veja Carregamento e espera).

### Considerações por plataforma

#### Web desktop

Diálogos ocupam uma parte pequena de telas grandes, e o véu cobre toda a janela, inclusive barras fixas do produto.

#### Web móvel

Prefira o sólido em barras fixas: o desfoque de fundo consome bateria e processamento. Folhas inferiores modais recebem o véu, que cobre também a área segura inferior.

#### Tablets e dobráveis

Em layouts de vários painéis, uma tarefa curta pode abrir num popover junto ao controle, sem véu ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html)). Quando um diálogo modal for necessário, o véu cobre todos os painéis. O bloqueio de região cobre só o painel que carrega.

### Recursos

#### Relacionados

- Elevação
- Estados de interação
- Modo escuro
- Cor
- Imagens
- Carregamento e espera
- Modalidade

#### Referências

- [Superfície](https://www.gov.br/ds/fundamentos-visuais/superficie) gov.br DS
- [Materials](https://developer.apple.com/design/human-interface-guidelines/materials) Apple HIG
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) Apple HIG
- [Material](https://fluent2.microsoft.design/material) Fluent 2
- [Visual depth](https://developer.samsung.com/one-ui/structure/visual-depth.html) Samsung One UI
- [Layout design for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/large_screen_layout.html) Samsung One UI
- [Materials](https://vercel.com/geist/materials) Geist
- [Farver](https://designsystem.dk/styleguide/farver/) Det Fælles Designsystem

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a escala de opacidade `--o-*`, a base do translúcido com contraste calculado, a camada de legibilidade sobre imagens, o bloqueio de região e a regra contra novos matizes. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                         |

## Movimento

O movimento do Trama explica mudanças de estado e de lugar, dá retorno imediato às ações e sai do caminho quando a pessoa prefere menos animação.

Animação no Trama tem função. Ela mostra de onde veio uma camada, para onde foi um item e que uma ação foi recebida. A Apple pede movimento com propósito e lembra que animação excessiva distrai e pode causar desconforto físico ([HIG](https://developer.apple.com/design/human-interface-guidelines/motion)). O gov.br pede movimentos que destaquem as relações entre elementos, a disponibilidade de uma ação e o seu resultado, e só quando aumentarem a compreensão ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

O sistema tem quatro durações e quatro curvas. Toda animação usa esses tokens, respeita `prefers-reduced-motion` e pode ser desligada por um controle do próprio produto.

### Durações

| Token        | Valor | Área          | Aplique em                                                                                           |
|--------------|-------|---------------|------------------------------------------------------------------------------------------------------|
| `--m-fast`   | 100ms | Micro         | Cor e borda em hover e pressionado, marcação de checkbox                                             |
| `--m-normal` | 200ms |               | Switch, acordeão, sombra de card, tooltips, menus e popovers, saída de diálogos                      |
| `--m-slow`   | 300ms |               | Entrada de diálogos, drawers, folhas inferiores e toasts                                             |
| `--m-slower` | 500ms | Média e macro | Transformações de contêiner grandes, como a passagem de lista para lista e detalhe. Teto do sistema. |

As áreas vêm do gov.br, que separa micro animações, sutis e ligadas a retorno de estado e de entrada de dados, médias, para elementos expansíveis, e macro, para elementos grandes e importantes, a usar com muita cautela ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)). A faixa do Trama vai de 100ms a 500ms, os limites do One UI: a menor duração perceptível e o máximo que não atrapalha a tarefa seguinte ([One UI](https://developer.samsung.com/one-ui/motion/basic.html)).

> **Divergência entre referências** O gov.br publica tokens de 0,8 e 1 segundo para macro animações ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)). O One UI fixa 500ms como teto ([One UI](https://developer.samsung.com/one-ui/motion/basic.html)), e o próprio gov.br diz que, a partir de 0,5 segundo, as animações começam a parecer pesadas e que a maioria deve ser muito rápida ou rápida. Pela convergência, o Trama mantém o teto de `--m-slower`. O gov.br também sugere cerca de 0,1 segundo para checkbox e switch; o Trama usa `--m-fast` no checkbox e mantém `--m-normal` no switch do kit, cujo botão percorre uma distância: nenhum dos critérios de decisão separa as duas opções, e o Trama mantém o valor do kit.

**Escolha a duração pelo tamanho, pela distância e pela frequência.** Elementos maiores e percursos mais longos pedem mais tempo ([Fluent](https://fluent2.microsoft.design/motion)). Quanto mais vezes a pessoa vê uma animação, mais curta e sutil ela deve ser ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

**Faça a saída mais curta que a entrada.** Quando uma camada fecha, a pessoa já decidiu sair. Um diálogo entra em `--m-slow` e sai em `--m-normal`. O gov.br dá o mesmo exemplo: uma janela que leva 0,30 segundo para aparecer e 0,20 a 0,25 para sumir ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

### Curvas

| Token               | Valor                  | Comportamento                    | Aplique em                                                         |
|---------------------|------------------------|----------------------------------|--------------------------------------------------------------------|
| `--m-ease-standard` | cubic-bezier(.2,0,0,1) | Acelera rápido e assenta devagar | Elementos que mudam dentro da tela: estados, tamanho, posição      |
| `--m-ease-enter`    | cubic-bezier(0,0,0,1)  | Começa rápido e desacelera       | Elementos que entram: diálogos, drawers, menus, toasts             |
| `--m-ease-exit`     | cubic-bezier(.3,0,1,1) | Começa devagar e acelera         | Somente elementos que saem da tela ou desaparecem                  |
| `--m-linear`        | linear                 | Velocidade constante             | Opacidade pura, rotação contínua do spinner, barras indeterminadas |

**Prefira a desaceleração.** Começar rápido dá sensação de resposta, e terminar devagar parece natural. O gov.br aponta a curva que desacelera como a melhor para interfaces e alerta que a curva que acelera parece lenta no início e termina de forma brusca ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)). Por isso `--m-ease-exit` só vale para o que sai da tela, cujo fim a pessoa não vê. O One UI usa a mesma divisão: aceleração para o que sai e desaceleração para o que chega ([One UI](https://developer.samsung.com/one-ui/motion/basic.html)).

**Use a curva linear só em opacidade e rotação.** Em deslocamentos e escalas, a velocidade constante parece artificial. O gov.br ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)) e o One UI ([One UI](https://developer.samsung.com/one-ui/motion/basic.html)) fazem o mesmo alerta.

### Catálogo de transições

Toda animação do Trama é uma destas transições, ou a combinação de no máximo duas. O catálogo segue o do gov.br, que pede cautela ao combinar tipos e prefere o efeito mais sutil ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

| Transição                          | Use para                                                         | Exemplo no Trama                         | Tokens                                   |
|------------------------------------|------------------------------------------------------------------|------------------------------------------|------------------------------------------|
| Opacidade (surgir e sumir)         | Elementos que entram ou saem depois de uma ação, troca de página | Tooltip, troca de painel de aba          | `--m-normal`, `--m-linear`               |
| Cor                                | Mudança de estado                                                | Hover e pressionado                      | `--m-fast`, `--m-ease-standard`          |
| Escala                             | Realçar a relevância de um elemento                              | Botão do switch, marca do checkbox       | `--m-fast` ou `--m-normal`               |
| Preenchimento (escala e opacidade) | Passar entre elementos sem relação forte                         | Abertura de popover a partir do controle | `--m-normal`, `--m-ease-enter`           |
| Deslocamento                       | Elementos com relação espacial ou de navegação                   | Drawer, folha inferior, toast            | `--m-slow` entrando, `--m-normal` saindo |
| Elevação                           | Subir ou descer de camada                                        | Card interativo de `--e-2` para `--e-3`  | `--m-normal`, `--m-ease-standard`        |
| Rotação                            | Indicar abertura ou atividade contínua                           | Indicador do acordeão, spinner           | `--m-normal`; spinner com `--m-linear`   |
| Canto                              | Mudar o arredondamento junto com a forma                         | Só dentro de uma transformação de forma  | A da transformação                       |
| Forma                              | Transformar um elemento em outro e mostrar a relação entre eles  | Lista que vira lista e detalhe           | `--m-slower`, `--m-ease-standard`        |

### Boas práticas

**Dê retorno imediato.** A resposta visual ao toque ou ao clique começa sem atraso ([One UI](https://developer.samsung.com/one-ui/motion/intro.html)).

**Nunca faça a pessoa esperar uma animação terminar.** Controles ficam utilizáveis durante a transição, e uma nova ação interrompe a anterior ([HIG](https://developer.apple.com/design/human-interface-guidelines/motion)). Prefira transições CSS, que revertem a partir do ponto atual.

**Siga o caminho que a pessoa espera.** Um drawer que entra pela direita sai pela direita ([HIG](https://developer.apple.com/design/human-interface-guidelines/motion)).

**Não anime várias coisas ao mesmo tempo.** A animação serve para levar o olhar a um ponto; várias juntas, mesmo sutis, competem com o conteúdo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)). Ao revelar uma lista, escalone só os primeiros itens visíveis, dentro de `--m-slower` no total ([Fluent](https://fluent2.microsoft.design/motion)).

**Evite surgimentos bruscos.** Um elemento que aparece de repente, rápido demais ou sem origem visível causa confusão e sobrecarga, sobretudo para pessoas com TDAH ou limitações intelectuais ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

**Não use movimento como único meio de comunicar.** Um aviso que treme precisa também de texto. Combine o retorno visual com outros canais ([HIG](https://developer.apple.com/design/human-interface-guidelines/motion)) e anuncie mudanças dinâmicas com regiões `aria-live`.

**Prefira componentes nativos.** Elementos como `<details>` e `<dialog>` já trazem recursos de acessibilidade integrados ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

**Teste com as pessoas.** Um movimento que parece sutil para quem o desenhou pode incomodar no contexto de quem usa ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

### Movimento reduzido

Pessoas com distúrbios vestibulares podem sentir náusea e desorientação ao fixar o olhar em objetos em movimento ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)). O Trama protege essas pessoas de duas formas.

**Siga a preferência do sistema.** Com `prefers-reduced-motion: reduce`, troque deslocamentos e escalas por esmaecimentos curtos ou mudança instantânea, pare animações automáticas e repetitivas, como o brilho do skeleton e carrosséis, e não anime desfoque nem profundidade ([HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)). Mantenha o retorno de estado (cor, borda, texto) sem transição, e um indicador de progresso estático com texto.

**Ofereça no produto um controle explícito para desligar animações não essenciais.** Nem todo mundo sabe ativar a preferência do sistema, e um computador compartilhado pode não tê-la. O gov.br pede uma opção explícita para ativar ou desativar as animações ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)). Coloque o controle nas configurações, comece ligado quando o sistema pedir menos movimento e guarde a escolha por pessoa.

``` code
@media (prefers-reduced-motion: reduce) {
  :root * { animation-duration: 0s !important; animation-iteration-count: 1 !important; transition-duration: 0s !important; }
}
:root[data-motion="reduced"] * {
  animation-duration: 0s !important; animation-iteration-count: 1 !important; transition-duration: 0s !important;
}
```

O `kit.css` aplica a regra do sistema a tudo que está dentro de `.tr-demo`. Em produção, aplique as duas regras no escopo raiz e defina `data-motion` no elemento `html` conforme a escolha da pessoa.

**Dê pausa a todo movimento automático.** Movimento que começa sozinho e dura mais de cinco segundos precisa de controle para pausar (WCAG 2.2, 2.2.2), e nada pisca mais de três vezes por segundo (WCAG 2.2, 2.3.1). O gov.br pede controle de pausa para movimento automático acima de cinco segundos e para elementos que piscam por mais de três segundos, pelo risco de crises em pessoas com epilepsia ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

### Considerações por plataforma

#### Web desktop

Com ponteiro, hover é a interação mais frequente. Mantenha-o em `--m-fast`, sem deslocamento nem mudança de tamanho. Um drawer de tela larga percorre mais pixels, mas continua em `--m-slow`.

#### Web móvel

Em gestos de arrastar, como fechar uma folha inferior, o elemento acompanha o dedo e só anima a partir do ponto em que a pessoa solta ([HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)). Celulares de entrada sofrem com animações de layout: anime só `transform` e `opacity`. O gov.br sugere movimentos simplificados em celulares e tablets ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/movimento)).

#### Tablets e dobráveis

Quando a classe de janela muda, por exemplo ao abrir um dobrável, a passagem de uma coluna para lista e detalhe pode usar uma transformação de forma em `--m-slower`. Ao entrar ou sair da postura semidobrada, mostre uma transição visual da mudança de layout ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Acessibilidade
- Estados de interação
- Configurações
- Carregamento e espera
- Carrossel
- Elevação
- Postura e dobra

#### Referências

- [Movimento](https://www.gov.br/ds/fundamentos-visuais/movimento) gov.br DS
- [Motion](https://developer.apple.com/design/human-interface-guidelines/motion) Apple HIG
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) Apple HIG
- [Motion](https://fluent2.microsoft.design/motion) Fluent 2
- [Motion introduction](https://developer.samsung.com/one-ui/motion/intro.html) Samsung One UI
- [Motion basics and usage](https://developer.samsung.com/one-ui/motion/basic.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o catálogo de transições, as áreas micro, média e macro, o controle explícito para desligar animações no produto e as regras sobre surgimentos bruscos e frequência. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                   |

## Privacidade

Peça só os dados de que precisa, explique para que servem, peça no momento certo e proteja o que as pessoas confiam a você.

As pessoas usam seus dispositivos de forma pessoal e esperam que os produtos ajudem a preservar sua privacidade ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)). Em produtos web, essa confiança se constrói em quatro lugares: nos formulários que coletam dados pessoais, nos pedidos de permissão do navegador, no consentimento para cookies e no que a interface mostra na tela.

Produtos que tratam dados de pessoas no Brasil estão sujeitos à Lei nº 13.709/2018, a Lei Geral de Proteção de Dados Pessoais (LGPD). O Padrão Digital de Governo pede que todo formulário respeite a LGPD e solicite o mínimo de informações absolutamente necessárias ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). As regras desta página são decisões de design e não substituem orientação jurídica: consulte a pessoa encarregada de dados da sua organização antes de publicar qualquer fluxo de coleta, como orienta o GOV.UK para as leis do Reino Unido ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)). Veja Legislação e normas.

### Boas práticas

#### Coleta de dados

**Peça apenas os dados de que realmente precisa.** Pedir mais do que uma função exige, ou pedir antes de a pessoa mostrar interesse por ela, abala a confiança ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)). Elimine campos desnecessários e não peça o que pode ser obtido de outra forma, coletado depois ou omitido ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). Para cada campo, pergunte: o serviço funciona sem ele? Se funciona, remova o campo.

**Dê a cada dado uma finalidade clara e diga qual é.** A coleta precisa ter um propósito conhecido e informado, nunca genérico ou para uso futuro. Explique o motivo, principalmente para dados pessoais e sensíveis ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). Use o texto de ajuda do campo (`.tr-hint`), como recomenda o DKFDS para informações sensíveis ([DKFDS](https://designsystem.dk/styleguide/typografi/tekst/)).

**Diga o que a pessoa ganha ao preencher campos opcionais.** Em cada campo opcional, deixe claro o benefício oferecido a quem responde ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)).

**Peça consentimento com opções desmarcadas, granulares e reversíveis.** Exiba as opções de consentimento sem marcação prévia; ofereça escolhas separadas por finalidade, com checkbox ou switch junto ao texto da pergunta; deixe a pessoa escolher como os dados serão usados e explique como retirar o consentimento ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)).

**Deixe a pessoa ver, corrigir e excluir os próprios dados.** Ofereça na área de conta um caminho para revisar e editar dados pessoais. Veja Contas e autenticação e Configurações.

#### Política de privacidade

**Escreva a política em linguagem simples.** Use termos de fácil entendimento, evite termos técnicos e "juridiquês" e divida o conteúdo por assunto, para que fique fácil de escanear ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). Pessoas compartilham menos quando não entendem como os dados serão usados ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)).

**Ponha a política ao alcance de todas as páginas.** Link a política de privacidade no rodapé e perto de cada formulário de coleta. Não esconda as regras em termos e condições ([GOV.UK](https://design-system.service.gov.uk/patterns/cookies-page/)).

#### Permissões do navegador

**Peça permissão só quando a função precisar.** Localização, câmera, microfone, notificações e área de transferência exigem consentimento do navegador. Espere a pessoa acionar a função que depende do recurso ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)). No Trama, o padrão é um botão explícito, como "Usar minha localização".

**Se precisar de contexto antes do pedido do navegador, mostre uma tela com um único botão.** Use "Continuar", nunca "Permitir", que se confunde com o botão do navegador, e não inclua outras ações ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)).

**Escreva o motivo numa frase ativa e específica.** A Apple contrasta "The app records during the night to detect snoring sounds" com a justificativa vaga e passiva "Microphone access is needed for a better experience" ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)).

**Faça** Explique o uso concreto e o que acontece com o dado.

**Não faça** Use justificativas vagas na voz passiva.

**Trate a recusa como resposta válida.** Se a pessoa negar o acesso, ofereça um caminho alternativo, como digitar o CEP. Nunca bloqueie o produto inteiro por uma permissão opcional.

**Nunca imite o pedido do sistema nem ofereça incentivos para aceitar.** A Apple rejeita telas que oferecem recompensas, imitam o alerta do sistema ou anotam a tela por trás dele ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)). O Trama aplica a mesma regra a todos os pedidos de consentimento.

#### Cookies e armazenamento

**Não grave nada não essencial antes do consentimento.** Cookies, `localStorage` e service workers não essenciais só podem ser definidos depois de aceitação ativa ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/), [DKFDS](https://designsystem.dk/komponenter/cookiemeddelelse/)). Aceitar e recusar têm o mesmo peso visual. O padrão completo, com banner, página de cookies e preferências, está em Consentimento de cookies.

#### Senhas e dados de acesso

**Oculte a senha por padrão e ofereça "Mostrar senha".** A pessoa pode não estar num lugar reservado. O botão de mostrar permite conferir o que foi digitado e dispensa o campo "Confirmar senha" ([GOV.UK](https://design-system.service.gov.uk/components/password-input/)). O gov.br também pede um recurso para mostrar e ocultar a senha ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)).

**Exija no mínimo 8 caracteres e nenhum máximo, e permita colar.** Bloqueie senhas comuns, explique as restrições e não force trocas periódicas ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/)). Use `autocomplete="new-password"` na criação e `current-password` no acesso; desligue `spellcheck` e `autocapitalize` ([GOV.UK](https://design-system.service.gov.uk/components/password-input/)). Mostre a força em texto (Fraca, Média, Forte) com dicas.

> **Divergência entre referências** O gov.br pede um segundo campo para confirmar a senha, sugere "pelo menos seis a oito caracteres" e níveis "Baixa, Média e Alta" ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). O GOV.UK exige no mínimo 8 caracteres e dispensa a confirmação quando há "Mostrar senha" ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/), [GOV.UK](https://design-system.service.gov.uk/components/password-input/)). O gov.br também recomenda o recurso de mostrar a senha, que já permite conferir o que foi digitado. O Trama fica com 8 caracteres no mínimo, sem campo de confirmação quando houver "Mostrar senha", e adota o medidor em texto pedido pelo gov.br, com os rótulos Fraca, Média e Forte.

**Não revele qual dado está errado no acesso.** Use "E-mail ou senha incorretos" ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/)). Ofereça sempre a opção de recuperar a senha em local visível ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)), por link ou código com validade, e nunca envie senhas por e-mail ([GOV.UK](https://design-system.service.gov.uk/patterns/passwords/)). Prefira passkeys quando possível ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)).

#### Exibição de dados pessoais

**Mascare dados sensíveis na tela.** Mostre só os dígitos necessários para reconhecer um documento, como "•••.456.789-••", e exija ação explícita para revelar o valor completo. O gov.br pede recursos de anonimização para senhas e dados pessoais sensíveis ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)).

**Avise quando um dado foi anonimizado.** Se um campo exibe um dado anonimizado, mostre uma mensagem do sistema dizendo isso; um ícone pode reforçar a condição ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)).

**Use o estado visitado de links com cuidado.** A cor de link visitado revela por onde a pessoa navegou e pode expor informação pessoal em situações sensíveis, como num computador compartilhado ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Em listas de resultados sobre saúde, processos ou benefícios, considere não diferenciar `--t-link-visited` de `--t-link`.

**Não coloque dados pessoais em URLs, títulos de página ou notificações.** Esses lugares aparecem em históricos, abas compartilhadas e telas bloqueadas.

### Considerações por plataforma

#### Web desktop

Computadores costumam ser compartilhados. Mantenha "Sair" sempre visível e encerre sessões inativas com aviso prévio e opção de continuar. Não presuma quem está conectado ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)).

#### Web móvel

Use o tipo de campo e o `autocomplete` corretos para que o gerenciador de senhas do sistema funcione. Em telas pequenas, a dica de finalidade de um campo fica acima dele, nunca escondida num ícone de ajuda: informação necessária para decidir não vai para um tooltip ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)).

#### Tablets e dobráveis

Telas grandes ficam visíveis para quem está por perto, e dobráveis abertos sobre a mesa no modo Flex expõem o conteúdo ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)). Mantenha dados sensíveis mascarados por padrão também nessas telas.

### Recursos

#### Relacionados

- Consentimento de cookies
- Legislação e normas
- Contas e autenticação
- Entrada de dados
- Inclusão
- Links
- Campos de texto

#### Referências

- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Estados](https://www.gov.br/ds/fundamentos-visuais/estados) gov.br DS
- [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) Apple HIG
- [Passwords](https://design-system.service.gov.uk/patterns/passwords/) GOV.UK Design System
- [Password input](https://design-system.service.gov.uk/components/password-input/) GOV.UK Design System
- [Cookies page](https://design-system.service.gov.uk/patterns/cookies-page/) GOV.UK Design System
- [Cookie banner](https://design-system.service.gov.uk/components/cookie-banner/) GOV.UK Design System
- [Cookiemeddelelse](https://designsystem.dk/komponenter/cookiemeddelelse/) Det Fælles Designsystem
- [Tekst](https://designsystem.dk/styleguide/typografi/tekst/) Det Fælles Designsystem
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta as práticas de LGPD do gov.br (finalidade, benefício de campos opcionais, consentimento desmarcado e granular, anonimização, política em linguagem simples), o cuidado com o estado visitado e o medidor de força de senha, e move o padrão de cookies para página própria. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                                                                          |

## Internacionalização e direita para esquerda

Prepare o produto para outros idiomas, regiões e direções de escrita antes de traduzi-lo, para que cada versão pareça feita para quem a usa.

Internacionalização é o trabalho de preparar o software para lidar com idiomas e regiões diferentes do seu; localização é fornecer textos e recursos traduzidos para cada local ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). O idioma padrão dos produtos Trama é o português do Brasil, mas componentes e tokens precisam funcionar em qualquer idioma, inclusive nos escritos da direita para a esquerda (RTL), como árabe e hebraico.

Linguagem simples, sem referências culturais e sem marcação de gênero desnecessária, já deixa o produto mais fácil de localizar ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). O mesmo vale para o português neutro pedido pelo Padrão Digital de Governo, sem regionalismos nem gírias ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Veja Escrita e conteúdo e Inclusão.

### Boas práticas

#### Idioma e escolha de idioma

**Declare o idioma em todas as páginas e em cada trecho de outro idioma.** Use `lang="pt-BR"` no elemento `html`. O atributo ajuda leitores de tela a usar a pronúncia correta e melhora a indexação por mecanismos de pesquisa; trechos em outro idioma recebem o próprio `lang`, exceto nomes próprios e termos técnicos compreendidos no contexto ([gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html); WCAG 2.2, 3.1.1 e 3.1.2).

**Deixe a pessoa escolher o idioma.** Não troque o idioma automaticamente com base na localização. Guarde a escolha na conta de quem está conectado e numa preferência local para visitantes ([HDS](https://hds.hel.fi/foundation/guidelines/localisation)). Essa preferência é funcional; se ela for gravada em cookie, siga Consentimento de cookies.

**Preserve o contexto ao trocar de idioma.** Mostre a página equivalente no novo idioma, sem mandar a pessoa para a página inicial. Se a página não existir no outro idioma, informe isso e ofereça próximos passos ([HDS](https://hds.hel.fi/foundation/guidelines/localisation)).

**Não use bandeiras para representar idiomas.** Idiomas não pertencem a um só país. Escreva o nome de cada idioma nele mesmo, com o código, como "Português (PT)", "English (EN)", "Español (ES)" ([HDS](https://hds.hel.fi/foundation/guidelines/localisation)).

**Traduza todo texto dos componentes, inclusive os rótulos ocultos.** Nomes acessíveis, textos de status e rótulos padrão também mudam de idioma. O cookiebar do gov.br recebe um conjunto de textos por idioma e não traduz nada sozinho: cada valor precisa ser informado no idioma usado ([gov.br DS](https://www.gov.br/ds/components/cookiebar)). Os componentes do Trama seguem o mesmo modelo.

#### Texto e layout

**Reserve espaço para a expansão do texto.** Traduções costumam ser mais longas ou mais curtas que o original. Não fixe larguras de botões, abas ou rótulos: o texto quebra a linha, nunca é truncado em títulos, botões, menus e mensagens. Teste com o idioma mais longo previsto.

**Não monte frases concatenando pedaços.** A ordem das palavras muda entre idiomas. Use mensagens completas com variáveis nomeadas e regras de plural do ICU, como em `{count, plural, one {# arquivo} other {# arquivos}}`.

**Formate datas, números, moedas e unidades pelo locale.** Use `Intl.DateTimeFormat`, `Intl.NumberFormat` e `Intl.RelativeTimeFormat`. Escreva o mês por extenso quando a data precisar ser entendida em regiões diferentes, porque "03/05" significa dias diferentes em cada região ([HDS](https://hds.hel.fi/foundation/guidelines/data-formats)). Use o fuso horário da pessoa quando disponível; senão, mostre o fuso, como "15:00 UTC-3" ([HDS](https://hds.hel.fi/foundation/guidelines/data-formats)). Em texto corrido, unidades vão por extenso, e a tradução precisa do plural correto de cada uma. Os formatos de pt-BR estão em Escrita e conteúdo.

**Use a pilha de fontes do Trama.** `--t-font-sans` recorre a fontes do sistema para escritas que a Inter não cobre. Confira a legibilidade de cada escrita nos tamanhos Caption (12/16) e Body small (14/20).

#### Dados de pessoas de outros países

**Aceite o formato de cada país e não bloqueie caracteres.** Aceite espaços, pontos, hífens, barras e parênteses, normalize no sistema e mostre o formato esperado no texto de ajuda. Formatar o valor exibido ao sair do campo é permitido; máscara que impede digitar ou apagar é proibida.

**Não divida números de telefone em vários campos e ofereça o código do país.** Campos separados aumentam o esforço e causam problemas para pessoas de outros países, que usam padrões diferentes; quando o serviço atende outros países, ofereça um seletor de código do país ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)).

> **Divergência entre referências** O gov.br recomenda máscaras de formatação dinâmicas, que funcionem também ao colar ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). Para pessoas de outros países, uma máscara presa ao formato brasileiro impede a digitação de um número válido. O Trama aceita qualquer formato, formata o valor exibido só ao sair do campo e proíbe máscaras que bloqueiem caracteres, mantendo do gov.br a dica de formato e o seletor de código do país.

#### Direita para esquerda

**Espelhe o layout inteiro com `dir="rtl"`.** Defina a direção no elemento `html`. Navegação lateral, ordem de colunas, alinhamento de texto, ícones direcionais e posição de botões se invertem. Componentes que seguem a direção do documento se espelham sozinhos ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left)). A ordem dos botões do Trama também se espelha: em formulários, a ação principal fica no início da linha, que em RTL é a direita.

**Escreva CSS com propriedades lógicas.** Use `margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `border-inline-start` e `text-align: start` no lugar de `left` e `right`.

> **Importante** Na versão 1.1, partes do `kit.css` ainda usam propriedades físicas: o indicador de página atual de `.tr-nav`, a borda entre painéis de `.tr-panes`, o alinhamento de `.tr-table th`, a posição de `.tr-drawer`, a margem do ícone de `.tr-link--external` e a margem de `.tr-input-action`. Esses componentes precisam de ajuste manual em RTL até a migração para propriedades lógicas.

**Alinhe parágrafos pelo idioma do texto.** Textos de uma ou duas linhas seguem a direção da interface. Parágrafos de três linhas ou mais seguem o idioma em que foram escritos ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left)). Use `dir="auto"` em conteúdo gerado por pessoas.

**Use o início da linha como alinhamento padrão.** À esquerda em LTR e à direita em RTL ([Fluent 2](https://fluent2.microsoft.design/typography)). Em tabelas, a regra de alinhar números ao fim da célula também se espelha.

**Alinhe todos os itens de uma lista do mesmo jeito.** Em RTL, inverta o alinhamento de todos os itens, inclusive os escritos em outra escrita ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left)).

#### Números

**Nunca inverta os algarismos de um número.** Os dígitos de um valor, telefone ou número de documento aparecem sempre na mesma ordem ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left)).

**Inverta a ordem de números que indicam progresso ou sequência.** Em sliders, barras de progresso e avaliações, os rótulos numéricos acompanham o controle espelhado ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left)).

**Use o sistema numérico do locale.** Hebraico usa algarismos ocidentais; árabe pode usar algarismos ocidentais ou orientais, conforme o país ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left)). `Intl.NumberFormat` resolve isso a partir do locale.

#### Controles e ícones

| Espelhe em RTL                                              | Não espelhe                                              |
|-------------------------------------------------------------|----------------------------------------------------------|
| Setas de voltar e avançar, chevrons de navegação, paginação | Logotipos e marcas                                       |
| Barras de progresso, sliders, indicadores de etapas         | Símbolos universais, como o sinal de verificação         |
| Ícones que representam texto ou direção de leitura          | Objetos do mundo real sem direção, como relógio e câmera |
| Ícones de movimento para frente ou para trás                | Controles que indicam uma direção física real            |
| Ordem de imagens com sequência significativa                | Fotografias e ilustrações                                |

As regras da tabela seguem a HIG ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left)). Os chevrons de expandir e recolher, que apontam para baixo e para cima, não mudam em RTL. Em SVG, aplique `transform: scaleX(-1)` só nos ícones marcados como direcionais no catálogo. Veja Iconografia.

**Equilibre escritas lado a lado.** Árabe e hebraico não têm maiúsculas e podem parecer menores ao lado de texto latino em caixa alta ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left)). Como o Trama não usa caixa alta, o caso é raro; quando acontecer, ajuste o tamanho da escrita RTL.

### Considerações por plataforma

#### Web desktop

Em RTL, a navegação lateral fica à direita e painéis de detalhe abrem a partir da esquerda. Atalhos com setas também se invertem: a seta para a esquerda avança.

#### Web móvel

Gestos de deslizar para voltar e carrosséis invertem o sentido em RTL. A ordem dos destinos da barra de navegação inferior também se inverte. Use o tipo de teclado adequado (`inputmode`) sem restringir os caracteres aceitos.

#### Tablets e dobráveis

Em layouts de dois painéis, a lista fica no lado de início (direita em RTL) e o detalhe no lado de fim. As proporções do Trama (42:58, 38:62 e 50:50) se mantêm, apenas espelhadas.

### Recursos

#### Relacionados

- Escrita e conteúdo
- Iconografia
- Tipografia
- Layout e grid
- Inclusão
- Entrada de dados

#### Referências

- [Acessibilidade no código HTML](https://www.gov.br/ds/guias/acessibilidade-html) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Cookiebar](https://www.gov.br/ds/components/cookiebar) gov.br DS
- [Princípios de UX writing](https://www.gov.br/ds/padroes/writing/principios-writing) gov.br DS
- [Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left) Apple HIG
- [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) Apple HIG
- [Typography](https://fluent2.microsoft.design/typography) Fluent 2
- [Localisation](https://hds.hel.fi/foundation/guidelines/localisation) Helsinki Design System
- [Data formats](https://hds.hel.fi/foundation/guidelines/data-formats) Helsinki Design System

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                                                             |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a regra do atributo `lang` do eMAG, tradução de rótulos ocultos, aceitação de formatos de outros países com seletor de código do país, unidades por extenso, espelhamento da ordem dos botões e a lista de classes do kit 1.1 com propriedades físicas. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                                                      |

