# IndicadoresDeProgresso

Um indicador de progresso mostra quanto de uma tarefa já foi feito e quanto falta, para que a pessoa saiba que o sistema está trabalhando e decida se espera.

Indicadores de progresso são transitórios: aparecem enquanto a operação acontece e somem quando ela termina ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)). O Trama tem duas formas de progresso determinado: a barra linear, padrão, e o anel circular com porcentagem, para um processo que ocupa uma área ou bloqueia a tela, como o carregamento determinado do [gov.br DS](https://www.gov.br/ds/components/loading). O spinner fica para esperas curtas sem medida. Uma variante estática, o medidor, mostra um valor dentro de um limite, como o uso de armazenamento.

**Use uma barra de progresso** para tarefas que levam mais de um segundo e cujo total é conhecido ou pode ser estimado: envio de arquivos, importação de planilhas, exportações, processamento em lote ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/progressbar/usage), [Geist](https://vercel.com/geist/progress)).

**Não use uma barra de progresso** para esperas abaixo de um segundo, em que qualquer indicador só pisca e confunde ([Fluent 2](https://fluent2.microsoft.design/wait-ux)). Para conteúdo com estrutura conhecida, use skeleton. Para esperas curtas sem total conhecido, use spinner. Para mostrar em que etapa de um formulário a pessoa está, use o indicador de etapas.

## Anatomia

1.  **Rótulo**: acima da barra, nomeia o trabalho em andamento.
2.  **Trilho**: altura de 4px, cor `--t-surface-2`, raio `--r-pill`.
3.  **Preenchimento**: `--t-brand`, cresce do lado inicial para o final.
4.  **Texto de status** (opcional): abaixo da barra, em `--t-fg-3`, com a quantidade feita ou o passo atual.
5.  **Cancelar** (opcional): botão alinhado ao rótulo, no canto final, só quando o sistema consegue interromper a operação em curso ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/progressbar/usage), [gov.br DS](https://www.gov.br/ds/components/loading)).

### Anel circular determinado

1.  **Círculo base**: `--t-surface-2`, a parte ainda não concluída.
2.  **Círculo progressivo**: `--t-brand`, cresce no sentido horário a partir do topo até completar a volta ([gov.br DS](https://www.gov.br/ds/components/loading)).
3.  **Rótulo percentual** (obrigatório): de 0% a 100% no centro, atualizado com o avanço.
4.  **Rótulo da tarefa e Cancelar**: ao lado ou abaixo do anel.

O anel tem tamanho único de 84px ([gov.br DS](https://www.gov.br/ds/components/loading)). Quando bloqueia a tela ou uma região, aparece centralizado sobre uma superfície `--t-surface-raised` com elevação `--e-6`, por cima de um scrim, para manter o contraste ([gov.br DS](https://www.gov.br/ds/components/loading)).

## Tipos

| Tipo               | Quando usar                                                                                                                                                                                                             |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Determinada        | O total é conhecido. É o tipo preferido, porque ajuda a pessoa a decidir se espera, faz outra coisa ou desiste ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)).        |
| Indeterminada      | A duração não pode ser estimada. Use apenas em tarefas curtas e troque para determinada assim que houver dados para estimar ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/progressbar/usage)). |
| Anel determinado   | O total é conhecido e o processo ocupa uma área ou bloqueia a tela, como gerar um documento ou enviar um arquivo grande por cima do formulário ([gov.br DS](https://www.gov.br/ds/components/loading)).                 |
| Medidor (estático) | Um valor dentro de um limite, sem animação: armazenamento, cota, consumo do período. Pode mudar de cor em limiares definidos ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/gauges)).       |

## Boas práticas

**Seja preciso e regular.** Mostrar 90% em cinco segundos e os últimos 10% em cinco minutos parece engano. Distribua o avanço de forma uniforme ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)).

**Nunca volte a barra.** Junte etapas relacionadas numa barra só e troque o texto de status quando uma etapa começa. Uma barra que recomeça ou anda para trás reduz a confiança ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/progressbar/usage)).

**Mantenha a barra em movimento.** Um indicador parado parece travado. Se o processo de fato parou, diga o que aconteceu e o que a pessoa pode fazer ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)).

**Não troque o formato no meio.** Spinner e barra têm formas e tamanhos diferentes; trocar um pelo outro desorganiza a interface ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)). Se começar indeterminada, a barra passa a determinada no mesmo lugar.

**Deixe a pessoa interromper.** Ofereça Cancelar quando interromper não tem efeito colateral, e sempre que a espera puder ser longa, para que a pessoa volte à tarefa anterior ([gov.br DS](https://www.gov.br/ds/components/loading)). Se cancelar perde o que já foi feito, ofereça Pausar também, e confirme o cancelamento ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)).

**Mostre a barra num lugar consistente.** Sob o elemento que iniciou a tarefa, num drawer ou num toast de progresso para processos em segundo plano ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/progressbar/usage), [Fluent 2](https://fluent2.microsoft.design/wait-ux)).

**Bloqueie só o que precisa esperar.** Se a pessoa pode continuar em outras partes, deixe a página livre e mostre o progresso no lugar da tarefa. Bloqueie uma região, ou a tela, só quando interagir durante o processo corromperia o resultado. O bloqueio usa scrim, fica na camada `--z-4` e traz sempre a superfície com o indicador ([gov.br DS](https://www.gov.br/ds/components/loading)). Nunca bloqueie a pesquisa nem os recursos de acessibilidade do produto ([gov.br DS](https://www.gov.br/ds/components/scrim)).

**Use os mesmos limiares do resto do produto.** Se o aviso de cota dispara em 80%, o medidor muda de cor em 80% também ([Geist](https://vercel.com/geist/progress)).

**Faça** nomeie o trabalho e use a unidade real.

**Não faça** use rótulo vago e estimativas de tempo pouco confiáveis.

### Estados e comportamento

- **Em andamento**: o preenchimento avança com transição de `--m-normal` e `--m-ease-standard`. Sem cores que piscam nem variações intensas, que prejudicam pessoas sensíveis a estímulos visuais ([gov.br DS](https://www.gov.br/ds/components/loading); WCAG 2.2, 2.3.1).
- **Indeterminado**: um segmento percorre o trilho em laço. Se pouco tempo falta, termine o ciclo da animação antes de sair do estado de carregamento ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/progressbar/usage)). Com `prefers-reduced-motion` ou com as animações desligadas no produto, o segmento fica parado e o texto de status carrega a informação.
- **Concluído**: a barra sai e dá lugar a um estado final, como um toast ou uma linha de sucesso. Não escreva "concluído com sucesso" sobre a barra cheia ([Geist](https://vercel.com/geist/progress)).
- **Erro**: o preenchimento passa a `--t-danger` e o texto de status é trocado por uma mensagem que diz o que falhou e o que fazer ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/progressbar/usage)).

## Conteúdo

**Nomeie o trabalho.** "Enviando notas fiscais", "Exportando relatório". Evite termos vagos como "Carregando" ou "Processando", que pouco acrescentam ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)).

**Use unidades reais, por extenso.** "12 de 30 arquivos", "1,2 gigabyte de 4 gigabytes". Abreviações como MB e GB só cabem em células de tabela e cartões compactos, com a unidade nomeada no cabeçalho. A barra sozinha não diz o que está progredindo ([Geist](https://vercel.com/geist/progress)). Evite estimativas de tempo, que raramente são precisas o bastante ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/progressbar/usage)).

**Escreva o rótulo em caixa de frase, sem ponto final.** No texto de status em andamento, use gerúndio com reticências precedidas de espaço não separável: "Verificando arquivos …" ([Fluent 2](https://fluent2.microsoft.design/wait-ux)).

## Acessibilidade

- Use `role="progressbar"` com `aria-valuemin`, `aria-valuemax` e `aria-valuenow`; na indeterminada, omita `aria-valuenow`. Dê nome com `aria-labelledby` apontando para o rótulo ([Geist](https://vercel.com/geist/progress)).
- Use `aria-valuetext` quando a unidade não for porcentagem: "12 de 30 arquivos".
- No anel, o rótulo percentual visível fica oculto para o leitor de tela (`aria-hidden="true"`), porque o valor já vem de `aria-valuenow`.
- Anuncie início e fim numa região viva com `role="status"` (anúncio educado): "Gerando o relatório anual", "Relatório gerado". A conclusão precisa chegar a quem usa tecnologia assistiva ([gov.br DS](https://www.gov.br/ds/components/loading)).
- Atualize `aria-valuenow` no máximo uma vez por segundo, para que o leitor de tela não anuncie cada incremento ([Geist](https://vercel.com/geist/progress)).
- O medidor estático usa `role="meter"`. Limiares por cor sempre vêm acompanhados de texto (WCAG 2.2, 1.4.1).
- Quando a operação bloqueia a tela, prenda o foco na superfície do indicador, com Cancelar focável, e marque o resto como `inert`.
- O preenchimento tem contraste de pelo menos 3:1 com o trilho e o fundo (WCAG 2.2, 1.4.11).

> **Divergência entre referências** O gov.br DS admite `aria-live="assertive"` para o status de carregamento ([gov.br DS](https://www.gov.br/ds/components/loading)); o Geist limita a frequência dos anúncios para não sobrecarregar o leitor de tela. Pelo critério de acessibilidade, o Trama anuncia progresso com `role="status"` (educado), que não interrompe a leitura em curso, e reserva o anúncio assertivo para falhas. O gov.br sugere também retorno sonoro; no Trama ele é opcional, desligável e sempre acompanhado do texto.

## Tokens usados

| Elemento                            | Token                                                 |
|-------------------------------------|-------------------------------------------------------|
| Trilho                              | `--t-surface-2`, `--r-pill`                           |
| Preenchimento                       | `--t-brand`                                           |
| Medidor em limiar de aviso ou erro  | `--t-warning-fill`, `--t-danger`                      |
| Anel: base, progresso e rótulo      | `--t-surface-2`, `--t-brand`, `--t-fg-1`              |
| Bloqueio                            | `--t-overlay`, `--t-surface-raised`, `--e-6`, `--z-4` |
| Rótulo e status                     | `--t-fg-1`, `--t-fg-3`                                |
| Espaço entre rótulo, barra e status | `--sp-100`                                            |
| Movimento                           | `--m-normal`, `--m-ease-standard`                     |

## Considerações por plataforma

### Web desktop

Limite a barra a 360px quando ela acompanha um formulário; em tabelas, a barra pode ocupar a célula. Tarefas longas que continuam enquanto a pessoa navega vão para um toast de progresso.

### Web móvel

A barra ocupa a largura do contêiner. O anel mantém os 84px e fica centralizado na área que carrega. Se a pessoa pode sair da página durante a tarefa, continue o trabalho no servidor e avise quando terminar, em vez de pedir que ela mantenha a tela aberta.

### Tablets e dobráveis

Mostre a barra no painel onde a tarefa começou. Ao abrir ou fechar um dobrável, a barra continua do ponto em que estava, sem reiniciar ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html)).

## Recursos

### Relacionados

- Carregamento e espera
- Spinner
- Skeleton
- Toasts
- Upload de arquivo

### Referências

- [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators) Apple HIG
- [Gauges](https://developer.apple.com/design/human-interface-guidelines/gauges) Apple HIG
- [Loading](https://developer.apple.com/design/human-interface-guidelines/loading) Apple HIG
- [Loading](https://www.gov.br/ds/components/loading) gov.br DS
- [Scrim](https://www.gov.br/ds/components/scrim) gov.br DS
- [Progress bar](https://fluent2.microsoft.design/components/web/react/core/progressbar/usage) Fluent 2
- [Wait UX](https://fluent2.microsoft.design/wait-ux) Fluent 2
- [Progress](https://vercel.com/geist/progress) Geist
- [Gauge](https://vercel.com/geist/gauge) Geist
- [Progress bar](https://blueprintjs.com/docs/#core/components/progress-bar) Blueprint
- [Designing for foldables](https://developer.samsung.com/one-ui/largescreen-and-foldable/designing_for_foldable.html) One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta o anel circular determinado, o bloqueio de região ou tela com scrim, o anúncio de início e fim em região viva e as unidades por extenso. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                       |
