# AreaDeTexto

Uma área de texto recebe respostas livres que ocupam mais de uma linha, como descrições, justificativas e comentários.

A área de texto do Trama (`.tr-textarea`) segue a mesma composição do campo de texto: rótulo, dica e mensagem acima do controle, dentro de um `.tr-field`. Os estados também são os mesmos do campo de texto, como prevê o gov.br ([gov.br](https://www.gov.br/ds/components/textarea)). Quando há contagem, um contador (`.tr-count`) aparece abaixo do controle.

**Quando usar.** Para texto corrido, sem estrutura, que exige várias linhas e não pode ser escolhido de uma lista, como o relato de uma situação ([DKFDS](https://designsystem.dk/komponenter/tekstomraade/); [gov.br](https://www.gov.br/ds/components/textarea)).

**Quando não usar.** Para respostas de uma linha, como nome ou telefone, use o campo de texto ([GOV.UK](https://design-system.service.gov.uk/components/textarea/)). Para informação estruturada, use campos separados ou controles de escolha ([DKFDS](https://designsystem.dk/komponenter/tekstomraade/)). Perguntas abertas são difíceis de responder: quando der, divida a pergunta em perguntas simples, com radios para as opções conhecidas ([GOV.UK](https://design-system.service.gov.uk/components/textarea/)).

## Anatomia

1.  **Rótulo** (`.tr-label`): sempre visível, acima do controle.
2.  **Dica** (`.tr-hint`, opcional): uma frase curta sobre o que escrever.
3.  **Mensagem** (condicional): erro, sucesso, alerta ou informativa, acima do controle, como no campo de texto.
4.  **Controle** (`.tr-textarea`): altura definida por `rows`, mínimo de 96px.
5.  **Alça de redimensionamento**: elemento nativo do navegador, no canto inferior ([gov.br](https://www.gov.br/ds/components/textarea)). O Trama permite redimensionar só na vertical.
6.  **Contador** (`.tr-count`, opcional): abaixo do controle, com a quantidade restante ou digitada ([HDS](https://hds.hel.fi/components/text-area)).

O contador fica abaixo para ficar separado da dica e do erro, e para ser visto de novo quando a pessoa rola até o fim do texto para enviar ([GOV.UK](https://design-system.service.gov.uk/components/character-count/)).

## Tipos

| Tipo                 | Quando usar                                                                                                                                                                |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simples              | Padrão. Sem contagem visível.                                                                                                                                              |
| Contador com limite  | Quando há motivo legal, técnico ou de pesquisa para limitar o tamanho. Mostra quanto resta ([gov.br](https://www.gov.br/ds/components/textarea)).                          |
| Contador sem limite  | Quando a quantidade escrita é só informação, como num relatório com tamanho recomendado. Mostra quanto foi digitado ([gov.br](https://www.gov.br/ds/components/textarea)). |
| Contador de palavras | Quando a resposta é longa e o limite faz mais sentido em palavras ([GOV.UK](https://design-system.service.gov.uk/components/character-count/)).                            |
| Contador com limiar  | Quando o limite técnico está muito acima do uso comum: o contador só aparece perto do limite ([GOV.UK](https://design-system.service.gov.uk/components/character-count/)). |

## Boas práticas

**Dimensione a altura pela resposta esperada.** Defina a altura com `rows`, proporcional ao texto que se espera ([GOV.UK](https://design-system.service.gov.uk/components/textarea/); [gov.br](https://www.gov.br/ds/components/textarea)). Não a deixe tão pequena que a pessoa precise rolar para revisar um texto comum, e nunca crie rolagem horizontal: o texto quebra por palavra ([DKFDS](https://designsystem.dk/komponenter/tekstomraade/)). Quando o texto passa da altura, use a barra de rolagem nativa do navegador ([gov.br](https://www.gov.br/ds/components/textarea)).

**Permita redimensionar só na vertical.** O `.tr-textarea` usa `resize: vertical`, para que a pessoa veja mais texto sem quebrar a coluna. Não deixe a área crescer a ponto de empurrar as ações principais para fora da tela ([Geist](https://vercel.com/geist/textarea)). Na classe Compacta, o tamanho é fixo e a alça some, porque falta espaço para arrastar ([gov.br](https://www.gov.br/ds/components/textarea)).

**Escolha a densidade pelo contexto.** A densidade muda o preenchimento interno: `--sp-100` por `--sp-200` na alta, `--sp-200` por `--sp-300` na padrão e `--sp-300` por `--sp-400` na baixa. Use a mesma densidade dos campos vizinhos ([gov.br](https://www.gov.br/ds/padroes/design/densidade)), a baixa em toque e a alta só com mouse, em painéis de ferramentas.

**Limite o tamanho só com bom motivo.** Teste o serviço sem contador primeiro. Use o limite quando houver evidência de que as pessoas escrevem mais do que o necessário ou uma razão legal ou técnica; se as pessoas batem no limite com frequência, aumente o limite ([GOV.UK](https://design-system.service.gov.uk/components/character-count/)).

**Nunca interrompa a digitação no limite.** Deixe a pessoa escrever ou colar o texto completo e editar depois ([GOV.UK](https://design-system.service.gov.uk/components/character-count/)). Mostre o excesso abaixo do campo enquanto ela digita ([DKFDS](https://designsystem.dk/komponenter/tekstomraade/)). Por isso o Trama não usa `maxlength` em áreas de texto.

**Mostre o limite antes de a pessoa começar.** O contador exibe o total desde o início, “Você pode digitar até 500 caracteres”, e passa a mostrar o restante durante a digitação ([gov.br](https://www.gov.br/ds/components/textarea)). Sem JavaScript, a frase estática continua informando o limite ([GOV.UK](https://design-system.service.gov.uk/components/character-count/)).

**Permita copiar e colar, e remova espaços vazios antes de validar.** As pessoas trazem textos prontos de outros documentos ([GOV.UK](https://design-system.service.gov.uk/components/textarea/)). Uma área com só quebras de linha não passa como preenchida ([Geist](https://vercel.com/geist/textarea)).

**Faça** altura compatível com a resposta e limite informado desde o início.

**Não faça** área de uma linha com corte silencioso no limite.

### Estados e comportamento

| Estado               | Aparência e comportamento                                                                                                                                  |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Padrão, hover e foco | Iguais aos do campo de texto; foco com anel `--t-focus` em `:focus-visible`                                                                                |
| Dentro do limite     | Contador em `--t-fg-3`: “Restam 120 caracteres”                                                                                                            |
| Acima do limite      | Contador em `--t-danger` e borda de erro: “31 caracteres acima do limite”                                                                                  |
| Erro ao enviar       | Mensagem acima do controle e contador abaixo, ao mesmo tempo ([GOV.UK](https://design-system.service.gov.uk/components/character-count/))                  |
| Sucesso e alerta     | `data-state="success"` ou `"warning"` com `.tr-field-msg--success` ou `--warning`, como no campo de texto                                                  |
| Informativo          | `.tr-field-msg--info`, quando a orientação precisa de mais ênfase que a dica ([gov.br](https://www.gov.br/ds/components/input))                            |
| Desabilitado         | Fundo `--t-surface-2`, texto `--t-fg-disabled`. Só quando a pessoa pode habilitá-la por uma ação dela, com o motivo ao lado; caso contrário, retire a área |

Mostre a borda vermelha só enquanto o texto estiver acima do limite. Se a pessoa corrigir, a borda some, mesmo que a mensagem do envio anterior continue até o próximo envio ([GOV.UK](https://design-system.service.gov.uk/components/character-count/)). Valide o conteúdo ao sair do campo e ao enviar ([Geist](https://vercel.com/geist/textarea)).

> **Divergência entre referências** *Bloqueio no limite:* o gov.br bloqueia a digitação quando o limite é atingido; GOV.UK e DKFDS deixam passar do limite e mostram o excesso. O GOV.UK testou o componente com 17 pessoas, incluindo pessoas com baixa familiaridade digital e com deficiência. Pelo critério de evidência, o Trama não bloqueia. *Redimensionamento:* o gov.br permite redimensionar na horizontal e na vertical; o Geist pede que a área não quebre o layout. Por acessibilidade (o conteúdo precisa caber na coluna sem rolagem horizontal, WCAG 2.2, 1.4.10), o Trama permite só a vertical. Na classe Compacta, todos fixam o tamanho. *Posição da dica e da mensagem:* o gov.br as coloca abaixo; o Trama as mantém acima, com o contador abaixo, pelos motivos registrados em Campos de texto.

## Conteúdo

**Rótulo.** Curto, direto, em caixa de frase e sem dois-pontos ([GOV.UK](https://design-system.service.gov.uk/components/textarea/)). Numa página de uma pergunta só, o rótulo pode ser o título.

**Dica.** Diga o que a resposta deve conter: “Conte o que aconteceu, quando e onde”. Não use placeholder para isso, porque ele desaparece ao digitar ([Fluent](https://fluent2.microsoft.design/components/web/react/core/textarea/usage)).

**Contador.** Escreva o número em frase completa e neutra: “Restam 42 caracteres”, “Resta 1 caractere”, “12 caracteres acima do limite”, “120 caracteres digitados”.

**Erros.**

| Situação           | Modelo                                    |
|--------------------|-------------------------------------------|
| Vazio              | Descreva o problema                       |
| Longo demais       | Resumo deve ter no máximo 200 caracteres  |
| Curto demais       | Resumo deve ter pelo menos 10 caracteres  |
| Entre dois limites | Resumo deve ter entre 10 e 200 caracteres |

Os modelos seguem a estrutura do GOV.UK para áreas de texto ([GOV.UK](https://design-system.service.gov.uk/components/textarea/)).

## Acessibilidade

- Use `<textarea>` com `<label for>`. Ligue dica, mensagem e contador ao controle com `aria-describedby` ([gov.br](https://www.gov.br/ds/components/textarea)).
- Siga a ordem de tabulação: botão de ajuda do rótulo e depois a área. Ao receber foco, a área aceita digitação na hora, e Ctrl com setas (Option no Mac) move o cursor entre palavras ([gov.br](https://www.gov.br/ds/components/textarea)).
- Atualize o contador visível a cada tecla, mas anuncie a contagem ao leitor de tela só quando a pessoa para de digitar, numa região `aria-live="polite"` separada ([GOV.UK](https://design-system.service.gov.uk/components/character-count/)). Mantenha uma mensagem oculta com o limite total ([DKFDS](https://designsystem.dk/komponenter/tekstomraade/)).
- Contadores podem contar emojis e alguns caracteres não latinos como mais de um ([GOV.UK](https://design-system.service.gov.uk/components/character-count/)). Use a mesma regra no cliente e no servidor.
- Informe erro, sucesso e alerta em texto com prefixo oculto, nunca só pela cor (WCAG 2.2, 1.4.1).
- Teste com zoom de 200% (WCAG 2.2, 1.4.4); o texto continua legível com os ajustes de acessibilidade ativados ([Apple](https://developer.apple.com/design/human-interface-guidelines/text-views)).

## Tokens usados

| Elemento            | Token                                                                    |
|---------------------|--------------------------------------------------------------------------|
| Preenchimento       | Padrão `--sp-200` por `--sp-300`; alta e baixa conforme a densidade      |
| Borda e raio        | `--stroke-thin`, `--t-border-control`, `--r-md`                          |
| Texto               | Body 16/24, `--t-fg-1`                                                   |
| Contador            | 13/18, `--t-fg-3`; acima do limite `--t-danger`                          |
| Estados             | `--t-danger`, `--t-success`, `--t-warning`, `--t-info`, `--stroke-thick` |
| Foco                | `--t-focus`                                                              |
| Espaço entre partes | `--sp-100`; entre campos `--f-gap-field`                                 |

## Considerações por plataforma

### Web desktop

A alça de redimensionamento fica visível no canto inferior. Ajuste a largura à resposta esperada e não ultrapasse a largura de leitura confortável da coluna; ao reduzir a janela, a área pode ocupar a largura toda ou encolher junto com a coluna ([gov.br](https://www.gov.br/ds/components/textarea)).

### Web móvel

Na classe Compacta, a área ocupa a largura toda, com altura generosa e tamanho fixo ([gov.br](https://www.gov.br/ds/components/textarea)). Ative o corretor ortográfico (`spellcheck="true"`) em textos corridos, porque os navegadores não o ativam de forma consistente ([GOV.UK](https://design-system.service.gov.uk/components/text-input/)). Deixe o botão de envio logo abaixo do contador.

### Tablets e dobráveis

Com teclado virtual aberto em orientação paisagem, sobra pouca altura. Mantenha o contador visível acima do teclado, rolando a área de texto quando ela recebe foco. Em toque, use densidade baixa.

## Recursos

### Relacionados

- Campos de texto
- Validação e mensagens de erro
- Resumo de erros
- Entrada de dados
- Escrita e conteúdo

### Referências

- [Textarea](https://www.gov.br/ds/components/textarea) gov.br DS
- [Input](https://www.gov.br/ds/components/input) gov.br DS
- [Densidade](https://www.gov.br/ds/padroes/design/densidade) gov.br DS
- [Text views](https://developer.apple.com/design/human-interface-guidelines/text-views) Apple HIG
- [Textarea](https://design-system.service.gov.uk/components/textarea/) GOV.UK Design System
- [Character count](https://design-system.service.gov.uk/components/character-count/) GOV.UK Design System
- [Text input](https://design-system.service.gov.uk/components/text-input/) GOV.UK Design System
- [Tekstområde](https://designsystem.dk/komponenter/tekstomraade/) Det Fælles Designsystem
- [TextArea](https://hds.hel.fi/components/text-area) Helsinki Design System
- [Textarea](https://fluent2.microsoft.design/components/web/react/core/textarea/usage) Fluent 2
- [Textarea](https://vercel.com/geist/textarea) Geist

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta contador sem limite, densidades, estados de sucesso, alerta e informativo, tamanho fixo na classe Compacta e ordem de tabulação, e reescreve o excesso de caracteres sem culpar a pessoa. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                        |
