# ResumoDeErros

O resumo de erros lista, no topo da página, tudo o que impede a pessoa de avançar e leva direto a cada campo que precisa de correção.

Quando um formulário volta com problemas, a pessoa precisa saber três coisas: que houve erro, quantos são e onde estão. O resumo responde às três de uma vez. Ele recebe o foco assim que a página carrega, é anunciado pelo leitor de tela e traz um link para cada campo com erro. Junto a cada campo, uma mensagem contextual de erro repete o mesmo texto; o gov.br DS chama de contextual a mensagem que se refere a um componente, como a validação de um campo ([gov.br DS](https://www.gov.br/ds/components/message)). As duas peças funcionam juntas: o Trama exige ambas sempre que há erro de validação ([GOV.UK](https://design-system.service.gov.uk/components/error-summary/), [Ontario](https://designsystem.ontario.ca/components/detail/error-messaging.html)).

**Use o resumo de erros** sempre que o envio de um formulário ou de uma etapa falhar na validação, mesmo que haja um único erro ([GOV.UK](https://design-system.service.gov.uk/components/error-summary/), [DKFDS](https://designsystem.dk/komponenter/fejlopsummering/)).

**Não use o resumo de erros** para dizer que a pessoa não tem direito a um serviço, não tem permissão ou esbarrou numa falha do sistema que ela não consegue corrigir. Leve-a a uma página que explique o problema e o que fazer em seguida ([GOV.UK](https://design-system.service.gov.uk/components/error-message/)). Para falhas de carregamento de uma seção, use uma mensagem de erro com a ação de tentar de novo.

## Anatomia

1.  **Contêiner**: borda `--stroke-thicker` em `--t-danger`, fundo `--t-surface-raised`, raio `--r-lg`, preenchimento `--sp-400`.
2.  **Título**: "Há um problema", como `h2` da página (a demonstração usa nível 3 por estar dentro desta documentação).
3.  **Lista de erros**: um link por erro, na ordem em que os campos aparecem, em `--t-danger` e peso 600.
4.  **Mensagens contextuais nos campos**: texto em `--t-danger` entre a dica e o campo, com ícone, prefixo oculto "Erro:", sem botão Fechar, e o campo com borda `--stroke-thick` em `--t-danger` ([gov.br DS](https://www.gov.br/ds/components/message)). A mensagem quebra a linha quando não cabe e nunca é truncada.

## Boas práticas

**Coloque o resumo no topo do conteúdo principal.** Abaixo do breadcrumb ou do link Voltar, acima do título `h1` ([GOV.UK](https://design-system.service.gov.uk/components/error-summary/), [DKFDS](https://designsystem.dk/komponenter/fejlopsummering/)). Num formulário dentro de um drawer ou diálogo, coloque-o no topo do formulário ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)).

**Mova o foco para o resumo.** Ao recarregar a página com erros, o foco vai para o contêiner do resumo, que tem `tabindex="-1"`, e não para o `h1` como numa página nova ([GOV.UK](https://design-system.service.gov.uk/components/error-summary/), [GOV.UK](https://design-system.service.gov.uk/patterns/validation/)). Se a pessoa reenviar com erros restantes, mova o foco de novo ([HDS](https://hds.hel.fi/components/notification)).

**Ligue cada erro ao campo certo.** Para campos únicos, aponte para o campo. Para grupos, como dia, mês e ano, aponte para o primeiro campo com erro, ou para o primeiro do grupo se não souber qual é. Para botões de opção e caixas de seleção, aponte para a primeira opção ([GOV.UK](https://design-system.service.gov.uk/components/error-summary/), [DKFDS](https://designsystem.dk/komponenter/fejlopsummering/)).

**Ao seguir um link, mostre o rótulo junto com o campo.** A rolagem deve parar com o rótulo visível, sem cortá-lo no topo da tela ([DKFDS](https://designsystem.dk/komponenter/fejlopsummering/)).

**Preserve tudo o que a pessoa digitou.** Mostre a página de novo com os campos como estavam, inclusive os que falharam, para que ela veja o erro e corrija sem redigitar ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)).

**Aceite o formato que a pessoa digitou.** Ignore espaços, pontos, hífens e barras em números e códigos, e normalize no sistema. Um erro causado por um caractere invisível ou colado por acidente é difícil de ver e de corrigir ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)). Mostre o formato esperado no texto de ajuda.

**Valide no envio e mantenha o botão sempre ativo.** Não valide quando a pessoa sai de um campo nem enquanto ela digita; espere o clique em Continuar. Validar antes de a pessoa terminar causa problemas, principalmente para quem digita mais devagar ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/)). Nunca desative o botão de envio para impedir o erro: deixe a pessoa enviar e mostre o resumo. Desative a validação nativa do HTML com `novalidate`, cuja aparência e posição variam entre navegadores ([Ontario](https://designsystem.ontario.ca/components/detail/error-messaging.html)).

**Não combine o resumo com outro banner.** Se a página tem erros de validação, mostre só o resumo ([GOV.UK](https://design-system.service.gov.uk/components/notification-banner/)).

**Faça** liste cada erro com o mesmo texto da mensagem do campo e um link para ele.

**Não faça** use mensagens genéricas, sem links e diferentes das que estão nos campos.

> **Divergência entre referências** O gov.br DS recomenda dar retorno visual imediato enquanto a pessoa preenche o campo, marcando-o com a cor de sucesso ou de erro ([gov.br DS](https://www.gov.br/ds/components/input)). O GOV.UK pede validar só no envio e relata que a validação durante o preenchimento causa problemas para quem digita devagar, com base no uso prolongado em serviços como a renovação de passaporte. Pelo critério de evidência, o Trama valida no envio. A exceção é o limite de caracteres de uma área de texto, que avisa durante a digitação para a pessoa não escrever além do limite, como faz o próprio GOV.UK.

### Estados e comportamento

- **Erros corrigidos**: o resumo continua até o próximo envio; não remova itens enquanto a pessoa digita, para que a lista não mude sob o cursor.
- **Novo envio sem erros**: a página avança e o resumo desaparece.
- **Formulário em etapas**: o resumo mostra só os erros da etapa atual. Na página de revisão, ele pode listar erros de etapas anteriores, com links para cada etapa ([DKFDS](https://designsystem.dk/komponenter/trinindikator/)).

## Conteúdo

**Use sempre o título "Há um problema".** O mesmo texto em todo o produto ajuda a reconhecer o componente ([GOV.UK](https://design-system.service.gov.uk/components/error-summary/)).

**Repita a mensagem do campo, palavra por palavra.** As duas mensagens precisam ter a mesma aparência, o mesmo som e o mesmo sentido, e fazer sentido fora de contexto ([GOV.UK](https://design-system.service.gov.uk/components/error-message/), [DKFDS](https://designsystem.dk/komponenter/fejlopsummering/)).

**Diga o que corrigir, com as palavras do rótulo.** Rótulo "Quantas horas você trabalha por semana?", erro "Digite quantas horas você trabalha por semana" ([GOV.UK](https://design-system.service.gov.uk/components/error-message/)). Evite "inválido", "por favor", "desculpe", "Ops", jargão técnico e humor. Não culpe a pessoa, mesmo quando o erro foi dela ([GOV.UK](https://design-system.service.gov.uk/components/error-message/), [Ontario](https://designsystem.ontario.ca/components/detail/error-messaging.html)).

**Seja específico.** "Ocorreu um erro" ou "Selecione uma opção" não ajudam. Diga o que aconteceu e como resolver ([GOV.UK](https://design-system.service.gov.uk/components/error-message/), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)).

## Acessibilidade

- Coloque `role="alert"` num elemento interno do resumo, e não no contêiner raiz. O GOV.UK fez essa mudança porque o leitor JAWS não lia o resumo inteiro com o papel na raiz ([GOV.UK](https://design-system.service.gov.uk/components/error-summary/)).
- Acrescente "Erro: " ao início do `<title>` da página, para que o leitor de tela anuncie o problema primeiro ([GOV.UK](https://design-system.service.gov.uk/patterns/validation/), [Ontario](https://designsystem.ontario.ca/components/detail/error-messaging.html)).
- Cada campo com erro tem `aria-invalid="true"` e `aria-describedby` apontando para a mensagem de erro; a mensagem começa com "Erro:" oculto visualmente ([GOV.UK](https://design-system.service.gov.uk/components/error-message/)).
- O erro é sinalizado por texto, ícone, borda mais grossa e cor, nunca só por cor (WCAG 2.2, 1.4.1 e 3.3.1). A mensagem diz como corrigir (WCAG 2.2, 3.3.3).
- O resumo é anunciado assim que aparece, porque o leitor de tela precisa ler imediatamente o retorno de uma ação da pessoa ([gov.br DS](https://www.gov.br/ds/components/message)). O resumo não some por tempo nem tem botão Fechar.

## Tokens usados

| Elemento                | Token                                |
|-------------------------|--------------------------------------|
| Borda do resumo         | `--stroke-thicker`, `--t-danger`     |
| Fundo                   | `--t-surface-raised`                 |
| Raio e preenchimento    | `--r-lg`, `--sp-400`                 |
| Links de erro           | `--t-danger`                         |
| Mensagem no campo       | `--t-danger`, Caption 13/18 semibold |
| Borda do campo com erro | `--stroke-thick`, `--t-danger`       |
| Foco                    | `--t-focus`                          |

Use `--t-danger` só para erros, para que o vermelho continue significando problema ([DKFDS](https://designsystem.dk/komponenter/fejlopsummering/)).

## Considerações por plataforma

### Web desktop

O resumo acompanha a largura da coluna do formulário. Links funcionam com Enter e levam o foco ao campo. Se a página tem cabeçalho fixo, role de modo que o rótulo não fique escondido sob ele (WCAG 2.2, 2.4.11).

### Web móvel

Como o resumo fica no topo e recebe o foco, a pessoa vê o problema sem rolar. Ao tocar num link, o teclado virtual abre sobre o campo; role a página de modo que o rótulo e o campo fiquem acima do teclado.

### Tablets e dobráveis

Se o formulário ocupa o painel de detalhe de um split view, o resumo fica no topo desse painel. Ao abrir ou fechar um dobrável, preserve os valores digitados e o estado de erro ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Validação e mensagens de erro
- Campos de texto
- Mensagens e banners
- Formulários em etapas e páginas de pergunta
- Escrita e conteúdo

### Referências

- [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) Apple HIG
- [Error summary](https://design-system.service.gov.uk/components/error-summary/) GOV.UK
- [Error message](https://design-system.service.gov.uk/components/error-message/) GOV.UK
- [Recover from validation errors](https://design-system.service.gov.uk/patterns/validation/) GOV.UK
- [Notification banner](https://design-system.service.gov.uk/components/notification-banner/) GOV.UK
- [Message (mensagem contextual)](https://www.gov.br/ds/components/message) gov.br DS
- [Input (acessibilidade)](https://www.gov.br/ds/components/input) gov.br DS
- [Fejlopsummering](https://designsystem.dk/komponenter/fejlopsummering/) DKFDS
- [Trinindikator](https://designsystem.dk/komponenter/trinindikator/) DKFDS
- [Notification (as error summary)](https://hds.hel.fi/components/notification) Helsinki Design System
- [Error messaging](https://designsystem.ontario.ca/components/detail/error-messaging.html) Ontario Design System
- [Message bar](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage) Fluent 2
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Adota o nome mensagem contextual, acrescenta a aceitação de qualquer formato digitado, proíbe desativar o botão de envio e registra a divergência sobre validação imediata. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                               |
