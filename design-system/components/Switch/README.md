# Switch

Um switch liga ou desliga um ajuste, e a mudança vale no momento do toque ou do clique.

O switch imita um interruptor físico, como o de uma lâmpada; por isso as pessoas esperam que algo aconteça assim que o acionam ([HDS](https://hds.hel.fi/components/toggle-button)). O gov.br o reserva para ações binárias de efeito imediato, sem botão de enviar ([gov.br](https://www.gov.br/ds/components/switch)). Essa é a diferença em relação ao radio e ao checkbox, cuja escolha só vale depois de enviar o formulário ([DKFDS](https://designsystem.dk/komponenter/toggle/)). No Trama, o switch (`.tr-switch`) é um trilho em forma de pílula com um botão circular que desliza para a direita e se preenche com `--t-brand` quando ligado. Tecnicamente, é um checkbox com aparência de interruptor ([Blueprint](https://blueprintjs.com/docs/#core/components/switch)).

**Quando usar.** Para um único ajuste de dois estados opostos, de efeito imediato, como preferências e configurações ([gov.br](https://www.gov.br/ds/components/switch)): mostrar processos arquivados, receber notificações, ativar o modo compacto ([Geist](https://vercel.com/geist/toggle)), ou alternar entre uma funcionalidade nova e a antiga ([gov.br](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)).

**Quando não usar.**

- Se a escolha só vale depois de um botão Salvar ou Enviar: use checkbox ou radios. Evite switches em formulários longos com botão de enviar, porque a pessoa não sabe se a mudança já valeu ([gov.br](https://www.gov.br/ds/components/switch)).
- Se o ajuste precisa de estado misto: use checkbox ([Fluent](https://fluent2.microsoft.design/components/web/react/core/switch/usage)).
- Se a pessoa escolhe entre opções nomeadas, como duas visualizações: use o controle segmentado.
- Para escolher itens de uma lista: o switch só gerencia o estado de algo ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)).
- Se o efeito depende de uma chamada demorada ao servidor ([HDS](https://hds.hel.fi/components/toggle-button)). No Trama, quando a espera for curta, o switch muda na hora e reverte com uma mensagem se o servidor recusar.

## Anatomia

1.  **Rótulo**: texto que nomeia o ajuste. Obrigatório no Trama.
2.  **Trilho**: raio `--r-pill`, borda `--t-border-control`. Ligado, preenchido com `--t-brand`.
3.  **Botão**: círculo que desliza. Desligado, em `--t-fg-2` à esquerda; ligado, em `--t-on-brand` à direita.
4.  **Ícone** (opcional): marca de seleção no botão ligado e “x” no desligado, para que o estado não dependa só da cor e da posição ([gov.br](https://www.gov.br/ds/components/switch)).
5.  **Rótulo de estado** (opcional): texto ao lado do trilho que nomeia a posição atual, sempre em par, como “Ativados” e “Desativados” ([gov.br](https://www.gov.br/ds/components/switch)).
6.  **Descrição** (opcional): uma frase abaixo, ligada por `aria-describedby`.
7.  **Rótulo do grupo** (opcional): nome do conjunto, com `role="group"` e `aria-labelledby`.

## Tipos

| Densidade | Classe e trilho               | Uso                                                                                                                        |
|-----------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Alta      | `.tr-switch--sm`, 32 por 18px | Só com mouse, em tabelas e painéis densos                                                                                  |
| Padrão    | `.tr-switch`, 40 por 22px     | Telas de configuração com mouse                                                                                            |
| Baixa     | `.tr-switch--lg`, 52 por 30px | Obrigatória em toque e na classe Compacta, com maior área de interação ([gov.br](https://www.gov.br/ds/components/switch)) |

## Boas práticas

**Aplique a mudança na hora e confirme o resultado.** Não peça Salvar nem Enviar ([gov.br](https://www.gov.br/ds/components/switch)). Quando o efeito não for visível na própria tela, mostre um toast que diga o que mudou, como “Avisos de prazo ativados” ([Geist](https://vercel.com/geist/toggle)).

**Todo switch tem um estado definido.** Ligado ou desligado, sempre com um valor padrão ([HDS](https://hds.hel.fi/components/toggle-button)). Ele muda o estado, mostra o estado atual e deixa claro qual é a outra opção ([HDS](https://hds.hel.fi/foundation/guidelines/checkbox-radiobutton-toggle)).

**Mantenha o switch parado enquanto ele muda.** O trilho não se desloca quando o botão desliza, o rótulo de estado troca ou o anel de foco aparece. Reserve para o rótulo de estado a largura do texto mais longo do par ([gov.br](https://www.gov.br/ds/components/switch)).

**Use rótulos de estado só em par e sempre na mesma posição.** Um rótulo para um só estado é ambíguo; mude o texto, nunca a posição ([gov.br](https://www.gov.br/ds/components/switch)). Prefira-os quando o switch aparece sozinho ou quando o público tem pouca familiaridade com o controle.

**Faça toda a linha clicável quando rótulo e trilho estão juntos.** A área de interação inclui o trilho e o rótulo. Se o rótulo fica longe do trilho, como numa coluna de tabela, só o trilho é interativo ([gov.br](https://www.gov.br/ds/components/switch)).

**Alinhe os switches em coluna e com o mesmo posicionamento de rótulo.** Empilhe-os para que os controles fiquem numa linha reta ([DKFDS](https://designsystem.dk/komponenter/toggle/)). O Trama coloca o trilho antes do texto, como no checkbox, e mantém essa posição em todo o produto ([gov.br](https://www.gov.br/ds/components/switch)).

**Agrupe switches com um checkbox principal.** Quando vários switches formam um conjunto, um checkbox principal liga ou desliga todos e mostra o estado misto quando só parte está ligada ([gov.br](https://www.gov.br/ds/components/switch)). Siga o ciclo descrito em Checkbox.

**Mostre perto do switch o que ele revela.** Se ligar o switch faz aparecer outros elementos, coloque-os logo abaixo dele ([HDS](https://hds.hel.fi/components/toggle-button/accessibility)).

**Desabilite só quando a pessoa puder habilitar.** Um switch fica desabilitado quando reflete uma escolha anterior da pessoa ([gov.br](https://www.gov.br/ds/components/switch)). Diga o motivo e a ação que o habilita, como “Cadastre um celular em Perfil para ativar”. Se a pessoa não pode habilitá-lo, retire o switch.

**Faça** rótulo que descreve o efeito quando ligado.

**Não faça** pergunta como rótulo: aumenta a carga cognitiva.

### Estados

| Estado       | Aparência                                                                               |
|--------------|-----------------------------------------------------------------------------------------|
| Desligado    | Trilho `--t-surface-raised` com borda `--t-border-control`; botão `--t-fg-2` à esquerda |
| Ligado       | Trilho `--t-brand`; botão `--t-on-brand` à direita                                      |
| Hover        | Camada `--o-hover` em volta do trilho, só com ponteiro                                  |
| Foco         | Anel de 2px `--t-focus` em volta do trilho, em `:focus-visible`                         |
| Desabilitado | Trilho e texto em `--t-fg-disabled`, com motivo e ação ao lado                          |
| Processando  | Mantém o novo estado e mostra um spinner pequeno ao lado do rótulo                      |

A transição do botão usa `--m-normal` com `--m-ease-standard`. Ela é removida com `prefers-reduced-motion` e com o controle de animações do produto, porque o estado continua claro pela posição do botão. A HDS considera essa animação não decorativa ([HDS](https://hds.hel.fi/components/toggle-button/accessibility)).

> **Divergência entre referências** *Rótulos de estado:* a versão 1.0 proibia “Ligado” e “Desligado” ao lado do trilho; o gov.br os recomenda, em par, porque ajudam a entender a posição da chave. Pelo critério de acessibilidade (o estado ganha uma pista em texto, além de cor e posição), o Trama passa a aceitá-los, em par e na mesma posição. *Rótulo obrigatório:* o gov.br trata o rótulo como opcional; o Fluent exige nome acessível mesmo quando o rótulo visível é dispensado. Pelo critério de acessibilidade (WCAG 2.2, 4.1.2), o Trama exige rótulo. *Controle de grupo:* a HIG admite um switch que liga ou desliga ajustes subordinados; o gov.br pede um checkbox principal. Pelo critério de acessibilidade, o Trama segue o gov.br, porque o switch não tem estado misto para mostrar um grupo parcialmente ligado.

## Conteúdo

**Nomeie o ajuste pelo efeito quando ligado.** “Modo compacto” basta quando o substantivo é claro; se for ambíguo, use um verbo específico, como “Permitir notificações” ([HDS](https://hds.hel.fi/components/toggle-button); [Fluent](https://fluent2.microsoft.design/components/web/react/core/switch/usage)). O rótulo não pode ser neutro nem ambíguo ([gov.br](https://www.gov.br/ds/components/switch)).

**Não use perguntas.** “Deseja receber notificações?” vira “Permitir notificações” ([Fluent](https://fluent2.microsoft.design/components/web/react/core/switch/usage)).

**Escreva rótulos curtos, em caixa de frase e sem ponto final** ([gov.br](https://www.gov.br/ds/components/switch); [Fluent](https://fluent2.microsoft.design/components/web/react/core/switch/usage)).

**Escreva rótulos de estado com até três palavras.** Use pares que concordam com o rótulo, como “Ativados” e “Desativados” ou “Visível” e “Oculto” ([gov.br](https://www.gov.br/ds/components/switch)).

**Descreva só o estado ligado.** A descrição opcional explica o que acontece quando o switch está ligado ([Geist](https://vercel.com/geist/toggle)).

## Acessibilidade

- Use `<input type="checkbox" role="switch">` dentro de `<label>`, como no `.tr-switch`, com o estado no atributo `checked`. Sem input nativo, atualize `aria-checked` a cada mudança ([gov.br](https://www.gov.br/ds/components/switch)).
- O leitor de tela anuncia o rótulo e o estado atual ([gov.br](https://www.gov.br/ds/components/switch)). Se os rótulos de estado só repetem ligado e desligado, oculte-os com `aria-hidden="true"` para não duplicar o anúncio.
- Tab leva ao switch e Espaço alterna o estado. Em implementações sem input nativo, aceite também Enter ([gov.br](https://www.gov.br/ds/components/switch)).
- Agrupe switches relacionados com `role="group"` e `aria-labelledby` ([DKFDS](https://designsystem.dk/komponenter/toggle/)).
- Se o switch altera algo em outra parte da tela, informe a mudança numa região `aria-live` ([HDS](https://hds.hel.fi/components/toggle-button/accessibility)).
- Ofereça área de interação ampla, inclusive para pessoas com deficiência motora ([gov.br](https://www.gov.br/ds/components/switch)): a linha tem pelo menos `--c-touch` de altura. A borda `--t-border-control` atende a 3:1 (WCAG 2.2, 1.4.11).

## Tokens usados

| Elemento                    | Token                                                                                          |
|-----------------------------|------------------------------------------------------------------------------------------------|
| Trilho                      | `--r-pill`, `--stroke-thin`, `--t-border-control`, `--t-surface-raised`                        |
| Trilho ligado               | `--t-brand`                                                                                    |
| Botão e ícone               | `--t-fg-2`; ligado `--t-on-brand`; ícone `--icon-xs` na alta e na padrão, `--icon-sm` na baixa |
| Espaço entre trilho e texto | `--sp-300`                                                                                     |
| Altura mínima da linha      | `--c-touch`                                                                                    |
| Hover                       | `--o-hover`                                                                                    |
| Movimento                   | `--m-normal`, `--m-ease-standard`                                                              |
| Foco                        | `--t-focus`, `--stroke-thick`                                                                  |

## Considerações por plataforma

### Web desktop

Use switches no corpo da página, não em barras de ferramentas ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)). Em telas de configuração densas, com mouse, a densidade alta é aceitável; alinhe os switches pela borda inicial da coluna de controles.

### Web móvel

Use a densidade baixa (`.tr-switch--lg`), que oferece área maior ao toque ([gov.br](https://www.gov.br/ds/components/switch)). Em listas de configuração, o switch pode ficar na extremidade final da linha, com o texto da linha como rótulo ([Apple](https://developer.apple.com/design/human-interface-guidelines/toggles)); a linha inteira continua sendo o alvo de toque.

### Tablets e dobráveis

Em telas de configuração com dois painéis, a lista de categorias fica num painel e os switches no outro. Em toque, mantenha a densidade baixa. Ao dobrar ou desdobrar o aparelho, preserve o estado e a posição de rolagem.

## Recursos

### Relacionados

- Checkbox
- Radio
- Controle segmentado
- Configurações
- Toasts
- Densidade

### Referências

- [Switch](https://www.gov.br/ds/components/switch) gov.br DS
- [Ajuda e comunicação](https://www.gov.br/ds/padroes/design/ajuda-comunicacao) gov.br DS
- [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles) Apple HIG
- [Toggle switch](https://designsystem.dk/komponenter/toggle/) Det Fælles Designsystem
- [ToggleButton](https://hds.hel.fi/components/toggle-button) Helsinki Design System
- [ToggleButton: acessibilidade](https://hds.hel.fi/components/toggle-button/accessibility) Helsinki Design System
- [Checkboxes, radio buttons, or toggles?](https://hds.hel.fi/foundation/guidelines/checkbox-radiobutton-toggle) Helsinki Design System
- [Switch](https://fluent2.microsoft.design/components/web/react/core/switch/usage) Fluent 2
- [Toggle](https://vercel.com/geist/toggle) Geist
- [Switch](https://blueprintjs.com/docs/#core/components/switch) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                   |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta densidades (`.tr-switch--sm` e `--lg`), ícones, rótulos de estado em par, área de interação, grupo com checkbox principal e a regra de desabilitado, e passa a exigir rótulo. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                            |
