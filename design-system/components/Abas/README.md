# Abas

Abas organizam conteúdo relacionado e mutuamente exclusivo em seções na mesma área, e a pessoa alterna entre elas com um clique.

Cada aba mostra uma vista de um mesmo contexto, como Visão geral, Atividade e Configurações de um projeto. As abas compartilham escopo, dados e endereço pai ([Geist](https://vercel.com/geist/tabs)). Elas ajudam quando há informação demais para uma página e ela se divide em categorias ou seções ([gov.br DS](https://www.gov.br/ds/components/tab)). Como só uma seção aparece por vez, nem todas as pessoas percebem o conteúdo das outras ([GOV.UK](https://design-system.service.gov.uk/components/tabs/), [DKFDS](https://designsystem.dk/komponenter/faneblade/)).

## Quando usar

- Quando o conteúdo se divide em seções claramente rotuladas e paralelas, como "Atuais", "Próximos" e "Anteriores" ([Ontario](https://designsystem.ontario.ca/components/detail/tabs.html)).
- Quando a primeira seção interessa à maioria e as pessoas não precisam ver todas ao mesmo tempo ([GOV.UK](https://design-system.service.gov.uk/components/tabs/)).
- Para conteúdo curto e enxuto, como listas, dados e visões gerais ([DKFDS](https://designsystem.dk/komponenter/faneblade/)).
- Para separar resultados de uma pesquisa por categoria, com a contagem de cada uma ([gov.br DS](https://www.gov.br/ds/components/tab)).

## Quando não usar

- **Para passos de um processo ou formulário.** Use páginas em sequência e o indicador de etapas ([DKFDS](https://designsystem.dk/komponenter/faneblade/), [HDS](https://hds.hel.fi/components/tabs)).
- **Quando a pessoa precisa comparar informações entre abas.** Mostre junto, em uma tabela ou lado a lado ([GOV.UK](https://design-system.service.gov.uk/components/tabs/), [HDS](https://hds.hel.fi/components/tabs)).
- **Quando a pessoa precisa ler tudo em ordem.** Mantenha em uma página, separada por títulos ([GOV.UK](https://design-system.service.gov.uk/components/tabs/)).
- **Dentro de outra aba.** Abas dentro de abas confundem a navegação e aumentam a carga cognitiva; para subdividir uma aba, use uma lista ou títulos ([gov.br DS](https://www.gov.br/ds/components/tab)).
- **Para navegar entre páginas sem relação.** Use a navegação lateral ou links ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tablist/usage)).
- **Para escolher um valor ou filtrar uma vista.** Use o controle segmentado.

## Anatomia

1.  **Superfície da lista.** Linha de abas na borda superior da área de conteúdo, com divisor inferior `--t-border-subtle` que se estende até o limite da área, mesmo quando as abas ocupam menos largura ([gov.br DS](https://www.gov.br/ds/components/tab)).
2.  **Aba.** Rótulo de texto, opcionalmente com ícone. A largura acompanha o rótulo mais o preenchimento ([gov.br DS](https://www.gov.br/ds/components/tab)). As abas ficam alinhadas ao início.
3.  **Contador (opcional).** Quantidade de itens da seção, em badge ao lado do rótulo.
4.  **Indicador de seleção.** Barra de 3 px em `--t-brand` sob a aba selecionada, com texto em `--t-fg-1`.
5.  **Painel.** Conteúdo da aba selecionada, logo abaixo da lista.
6.  **Sombras de rolagem.** Quando há abas ocultas, uma sombra no lado em que estão indica que a lista rola ([gov.br DS](https://www.gov.br/ds/components/tab)).

## Tipos

| Tipo                 | Uso                                                                                                                                                                                                                                                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Abas de conteúdo     | Alternam painéis dentro da página, sem trocar de endereço. Padrão.                                                                                                                                                                                                                                                                       |
| Abas de navegação    | Cada aba é uma subpágina com endereço próprio. Um conjunto por página, logo abaixo do título ([DKFDS](https://designsystem.dk/komponenter/faneblade/)).                                                                                                                                                                                  |
| Abas com ícone       | Só quando o ícone é inequívoco. Todas as abas têm ícone e texto, nunca mistura ([DKFDS](https://designsystem.dk/komponenter/faneblade/), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tablist/usage)). Na classe Compacta, o ícone pode ir acima do rótulo ([gov.br DS](https://www.gov.br/ds/components/tab)). |
| Abas em fundo escuro | Dentro de `.tr-inverse`, que redefine texto, indicador e divisor para os valores escuros. O gov.br oferece a mesma variante ([gov.br DS](https://www.gov.br/ds/components/tab)).                                                                                                                                                         |
| Abas verticais       | Para muitas seções em telas largas, à esquerda do painel ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tablist/usage)).                                                                                                                                                                                         |

> **Divergência entre referências** O gov.br e o Fluent permitem abas só com ícone, com tooltip e nome acessível ([gov.br DS](https://www.gov.br/ds/components/tab), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tablist/usage)). O DKFDS exige que todo ícone de aba venha com rótulo, porque um ícone mal interpretado confunde mais do que ajuda ([DKFDS](https://designsystem.dk/komponenter/faneblade/)). Pelo critério de acessibilidade, o Trama exige rótulo visível: tooltips não aparecem no toque, e o rótulo visível é o que comandos de voz e pessoas com deficiência cognitiva usam (WCAG 2.2, 2.5.3).

## Boas práticas

**Limite a quantidade.** Use no máximo seis abas em web desktop ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-views), [HDS](https://hds.hel.fi/components/tabs)) e quatro na classe Compacta ([Geist](https://vercel.com/geist/tabs)). Acima disso, consolide seções ou use outra navegação.

**Ordene pela necessidade.** A primeira aba é a seção mais usada e fica selecionada ao abrir a página ([GOV.UK](https://design-system.service.gov.uk/components/tabs/), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tablist/usage)).

**Há sempre uma aba selecionada.** Abas não se fecham e não ficam todas desmarcadas ([DKFDS](https://designsystem.dk/komponenter/faneblade/)).

**Não desabilite abas.** Se uma aba não tem conteúdo, retire-a ou explique dentro dela por que está vazia ([GOV.UK](https://design-system.service.gov.uk/components/tabs/), [DKFDS](https://designsystem.dk/komponenter/faneblade/)).

**Não quebre a lista em duas linhas; role na horizontal.** Quando as abas não cabem, a lista rola na horizontal, por arrasto no toque e pela barra de rolagem com mouse, com sombra no lado em que há abas ocultas ([gov.br DS](https://www.gov.br/ds/components/tab), [HDS](https://hds.hel.fi/components/tabs)). A aba selecionada e as vizinhas ficam sempre visíveis; ao mover o foco por teclado para uma aba oculta, role a lista até ela. Antes de recorrer à rolagem, tente reduzir as abas.

> **Divergência entre referências** O Fluent não rola nem quebra a lista e leva o excesso para um botão de menu, alertando que abas no menu são mais difíceis de achar ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tablist/usage)). O gov.br e o HDS rolam a lista com indicação nas bordas ([gov.br DS](https://www.gov.br/ds/components/tab), [HDS](https://hds.hel.fi/components/tabs)). O Trama adota a rolagem com sombras, posição da maioria, que mantém todas as abas no mesmo nível.

**Mantenha cada painel autossuficiente.** Controles dentro de um painel afetam só esse painel ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-views)). Trocar de aba não exige salvar nem enviar dados ([Ontario](https://designsystem.ontario.ca/components/detail/tabs.html)).

**Reflita a aba no endereço.** Atualize o fragmento ou o parâmetro da URL, para que links diretos, recarregar e o botão voltar restaurem a aba ([GOV.UK](https://design-system.service.gov.uk/components/tabs/), [Geist](https://vercel.com/geist/tabs)).

**Troque de aba instantaneamente.** Não mostre confirmação nem toast ao trocar ([Geist](https://vercel.com/geist/tabs)). Se o painel carregar dados, mostre um skeleton dentro dele.

**Faça** use rótulos curtos e paralelos, que se leem como categorias do mesmo conjunto.

**Não faça** misturar substantivos, verbos e categorias vagas ([Ontario](https://designsystem.ontario.ca/components/detail/tabs.html)), nem usar iniciais maiúsculas em cada palavra.

### Estados

| Estado          | Aparência                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Não selecionada | Texto `--t-fg-2`.                                                                                         |
| Hover           | Camada na cor do texto com `--o-hover`.                                                                   |
| Selecionada     | Texto `--t-fg-1`, indicador `--t-brand` e `aria-selected="true"`.                                         |
| Foco            | Anel `--t-focus` em `:focus-visible`, também na aba selecionada ([Geist](https://vercel.com/geist/tabs)). |

### Densidade

O gov.br define três densidades de aba, mudando só o preenchimento vertical ([gov.br DS](https://www.gov.br/ds/components/tab)). No Trama, a aba tem altura `--c-touch` na densidade padrão e `--c-h-lg` na baixa, obrigatória no toque e na classe Compacta. A densidade alta usa `--c-h-sm` e só vale com apontador fino, em espaços restritos de ferramentas. O preenchimento horizontal fica em `--sp-300` nas três.

## Conteúdo

- Escreva rótulos de uma ou duas palavras, três quando for inevitável, em geral substantivos que nomeiam o conteúdo ([gov.br DS](https://www.gov.br/ds/components/tab), [HDS](https://hds.hel.fi/components/tabs)). Verbos ficam em botões.
- Use caixa de frase, sem pontuação final ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tablist/usage), [HDS](https://hds.hel.fi/components/tabs)).
- Mantenha os rótulos paralelos em gramática e nível de abstração ([DKFDS](https://designsystem.dk/komponenter/faneblade/)).
- Mostre contagens em um badge ao lado do rótulo e retire-o quando a contagem for zero ([Geist](https://vercel.com/geist/tabs), [gov.br DS](https://www.gov.br/ds/components/tab)).
- Comece cada painel com um título que repete o rótulo da aba ([GOV.UK](https://design-system.service.gov.uk/components/tabs/), [gov.br DS](https://www.gov.br/ds/components/tab)).

> **Divergência entre referências** O gov.br aceita rótulos de uma a três palavras e prefere iniciais maiúsculas em todas as palavras de componentes de navegação ([gov.br DS](https://www.gov.br/ds/components/tab), [gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). HDS e Geist pedem uma ou duas palavras, e Fluent e HDS usam caixa de frase. O Trama segue as decisões D24 e D1: até duas palavras, três quando inevitável, em caixa de frase.

## Acessibilidade

**Use os papéis ARIA de abas.** `role="tablist"` no contêiner, `role="tab"` em cada `<button>` e `role="tabpanel"` nos painéis, com `aria-labelledby` apontando para a aba. Marque a aba selecionada com `aria-selected="true"`, as demais com `"false"`, e esconda os painéis inativos com `hidden` ([gov.br DS](https://www.gov.br/ds/components/tab), [DKFDS](https://designsystem.dk/komponenter/faneblade/)). Em abas de navegação, use links com `aria-current="page"` no lugar dos papéis de aba.

**Teclado com ativação manual.** Tab entra na lista pela aba selecionada e sai para o painel. Seta para a direita e para a esquerda movem o foco entre abas; Home e End vão à primeira e à última; Enter ou Espaço ativam a aba focada ([HDS](https://hds.hel.fi/components/tabs/accessibility), [gov.br DS](https://www.gov.br/ds/components/tab)). Não associe as setas para cima e para baixo ([GOV.UK](https://design-system.service.gov.uk/components/tabs/)).

> **Divergência entre referências** O gov.br põe o foco inicial na primeira aba interativa e sugere links dentro de `<nav>` com papel de aba ([gov.br DS](https://www.gov.br/ds/components/tab)). O HDS leva o foco à aba selecionada ([HDS](https://hds.hel.fi/components/tabs/accessibility)). O Trama usa botões com papel de aba e foco na aba selecionada, porque é ela que corresponde ao painel visível; `<nav>` com links fica para abas de navegação.

**Dê nome à lista e coloque o painel logo depois dela no DOM.** Sem título visível acima das abas, use `aria-label` no `tablist` ([Geist](https://vercel.com/geist/tabs), [HDS](https://hds.hel.fi/components/tabs/accessibility)).

**Inclua a contagem no nome da aba.** O badge faz parte do botão, e o leitor de tela anuncia "Arquivos 12". Mantenha a área de toque de `--c-touch` ([gov.br DS](https://www.gov.br/ds/components/tab)).

**Funcione sem JavaScript.** Sem script, mostre todos os painéis em sequência, com um sumário de links no topo ([GOV.UK](https://design-system.service.gov.uk/components/tabs/)).

## Tokens usados

| Elemento                                    | Token                                |
|---------------------------------------------|--------------------------------------|
| Divisor da lista                            | `--t-border-subtle`, `--stroke-thin` |
| Altura da aba (alta, padrão, baixa)         | `--c-h-sm`, `--c-touch`, `--c-h-lg`  |
| Preenchimento horizontal, espaço entre abas | `--sp-300`, `--sp-100`               |
| Rótulo                                      | Body small 14/20, peso 600           |
| Texto não selecionado, selecionado          | `--t-fg-2`, `--t-fg-1`               |
| Indicador                                   | `--t-brand`, `--stroke-thicker`      |
| Hover                                       | `--o-hover`                          |
| Sombras de rolagem                          | `--t-shadow-key`                     |
| Foco                                        | `--t-focus`, `--stroke-thick`        |
| Espaço entre lista e painel                 | `--sp-400`                           |

## Considerações por plataforma

### Web desktop

Deixe uma margem ao redor da área de abas ([HIG](https://developer.apple.com/design/human-interface-guidelines/tab-views)). Com abas ocultas, as setas do teclado rolam a lista na medida de cada aba ([gov.br DS](https://www.gov.br/ds/components/tab)). Abas verticais são uma opção em janelas grandes.

### Web móvel

Use no máximo quatro abas, em densidade baixa. A lista rola por arrasto, com a aba selecionada visível e sombra no lado das abas ocultas ([gov.br DS](https://www.gov.br/ds/components/tab)). Abas com ícone podem empilhar ícone e rótulo. A navegação principal do produto usa a barra de navegação inferior.

### Tablets e dobráveis

Em janelas médias, as abas cabem em largura total. Em layout de dois painéis, as abas pertencem ao painel de detalhe. Ao abrir ou fechar o dobrável, mantenha a aba selecionada ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Acordeão
- Controle segmentado
- Badges
- Barra de navegação e rail
- Densidade
- Teclado

### Referências

- [Tab](https://www.gov.br/ds/components/tab) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views) Apple HIG
- [Tabs](https://design-system.service.gov.uk/components/tabs/) GOV.UK Design System
- [Faneblade (Tabs)](https://designsystem.dk/komponenter/faneblade/) DKFDS
- [Tabs](https://hds.hel.fi/components/tabs) Helsinki Design System
- [Tabs: accessibility](https://hds.hel.fi/components/tabs/accessibility) Helsinki Design System
- [Tablist](https://fluent2.microsoft.design/components/web/react/core/tablist/usage) Fluent 2
- [Tabs](https://vercel.com/geist/tabs) Geist
- [Tabs](https://designsystem.ontario.ca/components/detail/tabs.html) Ontario Design System
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Entram a rolagem horizontal com sombras, o contador em badge, rótulos de até 3 palavras quando inevitável (D24), a proibição de abas dentro de abas, a variante em fundo escuro, densidades (D11) e o hover em camada (D10). |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                |
