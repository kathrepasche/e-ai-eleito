# Botoes

Um botão inicia uma ação imediata, como salvar, enviar ou excluir.

O botão combina estilo, conteúdo e papel ([HIG](https://developer.apple.com/design/human-interface-guidelines/buttons)). O gov.br organiza o botão em dois tipos (padrão e circular) e três ênfases (primária, secundária e terciária) ([gov.br DS](https://www.gov.br/ds/components/button)). No Trama, todo botão parte da classe `.tr-btn` e recebe modificadores de ênfase, tipo e densidade.

**Quando usar.** Para ações que mudam estado ou dados: enviar um formulário, salvar uma alteração, abrir um diálogo, iniciar uma tarefa ([GOV.UK](https://design-system.service.gov.uk/components/button/), [Geist](https://vercel.com/geist/button)).

**Quando não usar.** Para levar a pessoa a outra página ou outro endereço, use um link ([DKFDS](https://designsystem.dk/komponenter/knapper/), [Fluent](https://fluent2.microsoft.design/components/web/react/core/button/usage)). Para ligar e desligar uma configuração com efeito imediato, use um switch. Para escolher uma entre poucas opções de visualização, use um controle segmentado. Para várias ações relacionadas a um mesmo objeto, use um menu.

## Anatomia

1.  **Superfície**: retângulo com raio `--r-md` e altura `--c-h-md` na densidade padrão. Na ênfase sutil, a superfície transparente continua definindo a área de toque ([gov.br DS](https://www.gov.br/ds/components/button)).
2.  **Rótulo**: texto em peso 600, centralizado. Obrigatório no botão padrão; o botão circular leva o rótulo em `aria-label`.
3.  **Ícone**: opcional no botão padrão, antes do rótulo, separado por `--sp-200`; obrigatório no circular, em `--icon-md`.
4.  **Indicador de carregamento** e **seta de menu** (condicionais).

## Tipos

| Tipo           | Classe                                     | Uso                                                                                                                                                                  |
|----------------|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Primário       | `.tr-btn--primary`                         | A ação mais provável ou essencial da tela. Um por vista.                                                                                                             |
| Secundário     | `.tr-btn`                                  | Ações de apoio, que não são o objetivo principal da página ([gov.br DS](https://www.gov.br/ds/components/button)).                                                   |
| Sutil          | `.tr-btn--subtle`                          | Equivale à ênfase terciária do gov.br: ações opcionais e de suporte, como Cancelar, e botões dentro de outros componentes.                                           |
| Perigo         | `.tr-btn--danger`                          | Confirmação final de uma ação destrutiva que não se desfaz com facilidade.                                                                                           |
| Circular       | `.tr-btn--circle`                          | Ação comunicada só pelo ícone, isolada ou dentro de outros componentes ([gov.br DS](https://www.gov.br/ds/components/button)). 32, 40 ou 48px, conforme a densidade. |
| Ícone quadrado | `.tr-btn--icon`                            | Ícones agrupados numa barra de ferramentas.                                                                                                                          |
| Alternância    | qualquer tipo com `aria-pressed`           | Liga e desliga um estado, como Favorito ou Negrito.                                                                                                                  |
| Dividido       | `.tr-split`                                | Uma ação padrão clara com até quatro variações próximas ([Geist](https://vercel.com/geist/split-button)).                                                            |
| Bloco          | `.tr-btn--block`, `.tr-btn--block-compact` | Largura total do contêiner. A variante `--block-compact` ocupa a largura toda só abaixo de 600px e volta à largura do rótulo a partir da classe Média.               |

### Densidade

As densidades do gov.br (baixa 48px, padrão 40px, alta 32px) coincidem com as alturas de controle do Trama ([gov.br DS](https://www.gov.br/ds/components/button)): `.tr-btn--lg`, padrão e `.tr-btn--sm`, ou `data-density` no contêiner, que ajusta `--d-control`. Rótulo e ícone não mudam de tamanho. A densidade baixa é obrigatória em toque e na classe Compacta; a alta só vale com mouse ou trackpad, em tabelas e ferramentas.

## Boas práticas

**Tenha um botão primário por vista.** Mais de uma chamada principal reduz o impacto de cada uma e dificulta saber o que fazer a seguir ([GOV.UK](https://design-system.service.gov.uk/components/button/), [DKFDS](https://designsystem.dk/komponenter/knapper/)). Use a ênfase primária de forma limitada, em ações voltadas para o objetivo principal da tela ([gov.br DS](https://www.gov.br/ds/components/button)). Se várias ações têm a mesma prioridade, use o estilo secundário em todas ([Fluent](https://fluent2.microsoft.design/components/web/react/core/button/usage)).

**Destaque uma única ação de conversão por tela.** Quando a tela existe para levar a pessoa a iniciar ou concluir um fluxo relevante, como “Solicitar benefício”, essa ação usa `.tr-btn--primary.tr-btn--lg`, fica numa posição nobre com espaço livre em volta e nunca aparece desabilitada. Use no máximo uma dessas ações por tela e por fluxo ([gov.br DS](https://www.gov.br/ds/components/magicbutton)).

> **Divergência entre referências** O gov.br define o Magic Button, um componente separado com moldura, sombra e cor própria da paleta de destaque, para ações de conversão, no máximo um por tela ou fluxo e sem estado desabilitado ([gov.br DS](https://www.gov.br/ds/components/magicbutton)). As demais referências tratam a chamada principal com o próprio botão primário ([GOV.UK](https://design-system.service.gov.uk/components/button/), [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons)). O Trama adota as regras de uso do Magic Button e não cria variante visual: a ação de conversão é o botão primário em densidade baixa. O próprio gov.br diz que o botão comum pode substituí-lo em todos os contextos.

**Ordene pela regra D4.** Em páginas e formulários, a ação principal vem primeiro, alinhada ao início do conteúdo, e as secundárias depois ([GOV.UK](https://design-system.service.gov.uk/components/button/)). Em diálogos, drawers e barras de ação de painéis, as ações ficam alinhadas ao fim, com a principal por último, à direita. Empilhados na classe Compacta, a principal fica em cima.

> **Divergência entre referências** O gov.br põe sempre a ênfase de maior relevância à direita e, em pilha vertical, mais abaixo ([gov.br DS](https://www.gov.br/ds/components/button)). O GOV.UK alinha a ação principal à borda esquerda do formulário ([GOV.UK](https://design-system.service.gov.uk/components/button/)). O Trama segue a decisão D4: principal primeiro em páginas, onde quem usa ampliação de tela a encontra junto ao último campo; à direita em diálogos e painéis, como o gov.br; em cima na pilha, onde é a primeira encontrada ao rolar e com leitor de tela.

**Mantenha uma área de proteção.** Perto de outros componentes, o botão precisa de espaço para ser notado e para que sua área de clique não se confunda com a vizinha ([gov.br DS](https://www.gov.br/ds/components/button)). Use `--sp-200` entre botões de um grupo e `--f-gap-actions` antes das ações de um formulário.

**Não dê papel primário a uma ação destrutiva.** Pela proeminência visual, as pessoas às vezes escolhem o botão primário sem ler o rótulo ([HIG](https://developer.apple.com/design/human-interface-guidelines/buttons)). Reserve `.tr-btn--danger` para a confirmação final e use outro estilo na chamada inicial. O vermelho nunca comunica a gravidade sozinho: o rótulo e o contexto dizem o que vai acontecer ([GOV.UK](https://design-system.service.gov.uk/components/button/)).

**No botão dividido, mantenha a ação padrão fora do menu.** O segmento principal executa a ação; o menu traz só as variações ([Fluent](https://fluent2.microsoft.design/components/web/react/core/button/usage)). Nunca coloque uma ação destrutiva como ação padrão de um botão dividido.

**Use o botão circular só com ícones fortemente reconhecíveis.** Sem rótulo visível, o ícone carrega toda a mensagem. Em telas de toque não há tooltip por hover, então escolha ícones de entendimento imediato ([gov.br DS](https://www.gov.br/ds/components/button)). Quando o significado não for óbvio, use o botão padrão com texto.

**Faça** Destaque uma única ação principal, primeiro na linha, e mantenha as demais no estilo secundário.

**Não faça** Use vários botões primários na mesma vista. Nenhum deles se destaca.

### Estados

Repouso, hover, pressionado, foco, ativado, desabilitado e carregando ([gov.br DS](https://www.gov.br/ds/components/button)). No primário, hover usa `--t-brand-hover` e pressionado usa `--t-brand-pressed`. Nas demais ênfases, hover e pressionado são uma camada na cor do primeiro plano do botão com opacidade `--o-hover` e `--o-pressed`. O foco aparece só em `:focus-visible`. A transição dura `--m-fast`.

**Ativado.** Botão ligado ou com menu aberto mantém a camada de hover (`[aria-pressed="true"]`, `[aria-expanded="true"]`).

**Desabilitado.** Se a pessoa não pode habilitar a ação por algo que ela mesma faça, como uma permissão que não tem, retire o botão da interface. Se pode, mostre o botão desabilitado com `aria-disabled="true"`, para que continue focável, e explique o motivo num texto próximo ou num tooltip focável ([Geist](https://vercel.com/geist/button)). Nunca desabilite o botão de envio de um formulário: deixe-o ativo e explique o problema com a validação. Botões desabilitados têm baixo contraste e confundem parte das pessoas ([GOV.UK](https://design-system.service.gov.uk/components/button/)).

### Comportamento

**Alternância.** No comportamento toggle, cada clique troca entre dois estados opostos ([gov.br DS](https://www.gov.br/ds/components/button)). Escolha uma de duas formas e não misture: rótulo fixo com `aria-pressed` alternando entre `true` e `false`, ou rótulo que muda (“Expandir” e “Retrair”) sem `aria-pressed` ([gov.br DS](https://www.gov.br/ds/components/button)). Mostre o estado ligado também pelo ícone, além da cor.

**Mostre o carregamento dentro do botão.** Se a ação não termina na hora, troque o ícone por um indicador e mantenha um rótulo, como “Salvando…” ([HIG](https://developer.apple.com/design/human-interface-guidelines/buttons), [HDS](https://hds.hel.fi/components/button)). Mantenha a largura do botão para o layout não pular. Ao terminar, diga o que mudou, como “Endereço atualizado”, e anuncie numa região `aria-live`.

> **Divergência entre referências** O gov.br substitui todo o conteúdo do botão pelo indicador de carregamento ([gov.br DS](https://www.gov.br/ds/components/button)). A HIG e o HDS mostram o indicador ao lado de um rótulo ([HIG](https://developer.apple.com/design/human-interface-guidelines/buttons), [HDS](https://hds.hel.fi/components/button)). O Trama mantém o rótulo, pelo critério de acessibilidade: o texto visível continua informando o que acontece a quem não reconhece o indicador e preserva o nome do botão.

**Proteja contra envios duplicados.** Ignore o segundo clique enquanto a ação está em andamento e trate a duplicidade também no servidor ([GOV.UK](https://design-system.service.gov.uk/components/button/)).

## Conteúdo

**Comece pelo verbo no infinitivo e diga o que acontece.** Use uma ou duas palavras, três quando for inevitável, sem artigo ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy), [HDS](https://hds.hel.fi/components/button)). Acrescente o objeto quando ele esclarecer o resultado: “Excluir projeto”, “Cancelar envio” ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy), [Geist](https://vercel.com/geist/button)).

**Responda à pergunta com o mesmo verbo.** Para “Salvar as alterações?”, use “Salvar” e “Cancelar”, nunca “Sim” e “Não” ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)).

**Escreva em caixa de frase, sem ponto final.** Só a primeira palavra e os nomes próprios levam maiúscula ([Fluent](https://fluent2.microsoft.design/components/web/react/core/button/usage), [GOV.UK](https://design-system.service.gov.uk/components/button/)).

> **Divergência entre referências** O gov.br escreve rótulos de botão com iniciais maiúsculas em todas as palavras, exceto artigos e preposições, como “Gerar Relatório” ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Fluent, GOV.UK e DKFDS usam caixa de frase. Pela decisão transversal D1, o Trama usa caixa de frase: “Gerar relatório”.

**Não trunque o rótulo.** O gov.br proíbe quebra de linha no rótulo ([gov.br DS](https://www.gov.br/ds/components/button)). O Trama mantém a meta de uma linha, mas, se zoom ou largura estreita não deixarem o texto caber, o rótulo quebra a linha; reticências nunca cortam o texto (decisão D15; WCAG 2.2, 1.4.10).

| Situação                        | Rótulo do Trama    |
|---------------------------------|--------------------|
| Avançar numa etapa de tarefa    | Continuar          |
| Avançar salvando os dados       | Salvar e continuar |
| Última etapa de um fluxo        | Concluir           |
| Confirmar na página de revisão  | Confirmar e enviar |
| Anexar um arquivo               | Enviar arquivo     |
| Obter um arquivo                | Baixar             |
| Diálogo “Excluir este arquivo?” | Cancelar · Excluir |

A tabela segue o vocabulário controlado do Trama e padrões do GOV.UK ([GOV.UK](https://design-system.service.gov.uk/components/button/)). Evite “OK” e “Enviar” sem objeto.

## Acessibilidade

**Use o elemento certo.** Ação usa `<button>`; navegação usa `<a href>` ([gov.br DS](https://www.gov.br/ds/components/button), [DKFDS](https://designsystem.dk/komponenter/knapper/)). Link com aparência de botão também responde à tecla Espaço ([gov.br DS](https://www.gov.br/ds/components/button)).

**Dê nome a todo botão circular.** O `aria-label` nomeia a ação e o alvo, como “Adicionar membro à equipe”, e o mesmo texto aparece num tooltip no hover e no foco ([gov.br DS](https://www.gov.br/ds/components/button)). Não acrescente `aria-label` a um botão que já tem texto visível, porque ele substitui o rótulo lido ([Geist](https://vercel.com/geist/button)).

**Esconda ícones decorativos.** Ícone ao lado do rótulo leva `aria-hidden="true"` e nenhum `title`, para o leitor de tela não ler a mesma informação duas vezes ([gov.br DS](https://www.gov.br/ds/components/button)).

**Garanta contraste em todos os estados.** Texto do botão com pelo menos 4,5:1 e ícones e bordas com 3:1 contra o fundo (WCAG 2.2, 1.4.3 e 1.4.11).

**Respeite o alvo de toque.** Em toque, a área de ação mínima é `--c-touch` ([gov.br DS](https://www.gov.br/ds/components/button), [HIG](https://developer.apple.com/design/human-interface-guidelines/buttons)); um circular de 32px estende a área de ação além da superfície visível.

## Tokens usados

| Token                                               | Uso                                                    |
|-----------------------------------------------------|--------------------------------------------------------|
| `--t-brand`, `--t-brand-hover`, `--t-brand-pressed` | Fundo do primário em repouso, hover e pressionado      |
| `--t-on-brand`                                      | Texto do primário                                      |
| `--t-surface-raised`, `--t-border-control`          | Fundo e borda do secundário (3:1)                      |
| `--o-hover`, `--o-pressed`                          | Camada de estado do secundário, do sutil e do ativado  |
| `--t-danger`                                        | Fundo do botão de perigo                               |
| `--t-fg-disabled`                                   | Texto do botão desabilitado                            |
| `--c-h-sm`, `--c-h-md`, `--c-h-lg`, `--d-control`   | Alturas e lado do circular por densidade               |
| `--icon-md`                                         | Ícone                                                  |
| `--sp-200`, `--sp-400`, `--d-pad-x`                 | Espaço entre ícone e rótulo; margem interna horizontal |
| `--r-md`                                            | Raio do botão padrão                                   |
| `--t-focus`                                         | Anel de foco                                           |

## Considerações por plataforma

### Web desktop

Mostre um tooltip com o nome da ação em botões circulares, no hover e no foco. Use a densidade alta em barras de ferramentas e tabelas densas, mantendo o padrão nos formulários.

### Web móvel

Use densidade baixa. Na classe Compacta, use `.tr-btn--block-compact` quando houver uma ação central na tela ([DKFDS](https://designsystem.dk/komponenter/knapper/), [gov.br DS](https://www.gov.br/ds/components/button)); a ação de conversão ocupa a largura disponível ([gov.br DS](https://www.gov.br/ds/components/magicbutton)). Empilhe os botões com a principal em cima.

### Tablets e dobráveis

Mantenha as ações perto da área em que a pessoa segura o aparelho e perto do conteúdo que elas afetam. Em dobráveis parcialmente dobrados, mostre o conteúdo na metade de cima e os controles na metade de baixo, e evite botões perto da dobra ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Links
- Menus
- Barra de ferramentas
- Diálogos
- Densidade
- Estados de interação

### Referências

- [Button (Botão)](https://www.gov.br/ds/components/button) gov.br DS
- [Magic Button (Botão Destaque)](https://www.gov.br/ds/components/magicbutton) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons) Apple HIG
- [Button: usage](https://fluent2.microsoft.design/components/web/react/core/button/usage) Fluent 2
- [Button](https://design-system.service.gov.uk/components/button/) GOV.UK Design System
- [Knapper](https://designsystem.dk/komponenter/knapper/) DKFDS
- [Button](https://hds.hel.fi/components/button) Helsinki Design System
- [Button](https://vercel.com/geist/button) Geist
- [Split Button](https://vercel.com/geist/split-button) Geist
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                   |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o botão circular em três densidades, o comportamento de alternância, o bloco por classe de janela, a regra de uma ação de conversão por tela, a ordem D4, a caixa de frase D1 e a nova regra de desabilitado. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                            |
