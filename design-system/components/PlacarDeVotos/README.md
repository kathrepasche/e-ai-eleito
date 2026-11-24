# Placar de votos

O placar de votos mostra, no perfil do político, quantas vezes ele votou a favor, contra, se absteve ou faltou, e em quais votações.

**Quando usar.** Na seção "Como votou" do perfil de deputados e senadores.

**Quando não usar.** Para o presidente, que não vota, use a lista de decisões. Para comparar vários políticos, use a tabela comparativa.

## Anatomia

1. **Barra de proporção**: segmentos em `t-fg-1` (a favor), `t-fg-3` (contra), `t-brand` (abstenção) e vazio (falta), com raio `r-pill`.
2. **Linhas expansíveis**: uma por tipo de voto, com ícone, rótulo e número em `t-font-display`; abrem a lista das votações.

## Boas práticas

**A barra nunca está sozinha.** Os números e as listas abaixo dela carregam a informação; a barra só dá a proporção num relance.

**Liste da votação mais recente para a mais antiga**, com data, pauta e resultado.

**Informe que votações simbólicas não entram**, porque não registram voto individual.

## Acessibilidade

A barra leva `role="img"` e um `aria-label` com os números. As linhas usam `<details>` e `<summary>` nativos.

## Tokens

`t-fg-1`, `t-fg-3`, `t-brand`, `t-surface-2`, `r-pill`, `r-lg`, `t-font-display`.
