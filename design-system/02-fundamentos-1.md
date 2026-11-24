# Fundamentos: Acessibilidade a Formas e bordas

## Acessibilidade

Um produto acessível permite que qualquer pessoa perceba, opere e entenda a interface, seja qual for sua capacidade, seu dispositivo ou a forma como ela o usa.

O Trama adota como meta a conformidade com a **WCAG 2.2 no nível AA** em todos os tokens, componentes e padrões, nas três plataformas cobertas: web desktop, web móvel e tablets e dobráveis. Sempre que for viável sem custo para outros critérios, o Trama vai além do AA, como no alvo de toque de 44px. Produtos para o público brasileiro também observam a legislação descrita em Legislação e normas.

Acessibilidade diz respeito a muita gente. O Padrão Digital de Governo cita o Censo Demográfico de 2010 do IBGE: cerca de 45,6 milhões de pessoas declararam alguma deficiência visual, auditiva, motora, mental ou intelectual, o que correspondia a 23,9% da população ([gov.br DS](https://www.gov.br/ds/acessibilidade)). As dificuldades podem ser permanentes ou temporárias, como um braço quebrado ou uma tendinite ([gov.br DS](https://www.gov.br/ds/acessibilidade)), e também situacionais, como ouvir num trem barulhento ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)).

Usar o Trama não torna um produto acessível por si só: composição, conteúdo e fluxos continuam sob responsabilidade de cada equipe, como alerta o GOV.UK ([GOV.UK](https://design-system.service.gov.uk/accessibility/)).

### Quem precisa de acessibilidade

O gov.br agrupa as deficiências que mais afetam a interação com sistemas em quatro tipos: física, visual (baixa visão e cegueira, com necessidades diferentes), auditiva e cognitiva ([gov.br DS](https://www.gov.br/ds/acessibilidade)).

Todo componente do Trama precisa funcionar com as tecnologias assistivas que o gov.br destaca: ampliadores de tela, leitores de tela com voz ou braille, reconhecimento de voz, teclados alternativos e apontadores alternativos ([gov.br DS](https://www.gov.br/ds/acessibilidade)).

### Requisitos do Trama

A tabela resume o que todo produto construído com o Trama precisa cumprir. Os critérios citados são da WCAG 2.2.

| Tema                   | Requisito do Trama                                                                                                                                   | Critério WCAG 2.2                            |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| Contraste de texto     | 4.5:1 para texto normal; 3:1 para texto grande (Title 3 de 24px em diante, ou 18,66px em negrito).                                                   | 1.4.3 (AA)                                   |
| Contraste de não texto | 3:1 para contornos de controles, ícones informativos, indicadores de estado e anel de foco.                                                          | 1.4.11 (AA)                                  |
| Uso de cor             | Nenhuma informação transmitida só por cor.                                                                                                           | 1.4.1 (A)                                    |
| Foco                   | Anel de 2px `--t-focus` afastado 2px, só em `:focus-visible`; o elemento focado nunca fica totalmente coberto.                                       | 2.4.7 (AA), 2.4.11 (AA)                      |
| Teclado                | Toda função operável por teclado, sem armadilhas, em ordem lógica.                                                                                   | 2.1.1 (A), 2.1.2 (A), 2.4.3 (A)              |
| Alvo de ação           | 44 × 44px (`--c-touch`) em toque; 24 × 24px com mouse e trackpad. A área de ação pode ultrapassar a superfície visível.                              | 2.5.8 (AA); 2.5.5 (AAA) como referência      |
| Zoom e reflow          | Texto ampliável a 200% sem perda; conteúdo legível em 320px CSS de largura sem rolagem horizontal.                                                   | 1.4.4 (AA), 1.4.10 (AA)                      |
| Espaçamento de texto   | Layout resiste a altura de linha 1,5, espaço entre parágrafos de 2×, letras de 0,12× e palavras de 0,16× o tamanho da fonte.                         | 1.4.12 (AA)                                  |
| Movimento              | Respeitar `prefers-reduced-motion` e oferecer controle no produto para desligar animações não essenciais; nada pisca mais de três vezes por segundo. | 2.3.1 (A), 2.2.2 (A)                         |
| Tempo                  | Só toasts informativos sem ação somem sozinhos, com no mínimo 7 segundos e pausa em hover e foco.                                                    | 2.2.1 (A)                                    |
| Leitor de tela         | Nome, papel e valor expostos; mensagens de status anunciadas sem mover o foco.                                                                       | 4.1.2 (A), 4.1.3 (AA)                        |
| Formulários            | Rótulos visíveis, finalidade identificada por `autocomplete`, erros descritos em texto com sugestão de correção.                                     | 3.3.2 (A), 1.3.5 (AA), 3.3.1 (A), 3.3.3 (AA) |

> **Divergência entre referências** O gov.br e o eMAG tomam como base a WCAG 2.1 ([gov.br DS](https://www.gov.br/ds/acessibilidade), [gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html)). O GOV.UK, a referência mais recente lida, já trabalha com a WCAG 2.2 AA ([GOV.UK](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/)). A versão 2.2 inclui os critérios da 2.1 e acrescenta outros, como 2.4.11 e 2.5.8. Pelo critério de acessibilidade com mais margem, o Trama adota a WCAG 2.2 AA; um produto conforme ao Trama também atende aos critérios da 2.1.

### Boas práticas

#### Contraste e cor

**Use os pares de cor definidos pelos tokens alias.** Os pares abaixo foram calculados a partir dos valores do `kit.css` e atendem ao critério 1.4.3 nos dois temas. Ao combinar tokens de outra forma, meça o contraste nos temas claro e escuro. O gov.br faz a mesma exigência: toda cor escolhida precisa ser verificada em fundo claro e em fundo escuro ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)).

| Texto                            | Fundo                | Claro   | Escuro  |
|----------------------------------|----------------------|---------|---------|
| `--t-fg-1`                       | `--t-bg`             | 17.65:1 | 18.79:1 |
| `--t-fg-2`                       | `--t-bg`             | 9.56:1  | 11.36:1 |
| `--t-fg-3`                       | `--t-surface-2`      | 5.34:1  | 6.11:1  |
| `--t-on-brand`                   | `--t-brand`          | 6.04:1  | 7.85:1  |
| `--t-link`                       | `--t-bg`             | 6.04:1  | 10.34:1 |
| `--t-danger`                     | `--t-bg`             | 5.85:1  | 8.23:1  |
| `--t-success`                    | `--t-success-subtle` | 4.74:1  | 7.56:1  |
| `--t-border-control` (não texto) | `--t-bg`             | 3.15:1  | 5.09:1  |
| `--t-focus` (não texto)          | `--t-bg`             | 5.85:1  | 8.99:1  |

**Retire o que a pessoa não pode habilitar e explique o que está desabilitado.** `--t-fg-disabled` fica abaixo de 4.5:1, o que a WCAG permite em componentes inativos, e por isso é difícil de ler. Se a pessoa não tem como habilitar um elemento, ele sai da interface. Se pode, ele aparece desabilitado com o motivo em texto próximo ou num tooltip focável. Nunca desabilite o botão de envio de um formulário: valide ao enviar. O GOV.UK e o DKFDS também desaconselham botões desabilitados ([GOV.UK](https://design-system.service.gov.uk/components/button/), [DKFDS](https://designsystem.dk/komponenter/knapper/)).

**Transmita estados com forma, texto ou ícone além da cor.** Qualquer classificação feita por cor precisa também de uma identificação em texto ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Um campo com erro no Trama ganha borda de 2px, mensagem em texto e prefixo "Erro:" para leitores de tela.

**Faça** Combine cor, símbolo e palavra no status.

**Não faça** Diferencie estados apenas pela cor do indicador.

#### Foco e teclado

**Mostre o foco só na navegação por teclado.** O Trama aplica um contorno de `--stroke-thick` na cor `--t-focus`, afastado 2px, em `:focus-visible`. O clique não mostra o anel. Quando o sistema move o foco sem ação de teclado, como ao abrir uma etapa, use o foco tênue `.tr-focus-subtle`, de 1px. Não remova o `outline` sem substituí-lo por um indicador equivalente.

**Defina onde o foco começa.** Em página ou etapa nova, o foco vai para o título `h1`. Em diálogo informativo, para o botão Fechar; em diálogo de ação, para o primeiro campo ou para a ação principal; em diálogo destrutivo, para a ação segura, Cancelar. Ao fechar, devolva o foco ao elemento que abriu ([Fluent 2](https://fluent2.microsoft.design/accessibility)).

**Siga a ordem de leitura.** A ordem de foco acompanha a ordem visual: da esquerda para a direita e de cima para baixo em idiomas LTR ([Fluent 2](https://fluent2.microsoft.design/accessibility)).

**Não deixe elementos fixos cobrirem o foco.** Barras fixas, banners e rodapés pegajosos não podem esconder o elemento focado. O GOV.UK proíbe deixar o banner de cookies fixo no topo por esse motivo, e o DKFDS alerta que `position: fixed` ou `sticky` pode quebrar o critério 2.4.11 ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/), [DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/hjaelpeklasser/)).

**Ofereça links de pular.** Eles são os primeiros itens focáveis da página e ficam visíveis ao receber foco (WCAG 2.2, 2.4.1). Veja Links de pular, Teclado e Foco e seleção.

#### Alvo de ação e operação

**Garanta 44 × 44px de área tocável e 24 × 24px com mouse.** O token `--c-touch` define o mínimo de toque para checkbox, radio, switch, itens de lista e botões só com ícone. Controles visualmente menores, como o botão de fechar de um chip, ganham área invisível até o mínimo. A densidade alta só é permitida com apontador fino; a baixa é obrigatória em toque. Veja Densidade.

> **Divergência entre referências** O gov.br pede área de toque de 48 × 48px em ícones ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)), 40px no padrão de densidade ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)) e 44px no cookiebar ([gov.br DS](https://www.gov.br/ds/components/cookiebar)). A Apple usa 44 × 44 pt como tamanho padrão de controle ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)), e 44px coincide com o critério AAA 2.5.5. O Trama mantém 44px em todo alvo de toque, com no mínimo `--sp-200` entre alvos adjacentes ([One UI](https://developer.samsung.com/one-ui/accessibility/layout-and-typo.html)), e 24px com mouse, valor em que gov.br e WCAG 2.5.8 convergem.

**Ofereça alternativa a gestos e arrastes.** Toda ação feita por gesto, arraste ou múltiplos dedos precisa de um controle visível equivalente (WCAG 2.2, 2.5.7), como recomendam a Apple e a Samsung ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility), [One UI](https://developer.samsung.com/one-ui/accessibility/interaction-and-control.html)).

#### Zoom, reflow e texto

**Projete até 320px de largura.** Com zoom de 400% numa janela de 1280px, a página se comporta como uma tela de 320px, e o conteúdo precisa refluir sem rolagem horizontal ([Fluent 2](https://fluent2.microsoft.design/accessibility)).

**Use unidades relativas para texto.** Defina tamanhos de fonte em `rem`, com Body de 16px como base e nenhum texto abaixo de 12px. Teste a 200% de texto: nada pode ser cortado ou sobreposto ([One UI](https://developer.samsung.com/one-ui/accessibility/layout-and-typo.html)). Títulos, rótulos de botão e mensagens de erro quebram a linha em vez de truncar.

#### Movimento e tempo

**Respeite a preferência por movimento reduzido e ofereça um controle próprio.** Sob `prefers-reduced-motion: reduce`, o kit zera as durações de transição e animação. Além disso, ofereça no produto uma opção para desligar animações não essenciais, para quem não ajustou o sistema. Veja Movimento.

**Deixe a pessoa controlar o tempo das mensagens.** Só toasts informativos sem ação somem sozinhos, depois de pelo menos 7 segundos, com pausa em hover e foco. Mensagens com ação, de erro ou de alerta ficam até a pessoa fechar ou resolver. Não reproduza áudio ou vídeo automaticamente.

#### Leitor de tela e semântica

**Comece pelo HTML válido e semântico.** O eMAG define o processo em três passos: seguir os padrões web do W3C, seguir as recomendações de acessibilidade e avaliar a acessibilidade ([gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html)). Use cada elemento pelo que ele significa, listas como listas e tabelas só para dados tabulares, nunca para diagramar ([gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html)). O conteúdo principal deve funcionar sem CSS e o essencial sem JavaScript ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)). Use WAI-ARIA só quando o HTML nativo não resolver; quando a linguagem já tem a semântica, ela tem precedência ([gov.br DS](https://www.gov.br/ds/guias/wai-aria)). Veja HTML acessível e WAI-ARIA.

**Use títulos em ordem.** Um único `h1` por página, com o conteúdo principal, e níveis de `h2` a `h6` em hierarquia, sem pular níveis ([gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html), [Fluent 2](https://fluent2.microsoft.design/accessibility)).

**Associe todo campo a um rótulo.** Leitores de tela usam o `label` para dizer à pessoa o que preencher ([gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html)).

**Anuncie mudanças de estado.** O leitor de tela deve informar quando um checkbox é marcado, uma seção é expandida ou um item é excluído ([One UI](https://developer.samsung.com/one-ui/accessibility/screen-reader.html)). Use `role="status"` para confirmações e `role="alert"` só para erros que exigem atenção imediata.

**Escreva nomes acessíveis independentes do contexto visual.** "Novas mensagens disponíveis" funciona melhor do que "Novo" ([One UI](https://developer.samsung.com/one-ui/accessibility/screen-reader.html)). Links precisam fazer sentido fora do contexto, porque quem usa leitor de tela navega de link em link ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). O nome acessível contém o texto visível (WCAG 2.2, 2.5.3).

### Processo de teste

Ferramentas automáticas encontram só parte dos problemas. Um estudo do GDS de 2017, citado pelo GOV.UK, concluiu que cerca de 30% das falhas são detectadas por ferramentas como o axe-core ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)). O gov.br compara os avaliadores automáticos a corretores gramaticais, que não garantem a qualidade do texto mesmo sem apontar erros, e exige validação manual com checklists e avaliação por pessoas ([gov.br DS](https://www.gov.br/ds/acessibilidade), [gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html)). O Trama exige as quatro etapas abaixo antes de liberar um componente e as recomenda a cada tela de produto.

| Etapa                    | O que fazer                                                                                                                                                                                                                                                            |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1\. Revisão de design    | Conferir contraste dos pares de token, estados sem dependência de cor, alvos de ação, ordem de foco e anotações de leitor de tela no arquivo de design ([Fluent 2](https://fluent2.microsoft.design/accessibility)).                                                   |
| 2\. Testes automáticos   | Validar o HTML e rodar axe-core em todos os exemplos de código, em cada build ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/), [gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html)).                                    |
| 3\. Testes manuais       | Navegar só com teclado; usar NVDA com Firefox ou Chrome no Windows, VoiceOver com Safari no macOS e no iOS, TalkBack com Chrome no Android; testar zoom de 200% e 400%, cores forçadas do Windows e reconhecimento de voz; percorrer um checklist de validação humana. |
| 4\. Pesquisa com pessoas | Incluir pessoas com deficiência e com necessidades de acesso variadas nos testes de usabilidade ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/), [gov.br DS](https://www.gov.br/ds/acessibilidade)).                             |

**Registre problemas conhecidos.** Falhas sem correção rápida entram na página do componente e na declaração de acessibilidade, priorizadas pelo impacto em pessoas reais ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)).

### Considerações por plataforma

#### Web desktop

Teste a navegação completa por teclado, incluindo menus, diálogos e tabelas. Tooltips e popovers abertos por hover ou foco fecham com Esc (WCAG 2.2, 1.4.13).

#### Web móvel

A Lei nº 14.129/2021 estende a obrigação de acessibilidade dos serviços digitais públicos aos dispositivos móveis, como lembra o gov.br ([gov.br DS](https://www.gov.br/ds/acessibilidade)). Aplique sempre `--c-touch` e a densidade baixa. Não bloqueie o zoom com `user-scalable=no` nem com `maximum-scale`. Teste com VoiceOver e TalkBack.

#### Tablets e dobráveis

Teste nas duas orientações e nas telas externa e interna dos dobráveis. Ao abrir ou fechar o aparelho, preserve a posição de rolagem, o texto digitado e o foco atual ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Legislação e normas
- Inclusão
- Cor
- Densidade
- Foco e seleção
- Teclado
- Movimento
- Imagens
- HTML acessível e WAI-ARIA

#### Referências

- [Acessibilidade](https://www.gov.br/ds/acessibilidade) gov.br DS
- [Acessibilidade no código HTML](https://www.gov.br/ds/guias/acessibilidade-html) gov.br DS
- [Uso do WAI-ARIA](https://www.gov.br/ds/guias/wai-aria) gov.br DS
- [Cores](https://www.gov.br/ds/fundamentos-visuais/cores) gov.br DS
- [Iconografia](https://www.gov.br/ds/fundamentos-visuais/iconografia) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Cookiebar](https://www.gov.br/ds/components/cookiebar) gov.br DS
- [Princípios de UX writing](https://www.gov.br/ds/padroes/writing/principios-writing) gov.br DS
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) Apple HIG
- [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) Apple HIG
- [Accessibility](https://fluent2.microsoft.design/accessibility) Fluent 2
- [Accessibility](https://design-system.service.gov.uk/accessibility/) GOV.UK Design System
- [Accessibility strategy](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) GOV.UK Design System
- [Extending and modifying components](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/) GOV.UK Design System
- [Cookie banner](https://design-system.service.gov.uk/components/cookie-banner/) GOV.UK Design System
- [Hjælpeklasser](https://designsystem.dk/kom-i-gang/implementering-kode/hjaelpeklasser/) Det Fælles Designsystem
- [Screen reader](https://developer.samsung.com/one-ui/accessibility/screen-reader.html) Samsung One UI
- [Layout and typography](https://developer.samsung.com/one-ui/accessibility/layout-and-typo.html) Samsung One UI
- [Interaction and control](https://developer.samsung.com/one-ui/accessibility/interaction-and-control.html) Samsung One UI
- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) W3C

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta dados e leis citados pelo gov.br, o processo do eMAG, alvos de 24 e 44px, foco inicial e tempo, e registra divergências. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                       |

## Marca

Produtos construídos com o Trama expressam a própria marca com moderação, por meio de cor, logotipo, ilustração e voz, sem abrir mão de componentes e padrões familiares.

O Trama é um sistema de marca neutra. Ele fornece estrutura, componentes e tokens; cada produto traz sua identidade. A marca deve tornar o produto reconhecível e, ao mesmo tempo, oferecer uma experiência consistente com a plataforma ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/branding)). O Padrão Digital de Governo mostra o outro lado do mesmo objetivo: a paleta, os ícones e o texto padronizados existem para que a pessoa reconheça e memorize as interfaces do governo federal em qualquer sistema ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores), [gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)).

A cor azul-tinta de `--t-brand` é a marca padrão do próprio Trama e aparece em todo produto que não define a sua. Esta página explica onde a marca de um produto pode entrar, o que pode ser personalizado e como usar um logotipo.

### Boas práticas

#### Onde a marca entra

**Deixe a marca ceder espaço ao conteúdo.** Espaço ocupado só por um elemento de marca é espaço tirado do conteúdo ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/branding)). Todo elemento precisa ter função na tarefa da pessoa ([Ontario](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html)).

**Expresse a marca com componentes familiares.** Se precisar ajustar a aparência de um componente, preserve tamanho, posição e comportamento ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/branding)). No Trama, isso significa trocar valores de tokens alias de marca, nunca estrutura ou comportamento de componentes.

**Não use a tela de carregamento como peça de marca.** Ela some rápido demais para transmitir algo; apresente a marca numa tela de boas-vindas ou de onboarding ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/branding)). Veja Onboarding.

**Use ilustração para dar personalidade, com moderação.** O gov.br cita a ilustração como forma de personificar uma marca e de representar a identidade de governo, desde que não seja meramente decorativa ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Veja Ilustração.

#### Cor de marca

**Use a cor de marca com critério.** Cor de marca em excesso sobrecarrega a interface e dilui o impacto. Reserve-a para a ação principal e para indicadores de estado, como o item atual da navegação ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/branding)). No Trama, `--t-brand` aparece no botão primário, no item atual da navegação, em controles marcados, na barra de progresso e em links.

**Faça** Use a cor de marca na ação principal e deixe o resto neutro.

**Não faça** Aplique a cor de marca a todos os selos e a todas as ações.

**Não use cor de marca para comunicar status.** Sucesso, alerta e erro usam os tokens semânticos (`--t-success`, `--t-warning`, `--t-danger`). O HDS reserva as cores de status para estados ([HDS](https://hds.hel.fi/foundation/design-tokens/colour)), e o gov.br define cores de aviso próprias para informação, sucesso, alerta e erro ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)).

**Personalize só a família de tokens de marca, nos dois temas.** Tokens neutros, semânticos e de foco não mudam. Uma cor nova só entra depois de testada quanto a acessibilidade e aprovada pela equipe do sistema, regra que o gov.br aplica à sua paleta ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)).

| Token                                  | Uso                                             | Requisito                                                                 |
|----------------------------------------|-------------------------------------------------|---------------------------------------------------------------------------|
| `--t-brand`                            | Fundo do botão primário, indicadores de seleção | 3:1 contra `--t-bg` (WCAG 2.2, 1.4.11); 4.5:1 se usado como cor de texto  |
| `--t-brand-hover`, `--t-brand-pressed` | Estados de interação pré-calculados             | Progressivamente mais escuros no tema claro e mais claros no escuro       |
| `--t-on-brand`                         | Texto sobre `--t-brand`                         | 4.5:1 contra `--t-brand`, `--t-brand-hover` e `--t-brand-pressed` (1.4.3) |
| `--t-brand-subtle`                     | Fundo de item selecionado e badges de marca     | `--t-brand` sobre ele com 4.5:1                                           |
| `--t-link`                             | Links                                           | 4.5:1 contra `--t-bg` e distinto de `--t-link-visited`                    |

A cor de marca padrão do Trama atinge 6.04:1 entre `--t-on-brand` e `--t-brand` no tema claro e 7.85:1 no escuro. Veja Tokens de design e Cor.

#### Produtos para órgãos públicos

**Use a identidade do governo quando o produto for de um órgão federal.** O gov.br escolheu a família Blue Warm Vivid, com a cor Blue Warm Vivid 70, para representar a identidade do governo federal, e usa `#1351B4` como cor interativa em fundo claro e `#C5D4EB` em fundo escuro ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). Um produto Trama para esse contexto pode atribuir esses valores a `--t-brand` e `--t-link`. Pelos cálculos do Trama, `#1351B4` atinge 7.33:1 com texto branco, e `#C5D4EB` atinge 12.52:1 sobre `--t-bg` escuro; recalcule `--t-on-brand`, `--t-brand-hover` e `--t-brand-pressed` antes de publicar.

> **Divergência entre referências** O gov.br define o texto em fundo claro como `#333333`, de contraste menor que o preto, para deixar a leitura mais leve ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). O `--t-fg-1` do Trama, `#15191E`, atinge 17.65:1 contra 12.63:1 do `#333333`. Pelo critério de acessibilidade com mais margem, o Trama mantém `--t-fg-1` e não permite redefinir tokens de texto ao aplicar uma marca, inclusive a do governo.

#### Tipografia e voz

**Use fonte de marca só em títulos.** Se a marca tem uma fonte própria, ela pode substituir `--t-font-sans` de Title 3 em diante. Mantenha Inter no corpo e nos controles, que precisam de legibilidade em tamanhos pequenos ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/branding)). A fonte precisa suportar zoom de 200% e os pesos 400, 600 e 700. Títulos usam caixa de frase, nunca caixa alta.

**Expresse a voz da marca dentro das regras de escrita do Trama.** A HIG admite exclamações e emojis como parte da voz de uma marca ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/branding)). O Trama não os usa em texto de interface e pede voz neutra e desburocratizada, como o gov.br ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). A personalidade aparece na escolha de palavras e nos estados vazios. Veja Escrita e conteúdo.

### Logotipo do produto

O Trama não tem logotipo para uso em produtos. Cada produto usa o próprio logotipo, seguindo estas regras.

**Posicione o logotipo no início do cabeçalho.** À esquerda em LTR, à direita em RTL. O DKFDS exige o logotipo alinhado à esquerda no cabeçalho e o HDS o posiciona no canto superior esquerdo ([DKFDS](https://designsystem.dk/styleguide/logoer/), [HDS](https://hds.hel.fi/foundation/visual-assets/logo)). No kit, use `.tr-header__logo` seguido de `.tr-header__title`.

**Faça o logotipo levar à página inicial do produto.** Logotipo e nome formam um único link ([HDS](https://hds.hel.fi/components/logo), [DKFDS](https://designsystem.dk/styleguide/logoer/)). Se o link tirar a pessoa de um fluxo com dados não salvos, peça confirmação antes ([DKFDS](https://designsystem.dk/styleguide/logoer/)).

**Mostre o nome do produto ao lado do símbolo.** Isso ajuda a pessoa a saber em qual serviço está ([HDS](https://hds.hel.fi/components/logo)). Use o símbolo sozinho apenas quando não houver espaço ([Geist](https://vercel.com/geist/brands)).

**Escreva o texto alternativo como destino.** Use "\[Nome do produto\], página inicial", no padrão "\[portal\] forside" do DKFDS ([DKFDS](https://designsystem.dk/styleguide/logoer/)). Se o nome já aparece como texto no link, oculte a imagem com `alt=""`.

**Respeite tamanho e área de proteção.** No cabeçalho, a altura do logotipo não passa de 32px (`--icon-xl`); no rodapé, de 24px (`--icon-lg`). Use SVG. A área livre ao redor é, no mínimo, igual à altura do símbolo, como define o Geist para a marca Vercel ([Geist](https://vercel.com/geist/brands)).

**Não altere o logotipo e forneça versões para fundo claro e escuro.** Não redesenhe, distorça, recolora fora das versões aprovadas nem aplique efeitos ([HDS](https://hds.hel.fi/foundation/visual-assets/logo), [Geist](https://vercel.com/geist/brands)). Ambas as versões têm contraste AA contra o fundo ([HDS](https://hds.hel.fi/foundation/visual-assets/logo)). Em rodapés escuros dentro do tema claro, use `.tr-inverse`, que redefine os tokens alias para os valores escuros, e a versão do logotipo para fundo escuro. Nunca espelhe o logotipo em RTL ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/right-to-left)).

**Não repita o logotipo pela interface.** Cabeçalho e rodapé bastam ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/branding), [HDS](https://hds.hel.fi/foundation/visual-assets/logo)).

> **Nota** Não use símbolos de bibliotecas de ícones de terceiros como logotipo. A licença do SF Symbols, por exemplo, proíbe esse uso ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)). Ícones de marcas de terceiros, como redes sociais, seguem as regras de cada marca.

#### Favicon

**Forneça um favicon próprio do produto.** O favicon identifica o produto em abas, favoritos, histórico e resultados de pesquisa ([Ontario](https://designsystem.ontario.ca/components/detail/favicon.html)). Use o símbolo do produto. Siga o pacote do Ontario: um SVG que funcione nos temas claro e escuro, um ICO de 32 × 32px e PNGs de 48, 180, 192 e 512px no `manifest.json` ([Ontario](https://designsystem.ontario.ca/components/detail/favicon.html)).

### Considerações por plataforma

#### Web desktop

Logotipo completo com símbolo e nome no cabeçalho. Em navegação lateral recolhível, mostre o nome com o símbolo quando expandida e só o símbolo quando recolhida.

#### Web móvel

Na classe Compacta, use o símbolo com o nome em texto se couber; se não couber, o símbolo sozinho, com o nome do produto no `alt`. Ícones de atalho na tela inicial usam os PNGs de 180 e 192px ([Ontario](https://designsystem.ontario.ca/components/detail/favicon.html)).

#### Tablets e dobráveis

No rail de navegação (`.tr-rail`), mostre o símbolo no topo, sem o nome. Na tela externa de um dobrável, siga as regras da web móvel.

### Recursos

#### Relacionados

- Cor
- Tokens de design
- Ilustração
- Tipografia
- Escrita e conteúdo
- Cabeçalho
- Rodapé

#### Referências

- [Cores](https://www.gov.br/ds/fundamentos-visuais/cores) gov.br DS
- [Iconografia](https://www.gov.br/ds/fundamentos-visuais/iconografia) gov.br DS
- [Ilustração](https://www.gov.br/ds/fundamentos-visuais/ilustracao) gov.br DS
- [Princípios de UX writing](https://www.gov.br/ds/padroes/writing/principios-writing) gov.br DS
- [Branding](https://developer.apple.com/design/human-interface-guidelines/branding) Apple HIG
- [Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left) Apple HIG
- [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) Apple HIG
- [Logoer](https://designsystem.dk/styleguide/logoer/) Det Fælles Designsystem
- [Favicon](https://designsystem.ontario.ca/components/detail/favicon.html) Ontario Design System
- [Ontario Government design principles](https://designsystem.ontario.ca/docs/documentation/explore/design-principles.html) Ontario Design System
- [Logo (visual asset)](https://hds.hel.fi/foundation/visual-assets/logo) Helsinki Design System
- [Logo (component)](https://hds.hel.fi/components/logo) Helsinki Design System
- [Colour](https://hds.hel.fi/foundation/design-tokens/colour) Helsinki Design System
- [Brands](https://vercel.com/geist/brands) Geist

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a aplicação da identidade do governo federal em produtos para órgãos públicos, a aprovação de cores novas, a ilustração como expressão de marca, o cabeçalho com `.tr-header`, o rodapé com `.tr-inverse` e tamanhos de logotipo em tokens de ícone, e registra a divergência sobre a cor de texto. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                                                                                                  |

## Cor

A cor do Trama organiza superfícies, dá legibilidade ao texto, indica o que é interativo e comunica avisos, com um papel nomeado para cada valor nos dois temas.

O Trama organiza a cor em duas camadas. Os tokens globais (`--g-*`) guardam os valores brutos: uma rampa de neutros com leve viés frio e uma rampa de marca em azul-tinta. Os tokens alias (`--t-*`) dão significado a esses valores. Produtos usam somente os alias. Assim, quando o tema muda ou a paleta evolui, nenhuma tela precisa ser editada.

A paleta é contida: os neutros fazem quase todo o trabalho de estrutura, a marca aparece em poucos pontos de ação e as cores de aviso ficam reservadas para status, como na paleta majoritariamente cinza do DKFDS ([DKFDS](https://designsystem.dk/styleguide/farver/)).

### Funções da cor

Todo token alias pertence a uma de quatro funções. A divisão vem do Padrão Digital de Governo, que separa cores de superfície, de leitura, de interação e de avisos ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). Escolha a cor pela função, e nunca pela aparência.

| Função     | Tokens                                                                                                                    | Regra                                                                             |
|------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Superfície | `--t-bg`, `--t-surface-1`, `--t-surface-2`, `--t-surface-raised`, `--t-border-subtle`, `--t-border`, `--t-border-control` | Base neutra de páginas e componentes, e seus limites                              |
| Leitura    | `--t-fg-1`, `--t-fg-2`, `--t-fg-3`, `--t-on-brand`, `--t-fg-disabled`                                                     | Texto e ícones. Para cada superfície existe uma cor de leitura que passa de 4,5:1 |
| Interação  | `--t-brand` e variações, `--t-link`, `--t-link-visited`, `--t-focus`                                                      | Só em elementos acionáveis e nos seus estados                                     |
| Aviso      | `--t-danger`, `--t-warning`, `--t-success`, `--t-info`, com `-subtle`, `-border` e `-fill`                                | Erro, alerta, sucesso e informação, sempre com ícone ou texto                     |

O gov.br pede para evitar a cor de interação em elementos que não são interativos, para não confundir a pessoa ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). No Trama, azul-tinta em texto estático é proibido.

### Paleta

#### Superfície e leitura

| Amostra | Token alias          | Claro    | Escuro   | Papel                                 |
|---------|----------------------|----------|----------|---------------------------------------|
|         | `--t-bg`             | \#FFFFFF | \#0F1215 | Fundo da página                       |
|         | `--t-surface-1`      | \#F6F7F8 | \#171B20 | Áreas secundárias, barra lateral      |
|         | `--t-surface-2`      | \#EEF0F2 | \#1F242A | Trilhos, fundo do controle segmentado |
|         | `--t-surface-raised` | \#FFFFFF | \#1B2025 | Cards, menus, diálogos                |
|         | `--t-border-subtle`  | \#E1E4E8 | \#2A3037 | Divisores                             |
|         | `--t-border`         | \#C9CED4 | \#3A424B | Contornos de cards e chips            |
|         | `--t-border-control` | \#8A929C | \#7D8691 | Contorno de controles                 |
|         | `--t-fg-disabled`    | \#9AA1AA | \#5C646D | Texto e ícones desabilitados          |
|         | `--t-fg-3`           | \#5A636E | \#9AA3AD | Texto de apoio, legendas, placeholder |
|         | `--t-fg-2`           | \#3E4650 | \#C3CAD2 | Texto secundário                      |
|         | `--t-fg-1`           | \#15191E | \#FFFFFF | Texto principal                       |

#### Interação

| Amostra | Token alias         | Claro    | Escuro   | Papel                                    |
|---------|---------------------|----------|----------|------------------------------------------|
|         | `--t-brand`         | \#0E6E6E | \#4FC1BC | Ação principal, seleção, indicador ativo |
|         | `--t-brand-hover`   | \#0B5A5A | \#6FD0CB | Marca em hover                           |
|         | `--t-brand-pressed` | \#084646 | \#8FDCD8 | Marca pressionada                        |
|         | `--t-brand-subtle`  | \#E3F2F1 | \#12302F | Fundo de item ativo ou selecionado       |
|         | `--t-on-brand`      | \#FFFFFF | \#06201F | Texto e ícone sobre a marca              |
|         | `--t-link`          | \#0E6E6E | \#6FD0CB | Links                                    |
|         | `--t-link-visited`  | \#5B3E96 | \#C3A8F2 | Links visitados                          |
|         | `--t-focus`         | \#1A5FD0 | \#8AB4FF | Anel de foco, exclusivamente             |

#### Aviso

Cada cor de aviso tem a cor principal (texto, ícone, preenchimento forte), `-subtle` (fundo de mensagem ou badge) e `-border` (contorno de mensagem). `--t-warning-fill` é o amarelo de preenchimento, com ícone escuro por cima. `--t-success-fill` (#1E7A3A) e `--t-info-fill` (#1F5FBF) têm o mesmo valor nos dois temas e levam texto \#FFFFFF, com 5,38:1 e 6,09:1.

| Aviso      | Principal                        | Subtle | Border | Use para                                   |
|------------|----------------------------------|--------|--------|--------------------------------------------|
| Erro       | `--t-danger`                     |        |        | Erros, ações destrutivas, campos inválidos |
| Alerta     | `--t-warning` `--t-warning-fill` |        |        | Situações que pedem atenção sem bloquear   |
| Sucesso    | `--t-success`                    |        |        | Confirmações, etapas concluídas            |
| Informação | `--t-info`                       |        |        | Avisos neutros, dicas, novidades           |

#### Luminância dos tokens globais

O número de um token global da rampa clara indica a sua luminância. Tokens com o mesmo número têm luminância próxima e, por isso, contraste parecido sobre o branco: `--g-grey-60` tem luminância relativa 0,122 e 6,10:1 sobre \#FFFFFF; `--g-brand-60` tem 0,124 e 6,04:1. O gov.br organiza toda a paleta assim, com a mesma gradação de luminância em todas as famílias de cor ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). Na rampa do tema escuro (`--g-*-dk-*`), o número indica só a posição na rampa.

### Boas práticas

**Use os tokens alias, nunca o valor hexadecimal.** Escreva `--t-danger` em vez de \#C2261B. O valor pode mudar entre versões e entre temas, e o alias carrega a intenção. O GOV.UK dá a mesma orientação para suas cores funcionais ([GOV.UK](https://design-system.service.gov.uk/styles/colour/)), e a Apple pede que não se fixem valores de cores do sistema no código ([HIG](https://developer.apple.com/design/human-interface-guidelines/color)).

**Aplique a marca com parcimônia.** Reserve `--t-brand` para o botão primário, o item ativo da navegação, controles marcados e indicadores de progresso. Evite fundos grandes na cor da marca: eles enfraquecem a hierarquia ([Fluent](https://fluent2.microsoft.design/color)).

**Determine cada cor em fundo claro e em fundo escuro.** Antes de aplicar uma cor, verifique como ela se comporta nas duas luminâncias de fundo, porque um elemento pode cair numa superfície diferente da habitual ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). Para saber se um fundo é claro ou escuro, veja a cor de texto prevista para ele: texto escuro indica fundo claro ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

**Nunca dependa só da cor.** Junte a cor a um rótulo, um ícone ou uma forma. As mensagens do Trama trazem ícone e título; o link é sublinhado; o campo inválido ganha borda de `--stroke-thick` e mensagem de erro. Pessoas com daltonismo têm dificuldade com pares como vermelho e verde ([HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)), e um teste simples é ver a tela em tons de cinza ([One UI](https://developer.samsung.com/one-ui/accessibility/color-contrast.html)). Esse é o critério WCAG 2.2, 1.4.1.

**Use o foco só para foco.** `--t-focus` é azul, diferente da marca, para que o anel apareça sobre qualquer componente, inclusive um botão primário ([GOV.UK](https://design-system.service.gov.uk/styles/colour/)).

**Não crie matizes por sobreposição.** Uma camada colorida translúcida sobre outra cor gera um tom que não existe na paleta. Camadas de estado usam a cor do primeiro plano do próprio elemento, e a marca usa tokens pré-calculados (veja Estados de interação). O gov.br faz a mesma recomendação para seus overlays ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)).

### Contraste

O Trama cumpre o nível AA da WCAG 2.2 em todo par previsto: 4,5:1 para texto normal (1.4.3) e 3:1 para texto grande, contornos e partes gráficas que identificam um controle (1.4.11). O gov.br adota o mesmo nível mínimo e publica uma tabela de contraste entre suas cores de superfície e de leitura, marcando as combinações não recomendadas ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). As matrizes abaixo seguem esse modelo. As razões foram calculadas com a fórmula de luminância relativa da WCAG a partir dos valores hexadecimais do `kit.css`.

Legenda: **AAA** passa de 7:1; **AA** passa de 4,5:1; **G** fica entre 3:1 e 4,5:1, aceito só para partes gráficas, contornos e texto a partir de Title 3 (24px); **x** fica abaixo de 3:1 e é proibido. Na coluna `--t-border-control`, G é suficiente.

| Superfície / primeiro plano | `--t-fg-1` | `--t-fg-2` | `--t-fg-3` | `--t-brand` | `--t-link` | `--t-danger` | `--t-warning` | `--t-success` | `--t-info` | `--t-on-brand` | `--t-border-control` |
|-----------------------------|------------|------------|------------|-------------|------------|--------------|---------------|---------------|------------|----------------|----------------------|
| `--t-bg`                    | AAA 17,65  | AAA 9,56   | AA 6,10    | AA 6,04     | AA 6,04    | AA 5,85      | AA 5,93       | AA 5,38       | AA 6,09    | x              | G 3,15               |
| `--t-surface-1`             | AAA 16,46  | AAA 8,91   | AA 5,68    | AA 5,64     | AA 5,64    | AA 5,46      | AA 5,53       | AA 5,02       | AA 5,68    | x              | x                    |
| `--t-surface-2`             | AAA 15,45  | AAA 8,37   | AA 5,34    | AA 5,29     | AA 5,29    | AA 5,12      | AA 5,19       | AA 4,71       | AA 5,33    | x              | x                    |
| `--t-brand-subtle`          | AAA 15,33  | AAA 8,30   | AA 5,29    | AA 5,25     | AA 5,25    | AA 5,08      | AA 5,15       | AA 4,68       | AA 5,29    | x              | x                    |
| `--t-danger-subtle`         | AAA 15,31  | AAA 8,29   | AA 5,29    | AA 5,24     | AA 5,24    | AA 5,08      | AA 5,14       | AA 4,67       | AA 5,28    | x              | x                    |
| `--t-warning-subtle`        | AAA 16,15  | AAA 8,75   | AA 5,58    | AA 5,53     | AA 5,53    | AA 5,36      | AA 5,42       | AA 4,93       | AA 5,57    | x              | x                    |
| `--t-success-subtle`        | AAA 15,54  | AAA 8,42   | AA 5,37    | AA 5,32     | AA 5,32    | AA 5,16      | AA 5,22       | AA 4,74       | AA 5,36    | x              | x                    |
| `--t-info-subtle`           | AAA 15,38  | AAA 8,33   | AA 5,31    | AA 5,27     | AA 5,27    | AA 5,10      | AA 5,17       | AA 4,69       | AA 5,31    | x              | x                    |
| `--t-warning-fill`          | AAA 9,32   | AA 5,05    | G 3,22     | G 3,19      | G 3,19     | G 3,09       | G 3,13        | x             | G 3,22     | x              | x                    |
| `--t-brand`                 | x          | x          | x          | x           | x          | x            | x             | x             | x          | AA 6,04        | x                    |

Tema claro (`--t-surface-raised` é igual a `--t-bg`)

| Superfície / primeiro plano | `--t-fg-1` | `--t-fg-2` | `--t-fg-3` | `--t-brand` | `--t-link` | `--t-danger` | `--t-warning` | `--t-success` | `--t-info` | `--t-on-brand` | `--t-border-control` |
|-----------------------------|------------|------------|------------|-------------|------------|--------------|---------------|---------------|------------|----------------|----------------------|
| `--t-bg`                    | AAA 18,79  | AAA 11,36  | AAA 7,35   | AAA 8,67    | AAA 10,34  | AAA 8,23     | AAA 12,27     | AAA 9,91      | AAA 8,99   | x              | AA 5,09              |
| `--t-surface-1`             | AAA 17,30  | AAA 10,46  | AA 6,77    | AAA 7,98    | AAA 9,52   | AAA 7,58     | AAA 11,30     | AAA 9,12      | AAA 8,28   | x              | AA 4,69              |
| `--t-surface-2`             | AAA 15,62  | AAA 9,45   | AA 6,11    | AAA 7,21    | AAA 8,60   | AA 6,84      | AAA 10,20     | AAA 8,24      | AAA 7,48   | x              | G 4,23               |
| `--t-surface-raised`        | AAA 16,41  | AAA 9,92   | AA 6,42    | AAA 7,57    | AAA 9,03   | AAA 7,19     | AAA 10,71     | AAA 8,65      | AAA 7,85   | x              | G 4,45               |
| `--t-brand-subtle`          | AAA 14,10  | AAA 8,53   | AA 5,52    | AA 6,50     | AAA 7,76   | AA 6,18      | AAA 9,21      | AAA 7,44      | AA 6,75    | x              | G 3,82               |
| `--t-danger-subtle`         | AAA 16,00  | AAA 9,68   | AA 6,26    | AAA 7,38    | AAA 8,81   | AAA 7,01     | AAA 10,45     | AAA 8,44      | AAA 7,66   | x              | G 4,34               |
| `--t-warning-subtle`        | AAA 14,48  | AAA 8,76   | AA 5,67    | AA 6,68     | AAA 7,97   | AA 6,34      | AAA 9,46      | AAA 7,64      | AA 6,93    | x              | G 3,92               |
| `--t-success-subtle`        | AAA 14,33  | AAA 8,67   | AA 5,61    | AA 6,61     | AAA 7,89   | AA 6,28      | AAA 9,36      | AAA 7,56      | AA 6,86    | x              | G 3,88               |
| `--t-info-subtle`           | AAA 15,54  | AAA 9,40   | AA 6,08    | AAA 7,17    | AAA 8,55   | AA 6,81      | AAA 10,15     | AAA 8,20      | AAA 7,44   | x              | G 4,21               |
| `--t-warning-fill`          | x          | x          | x          | x           | x          | x            | x             | x             | x          | AAA 11,11      | x                    |
| `--t-brand`                 | x          | x          | x          | x           | x          | x            | x             | x             | x          | AAA 7,85       | x                    |

Tema escuro

Outros pares: `--t-on-brand` sobre `--t-brand-pressed` tem 10,63:1 e 10,86:1; o rótulo do botão destrutivo, 5,85:1 e 8,23:1; o ícone \#15191E sobre `--t-warning-fill`, 9,32:1 e 11,53:1; `.tr-mark`, 15,57:1 e 8,10:1.

#### Combinações proibidas

**Não coloque controles com contorno direto sobre `--t-surface-1` ou `--t-surface-2` no tema claro.** O contorno `--t-border-control` cai para 2,93:1 e 2,75:1, abaixo do critério 1.4.11. Ponha o grupo de campos, checkbox e botões neutros numa área `--t-bg` ou `--t-surface-raised`, onde o contorno tem 3,15:1.

**Nunca use `--t-warning-fill` como cor de texto.** O amarelo tem 1,89:1 contra `--t-bg` no claro. Use-o como preenchimento e escreva o texto em `--t-fg-1` ou `--t-warning`.

**Use sobre `--t-brand` apenas `--t-on-brand`.** Qualquer outro token de leitura fica abaixo de 3:1 sobre a marca.

**Trate as bordas leves como decoração.** `--t-border-subtle` (1,28:1 no claro) e `--t-border` (1,58:1) só aparecem onde o componente continua compreensível sem a linha. O DKFDS separa da mesma forma linhas com significado e linhas decorativas ([DKFDS](https://designsystem.dk/styleguide/borders/)).

**Aceite o baixo contraste só no estado desabilitado.** `--t-fg-disabled` tem 2,61:1 no claro e 3,13:1 no escuro. A WCAG isenta componentes inativos do critério 1.4.3, e o gov.br também excetua o desabilitado das regras de contraste ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

**Dentro de `.tr-inverse`, use os mesmos tokens.** O contexto invertido redefine superfície, leitura, interação e aviso com os valores do tema escuro, então os pares da matriz escura valem ali. Detalhes em Modo escuro.

> **Divergência entre referências** O gov.br usa \#333333 para texto sobre fundo claro, com 12,63:1 sobre o branco, por considerar o tom mais leve para a leitura ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). O Trama mantém `--t-fg-1` em \#15191E, com 17,65:1. Pelo critério de acessibilidade, vence a opção com mais margem, e o texto do Trama continua sem preto puro.

### Novas cores

**Use só as cores da paleta.** Um produto não cria tokens alias nem valores soltos. O gov.br exige que toda cor nova passe por teste de acessibilidade e por aprovação prévia da equipe de design do sistema ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). O Trama adota o mesmo processo:

1.  Diga a função da cor e por que nenhum token existente serve.
2.  Proponha os valores claro e escuro e o comportamento em `.tr-inverse`.
3.  Numere o token global pela luminância e calcule a nova linha ou coluna das matrizes nos dois temas.
4.  Envie à equipe do Trama. A cor entra no `kit.css` e no histórico só depois de aprovada.

### Considerações por plataforma

#### Web desktop

Teste as cores em diferentes condições de luz e dispositivos ([HIG](https://developer.apple.com/design/human-interface-guidelines/color)). Com o modo de cores forçadas (`forced-colors: active`), o navegador substitui as cores do Trama; garanta que bordas e o anel de foco usem `outline` ou `border` reais, que sobrevivem a essa substituição.

#### Web móvel

Telas de celular são usadas ao ar livre, sob luz forte. Não reduza o contraste para suavizar a interface. Use cores calmas em áreas grandes e cores vivas em áreas pequenas ([One UI](https://developer.samsung.com/one-ui/color/system.html)). Defina `<meta name="theme-color">` com o valor de `--t-bg` de cada tema.

#### Tablets e dobráveis

Diferencie painéis com superfície (`--t-surface-1` para a lista, `--t-bg` para o detalhe), sem usar a marca. Campos no painel `--t-surface-1` precisam de uma área `--t-bg` por trás.

### Recursos

#### Relacionados

- Modo escuro
- Estados de interação
- Tokens de design
- Acessibilidade
- Materiais
- Visualização de dados

#### Referências

- [Cores](https://www.gov.br/ds/fundamentos-visuais/cores) gov.br DS
- [Estados](https://www.gov.br/ds/fundamentos-visuais/estados) gov.br DS
- [Superfície](https://www.gov.br/ds/fundamentos-visuais/superficie) gov.br DS
- [Color](https://developer.apple.com/design/human-interface-guidelines/color) Apple HIG
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) Apple HIG
- [Color](https://fluent2.microsoft.design/color) Fluent 2
- [Colour](https://design-system.service.gov.uk/styles/colour/) GOV.UK Design System
- [Farver](https://designsystem.dk/styleguide/farver/) Det Fælles Designsystem
- [Hjørner, streger, skygger](https://designsystem.dk/styleguide/borders/) Det Fælles Designsystem
- [Color system and usage](https://developer.samsung.com/one-ui/color/system.html) Samsung One UI
- [Color and contrast](https://developer.samsung.com/one-ui/accessibility/color-contrast.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                 |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Organiza os tokens em funções, troca a lista de pares por matrizes de contraste com combinações proibidas, documenta a luminância dos globais, o contexto `.tr-inverse` e o processo para novas cores. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                          |

## Modo escuro

O modo escuro usa fundos mais escuros e primeiros planos mais claros para oferecer leitura confortável em pouca luz, com a mesma hierarquia e o mesmo contraste do tema claro.

Todo produto feito com o Trama funciona nos dois temas. O tema escuro troca o valor dos tokens alias (`--t-*`) e deixa os componentes intactos: um botão primário continua usando `--t-brand` e `--t-on-brand`, e o tema decide quais cores esses nomes representam. Quem usa só tokens alias recebe o modo escuro sem trabalho extra.

O tema escuro é uma paleta própria. A Apple descreve a paleta escura como fundos mais escuros e primeiros planos mais claros, e observa que essas cores não são simples inversões das claras ([HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode)). No Trama, os neutros escurecem, a marca clareia, o texto sobre a marca passa a ser escuro e as sombras ficam mais densas. O mesmo mecanismo serve para uma faixa escura dentro do tema claro, com `.tr-inverse`.

### Boas práticas

**Siga a preferência do sistema por padrão.** O Trama lê `prefers-color-scheme` e aplica o tema correspondente sem configuração. As pessoas costumam escolher o modo escuro para todo o sistema e esperam que os apps respeitem essa escolha ([HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode)). O sistema pode alternar o tema ao longo do dia, com a página aberta.

**Ofereça um seletor de tema só quando ele resolver um problema real, com a opção Sistema como padrão.** A Apple desaconselha uma configuração de aparência própria do app, porque obriga a pessoa a ajustar mais de um lugar ([HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode)). Na web, porém, a pessoa pode estar num computador compartilhado. Se oferecer o controle, use três opções (Sistema, Claro, Escuro), coloque-o uma única vez, nas configurações ou no rodapé, e não o reduza a um switch. O Geist segue esse desenho no seu Theme Switcher ([Geist](https://vercel.com/geist/theme-switcher)). No código, a escolha manual vira `data-theme="light"` ou `data-theme="dark"` no elemento `html`.

**Use apenas tokens alias.** Um valor hexadecimal fixo não muda com o tema e produz texto escuro sobre fundo escuro ([HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode)). Quando uma cor precisa ser fixa, documente o motivo. É o caso do ícone da mensagem de alerta, que usa \#15191E nos dois temas porque fica sempre sobre o amarelo de `--t-warning-fill` (9,32:1 no claro e 11,53:1 no escuro).

**Mantenha o contraste em ambos os temas.** A Apple fixa 4,5:1 como mínimo e recomenda 7:1 em cores personalizadas, especialmente em texto pequeno ([HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode)). No escuro, `--t-fg-1` tem 16,57:1 sobre `--t-bg`, `--t-fg-2` tem 11,36:1 e `--t-fg-3` tem 7,35:1. As matrizes completas estão em Cor.

**Troque também as cores de interação.** Link, link visitado e foco têm valores próprios no escuro, porque o tom do tema claro perde legibilidade sobre fundo escuro. O gov.br faz o mesmo com a cor de interação, o foco e o link visitado ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

**Reforce as camadas de estado.** No escuro, `--o-hover` passa de 0,16 para 0,30 e `--o-pressed` de 0,45 para 0,65. Uma camada fraca não aparece sobre fundo de pouco brilho; o gov.br descreve a opacidade do estado como inversamente proporcional ao brilho do fundo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Veja Estados de interação.

**Expresse profundidade com superfícies mais claras.** Sombras quase não aparecem sobre fundos escuros. Por isso `--t-surface-raised` (#1B2025) é mais claro que `--t-bg` (#0F1215), e cards, menus e diálogos se destacam pela luminosidade. A Apple usa a mesma ideia com fundos base e elevados ([HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode)), e o Geist pede para confirmar a separação nos dois temas ([Geist](https://vercel.com/geist/materials)).

**Evite o preto puro no fundo.** O fundo escuro do Trama é \#0F1215, para que superfícies elevadas fiquem visivelmente mais claras que a base. O texto principal é branco (#FFFFFF).

> **Divergência entre referências** O gov.br usa branco puro (#FFFFFF) como cor de leitura sobre fundo escuro ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). A versão 1.0 do Trama usava \#EEF1F4, com 16,57:1 sobre `--t-bg`, contra 18,79:1 do branco. Pelo critério de acessibilidade, o branco tem mais margem, e o Trama adotou \#FFFFFF em `--t-fg-1` no tema escuro na versão 1.1. Use sempre o token, nunca o valor fixo.

**Suavize imagens com fundo branco.** Uma foto com fundo branco brilha num contexto escuro. Escureça levemente a imagem ou use uma versão própria para o tema ([HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode)). O One UI também alerta que imagens podem parecer bruscas no modo escuro ([One UI](https://developer.samsung.com/one-ui/color/theme.html)).

**Teste antes de publicar.** O One UI pede testes nos dois modos antes de cada lançamento ([One UI](https://developer.samsung.com/one-ui/color/theme.html)). Inclua o modo de alto contraste do sistema e a redução de transparência, isolados e combinados ([HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode)).

### Fundo escuro dentro do tema claro

Rodapés, faixas de destaque e áreas de marca podem ser escuros numa página clara. O gov.br prevê isso: um elemento pode estar sobre fundo claro ou escuro independentemente do tema escolhido, e os estados mudam conforme o fundo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). No Trama, envolva a região em `.tr-inverse`. A classe redefine os tokens de superfície, leitura, interação, foco e opacidade de estado para os valores escuros, aplica `--t-bg` como fundo e declara `color-scheme: dark`.

**Use `.tr-inverse` em vez de cores escuras soltas.** A classe garante que texto, links, foco e camadas de estado tenham os mesmos contrastes do tema escuro: `--t-link` com 10,34:1 e `--t-focus` com 8,99:1 sobre o fundo.

**Use as cores de aviso normalmente dentro de `.tr-inverse`.** A classe redefine também `--t-danger`, `--t-warning`, `--t-success`, `--t-info` e os seus `-subtle` e `-border` com os valores do tema escuro, então mensagens, badges e botões destrutivos mantêm o contraste da matriz escura em Cor. Mesmo assim, prefira mostrar avisos importantes fora de faixas decorativas, onde a pessoa espera encontrá-los.

**Prefira neutros a fundos na cor da marca.** O gov.br usa tons escuros da sua cor institucional como superfície escura ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). O Trama usa o neutro \#0F1215 em `.tr-inverse`, porque fundos grandes na cor da marca enfraquecem a hierarquia ([Fluent](https://fluent2.microsoft.design/color)) e porque o azul-tinta fica reservado para interação.

### Como os tokens mudam

| Token                                   | Claro               | Escuro e `.tr-inverse`                            | O que muda                                       |
|-----------------------------------------|---------------------|---------------------------------------------------|--------------------------------------------------|
| `--t-bg`                                | \#FFFFFF            | \#0F1215                                          | Base mais escura da pilha                        |
| `--t-surface-raised`                    | \#FFFFFF            | \#1B2025                                          | Fica mais clara que a base para indicar elevação |
| `--t-fg-1`                              | \#15191E            | \#FFFFFF                                          | Texto principal claro                            |
| `--t-border-control`                    | \#8A929C            | \#7D8691                                          | Mantém o contorno de controles acima de 3:1      |
| `--t-brand`                             | \#0E6E6E            | \#4FC1BC                                          | A marca clareia para manter contraste            |
| `--t-brand-hover` e `--t-brand-pressed` | Mais escuros        | Mais claros                                       | A direção do estado se inverte                   |
| `--t-on-brand`                          | \#FFFFFF            | \#06201F                                          | Texto sobre a marca passa a ser escuro           |
| `--t-focus`                             | \#1A5FD0            | \#8AB4FF                                          | Anel de foco mais claro                          |
| `--o-hover` e `--o-pressed`             | 0,16 e 0,45         | 0,30 e 0,65                                       | Camadas de estado mais fortes                    |
| `--t-danger`, `--t-success`, `--t-info` | Saturados e escuros | Mais claros e menos saturados (só no tema escuro) | Legíveis sobre fundo escuro                      |
| `--t-shadow-key` e `--t-shadow-ambient` | 0,14 e 0,12         | 0,40 e 0,30 (só no tema escuro)                   | Sombras continuam perceptíveis                   |
| `--t-overlay`                           | rgba(15,18,21,.48)  | rgba(0,0,0,.64) (só no tema escuro)               | Véu mais opaco atrás de modais                   |

As cores de aviso ganham luminosidade e perdem saturação no tema escuro. O Fluent ajusta suas cores compartilhadas da mesma forma para reduzir o cansaço visual ([Fluent](https://fluent2.microsoft.design/color)).

**Faça** use `--t-danger`, `--t-danger-subtle`, `--t-brand` e `--t-on-brand`. Os valores se ajustam a cada tema.

**Não faça** fixe valores hexadecimais. No tema escuro, o vermelho e o azul-tinta do tema claro perdem contraste com o fundo.

### Implementação

O `kit.css` define os valores escuros duas vezes: dentro de `@media (prefers-color-scheme: dark)`, válido quando a página não forçou o tema claro, e em `:root[data-theme="dark"]`, para a escolha manual. Os dois blocos declaram `color-scheme: dark`, o que faz o navegador desenhar barras de rolagem, campos nativos e a seleção de texto no tema certo.

``` code
<!-- Segue o sistema (padrão) -->
<html lang="pt-BR">

<!-- Escolha manual da pessoa -->
<html lang="pt-BR" data-theme="dark">

<!-- Faixa escura dentro do tema claro -->
<div class="tr-inverse"><footer class="tr-footer">…</footer></div>
```

Aplique a escolha salva antes da primeira pintura da página para evitar um clarão no tema errado. Para imagens com versões distintas, use `<picture>` com `<source media="(prefers-color-scheme: dark)">`. No tema escuro, `.tr-inverse` não muda nada, porque os valores já são os escuros.

### Considerações por plataforma

#### Web desktop

Em uso prolongado, como painéis abertos o dia inteiro, o tema escuro reduz o brilho total da tela. Garanta que tabelas densas não dependam das linhas divisórias: `--t-border-subtle` escuro (#2A3037) é propositalmente discreto.

#### Web móvel

Declare `<meta name="theme-color">` duas vezes, uma por `media="(prefers-color-scheme: ...)"`, para que a barra do navegador acompanhe o fundo. O modo escuro reduz o brilho em ambientes noturnos ([One UI](https://developer.samsung.com/one-ui/color/theme.html)).

#### Tablets e dobráveis

Em dobráveis, a pessoa alterna entre a tela externa e a interna com frequência. O tema deve ser idêntico nas duas e não pode piscar durante a troca. Em layouts de vários painéis, diferencie os painéis por superfície (`--t-surface-1` e `--t-bg`), pois sombras entre painéis quase não aparecem no escuro.

### Recursos

#### Relacionados

- Cor
- Estados de interação
- Elevação
- Materiais
- Rodapé
- Configurações

#### Referências

- [Cores](https://www.gov.br/ds/fundamentos-visuais/cores) gov.br DS
- [Estados](https://www.gov.br/ds/fundamentos-visuais/estados) gov.br DS
- [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode) Apple HIG
- [Color](https://fluent2.microsoft.design/color) Fluent 2
- [Theme](https://developer.samsung.com/one-ui/color/theme.html) Samsung One UI
- [Theme Switcher](https://vercel.com/geist/theme-switcher) Geist
- [Materials](https://vercel.com/geist/materials) Geist

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                             |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o contexto escuro dentro do tema claro com `.tr-inverse` e seus limites, as opacidades de estado por tema e registra a divergência sobre o branco puro. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                      |

## Tokens de design

Tokens são decisões de design com nome: guardam cor, tipografia, espaçamento, forma, elevação e movimento num só lugar, para que design e código falem a mesma língua.

Tokens substituem valores fixos, como pixels e códigos hexadecimais, por nomes compartilhados entre design e engenharia. Com eles, uma mudança feita uma vez chega a todos os produtos, e temas como claro, escuro e alto contraste viram troca de valores ([Fluent 2](https://fluent2.microsoft.design/design-tokens)). No Trama, os tokens são propriedades personalizadas de CSS definidas em `kit.css`, como no HDS ([HDS](https://hds.hel.fi/foundation/design-tokens/colour)).

Os tokens alias cumprem na web o papel das cores definidas pelo sistema nas plataformas da Apple, que se adaptam sozinhas quando a pessoa troca a aparência ou ativa o aumento de contraste ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)). Os alias do Trama mudam de valor entre os temas claro e escuro; ainda não há tema de alto contraste. A classe `.tr-inverse` aplica os valores escuros a um trecho do tema claro, como um rodapé.

A versão 1.1 acrescenta tokens de opacidade, camada, ícone, densidade e formulário. Opacidades e camadas seguem os valores e a organização do Padrão Digital de Governo, que define a opacidade de superfícies em sete níveis e empilha os componentes em cinco camadas, da zero à 4 ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie), [gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)).

### Três camadas

| Camada      | Prefixo                                                                                               | O que guarda                                                                                                                    | Quem usa                                     |
|-------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| Globais     | `--g-*`                                                                                               | Valores brutos, sem significado de uso: a paleta de cinzas e a escala da cor de marca.                                          | Só o próprio sistema, para definir os alias. |
| Alias       | `--t-*`, `--sp-*`, `--r-*`, `--e-*`, `--m-*`, `--c-*`, `--o-*`, `--z-*`, `--icon-*`, `--d-*`, `--f-*` | Valores com papel definido: fundo, texto, borda, marca, estados, espaçamento, opacidade, camada, ícone, densidade e formulário. | Produtos e componentes.                      |
| Componentes | `.tr-*`                                                                                               | Classes que aplicam os alias a cada parte de um componente.                                                                     | Produtos, via markup.                        |

A separação segue o modelo do Fluent 2: tokens globais são independentes de contexto e guardam valores brutos; tokens alias dão significado a esses valores e podem agrupar vários valores, como numa sombra ([Fluent 2](https://fluent2.microsoft.design/design-tokens)).

**Use só tokens alias no código de produto.** Um produto que usa `--g-grey-92` no lugar de `--t-fg-1` perde o tema escuro, porque só os alias mudam de valor entre temas.

**Faça** Referencie tokens alias.

**Não faça** Use globais ou valores fixos fora da escala.

### Nomenclatura

O nome de um alias descreve a função, para que se saiba onde aplicá-lo sem decorar o valor ([Fluent 2](https://fluent2.microsoft.design/design-tokens)). O Fluent compõe os nomes de cor por categoria, papel e nível, com variantes de estado como hover e pressed ([Fluent 2](https://fluent2.microsoft.design/color-tokens)). O Trama usa uma versão mais curta do mesmo modelo:

| Padrão                                                                    | Exemplos                                                    |
|---------------------------------------------------------------------------|-------------------------------------------------------------|
| `--g-{família}-{passo}` e `--g-{família}-dk-{passo}` para a paleta escura | `--g-grey-60`, `--g-brand-dk-70`                            |
| `--t-{papel}`                                                             | `--t-bg`, `--t-focus`, `--t-link`                           |
| `--t-{papel}-{nível}`                                                     | `--t-fg-1`, `--t-surface-2`                                 |
| `--t-{papel}-{estado ou variante}`                                        | `--t-brand-hover`, `--t-danger-subtle`, `--t-danger-border` |
| `--sp-{múltiplo de 4px × 100}`                                            | `--sp-400` = 16px, `--sp-50` = 2px                          |
| `--{categoria}-{tamanho}`                                                 | `--r-md`, `--e-4`, `--m-fast`, `--c-h-lg`                   |

Nos tokens de cor, o número de `fg` e `surface` sobe conforme a ênfase diminui: `--t-fg-1` é o texto principal, `--t-fg-3` o texto de apoio. A paleta global segue a lógica do Geist, em que passos diferentes de uma escala servem a fundos, bordas e texto ([Geist](https://vercel.com/geist/colors)). O gov.br usa o mesmo princípio com outra notação: cada cor tem o nome da família e um grau de luminância, como "Blue Warm Vivid 70", e cada função (superfície, leitura, interação, aviso) indica uma cor principal e alternativas para fundo claro e escuro ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). Nos globais do Trama, como no gov.br, o número maior indica a cor mais escura: `--g-grey-92` é mais escuro que `--g-grey-60`.

### Tokens globais

| Token             | Valor    |     |
|-------------------|----------|-----|
| `--g-grey-0`      | \#FFFFFF |     |
| `--g-grey-2`      | \#F6F7F8 |     |
| `--g-grey-4`      | \#EEF0F2 |     |
| `--g-grey-8`      | \#E1E4E8 |     |
| `--g-grey-16`     | \#C9CED4 |     |
| `--g-grey-40`     | \#8A929C |     |
| `--g-grey-60`     | \#5A636E |     |
| `--g-grey-75`     | \#3E4650 |     |
| `--g-grey-92`     | \#15191E |     |
| `--g-grey-dk-0`   | \#0F1215 |     |
| `--g-grey-dk-4`   | \#171B20 |     |
| `--g-grey-dk-8`   | \#1F242A |     |
| `--g-grey-dk-16`  | \#2A3037 |     |
| `--g-grey-dk-24`  | \#3A424B |     |
| `--g-brand-10`    | \#E3F2F1 |     |
| `--g-brand-60`    | \#0E6E6E |     |
| `--g-brand-70`    | \#0B5A5A |     |
| `--g-brand-80`    | \#084646 |     |
| `--g-brand-dk-10` | \#12302F |     |
| `--g-brand-dk-60` | \#4FC1BC |     |
| `--g-brand-dk-70` | \#6FD0CB |     |
| `--g-brand-dk-80` | \#8FDCD8 |     |

### Tokens alias de cor

Cada alias tem um valor no tema claro e outro no escuro, como no Fluent, em que cada alias aponta para um global diferente por tema ([Fluent 2](https://fluent2.microsoft.design/color-tokens)). No `kit.css` 1.0, os alias guardam o valor resolvido; a coluna "Origem" indica o global correspondente quando há um. A amostra mostra o valor do tema ativo.

#### Superfícies e texto

| Token                |     | Claro              | Escuro          | Origem (claro / escuro) | Uso                                   |
|----------------------|-----|--------------------|-----------------|-------------------------|---------------------------------------|
| `--t-bg`             |     | \#FFFFFF           | \#0F1215        | grey-0 / grey-dk-0      | Fundo da página                       |
| `--t-surface-1`      |     | \#F6F7F8           | \#171B20        | grey-2 / grey-dk-4      | Áreas secundárias, barra lateral      |
| `--t-surface-2`      |     | \#EEF0F2           | \#1F242A        | grey-4 / grey-dk-8      | Hover em superfícies neutras          |
| `--t-surface-raised` |     | \#FFFFFF           | \#1B2025        | grey-0 / sem global     | Cards, menus, diálogos                |
| `--t-overlay`        |     | rgba(15,18,21,.48) | rgba(0,0,0,.64) | sem global              | Véu atrás de modais                   |
| `--t-fg-1`           |     | \#15191E           | \#FFFFFF        | grey-92 / sem global    | Texto principal                       |
| `--t-fg-2`           |     | \#3E4650           | \#C3CAD2        | grey-75 / sem global    | Texto secundário                      |
| `--t-fg-3`           |     | \#5A636E           | \#9AA3AD        | grey-60 / sem global    | Texto de apoio, legendas, placeholder |
| `--t-fg-disabled`    |     | \#9AA1AA           | \#5C646D        | sem global              | Texto de controles desabilitados      |
| `--t-border-subtle`  |     | \#E1E4E8           | \#2A3037        | grey-8 / grey-dk-16     | Divisores                             |
| `--t-border`         |     | \#C9CED4           | \#3A424B        | grey-16 / grey-dk-24    | Contorno de cards                     |
| `--t-border-control` |     | \#8A929C           | \#7D8691        | grey-40 / sem global    | Contorno de controles (3:1)           |

#### Marca, links e foco

| Token               |     | Claro    | Escuro   | Origem (claro / escuro) | Uso                                       |
|---------------------|-----|----------|----------|-------------------------|-------------------------------------------|
| `--t-brand`         |     | \#0E6E6E | \#4FC1BC | brand-60 / brand-dk-60  | Ação principal, seleção                   |
| `--t-brand-hover`   |     | \#0B5A5A | \#6FD0CB | brand-70 / brand-dk-70  | Hover da ação principal                   |
| `--t-brand-pressed` |     | \#084646 | \#8FDCD8 | brand-80 / brand-dk-80  | Ação principal pressionada                |
| `--t-brand-subtle`  |     | \#E3F2F1 | \#12302F | brand-10 / brand-dk-10  | Fundo de item selecionado, badge de marca |
| `--t-on-brand`      |     | \#FFFFFF | \#06201F | grey-0 / sem global     | Texto sobre a cor de marca                |
| `--t-link`          |     | \#0E6E6E | \#6FD0CB | brand-60 / brand-dk-70  | Links                                     |
| `--t-link-visited`  |     | \#5B3E96 | \#C3A8F2 | sem global              | Links visitados                           |
| `--t-focus`         |     | \#1A5FD0 | \#8AB4FF | sem global              | Anel de foco                              |

#### Semânticas

| Token                      |     | Claro                                                         | Escuro              | Uso                                               |
|----------------------------|-----|---------------------------------------------------------------|---------------------|---------------------------------------------------|
| `--t-danger`               |     | \#C2261B                                                      | \#FF8A80            | Texto, ícone e fundo de ações destrutivas e erros |
| `--t-danger-subtle`        |     | \#FCEBEA                                                      | \#3A1714            | Fundo de mensagens de erro                        |
| `--t-danger-border`        |     | \#E9A39D                                                      | \#7A2A24            | Borda de mensagens de erro                        |
| `--t-warning`              |     | \#8A5A00                                                      | \#FFC94D            | Texto de alerta                                   |
| `--t-warning-fill`         |     | \#F5B000                                                      | \#FFC94D            | Preenchimento de ícone de alerta                  |
| `--t-warning-subtle`       |     | \#FFF4DB                                                      | \#33280D            | Fundo de mensagens de alerta                      |
| `--t-warning-border`       |     | \#E8C46B                                                      | \#6B5216            | Borda de mensagens de alerta                      |
| `--t-success`              |     | \#1E7A3A                                                      | \#6FD08C            | Texto e ícone de sucesso                          |
| `--t-success-subtle`       |     | \#E6F4EA                                                      | \#12301C            | Fundo de mensagens de sucesso                     |
| `--t-success-border`       |     | \#9ACCA9                                                      | \#2C6B3F            | Borda de mensagens de sucesso                     |
| `--t-info`                 |     | \#1F5FBF                                                      | \#8AB4FF            | Texto e ícone informativo                         |
| `--t-info-subtle`          |     | \#E8F0FC                                                      | \#15243D            | Fundo de mensagens informativas                   |
| `--t-info-border`          |     | \#A6C1EC                                                      | \#2D4C80            | Borda de mensagens informativas                   |
| `--t-success-fill`         |     | \#1E7A3A                                                      | \#1E7A3A            | Preenchimento de ícone e indicador de sucesso     |
| `--t-info-fill`            |     | \#1F5FBF                                                      | \#1F5FBF            | Preenchimento de ícone e indicador informativo    |
| `--t-mark` / `--t-mark-fg` |     | \#FFF1B8 / \#15191E                                           | \#5C4A00 / \#FFF8DC | Realce de termo pesquisado (`.tr-mark`)           |
| `--t-overlay-text`         |     | Degradê de transparente a rgba(0,0,0,.72), de cima para baixo |                     | Legibilidade de texto sobre imagem                |
| `--t-shadow-key`           |     | rgba(0,0,0,.14)                                               | rgba(0,0,0,.40)     | Sombra direcional das elevações                   |
| `--t-shadow-ambient`       |     | rgba(0,0,0,.12)                                               | rgba(0,0,0,.30)     | Sombra difusa das elevações                       |

Sombras usam cores translúcidas para se misturar ao fundo; o Geist mostra que sombras opacas deixam um halo cinza ([Geist](https://vercel.com/geist/colors)).

`--t-overlay-text` corresponde ao overlay de legibilidade do gov.br, um degradê vertical de transparente a preto usado quando o texto sobre uma superfície não tem contraste suficiente ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)). O degradê do gov.br chega a preto opaco; o do Trama para em 72%, para que a imagem continue visível. Com qualquer imagem, meça 4.5:1 entre o texto e a área mais clara por trás dele.

### Tipografia

| Token           | Valor                                                                 |
|-----------------|-----------------------------------------------------------------------|
| `--t-font-sans` | "Inter", "Segoe UI", system-ui, -apple-system, sans-serif           |
| `--t-font-mono` | "JetBrains Mono", ui-monospace, "SFMono-Regular", Consolas, monospace |

| Classe            | Estilo        | Tamanho / altura de linha | Peso | Espaçamento |
|-------------------|---------------|---------------------------|------|-------------|
| `.tr-caption`     | Caption       | 12 / 16px                 | 400  | 0           |
| `.tr-body-sm`     | Body small    | 14 / 20px                 | 400  | 0           |
| `.tr-body`        | Body (padrão) | 16 / 24px                 | 400  | 0           |
| `.tr-body-lg`     | Body large    | 18 / 28px                 | 400  | 0           |
| `.tr-subtitle`    | Subtitle      | 20 / 28px                 | 600  | 0           |
| `.tr-title-3`     | Title 3       | 24 / 32px                 | 600  | 0           |
| `.tr-title-2`     | Title 2       | 28 / 36px                 | 600  | 0           |
| `.tr-title-1`     | Title 1       | 32 / 40px                 | 700  | -0.01em     |
| `.tr-large-title` | Large title   | 40 / 48px                 | 700  | -0.015em    |
| `.tr-display`     | Display       | 56 / 64px                 | 700  | -0.02em     |
| `.tr-mono`        | Mono          | 14 / 20px                 | 400  | 0           |

### Espaçamento

| Token      | Valor | Token       | Valor |
|------------|-------|-------------|-------|
| `--sp-0`   | 0     | `--sp-500`  | 20px  |
| `--sp-50`  | 2px   | `--sp-600`  | 24px  |
| `--sp-100` | 4px   | `--sp-800`  | 32px  |
| `--sp-150` | 6px   | `--sp-1000` | 40px  |
| `--sp-200` | 8px   | `--sp-1200` | 48px  |
| `--sp-300` | 12px  | `--sp-1600` | 64px  |
| `--sp-400` | 16px  | `--sp-2000` | 80px  |

### Forma

| Token              | Valor | Uso típico                                |
|--------------------|-------|-------------------------------------------|
| `--r-none`         | 0     | Elementos encostados nas bordas da janela |
| `--r-sm`           | 2px   | Botões internos de chips                  |
| `--r-md`           | 4px   | Padrão: botões, campos, chips             |
| `--r-lg`           | 8px   | Cards, menus, mensagens, listas           |
| `--r-xl`           | 12px  | Diálogos                                  |
| `--r-2xl`          | 16px  | Superfícies grandes de destaque           |
| `--r-pill`         | 999px | Badges, switch, campo de pesquisa         |
| `--stroke-thin`    | 1px   | Bordas de controles e divisores           |
| `--stroke-thick`   | 2px   | Anel de foco, borda de erro, checkbox     |
| `--stroke-thicker` | 3px   | Resumo de erros, spinner                  |

### Elevação

| Token   | Valor                            | Uso                      |
|---------|----------------------------------|--------------------------|
| `--e-1` | 0 0 2px ambient, 0 1px 2px key   | Segmento selecionado     |
| `--e-2` | 0 0 2px ambient, 0 2px 4px key   | Card elevado             |
| `--e-3` | 0 0 2px ambient, 0 4px 8px key   | Hover de card interativo |
| `--e-4` | 0 0 2px ambient, 0 8px 16px key  | Menus, popovers, toasts  |
| `--e-5` | 0 0 8px ambient, 0 14px 28px key | Drawers                  |
| `--e-6` | 0 0 8px ambient, 0 32px 64px key | Diálogos                 |

"ambient" e "key" correspondem a `--t-shadow-ambient` e `--t-shadow-key`. Veja Elevação.

### Movimento

| Token               | Valor                  | Uso                                 |
|---------------------|------------------------|-------------------------------------|
| `--m-fast`          | 100ms                  | Mudança de cor em hover e pressed   |
| `--m-normal`        | 200ms                  | Switch, acordeão, sombra de card    |
| `--m-slow`          | 300ms                  | Entrada de drawers e diálogos       |
| `--m-slower`        | 500ms                  | Transições de página                |
| `--m-ease-standard` | cubic-bezier(.2,0,0,1) | Movimento dentro da tela            |
| `--m-ease-enter`    | cubic-bezier(0,0,0,1)  | Elementos que entram (desacelera)   |
| `--m-ease-exit`     | cubic-bezier(.3,0,1,1) | Elementos que saem (acelera)        |
| `--m-linear`        | linear                 | Indicadores contínuos, como spinner |

### Controles

| Token       | Valor | Uso                                               |
|-------------|-------|---------------------------------------------------|
| `--c-h-sm`  | 32px  | Controles compactos, barras de ferramentas densas |
| `--c-h-md`  | 40px  | Altura padrão de botões e campos                  |
| `--c-h-lg`  | 48px  | Ação principal em telas de toque                  |
| `--c-touch` | 44px  | Área mínima de toque                              |

### Opacidade

A escala de opacidade tem os mesmos sete valores dos tokens de opacidade de superfície do gov.br, que vão de 0 a 1 e servem para deixar transparecer o que está atrás e para criar overlays ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)).

| Token                      | Valor                               | Uso no Trama                                                                        |
|----------------------------|-------------------------------------|-------------------------------------------------------------------------------------|
| `--o-none`                 | 0                                   | Camada invisível                                                                    |
| `--o-xs`                   | 0,16                                | Hover no tema claro; zona de soltura ativa                                          |
| `--o-sm`                   | 0,30                                | Hover no tema escuro                                                                |
| `--o-md`                   | 0,45                                | Pressionado no tema claro                                                           |
| `--o-lg`                   | 0,65                                | Pressionado no tema escuro; véu de região em carregamento                           |
| `--o-xl`                   | 0,85                                | Elemento sendo arrastado                                                            |
| `--o-full`                 | 1                                   | Opaco                                                                               |
| `--o-hover`, `--o-pressed` | xs e md no claro; sm e lg no escuro | Camada de estado: cor do primeiro plano do elemento, nesta opacidade, sobre o fundo |

**Use a camada de estado, não cores novas, para hover e pressionado.** A camada usa a cor do primeiro plano do próprio elemento, por isso funciona sobre qualquer fundo. A exceção é a marca, que usa os valores pré-calculados `--t-brand-hover` e `--t-brand-pressed`. O gov.br alerta que um overlay colorido sobre uma superfície de outra cor gera tonalidades novas que distorcem a identidade visual ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)). Veja Estados de interação.

### Camadas

As camadas são planos imaginários sem espessura; a função do componente define a camada, e a camada define a sombra ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)). O Trama adota a mesma distribuição de componentes por camada do gov.br.

| Token   | Valor | Componentes                                                    | Elevação no kit  |
|---------|-------|----------------------------------------------------------------|------------------|
| `--z-0` | 0     | Conteúdo, formulários, ações, tabelas, mensagens, rodapé       | Sem sombra       |
| `--z-1` | 100   | Cabeçalho, cards elevados, bordas de áreas com rolagem         | `--e-1`, `--e-2` |
| `--z-2` | 200   | Flutuantes de baixa prioridade: menus, seletores, notificações | `--e-4`          |
| `--z-3` | 300   | Navegação flutuante e cabeçalho fixo                           | `--e-3`, `--e-5` |
| `--z-4` | 400   | Diálogo, tooltip, carregamento bloqueante                      | `--e-6`          |

**Não use valores de `z-index` fora da escala.** Itens de uma mesma camada não ocupam o mesmo espaço na tela, e o leitor de tela prioriza o conteúdo da camada mais alta, como um diálogo aberto ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)).

> **Divergência entre referências** O gov.br põe o cookiebar na camada 4, com scrim opcional sobre a página ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao), [gov.br DS](https://www.gov.br/ds/components/cookiebar)). O GOV.UK proíbe o banner fixo por causa do critério 2.4.11 da WCAG 2.2 ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)). No Trama, o aviso de cookies fica no fluxo da página, em `--z-0`. Veja Consentimento de cookies.

### Ícones

| Token        | Valor | Uso                                                         |
|--------------|-------|-------------------------------------------------------------|
| `--icon-xs`  | 12px  | Só informativo, junto a Caption; nunca interativo           |
| `--icon-sm`  | 16px  | Junto a Body small, badges e metadados; botões `--c-h-sm`   |
| `--icon-md`  | 20px  | Botões `--c-h-md`, itens de menu, ícone de mensagens        |
| `--icon-lg`  | 24px  | Padrão: navegação, barras de ferramentas, botões `--c-h-lg` |
| `--icon-xl`  | 32px  | Destaques em cards e listas                                 |
| `--icon-2xl` | 48px  | Estados vazios pequenos                                     |
| `--icon-3xl` | 64px  | Máximo; acima disso, use ilustração                         |

Regras de uso em Iconografia.

### Densidade

O atributo `data-density` troca os valores dos tokens `--d-*` num contêiner, em passos de 4px, como na escala de densidade do gov.br ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)).

| Token         | Alta | Padrão | Baixa | Uso                                  |
|---------------|------|--------|-------|--------------------------------------|
| `--d-control` | 32px | 40px   | 48px  | Altura de botões e campos            |
| `--d-pad-x`   | 12px | 16px   | 24px  | Espaço interno horizontal            |
| `--d-pad-y`   | 8px  | 12px   | 16px  | Espaço interno vertical              |
| `--d-gap`     | 8px  | 12px   | 16px  | Espaço entre itens                   |
| `--d-row`     | 44px | 56px   | 64px  | Altura mínima de itens de lista      |
| `--d-cell-y`  | 6px  | 12px   | 16px  | Espaço vertical de células de tabela |

A densidade baixa é obrigatória em toque e na classe Compacta; a alta só vale com mouse ou trackpad, em tabelas, listas longas e ferramentas, e nunca em alertas e mensagens. Veja Densidade.

### Formulário

O gov.br pede espaços constantes por função em todo o produto: maior entre grupos e antes dos botões, intermediário entre o título e o primeiro campo, menor entre campos ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). O Trama transforma esses espaços em tokens.

| Token             | Valor              | Entre                                         |
|-------------------|--------------------|-----------------------------------------------|
| `--f-gap-title`   | 16px (`--sp-400`)  | Título ou legenda do grupo e o primeiro campo |
| `--f-gap-field`   | 24px (`--sp-600`)  | Um campo e o seguinte                         |
| `--f-gap-actions` | 32px (`--sp-800`)  | O último campo e os botões                    |
| `--f-gap-group`   | 40px (`--sp-1000`) | Um grupo de campos e o seguinte               |

> **Divergência entre referências** No gov.br, o espaço entre o título e o primeiro campo é intermediário, maior que o espaço entre campos ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). O Trama segue a ordem do gov.br para grupos, botões e campos (40, 32 e 24px) e usa um espaço menor sob o título, para que ele fique ligado ao grupo que nomeia. Nenhuma referência cita pesquisa sobre esse valor; a decisão pode mudar com testes.

### Boas práticas

**Não crie valores fora da escala.** Se um layout pede 14px de espaço, escolha `--sp-300` ou `--sp-400`. Um valor novo só entra no sistema quando vários produtos precisam dele.

**Use tokens também para opacidade, camada e espaço de formulário.** Margens de segurança vizinhas não se somam: vale a maior.

**Escolha o token pelo papel do elemento.** Um divisor usa `--t-border-subtle` mesmo que `--t-surface-2` pareça igual no tema claro; no escuro, os dois têm valores diferentes.

**Teste cada combinação nos dois temas.** Mesmo com tokens bem nomeados, meça o contraste de cada combinação nova ([HDS](https://hds.hel.fi/foundation/design-tokens/colour)). Veja os pares aprovados em Acessibilidade.

**Trate mudança de valor como mudança de versão.** No HDS, alterar o valor de um token de cor é uma mudança incompatível ([HDS](https://hds.hel.fi/getting-started/versioning)). O Trama segue versionamento semântico: renomear ou remover tokens e mudar valores de cor exige nova versão maior; adicionar tokens é versão menor.

### Considerações por plataforma

#### Web desktop

Nenhuma consideração adicional para Web desktop.

#### Web móvel

Aplique `data-density="baixa"` na classe Compacta e garanta `--c-touch` em todo alvo. As margens de layout por classe de janela (16, 24, 32, 40 e 48px) correspondem a `--sp-400`, `--sp-600`, `--sp-800`, `--sp-1000` e `--sp-1200`.

#### Tablets e dobráveis

Os tokens não mudam por plataforma. O que muda é a densidade: em tablets usados com toque, use a densidade baixa; com teclado e trackpad conectados, a padrão, e a alta só em tabelas e ferramentas.

### Recursos

#### Relacionados

- Cor
- Modo escuro
- Tipografia
- Espaçamento
- Formas e bordas
- Elevação
- Movimento
- Marca
- Estados de interação
- Densidade
- Iconografia
- CSS e tokens no código

#### Referências

- [Cores](https://www.gov.br/ds/fundamentos-visuais/cores) gov.br DS
- [Superfície](https://www.gov.br/ds/fundamentos-visuais/superficie) gov.br DS
- [Elevação](https://www.gov.br/ds/fundamentos-visuais/elevacao) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Cookiebar](https://www.gov.br/ds/components/cookiebar) gov.br DS
- [Cookie banner](https://design-system.service.gov.uk/components/cookie-banner/) GOV.UK Design System
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) Apple HIG
- [Design tokens](https://fluent2.microsoft.design/design-tokens) Fluent 2
- [Color tokens](https://fluent2.microsoft.design/color-tokens) Fluent 2
- [Colour](https://hds.hel.fi/foundation/design-tokens/colour) Helsinki Design System
- [Colour tokens](https://hds.hel.fi/foundation/design-tokens/colour/tokens) Helsinki Design System
- [Versioning](https://hds.hel.fi/getting-started/versioning) Helsinki Design System
- [Colors](https://vercel.com/geist/colors) Geist

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta os tokens de opacidade, camada, ícone, densidade e formulário, os tokens de cor de realce, preenchimento e overlay de texto, e a classe `.tr-inverse`, com as divergências sobre camada do aviso de cookies e espaço sob o título de formulário. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                                               |

## Elevação

A elevação usa camadas, sombra e luminosidade para mostrar o que está à frente, o que está atrás e o que pede atenção agora.

Elevação é a distância percebida entre um objeto e a superfície atrás dela. Quanto mais alto o objeto, mais importância e foco ele recebe ([Fluent](https://fluent2.microsoft.design/elevation)). O gov.br acrescenta que a função do componente define a camada onde ele fica, e a camada define a sombra ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)). O Trama organiza a interface em cinco camadas, de `--z-0` a `--z-4`, e expressa a altura com seis sombras, de `--e-1` a `--e-6`.

Cada sombra combina duas partes, como no Fluent: uma sombra-chave, nítida e direcional, que define as bordas do elemento, e uma sombra ambiente, suave e difusa, que sugere distância ([Fluent](https://fluent2.microsoft.design/elevation)). As cores são `--t-shadow-key` e `--t-shadow-ambient`, que mudam com o tema. Para véus e superfícies translúcidas, veja Materiais.

### Camadas

Cada camada tem um token de `z-index` e uma faixa de sombra. A divisão segue o gov.br, que define cinco camadas numeradas de zero a quatro, e cada uma projeta uma sombra mais intensa que a anterior ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)).

| Camada  | `z-index` | O que fica nela                                                                                                      | Sombra                                                             |
|---------|-----------|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| `--z-0` | 0         | Conteúdo, formulários, botões, links, tabelas, listas, mensagens, abas, rodapé                                       | Nenhuma                                                            |
| `--z-1` | 100       | Cabeçalho, cards elevados, bordas de áreas com rolagem                                                               | `--e-1` a `--e-3`                                                  |
| `--z-2` | 200       | Flutuantes de baixa prioridade: menus, popovers, seletores de data e hora, listas de combobox, toasts e notificações | `--e-4`                                                            |
| `--z-3` | 300       | Navegação flutuante: cabeçalho fixo, drawer de navegação, barra inferior fixa                                        | `--e-3` nas barras presas à borda, `--e-5` no drawer               |
| `--z-4` | 400       | Diálogos, drawers modais, tooltip, carregamento que bloqueia a tela                                                  | `--e-5` e `--e-6`; o tooltip usa fundo invertido e dispensa sombra |

**Escolha a camada pela função, e depois a sombra.** Um menu aberto dentro de um diálogo continua sendo um flutuante e usa `--e-4`; ele não herda `--e-6`. O DKFDS dá o mesmo exemplo com um tooltip dentro de um modal ([DKFDS](https://designsystem.dk/styleguide/borders/)). No código, a camada vem do contexto de empilhamento: o menu fica acima do diálogo que o contém.

**Mantenha a sombra coerente com a camada.** Um elemento com sombra maior fica acima de um elemento com sombra menor ([Geist](https://vercel.com/geist/materials)). A única exceção são as barras presas a uma borda da tela, como o cabeçalho fixo: elas projetam sombra para um só lado e usam `--e-3` mesmo na camada 3.

**Não sobreponha itens da mesma camada.** Dois elementos na mesma camada não ocupam o mesmo espaço da tela ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)). Se dois toasts precisam aparecer, empilhe-os lado a lado ou um sobre o outro, sem cobrir.

### Escala de sombras

| Token   | Desfoque da sombra-chave | Aplique em                                              |
|---------|--------------------------|---------------------------------------------------------|
| `--e-1` | 2px                      | Cabeçalho, segmento selecionado do controle segmentado  |
| `--e-2` | 4px                      | Card elevado (`.tr-card--elevated`) em repouso          |
| `--e-3` | 8px                      | Card interativo em hover, cabeçalho fixo                |
| `--e-4` | 16px                     | Menus, popovers, toasts, calendário, seletor de horário |
| `--e-5` | 28px                     | Drawers e folhas laterais                               |
| `--e-6` | 64px                     | Diálogos                                                |

Os desfoques seguem a rampa de seis sombras do Fluent (2, 4, 8, 16, 28 e 64), que atribui a 64 a diálogos e a 28 a folhas e navegação lateral ([Fluent](https://fluent2.microsoft.design/elevation)).

``` code
--e-4: 0 0 2px var(--t-shadow-ambient), 0 8px 16px var(--t-shadow-key);
--e-6: 0 0 8px var(--t-shadow-ambient), 0 32px 64px var(--t-shadow-key);
```

> **Divergência entre referências** O gov.br fixa o desfoque em 6px e a opacidade em 0,16, e varia só o deslocamento vertical da sombra (1, 3, 6 e 9px por camada) para simplificar o uso ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)). O Fluent varia desfoque e deslocamento juntos, com sombras nítidas para elementos próximos e difusas para os distantes ([Fluent](https://fluent2.microsoft.design/elevation)). Nenhuma das duas fontes traz pesquisa nem critério de acessibilidade sobre o tema, e as duas concordam no essencial: a sombra cresce com a camada. O Trama mantém a rampa do Fluent já publicada no kit.

### Boas práticas

**Use sombra só em elementos que ficam sobre outros elementos.** O conteúdo da página fica na camada 0 e se organiza com espaço, borda e superfície. O DKFDS reserva sombras para elementos sobrepostos ([DKFDS](https://designsystem.dk/styleguide/borders/)), e o gov.br pede para não usar elevação como decoração ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)).

**Escolha o nível mais baixo que ainda se destaque.** Elevação em excesso é uma fonte comum de ruído visual ([Geist](https://vercel.com/geist/materials)). Um card raramente precisa de mais que `--e-2`.

**Projete a sombra para baixo, exceto em elementos presos à borda inferior.** As sombras do Trama não têm deslocamento horizontal e caem para baixo, como se viessem de uma única fonte de luz ([Fluent](https://fluent2.microsoft.design/elevation)). Uma barra inferior fixa ou o rodapé de uma área com rolagem projetam a sombra para cima, sobre o conteúdo que passa por baixo. O gov.br permite inverter a direção para elementos nas margens da tela ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)).

**Retire a sombra ao pressionar e ao desabilitar.** Um card interativo pressionado volta ao plano e perde a sombra; um elemento desabilitado não tem sombra. O gov.br retira ou ameniza a elevação nos dois estados ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

**Mantenha as sombras discretas.** Contraste forte entre sombra e fundo tira a atenção da informação ([One UI](https://developer.samsung.com/one-ui/structure/visual-depth.html)). Não crie sombras com cores opacas ([Geist](https://vercel.com/geist/colors)).

**Use véu quando a nova camada interrompe a tarefa e só sombra quando ela continua a tarefa.** Um diálogo modal bloqueia a página e recebe o véu `--t-overlay`. Um menu ou popover continua ligado à página e usa só a sombra ([One UI](https://developer.samsung.com/one-ui/structure/visual-depth.html)).

**Não exiba vários níveis de camada ao mesmo tempo.** Um diálogo sobre um drawer sobre um menu confunde a hierarquia ([One UI](https://developer.samsung.com/one-ui/structure/visual-depth.html)). Feche a camada anterior antes de abrir outra quando possível.

### Bordas de rolagem

Quando um componente tem altura limitada e rola por dentro, o cabeçalho e o rodapé fixos sobem para a camada 1 enquanto escondem conteúdo, e ganham uma sombra curta. O gov.br chama esse comportamento de *content overflow* e o coloca na camada 1 ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)). No kit, `.tr-scroll` recebe `is-overflow-top` quando há conteúdo escondido acima e `is-overflow-bottom` quando há conteúdo abaixo.

**Mostre a sombra só enquanto houver conteúdo escondido.** No topo da lista, o cabeçalho fica sem sombra; no fim, o rodapé também. Torne a área de rolagem focável (`tabindex="0"`) e nomeada, para que quem usa teclado consiga rolar.

### Acessibilidade

**Faça a camada mais alta ser lida primeiro.** Leitores de tela não veem sombras, então a elevação precisa estar implícita na estrutura: o conteúdo das camadas mais altas tem prioridade de leitura ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/elevacao)). Ao abrir um diálogo, mova o foco para dentro dele e torne o resto da página inerte (`<dialog>` aberto com `showModal()`, ou `inert`). Ao abrir um menu ou popover, coloque-o no DOM logo depois do controle que o abriu, para que a leitura siga a ordem visual. Toasts usam regiões `aria-live`.

**Não comunique elevação só com sombra.** Uma camada sobreposta precisa de semântica (`role="dialog"`, `aria-modal`, `role="menu"`) e de foco visível nos controles internos ([Geist](https://vercel.com/geist/materials)).

### Elevação no tema escuro

No escuro, sombras perdem força. O Trama compensa de duas formas. As cores de sombra ficam mais densas: `--t-shadow-key` passa de 14% para 40% de opacidade e `--t-shadow-ambient` de 12% para 30% ([Fluent](https://fluent2.microsoft.design/elevation)). E superfícies elevadas ficam mais claras que a base: `--t-surface-raised` é \#1B2025 sobre `--t-bg` \#0F1215 ([HIG](https://developer.apple.com/design/human-interface-guidelines/dark-mode)).

### Considerações por plataforma

#### Web desktop

Com ponteiro, use a passagem de `--e-2` para `--e-3` como resposta de hover em cards interativos, com transição de `--m-normal`. Nunca use a elevação em hover como único sinal de que algo é clicável.

#### Web móvel

Sem hover, a elevação em repouso precisa bastar. Barras fixas ganham sombra só quando há conteúdo rolando por baixo, e voltam a nenhuma sombra no topo da página. A barra inferior fixa projeta a sombra para cima.

#### Tablets e dobráveis

Em layouts de vários painéis, os painéis ficam na camada 0 e se separam por divisor e superfície. Reserve a elevação para o que flutua sobre eles, como popovers abertos perto do controle que os acionou ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

### Recursos

#### Relacionados

- Materiais
- Modo escuro
- Formas e bordas
- Excesso de conteúdo
- Diálogos
- Drawers e folhas laterais
- Cabeçalho

#### Referências

- [Elevação](https://www.gov.br/ds/fundamentos-visuais/elevacao) gov.br DS
- [Estados](https://www.gov.br/ds/fundamentos-visuais/estados) gov.br DS
- [Elevation](https://fluent2.microsoft.design/elevation) Fluent 2
- [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode) Apple HIG
- [Visual depth](https://developer.samsung.com/one-ui/structure/visual-depth.html) Samsung One UI
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Hjørner, streger, skygger](https://designsystem.dk/styleguide/borders/) Det Fælles Designsystem
- [Materials](https://vercel.com/geist/materials) Geist
- [Colors](https://vercel.com/geist/colors) Geist

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta as camadas `--z-0` a `--z-4` ligadas às sombras, as bordas de rolagem elevadas, a ordem de leitura para leitores de tela, a sombra para cima em elementos presos à borda inferior e a retirada da sombra ao pressionar. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                      |

## Formas e bordas

Raios de canto e espessuras de borda consistentes tornam os componentes reconhecíveis à primeira vista e indicam o que é controle, o que é contêiner e o que está em foco.

Toda forma do Trama se define por três propriedades: o formato, o raio dos cantos e a borda. O Fluent descreve formas exatamente por esses três atributos ([Fluent](https://fluent2.microsoft.design/shapes)). O gov.br trata a mesma ideia como superfície, a forma que contém os elementos, e lista cinco propriedades combináveis: cor, borda, canto, sombra e opacidade ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)). A Apple lista formas de contêiner e linhas separadoras, ao lado do espaço vazio, entre os recursos para mostrar quais elementos estão relacionados ([HIG](https://developer.apple.com/design/human-interface-guidelines/layout)). Esta página cobre formato, canto e borda; cor está em Cor, sombra em Elevação e opacidade em Materiais.

O Trama tem um estilo contido: cantos levemente arredondados nos controles, um pouco mais arredondados nos contêineres e pílulas para trilhos e rótulos curtos. O gov.br pede consistência: se um produto arredonda as superfícies, todos os componentes que usam a mesma superfície seguem o mesmo padrão ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)).

### Formatos

| Formato     | Uso no Trama                                                                                                                            |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Retângulo   | Base de quase tudo: botões, campos, cards, menus, diálogos, tabelas, imagens                                                            |
| Círculo     | Avatares de pessoas, indicador de presença, radio, números do indicador de etapas, spinner, botão de ícone circular (`.tr-btn--circle`) |
| Pílula      | Trilhos (switch, progresso), badges, campo de pesquisa                                                                                  |
| Seta (bico) | Popovers ancorados a um único objeto                                                                                                    |

A divisão segue o Fluent: retângulo como base, círculo para pessoas, pílula para trilhos e rótulos, e bico para superfícies ligadas a um objeto ([Fluent](https://fluent2.microsoft.design/shapes)). Um avatar de grupo ou de organização usa `.tr-avatar--group`, com `--r-lg`, para que a forma diga se o item representa uma pessoa.

### Raios

| Token      | Valor            | Aplique em                                                                                     |
|------------|------------------|------------------------------------------------------------------------------------------------|
| `--r-none` | 0                | Elementos que encostam na borda da tela: barra inferior, cabeçalho, painéis lado a lado        |
| `--r-sm`   | 2px              | Elementos menores que 32px dentro de outro componente, como o botão de remover do chip         |
| `--r-md`   | 4px              | Padrão para controles: botões, campos, checkbox, chips, tooltips, itens de menu e de navegação |
| `--r-lg`   | 8px              | Contêineres: cards, menus, popovers, mensagens, toasts, tabelas, listas, rail                  |
| `--r-xl`   | 12px             | Diálogos e ilustrações de estado vazio                                                         |
| `--r-2xl`  | 16px             | Superfícies grandes de tela inteira, como folhas inferiores em celulares                       |
| `--r-pill` | Metade da altura | Badges, trilho do switch, barra de progresso, campo de pesquisa                                |

Os quatro primeiros degraus coincidem com os do Fluent, que usa 4px como padrão de retângulos e 2px para formas menores que 32px ([Fluent](https://fluent2.microsoft.design/shapes)). O gov.br publica 0, 4, 8 e 16px e a pílula ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)), todos presentes na escala do Trama.

**Calcule a pílula como metade da altura.** O raio de uma pílula é R = A / 2, em que A é a altura da superfície: um botão de 48px de altura tem raio de 24px ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)). No código, `--r-pill` usa um valor alto (999px), e o navegador limita o raio à metade do lado menor, com o mesmo resultado em qualquer altura.

### Boas práticas

**Aumente o raio com o tamanho e a elevação.** Controles pequenos usam `--r-md`; contêineres que agrupam controles usam `--r-lg`; superfícies que flutuam sobre a página inteira usam `--r-xl`. O Geist também aumenta o raio conforme a superfície sobe na hierarquia ([Geist](https://vercel.com/geist/materials)).

**Escolha o grau de arredondamento pelo tom do produto, e mantenha-o.** Cantos retos transmitem solidez e seriedade; cantos arredondados, modernidade e informalidade ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)). O Trama fixa o grau nos tokens. Um produto não troca raios por componente.

**Calcule o raio interno a partir do externo.** Quando um elemento arredondado fica dentro de outro, o raio interno é o raio externo menos o preenchimento entre eles. O `.tr-menu` tem `--r-lg` (8px) e preenchimento de `--sp-100` (4px), por isso seus itens usam `--r-md` (4px).

**Não arredonde cantos que criam vãos.** Em um botão dividido, os cantos internos entre as duas partes ficam retos, como o `.tr-split` do kit faz ([Fluent](https://fluent2.microsoft.design/shapes)).

**Use cantos retos onde o componente encontra a borda da tela.** Barras de navegação e abas que tocam a borda dispensam arredondamento ([Fluent](https://fluent2.microsoft.design/shapes)). O `.tr-card__media` arredonda só os cantos superiores, que coincidem com os do card.

**Use a pílula para trilhos e rótulos curtos.** Botões de ação ficam com `--r-md`. Pílulas em botões competem com badges e chips e enfraquecem a distinção entre ação e informação.

**Espelhe a forma final no skeleton.** Um placeholder de avatar é circular, um de botão usa `--r-md` ([Geist](https://vercel.com/geist/skeleton)).

### Bordas

| Token              | Valor | Aplique em                                                                                            |
|--------------------|-------|-------------------------------------------------------------------------------------------------------|
| `--stroke-thin`    | 1px   | Contornos de campos, botões neutros, cards, tabelas, divisores, foco tênue                            |
| `--stroke-thick`   | 2px   | Anel de foco, contorno de checkbox e radio, campo com estado de validação, área de soltar arquivos    |
| `--stroke-thicker` | 3px   | Resumo de erros, spinner, sublinhado de link em hover, indicador da aba e do item de navegação ativos |

Uma borda tem estilo, espessura, cor e lados. O Trama usa o estilo sólido em quase tudo e o tracejado só na área de soltar (`.tr-dropzone`), que comunica um lugar à espera de conteúdo. O gov.br define os mesmos quatro atributos e oferece espessuras de 0, 1, 2 e 4px ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)); o Fluent usa 1, 2 e 3px na web ([Fluent](https://fluent2.microsoft.design/shapes)). O Trama mantém 1, 2 e 3px.

**Separe bordas que comunicam de bordas que decoram.** Uma borda que a pessoa precisa ver para entender o componente, como o contorno de um campo, usa `--t-border-control`, com 3,15:1 sobre `--t-bg` no claro (WCAG 2.2, 1.4.11). Bordas decorativas usam `--t-border` ou `--t-border-subtle` e só aparecem onde o componente continua compreensível sem elas ([DKFDS](https://designsystem.dk/styleguide/borders/)).

**Use borda para separar superfícies claras do fundo.** Um card branco sobre fundo branco precisa de borda ou de sombra para existir. O gov.br recomenda a borda justamente para componentes brancos ou claros, e alerta que o excesso de bordas cria ruído e prejudica a leitura ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)).

**Desenhe cada borda uma vez.** Quando dois contêineres com borda se encostam, remova uma das bordas ou use um divisor interno. Bordas sobrepostas destacam as interseções ([Geist](https://vercel.com/geist/colors)).

**Desenhe a borda por dentro.** No navegador, com `box-sizing: border-box`, a borda fica dentro da largura do componente. Na ferramenta de design, configure traço interno, arremate projetado e junção em mitra, como o gov.br orienta ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)). Detalhes em Espaçamento.

**Engrosse a borda para indicar estado, sem mudar o tamanho do componente.** O campo inválido passa de `--stroke-thin` para `--stroke-thick` em `--t-danger`. Compense a diferença no preenchimento ou use `box-shadow` interna para que o texto não se mova.

**Use `outline` no foco.** O anel de foco é um `outline` de `--stroke-thick` em `--t-focus` com afastamento de 2px, mostrado só em `:focus-visible`. Ele acompanha o raio do componente nos navegadores atuais e continua visível no modo de cores forçadas. O foco tênue usa `--stroke-thin` (veja Estados de interação).

**Faça** use raio interno igual ao externo menos o preenchimento. O menu tem 8px e 4px de preenchimento; os itens têm 4px.

**Não faça** use a forma de badge para uma ação. A pessoa não reconhece "Enviar" como botão.

### Considerações por plataforma

#### Web desktop

Nenhuma consideração adicional para Web desktop.

#### Web móvel

Folhas inferiores e diálogos de tela cheia encostam nas bordas laterais e inferior. Arredonde só os cantos superiores, com `--r-2xl`, e deixe retos os cantos que tocam a borda da tela.

#### Tablets e dobráveis

Painéis lado a lado usam `--r-none` e um divisor de `--stroke-thin`. Cards e popovers dentro dos painéis mantêm os raios normais. Muitos tablets e dobráveis têm cantos de tela arredondados: mantenha conteúdo e controles dentro da margem da classe de janela.

### Recursos

#### Relacionados

- Elevação
- Materiais
- Cor
- Espaçamento
- Estados de interação
- Divisores

#### Referências

- [Superfície](https://www.gov.br/ds/fundamentos-visuais/superficie) gov.br DS
- [Shapes](https://fluent2.microsoft.design/shapes) Fluent 2
- [Hjørner, streger, skygger](https://designsystem.dk/styleguide/borders/) Det Fælles Designsystem
- [Materials](https://vercel.com/geist/materials) Geist
- [Colors](https://vercel.com/geist/colors) Geist
- [Skeleton](https://vercel.com/geist/skeleton) Geist
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) Apple HIG

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                               |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a fórmula da pílula, os atributos de borda, o traço interno nas ferramentas, a consistência de cantos por produto e o uso de borda em superfícies claras. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                        |

