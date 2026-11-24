# Badges

Um badge é um rótulo pequeno e somente de leitura que mostra o status de algo ou a quantidade de itens novos, ao lado do elemento a que se refere.

Badges ajudam a escanear: numa lista de pedidos, a pessoa vê de relance quais estão "Em separação" e quais estão "Entregues". Num item de navegação, um número indica mensagens não lidas. O badge descreve, e a ação mora em outro lugar. Ele nunca é botão nem link ([GOV.UK](https://design-system.service.gov.uk/components/tag/), [Geist](https://vercel.com/geist/badge)). No gov.br DS, o badge corresponde às tags de status e de contagem; as tags de interação, que a pessoa seleciona ou remove, ficam em Tags e chips ([gov.br DS](https://www.gov.br/ds/components/tag)).

**Use um badge** quando algo pode ter mais de um status e é útil saber qual é: situação de um pedido, fase de um recurso ("Beta"), plano de uma conta, ou uma contagem de itens que pedem atenção ([GOV.UK](https://design-system.service.gov.uk/components/tag/), [Ontario](https://designsystem.ontario.ca/components/detail/badges.html)).

**Não use um badge** para chamar atenção para conteúdo importante: use uma mensagem ([Ontario](https://designsystem.ontario.ca/components/detail/badges.html)). Para filtros clicáveis ou valores removíveis, use tags e chips. Não marque como "Novo" itens de páginas em que o mais recente já aparece primeiro, como uma lista de notícias ([DKFDS](https://designsystem.dk/komponenter/badges/)).

## Anatomia

1.  **Contêiner**: altura de 20px, raio `--r-pill`, preenchimento horizontal `--sp-200`, fundo suave da intenção.
2.  **Texto**: Caption 12/16 semibold, na cor forte da intenção.
3.  **Ícone** (opcional): à esquerda, separado por `--sp-100`, sempre acompanhado de texto ([gov.br DS](https://www.gov.br/ds/components/tag)).
4.  **Contorno de separação** (só quando sobrepõe outro elemento): anel de `--stroke-thick` em `--t-bg`, como no badge de contagem sobre um ícone ou avatar ([gov.br DS](https://www.gov.br/ds/components/tag)).

## Tipos

| Tipo     | Uso                                                                                                                                                                                                                                                                                                                               |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Status   | Uma ou duas palavras com cor de intenção. Neutro, informação, sucesso, aviso, erro e marca.                                                                                                                                                                                                                                       |
| Contagem | Número de itens não lidos ou pendentes num item de navegação, numa aba ou no acionador de notificações, como o avatar com badge do cabeçalho ([gov.br DS](https://www.gov.br/ds/components/notification)). Fundo `--t-danger`. Até três dígitos; acima de 999, mostre "999+" ([gov.br DS](https://www.gov.br/ds/components/tag)). |
| Ponto    | Um círculo de cor ao lado de um texto visível que nomeia o estado, como em listas de implantações ([Geist](https://vercel.com/geist/status-dot)). Nunca aparece sozinho.                                                                                                                                                          |

Associe cor a significado e mantenha a associação no produto todo: verde para positivo ou concluído, azul para informação, amarelo para aviso, vermelho para erro ou urgência, cinza para neutro ([DKFDS](https://designsystem.dk/komponenter/badges/), [Geist](https://vercel.com/geist/badge)). O Trama usa o fundo suave com texto forte, porque fundos escuros com texto branco foram confundidos com botões em pesquisas do [GOV.UK](https://design-system.service.gov.uk/components/tag/).

## Boas práticas

**Use uma cor por badge e poucas cores por tela.** Variedade de cores desvia a atenção do que importa ([gov.br DS](https://www.gov.br/ds/components/tag)).

**Use o menor número de status possível.** Quanto mais status, mais difícil lembrar o que cada um significa. Às vezes um só basta: se só os itens concluídos têm "Concluído", a ausência já diz "não concluído" ([GOV.UK](https://design-system.service.gov.uk/components/tag/), [Ontario](https://designsystem.ontario.ca/components/detail/badges.html)).

**Nunca torne o badge interativo.** Sem diferença visual entre badges clicáveis e não clicáveis, ninguém sabe em qual tocar. Se a pessoa pode agir sobre o valor, use um botão ou link ([GOV.UK](https://design-system.service.gov.uk/components/tag/), [Geist](https://vercel.com/geist/badge)). Teste se o posicionamento não faz o badge parecer botão ([DKFDS](https://designsystem.dk/komponenter/badges/)).

**Coloque o badge junto ao que ele descreve.** Perto o bastante para a relação ser óbvia, na mesma linha da tabela ou abaixo do título da seção ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/badge/usage), [HDS](https://hds.hel.fi/components/status-label)). Um badge que vale para a página inteira fica perto do canto superior esquerdo ([Ontario](https://designsystem.ontario.ca/components/detail/badges.html)).

**Use um badge por linha.** Dois badges lado a lado indicam que a linha precisa de outra coluna ([Geist](https://vercel.com/geist/badge)). Não misture tamanhos de badge no mesmo contexto ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/badge/usage)).

**Reserve o badge de contagem para o que pede atenção.** Use-o para itens não lidos ou pendentes, nunca para dados como temperatura, datas ou placares. Mantenha-o atualizado: zere a contagem assim que a pessoa vê os itens ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/notifications)). Use-o com moderação para não diluir o impacto ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/tab-bars)). Com mais de três dígitos, mostre "999+" e dê o número exato no nome acessível do elemento e num tooltip do elemento focável que contém o badge, como o link de navegação ([gov.br DS](https://www.gov.br/ds/components/tag)).

**Ofereça a solução para status de aviso e erro.** Um badge "Pagamento pendente" vem acompanhado, na mesma linha ou no detalhe, da ação que resolve ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/badge/usage)).

**Faça** use adjetivos curtos que descrevem o estado.

**Não faça** use verbos que sugerem clique ou frases inteiras dentro do badge.

### Estados e comportamento

- O badge é estático, sem estados de hover, foco ou pressionado.
- Se precisar de explicação (por exemplo, o que significa "Beta"), coloque um tooltip num ícone de informação ao lado, ou torne o badge focável apenas para exibir o tooltip ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/badge/usage), [Geist](https://vercel.com/geist/badge)).
- O badge cresce com o texto, tem altura fixa e nunca quebra em duas linhas ([HDS](https://hds.hel.fi/components/status-label), [gov.br DS](https://www.gov.br/ds/components/tag)). Como o texto tem no máximo 15 caracteres, ele não precisa ser truncado.
- A densidade da página não muda o badge: ele mantém 20px de altura em todas as densidades.
- Não troque a cor do badge a cada atualização intermediária de um processo; mude só quando o estado de fato mudar ([Geist](https://vercel.com/geist/status-dot)).

## Conteúdo

**Use uma ou duas palavras.** No máximo 15 caracteres ([Ontario](https://designsystem.ontario.ca/components/detail/badges.html), [HDS](https://hds.hel.fi/components/status-label)).

**Prefira adjetivos, particípios e substantivos.** "Aprovado", "Pendente", "Beta". Verbos sugerem que o badge faz algo ([GOV.UK](https://design-system.service.gov.uk/components/tag/), [gov.br DS](https://www.gov.br/ds/components/tag)).

**Use caixa de frase.** Texto em maiúsculas é mais difícil de ler ([GOV.UK](https://design-system.service.gov.uk/components/tag/)).

**Use os termos que a pessoa conhece do produto.** O badge repete o nome do status usado em filtros, relatórios e e-mails ([DKFDS](https://designsystem.dk/komponenter/badges/)).

## Acessibilidade

- O texto do badge carrega o significado; a cor é reforço (WCAG 2.2, 1.4.1). Um badge só com ícone precisa de nome acessível ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/badge/usage)), e o Trama desaconselha esse uso ([HDS](https://hds.hel.fi/components/status-label)).
- Num badge de contagem, inclua a informação no nome do elemento a que ele pertence: "Caixa de entrada, 3 não lidas" ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/badge/usage)). Com "999+", o nome traz o número exato: "Processos, 1.254 novos".
- O badge não recebe foco. Se o significado precisar de explicação, ela fica num elemento focável ao lado, que se alcança com Tab e se aciona com Enter ou Espaço ([gov.br DS](https://www.gov.br/ds/components/tag)).
- Quando o texto ao lado já nomeia o estado, oculte o ponto de cor com `aria-hidden="true"` para não ser lido duas vezes ([Geist](https://vercel.com/geist/status-dot)).
- O texto de cada intenção tem contraste mínimo de 4.5:1 sobre o fundo suave (WCAG 2.2, 1.4.3).

> **Divergência entre referências** Status só com cor: o gov.br DS aceita a tag de status sem rótulo, só a superfície circular, com tooltip para evitar ambiguidade. O Geist usa o ponto de cor ao lado de um texto que nomeia o estado. Pelo critério de acessibilidade, o Trama exige texto visível ao lado do ponto, porque um tooltip não chega a quem usa toque e a cor sozinha não atende WCAG 2.2, 1.4.1. Tamanho do texto: o gov.br permite até cem caracteres, com reticências a partir daí; o Ontario e o HDS limitam a 15. Pela convergência, o Trama mantém 15 caracteres. Limite da contagem: a versão 1.0 deixava o limite a cargo do produto; sem referência em contrário, o Trama adota o "999+" do gov.br.

## Tokens usados

| Variante   | Fundo                | Texto         |
|------------|----------------------|---------------|
| Neutro     | `--t-surface-2`      | `--t-fg-2`    |
| Marca      | `--t-brand-subtle`   | `--t-brand`   |
| Informação | `--t-info-subtle`    | `--t-info`    |
| Sucesso    | `--t-success-subtle` | `--t-success` |
| Aviso      | `--t-warning-subtle` | `--t-warning` |
| Erro       | `--t-danger-subtle`  | `--t-danger`  |
| Contagem   | `--t-danger`         | `--t-bg`      |

Forma: `--r-pill`, `--sp-200` de preenchimento horizontal, `--sp-100` entre ícone e texto. Contorno de separação sobre outros elementos: `--stroke-thick` em `--t-bg`.

## Considerações por plataforma

### Web desktop

Em tabelas, dê ao status uma coluna própria, alinhada à esquerda, para escanear de cima a baixo.

### Web móvel

Em listas, posicione o badge abaixo do título do item ou no fim da linha, sem truncar o título. Na barra de navegação inferior, o badge de contagem fica sobre o canto do ícone, com o contorno de separação. Como o tooltip não existe no toque, o número exato aparece na tela de destino.

### Tablets e dobráveis

Nenhuma consideração adicional para tablets e dobráveis.

## Recursos

### Relacionados

- Tags e chips
- Avatar
- Mensagens e banners
- Tabelas
- Cor

### Referências

- [Notifications (Badging)](https://developer.apple.com/design/human-interface-guidelines/notifications) Apple HIG
- [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) Apple HIG
- [Tag](https://design-system.service.gov.uk/components/tag/) GOV.UK
- [Tag](https://www.gov.br/ds/components/tag) gov.br DS
- [Notification](https://www.gov.br/ds/components/notification) gov.br DS
- [Badges](https://designsystem.dk/komponenter/badges/) DKFDS
- [StatusLabel](https://hds.hel.fi/components/status-label) Helsinki Design System
- [Badge](https://fluent2.microsoft.design/components/web/react/core/badge/usage) Fluent 2
- [Badge](https://vercel.com/geist/badge) Geist
- [Status Dot](https://vercel.com/geist/status-dot) Geist
- [Badges](https://designsystem.ontario.ca/components/detail/badges.html) Ontario Design System

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                           |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o limite "999+" com número exato acessível, o contorno de separação sobre outros elementos e a regra de poucas cores, e exige texto visível junto ao ponto de status. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                    |
