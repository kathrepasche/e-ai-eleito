# CampoNumericoEStepper

O campo numérico recebe um número digitado; o stepper acrescenta botões de menos e mais para ajustar o valor em passos.

O stepper é um controle de dois segmentos que aumenta ou diminui um valor incremental. Ele não mostra o valor por conta própria e por isso fica ao lado de um campo que o exibe ([Apple](https://developer.apple.com/design/human-interface-guidelines/steppers)). No Trama, campo e botões formam um único componente: a pessoa pode digitar, usar os botões ou usar as setas do teclado ([Blueprint](https://blueprintjs.com/docs/#core/components/numeric-input)).

O Padrão Digital de Governo não tem um componente de campo numérico nem de stepper. O Trama aplica a ele as regras transversais do gov.br para campos de entrada: densidades, estados de mensagem, ações internas acessíveis por teclado ([gov.br](https://www.gov.br/ds/components/input)), máscara e formato de números ([gov.br](https://www.gov.br/ds/padroes/design/formulario); [gov.br](https://www.gov.br/ds/padroes/writing/microcopy)), conciliadas com a regra de formatos de dado do Trama.

**Quando usar.**

- **Campo numérico sem stepper**: para números exatos e variados, como renda, área ou consumo. Esse é o caso mais comum.
- **Com stepper**: para mudanças pequenas e intuitivas, como quantidade de cópias, número de pessoas, ou de 0 a 100 em passos de 10 ([HDS](https://hds.hel.fi/components/number-input)).

**Quando não usar.** Não use stepper quando se esperam grandes variações de valor ([HDS](https://hds.hel.fi/components/number-input)). Para valores aproximados num intervalo, use o slider. Para números que são identificadores, como CPF, CEP, telefone ou cartão, use um campo de texto com `inputmode="numeric"`: eles não são quantidades e nunca devem ser incrementados. Para datas, use a entrada de data.

## Anatomia

1.  **Rótulo** (`.tr-label`): diz qual número se espera e, quando necessário, a unidade.
2.  **Dica** (`.tr-hint`): limites, formato e exemplo.
3.  **Campo** (`.tr-input`): largura proporcional à quantidade de dígitos esperada.
4.  **Prefixo ou sufixo** (`.tr-affix`, opcional): moeda ou unidade de medida.
5.  **Botões de menos e mais** (stepper, opcional): `.tr-btn--icon` com a altura da densidade (`--d-control`), um de cada lado do campo.

## Tipos

| Tipo              | Marcação                          | Uso                                                                                                                                              |
|-------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Inteiro           | `type="text" inputmode="numeric"` | Quantidades, anos, contagens                                                                                                                     |
| Decimal           | `type="text" inputmode="decimal"` | Dinheiro, medidas ([GOV.UK](https://design-system.service.gov.uk/components/text-input/))                                                        |
| Pode ser negativo | `type="text"` sem `inputmode`     | Saldos, temperaturas; alguns teclados numéricos não têm o sinal de menos ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)) |
| Com stepper       | Campo inteiro mais dois botões    | Mudanças pequenas, com passo lógico ([HDS](https://hds.hel.fi/components/number-input))                                                          |

> **Nota** O Trama não usa `<input type="number">`. Esse tipo pode mudar o valor quando a pessoa rola a página e não explica o erro quando ela digita outro caractere ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)). A HDS adota `type="number"` pelo auxílio a leitores de tela e teclados móveis ([HDS](https://hds.hel.fi/components/number-input)); o Trama obtém o teclado com `inputmode` e o papel `spinbutton` quando há stepper.

## Boas práticas

**Deixe claro qual valor o stepper altera.** Como os botões não exibem número, coloque-os junto do campo e nomeie-os com o valor que mudam ([Apple](https://developer.apple.com/design/human-interface-guidelines/steppers)).

**Permita sempre digitar.** Os botões servem para pequenos ajustes; quando os valores variam muito, a pessoa quer digitar o número exato, como no número de cópias de uma impressão ([Apple](https://developer.apple.com/design/human-interface-guidelines/steppers)). Sempre aceite entrada manual ([HDS](https://hds.hel.fi/components/number-input/accessibility)).

**Ofereça passos maiores pelo teclado.** Seta para cima e para baixo mudam um passo; Shift com seta muda dez passos ([Blueprint](https://blueprintjs.com/docs/#core/components/numeric-input)). Shift com clique nos botões também muda dez vezes o passo, como a HIG sugere para intervalos grandes ([Apple](https://developer.apple.com/design/human-interface-guidelines/steppers)).

**Defina mínimo, máximo e passo, e diga quais são.** Escreva os limites na dica ([HDS](https://hds.hel.fi/components/number-input)). Desabilite o botão de menos no mínimo e o de mais no máximo; a dica com os limites explica por quê. Ao digitar um valor fora do limite, mantenha o que foi digitado e mostre erro ao sair do campo.

**Dê um valor inicial quando fizer sentido e evite placeholder.** A HDS recomenda valor padrão e nenhum placeholder em campos numéricos, porque leitores de tela anunciam placeholders de formas diferentes e é difícil distingui-los do valor real ([HDS](https://hds.hel.fi/components/number-input/accessibility)). Em perguntas cujo valor a pessoa precisa informar, como renda, deixe o campo vazio.

**Mostre a unidade quando ela ajudar.** Use para unidades de medida e moedas; dispense quando for óbvia, como em “Número de pessoas” ([HDS](https://hds.hel.fi/components/number-input)). Repita a unidade no rótulo, porque leitores de tela não leem o afixo ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)).

**Aceite formatos variados e nunca bloqueie caracteres.** Aceite “2350”, “2.350” e “2.350,00”, com ou sem espaços, e normalize no sistema. Não impeça a digitação de letras ou sinais: se o valor não for número, explique no erro. Se a pessoa digitar a unidade ou o símbolo da moeda, aceite sem erro ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)). Não presuma o formato de exibição: separadores decimais e de milhar variam conforme o idioma ([Apple](https://developer.apple.com/design/human-interface-guidelines/text-fields)).

**Formate o valor só quando a pessoa sair do campo.** Reformatar a cada tecla move o cursor e impede digitar vírgulas e sinais. Guarde o texto digitado e converta para número só quando necessário ([Blueprint](https://blueprintjs.com/docs/#core/components/numeric-input)). Ao sair, exiba o número no formato brasileiro, com ponto de milhar e vírgula decimal, como “1.398.672,00” ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)).

**Use a densidade do formulário.** Campo e botões do stepper seguem `--d-control`: densidade alta só com mouse, em tabelas e painéis; baixa em toque e na classe Compacta ([gov.br](https://www.gov.br/ds/components/input)). Mantenha a mesma densidade nos campos vizinhos ([gov.br](https://www.gov.br/ds/padroes/design/densidade)).

**Faça** stepper para valores pequenos que mudam de um em um.

**Não faça** stepper para valores grandes e variados.

### Estados

| Estado                      | Aparência e comportamento                                                                                                                         |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Padrão, hover, foco, erro   | Iguais aos do campo de texto; foco em `:focus-visible`                                                                                            |
| Sucesso e alerta            | `data-state="success"` ou `"warning"` com `.tr-field-msg--success` ou `--warning`, por exemplo para um valor aceito mas muito acima do habitual   |
| No mínimo ou no máximo      | O botão correspondente fica desabilitado, em `--t-fg-disabled`                                                                                    |
| Botão pressionado e mantido | Repete o passo enquanto estiver pressionado                                                                                                       |
| Desabilitado                | Campo e botões desabilitados juntos, só quando a pessoa pode habilitá-los por uma ação dela, com o motivo ao lado; caso contrário, retire o campo |

> **Divergência entre referências** *Bloqueio de caracteres e máscara:* o gov.br sugere tornar indisponível qualquer caractere não numérico em campos de número e recomenda máscara dinâmica; o GOV.UK pede para não restringir a entrada e encontrou em pesquisa problemas no `type="number"`, que rejeita caracteres sem explicar. Pelo critério de evidência, o Trama aceita qualquer caractere, valida ao sair e formata o valor exibido. *Botões do stepper no Tab:* a versão 1.0 permitia tirá-los da ordem de tabulação; o gov.br pede que controles internos sejam alcançáveis com Tab. Pelo critério de acessibilidade (nem todos sabem que as setas ajustam o valor), o Trama os mantém na ordem de tabulação. *Tipo do campo:* a HDS adota `type="number"`; o Trama mantém `type="text"` com `inputmode`, pela mesma evidência do GOV.UK.

## Conteúdo

**Rótulo.** Claro e curto, para que a pessoa entenda na hora qual número informar ([HDS](https://hds.hel.fi/components/number-input)). Escreva a unidade por extenso no rótulo, como “Área construída, em metros quadrados”; o afixo pode usar o símbolo.

**Formato na dica.** Se o número segue um formato, explique na dica ([HDS](https://hds.hel.fi/components/number-input/accessibility)): “Inclua os centavos, como 2.350,00”.

**Erros.**

| Situação              | Modelo                                                             |
|-----------------------|--------------------------------------------------------------------|
| Não é número          | Horas por semana deve ser um número, como 30                       |
| Não é inteiro         | Horas por semana deve ser um número inteiro, como 30               |
| Abaixo do mínimo      | Horas por semana deve ser 16 ou mais                               |
| Acima do máximo       | Horas por semana deve ser 44 ou menos                              |
| Fora do intervalo     | Horas por semana deve ser entre 16 e 44                            |
| Dinheiro sem centavos | A renda mensal deve incluir os centavos, como 2.350,00 ou 1.200,50 |

Os modelos seguem a estrutura do GOV.UK para números; quando o campo aceita decimais, use um decimal no exemplo ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)).

## Acessibilidade

- Com stepper, dê ao campo `role="spinbutton"` com `aria-valuenow`, `aria-valuemin` e `aria-valuemax`, e use `aria-valuetext` quando houver unidade.
- Nomeie os botões de forma descritiva, como “Aumentar número de cópias” e “Diminuir número de cópias” ([HDS](https://hds.hel.fi/components/number-input/accessibility)). Os botões ficam na ordem de tabulação, depois do campo, e são acionados com Espaço ou Enter ([gov.br](https://www.gov.br/ds/components/input)).
- Anuncie o novo valor após cada clique, numa região `aria-live="polite"`, quando o foco permanecer no botão.
- Os botões têm a altura da densidade em uso e área de ação de pelo menos 24px com mouse e `--c-touch` em toque ([gov.br](https://www.gov.br/ds/padroes/design/densidade)).
- Use o prefixo oculto “Erro:” ou “Alerta:” nas mensagens, para que a cor não seja o único sinal (WCAG 2.2, 1.4.1).
- Não use só cor para indicar o limite atingido; o botão também fica desabilitado.

## Tokens usados

| Elemento                    | Token                                                       |
|-----------------------------|-------------------------------------------------------------|
| Campo                       | Tokens de `.tr-input`; texto com números tabulares          |
| Botões                      | `.tr-btn--icon`: `--c-h-md`, `--t-border-control`, `--r-md` |
| Espaço entre botões e campo | `--sp-300`                                                  |
| Afixo                       | `--t-fg-3`, preenchimento `--sp-300`                        |
| Botão no limite             | `--t-surface-2`, `--t-fg-disabled`                          |
| Erro                        | `--t-danger`                                                |
| Foco                        | `--t-focus`                                                 |

## Considerações por plataforma

### Web desktop

Com mouse, em tabelas e painéis, a densidade alta é aceitável. Suporte as setas e Shift com seta no campo, e Shift com clique nos botões ([Blueprint](https://blueprintjs.com/docs/#core/components/numeric-input)). Não altere o valor com a roda do mouse.

### Web móvel

`inputmode="numeric"` e `"decimal"` abrem o teclado numérico ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)). Na classe Compacta, use a densidade baixa: campo e botões com `--c-h-lg`, e espaço entre os botões para evitar toques no botão errado.

### Tablets e dobráveis

Com teclado físico conectado, as setas funcionam como no desktop. Nenhuma outra consideração adicional para tablets e dobráveis.

## Recursos

### Relacionados

- Campos de texto
- Slider
- Validação e mensagens de erro
- Internacionalização e direita para esquerda
- Teclado

### Referências

- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Steppers](https://developer.apple.com/design/human-interface-guidelines/steppers) Apple HIG
- [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) Apple HIG
- [Text input](https://design-system.service.gov.uk/components/text-input/) GOV.UK Design System
- [NumberInput](https://hds.hel.fi/components/number-input) Helsinki Design System
- [NumberInput: acessibilidade](https://hds.hel.fi/components/number-input/accessibility) Helsinki Design System
- [Numeric input](https://blueprintjs.com/docs/#core/components/numeric-input) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                        |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo, que não tem campo numérico próprio. Acrescenta densidades, estados de sucesso e alerta, formato brasileiro de números e unidades por extenso, proíbe bloquear caracteres e coloca os botões do stepper na ordem de tabulação. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                 |
