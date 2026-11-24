# MenuDeContexto

Um menu de contexto dá acesso rápido a ações ligadas a um item, aberto com o botão direito, com toque longo ou com a tecla de menu.

O menu de contexto oferece atalhos sem poluir a interface. Por ficar oculto, as pessoas podem não saber que ele existe ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)). Por isso o Trama o trata como atalho: toda ação dele também existe na interface visível. Visualmente, ele usa a mesma superfície do menu (`.tr-menu`), posicionada no ponto do clique, e segue o padrão dropdown do gov.br: superfície flutuante temporária, na camada dos flutuantes, que fecha ao concluir o objetivo, com Esc ou com clique fora ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). O gov.br não tem um componente de menu de contexto; as regras de superfície, fechamento e teclado do padrão dropdown valem aqui.

**Quando usar.** Para atalhos de uso frequente sobre uma linha de tabela, um arquivo, um card ou um objeto num canvas ([Geist](https://vercel.com/geist/context-menu)), especialmente em aplicações de trabalho que as pessoas usam por muito tempo.

**Quando não usar.** Como único caminho para uma ação; nesse caso, ofereça um botão ou um menu com gatilho visível ([Geist](https://vercel.com/geist/context-menu)). Para comandos globais da aplicação, use uma paleta de comandos ou a barra de ferramentas. Em páginas de serviço público e formulários de etapa única, onde as pessoas não esperam o botão direito, não use.

## Anatomia

1.  **Alvo**: o item ou a área sobre a qual a pessoa abriu o menu. O alvo fica destacado com `--t-brand-subtle` enquanto o menu está aberto.
2.  **Superfície**: `.tr-menu`, com `--e-4`, `--r-lg` e camada `--z-2`, ancorada no ponto do ponteiro.
3.  **Itens**: rótulos de até duas palavras, três quando inevitável; ícones opcionais e uniformes no grupo.
4.  **Separadores**: até três grupos.
5.  **Título** (raro): só quando esclarece o efeito, por exemplo “3 arquivos selecionados” ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)).

## Boas práticas

**Inclua só o que é relevante para o item.** O menu de contexto reúne os comandos mais prováveis naquele contexto. Deixe opções avançadas ou raras de fora ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)).

**Mantenha poucos itens e no máximo cerca de três grupos.** Menus longos são difíceis de varrer e rolar ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)).

**Ofereça as mesmas ações na interface principal.** Toda ação do menu de contexto aparece também num botão de linha, num menu visível ou na barra de ferramentas. Assim quem usa só mouse ou só teclado tem as mesmas possibilidades ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus), [Geist](https://vercel.com/geist/context-menu)).

**Seja consistente em toda a aplicação.** Se alguns itens têm menu de contexto e outros parecidos não, a pessoa não sabe onde o recurso existe e pode achar que há um defeito ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)).

**Oculte itens que não se aplicam.** O menu de contexto mostra só as ações relevantes ao item clicado ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)). Não mostre itens esmaecidos: como o menu já é calculado para aquele alvo, um comando que não se aplica sai da lista (decisão D9).

> **Divergência entre referências** A HIG admite manter recortar, copiar e colar esmaecidos no menu de contexto, porque as pessoas esperam encontrá-los ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)). A versão 1.0 do Trama seguia essa exceção. Pela decisão D9, que proíbe item desabilitado sem explicação em menus, o Trama retira esses itens quando não se aplicam; o menu nativo do navegador continua disponível em campos de texto, onde a pessoa espera copiar e colar.

**Limite submenus a um nível.** Mais de um nível complica a navegação. Dê ao submenu um título que antecipe o conteúdo ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)). Não esconda ações destrutivas dentro de submenus ([Geist](https://vercel.com/geist/context-menu)).

**Ponha ações destrutivas no fim, depois de um separador.** Identifique-as com `.tr-danger-item` e confirme antes de executar ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus), [Geist](https://vercel.com/geist/context-menu)).

**Não mostre atalhos de teclado.** O menu de contexto já é um atalho; os atalhos aparecem nos menus principais ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)).

**Faça** Mostre poucas ações, todas sobre o item clicado, com a destrutiva separada no fim.

**Não faça** Misture ações do item com comandos globais e deixe a ação destrutiva no meio da lista.

### Comportamento

**Abra com o botão direito no desktop e com toque longo em telas de toque.** Suprima o menu nativo do navegador apenas na área do alvo, nunca na página inteira ([Geist](https://vercel.com/geist/context-menu)). O Blueprint também implementa o menu de contexto como um popover ligado ao clique com botão direito no alvo ([Blueprint](https://blueprintjs.com/docs/#core/components/context-menu)).

**Posicione no ponteiro, sem criar espaço.** Se o menu ultrapassar a janela, inverta primeiro na horizontal e depois na vertical ([Geist](https://vercel.com/geist/context-menu)). A superfície usa só o espaço visível e nunca faz surgir barra de rolagem na página ([gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). Quando ele abre acima do alvo, considere inverter a ordem dos itens para que os mais usados fiquem mais perto do ponto de abertura ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)).

**Feche ao ativar um item, com Esc e com clique fora.** Não feche quando o ponteiro sai do menu ([Geist](https://vercel.com/geist/context-menu)). Não use véu: o menu de contexto é um atalho leve e não bloqueia o resto da tela.

**Considere criar objetos a partir de um espaço vazio.** Um menu de contexto aberto entre itens pode oferecer “Nova pasta” ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)).

**Aplique a ação a toda a seleção.** Com vários itens selecionados, o menu age sobre todos, e o título informa a quantidade.

## Conteúdo

Os itens seguem as regras de Menus: verbo no infinitivo e objeto, sem artigo, como “Abrir em nova aba” ou “Copiar link” ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)); caixa de frase; reticências só quando o item abre um diálogo, como “Renomear…” ([Geist](https://vercel.com/geist/context-menu)). Nunca trunque um item: se não couber, ele quebra a linha (decisão D15). Use os mesmos ícones das ações equivalentes no resto da aplicação, como copiar, compartilhar e excluir ([HIG](https://developer.apple.com/design/human-interface-guidelines/context-menus)). Escreva a ação destrutiva com verbo e objeto, como “Excluir arquivo”.

## Acessibilidade

**Abra também pelo teclado.** A tecla de menu e Shift+F10 abrem o mesmo menu sobre o item focado ([Geist](https://vercel.com/geist/context-menu)).

**Navegue como num menu comum.** Setas para cima e para baixo movem o foco, Enter ou Espaço ativam, Esc fecha e devolve o foco ao item de origem ([Geist](https://vercel.com/geist/context-menu), [gov.br DS](https://www.gov.br/ds/padroes/design/dropdown)). O foco do item de origem volta com o anel completo, porque o retorno resulta de uma tecla da pessoa. Use `role="menu"` e `menuitem`, e dê à superfície um `aria-label` que nomeie o alvo.

**Exponha ações ocultas para outras formas de entrada.** Se ações de um item aparecem só no hover ou no foco, ofereça-as também num menu de contexto, para pessoas que usam controle por voz, rastreamento ocular ou acionadores ([Fluent](https://fluent2.microsoft.design/components/web/react/core/nav/usage)). O inverso também vale: o menu de contexto nunca é o único caminho.

**Não dependa de gestos.** O toque longo é difícil para parte das pessoas e não é descoberto por todas. A ação equivalente visível resolve os dois problemas (WCAG 2.2, 2.5.1).

## Tokens usados

| Token                                   | Uso                                          |
|-----------------------------------------|----------------------------------------------|
| `--t-surface-raised`, `--e-4`, `--r-lg` | Superfície do menu                           |
| `--t-brand-subtle`                      | Destaque do alvo enquanto o menu está aberto |
| `--o-hover`                             | Camada de hover do item                      |
| `--z-2`                                 | Camada dos flutuantes                        |
| `--t-danger`                            | Item destrutivo                              |
| `--t-border-subtle`                     | Separadores                                  |
| `--m-fast`, `--m-ease-enter`            | Aparição do menu                             |

## Considerações por plataforma

### Web desktop

É o contexto principal do componente. Abra com o botão direito e com o clique secundário do trackpad. Mantenha o menu nativo do navegador disponível em campos de texto e links, onde as pessoas esperam copiar e colar.

### Web móvel

Abra com toque longo sobre o item e mostre os itens em densidade baixa, com altura de `--c-touch`. Em listas, o toque longo também pode iniciar a seleção múltipla; escolha um dos dois comportamentos e use o mesmo em toda a aplicação. Ofereça sempre um botão “Mais opções” visível na linha, porque o toque longo é pouco descoberto.

### Tablets e dobráveis

Em telas de toque, segurar um item da lista abre um menu suspenso, sem título, com opções adicionais para aquele item ([One UI](https://developer.samsung.com/one-ui/comp/dialog.html)). Com trackpad ou mouse conectado, o clique secundário abre o mesmo menu. Mantenha o menu perto do item tocado ([One UI](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html)).

## Recursos

### Relacionados

- Menus
- Barra de ferramentas
- Mouse e trackpad
- Toque e gestos

### Referências

- [Dropdown (Elemento Flutuante)](https://www.gov.br/ds/padroes/design/dropdown) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus) Apple HIG
- [Context Menu](https://vercel.com/geist/context-menu) Geist
- [Context Menu](https://blueprintjs.com/docs/#core/components/context-menu) Blueprint
- [Nav: usage](https://fluent2.microsoft.design/components/web/react/core/nav/usage) Fluent 2
- [Dialog](https://developer.samsung.com/one-ui/comp/dialog.html) Samsung One UI
- [Designing for large screens](https://developer.samsung.com/one-ui/largescreen-and-foldable/intro.html) Samsung One UI

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                              |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Aplica as regras de superfície, fechamento e teclado do padrão dropdown, retira itens esmaecidos (D9) e proíbe truncar itens (D15). |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                       |
