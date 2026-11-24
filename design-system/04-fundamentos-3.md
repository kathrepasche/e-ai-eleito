# Fundamentos: Tipografia a Ilustração

## Tipografia

A tipografia do Trama garante texto legível, comunica hierarquia com poucos estilos, espaça os blocos de texto com tokens e se adapta quando a pessoa amplia o texto.

O E aí, Eleito? usa três famílias. **Space Grotesk** compõe os títulos (estilos do grupo Títulos, `font-display`). **Inter** compõe todo o resto do texto da interface, de legendas a parágrafos. **JetBrains Mono** fica reservada para código, identificadores e dados que precisam de alinhamento por caractere. A Apple recomenda minimizar o número de fontes, porque misturar muitas obscurece a hierarquia ([HIG](https://developer.apple.com/design/human-interface-guidelines/typography)), e o gov.br usa uma única família para todo o texto, com uma fonte monoespaçada só para código ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)).

A escala tem dez estilos, cada um com tamanho, altura de linha e peso definidos. As alturas de linha são múltiplos de 4px e se encaixam na grade de espaçamento, como no GOV.UK, que usa múltiplos de 5px para criar ritmo vertical ([GOV.UK](https://design-system.service.gov.uk/styles/type-scale/)).

### Escala tipográfica

| Estilo      | Classe            | Tamanho / linha | Peso | Uso                                                                           |
|-------------|-------------------|-----------------|------|-------------------------------------------------------------------------------|
| Display     | `.tr-display`     | 56 / 64         | 700  | Números e mensagens de destaque em páginas de entrada. No máximo um por tela. |
| Large title | `.tr-large-title` | 40 / 48         | 700  | Título de página em telas amplas e páginas editoriais                         |
| Title 1     | `.tr-title-1`     | 32 / 40         | 700  | Título de página (`h1`) padrão                                                |
| Title 2     | `.tr-title-2`     | 28 / 36         | 600  | Seções principais (`h2`)                                                      |
| Title 3     | `.tr-title-3`     | 24 / 32         | 600  | Subseções (`h3`)                                                              |
| Subtitle    | `.tr-subtitle`    | 20 / 28         | 600  | Títulos de diálogo, card e grupo (`h4`)                                       |
| Body large  | `.tr-body-lg`     | 18 / 28         | 400  | Parágrafo de abertura, uma vez por página                                     |
| Body        | `.tr-body`        | 16 / 24         | 400  | Texto corrido, valores de campos                                              |
| Body small  | `.tr-body-sm`     | 14 / 20         | 400  | Tabelas, menus, navegação, rótulos de campo e botão                           |
| Caption     | `.tr-caption`     | 12 / 16         | 400  | Legendas, carimbos de data, badges. Menor tamanho permitido.                  |
| Mono        | `.tr-mono`        | 14 / 20         | 400  | Código, IDs, hashes, valores técnicos                                         |

Os valores estão em px CSS para facilitar a leitura. No código, declare tamanhos em `rem`, para que o texto acompanhe o tamanho de fonte escolhido no navegador ([GOV.UK](https://design-system.service.gov.uk/styles/type-scale/)). A proporção entre altura de linha e tamanho cai à medida que o texto cresce: cerca de 1,5 em Body e Body large, 1,25 em Title 1 e 1,14 em Display. O gov.br segue a mesma lógica, com 1,45 até o tamanho base e 1,15 acima dele ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)).

> **Divergência entre referências** O gov.br adota fonte base de 14px e uma escala modular de razão 1,2, com tamanhos fracionários como 16,8px e 20,16px, e diz que a escolha da base não é definitiva ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). O Trama mantém Body em 16px, como o texto corrido do DKFDS ([DKFDS](https://designsystem.dk/styleguide/typografi/tekst/)) e o tamanho padrão do GOV.UK ([GOV.UK](https://design-system.service.gov.uk/styles/paragraphs/)), pela convergência das referências. Mantém também a escala de valores inteiros, para que tamanhos e entrelinhas caiam na grade de 4px. O gov.br pede unidades `em`; o Trama usa `rem`, que também é relativa ao tamanho escolhido pela pessoa e não se acumula em componentes aninhados.

### Espaço entre blocos de texto

O espaço antes e depois de títulos, parágrafos e listas também é tokenizado. O gov.br define margens próprias para cada nível de título, para o parágrafo, para os itens de lista e para o rótulo de campo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). O Trama faz o mesmo com tokens `--tx-*`, que apontam para a escala de espaçamento.

| Token              | Valor              | Onde                                      |
|--------------------|--------------------|-------------------------------------------|
| `--tx-h1-after`    | `--sp-800` (32px)  | Depois do título da página                |
| `--tx-h2-before`   | `--sp-1000` (40px) | Antes de uma seção                        |
| `--tx-h2-after`    | `--sp-400` (16px)  | Entre o título da seção e o texto         |
| `--tx-h3-before`   | `--sp-800` (32px)  | Antes de uma subseção                     |
| `--tx-h3-after`    | `--sp-300` (12px)  | Entre o título da subseção e o texto      |
| `--tx-h4-before`   | `--sp-600` (24px)  | Antes de um título de grupo               |
| `--tx-h4-after`    | `--sp-200` (8px)   | Entre o título de grupo e o texto         |
| `--tx-p-after`     | `--sp-400` (16px)  | Entre parágrafos                          |
| `--tx-li-after`    | `--sp-200` (8px)   | Entre itens de uma lista                  |
| `--tx-list-after`  | `--sp-400` (16px)  | Depois da lista inteira                   |
| `--tx-label-after` | `--sp-100` (4px)   | Entre rótulo e campo, como no `.tr-field` |

``` code
:root {
  --tx-h1-after: var(--sp-800);
  --tx-h2-before: var(--sp-1000); --tx-h2-after: var(--sp-400);
  --tx-h3-before: var(--sp-800);  --tx-h3-after: var(--sp-300);
  --tx-h4-before: var(--sp-600);  --tx-h4-after: var(--sp-200);
  --tx-p-after: var(--sp-400);
  --tx-li-after: var(--sp-200);   --tx-list-after: var(--sp-400);
  --tx-label-after: var(--sp-100);
}
.conteudo h2 { margin-block: var(--tx-h2-before) var(--tx-h2-after); }
.conteudo p  { margin-block: 0 var(--tx-p-after); }
```

**Deixe o título mais perto do texto que ele abre.** O espaço antes de um título é sempre maior que o espaço depois dele, para que o título se agrupe com o seu conteúdo.

**Não some as margens de blocos vizinhos.** Quando um parágrafo termina e um título começa, vale a maior das duas margens. Em fluxo de bloco, o CSS já faz isso com o colapso de margens verticais. Em contêineres `flex` e `grid`, as margens não colapsam: use `gap` ou aplique só a margem anterior do título. O gov.br define essa otimização para margens de segurança vizinhas ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/espacamento)).

**Reduza os espaços antes de títulos na classe Compacta.** Abaixo de 600px, `--tx-h2-before` passa para `--sp-800` e `--tx-h3-before` para `--sp-600`. O gov.br também reduz margens de títulos na grid de 4 colunas ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)).

### Espaçamento entre letras

Os estilos a partir de Title 1 têm espaçamento negativo entre letras, declarado em `em` para acompanhar o tamanho. Ferramentas de design costumam medir o espaçamento de bloco (tracking) em milésimos de em. Para converter, use a fórmula do gov.br ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)):

``` code
letter-spacing (px) = tamanho da fonte (px) × tracking / 1000
letter-spacing (em) = tracking / 1000
```

| Estilo             | Tracking | CSS                       | Em px   |
|--------------------|----------|---------------------------|---------|
| Title 1 (32px)     | −10      | `letter-spacing: -.01em`  | −0,32px |
| Large title (40px) | −15      | `letter-spacing: -.015em` | −0,6px  |
| Display (56px)     | −20      | `letter-spacing: -.02em`  | −1,12px |

**Declare o espaçamento em `em`, nunca em px.** Em px, o valor não acompanha a ampliação de texto nem as reduções de título da classe Compacta. Não aplique espaçamento negativo a estilos de leitura.

### Boas práticas

**Use Body (16px) como texto padrão.** Parágrafos, valores digitados em campos e conteúdo de leitura usam `.tr-body`. Campos de texto ficam em 16px também para evitar que navegadores móveis ampliem a página ao focar o campo.

**Use Body small em interfaces densas e evite-o em texto de leitura.** Tabelas, menus e navegação lateral usam 14/20. O GOV.UK recomenda o tamanho pequeno com parcimônia ([GOV.UK](https://design-system.service.gov.uk/styles/paragraphs/)).

**Nunca use texto menor que Caption.** 12px é o piso do Trama, inclusive em densidade alta.

**Use só os pesos 400, 600 e 700.** Pesos finos são difíceis de ler, especialmente em tamanhos pequenos ([HIG](https://developer.apple.com/design/human-interface-guidelines/typography)).

**Construa hierarquia com tamanho, peso e cor, nessa ordem.** Para rebaixar um texto, troque `--t-fg-1` por `--t-fg-2` ou `--t-fg-3` antes de reduzir o tamanho ([HIG](https://developer.apple.com/design/human-interface-guidelines/typography)).

**Siga a ordem dos níveis de título no HTML.** Um `h3` fica sempre abaixo de um `h2`; não pule níveis. Se precisar de outra aparência, aplique outra classe e mantenha a tag correta. O DKFDS exige essa estrutura porque os títulos funcionam como índice para leitores de tela ([DKFDS](https://designsystem.dk/styleguide/typografi/overskrifter/)), e o gov.br pede marcação semântica para que leitores de tela distingam os elementos do texto ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)).

**Escreva títulos em caixa de frase e nunca em caixa alta.** Só a primeira palavra, nomes próprios e siglas começam com maiúscula ([GOV.UK](https://design-system.service.gov.uk/styles/headings/)). O Fluent desaconselha caixa alta por ser difícil de ler ([Fluent](https://fluent2.microsoft.design/typography)).

**Não use itálico em placeholder nem em texto de interface.** O DKFDS desaconselha itálico porque reduz a legibilidade, e sublinhado fora de links, porque parece link ([DKFDS](https://designsystem.dk/styleguide/typografi/tekst/)).

> **Divergência entre referências** O gov.br usa caixa alta nos títulos H5 e H6 e itálico no placeholder ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). O GOV.UK e o Fluent pedem caixa de frase e o DKFDS desaconselha itálico. Pela convergência, o Trama não usa caixa alta em títulos nem itálico em placeholder.

**Limite a linha a cerca de 75 caracteres.** Aplique `max-width: 75ch` a blocos de texto corrido. O GOV.UK usa colunas de dois terços para não passar desse limite ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)), e o DKFDS limita parágrafos a aproximadamente 75 caracteres no desktop ([DKFDS](https://designsystem.dk/styleguide/typografi/tekst/)).

**Alinhe o texto à esquerda e nunca justifique.** Centralize só textos curtos, como um estado vazio. O texto justificado cria espaços irregulares entre palavras ([GOV.UK](https://design-system.service.gov.uk/styles/font-override-classes/)). Em idiomas da direita para a esquerda, veja Internacionalização.

**Use algarismos tabulares em números comparáveis.** Em tabelas, contadores e valores que atualizam, aplique `font-variant-numeric: tabular-nums`, como a classe `.num` de `.tr-table` já faz ([GOV.UK](https://design-system.service.gov.uk/styles/font-override-classes/)).

**Destaque trechos com `.tr-mark`.** Use o elemento `mark` com a classe para termos encontrados numa pesquisa. O par `--t-mark-fg` sobre `--t-mark` tem 15,57:1 no claro e 8,10:1 no escuro.

**Declare fontes de reserva.** Se Inter não carregar, `--t-font-sans` recai em fontes do sistema sem serifa. O gov.br também pede uma fonte de reserva para quando a principal não carrega ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)).

### Acessibilidade

**Garanta contraste de 4,5:1 para todo texto abaixo de Title 3.** A WCAG 2.2, 1.4.3, aceita 3:1 para texto grande. O gov.br considera texto grande a partir de 24px, ou 19px em negrito ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). No Trama, trate como texto grande somente estilos a partir de Title 3 (24px). Subtitle (20px, peso 600) segue o limite de 4,5:1.

**Suporte ampliação de texto até 200%.** A WCAG 2.2, 1.4.4, exige que o texto possa ser ampliado até 200% sem perda de conteúdo ou função. Não fixe alturas de contêineres com texto; deixe linhas crescerem e elementos lado a lado empilharem ([HIG](https://developer.apple.com/design/human-interface-guidelines/typography)).

**Quebre a linha em vez de truncar.** Títulos, itens de menu e navegação, rótulos de botão e mensagens nunca são truncados. Truncamento só é aceito em células de tabela, breadcrumb, nomes de arquivo e chips, com o texto completo acessível (veja Excesso de conteúdo). Em e-mails e URLs longos, use `overflow-wrap: anywhere` ([GOV.UK](https://design-system.service.gov.uk/styles/font-override-classes/)).

**Preserve o espaçamento ajustado pela pessoa.** A WCAG 2.2, 1.4.12, exige que o conteúdo continue funcionando quando a pessoa aumenta altura de linha e espaçamento entre letras e palavras.

### Considerações por plataforma

#### Web desktop

Use Title 1 para o `h1` da maioria das páginas e reserve Large title para páginas de entrada e conteúdo editorial. Em telas largas, limite o comprimento da linha com a coluna de leitura descrita em Layout e grid, e não aumente o corpo do texto.

#### Web móvel

Na classe Compacta, reduza os estilos maiores um degrau: Display passa a Large title, Large title passa a Title 1 e Title 1 passa a Title 2. Body continua em 16px. O GOV.UK reduz os títulos grandes em telas pequenas e mantém o corpo do texto ([GOV.UK](https://design-system.service.gov.uk/get-started/new-type-scale/)), o DKFDS leva o título 1 de 48px a 32px no celular ([DKFDS](https://designsystem.dk/styleguide/typografi/overskrifter/)), e o gov.br reduz os títulos na grid de 4 colunas ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)).

#### Tablets e dobráveis

Use a escala do desktop a partir da classe Média (600px). Em layouts de dois painéis, o painel de lista usa Body small e Subtitle para títulos de item; o painel de detalhe usa a escala completa. Teste com o tamanho de fonte do sistema ampliado, pois tablets são muito usados para leitura.

### Recursos

#### Relacionados

- Texto e títulos
- Escrita e conteúdo
- Espaçamento
- Layout e grid
- Excesso de conteúdo
- Internacionalização e direita para esquerda

#### Referências

- [Tipografia](https://www.gov.br/ds/fundamentos-visuais/tipografia) gov.br DS
- [Espaçamento](https://www.gov.br/ds/fundamentos-visuais/espacamento) gov.br DS
- [Cores](https://www.gov.br/ds/fundamentos-visuais/cores) gov.br DS
- [Typography](https://developer.apple.com/design/human-interface-guidelines/typography) Apple HIG
- [Typography](https://fluent2.microsoft.design/typography) Fluent 2
- [Type scale](https://design-system.service.gov.uk/styles/type-scale/) GOV.UK Design System
- [Using the updated type scale](https://design-system.service.gov.uk/get-started/new-type-scale/) GOV.UK Design System
- [Headings](https://design-system.service.gov.uk/styles/headings/) GOV.UK Design System
- [Paragraphs](https://design-system.service.gov.uk/styles/paragraphs/) GOV.UK Design System
- [Font override classes](https://design-system.service.gov.uk/styles/font-override-classes/) GOV.UK Design System
- [Layout](https://design-system.service.gov.uk/styles/layout/) GOV.UK Design System
- [Overskrifter](https://designsystem.dk/styleguide/typografi/overskrifter/) Det Fælles Designsystem
- [Tekst](https://designsystem.dk/styleguide/typografi/tekst/) Det Fælles Designsystem

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                    |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta os tokens de espaço entre blocos de texto, a fórmula de espaçamento entre letras, as regras de caixa alta, itálico, truncamento e destaque, e registra as divergências de fonte base e escala. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                             |

## Escrita e conteúdo

As palavras são material de design: o que você diz, e quando diz, determina se a pessoa entende a tela e consegue concluir a tarefa.

Todo texto de interface ajuda a pessoa a fazer uma escolha, executar uma ação ou entender o que está acontecendo; o texto que não cumpre nenhum desses papéis sai da tela ([One UI](https://developer.samsung.com/one-ui/writing/focused-and-purposeful.html)). As regras do Trama seguem a linguagem simples, cujo objetivo é que a pessoa localize rápido a informação de que precisa, entenda e use. Escrever simples exige trabalho e não significa escrever de forma simplória ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)).

Esta página define a voz do Trama, as regras de escrita em português do Brasil, o microcopy de cada tipo de componente e o vocabulário controlado. Linguagem inclusiva está em Inclusão; texto alternativo, em Imagens.

### Voz e tom

A **voz** é a personalidade constante do produto. O **tom** varia com a situação ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/writing), [gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). A voz do Trama tem três traços:

| Traço      | Significa                                                                                              | Evite                                                                     |
|------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Clara      | Palavras do dia a dia, frases curtas, uma ideia por frase, termos técnicos explicados logo em seguida. | Jargão, siglas sem explicação, juridiquês, código de erro sem explicação. |
| Direta     | Voz ativa, objetivo no início da frase, informação mais importante primeiro.                           | Rodeios, "gostaríamos de informar que", avisos defensivos.                |
| Respeitosa | Trata a pessoa por "você", nunca culpa, oferece saída.                                                 | Intimidade forçada, gírias, piadas, exclamações, "Ops".                   |

> **Divergência entre referências** O Fluent recomenda uma voz informal e conversacional ([Fluent 2](https://fluent2.microsoft.design/content-design)). O gov.br pede uma voz neutra, formal, direta e desburocratizada ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Em linguagem para o público brasileiro, o gov.br pesa mais. O Trama adota a voz neutra e desburocratizada: trata a pessoa por "você", sem gíria e sem fórmulas burocráticas.

**Ajuste o tom ao momento da pessoa.** Pergunte se ela está aliviada por concluir uma tarefa ou confusa procurando ajuda ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Um erro de pagamento pede tom sóbrio; uma confirmação pode ser calorosa, sem exclamação.

### Regras de escrita em português

**Escreva para uma pessoa, no singular, com "você".** Veja Inclusão.

**Comece pelo objetivo.** Escreva "Consulte seu extrato nas opções do perfil", e não "Acesse as opções do perfil para consultar seu extrato" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)).

**Seja breve sem omitir.** "Digite seu e-mail para acessar a primeira aula" substitui "Basta preencher seu e-mail favorito abaixo e você terá acesso instantâneo" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)).

**Limite parágrafos a 4 linhas.** Divida textos longos, use títulos ao mudar de assunto e listas quando houver itens ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)).

**Use voz ativa.** "Use o botão Pesquisar" no lugar de "O botão Pesquisar deve ser utilizado". A passiva vale quando a ação importa mais do que quem a fez, como em "Sua conta foi validada pela equipe de suporte" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)), ou para não precisar dizer "nós" ([Fluent 2](https://fluent2.microsoft.design/content-design)).

**Não negue um termo negativo.** Dupla negação aumenta a carga cognitiva: "Quero cancelar esta ação" é mais claro do que "Não quero cancelar esta ação" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Rótulos também são positivos: "Cancelar envio de e-mails", não "Não me envie mais e-mails" ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Evite estrangeirismos com equivalente comum.** "Exclua um item", não "Delete um item". Palavras estrangeiras de uso popular, como WhatsApp, continuam ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)).

**Escreva a sigla por extenso na primeira vez.** Na primeira ocorrência, use o nome completo com a sigla entre parênteses; depois, só a sigla ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Em rótulos de ação, evite siglas e abreviações ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

> **Divergência entre referências** O gov.br manda escrever siglas de até três letras em maiúsculas e, de quatro letras ou mais, só com a inicial maiúscula, com o exemplo "Embraer" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Aplicada ao pé da letra, a regra produziria "Cnpj" e "Inss", siglas lidas letra a letra. O Trama segue o gov.br para siglas lidas como palavra (Embraer, Detran, Inmetro) e mantém em maiúsculas as soletradas (CPF, CNPJ, INSS).

**Use algarismos.** "Você tem 4 mensagens novas" é lido mais rápido e ocupa menos espaço do que "quatro" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)).

**Não use direção, forma ou cor como referência.** "Acima", "à esquerda" ou "o botão verde" quebram em outros tamanhos de tela, em RTL e para quem não enxerga ([Fluent 2](https://fluent2.microsoft.design/content-design)). Em texto que aparece em todas as plataformas, prefira "selecione" a "clique" ou "toque" ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/writing)).

### Capitalização e pontuação

**Use caixa de frase em toda a interface.** Só a primeira letra da frase, nomes próprios e siglas ficam em maiúscula, em títulos, botões, navegação, abas, rótulos e mensagens ([Fluent 2](https://fluent2.microsoft.design/content-design), [GOV.UK](https://design-system.service.gov.uk/components/button/)). Nunca escreva palavras inteiras em caixa alta ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Faça** Caixa de frase, com maiúscula em siglas e nomes próprios.

**Não faça** Iniciais maiúsculas em cada palavra ou texto todo em caixa alta.

> **Divergência entre referências** O gov.br usa iniciais maiúsculas em botões ("Gerar Relatório"), títulos e navegação, e caixa de frase nos demais textos ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). O Fluent usa caixa de frase na web ([Fluent 2](https://fluent2.microsoft.design/content-design)), o GOV.UK pede caixa de frase em botões ([GOV.UK](https://design-system.service.gov.uk/components/button/)) e a Apple pede um único estilo aplicado com consistência ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/writing)). Sem pesquisa citada de nenhum lado, vale a convergência: o Trama usa caixa de frase em tudo.

| Elemento                                        | Regra                                                                                                                                                                                     | Exemplo                   |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| Botões, rótulos, abas, itens de menu, títulos   | Sem ponto final; título com interrogação quando for pergunta ([Fluent 2](https://fluent2.microsoft.design/content-design), [gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). | Salvar alterações         |
| Dicas, descrições, mensagens com frase completa | Ponto final.                                                                                                                                                                              | Use o e-mail do trabalho. |
| Exclamação                                      | Não use, nem em confirmações.                                                                                                                                                             | Endereço atualizado       |
| Reticências                                     | Em itens de menu que pedem uma etapa a mais antes de executar e em estados de progresso.                                                                                                  | Salvar como…, Enviando…   |
| Dois-pontos                                     | Não use no fim de rótulos de campo. O gov.br aceita qualquer opção desde que consistente ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)); o Trama fixa "sem".              | E-mail                    |
| Aspas                                           | Aspas duplas para nomes de itens criados pela pessoa.                                                                                                                                     | Excluir "Orçamento 2027"? |
| Travessão e meia-risca                          | Não use. Prefira vírgula, dois-pontos, parênteses ou ponto. Em intervalos, escreva "a".                                                                                                   | 10 a 14 de outubro        |

### Microcopy por tipo de componente

Os grupos seguem a organização do microcopy do gov.br ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

#### Ação: botões, links e tags

**Escreva rótulos de ação com até 2 palavras, 3 quando inevitável, sem artigo.** "Adicionar marcação", não "Adicionar uma marcação" ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Corte palavras só enquanto o sentido se mantém: "Remover todos os usuários" diz algo que "Remover usuários" não diz ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Escreva para caber numa linha; se não couber, o rótulo quebra e nunca é truncado.

**Comece com um verbo no infinitivo que diga o resultado.** "Enviar documento" informa mais do que "Enviar" ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Repita o verbo da pergunta e nunca use só "Sim", "Não" ou "OK".** "Quer salvar seus dados?" leva a "Cancelar" e "Salvar" ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Prefira "Aceitar" a "Ok" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Numa ação destrutiva, o rótulo diz o que vai acontecer, sem depender da cor ([GOV.UK](https://design-system.service.gov.uk/components/button/)).

**Escreva tags sem verbo.** Use substantivos ou adjetivos: "Criação de conteúdo", não "Criar conteúdo" ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Escreva links que digam o destino.** O texto do link faz sentido fora do contexto, porque leitores de tela listam links isolados. Evite "clique aqui", "leia mais" e "saiba mais" soltos e prefira palavras-chave curtas: "O vestibular está com inscrições abertas" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing), [gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Não repita o texto do link no atributo `title` ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Se o link abrir em nova aba, diga "(abre em nova aba)" no próprio texto.

#### Entrada de dados

**Escreva rótulos com até 3 palavras, sempre visíveis, acima do campo.** Rótulos curtos e completos dizem rápido o que preencher; acima do campo, não disputam espaço horizontal no celular ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Nunca substitua o rótulo por placeholder ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)). Mostre o formato esperado na dica, como "Formato: (11) 91234-5678", e aceite qualquer formato digitado. Placeholder, se houver, é um exemplo genérico e não fica em itálico.

#### Feedback: mensagens, erros e estados vazios

**Diga o que mudou, sem "com sucesso" e sem exclamação.** "Arquivo enviado", "Endereço atualizado".

> **Divergência entre referências** O gov.br recomenda "O arquivo foi enviado com sucesso!" e desaconselha "Arquivo enviado" ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). O Fluent reserva a exclamação para celebrações ([Fluent 2](https://fluent2.microsoft.design/content-design)), e o próprio gov.br pede concisão e mensagens curtas, porque quanto mais longa, menos lida ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). O Trama fica com a confirmação curta que nomeia o que mudou, sem "com sucesso" e sem exclamação.

**Nunca culpe a pessoa, mesmo quando o erro foi dela.** Diga o que aconteceu e como resolver: "Insira um e-mail no formato nome@provedor.com", não "Você digitou seu e-mail incorretamente" ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Mostre a mensagem perto do problema ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/writing)) e reaproveite as palavras do rótulo ([GOV.UK](https://design-system.service.gov.uk/components/error-message/)).

**Mantenha o tom neutro, sem humor e sem "Ops".** Mensagens de "Ops!" não suavizam nada e podem incomodar; não faça humor em erro ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/writing)). Evite "inválido", "proibido", "você esqueceu" e jargão técnico: "A senha não está correta" ajuda mais do que "Erro do sistema (código \#2234)" ([GOV.UK](https://design-system.service.gov.uk/components/error-message/), [gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Veja Validação e mensagens de erro.

**Diga num estado vazio para que serve a tela e o que fazer.** Dê uma orientação útil sobre o próximo passo ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/writing)).

#### Visualização de dados

**Alinhe pelo tipo de dado.** Texto à esquerda; números e valores monetários à direita, com algarismos tabulares; identificadores e números que não se somam à esquerda; ícones ao centro ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Use ponto como separador de milhar e vírgula como decimal: 1.398.672,00 ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Datas em tabelas têm sempre o mesmo número de dígitos ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)).

### Formatos em pt-BR

| Tipo                         | Formato do Trama                                                                                                                                               | Exemplo                   |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| Data curta (tabelas, campos) | dd/mm/aaaa, com zeros à esquerda                                                                                                                               | 05/03/2026                |
| Data longa (texto corrido)   | dia de mês de ano, mês em minúscula                                                                                                                            | 5 de março de 2026        |
| Hora em interface            | 24 horas, com dois-pontos                                                                                                                                      | 09:30, 18:00              |
| Hora em texto corrido        | h e min                                                                                                                                                        | 9h30, 18h                 |
| Intervalo                    | "a", "das… às" ou "de… até"                                                                                                                                    | das 9h às 18h             |
| Milhar e decimal             | Ponto para milhar, vírgula para decimal                                                                                                                        | 1.234,56                  |
| Moeda                        | R\$ seguido de espaço não separável                                                                                                                            | R\$ 1.250,00              |
| Unidades                     | Por extenso em texto corrido e rótulos acessíveis; abreviadas (min, h, d, kB, MB) só em eixos, células e cartões compactos, com a unidade nomeada no cabeçalho | Tempo estimado: 5 minutos |
| Telefone                     | DDD entre parênteses                                                                                                                                           | \(11\) 91234-5678         |

Formate com `Intl.DateTimeFormat` e `Intl.NumberFormat` no locale `pt-BR`. Veja Internacionalização.

### Vocabulário controlado

Quanto mais padronizado o vocabulário, menor o esforço cognitivo; se um site usa "Agendar" numa página, não usa "Programar" em outra ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). Use sempre a palavra da coluna "Use". A coluna "Ação contrária" segue o modelo do dicionário do gov.br e define o par de cada verbo.

| Use            | Para                                                               | Ação contrária        | Não use                                  |
|----------------|--------------------------------------------------------------------|-----------------------|------------------------------------------|
| Pesquisar      | Procurar por termo ou consultar dados                              | Limpar pesquisa       | Buscar, Procurar, Consultar              |
| Filtrar        | Restringir uma lista por critérios                                 | Limpar filtros        | Refinar                                  |
| Baixar         | Transferir um arquivo para o dispositivo                           | Enviar arquivo        | Fazer download, Descarregar              |
| Enviar arquivo | Transferir um arquivo do dispositivo para o serviço                | Baixar                | Fazer upload, Subir, Carregar            |
| Anexar         | Juntar um arquivo a uma mensagem ou pedido que será enviado depois | Remover anexo         | Atachar                                  |
| Enviar         | Transmitir formulário, mensagem ou pedido                          | Cancelar envio        | Submeter, Mandar                         |
| Criar          | Gerar um objeto novo do zero                                       | Excluir               | Novo (sozinho)                           |
| Adicionar      | Incluir um item existente numa lista ou grupo                      | Remover               | Inserir, Incluir                         |
| Remover        | Tirar um item de uma lista sem apagá-lo do sistema                 | Adicionar             | Retirar                                  |
| Excluir        | Apagar definitivamente ou mover para a lixeira                     | Recuperar             | Deletar, Apagar, Eliminar                |
| Arquivar       | Tirar de circulação sem apagar                                     | Restaurar             | Ocultar                                  |
| Editar         | Abrir um item para alteração                                       | Cancelar edição       | Alterar, Modificar                       |
| Salvar         | Gravar alterações e permanecer no contexto                         | Descartar alterações  | Gravar                                   |
| Visualizar     | Abrir a prévia de um item sem editar                               | Fechar                | Ver, Exibir                              |
| Mostrar        | Revelar no lugar um conteúdo oculto, como a senha                  | Ocultar               | Exibir, Desocultar                       |
| Continuar      | Avançar em fluxo de tarefa, com a pessoa ativa                     | Voltar                | Seguir, Avançar, Prosseguir              |
| Próximo        | Avançar em leitura passiva, como onboarding e carrossel            | Anterior              | Seguinte                                 |
| Concluir       | Terminar a última etapa de um fluxo                                | Cancelar              | Finalizar, Pronto                        |
| Cancelar       | Abandonar a tarefa atual sem salvar                                | Continuar             | Abortar                                  |
| Fechar         | Dispensar painel, diálogo ou mensagem sem efeito nos dados         | Abrir                 | Sair, OK                                 |
| Confirmar      | Aceitar uma ação já revisada                                       | Cancelar              | Sim, OK                                  |
| Entrar         | Iniciar sessão                                                     | Sair                  | Logar, Login, Acessar                    |
| Exportar       | Converter dados para outro formato ou sistema                      | Importar              | Extrair                                  |
| Desfazer       | Reverter a última ação                                             | Refazer               | Reverter                                 |
| Copiar         | Levar conteúdo para a área de transferência                        | Colar                 | Copiar para o clipboard                  |
| Compartilhar   | Dar acesso a outra pessoa                                          | Parar de compartilhar | Enviar link (quando a ação é dar acesso) |
| Ativar         | Ligar uma função ou preferência                                    | Desativar             | Habilitar, Ligar                         |

> **Divergência entre referências** O dicionário do gov.br usa "Fazer download", com ação contrária "Importar", e "Visualizar", com sinônimo "Mostrar" ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)). A própria regra do gov.br de evitar estrangeirismos com equivalente comum leva a "Baixar", forma que o gov.br também usa no catálogo de ícones ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/iconografia)); o par natural de "Baixar" é "Enviar arquivo". "Mostrar senha" é o rótulo do GOV.UK ([GOV.UK](https://design-system.service.gov.uk/components/password-input/)); o Trama separa "Mostrar", para revelar no lugar, de "Visualizar", para abrir uma prévia. Na versão 1.0, o Trama usava "Buscar"; passou a usar "Pesquisar", do vocabulário do gov.br. "Continuar" e "Próximo" seguem a distinção do gov.br entre tarefa e leitura passiva, mais precisa do que a escolha livre entre os dois termos admitida pela Apple ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/writing)).

### Considerações por plataforma

#### Web desktop

Mantenha o texto tão curto quanto no celular, mesmo com mais espaço.

#### Web móvel

Telas pequenas exigem brevidade ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/writing)). Teste rótulos de botão em 320px: se quebrarem em mais de duas linhas, reescreva. Diga "toque", não "clique". Ofereça os dados de gráficos também em tabela, porque gráficos podem ser difíceis de ler no celular ([gov.br DS](https://www.gov.br/ds/padroes/writing/principios-writing)).

#### Tablets e dobráveis

O mesmo texto aparece na tela externa estreita e na tela interna larga de um dobrável. Escreva para a largura menor e confira que nada é truncado na transição ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

### Recursos

#### Relacionados

- Inclusão
- Validação e mensagens de erro
- Botões
- Links
- Estados vazios
- Internacionalização e direita para esquerda
- Iconografia

#### Referências

- [Princípios de UX writing](https://www.gov.br/ds/padroes/writing/principios-writing) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Iconografia](https://www.gov.br/ds/fundamentos-visuais/iconografia) gov.br DS
- [Writing](https://developer.apple.com/design/human-interface-guidelines/writing) Apple HIG
- [Content design](https://fluent2.microsoft.design/content-design) Fluent 2
- [Error message](https://design-system.service.gov.uk/components/error-message/) GOV.UK Design System
- [Button](https://design-system.service.gov.uk/components/button/) GOV.UK Design System
- [Password input](https://design-system.service.gov.uk/components/password-input/) GOV.UK Design System
- [Focused and purposeful](https://developer.samsung.com/one-ui/writing/focused-and-purposeful.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta regras em pt-BR, microcopy e vocabulário controlado com ação contrária, e registra divergências. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                               |

## Estados de interação

Estados mostram o que pode ser acionado, o que a pessoa está fazendo agora e o resultado das ações, sempre com o mesmo desenho em todos os componentes.

Um estado é a resposta visual de um elemento a uma interação ou a uma condição. O Trama divide os estados em dois grupos, como o Padrão Digital de Governo: estados de interação, que respondem ao que a pessoa faz com mouse, toque, teclado, voz ou leitor de tela, e estados de aviso, que comunicam erro, alerta, sucesso ou informação ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O repouso é a ausência de estado: o elemento aparece como foi desenhado.

Todos os componentes do kit calculam hover e pressionado da mesma forma, com uma camada translúcida por cima do fundo. Um componente novo herda o comportamento sem cores próprias.

### Como os estados são calculados

O **fundo** é a superfície do elemento que recebe o estado; o **primeiro plano** é o texto, o ícone e tudo o que está sobre essa superfície. A referência muda conforme o elemento: para um card, o botão dentro dele é primeiro plano; para o botão, o rótulo é o primeiro plano ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

**Desenhe hover e pressionado como uma camada na cor do primeiro plano.** A camada usa `currentColor` com a opacidade `--o-hover` ou `--o-pressed` e fica por cima do fundo, como uma imagem de fundo. O gov.br define o mesmo método, com a cor do primeiro plano e opacidades 0,16 e 0,30 para hover e 0,45 e 0,65 para pressionado ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O Blueprint usa a mesma técnica de empilhar uma cor translúcida com `linear-gradient(cor 0 0)` em `background-image` ([Blueprint](https://blueprintjs.com/docs/)).

| Token         | Tema claro      | Tema escuro e `.tr-inverse` | Uso                   |
|---------------|-----------------|-----------------------------|-----------------------|
| `--o-hover`   | 0,16 (`--o-xs`) | 0,30 (`--o-sm`)             | Camada de hover       |
| `--o-pressed` | 0,45 (`--o-md`) | 0,65 (`--o-lg`)             | Camada de pressionado |

A opacidade é maior no escuro porque a camada precisa de mais força para ser percebida sobre um fundo de pouco brilho. O gov.br descreve a opacidade como inversamente proporcional ao brilho do fundo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O `.tr-inverse` troca os valores sozinho, então um rodapé escuro no tema claro já recebe a camada certa.

**Use os tokens pré-calculados na cor da marca.** Uma camada sobre o azul-tinta criaria um matiz que não existe na paleta. O botão primário passa para `--t-brand-hover` e `--t-brand-pressed`, que mantêm o rótulo em 8,00:1 e 10,63:1 no claro. O gov.br pede para evitar novos matizes gerados por sobreposição de cores ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/superficie)).

**Confira o contraste do primeiro plano sobre a camada.** Com a camada de hover, o rótulo de um botão neutro fica em 12,64:1 no claro e 6,06:1 no escuro. No botão neutro, o kit aplica 60% de `--o-pressed` para preservar o rótulo: 9,78:1 no claro e 4,51:1 no escuro.

> **Importante** O botão neutro pressionado no tema escuro fica em 4,51:1, logo acima do critério WCAG 2.2, 1.4.3. A margem é pequena: em componentes novos, meça o rótulo sobre a camada e reduza a opacidade se ele cair abaixo de 4,5:1.

### Estados de interação

| Estado               | Comunica                                                     | Desenho no Trama                                                                                                         | Não se aplica a                                                     |
|----------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Interativo (repouso) | Que o elemento pode ser acionado                             | Cor de interação (`--t-brand`, `--t-link`), contorno `--t-border-control`, sublinhado em links, cursor de mão            | Texto estático e decoração                                          |
| Hover                | Que o ponteiro está sobre o elemento                         | Camada `--o-hover`; links engrossam o sublinhado                                                                         | Toque, elementos desabilitados                                      |
| Foco                 | Qual elemento recebe o teclado ou a voz                      | Anel de `--stroke-thick` em `--t-focus`, afastado 2px, só em `:focus-visible`                                            | Clique e toque, elementos com `disabled`                            |
| Foco tênue           | Foco movido pelo sistema, sem ação de teclado                | `.tr-focus-subtle`: contorno de `--stroke-thin` afastado 1px                                                             | Foco por teclado                                                    |
| Pressionado          | Que o elemento está sendo acionado                           | Camada `--o-pressed`; sombra retirada                                                                                    | Elementos desabilitados, arrasto                                    |
| Ativo ou atual       | O item em vigor num conjunto, com efeito imediato            | `aria-current`: `--t-brand-subtle` com barra de 3px, sublinhado de 3px ou preenchimento `--t-brand`                      | Conjuntos com vários itens ativos ao mesmo tempo                    |
| Selecionado          | Uma escolha para ação posterior                              | `aria-selected` ou `aria-checked`: fundo `--t-brand-subtle` e um elemento gráfico (marca, checkbox, texto "Selecionado") | Navegação, diálogo, tooltip, botão, mensagem, divisor               |
| Ligado e desligado   | A alternância entre duas opções                              | Switch, `aria-pressed`: `--t-brand` ligado, `--t-border-control` desligado                                               | Escolhas com mais de duas opções                                    |
| Visitado             | Que o destino de um link já foi aberto                       | `--t-link-visited`                                                                                                       | Botões, navegação, links de ação                                    |
| Desabilitado         | Indisponível agora, por um motivo que a pessoa pode resolver | Fundo `--t-surface-2`, borda `--t-border-subtle`, texto `--t-fg-disabled`, cursor `not-allowed`, sem sombra              | Botão de envio de formulário, itens que a pessoa não pode habilitar |
| Arrastável           | Que o elemento pode ser movido                               | Ícone de alça no início ou no topo, cursor `grab`                                                                        | Elementos redimensionáveis                                          |
| Arrastando           | O elemento em movimento                                      | `.tr-dragging`: opacidade `--o-xl`, rotação, `--e-4`, cursor `grabbing`                                                  | Mais de um elemento por vez                                         |
| Área de soltar       | Onde o elemento pode ser solto                               | `.tr-dropzone`: borda tracejada de `--stroke-thick`                                                                      | Áreas que não aceitam o item arrastado                              |
| Área de soltar ativa | Onde o elemento cairá se for solto agora                     | `.tr-dropzone--active`: borda `--t-brand` e camada da marca em `--o-xs`                                                  | Mais de uma área ao mesmo tempo                                     |

#### Ativo ou selecionado

**Use "ativo" quando a escolha age na hora e "selecionado" quando ela prepara uma ação.** Um item de navegação abre a página; uma aba troca o painel; um botão de alinhamento muda o texto: são ativos, e só um vale por vez. Marcar três arquivos para depois excluí-los é seleção, e vários itens podem estar selecionados ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Na navegação, use `aria-current`. Abas são a exceção de atributo: o padrão WAI-ARIA de abas exige `aria-selected`, mas a aparência é a de estado ativo, com o sublinhado de 3px do `.tr-tab`.

**Mostre a seleção com fundo e um elemento gráfico.** Cor sozinha não basta. O `.tr-list` com `aria-selected="true"` recebe `--t-brand-subtle` e o texto "Selecionado"; tabelas e listas longas usam checkbox. O gov.br pede fundo e ícone de seleção ou checkbox ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). A Apple prefere destacar a linha inteira em listas e coleções e usar anel de foco em campos de texto ([HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)).

#### Foco e foco tênue

**Mostre o anel só quando o foco vier do teclado ou da voz.** O Trama usa `:focus-visible`, então um clique não desenha o anel. O gov.br pede o mesmo: clicar ou tocar não gera foco visual, mas o foco por teclado precisa existir ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

**Use o foco tênue quando o sistema mover o foco.** Ao abrir uma página nova, o Trama leva o foco ao título `h1`; ao validar um formulário, leva ao resumo de erros. Nesses casos, aplique `.tr-focus-subtle` com `tabindex="-1"`: o contorno de 1px indica onde a leitura recomeça sem competir com o conteúdo. A Apple pede para evitar mover o foco sem interação da pessoa ([HIG](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)); por isso o Trama só move o foco nos momentos definidos em Foco e seleção.

> **Divergência entre referências** O gov.br desenha o foco com borda tracejada de 4px em amarelo-ouro e 4px de afastamento ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O Trama mantém o anel sólido de 2px em `--t-focus`, afastado 2px. Pelo critério de acessibilidade, o azul do Trama tem 5,85:1 sobre `--t-bg` no claro e 8,99:1 no escuro, acima dos 3:1 pedidos para partes gráficas de componentes (WCAG 2.2, 1.4.11), e continua visível em modo de cores forçadas por ser um `outline`.

#### Desabilitado

**Retire da interface o que a pessoa não pode habilitar.** Se nenhuma ação dela torna o elemento disponível, não o mostre. Se pode, mostre desabilitado e diga por quê, num texto próximo ligado por `aria-describedby` ou num tooltip focável. O gov.br dá o exemplo de um produto em falta: retire o botão de compra em vez de desabilitá-lo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Nunca desabilite o botão de envio de um formulário: valide ao enviar.

**Não herde outros estados no desabilitado.** Um elemento desabilitado não recebe hover, pressionado, arraste nem área de soltar, e perde a sombra.

> **Divergência entre referências** O gov.br desenha o desabilitado com opacidade 0,45 sobre o elemento inteiro e diz que ele não recebe foco ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). O Trama usa tokens fixos: `--t-fg-disabled` tem 2,61:1 sobre `--t-bg` no claro, contra 2,52:1 do texto \#333333 do gov.br a 45%, e 3,13:1 no escuro. Pelo critério de acessibilidade, o Trama também mantém focável o controle que precisa explicar o motivo: use `aria-disabled="true"` nele, para que o leitor de tela encontre o controle e a explicação. Use `disabled` quando a explicação já estiver no texto visível ao lado.

### Exclusividade, prioridade e herança

**Mantenha um único hover, um único foco e um único pressionado por vez.** Também só existe um elemento sendo arrastado e uma área de soltar ativa por vez, e um único item ativo em cada conjunto ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Um elemento tem um só tipo de foco: normal ou tênue.

**Combine os estados e dê prioridade à interação direta.** Estados se somam: um item ativo em hover mostra o fundo ativo e a camada de hover; um botão focado e pressionado mostra o anel e a camada. Quando dois desenhos disputam a mesma propriedade, vence o estado causado por último pela interação direta da pessoa. No menu, o hover sobre um item prevalece sobre o desenho do item ativo ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

**Mantenha o estado enquanto durar o efeito.** Um botão que abriu um menu continua com a camada de hover enquanto o menu estiver aberto; no kit, `aria-expanded="true"` faz isso. O estado arrastando não herda o pressionado.

**Ajuste a área do estado quando o contraste pedir.** Se um texto ou ícone fica difícil de ler com o estado aplicado, aumente o fundo do estado em 4px ou 8px sem sobrepor vizinhos ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

### Arrastar e soltar

**Ative a área de soltar pela posição do ponteiro ou do dedo.** A referência é o ponto de contato, e a área sensível pode ser maior que a borda visível, nunca menor ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Ofereça também uma alternativa sem arraste, como o comando Mover, para teclado e leitores de tela (WCAG 2.2, 2.5.7). Detalhes em Arrastar e soltar.

### Estados de aviso

Cada aviso combina uma cor e um ícone, e nunca depende só da cor.

| Aviso      | Tokens                                                    | Ícone                   | Persistência                      |
|------------|-----------------------------------------------------------|-------------------------|-----------------------------------|
| Erro       | `--t-danger`, `aria-invalid="true"`                       | Exclamação ou X         | Até ser resolvido                 |
| Alerta     | `--t-warning`, `--t-warning-fill`, `data-state="warning"` | Exclamação em triângulo | Até a pessoa fechar               |
| Sucesso    | `--t-success`, `data-state="success"`                     | Marca de confirmação    | Some sozinho só em toast sem ação |
| Informação | `--t-info`                                                | Letra i                 | Some sozinho só em toast sem ação |

Os ícones e a persistência seguem o gov.br, que mantém o erro até a solução e permite dispensar sucesso e informação automaticamente ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). No Trama, só toasts informativos sem ação somem sozinhos, depois de pelo menos 7 segundos e com pausa em hover e foco (veja Toasts).

**Faça** mantenha o botão de envio sempre habilitado e mostre os erros ao enviar.

**Não faça** desabilite o envio até o formulário ficar completo. A pessoa não sabe o que falta.

### Considerações por plataforma

#### Web desktop

Hover é o estado mais frequente com mouse e trackpad. Mantenha-o sutil e em `--m-fast`. Nunca esconda uma ação até o hover: quem usa teclado ou toque não a encontra. Em listas e tabelas, o hover da linha pode ajudar a seguir a leitura, um uso que o gov.br considera raro e aceitável ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)).

#### Web móvel

Não há hover. O pressionado é o retorno imediato do toque e precisa aparecer assim que o dedo encosta. Navegadores móveis podem manter o estilo de `:hover` depois do toque; envolva regras de hover em `@media (hover: hover)` quando criar componentes novos.

#### Tablets e dobráveis

A mesma pessoa alterna entre toque, teclado e trackpad. Desenhe todos os estados para todos os métodos: o anel de foco aparece quando um teclado está conectado, o hover aparece com trackpad, e o pressionado vale para toque e caneta.

### Recursos

#### Relacionados

- Cor
- Foco e seleção
- Materiais
- Arrastar e soltar
- Validação e mensagens de erro
- Botões
- Densidade

#### Referências

- [Estados](https://www.gov.br/ds/fundamentos-visuais/estados) gov.br DS
- [Superfície](https://www.gov.br/ds/fundamentos-visuais/superficie) gov.br DS
- [Cores](https://www.gov.br/ds/fundamentos-visuais/cores) gov.br DS
- [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) Apple HIG
- [Design tokens](https://blueprintjs.com/docs/) Blueprint

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## Densidade

A densidade ajusta os espaços vazios dos componentes em três níveis para caber mais informação ou dar mais conforto, sem mudar o que cada componente é.

Densidade é a quantidade de espaço vazio dentro e em volta dos componentes. O gov.br a define como a especificação desses espaços, ajustável numa escala de intensidade ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). O Trama oferece três níveis: **alta**, com componentes mais compactos; **padrão**, o desenho de referência de cada componente; e **baixa**, com componentes mais amplos.

O nível vale para uma região inteira, nunca para um componente isolado. Aplique `data-density="alta"` ou `data-density="baixa"` no contêiner, e os componentes dentro dele trocam de valores. Sem o atributo, vale a densidade padrão. A Apple pede para escolher tamanho e densidade do conteúdo pela distância de visualização e pelo método de entrada ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados)), e esse é o critério do Trama.

### Escala de densidade

Os níveis andam em passos de 4px a partir do valor padrão de cada componente. O componente decide quantos passos sobe ou desce: um preenchimento de 8px pode ir a 4px e 12px; um de 16px pode ir a 8px e 24px. O gov.br usa a mesma escala de 4px e o mesmo raciocínio de passos por componente ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). O Blueprint também deriva as medidas de um passo de 4px: o botão padrão tem 7,5 passos de altura e o grande tem 10 ([Blueprint](https://blueprintjs.com/docs/)).

O kit expressa os níveis com tokens `--d-*`, que `[data-density]` troca:

| Token         | Alta              | Padrão            | Baixa             |
|---------------|-------------------|-------------------|-------------------|
| `--d-control` | 32px (`--c-h-sm`) | 40px (`--c-h-md`) | 48px (`--c-h-lg`) |
| `--d-pad-x`   | `--sp-300` (12px) | `--sp-400` (16px) | `--sp-600` (24px) |
| `--d-pad-y`   | `--sp-200` (8px)  | `--sp-300` (12px) | `--sp-400` (16px) |
| `--d-gap`     | `--sp-200` (8px)  | `--sp-300` (12px) | `--sp-400` (16px) |
| `--d-row`     | 44px              | 56px              | 64px              |
| `--d-cell-y`  | `--sp-150` (6px)  | `--sp-300` (12px) | `--sp-400` (16px) |

### Valores por componente

| Componente                        | Medida                                           | Alta    | Padrão  | Baixa   | Como aplicar                                                                      |
|-----------------------------------|--------------------------------------------------|---------|---------|---------|-----------------------------------------------------------------------------------|
| Botão (`.tr-btn`)                 | Altura e preenchimento lateral                   | 32 e 12 | 40 e 16 | 48 e 24 | Automático com `[data-density]`                                                   |
| Campo (`.tr-input`, `.tr-select`) | Altura                                           | 32      | 40      | 48      | Automático; o texto digitado continua em 16px                                     |
| Linha de lista (`.tr-list li`)    | Altura mínima                                    | 44      | 56      | 64      | Automático                                                                        |
| Célula de tabela (`.tr-table td`) | Altura da linha (texto de 20 mais preenchimento) | 32      | 44      | 52      | Automático, pelo preenchimento vertical `--d-cell-y`                              |
| Switch (`.tr-switch`)             | Trilho (largura e altura)                        | 32 e 18 | 40 e 22 | 52 e 30 | Classe `.tr-switch--sm` ou `.tr-switch--lg`; a linha do rótulo mantém `--c-touch` |

Valores em px CSS. As diferenças entre níveis são sempre múltiplos de 4px.

### Mínimos

**Mantenha pelo menos 4px de área de leitura.** Entre o conteúdo e a borda da superfície do componente, nunca deixe menos que `--sp-100`, em nenhum nível ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)).

**Garanta a área de ação: 24px com mouse e 44px no toque.** Com apontador fino, o alvo tem pelo menos 24 por 24px, o mínimo da WCAG 2.2, 2.5.8. No toque, o alvo tem `--c-touch` (44px). A área de ação pode ultrapassar a superfície visível: um switch de trilho com 18px de altura continua com a linha inteira de 44px clicável, e um ícone de 24px pode ter preenchimento invisível até 44px. O gov.br prevê essa área estendida quando a superfície não alcança o mínimo ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)).

> **Divergência entre referências** O gov.br fixa 24px para mouse e 40px para toque ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). A Apple recomenda 44 por 44pt como tamanho padrão de controle no iPadOS e 28 por 28pt no macOS, com mínimos de 28 e 20 ([HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)). O Trama decide 44px no toque, pelo critério de acessibilidade, com mais margem, e 24px com mouse, o mínimo do critério WCAG 2.2, 2.5.8.

### Como ajustar

**Ajuste por preenchimento ou por dimensão.** Há duas formas: mudar o preenchimento interno (nos quatro lados ou só em dois lados opostos) ou mudar a largura e a altura do componente ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). O botão do kit muda altura e preenchimento lateral; a célula de tabela muda só o preenchimento vertical; a linha de lista muda só a altura mínima.

**Mude só dimensões e espaços.** Tamanho de fonte, peso, cor, raio e alinhamento interno ficam iguais nos três níveis. Uma tabela em densidade alta continua com Body small e com as mesmas colunas.

**Use o mesmo nível em componentes vizinhos.** Um botão de 32px ao lado de um campo de 40px quebra o alinhamento da linha. Aplique `data-density` no contêiner comum, e não em cada componente.

**Fique nos três níveis.** O gov.br permite criar níveis além dos três para casos extremos ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)). O Trama não publica outros níveis: um caso que não caiba em alta, padrão ou baixa é levado à equipe do sistema.

### Quando usar cada nível

| Nível  | Use em                                                                                                                                                           | Evite em                                                                                                                                       |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Alta   | Tabelas extensas, listas longas, ferramentas de trabalho e painéis de controle, sempre com apontador fino (mouse ou trackpad); botões dentro de linhas de tabela | Toque, classe Compacta, alertas, mensagens e banners, formulários de serviço ao público, elementos de interação frequente ou de leitura rápida |
| Padrão | A maior parte das telas com mouse e teclado                                                                                                                      | Telas de toque, onde a baixa é obrigatória                                                                                                     |
| Baixa  | Qualquer tela de toque, a classe Compacta inteira, formulários longos de serviço público, elementos que precisam de destaque                                     | Tabelas de trabalho em desktop, onde esconde dados sem ganho                                                                                   |

O gov.br lista os mesmos usos: otimizar tabelas e listas grandes, encaixar elementos em espaços pequenos, compactar componentes dentro de outros, ampliar o espaço para reduzir sobrecarga e dar foco a um elemento. Também pede para não aumentar a densidade em alertas e mensagens e para evitá-la em elementos de interação frequente ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)).

**Troque para baixa quando o apontador for grosso.** Uma ferramenta em densidade alta aberta num tablet precisa voltar à baixa. Ao carregar a página, marque a raiz com `data-density="baixa"` quando `matchMedia("(pointer: coarse)")` for verdadeiro, e garanta pelo CSS que regiões marcadas como alta também cedam:

``` code
@media (pointer: coarse), (max-width: 599px) {
  [data-density] {
    --d-control: var(--c-h-lg);
    --d-pad-x: var(--sp-600);
    --d-pad-y: var(--sp-400);
    --d-gap: var(--sp-400);
    --d-row: 64px;
    --d-cell-y: var(--sp-400);
  }
}
```

A Apple recomenda aproveitar telas grandes com densidade confortável, que não force a vista para ler ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos)). Ofereça a escolha de densidade nas configurações do produto quando o público trabalhar o dia inteiro com tabelas, e guarde a escolha por pessoa.

**Faça** mantenha alertas e mensagens na densidade padrão, mesmo dentro de uma tela densa.

**Não faça** use densidade alta num formulário aberto no celular. Botões de 32px ficam abaixo do alvo de toque de 44px.

### Considerações por plataforma

#### Web desktop

É a única plataforma onde a densidade alta é permitida, e só em regiões de trabalho: tabelas, listas e barras de ferramentas. O cabeçalho, a navegação principal e os formulários ficam no padrão.

#### Web móvel

A classe Compacta usa sempre a densidade baixa. Não há exceção para tabelas: em telas estreitas, reduza colunas antes de reduzir espaço.

#### Tablets e dobráveis

Com toque, use a baixa. Com teclado e trackpad conectados, a padrão é aceitável, mas a pessoa pode voltar ao toque a qualquer momento; prefira a baixa quando não souber o método de entrada. A Apple lembra que no iPad as pessoas combinam toque, teclado, apontador e caneta ([HIG](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados)).

### Recursos

#### Relacionados

- Espaçamento
- Estados de interação
- Tabelas
- Listas
- Botões
- Toque e gestos
- Mouse e trackpad

#### Referências

- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) Apple HIG
- [Designing for iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados) Apple HIG
- [Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) Apple HIG
- [Design tokens](https://blueprintjs.com/docs/) Blueprint

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## Legislação e normas

Produtos digitais para o público brasileiro respondem a leis de acessibilidade, de proteção de dados e de governo digital; o Trama traduz essas exigências em requisitos de design, sem substituir a orientação jurídica.

Esta página reúne as leis e normas que o Trama considera ao definir componentes e padrões, e diz o que as referências do sistema afirmam sobre cada uma. Ela não é um parecer jurídico. O GOV.UK faz o mesmo alerta: a organização responsável pelo serviço responde pelo cumprimento da legislação de proteção de dados, e as orientações de design não são aconselhamento legal ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/)). Consulte a área jurídica e a pessoa encarregada de dados da sua organização.

O Trama adota a WCAG 2.2 no nível AA como meta em todos os produtos. Produtos para o público brasileiro também observam a Lei nº 13.146/2015 e a Lei nº 13.709/2018. Produtos para órgãos públicos observam ainda a Lei nº 14.129/2021 e o eMAG.

### O que se aplica a cada produto

| Norma                       | Todo produto Trama | Público brasileiro | Órgãos públicos |
|-----------------------------|--------------------|--------------------|-----------------|
| WCAG 2.2, nível AA          | Sim                | Sim                | Sim             |
| Lei nº 13.146/2015, art. 63 |                    | Sim                | Sim             |
| Lei nº 13.709/2018 (LGPD)   |                    | Sim                | Sim             |
| Lei nº 14.129/2021          |                    |                    | Sim             |
| eMAG                        |                    |                    | Sim             |

Quando uma norma exigir mais do que o Trama, vale a norma. O GOV.UK segue a mesma regra: se uma regulação exigir uma versão mais nova da WCAG ou um prazo menor, a exigência regulatória tem precedência ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/)).

### Acessibilidade

#### Lei nº 13.146/2015, Estatuto da Pessoa com Deficiência

A lei, de 6 de julho de 2015, destina-se a assegurar e promover, em condições de igualdade, os direitos e as liberdades fundamentais da pessoa com deficiência. Ela define acessibilidade como a possibilidade e a condição de alcance para utilização, com segurança e autonomia, de espaços, equipamentos, transportes, informação e comunicação, inclusive seus sistemas e tecnologias ([gov.br DS](https://www.gov.br/ds/acessibilidade)).

O artigo 63 torna obrigatória a acessibilidade nos sítios da internet mantidos por empresas com sede ou representação comercial no País ou por órgãos de governo, para uso da pessoa com deficiência, conforme as melhores práticas e diretrizes de acessibilidade adotadas internacionalmente ([gov.br DS](https://www.gov.br/ds/acessibilidade)). O gov.br identifica essas diretrizes internacionais com a WCAG, do W3C ([gov.br DS](https://www.gov.br/ds/acessibilidade)).

> **Nota** Na lista de referências da página de acessibilidade do gov.br, a Lei nº 13.146/2015 aparece com o rótulo "Lei do Governo Digital", que pertence à Lei nº 14.129/2021 ([gov.br DS](https://www.gov.br/ds/acessibilidade)). No texto da mesma página, a Lei nº 13.146/2015 é chamada corretamente de Estatuto da Pessoa com Deficiência. O Trama usa os nomes do texto.

#### Lei nº 14.129/2021, Lei do Governo Digital

A lei, de 29 de março de 2021, dispõe sobre princípios, regras e instrumentos para aumentar a eficiência da administração pública, especialmente por meio da desburocratização, da inovação, da transformação digital e da participação do cidadão. Segundo o gov.br, ela estabelece a acessibilidade como princípio e diretriz do Governo Digital, e seu artigo 3º estende a obrigação aos serviços digitais em dispositivos móveis ([gov.br DS](https://www.gov.br/ds/acessibilidade)). Por isso, no Trama, um serviço público que só funciona bem no desktop não está conforme.

#### eMAG, Modelo de Acessibilidade em Governo Eletrônico

O eMAG é o norteador do desenvolvimento e da adaptação de conteúdos digitais do governo federal. Suas recomendações permitem implementar a acessibilidade de forma padronizada, coerente com as necessidades brasileiras e em conformidade com os padrões internacionais, e se baseiam na WCAG ([gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html)). O eMAG define três passos ([gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html)):

1.  Seguir os padrões web do W3C, com HTML válido e semântico.
2.  Seguir as diretrizes de acessibilidade.
3.  Avaliar a acessibilidade, com validadores automáticos seguidos de validação manual por checklist, porque os validadores sozinhos não determinam se um site é acessível.

O guia de HTML do gov.br cita, entre as práticas do eMAG: um único `h1` e títulos em hierarquia, listas pela finalidade, tabelas só para dados, idioma declarado em todas as páginas, texto alternativo em imagens e rótulos associados aos campos ([gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html)). O Trama incorpora todas em Acessibilidade e HTML acessível e WAI-ARIA.

#### WCAG 2.2

As Diretrizes de Acessibilidade para Conteúdo Web, do W3C, organizam requisitos em quatro princípios (perceptível, operável, compreensível e robusto) e três níveis de conformidade: A, AA e AAA ([gov.br DS](https://www.gov.br/ds/acessibilidade)). O gov.br trabalha com o nível AA ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/cores)). A versão 2.2 mantém os critérios da 2.1, com exceção do 4.1.1, que deixou de ser exigido, e acrescenta critérios como 2.4.11 (foco não encoberto), 2.5.7 (movimentos de arrastar), 2.5.8 (tamanho do alvo) e 3.3.8 (autenticação acessível).

> **Divergência entre referências** O gov.br e o eMAG descrevem a WCAG 2.1 ([gov.br DS](https://www.gov.br/ds/acessibilidade), [gov.br DS](https://www.gov.br/ds/guias/acessibilidade-html)). O GOV.UK já usa a WCAG 2.2 AA ([GOV.UK](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/)), e o HDS acompanha a 2.2 por precaução, embora a norma europeia que ele segue cite versões anteriores ([HDS](https://hds.hel.fi/about/accessibility/hds-accessibility)). Pelo critério de acessibilidade com mais margem, o Trama adota a 2.2 AA; quem cumpre a 2.2 cumpre também os critérios mantidos da 2.1.

#### Norma do Padrão Digital de Governo

A página de legislação do gov.br lista a norma que disciplina a implantação e a gestão do Padrão Digital de Governo nos órgãos e entidades do Poder Executivo federal ([gov.br DS](https://www.gov.br/ds/downloads/legislacao)). Produtos Trama feitos para esses órgãos devem confirmar com o órgão contratante como essa norma se aplica, inclusive quanto ao uso da identidade visual do governo, tratada em Marca.

### Proteção de dados

#### Lei nº 13.709/2018, Lei Geral de Proteção de Dados Pessoais

O gov.br trata a LGPD como requisito de interface em dois pontos. Primeiro, o cookiebar é obrigatório em produtos do governo que coletam ou tratam dados das pessoas, e deve permitir dar e revogar consentimento, ver a finalidade, a duração e os dados de cada cookie ([gov.br DS](https://www.gov.br/ds/components/cookiebar)). Segundo, todo formulário deve pedir o mínimo de informações absolutamente necessárias, com finalidade clara e informada para cada dado ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)).

As práticas de formulário que o gov.br associa à LGPD são ([gov.br DS](https://www.gov.br/ds/padroes/design/formulario)):

- explicar o motivo da coleta, principalmente de dados pessoais e sensíveis;
- deixar claro o benefício de preencher campos opcionais;
- exibir opções de consentimento sem marcação prévia e, sempre que possível, de forma granular;
- explicar como retirar o consentimento;
- oferecer recursos de anonimização de senhas e dados sensíveis e avisar quando um dado foi anonimizado;
- escrever políticas de privacidade em termos simples, sem "juridiquês", divididas por assunto.

O Trama aplica essas práticas em Privacidade e Consentimento de cookies.

### Outras referências e seus contextos legais

As referências estrangeiras do Trama respondem a outras leis. Elas ajudam a entender as decisões, mas não valem para produtos brasileiros.

| Sistema | Base legal citada                                                                                                                                                                                                                  | Padrão técnico                                                                                                                             |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| GOV.UK  | Regulações de acessibilidade do setor público; PECR e GDPR para cookies ([GOV.UK](https://design-system.service.gov.uk/accessibility/), [GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/))                  | WCAG AA na versão publicada há pelo menos um ano ([GOV.UK](https://design-system.service.gov.uk/accessibility/accessibility-strategy/))    |
| DKFDS   | Lei nº 692, de 8 de junho de 2018, a lei dinamarquesa de acessibilidade web; regulamento de cookies ([DKFDS](https://designsystem.dk/kom-i-gang/tilgaengelighed/), [DKFDS](https://designsystem.dk/komponenter/cookiemeddelelse/)) | EN 301 549 v3.2.1, cujos capítulos principais remetem à WCAG 2.1 ([DKFDS](https://designsystem.dk/kom-i-gang/tilgaengelighed/))            |
| HDS     | Diretiva europeia 2016/2102 de acessibilidade web ([HDS](https://hds.hel.fi/about/accessibility/hds-accessibility))                                                                                                                | WCAG 2.0 AA exigida; segue a 2.1, aplica critérios AAA e acompanha a 2.2 ([HDS](https://hds.hel.fi/about/accessibility/hds-accessibility)) |

A Apple não trata de leis nas diretrizes de design, mas pede que as equipes conheçam suas obrigações sobre rastreamento e respeitem as escolhas de privacidade das pessoas ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/privacy)).

### Boas práticas

**Identifique as normas no início do projeto.** Registre no documento do produto quem é o público, se o produto é de órgão público e quais dados pessoais ele trata. A tabela do início desta página indica o conjunto mínimo.

**Avalie com pessoas e não só com ferramentas.** Validadores automáticos não garantem conformidade em nenhum nível; o gov.br compara esses validadores a corretores gramaticais e exige avaliação humana por pessoas e especialistas ([gov.br DS](https://www.gov.br/ds/acessibilidade)).

**Use os componentes do Trama sem alterar sua acessibilidade.** Um componente modificado precisa continuar atendendo à WCAG 2.2 AA, exigência que o GOV.UK faz a quem estende seus componentes ([GOV.UK](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/)).

**Publique uma declaração de acessibilidade e uma política de privacidade.** O GOV.UK mantém uma declaração de acessibilidade para pessoas e equipes ([GOV.UK](https://design-system.service.gov.uk/accessibility/)). No Trama, as duas páginas ficam no rodapé de todo produto. Veja Rodapé.

### Considerações por plataforma

#### Web desktop

Nenhuma consideração adicional para Web desktop.

#### Web móvel

Para serviços públicos, a Lei nº 14.129/2021 inclui os dispositivos móveis no alcance da obrigação de acessibilidade, segundo o gov.br ([gov.br DS](https://www.gov.br/ds/acessibilidade)). Teste toda tarefa na classe Compacta, com leitor de tela e zoom.

#### Tablets e dobráveis

Nenhuma consideração adicional para Tablets e dobráveis: as mesmas normas valem para a tela externa e a interna.

### Recursos

#### Relacionados

- Acessibilidade
- Privacidade
- Consentimento de cookies
- HTML acessível e WAI-ARIA
- Padrão mínimo

#### Referências

- [Acessibilidade](https://www.gov.br/ds/acessibilidade) gov.br DS
- [Acessibilidade no código HTML](https://www.gov.br/ds/guias/acessibilidade-html) gov.br DS
- [Cookiebar](https://www.gov.br/ds/components/cookiebar) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Cores](https://www.gov.br/ds/fundamentos-visuais/cores) gov.br DS
- [Legislação](https://www.gov.br/ds/downloads/legislacao) gov.br DS
- [Lei nº 13.146/2015](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm) Planalto
- [Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709.htm) Planalto
- [Lei nº 14.129/2021](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14129.htm) Planalto
- [Modelo de Acessibilidade em Governo Eletrônico (eMAG)](http://emag.governoeletronico.gov.br/) Governo Federal
- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) W3C
- [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) Apple HIG
- [Accessibility](https://design-system.service.gov.uk/accessibility/) GOV.UK Design System
- [Accessibility strategy](https://design-system.service.gov.uk/accessibility/accessibility-strategy/) GOV.UK Design System
- [Extending and modifying components](https://design-system.service.gov.uk/get-started/extending-and-modifying-components/) GOV.UK Design System
- [Cookie banner](https://design-system.service.gov.uk/components/cookie-banner/) GOV.UK Design System
- [Tilgængelighed](https://designsystem.dk/kom-i-gang/tilgaengelighed/) Det Fælles Designsystem
- [Cookiemeddelelse](https://designsystem.dk/komponenter/cookiemeddelelse/) Det Fælles Designsystem
- [HDS Accessibility](https://hds.hel.fi/about/accessibility/hds-accessibility) Helsinki Design System

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

## Ilustração

Uma ilustração explica uma ideia ou um estado de forma mais rápida e acolhedora do que o texto sozinho, desde que tenha uma função clara e nunca carregue informação que só ela transmite.

O Padrão Digital de Governo define ilustração como uma imagem que comunica um estado de forma mais amigável e ajuda a transmitir ideias simples ou complexas. Por ser uma ferramenta visual e emocional poderosa, ela deve ser usada com moderação: usada só como decoração, perde o poder de comunicar e distrai ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). O GOV.UK restringe o uso ao mesmo papel: mostrar de forma simplificada algo complexo, como uma interação física ou o lugar de um número num documento ([GOV.UK](https://design-system.service.gov.uk/styles/images/)).

Esta página define quando usar ilustração, como compor, quais cores e tamanhos usar e como torná-la acessível. Fotografia está em Imagens; ícones, em Iconografia.

### Quando usar

**Use ilustração só num cenário previsto.** O gov.br lista quatro cenários: estados vazios, onboarding, mensagens com título e corpo (informativas ou de erro) e chamadas para ação ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). O Trama acrescenta instruções físicas, como enquadrar um documento na câmera, do GOV.UK ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Se a ilustração não se encaixar em nenhum cenário, ela provavelmente não é a melhor solução ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)).

| Cenário                     | Para quê                                                                                                                | Componente        |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------|
| Estado vazio                | Mostrar o estado do sistema, para que serve a área e o que fazer a seguir. Nunca para mensagens de validação de campos. | Estados vazios    |
| Onboarding                  | Apresentar um recurso novo ou pouco usado.                                                                              | Onboarding        |
| Mensagem com título e corpo | Configuração necessária, manutenção, página indisponível, sem conexão.                                                  | Modelos de página |
| Chamada para ação           | Ilustração da ação esperada, título e frase de destaque.                                                                | Cards             |
| Instrução física            | Mostrar uma interação com objeto real ou onde achar um dado num documento.                                              | Imagem            |

Os cenários e o uso em estados vazios seguem o gov.br ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)).

**Escolha ilustração para o abstrato e foto para o real.** Ilustrações funcionam melhor com assuntos abstratos, processos, diagramas e fluxos; representações que precisam ser realistas funcionam melhor com fotografia ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Ideias simples e únicas cabem num ícone ([Ontario](https://designsystem.ontario.ca/components/detail/icons-primary.html)).

**Nunca ponha corpo de mensagem sem título.** A ilustração pode vir com título e corpo, ou só com título; corpo sem título não ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)).

### Anatomia

O gov.br decompõe a ilustração em oito elementos ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). O Trama mantém a lista e ajusta o que é obrigatório.

| Elemento           | gov.br      | Trama                 | Regra do Trama                                                                          |
|--------------------|-------------|-----------------------|-----------------------------------------------------------------------------------------|
| Elementos de fundo | Obrigatório | Opcional              | Formas geométricas simples que unem a composição sem competir com o elemento principal. |
| Spot ou objeto     | Obrigatório | Obrigatório           | O foco da história; em estados vazios, costuma ser o único elemento.                    |
| Luz e sombra       | Obrigatório | Opcional              | Só camadas de preto ou branco em opacidade, nunca uma cor nova.                         |
| Personagem         | Opcional    | Opcional              | Evite em ilustrações funcionais; quando usar, represente a diversidade brasileira.      |
| Cor                | Opcional    | Obrigatório           | Até 5 cores da paleta de tokens, na proporção 60/30/10.                                 |
| Linha de contorno  | Opcional    | Opcional              | Traço de 1 ou 2px, terminais e junções arredondados, em `currentColor`.                 |
| Textura e padrões  | Opcional    | Só em alta fidelidade | Fora da interface de tarefas, como em capas de onboarding.                              |

### Boas práticas

#### Estilo

**Use cores chapadas e poucos elementos.** Comunique com o menor número possível de elementos visuais; evite sombras e degradês, exceto para mostrar uma característica do objeto ou profundidade, e mantenha cores, espessuras de linha e raios iguais em todas as ilustrações do serviço ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Num mesmo produto, estilos diferentes convivem se paleta, luz e sombra e traço forem consistentes ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)).

> **Divergência entre referências** O gov.br torna luz e sombra obrigatórias, aplicadas com camadas de preto e branco em modo de mesclagem luz suave, em incrementos de 10% de opacidade, e usa degradês e texturas granuladas no estilo de alta fidelidade ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). O GOV.UK pede cores chapadas e evita sombras e degradês ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Nenhuma das duas cita pesquisa. O Trama decide pela cor chapada como padrão, porque ela se adapta aos temas claro e escuro só com a troca de tokens, e aceita luz e sombra pelo método do gov.br, que também não cria cores novas. Degradês e texturas ficam restritos a ilustrações de alta fidelidade fora da interface de tarefas.

**Escolha o estilo pela intenção.** O gov.br descreve três eixos: abstrato ou literal, micro ou macro, baixa ou alta fidelidade ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Para instruções e estados, o Trama usa literal e baixa fidelidade, que explicam mais e cansam menos. Abstrato e alta fidelidade servem a onboarding e páginas de entrada.

**Ajuste a complexidade ao espaço.** O gov.br organiza as ilustrações em modelos (cenas com vários personagens, para áreas grandes), organismos, moléculas (pequenas e versáteis) e ícones ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Na interface de tarefas, use moléculas e spots.

#### Cor

**Use até 5 cores, na proporção 60/30/10.** Uma cor dominante, uma secundária em harmonia e de uma a três de destaque; as outras cores permitidas são de sombreamento ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Monocromia e cores análogas, com dois ou três matizes vizinhos, são as combinações mais seguras; cores complementares ficam para detalhes ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)).

**Não use a cor de ação como cor dominante.** A cor de elementos interativos numa ilustração compete com eles e pode obscurecer o que importa no layout ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). No Trama, `--t-brand` aparece só como destaque (os 10%); a base usa `--t-brand-subtle`, `--t-surface-2` e `--t-border`.

**Reserve vermelho e amarelo para alertas.** Esses tons são das mensagens da interface e só entram numa ilustração em casos específicos, como tons de pele ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Não use `--t-danger` nem `--t-warning` como cor decorativa.

**Ofereça versões para os dois temas.** Com SVG, prefira `currentColor` e variáveis de token, para que a ilustração mude com o tema. O gov.br define a linha de contorno em preto `#000000` ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)); o Trama usa `--t-fg-1`, que se inverte no tema escuro. Veja Modo escuro.

#### Pessoas e diversidade

**Evite pessoas em ilustrações funcionais.** O GOV.UK recomenda evitar pessoas e, quando necessário, não mostrar só um tipo de pessoa ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Ilustrações abstratas e conceituais também tornam o conteúdo mais inclusivo ([HDS](https://hds.hel.fi/foundation/guidelines/inclusivity)).

**Quando houver personagens, represente a pluralidade brasileira sem estereótipos.** O gov.br pede personagens variados em gênero, etnia e ocupação, com tons de pele e cores de cabelo diversos, tomando como referência as categorias de cor ou raça do IBGE: brancos, pardos, pretos, amarelos e indígenas ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Evite estereótipos de ocupação e inclua pessoas com deficiência ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). Veja Inclusão.

#### Tom

**Mantenha ilustrações de erro sóbrias.** Numa página de erro, a ilustração ajuda a reconhecer o tipo de problema, sem humor e sem personagens em situação cômica. O texto diz o que aconteceu e como resolver.

**Faça** Use uma ilustração simples e um texto que diga o que fazer.

**Não faça** Use humor ou "Ops" para suavizar o erro.

> **Divergência entre referências** O gov.br sugere suavizar situações de erro com ilustrações lúdicas ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). O próprio gov.br pede para não fazer humor em mensagens de erro ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)), e a Apple lembra que o humor é subjetivo e cansa com a repetição ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)). O Trama mantém o tom neutro também na ilustração: erros não têm humor, em texto nem em imagem.

#### Tamanhos e formato

**Use a variante certa para o espaço.** A maioria das ilustrações existe em dois tamanhos; abaixo de 160px os detalhes viram ruído ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)).

| Largura disponível | Use                                                        |
|--------------------|------------------------------------------------------------|
| Mais de 160px      | Variante grande                                            |
| De 80 a 160px      | Variante pequena, reduzida ao essencial                    |
| Menos de 80px      | Ícone, no máximo `--icon-3xl` (64px), em vez de ilustração |

Os limites seguem o gov.br ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)).

**Entregue em SVG.** SVG redimensiona sem pixelização, permite trocar cores e costuma gerar arquivos menores ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). A Apple recomenda PDF ou SVG para arte plana que precisa escalar e pede testes em aparelhos reais ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/images)).

### Acessibilidade

**Ponha toda a informação no texto.** Imagens são apoio visual; o texto precisa conter tudo o que a pessoa precisa para concluir o serviço ([GOV.UK](https://design-system.service.gov.uk/styles/images/)). Assim, a ilustração pode ser decorativa.

**Oculte ilustrações decorativas e nomeie as informativas.** Uma ilustração decorativa recebe `aria-hidden="true"` no SVG, como pede o gov.br ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Se ela mostrar algo que o texto não diz, como onde fica um número num documento, use `role="img"` com um nome de até 125 caracteres (WCAG 2.2, 1.1.1). Veja Imagens.

> **Divergência entre referências** O gov.br exige `aria-hidden="true"` em toda tag SVG de ilustração ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). O GOV.UK pede texto alternativo quando a imagem traz detalhes que o texto não inclui ([GOV.UK](https://design-system.service.gov.uk/styles/images/)), e a WCAG 1.1.1 exige alternativa para conteúdo não textual informativo. Pelo critério de acessibilidade, o Trama oculta só as decorativas.

**Garanta 3:1 nos elementos que carregam significado.** Se a ilustração transmite informação que o texto não captura por inteiro, os conceitos principais precisam de contraste de 3:1 ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao); WCAG 2.2, 1.4.11).

**Não coloque texto dentro da ilustração.** Texto em imagem não pode ser lido por leitor de tela, ampliado ou traduzido ([GOV.UK](https://design-system.service.gov.uk/styles/images/)).

**Não anime ilustrações sem controle.** Animações respeitam `prefers-reduced-motion` e o controle de animações do produto. Veja Movimento.

### Considerações por plataforma

#### Web desktop

Ilustrações grandes cabem em páginas de entrada e onboarding. Em telas de trabalho, use spots pequenos e não ocupe a área de conteúdo.

#### Web móvel

Planeje a ilustração para cada grade: uma capa horizontal no desktop pode precisar de proporção quadrada ou vertical no celular, e nas grades de 8 e 4 colunas o gov.br usa variantes resumidas, com menos detalhes ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/ilustracao)). Na classe Compacta, use a variante pequena e não deixe a ilustração empurrar a ação principal para fora da primeira tela.

#### Tablets e dobráveis

Ao abrir ou fechar um dobrável, troque a variante pela largura disponível, não pelo tipo de aparelho. Não deixe o elemento principal da ilustração sobre a dobra.

### Recursos

#### Relacionados

- Imagens
- Iconografia
- Estados vazios
- Onboarding
- Inclusão
- Marca
- Modo escuro

#### Referências

- [Ilustração](https://www.gov.br/ds/fundamentos-visuais/ilustracao) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Images](https://design-system.service.gov.uk/styles/images/) GOV.UK Design System
- [Images](https://developer.apple.com/design/human-interface-guidelines/images) Apple HIG
- [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) Apple HIG
- [Inclusivity](https://hds.hel.fi/foundation/guidelines/inclusivity) Helsinki Design System
- [Primary icons](https://designsystem.ontario.ca/components/detail/icons-primary.html) Ontario Design System
- [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) W3C

### Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |

