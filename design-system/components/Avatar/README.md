# Avatar

Um avatar representa uma pessoa ou um grupo com foto, iniciais ou ícone, pode indicar se essa pessoa está disponível e pode abrir o menu da conta.

Avatares tornam reconhecível quem fez o quê: o autor de um comentário, o responsável por uma tarefa, os participantes de um documento. A foto cria uma ligação mais direta que o texto, por isso o Trama a prefere quando existe; sem foto, mostra as iniciais ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/lockups)). O avatar acompanha o nome sempre que há espaço: sozinho, ele exige que a pessoa reconheça um rosto ou duas letras.

**Use um avatar** para representar a pessoa que entrou no sistema, no cabeçalho, e para identificar pessoas, equipes ou organizações em listas, comentários, conversas, campos de responsável e listas de participantes ([gov.br DS](https://www.gov.br/ds/components/avatar)) ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/avatar/usage), [Geist](https://vercel.com/geist/avatar)).

**Não use um avatar** como ícone decorativo de seção, para representar objetos (arquivos, produtos) ou como único meio de identificar alguém em tabelas densas: ali, o nome em texto é mais rápido de ler. Para mostrar muitas pessoas, use o grupo de avatares descrito abaixo.

## Anatomia

1.  **Contêiner**: círculo para pessoas; quadrado de raio `--r-lg` para grupos, equipes e organizações ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/avatar/usage)).
2.  **Conteúdo**: foto, iniciais em `--t-brand` sobre `--t-brand-subtle`, ou ícone genérico de pessoa ([gov.br DS](https://www.gov.br/ds/components/avatar)).
3.  **Indicador de menu** (opcional, no acionador): seta à direita, centralizada na vertical, para baixo com o menu fechado e para cima com o menu aberto ([gov.br DS](https://www.gov.br/ds/components/avatar)).
4.  **Indicador de presença** (opcional): ponto no canto inferior, com anel de 2px na cor do fundo para separá-lo do avatar.

## Tipos

### Conteúdo

| Tipo     | Quando aparece                                         |
|----------|--------------------------------------------------------|
| Foto     | A pessoa escolheu uma foto para se representar.        |
| Iniciais | Não há foto, ou a pessoa preferiu as iniciais.         |
| Ícone    | Primeiro acesso, ou quando nem o nome está disponível. |

A pessoa pode trocar de um tipo para outro a qualquer momento ([gov.br DS](https://www.gov.br/ds/components/avatar)).

### Tamanhos

| Tamanho        | Medida | Uso                                                                    |
|----------------|--------|------------------------------------------------------------------------|
| Pequeno        | 24px   | Ao lado de texto de 14px: menções, linhas de tabela, grupos compactos. |
| Médio (padrão) | 40px   | Listas, comentários, campos de responsável.                            |
| Grande         | 56px   | Cabeçalhos de perfil e de conta, tela de troca de foto.                |

Para mostrar a foto em destaque numa página de perfil, acima de 56px, use o componente Imagem com recorte circular.

Escolha o tamanho pelo texto ao lado: avatares menores acompanham rótulos menores e os maiores ficam em cabeçalhos ([Geist](https://vercel.com/geist/avatar)).

### Grupo de avatares

Para várias pessoas, o Trama mostra até cinco posições. Com mais de cinco, a quinta posição vira um avatar de excedente com a quantidade restante, por exemplo "+3", que pode abrir uma lista com todos os nomes ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/avatargroup/usage)). No layout empilhado, os avatares se sobrepõem e o primeiro fica por cima, para que o primeiro autor continue em destaque ([Geist](https://vercel.com/geist/avatar)). Use o layout espaçado quando precisar mostrar presença em cada avatar ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/avatargroup/usage)).

## Boas práticas

**Use a foto primeiro e as iniciais como alternativa.** Se a foto não carregar ou não existir, mostre de uma a duas letras maiúsculas tiradas do nome. O estado de carregamento usa um skeleton circular, nunca como substituto permanente ([Geist](https://vercel.com/geist/avatar)).

**Derive as iniciais do nome real.** Primeira letra do primeiro nome e do último sobrenome. Sem emoji, pontuação ou "?" ([Geist](https://vercel.com/geist/avatar)). Quando nem o nome está disponível, use o ícone genérico de pessoa.

**Não atribua gênero ao avatar genérico.** O ícone padrão representa uma pessoa, sem marcas de gênero, e a pessoa pode trocar a própria imagem ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/inclusion)).

**Mostre o nome junto ao avatar.** Em listas e comentários, o nome em texto fica ao lado. Só omita o nome em grupos compactos, e então ofereça o nome em tooltip e no nome acessível.

**Facilite a troca da imagem.** Ofereça na conta as opções de foto, iniciais ou ícone. Para enviar uma foto, use o botão "Enviar foto", aceite os formatos de imagem mais comuns (JPG, PNG e GIF) e informe no texto de ajuda o tamanho máximo do arquivo; o gov.br sugere 1 megabyte ([gov.br DS](https://www.gov.br/ds/components/avatar)). Mostre a prévia no tamanho grande antes de salvar e ofereça "Remover foto", que volta às iniciais.

**Abra o menu da conta só por clique ou toque.** No cabeçalho, o avatar pode ser o acionador do menu da conta, com o nome e o e-mail da pessoa no topo e "Sair" no fim ([gov.br DS](https://www.gov.br/ds/components/avatar), [gov.br DS](https://www.gov.br/ds/components/notification)). Use um botão com `aria-haspopup="menu"` e `aria-expanded`, e mostre o nome ao lado quando houver espaço. Um badge de contagem no avatar indica notificações novas.

**Mantenha a cor das iniciais neutra e consistente.** O Trama usa uma única combinação de marca para todas as iniciais, para que a cor não seja lida como status.

**Faça** acompanhe o avatar do nome da pessoa.

**Não faça** use pontuação, letras minúsculas ou avatares sem nome.

### Estados e comportamento

- **Estático**: por padrão, o avatar não tem estados e não recebe foco ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/avatar/usage)).
- **Interativo**: se o avatar abre um perfil, um menu ou um cartão de contexto, envolva-o num link ou botão com foco, hover, pressionado e alvo mínimo de `--c-touch` no toque ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/avatar/usage), [gov.br DS](https://www.gov.br/ds/components/avatar)).
- **Menu aberto**: o acionador mostra o estado aberto com a camada de estado e o indicador para cima; o menu fica em `--z-2`.
- **Presença**: disponível, ocupado, ausente e offline. Em avatares de 32px ou menos o ponto fica difícil de perceber; ofereça o status também em texto, como num tooltip ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/avatar/usage)).
- **Atividade**: um anel em `--t-brand` ao redor do avatar pode indicar quem está editando ou falando agora ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/avatar/usage)).

> **Divergência entre referências** Acionamento: o gov.br DS permite abrir o menu do avatar com clique ou com hover. Pelo critério de acessibilidade, o Trama abre o menu só por clique, toque ou teclado: um menu de ações que surge com hover não existe no toque e fecha quando o ponteiro se afasta (WCAG 2.2, 1.4.13). O hover fica restrito a tooltip e cartão de contexto. Tamanhos: o gov.br usa 40, 100 e 160px; o Trama mantém 24, 40 e 56px, que acompanham o texto ao lado, como pede o Geist, e leva fotos maiores para o componente Imagem. Iniciais: o gov.br mostra uma inicial; o Trama mantém até duas, como o Geist, porque duas letras distinguem pessoas com o mesmo primeiro nome. Nenhum critério de evidência ou contexto brasileiro favorece outra opção nesses dois pontos.

## Conteúdo

O nome acessível é o nome literal da entidade: "Marina Teixeira", "Equipe Financeiro". Não escreva "Avatar de" nem "Foto de" ([Geist](https://vercel.com/geist/avatar)). O avatar de excedente diz quantas pessoas faltam ("+3"), nunca "Mais".

## Acessibilidade

- Avatar sozinho: `<img alt="Nome">` para foto, ou `role="img"` com `aria-label` para iniciais. No avatar de ícone, o ícone tem `aria-hidden="true"` e o contêiner leva o nome ([gov.br DS](https://www.gov.br/ds/components/avatar)).
- Avatar ao lado do nome visível: decorativo, com `alt=""` ou `aria-hidden="true"`, para não repetir o nome.
- Grupo: um único nome acessível para o conjunto, como "5 participantes: Ana Lopes, Bruno Dias e mais 3" ([Geist](https://vercel.com/geist/avatar)).
- A presença entra no nome acessível ("Marina Teixeira, disponível"), porque cor e forma do ponto não bastam (WCAG 2.2, 1.4.1).
- As iniciais têm contraste mínimo de 4.5:1 com o fundo (WCAG 2.2, 1.4.3).
- O avatar interativo é alcançado com Tab e acionado com Enter ou Espaço, com o foco sempre visível ([gov.br DS](https://www.gov.br/ds/components/avatar)). Quando não há nome visível ao lado, um tooltip no avatar focável mostra o nome completo ([gov.br DS](https://www.gov.br/ds/components/avatar)).

## Tokens usados

| Elemento                   | Token                                   |
|----------------------------|-----------------------------------------|
| Fundo das iniciais         | `--t-brand-subtle`                      |
| Iniciais                   | `--t-brand`, peso 600                   |
| Raio do avatar de grupo    | `--r-lg`                                |
| Presença disponível        | `--t-success`                           |
| Presença ocupado e ausente | `--t-danger`, `--t-warning-fill`        |
| Anel da presença           | `--t-bg`, `--stroke-thick`              |
| Anel de atividade          | `--t-brand`, `--stroke-thick`           |
| Espaço até o nome          | `--sp-300`                              |
| Acionador de menu          | `--o-hover`, `--o-pressed`, `--c-touch` |
| Menu da conta              | `--e-4`, `--z-2`                        |

## Considerações por plataforma

### Web desktop

Hover num avatar de outra pessoa pode abrir um cartão de contexto com nome, cargo e uma ação; o mesmo conteúdo abre com foco do teclado. O avatar da própria conta, no cabeçalho, abre o menu por clique, com o nome ao lado a partir da classe Expandida.

### Web móvel

Não existe hover: o toque no avatar leva ao perfil ou abre o menu da conta. No cabeçalho da classe Compacta, mostre só o avatar, com alvo de `--c-touch` e o nome no nome acessível ([gov.br DS](https://www.gov.br/ds/components/avatar)). Para enviar foto, aceite a câmera e a galeria do aparelho pelo seletor de arquivos do navegador. Como presença em avatares pequenos é difícil de ver, mostre o status em texto no perfil ou na lista.

### Tablets e dobráveis

Nenhuma consideração adicional para tablets e dobráveis.

## Recursos

### Relacionados

- Badges
- Listas
- Imagem
- Inclusão
- Popovers
- Menus
- Upload de arquivo

### Referências

- [Lockups (Monograms)](https://developer.apple.com/design/human-interface-guidelines/lockups) Apple HIG
- [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion) Apple HIG
- [Avatar](https://www.gov.br/ds/components/avatar) gov.br DS
- [Notification](https://www.gov.br/ds/components/notification) gov.br DS
- [Avatar](https://fluent2.microsoft.design/components/web/react/core/avatar/usage) Fluent 2
- [Avatar group](https://fluent2.microsoft.design/components/web/react/core/avatargroup/usage) Fluent 2
- [Avatar](https://vercel.com/geist/avatar) Geist

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                       |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o avatar como acionador do menu da conta, a troca e o envio de foto, os tipos de conteúdo e o tooltip com o nome, e registra as divergências de acionamento, tamanhos e iniciais. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                |
