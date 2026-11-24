# Chip de pauta

O chip de pauta permite escolher os temas que a pessoa quer acompanhar e filtrar listas por tema.

**Quando usar.** No cadastro ("O que importa pra você?"), no perfil do político para filtrar o histórico e no formulário do Modo eleição.

**Quando não usar.** Para escolher uma única opção entre poucas, use radio ou controle segmentado. Para remover itens já aplicados, use `.tr-chip` com botão de remover.

## Anatomia

1. **Pílula** com raio `r-pill` e altura mínima `c-touch`.
2. **Estado selecionado**: fundo `t-fg-1`, texto `t-bg` e check no amarelo `t-mark`.

## Boas práticas

**No cadastro, de 3 a 5 pautas, ou "Todas as pautas"**, como um botão separado acima dos chips.

**O estado selecionado muda forma e preenchimento**, não só a cor.

## Acessibilidade

Cada chip é um `<button>` com `aria-pressed`. O grupo fica dentro de um `<fieldset>` com `<legend>` quando faz parte de um formulário.

## Tokens

`r-pill`, `c-touch`, `t-border-control`, `t-fg-1`, `t-bg`, `t-mark`.
