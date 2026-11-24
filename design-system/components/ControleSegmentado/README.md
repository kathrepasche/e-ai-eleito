# ControleSegmentado

Um controle segmentado é uma fileira de dois ou mais segmentos, cada um funcionando como um botão, para escolher uma entre opções muito relacionadas.

Os segmentos costumam ter a mesma largura e podem conter texto ou ícone ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)). Em relação a um grupo de botões comum, o controle segmentado sinaliza que se trata de uma seleção e tem peso visual menor, adequado a formulários ([Blueprint](https://blueprintjs.com/docs/#core/components/segmented-control)). No Trama, o controle (`.tr-seg`) é uma faixa `--t-surface-2` em que o segmento escolhido aparece elevado, em `--t-surface-raised` com sombra `--e-1`.

O Padrão Digital de Governo não tem um componente de controle segmentado. O padrão dropdown do gov.br pede que escolhas de duas opções fiquem diretamente na interface, e não numa lista suspensa ([gov.br](https://www.gov.br/ds/padroes/design/dropdown)). O Trama aplica ao controle as regras transversais do gov.br: densidades dos botões, área mínima de ação, estados e escrita de rótulos.

**Quando usar.**

- Para alternar entre visualizações do mesmo conteúdo, como lista, grade e calendário, ou código e resultado ([Geist](https://vercel.com/geist/switch)).
- Para escolher um atributo que afeta um objeto ou a tela, como o alinhamento de um texto ou o período de um gráfico ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)).
- Quando é importante manter as opções agrupadas e mostrar claramente qual está ativa ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)).

**Quando não usar.**

- Para navegar entre seções independentes do produto: use a barra de navegação ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)). Para trocar painéis de conteúdo na área principal da página, use abas ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)).
- Com mais de três opções ou rótulos de mais de duas palavras: use abas ou select ([Geist](https://vercel.com/geist/switch)).
- Para ligar ou desligar um único ajuste: use um switch ([Geist](https://vercel.com/geist/switch)).
- Para alternar entre duas ações opostas num mesmo lugar, como Expandir e Recolher: use um único botão com comportamento de alternância, que troca o rótulo ou o ícone a cada clique ([gov.br](https://www.gov.br/ds/components/button)).
- Para respostas de formulário que a pessoa precisa ler com calma: use radios, que acomodam textos longos e dicas.

## Anatomia

1.  **Faixa**: contêiner `--t-surface-2`, raio `--r-lg`, preenchimento de 2px.
2.  **Segmento**: botão com altura definida pela densidade (32px no kit, a densidade alta), texto 14/20 semibold em `--t-fg-2`.
3.  **Segmento selecionado**: fundo `--t-surface-raised`, texto `--t-fg-1`, sombra `--e-1`.
4.  **Rótulo** (opcional): texto que apresenta o controle, ao lado ou acima.

## Tipos

| Tipo          | Uso                                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------|
| Escolha única | Padrão do Trama. Um segmento sempre selecionado.                                                               |
| Só ícones     | Barras de ferramentas densas, com tooltip em cada segmento ([Geist](https://vercel.com/geist/switch)).         |
| Largura total | Telas compactas, com os segmentos dividindo a largura do contêiner ([Geist](https://vercel.com/geist/switch)). |

| Densidade | Altura do segmento | Uso                                                          |
|-----------|--------------------|--------------------------------------------------------------|
| Alta      | 32px (`--c-h-sm`)  | Só com mouse, em barras de ferramentas e painéis de inspeção |
| Padrão    | 40px (`--c-h-md`)  | Cabeçalhos de lista e de gráfico com mouse                   |
| Baixa     | 48px (`--c-h-lg`)  | Obrigatória em toque e na classe Compacta                    |

A HIG também prevê segmentos de escolha múltipla e segmentos que executam ações sem guardar seleção ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)). O Trama não adota esses usos no controle segmentado: para ações agrupadas, use um grupo de botões na barra de ferramentas.

## Boas práticas

**Mantenha um único tipo de comportamento.** Não misture segmentos que guardam seleção com segmentos que executam ações ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)).

**Limite o número de segmentos.** Segmentos demais ficam difíceis de ler e de percorrer. A HIG indica até cinco a sete em interfaces largas e até cerca de cinco no iPhone ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)); o Geist, de duas a três opções ([Geist](https://vercel.com/geist/switch)). O Trama usa de dois a quatro, e no máximo três em janelas compactas.

**Mantenha os segmentos com a mesma largura.** Segmentos iguais dão equilíbrio ao controle ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)). Dimensione cada um pelo rótulo mais longo, para que o realce não mude de tamanho ao trocar de seleção; teste com o texto mais longo do conjunto ([Geist](https://vercel.com/geist/switch)).

**Defina sempre um segmento selecionado.** O controle começa com exatamente uma opção ativa ([Geist](https://vercel.com/geist/switch)), geralmente a visualização padrão.

**Aplique a escolha na hora.** Trocar de segmento muda a visualização imediatamente, sem botão de confirmar. Preserve a escolha da pessoa ao voltar à tela.

**Use a densidade dos botões vizinhos.** As alturas seguem as três densidades dos botões, 32, 40 e 48px ([gov.br](https://www.gov.br/ds/components/button)), e controles próximos usam a mesma densidade ([gov.br](https://www.gov.br/ds/padroes/design/densidade)). Nunca use densidade alta num controle que pede atenção ou que é usado com toque ([gov.br](https://www.gov.br/ds/padroes/design/densidade)).

**Não desabilite segmentos sem saída.** Se a pessoa não pode habilitar o segmento por uma ação dela, retire-o. Se pode, mostre-o desabilitado e explique por quê num tooltip focável.

**Não coloque outros elementos focáveis colados no controle.** Deixe ao menos `--sp-300` de espaço para evitar toques e focos acidentais ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)).

**Faça** rótulos curtos, paralelos e de tamanho parecido.

**Não faça** rótulos desiguais, nem uma ação no meio de opções de seleção.

### Estados

| Estado          | Aparência                                                       |
|-----------------|-----------------------------------------------------------------|
| Não selecionado | Fundo transparente, texto `--t-fg-2`                            |
| Hover           | Camada `--o-hover` na cor do texto do segmento, só com ponteiro |
| Pressionado     | Camada `--o-pressed` enquanto o segmento é acionado             |
| Selecionado     | `--t-surface-raised`, `--t-fg-1`, `--e-1`                       |
| Foco            | Anel de 2px `--t-focus` no segmento                             |
| Desabilitado    | Texto `--t-fg-disabled`, com o motivo num tooltip focável       |

O realce desliza entre segmentos em `--m-normal` com `--m-ease-standard`, e troca sem animação com `prefers-reduced-motion` ou com o controle de animações do produto.

> **Divergência entre referências** *Número de segmentos:* a HIG aceita até cinco a sete segmentos em interfaces largas; o Geist recomenda de dois a três. Não há evidência citada nem diferença de acessibilidade. Pelo critério de contexto brasileiro (rótulos em português costumam ser mais longos), o Trama mantém de dois a quatro segmentos, e no máximo três na classe Compacta. *Altura:* a versão 1.0 fixava 32px; com as densidades, 32px vale só para a densidade alta com mouse.

## Conteúdo

**Use texto ou ícones, sem misturar.** Ícones num segmento e texto em outro deixam o controle desconexo ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)).

**Use substantivos ou frases nominais.** Os rótulos descrevem cada segmento ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)). Mantenha de uma a duas palavras e construção paralela, como “Origem” e “Resultado” ([Geist](https://vercel.com/geist/switch)). Use caixa de frase, evite siglas e não trunque os rótulos ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)).

**Dispense o rótulo quando os segmentos se explicam.** Um controle com texto nos segmentos não precisa de texto introdutório ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)). Com ícones, use um rótulo ou tooltips ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)).

## Acessibilidade

- Agrupe os segmentos com `role="group"` e um nome acessível (`aria-label` ou `aria-labelledby`). Marque o selecionado com `aria-pressed="true"` e os demais com `"false"`, como no `.tr-seg`.
- Quando o controle troca painéis de conteúdo logo abaixo, use o padrão de abas (`role="tablist"`, `role="tab"` e `aria-selected`). Quando ele faz parte de um formulário, use radios nativos estilizados, porque a semântica de radio garante a exclusividade ([Geist](https://vercel.com/geist/switch)).
- Segmentos só com ícone precisam de texto para leitor de tela e de tooltip com o mesmo texto para quem enxerga ([Geist](https://vercel.com/geist/switch)).
- O segmento selecionado se diferencia por fundo, sombra e cor do texto. Confirme que o texto não selecionado em `--t-fg-2` sobre `--t-surface-2` atende a 4,5:1 (WCAG 2.2, 1.4.3).
- A área de ação de cada segmento tem pelo menos 24px com mouse e `--c-touch` em toque, e pode ultrapassar a superfície visível ([gov.br](https://www.gov.br/ds/padroes/design/densidade)). O critério WCAG 2.2, 2.5.8 define o mínimo de 24px.

## Tokens usados

| Elemento                  | Token                                                      |
|---------------------------|------------------------------------------------------------|
| Faixa                     | `--t-surface-2`, `--r-lg`                                  |
| Segmento selecionado      | `--t-surface-raised`, `--e-1`                              |
| Texto                     | `--t-fg-2`; selecionado `--t-fg-1`                         |
| Preenchimento do segmento | `--sp-400` horizontal                                      |
| Altura                    | `--c-h-sm`, `--c-h-md` ou `--c-h-lg`, conforme a densidade |
| Hover e pressionado       | `--o-hover`, `--o-pressed`                                 |
| Movimento                 | `--m-normal`, `--m-ease-standard`                          |
| Foco                      | `--t-focus`                                                |

## Considerações por plataforma

### Web desktop

O controle segmentado funciona bem em barras de ferramentas e painéis de inspeção, para trocar visualizações ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)). Para segmentos com ícone, ofereça tooltip em cada um ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)).

### Web móvel

Use o tipo de largura total, a densidade baixa e no máximo três segmentos curtos. O controle é útil para alternar subtelas muito relacionadas, como evento e lembrete num mesmo formulário ([Apple](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)).

### Tablets e dobráveis

Em janelas expandidas, o controle pode ficar na barra superior do painel que ele afeta. Num dobrável aberto com dois painéis, mantenha o controle no painel cujo conteúdo ele troca.

## Recursos

### Relacionados

- Abas
- Radio
- Switch
- Botões
- Barra de ferramentas
- Densidade

### Referências

- [Button](https://www.gov.br/ds/components/button) gov.br DS
- [Dropdown](https://www.gov.br/ds/padroes/design/dropdown) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) Apple HIG
- [Switch](https://vercel.com/geist/switch) Geist
- [Segmented control](https://blueprintjs.com/docs/#core/components/segmented-control) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo, que não tem controle segmentado. Acrescenta três densidades, área mínima de ação, estados de hover e pressionado por camada, a regra de desabilitado e a alternativa do botão com alternância. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                  |
