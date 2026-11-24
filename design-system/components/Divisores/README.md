# Divisores

Um divisor é uma linha neutra, horizontal ou vertical, que separa grupos de conteúdo ou de controles quando o espaço sozinho não basta.

Divisores ajudam a ler uma tela densa, mas cada linha adiciona ruído. Espaço em branco e alinhamento resolvem a maior parte dos agrupamentos sem nenhuma linha ([HIG](https://developer.apple.com/design/human-interface-guidelines/boxes)). Use o divisor quando os elementos não puderem ser separados por distância ([gov.br DS](https://www.gov.br/ds/components/divider)): entre grupos de uma lista, de um menu, de uma barra de ferramentas e entre seções de um texto longo.

## Quando usar

- Para separar seções de conteúdo quando o espaço disponível não marca a separação ([gov.br DS](https://www.gov.br/ds/components/divider), [Blueprint](https://blueprintjs.com/docs/#core/components/divider)).
- Para criar uma quebra temática entre seções de texto, com o elemento `<hr>` ([GOV.UK](https://design-system.service.gov.uk/styles/section-break/)).
- Para separar grupos de ações em uma barra de ferramentas ou em um menu, e grupos de itens em uma lista.
- Para delimitar painéis adjacentes em um split view.

## Quando não usar

- **Quando o espaço já separa.** Se a distância entre os blocos marca a separação, a linha é redundante ([gov.br DS](https://www.gov.br/ds/components/divider)).
- **Para sublinhar títulos.** Coloque o divisor acima do título da seção, nunca abaixo ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/divider/usage)).
- **Entre cada item de um grupo.** Reserve a linha para a fronteira entre grupos ([gov.br DS](https://www.gov.br/ds/components/divider)).
- **Para circundar um item.** Use borda, ou um card ([gov.br DS](https://www.gov.br/ds/components/divider)).
- **Junto a outra linha.** Se o contêiner já tem borda, não acrescente um divisor encostado nela.

## Anatomia

1.  **Linha.** A borda de uma superfície formando uma linha reta ([gov.br DS](https://www.gov.br/ds/components/divider)): `--stroke-thin` na cor `--t-border-subtle` por padrão.
2.  **Margens.** Espaço acima e abaixo (ou dos lados, no vertical). `.tr-divider` aplica `--sp-300` acima e abaixo.
3.  **Rótulo (opcional).** Texto curto que anuncia a próxima seção.

## Tipos

| Tipo                      | Implementação                                                                 | Uso                                                                                                                                                                                                                                                              |
|---------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bloco                     | `.tr-divider`                                                                 | Ocupa toda a largura do contêiner e marca uma separação forte ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/divider/usage)).                                                                                                            |
| Com sangria               | `.tr-divider` com margem lateral negativa igual ao preenchimento do contêiner | Dentro de um card ou painel, a linha atravessa até as bordas, sem margens ([gov.br DS](https://www.gov.br/ds/components/divider)). Use para separar áreas da mesma superfície, como o rodapé de ações.                                                           |
| Recuado                   | `.tr-divider--inset`                                                          | Para antes das bordas e sugere relação próxima, como linhas de uma lista com avatar ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/divider/usage)).                                                                                      |
| Vertical                  | `.tr-toolbar__sep`                                                            | Separa grupos lado a lado; funciona dentro de um contêiner flexível ([gov.br DS](https://www.gov.br/ds/components/divider), [Geist](https://vercel.com/geist/separator)).                                                                                        |
| Tracejado                 | `border-top-style: dashed`                                                    | O gov.br oferece o estilo tracejado ([gov.br DS](https://www.gov.br/ds/components/divider)). O Trama reserva o tracejado para limites provisórios, como o ponto de inserção durante um arrasto e a borda de uma área de soltar, em coerência com `.tr-dropzone`. |
| Com rótulo                | `.tr-divider` com texto                                                       | Separa caminhos alternativos em formulários, como "ou".                                                                                                                                                                                                          |
| Quebra de seção invisível | `<hr>` sem linha                                                              | Mantém a semântica de quebra temática usando apenas a margem ([GOV.UK](https://design-system.service.gov.uk/styles/section-break/)).                                                                                                                             |

### Espessuras

O gov.br define três espessuras de divisor ([gov.br DS](https://www.gov.br/ds/components/divider)). O Trama usa os tokens de borda:

| Espessura     | Token              | Uso                                                                                                                                                                                                                              |
|---------------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fina (padrão) | `--stroke-thin`    | Quase todos os casos. Dá o máximo de espaço ao conteúdo ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)).                                                                                      |
| Média         | `--stroke-thick`   | Quando os dois lados têm linhas fortes que escondem a fina, como tabelas lado a lado ([HIG](https://developer.apple.com/design/human-interface-guidelines/split-views)), ou para separar grupos de colunas em tabelas complexas. |
| Grossa        | `--stroke-thicker` | Só para separar blocos de nível mais alto em páginas longas, nunca entre itens.                                                                                                                                                  |

## Boas práticas

**Prefira espaço a linhas.** Comece com `--sp-600` ou `--sp-800` entre grupos. Acrescente o divisor só se a separação continuar ambígua. Use divisores com moderação ([gov.br DS](https://www.gov.br/ds/components/divider)).

**Use o divisor entre grupos.** Uma linha entre grupos deixa o layout limpo; uma linha entre cada subitem o deixa poluído ([gov.br DS](https://www.gov.br/ds/components/divider)).

**Deixe a linha visível e discreta.** O divisor nunca chama mais atenção que o conteúdo ([gov.br DS](https://www.gov.br/ds/components/divider)). Não use cor de marca nem cores semânticas.

**Respeite as margens mínimas.** Deixe pelo menos `--sp-300` acima e abaixo de divisores simples ou com texto, e `--sp-200` em divisores com ícone ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/divider/usage)). Quando a margem do divisor encontra a margem de outro elemento, vale a maior, sem somar.

> **Divergência entre referências** O Fluent pede 12 px acima e abaixo de divisores simples ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/divider/usage)). O gov.br especifica o token de espaçamento `--spacing-scale-2x`, que o próprio sistema equivale a 16 px ([gov.br DS](https://www.gov.br/ds/components/divider), [gov.br DS](https://www.gov.br/ds/padroes/design/collapse)). Não há pesquisa nem impacto de acessibilidade em nenhuma das opções. O Trama mantém `--sp-300` como mínimo, que já é o valor de `.tr-divider`, e usa `--sp-400` entre seções de página.

**Em textos longos, coloque o divisor antes do título.** A linha agrupa o título com o conteúdo que vem depois ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/divider/usage)).

**Troque a cor quando o fundo esconder a linha.** Em fundos com cor igual ou próxima à do divisor, use `--t-border` ([gov.br DS](https://www.gov.br/ds/components/divider)). Em faixas escuras, envolva o conteúdo em `.tr-inverse`, que ajusta `--t-border-subtle` automaticamente. Não use cores aleatórias.

**Ajuste o divisor a molduras.** Quando um divisor encontra uma moldura de 1 px, recue-o 1 px em cada ponta para não sobrepor a moldura ([Geist](https://vercel.com/geist/separator)).

**Faça** coloque o divisor acima do título para abrir a nova seção.

**Não faça** sublinhar o título com um divisor nem separar cada parágrafo com uma linha.

### Comportamento

O divisor não é interativo e não tem estados ([gov.br DS](https://www.gov.br/ds/components/divider)). A exceção é o divisor entre painéis redimensionáveis, que é um controle com papel próprio e está documentado em Painéis e split view. O divisor se adapta à largura do contêiner em qualquer classe de janela. No modo escuro, `--t-border-subtle` muda automaticamente; não ajuste a opacidade da linha à mão.

## Conteúdo

- Use rótulo em divisor só quando ele ajudar a entender a próxima seção. Mantenha-o curto e em caixa de frase ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/divider/usage)).
- Em formulários com alternativas, o rótulo "ou" entre dois caminhos é aceitável. Não use rótulos decorativos.

## Acessibilidade

**Escolha entre semântica e decoração.** Use `<hr>` quando a linha marca uma mudança de tema no conteúdo; leitores de tela anunciam o separador, o que expõe a estrutura (WCAG 2.2, 1.3.1). Quando a linha só enfeita, desenhe-a com borda CSS ou esconda-a com `aria-hidden="true"`, e o foco nunca passa por ela ([gov.br DS](https://www.gov.br/ds/components/divider), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/divider/usage)).

> **Divergência entre referências** O gov.br trata todo divisor como decorativo, a ser ignorado pelo leitor de tela, e ao mesmo tempo recomenda a tag `<hr>` ([gov.br DS](https://www.gov.br/ds/components/divider)). O GOV.UK usa `<hr>` como quebra de seção ([GOV.UK](https://design-system.service.gov.uk/styles/section-break/)) e o Fluent distingue divisor semântico de decorativo ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/divider/usage)). Pelo critério de acessibilidade e pela maioria, o Trama mantém a distinção: `<hr>` anunciado quando separa temas, borda CSS silenciosa quando só decora.

**Divisores verticais em barras.** Dentro de `role="toolbar"` ou `role="menu"`, use `role="separator"` com `aria-orientation`.

**Não dependa da linha para comunicar agrupamento essencial.** Divisores decorativos não têm contraste mínimo ([gov.br DS](https://www.gov.br/ds/components/divider)). Se a separação é necessária para entender a interface, reforce com título ou espaço, ou use `--t-border`.

## Tokens usados

| Elemento                             | Token                                                 |
|--------------------------------------|-------------------------------------------------------|
| Cor da linha                         | `--t-border-subtle`                                   |
| Cor reforçada                        | `--t-border`                                          |
| Espessuras                           | `--stroke-thin`, `--stroke-thick`, `--stroke-thicker` |
| Margem vertical mínima, entre seções | `--sp-300`, `--sp-400`                                |
| Margem com ícone, margem do vertical | `--sp-200`, `--sp-100`                                |
| Recuo lateral (inset)                | `--sp-400`                                            |
| Rótulo                               | Caption 12/16, `--t-fg-3`                             |

## Considerações por plataforma

### Web desktop

Nenhuma consideração adicional para Web desktop.

### Web móvel

Em listas de largura total, use o divisor recuado alinhado ao início do texto, para que a linha não colida com ícones ou avatares. Evite divisores verticais em barras estreitas; com pouco espaço, agrupe ações em um menu.

### Tablets e dobráveis

Entre painéis, use um divisor vertical fino de borda a borda. Em dobráveis abertos com proporção 50:50, alinhe o divisor entre painéis à dobra e não coloque controles sobre ela ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Espaçamento
- Formas e bordas
- Listas
- Barra de ferramentas
- Painéis e split view

### Referências

- [Divider](https://www.gov.br/ds/components/divider) gov.br DS
- [Padrão Collapse](https://www.gov.br/ds/padroes/design/collapse) gov.br DS
- [Boxes](https://developer.apple.com/design/human-interface-guidelines/boxes) Apple HIG
- [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views) Apple HIG
- [Divider](https://fluent2.microsoft.design/components/web/react/core/divider/usage) Fluent 2
- [Section break](https://design-system.service.gov.uk/styles/section-break/) GOV.UK Design System
- [Separator](https://vercel.com/geist/separator) Geist
- [Divider](https://blueprintjs.com/docs/#core/components/divider) Blueprint
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                             |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Entram o divisor tracejado, as três espessuras, a sangria dentro de superfícies, a regra de separar grupos e as decisões sobre margem e semântica. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                      |
