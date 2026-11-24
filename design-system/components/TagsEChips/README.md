# TagsEChips

Tags e chips representam palavras-chave, categorias, filtros ou valores escolhidos, em blocos curtos que a pessoa pode remover, selecionar ou apenas ler.

No Trama, o chip (`.tr-chip`) é um bloco compacto de texto, com borda `--t-border`, fundo `--t-surface-1` e, quando dispensável, um botão de remover. Ele serve para metadados de conteúdo ([DKFDS](https://designsystem.dk/komponenter/tags/)), filtros ativos e valores escolhidos num campo ([Blueprint](https://blueprintjs.com/docs/#core/components/tag)). O gov.br reúne sob o nome tag cinco tipos: interação, texto, status, contagem e ícone ([gov.br DS](https://www.gov.br/ds/components/tag)). O Trama cobre aqui os dois primeiros; status e contagem usam o badge.

**Quando usar.** Para rotular e categorizar itens com palavras-chave ([gov.br DS](https://www.gov.br/ds/components/tag)); para mostrar filtros de um objeto ([HDS](https://hds.hel.fi/components/tag)); para representar termos de pesquisa que a pessoa edita como unidade ([HIG](https://developer.apple.com/design/human-interface-guidelines/search-fields)); e para listar destinatários ou etiquetas digitados num campo ([HIG](https://developer.apple.com/design/human-interface-guidelines/token-fields)).

**Quando não usar.** Para status de sistema e contagens, use o badge ([Fluent](https://fluent2.microsoft.design/components/web/react/core/tag/usage), [HDS](https://hds.hel.fi/components/tag)). Para ações, como Salvar, use um botão; e evite chips interativos perto de botões, porque se confundem ([gov.br DS](https://www.gov.br/ds/components/tag)). Para substituir a navegação do site, use a navegação ([DKFDS](https://designsystem.dk/komponenter/tags/)).

## Anatomia

1.  **Superfície** (`.tr-chip`): 28px de altura na densidade padrão, raio `--r-md`, borda `--t-border`, fundo `--t-surface-1`. Uma linha só ([gov.br DS](https://www.gov.br/ds/components/tag)).
2.  **Ícone** (opcional): à esquerda do rótulo, quando reforça a mensagem ([gov.br DS](https://www.gov.br/ds/components/tag)).
3.  **Rótulo**: substantivo ou adjetivo curto, obrigatório.
4.  **Botão de remover**: só no chip dispensável; botão de 24px, sempre a ação secundária ([gov.br DS](https://www.gov.br/ds/components/tag), [Fluent](https://fluent2.microsoft.design/components/web/react/core/tag/usage)).

O Trama dá ao chip raio `--r-md` e reserva `--r-pill` ao badge, como o gov.br, que usa cantos levemente arredondados nas tags de interação e de texto e pílula nas de contagem e ícone ([gov.br DS](https://www.gov.br/ds/components/tag)). O GOV.UK mudou o visual das próprias tags depois que pessoas tentaram clicar nelas achando que eram botões ([GOV.UK](https://design-system.service.gov.uk/components/tag/)).

## Tipos

| Tipo          | Interação                | Uso                                                                                                                                                                                                                 |
|---------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Texto         | Nenhuma                  | Palavras-chave e categorias de um conteúdo. Nunca interativo ([gov.br DS](https://www.gov.br/ds/components/tag)).                                                                                                   |
| Dispensável   | Botão de remover         | Filtros ativos e valores que a pessoa adicionou; remover desfaz a escolha ([gov.br DS](https://www.gov.br/ds/components/tag), [HDS](https://hds.hel.fi/components/tag)).                                            |
| Persistente   | Seleciona e desseleciona | Filtros e preferências que ligam e desligam; vários podem estar selecionados. Usa `aria-pressed` ([gov.br DS](https://www.gov.br/ds/components/tag), [Geist](https://vercel.com/geist/badge)).                      |
| Link          | Navega                   | Leva à lista de conteúdos da mesma categoria; é navegação direta ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao), [HDS](https://hds.hel.fi/components/tag)).                                           |
| Campo de tags | Digitar e escolher       | Transforma o texto digitado ou escolhido numa lista em chips dispensáveis ([gov.br DS](https://www.gov.br/ds/components/tag), [Blueprint](https://blueprintjs.com/docs/#core/components/tag-input)). Veja Combobox. |

**Contagem.** A tag de contagem do gov.br corresponde ao `.tr-badge--count`: até três dígitos e, acima de 999, “999+”, com o valor exato num tooltip e no nome acessível ([gov.br DS](https://www.gov.br/ds/components/tag)). A tag de status e a de ícone também viram badge; status só por cor exige tooltip ([gov.br DS](https://www.gov.br/ds/components/tag)).

## Boas práticas

**Não misture tipos no mesmo grupo.** Dispensáveis e persistentes nunca aparecem juntos no mesmo componente ou grupo ([gov.br DS](https://www.gov.br/ds/components/tag)), e chips interativos não se misturam com chips de texto: depois de aprender como um grupo se comporta, a pessoa espera o mesmo sempre ([gov.br DS](https://www.gov.br/ds/components/tag)).

**Use o mínimo de chips que faça sentido.** Se tudo parece importante, nada chama atenção ([gov.br DS](https://www.gov.br/ds/components/tag), [GOV.UK](https://design-system.service.gov.uk/components/tag/)). Os chips precisam poder ser ignorados sem prejudicar o uso ([DKFDS](https://designsystem.dk/komponenter/tags/)). Use uma cor por chip e não exagere na variedade ([gov.br DS](https://www.gov.br/ds/components/tag)).

**Disponha lado a lado e deixe quebrar linha.** Os chips ocupam o espaço horizontal e passam para a linha seguinte quando ele acaba, com espaço constante de `--sp-200` entre eles ([gov.br DS](https://www.gov.br/ds/components/tag), [HDS](https://hds.hel.fi/components/tag)). Dentro de cards, tabelas e diálogos, seguem as regras desses componentes.

**Mostre um chip “+n” quando faltar espaço.** Ele mostra quantos estão ocultos e é interativo. Se a pessoa precisa ver todos para editar, deixe quebrar linha ([Fluent](https://fluent2.microsoft.design/components/web/react/core/tag/usage)).

**Não torne interativo um chip que só informa.** Um chip nunca substitui um botão de ação ([HDS](https://hds.hel.fi/components/tag)).

**Faça** Mostre a informação mais útil, como o nome da pessoa, e dê ao botão de remover um nome que inclua o valor.

**Não faça** Use verbos nos rótulos, misture chips dispensáveis, persistentes e de texto no mesmo grupo e mostre identificadores internos.

### Estados

Só chips interativos têm estados: repouso, hover, pressionado, foco, selecionado e arrastado. No chip dispensável, hover, pressionado e foco acontecem no botão de remover; no persistente e no de link, no chip inteiro ([gov.br DS](https://www.gov.br/ds/components/tag)). Hover é a camada `--o-hover`. O selecionado usa `aria-pressed="true"` e um sinal além da cor, como o ✓. Ao arrastar para reordenar, o chip usa `.tr-dragging` e os vizinhos se deslocam para abrir espaço ([gov.br DS](https://www.gov.br/ds/components/tag)). Não há chip desabilitado: num campo editável, um valor que não se altera aparece sem botão de remover ([Fluent](https://fluent2.microsoft.design/components/web/react/core/tag/usage)).

### Densidade

Três densidades, como no gov.br ([gov.br DS](https://www.gov.br/ds/components/tag)): alta com mouse em tabelas e listas densas; padrão; baixa em toque e na classe Compacta, com área de ação de `--c-touch` nos chips interativos.

### Comportamento

**Crie chips por digitação ou por escolha.** Use um campo de texto para chips criados livremente e um select ou combobox para chips sugeridos pelo sistema; os chips criados são sempre dispensáveis ([gov.br DS](https://www.gov.br/ds/components/tag)). Enter conclui a criação, assim como um botão “Adicionar” ou sair do campo depois de digitar ([gov.br DS](https://www.gov.br/ds/components/tag)); a vírgula também separa valores ([HIG](https://developer.apple.com/design/human-interface-guidelines/token-fields), [Blueprint](https://blueprintjs.com/docs/#core/components/tag-input)). Mantenha rótulos consistentes: sugira os existentes com autocompletar para evitar duplicatas como “Contrato” e “Contratos” ([gov.br DS](https://www.gov.br/ds/components/tag)).

**Remova com Backspace e devolva o foco.** Com o cursor no início do campo, Backspace remove o último chip ([Fluent](https://fluent2.microsoft.design/components/web/react/core/tagpicker/usage), [Blueprint](https://blueprintjs.com/docs/#core/components/tag-input)). Depois de remover pelo botão, mova o foco para o chip seguinte ou, se não houver, para o campo. Para muitos filtros, ofereça “Limpar tudo” ([Fluent](https://fluent2.microsoft.design/components/web/react/core/tagpicker/usage)).

## Conteúdo

**Use substantivos ou adjetivos, nunca verbos.** “Criação de conteúdo”, não “Criar conteúdo” ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy), [gov.br DS](https://www.gov.br/ds/components/tag)).

**Use o mínimo de palavras, de preferência uma.** ([gov.br DS](https://www.gov.br/ds/components/tag), [HDS](https://hds.hel.fi/components/tag)). Escreva em caixa de frase, com termos que a pessoa reconhece do contexto ([DKFDS](https://designsystem.dk/komponenter/tags/)). Em chips de filtro, mostre o campo e o valor, como “Ano: 2026”.

**Limite a 100 caracteres e a uma linha.** Se um texto maior for inevitável, ou se o chip passar da largura disponível, trunque com reticências (`.tr-truncate`), mostre o texto completo num tooltip focável e mantenha-o no nome acessível ([gov.br DS](https://www.gov.br/ds/components/tag)). Nunca deixe menos de três caracteres de uma palavra (decisão D15).

> **Divergência entre referências** O Fluent desaconselha truncar o texto de tags ([Fluent](https://fluent2.microsoft.design/components/web/react/core/tag/usage)). O gov.br limita a tag a 100 caracteres e trunca a partir daí, com tooltip ([gov.br DS](https://www.gov.br/ds/components/tag)). A decisão D15 permite truncar chips com o texto completo acessível. O Trama adota o limite de 100 caracteres do gov.br e trunca também por largura, porque valores digitados pela pessoa podem ter qualquer tamanho; o texto completo continua no tooltip e no nome acessível.

## Acessibilidade

**Agrupe chips numa lista com nome.** Use `ul`, ou `role="list"`, com `aria-labelledby` apontando para o título do grupo.

**Dê nome ao botão de remover.** “Remover filtro Ano: 2026” ([HDS](https://hds.hel.fi/components/tag/accessibility)). O foco passa por todos os controles internos, que ativam com Enter ou Espaço ([gov.br DS](https://www.gov.br/ds/components/tag)).

**Escolha o papel pelo efeito.** Se leva a outra página, é link; se muda o conteúdo, como filtrar, é botão ([HDS](https://hds.hel.fi/components/tag/accessibility)). O persistente é botão com `aria-pressed`.

**Não use só a cor.** O texto carrega o significado; a cor não pode ser a única forma de diferenciar categorias ([gov.br DS](https://www.gov.br/ds/components/tag); WCAG 2.2, 1.4.1). Cores personalizadas atendem 4,5:1 para o texto (WCAG 2.2, 1.4.3).

**Garanta alvos.** O botão de remover tem 24px, o mínimo do critério WCAG 2.2, 2.5.8 com mouse; em toque, a área de ação chega a `--c-touch`. Anuncie inclusão e remoção numa região `aria-live`.

## Tokens usados

| Token                              | Uso                                               |
|------------------------------------|---------------------------------------------------|
| `--t-surface-1`, `--t-border`      | Fundo e borda do chip                             |
| `--t-fg-1`, `--t-fg-2`             | Rótulo; ícone de remover                          |
| `--o-hover`, `--o-pressed`         | Estados do botão de remover e do chip persistente |
| `--r-md`, `--r-sm`                 | Raio do chip e do botão de remover                |
| `--sp-100`, `--sp-300`, `--sp-200` | Espaços internos; espaço entre chips              |
| `--t-focus`                        | Anel de foco                                      |

## Considerações por plataforma

### Web desktop

No campo de tags, as setas para a esquerda e para a direita levam o foco aos chips, e Backspace ou Delete removem o chip focado ([Blueprint](https://blueprintjs.com/docs/#core/components/tag-input)). Um menu de contexto no chip pode oferecer editar o valor ([HIG](https://developer.apple.com/design/human-interface-guidelines/token-fields)); ofereça a mesma ação por teclado.

### Web móvel

Use densidade baixa e deixe os chips quebrarem linha; não use rolagem horizontal escondida para filtros importantes. Mostre o resumo dos filtros ativos acima dos resultados, com “Limpar tudo”.

### Tablets e dobráveis

Em layouts de dois painéis, os chips de filtro ficam no topo do painel da lista que eles filtram. Ao mudar de classe de janela, preserve os filtros ativos e recalcule o chip “+n”.

## Recursos

### Relacionados

- Badges
- Campo de pesquisa
- Combobox
- Pesquisa

### Referências

- [Tag (Etiqueta)](https://www.gov.br/ds/components/tag) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Navegação](https://www.gov.br/ds/padroes/design/navegacao) gov.br DS
- [Token fields](https://developer.apple.com/design/human-interface-guidelines/token-fields) Apple HIG
- [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields) Apple HIG
- [Tag: usage](https://fluent2.microsoft.design/components/web/react/core/tag/usage) Fluent 2
- [TagPicker: usage](https://fluent2.microsoft.design/components/web/react/core/tagpicker/usage) Fluent 2
- [Tag](https://design-system.service.gov.uk/components/tag/) GOV.UK Design System
- [Tags](https://designsystem.dk/komponenter/tags/) DKFDS
- [Tag](https://hds.hel.fi/components/tag) Helsinki Design System
- [Tag: accessibility](https://hds.hel.fi/components/tag/accessibility) Helsinki Design System
- [Badge](https://vercel.com/geist/badge) Geist
- [Tag](https://blueprintjs.com/docs/#core/components/tag) Blueprint
- [Tag input](https://blueprintjs.com/docs/#core/components/tag-input) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta os tipos dispensável e persistente, a proibição de misturá-los, rótulos sem verbo, o limite de 100 caracteres, a contagem até 999+, a criação por Enter, botão ou saída do campo, densidades e reordenação por arraste. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                      |
