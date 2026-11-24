# Acordeao

Um acordeão empilha seções com cabeçalhos clicáveis que mostram e escondem o conteúdo relacionado, para que a pessoa abra só o que é relevante para ela.

O acordeão reduz a quantidade de informação visível de uma vez, o que ajuda em conteúdo extenso e em telas de celular ([gov.br DS](https://www.gov.br/ds/components/accordion)). Esse benefício tem um custo: conteúdo escondido é visto por menos gente, e nem todas as pessoas percebem ou entendem o componente ([GOV.UK](https://design-system.service.gov.uk/components/accordion/), [DKFDS](https://designsystem.dk/komponenter/accordions/)). Antes de usar um acordeão, teste o conteúdo sem ele. Texto bem escrito e dividido por títulos costuma resolver.

O acordeão aplica o padrão de expandir e recolher do Trama a várias seções. Para um único bloco de informação secundária, use a variação **detalhes**.

## Quando usar

- Quando a pessoa precisa de uma visão geral de várias seções e vai abrir só as que se aplicam a ela ([GOV.UK](https://design-system.service.gov.uk/components/accordion/)).
- Quando apenas uma das opções se aplica à situação de cada pessoa, como regras diferentes por tipo de residência ([Ontario](https://designsystem.ontario.ca/components/detail/accordions.html)).
- Para informação adicional sobre um tópico, que só parte das pessoas precisa ler ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)).
- Em sistemas de uso frequente, em que as pessoas sabem o que procuram ([GOV.UK](https://design-system.service.gov.uk/components/accordion/)), e para opções avançadas que a maioria pula ([Geist](https://vercel.com/geist/collapse)).

## Quando não usar

- **Para conteúdo que todos precisam ler ou que tem prioridade.** Deixe visível e separe por títulos, ou use um sumário com links ([GOV.UK](https://design-system.service.gov.uk/components/accordion/), [gov.br DS](https://www.gov.br/ds/padroes/design/collapse)).
- **Para conteúdo que ocupa quase uma tela inteira quando aberto.** Leve-o para uma página própria ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)).
- **Para pouco conteúdo.** Duas ou três palavras não justificam uma seção recolhível; deixe o texto visível na página ([DKFDS](https://designsystem.dk/komponenter/accordions/), [gov.br DS](https://www.gov.br/ds/padroes/design/collapse)).
- **Para dividir um formulário ou uma sequência de passos.** Use páginas separadas e o indicador de etapas ([DKFDS](https://designsystem.dk/komponenter/accordions/)).
- **Para alternar entre vistas irmãs com o mesmo peso.** Use abas. Para resultados de pesquisa e listas longas, use uma lista ([DKFDS](https://designsystem.dk/komponenter/accordions/)).

## Anatomia

1.  **Cabeçalho.** Botão que ocupa toda a largura da linha e contém o rótulo. A área inteira é clicável ([GOV.UK](https://design-system.service.gov.uk/components/accordion/), [gov.br DS](https://www.gov.br/ds/components/accordion)).
2.  **Indicador.** Chevron no fim do cabeçalho, para baixo quando a seção está fechada e para cima quando está aberta. A seta aponta para onde o conteúdo vai se mover ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)). Use a mesma posição em todo o produto ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/accordion/usage)).
3.  **Resumo (opcional).** Uma linha curta sob o rótulo.
4.  **Painel.** Conteúdo revelado logo abaixo do cabeçalho. Ao abrir, ele empurra o conteúdo seguinte para baixo; ao fechar, o conteúdo volta ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)).
5.  **Divisores.** Linhas entre as seções que delimitam cada uma ([gov.br DS](https://www.gov.br/ds/components/accordion)).

> **Divergência entre referências** A HIG usa o triângulo de revelação no início, apontando para a direita quando fechado e para baixo quando aberto ([HIG](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls)). O acordeão do gov.br coloca o ícone à esquerda, antes do texto ([gov.br DS](https://www.gov.br/ds/components/accordion)), mas o padrão de expandir e recolher do mesmo sistema põe o identificador à direita por padrão ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)). O Fluent aceita as duas posições, desde que consistentes ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/accordion/usage)). Nenhuma fonte traz pesquisa. O Trama adota a decisão D8: chevron no fim, para baixo e para cima, em acordeões e seções recolhíveis. O indicador no início fica para árvores, listas hierárquicas e linhas de tabela, em que o fim da linha é ocupado por outras ações.

## Tipos

| Tipo                     | Quando usar                                                                                                                                                                                     | Implementação                                                                                                             |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Acordeão                 | Duas ou mais seções relacionadas.                                                                                                                                                               | Cada cabeçalho é um `<button aria-expanded>` dentro de um título `<h2>` a `<h6>`.                                         |
| Detalhes                 | Um único bloco de ajuda que só algumas pessoas precisam. Menos proeminente que o acordeão ([GOV.UK](https://design-system.service.gov.uk/components/details/)).                                 | `<details>` e `<summary>` nativos, com aparência de link.                                                                 |
| Acordeão em card         | Um acordeão isolado que precisa se destacar. Para vários empilhados, prefira o padrão, que é mais leve ([HDS](https://hds.hel.fi/components/accordion)).                                        | Envolva o acordeão em `.tr-card`.                                                                                         |
| Acordeão em fundo escuro | Dentro de rodapés e faixas escuras no tema claro. O gov.br chama essa versão de negativa e mantém os mesmos estilos, com texto claro ([gov.br DS](https://www.gov.br/ds/components/accordion)). | Coloque o acordeão dentro de `.tr-inverse`, que redefine os tokens alias para os valores escuros. Não troque cores à mão. |

## Boas práticas

**Comece com as seções fechadas.** Abra uma seção no carregamento só quando a pessoa precisa ler esse conteúdo para agir, ou quando ela volta à página e você restaura o estado anterior ([HDS](https://hds.hel.fi/components/accordion), [GOV.UK](https://design-system.service.gov.uk/components/accordion/)).

**Deixe as seções independentes.** Por padrão, abrir uma seção não fecha as outras e nada abre ou fecha sozinho ([HDS](https://hds.hel.fi/components/accordion), [gov.br DS](https://www.gov.br/ds/components/accordion)). Várias seções abertas ajudam quando a pessoa precisa consultar ou comparar blocos ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)). Use o modo de uma seção por vez só quando as seções forem mutuamente exclusivas.

> **Divergência entre referências** No Fluent, abrir um item fecha os outros por padrão, e vários abertos são permitidos quando não sobrecarregam ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/accordion/usage)). O gov.br e o HDS permitem várias seções abertas por padrão ([gov.br DS](https://www.gov.br/ds/components/accordion), [HDS](https://hds.hel.fi/components/accordion)). Sem pesquisa citada, o Trama decide pela acessibilidade e pela maioria: seções independentes, porque fechar uma seção que a pessoa não tocou muda o conteúdo sem ação dela.

**Não aninhe.** Nada de acordeão dentro de acordeão, nem dentro de abas ou de detalhes. Para agrupar acordeões, use títulos comuns ([DKFDS](https://designsystem.dk/komponenter/accordions/), [gov.br DS](https://www.gov.br/ds/components/accordion)).

**Não exija comparação entre seções.** Se a pessoa precisa de uma seção para entender outra, mostre o conteúdo junto ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/accordion/usage)).

**Deixe o painel crescer com o conteúdo.** Não fixe a altura do painel com rolagem interna. O gov.br admite altura fixa, mas alerta contra rolagem extensa em área pequena ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)); se o conteúdo é grande demais para o painel, ele merece uma página.

**Ofereça "Abrir todas" em grupos longos.** Com cinco ou mais seções, coloque um botão sutil acima do grupo que alterna entre "Abrir todas as seções" e "Fechar todas as seções" ([DKFDS](https://designsystem.dk/komponenter/accordions/)).

**Não desabilite seções.** Se uma seção não tem conteúdo, retire-a. Se o conteúdo depende de uma ação da pessoa, deixe a seção abrir e explique dentro dela o que falta ([GOV.UK](https://design-system.service.gov.uk/components/accordion/)).

**Não esconda ações destrutivas.** Uma ação perigosa dentro de uma seção fechada exige dois cliques para chegar ao aviso ([Geist](https://vercel.com/geist/collapse)).

**Faça** escreva rótulos curtos que dizem o que a seção contém.

**Não faça** usar rótulos vagos ou siglas que o público não reconhece ([Ontario](https://designsystem.ontario.ca/components/detail/accordions.html), [gov.br DS](https://www.gov.br/ds/components/accordion)).

### Estados

| Estado  | Aparência                                                                                                                                                                         |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fechado | Chevron para baixo, painel oculto.                                                                                                                                                |
| Aberto  | Chevron para cima, painel visível. A rotação usa `--m-normal` e `--m-ease-standard`; com movimento reduzido, a troca é imediata.                                                  |
| Hover   | Camada na cor do texto do cabeçalho com opacidade `--o-hover`, em toda a área do cabeçalho.                                                                                       |
| Foco    | Anel `--t-focus` de `--stroke-thick` afastado 2 px, só em `:focus-visible`.                                                                                                       |
| Erro    | Quando um campo dentro do painel tem erro, abra a seção, mostre a mensagem no campo e liste o erro no resumo de erros ([DKFDS](https://designsystem.dk/komponenter/accordions/)). |

### Densidade

O cabeçalho tem altura mínima `--c-h-lg` na densidade padrão. Na densidade baixa, acrescente `--sp-200` de preenchimento vertical; ela é obrigatória no toque e na classe Compacta. A densidade alta reduz o cabeçalho para `--c-h-md` e só vale com apontador fino, em ferramentas com muitas seções. Mantenha a mesma densidade em todos os acordeões de uma tela ([gov.br DS](https://www.gov.br/ds/padroes/design/densidade)).

## Conteúdo

- Escreva o rótulo como uma frase curta que resume o conteúdo, em caixa de frase e sem ponto final ([gov.br DS](https://www.gov.br/ds/components/accordion), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/accordion/usage)).
- Escreva para caber em uma linha ([gov.br DS](https://www.gov.br/ds/components/accordion)). Se não couber, o rótulo quebra; nunca trunque.
- Nomeie o tema, como "Configurações avançadas". Evite começar com "Mostrar" ([Geist](https://vercel.com/geist/collapse)).
- Evite siglas e expressões que o público em geral não reconhece. Se a sigla for necessária, escreva o nome completo no painel na primeira menção ([gov.br DS](https://www.gov.br/ds/components/accordion)).
- Use o resumo só se for indispensável e com poucas palavras, porque todo o texto do cabeçalho é lido de uma vez pelo leitor de tela ([GOV.UK](https://design-system.service.gov.uk/components/accordion/)).

## Acessibilidade

**Use um botão dentro de um título.** O cabeçalho é um `<button>` ([gov.br DS](https://www.gov.br/ds/components/accordion)) com `aria-expanded` e `aria-controls` apontando para o painel ([Ontario](https://designsystem.ontario.ca/components/detail/accordions.html)). Envolva o botão em um título com o nível certo para a página ([HDS](https://hds.hel.fi/components/accordion)). O chevron é decorativo e leva `aria-hidden="true"`.

``` code
<h3>
  <button type="button" aria-expanded="false" aria-controls="sec-docs" id="btn-docs">
    Documentos para enviar
    <svg aria-hidden="true" …></svg>
  </button>
</h3>
<div id="sec-docs" role="region" aria-labelledby="btn-docs" hidden="until-found">
  …
</div>
```

**Coloque o painel logo após o botão no DOM.** Assim, o próximo elemento focável depois do cabeçalho é o conteúdo ([HDS](https://hds.hel.fi/components/accordion/accessibility)).

**Permita a pesquisa na página.** Mantenha o conteúdo fechado no DOM com `hidden="until-found"`, para que a pesquisa do navegador abra a seção; ao receber `beforematch`, atualize `aria-expanded` e o chevron ([Ontario](https://designsystem.ontario.ca/components/detail/accordions.html)).

**Teclado.** Tab move o foco entre cabeçalhos; Enter e Espaço abrem e fecham ([Geist](https://vercel.com/geist/collapse)). A pessoa sai do painel aberto com Tab (WCAG 2.2, 2.1.2).

**Contraste no fundo escuro.** Na variante em `.tr-inverse`, texto e chevron usam `--t-fg-1` escuro, que mantém 4,5:1 com o fundo (WCAG 2.2, 1.4.3). O gov.br também passa a fonte para branco nessa versão por acessibilidade ([gov.br DS](https://www.gov.br/ds/components/accordion)).

**Funcione sem JavaScript.** Sem script, mostre todas as seções abertas ([GOV.UK](https://design-system.service.gov.uk/components/accordion/)).

> **Nota** As demonstrações usam `<details>` para funcionar sem JavaScript. Em produção, use `<details>` só no tipo Detalhes; no acordeão, use a estrutura de título e botão acima.

## Tokens usados

| Elemento                                       | Token                                |
|------------------------------------------------|--------------------------------------|
| Divisores entre seções                         | `--t-border-subtle`, `--stroke-thin` |
| Rótulo                                         | Body 16/24, peso 600, `--t-fg-1`     |
| Altura mínima do cabeçalho (alta, padrão)      | `--c-h-md`, `--c-h-lg`               |
| Preenchimento lateral do cabeçalho e do painel | `--sp-200`                           |
| Espaço inferior do painel                      | `--sp-400`                           |
| Texto do painel                                | `--t-fg-2`                           |
| Hover do cabeçalho                             | `--o-hover`                          |
| Foco                                           | `--t-focus`, `--stroke-thick`        |
| Rotação do chevron                             | `--m-normal`, `--m-ease-standard`    |
| Fundo escuro                                   | `.tr-inverse`                        |

## Considerações por plataforma

### Web desktop

Use o cursor de mão em todo o cabeçalho e o realce de hover. O botão "Abrir todas as seções" ajuda quem quer imprimir ou usar a pesquisa do navegador; veja também Impressão, em que todas as seções saem abertas.

### Web móvel

Acordeões encurtam páginas longas em telas compactas ([gov.br DS](https://www.gov.br/ds/components/accordion)), mas o risco de conteúdo não visto aumenta. Use a densidade baixa. Ao abrir uma seção longa, não role a página automaticamente; o cabeçalho permanece onde a pessoa tocou.

### Tablets e dobráveis

Em janelas expandidas, avalie se as seções cabem visíveis em um layout de dois painéis antes de recolhê-las. Abrir ou fechar o dobrável não altera quais seções estão abertas ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Abas
- Divisores
- Listas
- Oferecer ajuda
- Densidade
- Teclado

### Referências

- [Accordion](https://www.gov.br/ds/components/accordion) gov.br DS
- [Padrão Collapse](https://www.gov.br/ds/padroes/design/collapse) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls) Apple HIG
- [Accordion](https://design-system.service.gov.uk/components/accordion/) GOV.UK Design System
- [Details](https://design-system.service.gov.uk/components/details/) GOV.UK Design System
- [Accordions](https://designsystem.dk/komponenter/accordions/) DKFDS
- [Accordion](https://hds.hel.fi/components/accordion) Helsinki Design System
- [Accordion: accessibility](https://hds.hel.fi/components/accordion/accessibility) Helsinki Design System
- [Accordion](https://fluent2.microsoft.design/components/web/react/core/accordion/usage) Fluent 2
- [Collapse](https://vercel.com/geist/collapse) Geist
- [Accordions](https://designsystem.ontario.ca/components/detail/accordions.html) Ontario Design System
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                           |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Chevron passa para o fim do cabeçalho (D8), entram a variante em fundo escuro, os limites de uso do padrão de expandir e recolher, densidades e hover em camada. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                    |
