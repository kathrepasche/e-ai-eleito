# Spinner

Um spinner indica, no lugar onde algo está sendo processado, que o sistema recebeu a ação e ainda está trabalhando, sem dizer quanto falta.

O spinner é um indicador indeterminado e circular. Ele tranquiliza: a ação foi recebida e está em andamento ([HDS](https://hds.hel.fi/components/loading-spinner)). O gov.br DS o chama de carregamento indeterminado e o usa no envio de formulários, no envio de arquivos e no carregamento de dados ([gov.br DS](https://www.gov.br/ds/components/loading)). Como não informa duração, o Trama o reserva para esperas curtas, no ponto exato da interface em que o resultado vai aparecer. Para esperas longas ou com total conhecido, a barra de progresso informa mais.

**Use um spinner** para esperas de uma ação específica entre um e três segundos: envio de um botão, atualização de uma seção, nova tentativa numa linha de tabela, pesquisa num campo ([Fluent 2](https://fluent2.microsoft.design/wait-ux), [Geist](https://vercel.com/geist/spinner)).

**Não use um spinner** para esperas abaixo de um segundo, nem para atualizações automáticas e ao vivo de conteúdo ([DKFDS](https://designsystem.dk/komponenter/spinner/)). Quando o layout final é conhecido, prefira skeleton. Quando o total é conhecido ou a espera passa de três segundos, use uma barra de progresso. O spinner também não compensa uma lentidão permanente do produto ([DKFDS](https://designsystem.dk/komponenter/spinner/)).

## Anatomia

1.  **Trilho**: anel completo em `--t-brand-subtle`, espessura `--stroke-thicker`.
2.  **Cabeça**: arco em `--t-brand` que gira em velocidade constante, com curva `--m-linear`.
3.  **Rótulo** (condicional): texto ao lado, em `--t-fg-2`, Body small 14/20, separado por `--sp-300`. Recomendado quando a espera tende a ser maior ([gov.br DS](https://www.gov.br/ds/components/loading)).
4.  **Superfície e scrim** (só no bloqueio): o conteúdo atrás é esmaecido com `--t-bg` em `--o-lg` e o spinner fica centralizado sobre ele ([gov.br DS](https://www.gov.br/ds/components/loading), [DKFDS](https://designsystem.dk/komponenter/spinner/)).

## Tipos

| Tamanho | Diâmetro           | Uso                                                                                                                                                               |
|---------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pequeno | 20px (`--icon-md`) | Dentro de componentes: botões, células de tabela, campos de pesquisa, itens de lista. A pessoa continua usando o resto da página. Pareado com texto de 14 a 16px. |
| Grande  | 32px (`--icon-xl`) | No corpo da página: uma seção ou card inteiro aguardando dados, e o bloqueio de região.                                                                           |

A divisão em um tamanho local e outro de seção segue o [DKFDS](https://designsystem.dk/komponenter/spinner/) e o [HDS](https://hds.hel.fi/components/loading-spinner). Escolha o tamanho conforme o texto ou o ícone ao redor ([Geist](https://vercel.com/geist/spinner)). Quando o total é conhecido, use o anel determinado de 84px descrito em Indicadores de progresso.

> **Divergência entre referências** O gov.br DS define o carregamento indeterminado em 24px dentro de componentes e 44px no corpo da página. Nenhum critério de evidência, acessibilidade ou contexto brasileiro separa esses valores dos do Trama; o Trama mantém 20px e 32px, alinhados aos tokens de ícone `--icon-md` e `--icon-xl`, e adota do gov.br a divisão por contexto: dentro de componente, no corpo da página e no bloqueio.

## Boas práticas

**Mostre o spinner onde o resultado vai aparecer.** Se só uma seção carrega, o spinner fica nela, centralizado horizontalmente no topo para continuar visível em telas pequenas, e o resto da página segue utilizável ([DKFDS](https://designsystem.dk/komponenter/spinner/), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/spinner/usage)). Prefira não bloquear nada.

**Bloqueie uma região só quando interagir com ela daria resultado errado.** Use `.tr-region-busy`: o conteúdo atrás fica esmaecido, o spinner fica centralizado e a região recebe `inert` e `aria-busy="true"`, porque o scrim sozinho não desativa os controles ([gov.br DS](https://www.gov.br/ds/components/loading), [gov.br DS](https://www.gov.br/ds/components/scrim)). O bloqueio da tela inteira fica para processos que afetam toda a página, como assinar um documento, na camada `--z-4`. Nunca bloqueie a pesquisa nem os recursos de acessibilidade ([gov.br DS](https://www.gov.br/ds/components/scrim)).

**Respeite os limiares de tempo.** Abaixo de um segundo, não mostre nada. Entre um e três segundos, mostre o spinner. Acima de três segundos, troque por barra de progresso ou acrescente um texto que mostre que o processo continua ([Fluent 2](https://fluent2.microsoft.design/wait-ux)).

**Depois de aparecer, mantenha o spinner por pelo menos um segundo.** Um indicador que pisca preocupa a pessoa sobre o que passou pela tela ([Ontario](https://designsystem.ontario.ca/components/detail/loading-indicator.html)).

**Mostre um spinner por vez.** Vários spinners simultâneos confundem quem vê e quem usa tecnologia assistiva ([HDS](https://hds.hel.fi/components/loading-spinner/accessibility), [Fluent 2](https://fluent2.microsoft.design/wait-ux)). Não junte o spinner a outro indicador animado na mesma linha.

**Dê uma saída para esperas sem fim.** Ofereça Cancelar em esperas que podem se alongar, para a pessoa voltar à tarefa anterior ([gov.br DS](https://www.gov.br/ds/components/loading)). Depois de um tempo razoável, troque o spinner por uma mensagem de erro com ação de tentar de novo, para que a pessoa não fique presa ([DKFDS](https://designsystem.dk/komponenter/spinner/)).

**Use o estado de carregamento do botão.** Durante o envio, o texto do botão some, o spinner pequeno aparece e o botão continua focável com `aria-disabled="true"` ([DKFDS](https://designsystem.dk/komponenter/spinner/), [Geist](https://vercel.com/geist/spinner)). A largura do botão não muda.

**Faça** coloque o spinner na seção que carrega, com um rótulo que nomeia o trabalho.

**Não faça** espalhe vários spinners com o texto genérico "Carregando".

### Estados e comportamento

- **Início**: monte o spinner só quando a ação começa. Um spinner pré-renderizado e oculto pode aparecer parado no meio do giro ([Geist](https://vercel.com/geist/spinner)).
- **Conteúdo atrás**: se o spinner grande fica sobre conteúdo existente, esmaeça o conteúdo e ponha o spinner numa caixa com fundo, para manter o contraste ([DKFDS](https://designsystem.dk/komponenter/spinner/)).
- **Movimento**: o giro é contínuo e no sentido horário ([gov.br DS](https://www.gov.br/ds/components/loading)), sem flashes nem trocas intensas de cor.
- **Movimento reduzido**: com `prefers-reduced-motion` ou com as animações desligadas no produto, o Trama para o giro. Como um indicador parado pode parecer travado ([Ontario](https://designsystem.ontario.ca/components/detail/loading-indicator.html)), o rótulo visível passa a ser obrigatório nesse modo.
- **Fim**: o spinner sai e o conteúdo entra no mesmo lugar. Se o botão sumir ou mudar de lugar após o carregamento, mova o foco para um elemento adequado, como o primeiro item do conteúdo novo ([DKFDS](https://designsystem.dk/komponenter/spinner/)).

## Conteúdo

**Rotule quando a espera passar de três segundos.** Em botões e ações iniciadas pela pessoa, o rótulo visível é dispensável, porque ela sabe o que pediu ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)). Em seções, ou quando a espera se alonga, mostre o rótulo ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/spinner/usage)).

**Repita o verbo da ação, no gerúndio.** Botão "Pesquisar", rótulo "Pesquisando pedidos …". Até três palavras, caixa de frase, reticências precedidas de espaço não separável ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/spinner/usage)).

**Evite "Carregando" sempre que possível.** Se não der para ser específico, use uma frase geral como "Preparando tudo …" ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/spinner/usage)). Em esperas muito longas, atualize o texto com o passo atual: "Localizando endereço …" ([Ontario](https://designsystem.ontario.ca/components/detail/loading-indicator.html)).

## Acessibilidade

- O círculo animado é decorativo (`aria-hidden="true"`). O significado vem de texto: o rótulo visível ou um texto oculto.
- Anuncie início e fim numa região viva dedicada (`role="status"`, anúncio educado) criada antes do carregamento, fora do botão: nem todos os leitores de tela percebem mudanças dentro de botões ([DKFDS](https://designsystem.dk/komponenter/spinner/)).
- Anuncie também a conclusão, com textos como "Conteúdo da página carregado" ([HDS](https://hds.hel.fi/components/loading-spinner/accessibility), [gov.br DS](https://www.gov.br/ds/components/loading)). Reserve `role="alert"` para a falha. O gov.br admite `aria-live="assertive"` no status; o Trama usa o anúncio educado no andamento, que não interrompe a leitura, como explica a nota em Indicadores de progresso.
- Se o spinner for uma imagem ou SVG, dê a ele uma descrição, como `title` ou `alt` "Carregando", quando não houver rótulo de texto ([gov.br DS](https://www.gov.br/ds/components/loading)).
- Marque a área que está sendo atualizada com `aria-busy="true"` e mantenha o gatilho focável durante o carregamento ([Geist](https://vercel.com/geist/spinner)).
- A cabeça do spinner tem contraste de pelo menos 3:1 com o fundo (WCAG 2.2, 1.4.11; também exigido pelo [HDS](https://hds.hel.fi/components/loading-spinner)).

## Tokens usados

| Elemento            | Token                                       |
|---------------------|---------------------------------------------|
| Trilho              | `--t-brand-subtle`                          |
| Cabeça              | `--t-brand`                                 |
| Espessura           | `--stroke-thicker`                          |
| Rótulo              | `--t-fg-2`                                  |
| Espaço até o rótulo | `--sp-300`                                  |
| Curva               | `--m-linear`                                |
| Tamanhos            | `--icon-md`, `--icon-xl`                    |
| Bloqueio de região  | `--t-bg`, `--o-lg`; tela inteira em `--z-4` |

Em botões primários, o spinner herda `--t-on-brand` para manter o contraste sobre o fundo de marca.

## Considerações por plataforma

### Web desktop

Num campo de pesquisa, alinhe o spinner ao início da área de resultados, onde o texto vai aparecer ([Ontario](https://designsystem.ontario.ca/components/detail/loading-indicator.html)). Spinners pequenos funcionam bem para tarefas assíncronas em segundo plano, como obter mensagens novas do servidor ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)).

### Web móvel

Conexões móveis oscilam, então o limite de tempo para trocar o spinner por erro precisa considerar redes lentas. Mantenha o spinner da seção no topo da área visível, nunca no centro de uma área longa que exija rolagem para ser vista.

### Tablets e dobráveis

Em layouts de dois painéis, o spinner aparece só no painel que carrega; o outro continua interativo. Nenhuma consideração adicional para dobráveis.

## Recursos

### Relacionados

- Carregamento e espera
- Indicadores de progresso
- Skeleton
- Botões

### Referências

- [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators) Apple HIG
- [Loading](https://www.gov.br/ds/components/loading) gov.br DS
- [Scrim](https://www.gov.br/ds/components/scrim) gov.br DS
- [Spinner](https://fluent2.microsoft.design/components/web/react/core/spinner/usage) Fluent 2
- [Wait UX](https://fluent2.microsoft.design/wait-ux) Fluent 2
- [Loading spinner](https://designsystem.dk/komponenter/spinner/) DKFDS
- [LoadingSpinner](https://hds.hel.fi/components/loading-spinner) Helsinki Design System
- [LoadingSpinner: accessibility](https://hds.hel.fi/components/loading-spinner/accessibility) Helsinki Design System
- [Spinner](https://vercel.com/geist/spinner) Geist
- [Loading indicator](https://designsystem.ontario.ca/components/detail/loading-indicator.html) Ontario Design System
- [Spinner](https://blueprintjs.com/docs/#core/components/spinner) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                             |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o bloqueio de região com `.tr-region-busy`, os contextos de uso por tamanho, Cancelar em esperas longas, a descrição de spinners em imagem e o vocabulário "Pesquisar". |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                      |
