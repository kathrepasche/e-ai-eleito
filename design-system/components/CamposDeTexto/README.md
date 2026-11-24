# CamposDeTexto

Um campo de texto recebe uma informação curta, de uma linha, digitada pela pessoa.

Use o campo de texto para pedir nomes, e-mails, códigos, telefones, valores e outras respostas que cabem numa linha. O Trama entrega o campo sempre dentro de um `.tr-field`, que reúne rótulo, dica, mensagem e o próprio controle. Essa composição é a mesma em todos os controles de formulário do sistema.

**Quando usar.** Quando a resposta é livre e curta, e quando é mais fácil digitar do que escolher, por exemplo para colar uma informação copiada de outro lugar ([DKFDS](https://designsystem.dk/komponenter/inputfelter/)). Também serve para pesquisar por palavra-chave ([gov.br](https://www.gov.br/ds/components/input)).

**Quando não usar.** Para respostas de várias linhas, use a área de texto. Para escolher entre valores conhecidos, use radio, select ou combobox. Para datas, use a entrada de data. Para a pesquisa principal de uma página, use o campo de pesquisa.

## Anatomia

1.  **Rótulo** (`.tr-label`): sempre presente e visível, acima do controle.
2.  **Botão de ajuda** (opcional): na linha do rótulo, para complementos que não são requisitos do campo ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Veja Oferecer ajuda.
3.  **Dica** (`.tr-hint`, opcional): uma frase curta entre o rótulo e o controle, ligada por `aria-describedby`.
4.  **Mensagem** (condicional): erro (`.tr-error-msg`), sucesso, alerta ou informativa (`.tr-field-msg--success`, `--warning`, `--info`), entre a dica e o controle. Os quatro objetivos vêm do gov.br ([gov.br](https://www.gov.br/ds/components/input)).
5.  **Controle** (`.tr-input`): altura `--d-control`, borda `--t-border-control` e raio `--r-md`.
6.  **Ícone ilustrativo** (opcional): no início do controle, só reforça o tipo de dado e não recebe clique ([gov.br](https://www.gov.br/ds/components/input)).
7.  **Prefixo e sufixo** (`.tr-affix` dentro de `.tr-input-wrap`, opcionais): moeda ou unidade.
8.  **Ação interna** (opcional): botão no fim do controle, como “Mostrar senha” ou Pesquisar. Use `.tr-input-action` com ícone ou, quando o ícone não basta, um botão só com texto ([gov.br](https://www.gov.br/ds/components/input)).

## Tipos

| Tipo     | Uso                                                                                                                        | Marcação                                               |
|----------|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| Texto    | Nomes, endereços, códigos alfanuméricos                                                                                    | `type="text"`                                          |
| E-mail   | Endereço de e-mail                                                                                                         | `type="email"`, `autocomplete="email"`                 |
| Telefone | Números de telefone                                                                                                        | `type="tel"`, `autocomplete="tel"`                     |
| Número   | CPF, CEP, quantidade, valores                                                                                              | `type="text"` com `inputmode="numeric"` ou `"decimal"` |
| Senha    | Criar ou digitar senha                                                                                                     | `type="password"` com botão “Mostrar senha”            |
| Destaque | Pesquisa principal de uma página, quando o campo precisa chamar atenção ([gov.br](https://www.gov.br/ds/components/input)) | `.tr-input--feature`                                   |

**Senha.** Siga a regra do Trama: mínimo de 8 caracteres, sem máximo, colar permitido, botão “Mostrar senha” e nenhum campo de confirmação, porque o botão resolve a conferência ([GOV.UK](https://design-system.service.gov.uk/components/password-input/)). Ao criar a senha, mostre um medidor com texto (Fraca, Média, Forte) e dicas para fortalecê-la ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Use `autocomplete="new-password"` ao criar e `current-password` ao entrar ([HDS](https://hds.hel.fi/components/password-input)).

**Somente leitura.** Use `readonly` para um valor que veio de outra fonte e não pode ser alterado nesta tela. Ele recebe foco e permite copiar ([HDS](https://hds.hel.fi/components/text-input)).

## Boas práticas

**Dê a todo campo um rótulo visível, acima do controle.** Frase curta, de até três palavras, em caixa de frase e sem dois-pontos ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy); [GOV.UK](https://design-system.service.gov.uk/components/text-input/)). Rótulos acima não ocupam espaço horizontal e funcionam igual no celular ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)).

**Ponha formato e exemplo na dica, nunca só no placeholder.** O placeholder some ao digitar, nem todo leitor de tela o anuncia e o estilo padrão dos navegadores costuma falhar no contraste do critério WCAG 2.2, 1.4.3 ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)). O Trama usa placeholder só no campo destaque de pesquisa, como exemplo redundante, sem itálico e em `--t-fg-3`.

**Ajuste a largura ao tamanho da resposta.** Errar é mais provável quando a pessoa não vê o que digitou ([gov.br](https://www.gov.br/ds/components/input)), e campos longos demais sugerem que a pergunta foi mal entendida ([DKFDS](https://designsystem.dk/komponenter/inputfelter/)). A largura não muda com o texto digitado ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). Quando falta espaço, o campo desce para a linha de baixo em vez de encolher ([gov.br](https://www.gov.br/ds/components/input)).

**Escolha a densidade pelo contexto.** A padrão serve à maioria dos formulários. A alta (`data-density="alta"`) só com mouse ou trackpad, dentro de tabelas, barras de ferramentas e cabeçalhos ([gov.br](https://www.gov.br/ds/components/input)). A baixa é obrigatória em toque e na classe Compacta, onde o campo ocupa a largura toda ([gov.br](https://www.gov.br/ds/components/input)). Use a mesma densidade em campos vizinhos ([gov.br](https://www.gov.br/ds/padroes/design/densidade)). Veja Densidade.

**Aceite o dado no formato em que a pessoa escreve.** Aceite espaços, pontos, hífens e barras, normalize no sistema e mostre o formato na dica. Nunca bloqueie caracteres durante a digitação. Ao sair do campo, você pode formatar o valor exibido, como “123.456.789-09”; a máscara que impede digitar, colar ou apagar é proibida. Se a pessoa digitar “R\$” num campo que já tem o prefixo, aceite sem erro ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)). Não divida telefone, CPF ou protocolo em várias caixas ([gov.br](https://www.gov.br/ds/components/input)).

**Peça números com `inputmode`, sem `type="number"`.** Esse tipo pode mudar o valor quando a pessoa rola a página e não explica o erro quando ela digita outro caractere; o GOV.UK chegou a isso em pesquisa ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)). Para valores negativos, use `type="text"` sem `inputmode`.

**Não limite o comprimento com `maxlength`.** O atributo corta o texto colado sem avisar. Informe o limite na dica e mostre erro só se o valor normalizado passar dele ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)).

**Use `autocomplete` e permita colar.** Nome, e-mail, telefone e CEP preenchidos pelo navegador atendem ao critério WCAG 2.2, 1.3.5. Nunca bloqueie colar, nem em senhas ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)). Desligue o corretor (`spellcheck="false"`) em nomes, e-mails e documentos.

**Faça** rótulo visível, exemplo na dica e largura próxima ao tamanho da resposta.

**Não faça** placeholder como rótulo: a instrução some na primeira tecla.

### Estados

| Estado          | Aparência e uso                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Padrão          | Borda de 1px `--t-border-control` sobre `--t-surface-raised`                                                                                                               |
| Hover           | Borda `--t-fg-2` e cursor de texto. Com o campo em foco, o hover não muda a superfície ([gov.br](https://www.gov.br/ds/components/input))                                  |
| Foco            | Anel de 2px `--t-focus` afastado 2px, em `:focus-visible`. O campo não tem estado pressionado: o clique já leva ao foco ([gov.br](https://www.gov.br/ds/components/input)) |
| Erro            | `aria-invalid="true"`, borda de 2px `--t-danger` e `.tr-error-msg`                                                                                                         |
| Sucesso         | `data-state="success"`, borda de 2px `--t-success` e `.tr-field-msg--success`. Use quando o sistema confirmou algo que a pessoa não podia conferir sozinha, como um código |
| Alerta          | `data-state="warning"`, borda `--t-warning` e `.tr-field-msg--warning`. O valor é aceito, mas merece atenção                                                               |
| Informativo     | `.tr-field-msg--info`, sem mudar a borda. Use no lugar da dica quando a informação precisa de mais ênfase ([gov.br](https://www.gov.br/ds/components/input))               |
| Somente leitura | Texto em `--t-fg-1`, recebe foco e permite copiar                                                                                                                          |
| Desabilitado    | Fundo `--t-surface-2`, texto `--t-fg-disabled`. Só quando a pessoa pode habilitar o campo por uma ação dela, com o motivo escrito ao lado; caso contrário, retire o campo  |

**Valide ao sair do campo e ao enviar.** Verifique o formato quando o foco deixa o campo, sem interromper a digitação a cada tecla ([Geist](https://vercel.com/geist/input)). Ao enviar, mostre também o resumo de erros. Veja Validação e mensagens de erro.

> **Divergência entre referências** *Placeholder:* o gov.br admite placeholder com exemplos e formatos, em itálico; GOV.UK e DKFDS o evitam. Pelo critério de acessibilidade, o Trama leva formatos para a dica e usa placeholder só como exemplo redundante na pesquisa, sem itálico. *Posição da dica e da mensagem:* o gov.br as coloca abaixo do campo; GOV.UK e DKFDS, acima. Pelo critério de acessibilidade, o Trama mantém acima: a instrução é lida antes do campo e não fica escondida pelo teclado virtual ou pela lista de sugestões. *Rótulo lateral:* a página de input do gov.br permite o rótulo à esquerda; a de microcopy do gov.br e o GOV.UK pedem o rótulo acima. Por convergência, o Trama usa só o rótulo acima. *Máscara:* o gov.br recomenda máscara dinâmica; o GOV.UK pede para não restringir a digitação. O Trama aceita qualquer formato e formata ao sair do campo (regra de formatos de dado). *Retorno imediato:* o gov.br pede marcar sucesso ou erro assim que a pessoa preenche; Geist e HIG validam ao sair do campo. Por convergência, o Trama valida ao sair e reserva o sucesso para verificações do sistema. *Foco inicial:* o gov.br põe o foco no primeiro campo obrigatório; o Trama põe o foco no título da página nova ou da etapa.

## Conteúdo

**Rótulos.** Substantivos ou frases curtas: “Nome completo”, “E-mail”, “CEP”. Escreva no positivo ([gov.br](https://www.gov.br/ds/padroes/writing/microcopy)). Quando a página faz uma única pergunta, o rótulo pode ser o título da página e passar de três palavras ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)).

**Dicas.** Uma frase curta, sem ponto final e sem links, porque leitores de tela leem a dica inteira e não avisam que um trecho é link ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)).

**Afixos.** Repita a informação no rótulo, porque leitores de tela não leem o afixo: “Valor do aluguel, em reais” com o prefixo “R\$” ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)).

**Obrigatório e opcional.** Diga no início do formulário que todos os campos são obrigatórios e marque as exceções com “(opcional)” no rótulo. Se a maioria for opcional, marque os obrigatórios com “(obrigatório)”, nunca os dois tipos juntos ([gov.br](https://www.gov.br/ds/padroes/design/formulario)). O Trama não usa asterisco.

**Mensagens.** Erros dizem o que fazer, sem culpar a pessoa. Sucesso diz o que mudou, sem “com sucesso”: “Código confirmado”.

| Situação             | Modelo                                                   |
|----------------------|----------------------------------------------------------|
| Vazio                | Digite seu nome completo                                 |
| Longo demais         | Endereço deve ter no máximo 120 caracteres               |
| Caractere não aceito | Nome deve conter só letras, espaços, hífens e apóstrofos |
| Fora do formato      | Digite um CPF com 11 números, como 123.456.789-09        |
| Fora do intervalo    | Horas por semana deve ser entre 16 e 44                  |

Os modelos seguem a estrutura do GOV.UK para cada tipo de erro ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)). Em telas de entrada na conta, não revele se o erro está no usuário ou na senha ([GOV.UK](https://design-system.service.gov.uk/components/password-input/)).

## Acessibilidade

- Associe rótulo e controle com `<label for>` e use o `type` que corresponde ao dado ([gov.br](https://www.gov.br/ds/components/input)). Ligue dica e mensagem com `aria-describedby`, mensagem primeiro.
- Comece cada mensagem com um prefixo oculto (“Erro:”, “Sucesso:”, “Alerta:”), para que a cor da borda não seja o único sinal (WCAG 2.2, 1.4.1).
- Siga a ordem de tabulação: botão de ajuda do rótulo, campo e, por fim, as ações internas. Cada ação interna recebe foco com Tab e é acionada com Espaço ou Enter ([gov.br](https://www.gov.br/ds/components/input)).
- Ao receber foco, o campo aceita digitação na hora. Não intercepte Ctrl com setas (Option com setas no Mac), que movem o cursor entre palavras ([gov.br](https://www.gov.br/ds/components/input)).
- A ação interna tem 32px visíveis; com toque, estenda a área de ação até `--c-touch` além da superfície visível.
- Use `required` no controle obrigatório e `autocomplete` com o propósito correto (WCAG 2.2, 1.3.5).
- A borda `--t-border-control` atende ao contraste de 3:1 para componentes (WCAG 2.2, 1.4.11).

## Tokens usados

| Elemento                     | Token                                                                                |
|------------------------------|--------------------------------------------------------------------------------------|
| Altura                       | `--d-control`: `--c-h-sm` (alta), `--c-h-md` (padrão), `--c-h-lg` (baixa e destaque) |
| Preenchimento horizontal     | `--sp-300`                                                                           |
| Borda e raio                 | `--stroke-thin`, `--t-border-control`, `--r-md`; destaque `--r-lg`                   |
| Texto digitado               | Body 16/24, `--t-fg-1`; destaque 18px                                                |
| Dica, afixo e ícone          | `--t-fg-3`; ícone `--icon-sm`                                                        |
| Mensagens e bordas de estado | `--t-danger`, `--t-success`, `--t-warning`, `--t-info`, `--stroke-thick`             |
| Espaço entre campos          | `--f-gap-field`; entre rótulo, dica e controle, `--sp-100`                           |
| Foco                         | `--t-focus`, `--stroke-thick`                                                        |
| Desabilitado                 | `--t-surface-2`, `--t-border-subtle`, `--t-fg-disabled`                              |

## Considerações por plataforma

### Web desktop

Nas classes Expandida em diante, campos de um mesmo grupo podem ficar lado a lado quando se complementam, com larguras fixas pelo tipo de dado ([gov.br](https://www.gov.br/ds/components/input)). Não estique o campo até a borda da coluna. Em tabelas e cabeçalhos, use densidade alta.

### Web móvel

Na classe Compacta, o campo ocupa a largura toda e usa densidade baixa ([gov.br](https://www.gov.br/ds/components/input)). Escolha `type` e `inputmode` para abrir o teclado adequado e use `enterkeyhint` para rotular a tecla Enter ([Apple](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards)). Mantenha o texto do controle em 16px.

### Tablets e dobráveis

Com o teclado virtual aberto, a área visível diminui. Role o campo com foco para cima do teclado e mantenha a mensagem visível. Em toque, use densidade baixa mesmo em janelas Expandidas.

## Recursos

### Relacionados

- Área de texto
- Campo numérico e stepper
- Combobox
- Campo de pesquisa
- Entrada de dados
- Validação e mensagens de erro
- Densidade

### Referências

- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Formulário](https://www.gov.br/ds/padroes/design/formulario) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) Apple HIG
- [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards) Apple HIG
- [Text input](https://design-system.service.gov.uk/components/text-input/) GOV.UK Design System
- [Password input](https://design-system.service.gov.uk/components/password-input/) GOV.UK Design System
- [Inputfelter](https://designsystem.dk/komponenter/inputfelter/) Det Fælles Designsystem
- [TextInput](https://hds.hel.fi/components/text-input) Helsinki Design System
- [PasswordInput](https://hds.hel.fi/components/password-input) Helsinki Design System
- [Field](https://fluent2.microsoft.design/components/web/react/core/field/usage) Fluent 2
- [Input](https://vercel.com/geist/input) Geist

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                 |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta densidades, campo destaque, ícone e ação interna, estados de sucesso, alerta e informativo, ordem de tabulação e a regra de formatos, e retira o asterisco. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                          |
