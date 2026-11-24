# Breadcrumb

O breadcrumb mostra onde a página está na hierarquia do site e permite subir de nível com um clique.

O breadcrumb é uma navegação secundária: orienta a pessoa e dá acesso rápido aos níveis acima. Ele complementa a navegação principal ([gov.br DS](https://www.gov.br/ds/components/breadcrumb), [Fluent](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage), [DKFDS](https://designsystem.dk/komponenter/broedkrumme/)). É o componente da navegação reversa ascendente, que sobe pelos níveis até a página inicial ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). No Trama, ele é o `.tr-breadcrumb`, uma lista ordenada de links separados por barras. Esta página também cobre o **link de voltar**, usado na navegação reversa cronológica dos fluxos lineares.

**Quando usar.** Em sites e aplicações com vários níveis de hierarquia, para mostrar a localização e permitir voltar pelos níveis ([GOV.UK](https://design-system.service.gov.uk/components/breadcrumbs/), [gov.br DS](https://www.gov.br/ds/components/breadcrumb)).

**Quando não usar.** Em sites sem agrupamento ou hierarquia lógica ([gov.br DS](https://www.gov.br/ds/components/breadcrumb), [GOV.UK](https://design-system.service.gov.uk/components/breadcrumbs/)). Um mapa do site ajuda a decidir se o breadcrumb melhora a navegação entre categorias ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)). Para mostrar progresso num fluxo linear, use o indicador de etapas e o link de voltar. Nunca use breadcrumb e link de voltar na mesma página ([GOV.UK](https://design-system.service.gov.uk/components/back-link/)).

## Anatomia

1.  **Contêiner**: `<nav aria-label="Breadcrumb">` com uma lista ordenada.
2.  **Início**: primeiro item, sempre presente no tipo padrão, leva à página inicial ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)).
3.  **Itens anteriores**: links para os níveis acima, em `--t-link`.
4.  **Separador**: barra “/” em `--t-fg-3`, gerada por CSS, fora do foco e da leitura ([gov.br DS](https://www.gov.br/ds/components/breadcrumb), [Fluent](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage)).
5.  **Botão de níveis ocultos** (condicional): botão circular que abre a lista dos níveis truncados.
6.  **Página atual**: texto em `--t-fg-1`, peso 600, sem link, com `aria-current="page"` ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)).

## Tipos

| Tipo                | Uso                                                                                                                                                                                      |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Padrão              | Classes Média em diante: de Início até a página atual, cada item um link, exceto o último ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)).                                    |
| Padrão truncado     | Com mais de cinco itens, contando Início e a página atual, ou quando a trilha não cabe. Os intermediários vão para uma lista ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)). |
| Especial            | Classe Compacta, obrigatório: todos os níveis acima vão para a lista e só a página atual fica visível ao lado do botão ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)).       |
| Caminho informativo | Texto sem links que dá contexto num fluxo em que a pessoa não deve sair da tarefa ([Fluent](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage)).               |
| Link de voltar      | Fluxos lineares e páginas de pergunta: leva à página anterior, no estado em que a pessoa a deixou ([GOV.UK](https://design-system.service.gov.uk/components/back-link/)).                |

O gov.br permite usar o tipo especial também em telas largas; se o produto fizer essa escolha, ela vale para o produto inteiro e não se reverte ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)).

## Boas práticas

**Mostre a hierarquia, sem refletir o histórico.** Se várias rotas levam à mesma página, mostre um único caminho, o mais óbvio ([DKFDS](https://designsystem.dk/komponenter/broedkrumme/), [Fluent](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage)).

**Comece em Início e termine na página atual.** A página atual fica destacada e não é link ([gov.br DS](https://www.gov.br/ds/components/breadcrumb), [DKFDS](https://designsystem.dk/komponenter/broedkrumme/)). O GOV.UK termina na seção mãe e deixa a página atual para o título ([GOV.UK](https://design-system.service.gov.uk/components/breadcrumbs/)); o Trama inclui a página atual, como a maioria.

**Trunque preservando três pontos de apoio.** Ao truncar, nunca esconda Início, o último ancestral e a página atual; os níveis entre eles vão para a lista, na ordem da hierarquia, de cima para baixo ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)).

> **Divergência entre referências** O Fluent recolhe os itens a partir do segundo e mantém visíveis só o primeiro e o último ([Fluent](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage)), e a versão 1.0 do Trama seguia essa regra. O gov.br também preserva o último ancestral e começa a truncar quando há mais de cinco itens ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)). O Trama adota o gov.br, pelo critério de acessibilidade: o último ancestral é o destino mais usado para subir um nível e continua a um único Tab, sem abrir a lista.

**Encurte nomes longos.** Resuma o nome do nível; se ainda assim passar de 30 caracteres, trunque o rótulo com reticências e mostre o nome completo num tooltip no hover e no foco ([Fluent](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage), [gov.br DS](https://www.gov.br/ds/components/breadcrumb)). Nunca deixe menos de três caracteres de uma palavra. A página atual não é truncada: ela repete o título da página.

**Inclua só páginas que existem.** Categorias lógicas sem página de destino ficam fora ([DKFDS](https://designsystem.dk/komponenter/broedkrumme/)). Se precisar mostrá-las, escreva-as como texto comum, sem link e sem aparência de desabilitado.

**Posicione no topo, logo abaixo do cabeçalho e antes do `<main>`.** Use a mesma posição em todas as telas ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)). Assim o link “Pular para o conteúdo” também pula o breadcrumb ([GOV.UK](https://design-system.service.gov.uk/components/breadcrumbs/)).

**Faça** Use nomes curtos, iguais aos títulos das páginas, em caixa de frase.

**Não faça** Esconda Início no tipo padrão, mostre o histórico da pessoa e transforme a página atual em link.

### Comportamento

**Não quebre a trilha em várias linhas.** Quando ela não cabe, trunque como descrito acima ([Fluent](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage), [DKFDS](https://designsystem.dk/komponenter/broedkrumme/)). O breadcrumb ocupa entre 30% e 50% da largura da superfície ([Fluent](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage)).

**A lista de níveis ocultos segue o padrão dropdown.** Abre abaixo do botão, mantém o botão no estado ativado, não cria espaço extra e fecha com Esc, com clique fora ou ao escolher um nível ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)).

**Link de voltar.** Leva à página anterior no estado e na posição de rolagem em que a pessoa a deixou ([GOV.UK](https://design-system.service.gov.uk/components/back-link/), [gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). Se a página anterior não existe mais, mostre uma mensagem clara em vez de uma tela de erro sem contexto ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). Funciona sem JavaScript ou fica oculto quando isso não é possível, e fica no topo, antes do `<main>` ([GOV.UK](https://design-system.service.gov.uk/components/back-link/)). Não o use quando a pessoa pode ter chegado por pesquisa ou por um link externo ([DKFDS](https://designsystem.dk/komponenter/tilbage-link/)).

## Conteúdo

Use nomes curtos, específicos e fáceis de varrer, iguais ao título de cada página, em caixa de frase ([Fluent](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage)). No link de voltar, “Voltar” basta em jornadas simples; em sistemas com muitas áreas, use “Voltar para \[página\]” ([GOV.UK](https://design-system.service.gov.uk/components/back-link/)).

> **Divergência entre referências** O gov.br escreve links e título do breadcrumb em caixa alta e usa um botão de ícone de casa como primeiro item ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)). Pelas decisões D1 e D16, o Trama usa caixa de frase. O primeiro item é o texto “Início”, que se entende sem depender do reconhecimento de um ícone; se o produto usar o ícone, o botão leva `aria-label="Início"`.

## Acessibilidade

**Estruture com `<nav>`, `aria-label` e `<ol>`.** A lista ordenada comunica a sequência da hierarquia ([Fluent](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage), [HDS](https://hds.hel.fi/components/breadcrumb/accessibility)). O gov.br usa lista não ordenada ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)); o Trama mantém `ol`, posição da maioria, porque a ordem dos itens tem significado.

**Teclado.** Tab e Shift+Tab percorrem links e o botão de níveis ocultos; a página atual e os separadores ficam fora do foco. Enter abre a lista; o foco percorre os níveis e, ao fechar, volta ao fluxo da trilha ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)).

**Nomeie o botão de níveis ocultos.** Diga o que ele abre, como “Mostrar 3 níveis ocultos”, use `aria-expanded` e mostre o mesmo texto num tooltip ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)).

**Exponha o nome completo dos itens truncados.** O link mantém o nome inteiro como nome acessível; o tooltip mostra o mesmo texto no foco (decisão D15).

**Marque o item atual com `aria-current="page"`.** ([HDS](https://hds.hel.fi/components/breadcrumb/accessibility))

**Garanta o alvo de toque e o zoom.** Em toque, cada item tem área de ação de `--c-touch` ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)). Com zoom de 400%, a trilha passa ao tipo especial (WCAG 2.2, 1.4.10).

## Tokens usados

| Token                   | Uso                                  |
|-------------------------|--------------------------------------|
| `--t-link`              | Itens anteriores                     |
| `--t-fg-1`              | Página atual                         |
| `--t-fg-3`              | Separador                            |
| `--sp-100`              | Espaço entre item e separador        |
| `--c-h-sm`, `--o-hover` | Botão de níveis ocultos e seu estado |
| `--e-4`, `--z-2`        | Lista de níveis ocultos              |
| `--t-focus`             | Anel de foco                         |

## Considerações por plataforma

### Web desktop

Use o tipo padrão e trunque quando houver mais de cinco itens ou faltar espaço ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)).

### Web móvel

Na classe Compacta, use o tipo especial: o botão de níveis ocultos seguido da página atual ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)). O link de voltar continua visível nessa classe ([DKFDS](https://designsystem.dk/komponenter/tilbage-link/)).

> **Divergência entre referências** Em telas pequenas, o HDS mostra só o link para o nível imediatamente acima ([HDS](https://hds.hel.fi/components/breadcrumb)), o GOV.UK oferece uma variante que mostra o primeiro e o último item ([GOV.UK](https://design-system.service.gov.uk/components/breadcrumbs/)), e o gov.br exige o tipo especial, com todos os níveis acima numa lista ([gov.br DS](https://www.gov.br/ds/components/breadcrumb)). Não há maioria nem pesquisa citada. O Trama adota o gov.br pelo contexto brasileiro, por ser a convenção dos serviços públicos que o público do Trama já usa, e porque a lista mantém acesso a todos os níveis, que a versão 1.0 (só o nível acima) perdia.

### Tablets e dobráveis

Na classe Média, use o tipo padrão truncado. Em layouts de dois painéis, a hierarquia já aparece no painel da lista; avalie se o breadcrumb continua útil no detalhe. Ao abrir o dobrável e passar para a classe Média, troque o tipo especial pelo padrão, mantendo a página atual.

> **Nota** A HIG tem um componente parecido, o controle de caminho do macOS, em dois estilos: o padrão, que oculta os nomes entre o primeiro e o último item quando a lista não cabe, e o pop-up, que mostra só o item atual e abre um menu com os níveis acima ([HIG](https://developer.apple.com/design/human-interface-guidelines/path-controls)). O estilo pop-up corresponde ao tipo especial do Trama.

## Recursos

### Relacionados

- Estruturar a navegação
- Navegação lateral
- Links
- Formulários em etapas e páginas de pergunta
- Excesso de conteúdo

### Referências

- [Breadcrumb (Migalhas de Pão)](https://www.gov.br/ds/components/breadcrumb) gov.br DS
- [Navegação](https://www.gov.br/ds/padroes/design/navegacao) gov.br DS
- [Dropdown (Elemento Flutuante)](https://www.gov.br/ds/padroes/design/dropdown) gov.br DS
- [Path controls](https://developer.apple.com/design/human-interface-guidelines/path-controls) Apple HIG
- [Breadcrumb: usage](https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage) Fluent 2
- [Breadcrumbs](https://design-system.service.gov.uk/components/breadcrumbs/) GOV.UK Design System
- [Back link](https://design-system.service.gov.uk/components/back-link/) GOV.UK Design System
- [Brødkrumme](https://designsystem.dk/komponenter/broedkrumme/) DKFDS
- [Tilbage-link](https://designsystem.dk/komponenter/tilbage-link/) DKFDS
- [Breadcrumb](https://hds.hel.fi/components/breadcrumb) Helsinki Design System
- [Breadcrumb: accessibility](https://hds.hel.fi/components/breadcrumb/accessibility) Helsinki Design System

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                             |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Passa a truncar com mais de cinco itens preservando Início, último ancestral e página atual, adota o tipo especial na classe Compacta e acrescenta o retorno ao estado anterior no link de voltar. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                      |
