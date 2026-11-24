# ListaDeResumo

Uma lista de resumo apresenta fatos como pares de chave e valor, com uma ação opcional por linha, para revisar respostas ou mostrar os metadados de um objeto.

Cada linha tem uma **chave**, que nomeia a informação ("Nome"), e um **valor**, que é a informação em si ("Maria Souza") ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)). O uso mais comum é a página de revisão no fim de um formulário, em que cada linha tem um link "Alterar" (veja Revisar respostas e confirmação). Também serve para metadados em páginas de detalhe, como "Última atualização" e "Responsável".

O gov.br não tem um componente de lista de resumo; ele trata a lista de definições (`<dl>`) como estilo tipográfico para exibir termos e explicações ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/tipografia)). O Trama usa esse mesmo elemento como base do componente e aplica a ele as regras brasileiras de formato de dado e de escrita.

## Quando usar

- Para mostrar uma lista de fatos sobre um assunto ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)).
- Para resumir as respostas antes do envio de um formulário ([Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)).
- Para metadados de um item em página de detalhe: região, plano, data de criação ([Geist](https://vercel.com/geist/description)).
- Em recibos e páginas de confirmação ([DKFDS](https://designsystem.dk/komponenter/tables/)).

## Quando não usar

- **Para dados tabulares com vários registros e colunas comparáveis.** Use uma tabela ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/), [DKFDS](https://designsystem.dk/komponenter/tables/)).
- **Para uma lista simples de itens ou tarefas.** Use uma lista ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)).
- **Para texto de ajuda sob um campo.** Use a dica do campo ([Geist](https://vercel.com/geist/description)).
- **Dentro de um acordeão.** A revisão precisa estar visível ([Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)).

## Anatomia

1.  **Título da seção.** Dá estrutura à página, mesmo quando a seção tem uma única linha ([Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)).
2.  **Chave.** Nome ou pergunta, em `<dt>`.
3.  **Valor.** A informação, em `<dd>`.
4.  **Ação de linha (opcional).** Link como "Alterar", em um segundo `<dd>`.
5.  **Divisores.** Linhas acima e abaixo de cada linha, que ligam a ação à informação.

## Tipos

| Tipo           | Uso                                                                                                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Com ações      | Revisão de respostas; cada linha leva de volta à pergunta.                                                                                                                                                        |
| Sem ações      | Metadados somente leitura. Pode dispensar os divisores ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)).                                                                                 |
| Mista          | Algumas linhas com ação e outras sem; mantenha a coluna de ação mesmo vazia, para que os divisores fiquem contínuos ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)).                    |
| Card de resumo | Várias listas que descrevem o mesmo tipo de coisa, como pessoas, cada uma em um card com título e ações que valem para a lista inteira ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)). |

## Boas práticas

**Use duas ou três colunas.** Chave, valor e, se houver, ação ([DKFDS](https://designsystem.dk/komponenter/tables/)).

**Mantenha os divisores quando houver ações.** As linhas mostram a que informação cada ação pertence e ajudam quem usa ampliação de tela ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)).

**Limite a largura.** Em janelas expandidas, a lista ocupa 8 de 12 colunas, para que as ações fiquem perto do conteúdo e não escapem a quem usa ampliação. Use largura total só para respostas longas, como textos de área de texto ([Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)).

**Use a mesma largura em listas da mesma página.** Divida listas longas em seções com títulos ([DKFDS](https://designsystem.dk/komponenter/tables/)).

**Mostre informação faltante com um link para preenchê-la.** Quando falta uma resposta obrigatória, coloque no valor um link para a pergunta, no lugar do "Alterar" ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)).

**Inclua as perguntas opcionais sem resposta.** Escreva "Não informado" ou "Não se aplica" no valor ([Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)).

**Ao voltar para alterar, preencha com o que a pessoa já respondeu.** Depois de salvar, retorne à página de resumo ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)).

**Agrupe ações repetidas.** Se várias linhas levam ao mesmo lugar, use uma única ação no título da seção ou do card. Não coloque mais de 2 ou 3 ações nesse título ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/), [Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)). Ações difíceis de desfazer pedem confirmação.

**Faça** reúna um endereço em uma chave só e reescreva perguntas longas como chaves curtas ([Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)).

**Não faça** repetir as perguntas inteiras e usar "Alterar" sem dizer o que muda.

### Comportamento

- Em janelas compactas, cada linha vira uma pilha: chave, valor e ação, um abaixo do outro.
- Valores longos quebram linha. Nunca trunque respostas em uma página de revisão.
- Mostre os valores normalizados e formatados no padrão brasileiro: CPF com pontos e hífen, CEP com hífen, números com ponto de milhar e vírgula decimal ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)), mesmo que a pessoa tenha digitado sem pontuação. O conteúdo não muda; só a apresentação.
- Escreva datas por extenso ("12 de março de 1988") e unidades por extenso ("30 dias").
- **Densidade.** A lista de resumo usa a densidade padrão ou a baixa. Na baixa, obrigatória no toque, o preenchimento vertical da linha passa de `--sp-300` para `--sp-400`. Não use a densidade alta: a revisão pede leitura atenta.

## Conteúdo

- Escreva chaves como substantivos curtos, de até três palavras, em caixa de frase: "Data de nascimento". O Geist usa substantivos curtos na chave e frase comum no valor ([Geist](https://vercel.com/geist/description)).
- Não termine chaves com dois-pontos. A HIG desaconselha dois-pontos finais em cabeçalhos de coluna ([HIG](https://developer.apple.com/design/human-interface-guidelines/outline-views)).
- Use "Alterar" para ações de linha. Ações de seção dizem o que fazem, com até duas palavras e sem artigo: "Remover dependente", "Alterar endereço" ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)). Para apagar, use "Excluir".
- Depois de salvar uma alteração e voltar ao resumo, confirme o que mudou: "Endereço atualizado", sem "com sucesso" e sem exclamação.
- Não coloque controles na chave. Botões, menus e links ficam no valor ou na coluna de ação ([Geist](https://vercel.com/geist/description)).
- Deixe valores úteis selecionáveis, como números de protocolo ([HIG](https://developer.apple.com/design/human-interface-guidelines/labels)).

> **Divergência entre referências** O gov.br aceita dois-pontos no fim dos rótulos, desde que o padrão seja o mesmo em todo o formulário, e pede rótulos de no máximo três palavras ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). A HIG desaconselha os dois-pontos finais ([HIG](https://developer.apple.com/design/human-interface-guidelines/outline-views)). Sem pesquisa citada de nenhum lado, o Trama não usa dois-pontos: a relação entre chave e valor já vem da estrutura `<dl>` e das colunas. Adota do gov.br o limite de três palavras por chave.

## Acessibilidade

**Use lista de descrição.** `<dl>`, `<dt>` e `<dd>` fazem o leitor de tela anunciar cada par como termo e definição. Só use para informação com chave e pelo menos um valor ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/)). Não envolva a lista em parágrafos que quebrem essa semântica ([Geist](https://vercel.com/geist/description)).

**Dê contexto às ações.** Fora de contexto, "Alterar" não diz o que muda. Acrescente texto oculto com a chave, para que o leitor de tela anuncie "Alterar nome completo" ([GOV.UK](https://design-system.service.gov.uk/components/summary-list/), [Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)). Atende ao WCAG 2.2, 2.4.4.

**Siga a hierarquia de títulos.** O título de cada seção segue o nível da página, sem pular níveis ([Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)).

**Alternativa em tabela.** O DKFDS implementa a lista estruturada como tabela com `scope="row"` em cada cabeçalho de linha ([DKFDS](https://designsystem.dk/komponenter/tables/)). O Trama usa `<dl>` como padrão.

## Tokens usados

| Elemento                        | Token                                                        |
|---------------------------------|--------------------------------------------------------------|
| Divisores                       | `--t-border-subtle`, `--stroke-thin`                         |
| Preenchimento vertical da linha | `--sp-300`                                                   |
| Espaço entre colunas            | `--sp-400`                                                   |
| Chave                           | peso 600, `--t-fg-1`                                         |
| Valor                           | peso 400, `--t-fg-1`                                         |
| Valor ausente                   | `--t-fg-2`                                                   |
| Ação                            | `--t-link`                                                   |
| Card de resumo                  | `--t-surface-raised`, `--r-lg`, cabeçalho em `--t-surface-1` |

## Considerações por plataforma

### Web desktop

Use a proporção de colunas que aproxima o valor da chave quando as chaves forem curtas; o Ontario oferece proporções como 1:2 e 1:3 entre chave e valor ([Ontario](https://designsystem.ontario.ca/components/detail/summary-list.html)). A lista do Trama usa 1:2 com a coluna de ação no tamanho do conteúdo.

### Web móvel

Empilhe chave, valor e ação em cada linha. Mantenha os divisores entre linhas, porque eles ligam a ação ao valor. A ação continua um link de texto com área de toque de pelo menos `--c-touch` de altura.

### Tablets e dobráveis

Em janela média, use o layout em colunas da web desktop. Em um painel de detalhe estreito, empilhe como na web móvel.

## Recursos

### Relacionados

- Revisar respostas e confirmação
- Formulários em etapas e páginas de pergunta
- Tabelas
- Cards
- Links

### Referências

- [Summary list](https://design-system.service.gov.uk/components/summary-list/) GOV.UK Design System
- [Summary list](https://designsystem.ontario.ca/components/detail/summary-list.html) Ontario Design System
- [Tabeller (Strukturerede lister)](https://designsystem.dk/komponenter/tables/) DKFDS
- [Description](https://vercel.com/geist/description) Geist
- [Labels](https://developer.apple.com/design/human-interface-guidelines/labels) Apple HIG
- [Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views) Apple HIG
- [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) Apple HIG
- [Tipografia](https://www.gov.br/ds/fundamentos-visuais/tipografia) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                   |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Entram a formatação brasileira dos valores exibidos (D3), datas e unidades por extenso (D21), confirmação do que mudou (D2), limites de rótulo (D24) e densidades (D11). |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                            |
