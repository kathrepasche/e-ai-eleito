# Toasts

Um toast é uma mensagem breve que aparece num canto fixo da janela para confirmar o resultado de uma ação sem interromper a tarefa.

O toast surge sobre a página, não bloqueia nada e não recebe o foco. É o retorno certo para "Arquivo salvo" ou "Convite enviado": a pessoa percebe que a ação deu certo e segue trabalhando. No Trama, só o toast informativo sem ação some sozinho. Toasts com ação, de aviso ou de erro ficam até a pessoa fechar ou resolver. Como alguns somem, o toast só carrega informação útil e relevante que não seja crítica ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/toast/usage)).

**Use um toast** para confirmar ações iniciadas pela pessoa (salvar, mover, arquivar), oferecer Desfazer logo após uma ação reversível e acompanhar uma tarefa longa em segundo plano, como um envio de arquivos.

**Não use um toast** para erros que a pessoa precisa investigar, falhas de pagamento ou permissões negadas: esses casos pedem uma mensagem na página, com o passo de recuperação ([Geist](https://vercel.com/geist/toast)). Erros de campo ficam junto ao campo, com resumo de erros. Decisões críticas vão num diálogo ([DKFDS](https://designsystem.dk/komponenter/toastbesked/)). Avisos que a pessoa precisa consultar depois vão para o painel de notificações. Não confirme ações rotineiras cujo efeito já está visível na tela, como marcar uma caixa de seleção.

## Anatomia

1.  **Ícone** (opcional): indica a intenção (informação, sucesso, aviso, erro ou progresso).
2.  **Título** (obrigatório): uma frase curta em peso 600.
3.  **Corpo** (opcional): próximo passo ou detalhe, em `--t-fg-2`.
4.  **Ação** (opcional): no máximo um botão, como Desfazer ou Abrir.
5.  **Fechar**: obrigatório em todo toast que não some sozinho. Opcional no toast informativo sem ação.

Os toasts vivem numa área própria, a torradeira, que define a posição, o empilhamento e a camada `--z-2`.

## Tipos

| Tipo                 | Exemplo                                                | Duração                                                                               |
|----------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------|
| Informativo sem ação | "Projeto arquivado", "Ana mencionou você em Orçamento" | Some após no mínimo 7 segundos, com a contagem pausada em hover e foco.               |
| Com ação             | "Mensagem excluída" + Desfazer                         | Permanece até a pessoa agir ou fechar.                                                |
| Progresso            | "Enviando 6 arquivos"                                  | Permanece até a tarefa terminar e então vira toast informativo, ou de erro se falhar. |
| Aviso                | "3 de 5 convites enviados"                             | Permanece até a pessoa fechar.                                                        |
| Erro                 | "Não foi possível salvar o rascunho"                   | Permanece até a pessoa fechar ou a ação ser refeita.                                  |

A duração mínima de 7 segundos segue o padrão do [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/toast/usage). Toasts com ação, de aviso ou de erro não somem sozinhos, para atender ao critério de tempo ajustável (WCAG 2.2, 2.2.1), que o [DKFDS](https://designsystem.dk/komponenter/toastbesked/) também exige.

> **Divergência entre referências** O gov.br DS recomenda evitar mensagens que desaparecem automaticamente, porque podem passar despercebidas ([gov.br DS](https://www.gov.br/ds/components/message)). O Fluent 2 fecha toasts depois de 7 segundos por padrão. O Trama fica com a síntese da decisão D23: só o toast informativo sem ação some sozinho, com no mínimo 7 segundos e pausa em hover e foco, e o mesmo conteúdo fica disponível no painel de notificações. Tudo o que pede ação, avisa ou relata erro permanece. A versão 1.0 deixava o toast com Desfazer sumir quando a pessoa iniciava outra ação e aceitava toast de erro que sumia; as duas regras foram retiradas.

## Boas práticas

**Escolha a intenção pelo que a pessoa viveu.** Trate uma implantação cancelada pela própria pessoa como informação neutra e uma ação concluída só em parte como aviso ([Geist](https://vercel.com/geist/toast)).

**Pause o tempo enquanto a pessoa interage.** Hover ou foco no toast congelam a contagem; ao sair, ela recomeça ([Blueprint](https://blueprintjs.com/docs/#core/components/toast)).

**Empilhe no máximo quatro.** O toast novo entra na borda e empurra os antigos para o centro, com `--sp-400` entre eles ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/toast/usage)). Se a ordem importa, inclua o horário ([DKFDS](https://designsystem.dk/komponenter/toastbesked/)).

**Não narre um fluxo com vários toasts.** Emita um toast no fim, de sucesso ou de erro, ou use um único toast de progresso ([Geist](https://vercel.com/geist/toast)). Agrupe processos simultâneos parecidos: "Enviando 6 arquivos" ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/toast/usage)). Interrupções frequentes prejudicam principalmente pessoas com deficiência cognitiva e visual ([gov.br DS](https://www.gov.br/ds/components/message)).

**Garanta outro caminho para tudo que o toast oferece.** A ação no toast é um atalho: Desfazer também existe no menu ou com Ctrl+Z, e a mensagem perdida aparece no painel de notificações ([HDS](https://hds.hel.fi/components/notification)). Nunca coloque navegação principal num toast ([Geist](https://vercel.com/geist/toast)).

**Use toasts com moderação.** Eles passam rápido de úteis a invasivos ([DKFDS](https://designsystem.dk/komponenter/toastbesked/)). Confirme só ações importantes; a pessoa espera que ações rotineiras funcionem ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/feedback)).

**Faça** confirme com substantivo e particípio, sem "com sucesso".

**Não faça** mostre um problema crítico num toast sem saída, com tom informal.

### Estados e comportamento

- **Entrada e saída**: desliza da borda em `--m-normal` com `--m-ease-enter` e sai em `--m-fast` com `--m-ease-exit`. Com `prefers-reduced-motion` ou com as animações desligadas no produto, aparece e some com troca de opacidade apenas.
- **Progresso**: use barra determinada com porcentagem quando o tempo é previsível e spinner quando não é; nunca os dois no mesmo toast ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/toast/usage)).
- **Erro de ação transitória**: aceitável num toast quando curto e com o passo seguinte ("Não foi possível salvar. Tente de novo."); ele permanece até ser fechado. Se o erro exige investigação, use uma mensagem na página ([Geist](https://vercel.com/geist/toast)).
- **Fechamento**: ao fechar pelo botão, o foco volta ao elemento que estava ativo antes ([HDS](https://hds.hel.fi/components/notification/accessibility), [gov.br DS](https://www.gov.br/ds/components/message)).

## Conteúdo

**Confirmações: diga o que mudou.** Substantivo e particípio: "Arquivo salvo", "Domínio adicionado". Não escreva "com sucesso" nem use exclamação ([Geist](https://vercel.com/geist/toast), [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/toast/usage)).

**Progresso: gerúndio e objeto.** "Enviando arquivo", "Exportando relatório" ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/toast/usage)).

**Erros: duas frases, a segunda com a saída.** "Não foi possível verificar o domínio. Tente de novo." ([Geist](https://vercel.com/geist/toast)). Tom neutro, sem "Ops" e sem culpar a pessoa.

**Use o mesmo verbo do botão que originou a ação.** Botão "Excluir projeto", toast "Projeto excluído" ([Geist](https://vercel.com/geist/toast)).

**Seja curto.** Título em uma linha, corpo com até 60 caracteres e rótulo de botão com uma ou duas palavras ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/toast/usage)). O toast nunca passa de três linhas ([One UI](https://developer.samsung.com/one-ui/comp/toast.html)), e o texto quebra em vez de ser truncado. O botão de reverter se chama sempre "Desfazer".

## Acessibilidade

- A torradeira é uma região viva criada no carregamento da página. Toasts de informação, sucesso e progresso usam `role="status"` (anúncio educado); toasts de aviso e erro usam `role="alert"` ([Geist](https://vercel.com/geist/toast)).
- O toast não rouba o foco ([Blueprint](https://blueprintjs.com/docs/#core/components/toast)). Ofereça um atalho de teclado documentado para chegar à torradeira quando houver ação.
- O produto pode tocar um som curto ao exibir um toast de erro, como sinal adicional para quem usa tecnologia assistiva ([gov.br DS](https://www.gov.br/ds/components/message)). O som é opcional, desligável nas configurações e nunca é o único sinal.
- Não use toasts que somem para mensagens críticas ou longas: o leitor de tela pode não terminar a leitura ([HDS](https://hds.hel.fi/components/notification/accessibility)).
- A intenção nunca depende só da cor: título e ícone dizem o mesmo (WCAG 2.2, 1.4.1). O botão Fechar e a ação têm alvo de `--c-touch` no toque.

## Tokens usados

| Elemento                               | Token                                                       |
|----------------------------------------|-------------------------------------------------------------|
| Superfície                             | `--t-surface-raised`, `--r-lg`                              |
| Elevação e camada                      | `--e-4`, `--z-2`                                            |
| Preenchimento                          | `--sp-300`, `--sp-400`                                      |
| Espaço entre toasts e margem da janela | `--sp-400`                                                  |
| Título e corpo                         | `--t-fg-1`, `--t-fg-2`                                      |
| Ícones de intenção                     | `--t-info`, `--t-success`, `--t-warning-fill`, `--t-danger` |
| Movimento                              | `--m-normal`, `--m-fast`, `--m-ease-enter`, `--m-ease-exit` |

## Considerações por plataforma

### Web desktop

Posicione a torradeira no canto inferior direito, a `--sp-400` das bordas, com largura de até 360px. Mantenha a mesma posição em todo o produto; se houver um painel de notificações, alinhe a torradeira ao lado onde ele abre ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/toast/usage)). Como fica em `--z-2`, a torradeira nunca cobre um cabeçalho fixo nem um diálogo aberto.

### Web móvel

Na classe Compacta, centralize o toast na parte inferior, com a largura da tela menos as margens, acima da barra de navegação inferior (a posição inferior central também é usada pelo [HDS](https://hds.hel.fi/components/notification)). Mostre um toast por vez. O botão de ação tem alvo mínimo de `--c-touch`.

### Tablets e dobráveis

Nas classes Média e Expandida, volte ao canto inferior direito. Em layouts de dois painéis, ancore o toast ao painel onde a ação aconteceu. Em dobráveis no modo Flex, evite que o toast caia sobre a dobra.

## Recursos

### Relacionados

- Mensagens e banners
- Feedback
- Notificações
- Desfazer e refazer
- Indicadores de progresso

### Referências

- [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback) Apple HIG
- [Message](https://www.gov.br/ds/components/message) gov.br DS
- [Notification](https://www.gov.br/ds/components/notification) gov.br DS
- [Toast](https://fluent2.microsoft.design/components/web/react/core/toast/usage) Fluent 2
- [Toast](https://vercel.com/geist/toast) Geist
- [Toast](https://blueprintjs.com/docs/#core/components/toast) Blueprint
- [Toastbesked](https://designsystem.dk/komponenter/toastbesked/) DKFDS
- [Notification](https://hds.hel.fi/components/notification) Helsinki Design System
- [Notification: accessibility](https://hds.hel.fi/components/notification/accessibility) Helsinki Design System
- [Toasts](https://developer.samsung.com/one-ui/comp/toast.html) One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                             |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Aplica a decisão D23 (só o toast informativo sem ação some sozinho), torna o Fechar obrigatório nos toasts persistentes, acrescenta os tipos aviso e erro, a camada, o som opcional e o retorno do foco ao fechar. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                      |
