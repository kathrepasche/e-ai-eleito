# Card do político

O card do político resume, na página Tô de olho, o que um político fez na semana nas pautas da pessoa.

**Quando usar.** Um card por político acompanhado, dentro da seção do cargo dele.

**Quando não usar.** Para o histórico completo, use o perfil do político. Para comparar políticos, use a tabela comparativa (`.tr-table`).

## Anatomia

1. **Topo**: avatar com iniciais (`.tr-avatar`), nome em `t-font-display`, cargo, partido e UF em `t-fg-3`, ação "Tirar o olho".
2. **Resumo**: uma frase com o número que importa em negrito.
3. **Itens**: ícone de voto, data e pauta, e a frase em linguagem simples.
4. **Aviso de silêncio** (`.ee-silencio`), quando houver.
5. **Ações**: "Ver histórico completo" e "Cobrar".

## Boas práticas

**Todos os cards têm o mesmo formato e o mesmo peso visual**, de qualquer partido ou cargo.

**Escreva o fato, não o julgamento.** "Faltou à votação", nunca "deputada faltosa".

**Mostre só as pautas que a pessoa escolheu.** Sem votações nas pautas dela, diga isso: "Nenhuma votação das suas pautas nesta semana".

## Conteúdo

Botões: "Ver histórico completo", "Cobrar", "Tirar o olho". Para o presidente, "Ver todas as decisões".

## Acessibilidade

O botão "Tirar o olho" leva `aria-label="Parar de ficar de olho em [nome]"`, porque a brincadeira não se explica fora de contexto. O card é um `<article>` com o nome como título.

## Tokens

`t-surface-raised`, `t-border-subtle`, `r-lg`, `sp-500`, `t-font-display`, `t-fg-3`.
