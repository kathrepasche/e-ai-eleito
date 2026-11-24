# Tooltips

Um tooltip é um rótulo flutuante e breve que nomeia um controle ou acrescenta um detalhe útil, sem ser indispensável, sobre ele.

O tooltip aparece junto ao elemento e desaparece quando a pessoa se afasta dele. Ele complementa a interface: o que a pessoa precisa saber para concluir a tarefa fica visível na página, como texto de apoio ou rótulo. No Trama existem dois tipos: o tooltip de rótulo, que aparece com hover ou foco num botão de ícone, e o tooltip de ajuda, que abre com clique num ícone de informação. Conteúdo com formatação, imagem, links ou botões vai num popover, que o gov.br DS chama de tooltip do tipo popover ([gov.br DS](https://www.gov.br/ds/components/tooltip)).

**Use um tooltip** para nomear botões só com ícone, explicar uma restrição ou limite de um controle, mostrar o texto completo de um conteúdo truncado ou dizer por que um controle está desativado ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tooltip/usage), [Geist](https://vercel.com/geist/tooltip)).

**Não use um tooltip** para informação essencial, como requisitos de formato de um campo: use texto de apoio visível ([DKFDS](https://designsystem.dk/komponenter/tooltip/), [HDS](https://hds.hel.fi/components/tooltip)). Não use para retorno do sistema, confirmações nem mensagens de erro: use toast, mensagem ou a mensagem junto ao campo ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tooltip/usage), [Ontario](https://designsystem.ontario.ca/components/detail/error-messaging.html)). Se você precisa de um texto para explicar o que a pessoa deve fazer, o tooltip também não basta; ofereça ajuda na página ou um guia ([gov.br DS](https://www.gov.br/ds/components/tooltip)).

## Anatomia

1.  **Alvo**: o controle descrito, ou um ícone de informação dedicado no tooltip de ajuda. Sempre focável.
2.  **Balão**: fundo `--t-fg-1`, texto `--t-bg`, raio `--r-md`, preenchimento `--sp-100` por `--sp-200`, texto 13/18. Largura mínima de 108px, o equivalente a cerca de 12 caracteres, e máxima de 240px; entre esses limites, a largura acompanha o texto e a altura cresce com ele ([gov.br DS](https://www.gov.br/ds/components/tooltip)).
3.  **Seta** (obrigatória): 16 por 8px, aponta para o alvo e fica centralizada no lado do balão em que aparece ([gov.br DS](https://www.gov.br/ds/components/tooltip), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tooltip/usage)).

O balão fica a `--sp-100` (4px) do alvo, a mesma distância usada pelo [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tooltip/usage), e flutua na camada `--z-4`, acima de diálogos, para nunca ser coberto ([gov.br DS](https://www.gov.br/ds/components/tooltip)).

## Tipos

| Tipo                         | Abre com                                        | Fecha com                                | Uso                                                                                    |
|------------------------------|-------------------------------------------------|------------------------------------------|----------------------------------------------------------------------------------------|
| Tooltip de rótulo            | Hover após 300ms ou foco por teclado.           | Saída do ponteiro, perda de foco ou Esc. | Nomear botões de ícone, descrever atalhos e mostrar texto truncado.                    |
| Tooltip de ajuda (toggletip) | Clique, toque ou Enter num ícone de informação. | Novo clique, clique fora ou Esc.         | Detalhe que só algumas pessoas precisam, ao lado de um rótulo de campo ou de um termo. |

O atraso de 300ms evita que o tooltip apareça quando o cursor apenas atravessa o elemento ([DKFDS](https://designsystem.dk/komponenter/tooltip/)). O tooltip de ajuda abre por clique para permitir selecionar o texto ([HDS](https://hds.hel.fi/components/tooltip/accessibility)).

## Boas práticas

**Descreva só o controle indicado.** Não explique controles vizinhos nem a tarefa maior ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help)).

**Não repita o rótulo visível.** Um tooltip "Limite de taxa" sobre o botão "Limite de taxa" não acrescenta nada. Explique o porquê, o escopo ou o limite ([Geist](https://vercel.com/geist/tooltip), [DKFDS](https://designsystem.dk/komponenter/tooltip/)).

**Mantenha o rótulo visível em ícones sempre que houver espaço.** Ícone sem texto só se justifica para ícones muito conhecidos; nesses casos, o tooltip de rótulo é obrigatório ([DKFDS](https://designsystem.dk/komponenter/tooltip/)). O tooltip nunca substitui rótulos de campos ([HDS](https://hds.hel.fi/components/tooltip)).

**Ponha tooltips só em elementos focáveis.** Links, botões e campos. Um tooltip sobre texto estático fica fora do alcance de quem usa teclado ([gov.br DS](https://www.gov.br/ds/components/tooltip)). Quando um texto truncado precisa do tooltip, torne o contêiner focável.

**Nunca coloque links ou botões no tooltip.** Quem usa toque não alcança um controle revelado por hover ([Geist](https://vercel.com/geist/tooltip), [DKFDS](https://designsystem.dk/komponenter/tooltip/)).

**Não envolva um campo rotulado com tooltip.** O texto vira um segundo rótulo invisível para leitores de tela. Coloque a ajuda num ícone ao lado ([Geist](https://vercel.com/geist/tooltip)).

**Posicione acima do alvo e inverta perto das bordas.** A posição padrão é acima. Perto do topo da janela, o tooltip vai para baixo; perto da base, para cima; perto da borda esquerda, para a direita; perto da borda direita, para a esquerda ([gov.br DS](https://www.gov.br/ds/components/tooltip)). Em qualquer posição, ele não esconde o que explica ([DKFDS](https://designsystem.dk/komponenter/tooltip/)).

**Mostre um tooltip por vez.** Ele atrai a atenção para um ponto; dois ao mesmo tempo competem ([gov.br DS](https://www.gov.br/ds/components/tooltip)).

**Não use tooltips para apresentar novidades.** Para chamar atenção a uma função nova, use o padrão de onboarding, que pode ser dispensado e não volta depois de aprendido ([gov.br DS](https://www.gov.br/ds/components/tooltip)).

**Faça** comece pelo verbo e descreva o que o controle faz.

**Não faça** descreva a interação ou escreva um parágrafo.

### Estados e comportamento

- **Exibição**: hover com atraso ou foco imediato. Só um tooltip aparece por vez.
- **Persistência**: o tooltip continua visível enquanto o ponteiro está sobre o alvo ou sobre o próprio balão, e some ao perder foco ou com Esc (WCAG 2.2, 1.4.13). Ele nunca fecha por tempo.
- **Junto com popover**: se o mesmo alvo abre um popover, o tooltip some enquanto o popover está aberto ([Blueprint](https://blueprintjs.com/docs/#core/components/tooltip)).
- **Controle desativado**: botões com o atributo `disabled` não recebem eventos nem foco; use `aria-disabled="true"` para que o tooltip possa explicar a condição ([Blueprint](https://blueprintjs.com/docs/#core/components/tooltip)).
- **Estados diferentes**: o texto pode mudar conforme o estado do controle, por exemplo "Fixar" e "Desafixar" ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help)).
- **Movimento**: entrada em `--m-fast`; sem transição com `prefers-reduced-motion` ou com as animações desligadas no produto.

> **Divergência entre referências** Feedback: o gov.br DS usa o tooltip também para feedback de uma ação anterior, com estados de sucesso, alerta e erro, e permite que ele feche após um tempo programado. O Fluent 2 e o Ontario excluem o tooltip de retorno do sistema e de erros. Pelo critério de acessibilidade, o Trama não tem tooltip de feedback nem fechamento por tempo: uma mensagem que some sozinha ou que só aparece com hover pode não ser percebida, e o conteúdo precisa persistir enquanto a pessoa o consulta (WCAG 2.2, 1.4.13). Nome acessível: o Geist dá o nome do botão de ícone com `aria-label`; o gov.br liga o gatilho ao tooltip com `aria-labelledby`. O Trama segue o gov.br no tooltip de rótulo, porque o texto lido é o mesmo que aparece na tela e não é anunciado duas vezes, e usa `aria-describedby` no tooltip que descreve. Sombra: o gov.br exige sombra no balão; o Trama dispensa a sombra porque o fundo invertido já separa o balão da página com contraste alto nos dois temas.

## Conteúdo

**Seja breve.** Limite o texto a 60 a 75 caracteres, lembrando que a tradução costuma alongar frases ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help)). O tooltip de ajuda aceita até três frases curtas; mais que isso vira página ([HDS](https://hds.hel.fi/components/tooltip)).

**Comece pelo verbo e oriente para a ação.** "Restaurar configurações padrão", "Adicionar ou remover idioma" ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/offering-help), [gov.br DS](https://www.gov.br/ds/components/tooltip)).

**Para controles sem rótulo, use o nome do comando.** "Duplicar", "Filtros". Escreva o tooltip de rótulo tão curto quanto seria o rótulo visível: "Excluir", nunca "Clique para excluir" ([DKFDS](https://designsystem.dk/komponenter/tooltip/)).

**Use caixa de frase e pontue só frases completas.** Fragmentos não levam ponto final ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tooltip/usage)). Não use título dentro do tooltip; se o conteúdo pede título, ele é um popover.

## Acessibilidade

- O balão tem `role="tooltip"` e um `id`. No tooltip de rótulo, o alvo aponta para ele com `aria-labelledby`; no tooltip que descreve, com `aria-describedby` ([gov.br DS](https://www.gov.br/ds/components/tooltip), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/tooltip/usage)).
- O tooltip aparece ao focar o alvo pelo teclado e não recebe foco; seu conteúdo é lido a partir do alvo. Esc fecha ([gov.br DS](https://www.gov.br/ds/components/tooltip)).
- Nunca dependa só do hover: ele não existe no teclado nem no toque ([gov.br DS](https://www.gov.br/ds/components/tooltip)).
- O ícone do tooltip de ajuda é um botão com nome acessível, como "Mais informações sobre o CPF" ([HDS](https://hds.hel.fi/components/tooltip/accessibility)).
- O conteúdo do tooltip não aparece na impressão. O que precisa ser impresso fica na página ([DKFDS](https://designsystem.dk/komponenter/tooltip/)).

## Tokens usados

| Elemento                 | Token                        |
|--------------------------|------------------------------|
| Fundo do balão e da seta | `--t-fg-1`                   |
| Texto do balão           | `--t-bg`                     |
| Raio                     | `--r-md`                     |
| Preenchimento            | `--sp-100`, `--sp-200`       |
| Distância do alvo        | `--sp-100`                   |
| Camada                   | `--z-4`                      |
| Movimento                | `--m-fast`, `--m-ease-enter` |

Como fundo e texto invertem entre os temas, o contraste entre `--t-fg-1` e `--t-bg` se mantém no claro e no escuro.

## Considerações por plataforma

### Web desktop

Tooltips de rótulo funcionam com ponteiro e teclado. Inclua o atalho de teclado no tooltip quando houver um, por exemplo "Duplicar (Ctrl+D)".

### Web móvel

Não há hover: na classe Compacta, o tooltip abre só por toque ou foco ([gov.br DS](https://www.gov.br/ds/components/tooltip)). Tooltips de rótulo dependem de toque longo, um gesto pouco conhecido, e muitas pessoas nunca os verão ([DKFDS](https://designsystem.dk/komponenter/tooltip/)). Por isso, prefira botões com texto visível. Quando usar botão só com ícone, mostre o rótulo no toque longo e oculte com um toque fora, como fazem os rótulos de ícone do [One UI](https://developer.samsung.com/one-ui/comp/toast.html). Tooltips de ajuda funcionam por toque e cabem na largura da tela menos as margens; as regras de inversão evitam que o balão saia da tela.

### Tablets e dobráveis

Tablets com teclado e trackpad recebem hover; sem eles, aplique as regras da web móvel. Detecte a capacidade com `@media (hover: hover)` em vez de supor pelo tamanho da tela.

## Recursos

### Relacionados

- Popovers
- Oferecer ajuda
- Botões
- Iconografia
- Mouse e trackpad

### Referências

- [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help) Apple HIG
- [Tooltip](https://www.gov.br/ds/components/tooltip) gov.br DS
- [Utilitário Tooltip](https://www.gov.br/ds/utilitarios/js/tooltip) gov.br DS
- [Tooltip](https://fluent2.microsoft.design/components/web/react/core/tooltip/usage) Fluent 2
- [Tooltip](https://designsystem.dk/komponenter/tooltip/) DKFDS
- [Tooltip](https://hds.hel.fi/components/tooltip) Helsinki Design System
- [Tooltip: accessibility](https://hds.hel.fi/components/tooltip/accessibility) Helsinki Design System
- [Tooltip](https://vercel.com/geist/tooltip) Geist
- [Tooltip](https://blueprintjs.com/docs/#core/components/tooltip) Blueprint
- [Toasts (label toast)](https://developer.samsung.com/one-ui/comp/toast.html) One UI
- [Error messaging](https://designsystem.ontario.ca/components/detail/error-messaging.html) Ontario Design System

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                           |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta largura mínima, seta obrigatória, inversão perto das bordas, camada e acionamento no toque, liga o rótulo por `aria-labelledby` e exclui tooltips de feedback e fechamento por tempo. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                    |
