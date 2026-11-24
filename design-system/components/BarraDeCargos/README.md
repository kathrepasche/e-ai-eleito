# Barra de cargos

A barra de cargos fica fixa no topo da página Tô de olho e leva a pessoa à seção de cada cargo.

**Quando usar.** Na página Tô de olho, acima das seções de cargo.

**Quando não usar.** Para filtrar conteúdo por pauta, use chips de pauta (`.ee-pauta`). Para navegação principal do site, use o cabeçalho.

## Anatomia

1. **Barra**: fixa (`position: sticky`), fundo `t-bg`, divisor `t-border-subtle`, rolagem horizontal no celular.
2. **Botões de cargo**: pílula `r-pill`, altura mínima `c-touch`.
3. **Contador**: quantos políticos a pessoa acompanha naquele cargo. Cargos ainda sem acompanhamento não mostram contador.

## Boas práticas

**Mostre sempre todos os cargos, na mesma ordem**: Presidente, Senadores, Deputados federais, Deputados estaduais, Vereadores. Um cargo oculto pela pessoa sai da barra e pode voltar em Preferências.

**Marque a seção visível com `aria-current="true"`.**

## Acessibilidade

A barra é um `<nav aria-label="Cargos">`. Cada botão tem alvo de toque de pelo menos 44 x 44px (`c-touch`).

## Tokens

`t-bg`, `t-border-subtle`, `t-surface-raised`, `t-fg-1`, `r-pill`, `c-touch`, `z-1`.
