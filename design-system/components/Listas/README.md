# Listas

Uma lista organiza itens semelhantes em sequência, na vertical ou na horizontal, para que a pessoa os percorra, escolha um item ou aja sobre ele.

O formato em linhas facilita escanear e ler texto ([HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)). Cada item pode conter imagens, ícones e elementos interativos ([gov.br DS](https://www.gov.br/ds/components/list)). O Trama tem dois níveis de lista: a **lista de texto** (`<ul>` e `<ol>` no corpo do conteúdo, documentada em Texto e títulos) e a **lista de itens** (`.tr-list`), tratada nesta página.

## Quando usar

- Para itens do mesmo tipo com a mesma estrutura: pessoas, arquivos, dispositivos, configurações ([gov.br DS](https://www.gov.br/ds/components/list)).
- Para navegar por uma hierarquia: cada linha leva a uma tela de detalhe ([HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)).
- Para listas de configurações com um switch ao final de cada linha ([One UI](https://developer.samsung.com/one-ui/comp/list.html)).
- Para escolher um ou mais itens de um conjunto e agir depois sobre a seleção.

## Quando não usar

- **Para dados com colunas comparáveis.** Use uma tabela ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/list/usage)).
- **Para hierarquias com mais de um subnível.** Use uma árvore ou um split view ([gov.br DS](https://www.gov.br/ds/components/list)).
- **Para pares de chave e valor de um único objeto.** Use a lista de resumo.
- **Para muitas imagens ou itens de tamanhos muito diferentes.** Use uma grade de cards ([HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)).

## Anatomia

1.  **Cabeçalho (opcional).** Título da lista e, se houver, ações que valem para a lista inteira ([gov.br DS](https://www.gov.br/ds/components/list)).
2.  **Item.** Unidade que, repetida, forma a lista. Divide-se em três áreas ([gov.br DS](https://www.gov.br/ds/components/list)):
    - **Suporte visual (opcional):** ícone, avatar, miniatura ou checkbox de seleção.
    - **Área principal:** texto principal (obrigatório) e texto secundário (opcional). É a única área que muda de largura com a janela ([gov.br DS](https://www.gov.br/ds/components/list)).
    - **Suporte complementar (opcional):** metadado, switch, botão, menu de mais ações ou seta de navegação, centralizado na vertical.
3.  **Rótulo de grupo (opcional).** Item com formatação própria que nomeia um grupo ([gov.br DS](https://www.gov.br/ds/components/list)).
4.  **Divisor (opcional).** Abaixo de cada item na lista vertical, à direita na horizontal.
5.  **Superfície.** `--t-surface-raised`, com contorno `--t-border-subtle`.

## Tipos

| Tipo             | Uso                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Vertical         | Padrão. Itens em ordem alfabética, cronológica, conceitual ou por outro critério lógico ([gov.br DS](https://www.gov.br/ds/components/list)).                                                                                                    |
| Horizontal       | Aproveita o espaço horizontal da tela, com divisores verticais entre os itens ([gov.br DS](https://www.gov.br/ds/components/list)). Use para poucos itens curtos; na classe Compacta, volta a ser vertical. Se a lista alterna vistas, use abas. |
| De navegação     | Cada linha leva a outra tela; mostre uma seta no fim. Marque o item da tela atual com `aria-current` ([HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)).                                                    |
| Selecionável     | Seleção simples ou múltipla para uma ação posterior. Use `.tr-list--interactive` e `aria-selected`.                                                                                                                                              |
| De ações         | Linha com conteúdo e uma ou duas ações; mais ações vão para um menu ([Geist](https://vercel.com/geist/entity)).                                                                                                                                  |
| De configurações | Cada linha é uma opção com switch ou valor atual no fim ([One UI](https://developer.samsung.com/one-ui/comp/list.html)).                                                                                                                         |

### Agrupamentos

Listas com muitos itens ficam mais fáceis de percorrer quando os itens são agrupados por afinidade. O gov.br descreve três formas, que podem ser combinadas ([gov.br DS](https://www.gov.br/ds/components/list)):

- **Com rótulos:** um item de rótulo nomeia cada grupo. O rótulo segue a densidade da lista.
- **Com divisores:** um divisor separa um grupo do seguinte, e não aparece entre os itens do mesmo grupo.
- **Com expansão:** o rótulo esconde e mostra os itens do grupo, empurrando os itens seguintes.

### Hierarquia

**Use no máximo um subnível.** Evite listas com mais de um subnível ([gov.br DS](https://www.gov.br/ds/components/list)). Para estruturas mais profundas, leve o restante para outra página ou use um split view.

**Recue os subitens pelo menos `--sp-400`.** O gov.br pede recuo mínimo de 16 px a partir do item pai, porque recuos menores ficam sutis demais ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)). Reforce o nível com peso tipográfico, sem itálico nem sublinhado, e combine no máximo dois ou três recursos, como recuo, peso e fundo ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)).

**Em listas hierárquicas, o indicador de expansão fica no início.** Chevron à esquerda do rótulo, para a direita quando fechado e para baixo quando aberto, como em árvores; o fim da linha fica livre para metadados e ações ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)).

> **Divergência entre referências** O Fluent proíbe subníveis em listas e manda usar árvore ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/list/usage)). O gov.br permite agrupamento com expansão e desaconselha só mais de um subnível; no componente de lista, ele põe o chevron do rótulo no fim, mas o padrão de expandir e recolher do mesmo sistema manda usar o identificador à esquerda em árvores ([gov.br DS](https://www.gov.br/ds/components/list), [gov.br DS](https://www.gov.br/ds/padroes/design/collapse)). Nenhuma fonte traz pesquisa. O Trama permite um subnível, com recuo mínimo, e aplica a decisão D8: indicador no início em listas hierárquicas.

## Boas práticas

**Mantenha a estrutura igual em todos os itens.** Mesma largura, mesma posição dos recursos visuais e complementares e, de preferência, a mesma altura; alturas variadas prejudicam a leitura escaneada ([gov.br DS](https://www.gov.br/ds/components/item), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/list/usage)).

**Não varie o espaçamento dentro de uma lista.** Use o mesmo espaço entre todos os itens ([gov.br DS](https://www.gov.br/ds/components/list)).

**Limite a uma ou duas ações visíveis por linha.** Mais do que isso vai para um menu ([Geist](https://vercel.com/geist/entity)). Não coloque botões primários nem componentes de navegação, como carrossel, paginação e abas, dentro de um item ([gov.br DS](https://www.gov.br/ds/components/item)).

**Deixe claro o que é interativo.** Ou o item inteiro é interativo, e toda a superfície tem hover, ou só os controles dentro dele têm ação e hover ([gov.br DS](https://www.gov.br/ds/components/item)). Não misture os dois modelos na mesma lista.

**Use divisores com moderação.** Em listas longas, eles ajudam a distinguir itens; em listas curtas com espaço suficiente, sobram ([gov.br DS](https://www.gov.br/ds/components/list)).

**Preserve a legibilidade em larguras estreitas.** Quebre o texto principal em duas linhas antes de truncar. Nomes de arquivo e identificadores podem ser truncados no meio, com o texto completo acessível ([HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)).

**Permita reordenar quando fizer sentido.** Durante o arrasto, o item usa o estado arrastando (`.tr-dragging`); itens também podem passar de uma lista a outra ([gov.br DS](https://www.gov.br/ds/components/list)). Ofereça alternativa ao arrasto (veja Arrastar e soltar).

**Faça** use botões com verbo e objeto, que continuam claros fora do contexto da linha ([Geist](https://vercel.com/geist/entity)).

**Não faça** encher a linha de botões com verbos soltos.

### Estados

| Estado              | Regra                                                                                                                                          |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Hover e pressionado | Em itens interativos, camada na cor do texto com `--o-hover` e `--o-pressed` sobre toda a superfície (`.tr-list--interactive`).                |
| Atual               | Em listas de navegação, o item da tela aberta leva `aria-current="page"` e destaque persistente.                                               |
| Selecionado         | Em coleções, para ação posterior: `aria-selected="true"`, fundo `--t-brand-subtle` e marca em texto ("Selecionado") ou checkbox, nunca só cor. |
| Desabilitado        | Se a pessoa não pode habilitar o item por uma ação dela, retire-o. Se pode, mostre o item desabilitado com o motivo no texto secundário.       |
| Arrastando          | `.tr-dragging` no item em movimento.                                                                                                           |
| Carregando, vazio   | Linhas de skeleton com a mesma anatomia; estado vazio no lugar da lista inteira.                                                               |

> **Divergência entre referências** O Fluent diz que listas não devem ter itens vazios ou desabilitados ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/list/usage)); o gov.br prevê o estado desabilitado em itens de lista ([gov.br DS](https://www.gov.br/ds/components/list)). O Trama aplica a decisão D9: retira o que a pessoa não pode habilitar e explica o motivo quando ela pode.

### Densidade

A densidade muda o preenchimento vertical do item, com o texto principal como base ([gov.br DS](https://www.gov.br/ds/components/list)). No Trama, `data-density` troca a altura mínima da linha (`--d-row`): 44 px na alta, 56 px na padrão e 64 px na baixa. A densidade alta só vale com apontador fino, em listas longas e ferramentas; evite-a abaixo de 4 colunas ([gov.br DS](https://www.gov.br/ds/components/list)). A baixa é obrigatória no toque e na classe Compacta.

## Conteúdo

- Escreva o texto principal como substantivo ou frase verbal curta. O One UI pede até 31 caracteres em configurações para não quebrar linha ([One UI](https://developer.samsung.com/one-ui/comp/list.html)).
- Use o texto secundário só quando o principal não bastar ([One UI](https://developer.samsung.com/one-ui/comp/list.html)).
- Escreva rótulos de grupo em caixa de frase, com peso 600. Não use caixa alta.
- Use unidades por extenso no texto secundário ("há 5 minutos"); abreviações só em metadados compactos com a unidade nomeada no cabeçalho.

> **Divergência entre referências** O gov.br sugere letras maiúsculas no subtítulo do item e nos rótulos de grupo ([gov.br DS](https://www.gov.br/ds/components/list)). O Trama segue as decisões D1 e D16: caixa de frase e nenhum título em caixa alta, alinhado a Fluent, GOV.UK e DKFDS.

## Acessibilidade

**Use a estrutura nativa.** `<ul>` ou `<ol>` com `<li>`, para que o leitor de tela anuncie a quantidade de itens. Em listas de seleção sem outros elementos focáveis, use `role="listbox"` com itens `role="option"` e `aria-selected`; rótulos de grupo ficam fora da seleção. Não use `role="grid"` em listas com ações opcionais ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/list/usage)).

**Teclado.** Em listas comuns, Tab e Shift+Tab percorrem os controles; em `listbox`, as setas para cima e para baixo movem o foco entre os itens ([gov.br DS](https://www.gov.br/ds/components/list)). Espaço alterna a seleção e Enter executa a ação principal. Em listas com várias ações por linha, a seta para a direita leva às ações e a seta para a esquerda ou Esc volta à linha ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/list/usage)).

**Dê contexto às ações repetidas.** Inclua o nome do item no nome acessível do botão, como na demonstração ("Desconectar Notebook do escritório").

**Expansão anunciada.** O rótulo de um grupo expansível é um botão com `aria-expanded`; o chevron é decorativo.

**Alvos de toque.** No toque, linhas e controles têm pelo menos `--c-touch` ([gov.br DS](https://www.gov.br/ds/components/item)). Imagens com informação têm texto alternativo ([gov.br DS](https://www.gov.br/ds/components/list)).

## Tokens usados

| Elemento                                     | Token                                                      |
|----------------------------------------------|------------------------------------------------------------|
| Superfície, contorno e divisores             | `--t-surface-raised`, `--t-border-subtle`, `--stroke-thin` |
| Raio do contêiner                            | `--r-lg`                                                   |
| Altura mínima da linha por densidade         | `--d-row`                                                  |
| Preenchimento horizontal, espaço entre áreas | `--sp-400`, `--sp-300`                                     |
| Recuo de subnível                            | `--sp-400` no mínimo                                       |
| Texto principal, secundário                  | `--t-fg-1`, `--t-fg-3`                                     |
| Hover, pressionado                           | `--o-hover`, `--o-pressed`                                 |
| Selecionado                                  | `--t-brand-subtle`, `--t-brand`                            |

## Considerações por plataforma

### Web desktop

Mostre ações secundárias também no foco, além do hover. Ofereça menu de contexto com as ações da linha e seleção múltipla com Shift e Ctrl ou Cmd. A densidade alta é permitida em listas longas.

### Web móvel

Listas ocupam a largura total, em densidade baixa. Listas horizontais viram verticais. Não esconda ações atrás de hover. Gestos de deslizar para revelar ações precisam de alternativa visível (veja Toque e gestos).

### Tablets e dobráveis

Em janelas médias e maiores, a lista vai para o painel de lista de um layout lista e detalhe, e o item atual fica destacado ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views), [One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)). Ao abrir ou fechar o dobrável, mantenha a posição de rolagem ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Tabelas
- Lista de resumo
- Painéis e split view
- Divisores
- Densidade
- Estados de interação

### Referências

- [List](https://www.gov.br/ds/components/list) gov.br DS
- [Item](https://www.gov.br/ds/components/item) gov.br DS
- [Padrão Collapse](https://www.gov.br/ds/padroes/design/collapse) gov.br DS
- [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) Apple HIG
- [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views) Apple HIG
- [List](https://fluent2.microsoft.design/components/web/react/core/list/usage) Fluent 2
- [Lists](https://developer.samsung.com/one-ui/comp/list.html) Samsung One UI
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI
- [Entity](https://vercel.com/geist/entity) Geist

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Entram as três áreas do item, a lista horizontal, os agrupamentos, a hierarquia de um subnível com recuo mínimo e indicador no início (D8), as densidades (D11) e os estados selecionado e atual (D10). |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                           |
