# Links

Um link leva a pessoa a outra página, a outro site, a outro ponto da mesma página ou a um arquivo.

O link é o elemento de navegação mais básico da web. No Trama ele usa a classe `.tr-link`: cor `--t-link`, sublinhado de 1px em repouso e de 3px no hover, e cor de visitado `--t-link-visited`. O modificador `.tr-link--external` acrescenta o ícone de link externo. O gov.br trata o hiperlink como elemento de ação, ao lado do botão, e pede textos que indiquem o destino com clareza ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Quando usar.** Para navegar para outra página da aplicação, para outro site, para uma seção da mesma página e para endereços de e-mail ou telefone ([HDS](https://hds.hel.fi/components/link), [DKFDS](https://designsystem.dk/styleguide/typografi/links/)). Hiperlinks também permitem saltar para qualquer nível da hierarquia, mesmo os não adjacentes ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)); veja Estruturar a navegação.

**Quando não usar.** Para ações que mudam dados ou estado, como salvar ou excluir, use um botão ([Fluent](https://fluent2.microsoft.design/components/web/react/core/link/usage)). Para voltar ao passo anterior de um fluxo, use o link de voltar descrito em Breadcrumb. Para a navegação principal, use a barra de navegação ou a navegação lateral.

## Anatomia

1.  **Texto do link**: descreve o destino. É a única parte obrigatória.
2.  **Sublinhado**: segunda pista visual além da cor. Aparece em repouso no link padrão.
3.  **Ícone de destino** (condicional): ao fim do texto, na mesma cor dele ([HDS](https://hds.hel.fi/components/link/accessibility)). O ícone de link externo é obrigatório em links que saem do domínio do produto.
4.  **Indicação de tipo** (opcional): formato e tamanho de arquivo entre parênteses.
5.  **Texto acessível complementar** (condicional): “(site externo)” ou “(abre em nova aba)”.

## Tipos

| Tipo                   | Classe                                      | Uso                                                                                                                                                     |
|------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Padrão                 | `.tr-link`                                  | Quase todos os casos. É o tipo mais acessível ([Fluent](https://fluent2.microsoft.design/components/web/react/core/link/usage)).                        |
| Externo                | `.tr-link.tr-link--external`                | Destinos fora do domínio do produto ([DKFDS](https://designsystem.dk/styleguide/typografi/links/), [gov.br DS](https://www.gov.br/ds/components/menu)). |
| Sutil                  | `.tr-link--subtle`                          | Áreas claramente navegacionais, como rodapé, onde a posição já indica que o texto é link.                                                               |
| Avulso                 | `.tr-link` em parágrafo próprio             | Links listados depois do conteúdo, muitas vezes com ícone do tipo de destino ([HDS](https://hds.hel.fi/components/link)).                               |
| Sem estado de visitado | `.tr-link` com cor de visitado neutralizada | Páginas cujo conteúdo muda com frequência, como painéis administrativos ([GOV.UK](https://design-system.service.gov.uk/styles/links/)).                 |

## Boas práticas

**Dê ao link pelo menos duas pistas visuais.** Cor e sublinhado, ou cor e ícone. Um link nunca é indicado só pela cor ([Fluent](https://fluent2.microsoft.design/components/web/react/core/link/usage), [DKFDS](https://designsystem.dk/styleguide/typografi/links/); WCAG 2.2, 1.4.1).

**Remova o sublinhado só quando o contexto deixa claro que é link.** Cabeçalhos, navegação lateral e rodapés são esses lugares ([GOV.UK](https://design-system.service.gov.uk/styles/links/)).

**Use poucos links no meio do texto.** Muitos links embutidos interrompem a leitura ([HDS](https://hds.hel.fi/components/link)). Em fluxos de serviço, links para fora podem tirar a pessoa do contexto; mantenha só os que ajudam a completar a tarefa ([DKFDS](https://designsystem.dk/styleguide/typografi/links/)).

**Abra na mesma aba por padrão.** Uma nova aba desorienta e causa problemas para quem não percebe visualmente que ela abriu ([GOV.UK](https://design-system.service.gov.uk/styles/links/)). Abra em nova aba só quando a pessoa perderia dados preenchidos, diga “(abre em nova aba)” no texto do link e acrescente `rel="noopener noreferrer"` ([GOV.UK](https://design-system.service.gov.uk/styles/links/)).

**Marque o link que sai do produto.** Use `.tr-link--external` e inclua “(site externo)” em texto visualmente oculto, porque o ícone sozinho não chega ao leitor de tela. Nomeie também o site no texto, como “tabela de tarifas do Banco Central” ([GOV.UK](https://design-system.service.gov.uk/styles/links/)).

> **Divergência entre referências** O DKFDS manda abrir links externos sempre em nova aba e com ícone ([DKFDS](https://designsystem.dk/styleguide/typografi/links/)). O GOV.UK pede para não usar ícone de link externo, deixar o destino claro no texto e evitar nova aba ([GOV.UK](https://design-system.service.gov.uk/styles/links/)). O HDS usa ícone ([HDS](https://hds.hel.fi/components/link)), e o gov.br usa o ícone de link externo nos links do rodapé do menu ([gov.br DS](https://www.gov.br/ds/components/menu)). A versão 1.0 do Trama dispensava o ícone quando o texto nomeava o site. Pela decisão transversal D14, o Trama passa a usar o ícone com texto acessível em todo link externo, posição da maioria, e mantém a regra do GOV.UK sobre a aba: mesma aba por padrão.

**Avise quando o link leva a um arquivo.** Escreva o formato entre parênteses se ele não estiver no texto, como “(PDF)” ([DKFDS](https://designsystem.dk/styleguide/typografi/links/)), e o tamanho, com a unidade abreviada só nesse caso: “(PDF, 1,2 MB)”.

**Avise antes de a pessoa perder dados.** Se seguir um link descarta respostas não salvas, peça confirmação antes de sair ([DKFDS](https://designsystem.dk/styleguide/typografi/links/)).

**Faça** Use palavras-chave que façam sentido fora da frase e digam para onde o link leva.

**Não faça** Use “clique aqui”, “saiba mais” sem complemento ou o endereço da página como texto.

### Estados

Repouso, hover, foco, pressionado e visitado. No hover, o sublinhado engrossa de `--stroke-thin` para `--stroke-thicker`. O foco aparece em `:focus-visible`, com o anel de `--t-focus`. O visitado usa `--t-link-visited` ([DKFDS](https://designsystem.dk/styleguide/typografi/links/)). Todo efeito de hover também funciona com teclado ([DKFDS](https://designsystem.dk/styleguide/typografi/links/)). Link não tem estado desabilitado: se o destino não existe para a pessoa, retire o link e deixe o texto comum.

### Comportamento

Enter ativa o link e leva ao destino ([HDS](https://hds.hel.fi/components/link/accessibility)). Links para âncoras na mesma página movem o foco para o alvo. Quando a pessoa precisa encontrar uma configuração, ofereça um link direto para ela em vez de descrever o caminho ([HIG](https://developer.apple.com/design/human-interface-guidelines/writing)). Links longos quebram a linha normalmente; o ícone externo acompanha a última palavra.

## Conteúdo

**Seja objetivo e indique o destino.** Prefira palavras-chave a frases longas e evite “clique aqui” e “saiba mais” ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy), [HIG](https://developer.apple.com/design/human-interface-guidelines/writing)). Quem usa leitor de tela navega pulando de link em link e precisa decidir sem ler o contexto ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Forneça links quando se referir a algo relevante.** Se o texto menciona uma norma, um formulário ou um serviço, ligue o nome a ele ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Deixe a pontuação de fora do link.** Se o link termina a frase, o ponto final fica fora do texto clicável ([GOV.UK](https://design-system.service.gov.uk/styles/links/)). Links avulsos não levam ponto final.

**Use caixa de frase.** Só a primeira palavra e os nomes próprios em maiúscula ([Fluent](https://fluent2.microsoft.design/components/web/react/core/link/usage)).

**Não repita o mesmo texto para destinos diferentes.** Vários “Ver detalhes” numa lista obrigam a pessoa a procurar o contexto em volta ([HDS](https://hds.hel.fi/components/link/accessibility)).

## Acessibilidade

**Use sempre `<a>` com `href`.** Sem `href`, o link não recebe foco nem aparece na lista de links do leitor de tela ([DKFDS](https://designsystem.dk/styleguide/typografi/links/)).

**Garanta que o propósito se entende pelo texto ou pelo contexto programático.** Tecnologias assistivas oferecem uma lista de todos os links da página ([HDS](https://hds.hel.fi/components/link/accessibility); WCAG 2.2, 2.4.4). Quando um texto genérico for inevitável, complete com texto visualmente oculto (`.tr-visually-hidden`), como “Ver detalhes do pedido 4821”. Prefira esse recurso ao `aria-label`, porque o nome acessível precisa conter o texto visível para quem usa controle por voz (WCAG 2.2, 2.5.3). O mesmo recurso leva “(site externo)” ao link com `.tr-link--external`.

**Descreva imagens que são links.** O `alt` da imagem diz o destino do link ([HDS](https://hds.hel.fi/components/link/accessibility)).

**Mantenha contraste.** `--t-link` sobre `--t-bg` atende 4,5:1 nos dois temas (WCAG 2.2, 1.4.3). Em faixas escuras, use `.tr-inverse`, que redefine `--t-link` para o valor escuro; o GOV.UK exige os mesmos 4,5:1 para links claros em fundo escuro ([GOV.UK](https://design-system.service.gov.uk/styles/links/)).

**Espace links avulsos.** Em toque, cada link avulso tem área de ação de `--c-touch`; com mouse, ao menos 24px (WCAG 2.2, 2.5.8). Links dentro de frases estão isentos desse critério.

## Tokens usados

| Token                               | Uso                                           |
|-------------------------------------|-----------------------------------------------|
| `--t-link`                          | Cor do link e do ícone externo                |
| `--t-link-visited`                  | Cor do link visitado                          |
| `--t-fg-1`                          | Cor do link sutil                             |
| `--stroke-thin`, `--stroke-thicker` | Espessura do sublinhado em repouso e no hover |
| `--t-focus`, `--stroke-thick`       | Anel de foco                                  |
| `--c-touch`                         | Área de ação de links avulsos em toque        |

## Considerações por plataforma

### Web desktop

O cursor de mão e o sublinhado mais grosso no hover confirmam que o texto é clicável. Não esconda o sublinhado em repouso no corpo do texto contando só com o hover.

### Web móvel

Não há hover. O sublinhado em repouso é a pista principal. Em listas de links avulsos, dê a cada link uma linha própria e área de toque de `--c-touch`. Links de telefone (`tel:`) e e-mail (`mailto:`) são especialmente úteis nessa classe.

### Tablets e dobráveis

Em layouts de dois painéis, um link na lista pode abrir o destino no painel de detalhe sem trocar a tela inteira. Nesse caso, o link mantém a semântica de navegação e atualiza o endereço da página.

## Recursos

### Relacionados

- Botões
- Breadcrumb
- Estruturar a navegação
- Escrita e conteúdo

### Referências

- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Navegação](https://www.gov.br/ds/padroes/design/navegacao) gov.br DS
- [Menu de Navegação](https://www.gov.br/ds/components/menu) gov.br DS
- [Writing](https://developer.apple.com/design/human-interface-guidelines/writing) Apple HIG
- [Link: usage](https://fluent2.microsoft.design/components/web/react/core/link/usage) Fluent 2
- [Links](https://design-system.service.gov.uk/styles/links/) GOV.UK Design System
- [Links](https://designsystem.dk/styleguide/typografi/links/) DKFDS
- [Link](https://hds.hel.fi/components/link) Helsinki Design System
- [Link: accessibility](https://hds.hel.fi/components/link/accessibility) Helsinki Design System

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Passa a exigir o ícone de link externo com texto acessível (D14), acrescenta regras de microcopy de hiperlinks e retira o estado desabilitado. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                  |
