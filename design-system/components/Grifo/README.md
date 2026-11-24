# Grifo

O grifo destaca, como um marca-texto, a palavra que a pessoa precisa ver primeiro.

**Quando usar.** Em títulos e frases curtas, para marcar o número ou o tema que resume a informação: "Tô de olho em 3 políticos", "nenhuma palavra sobre segurança".

**Quando não usar.** Para avisos e erros, use uma mensagem (`.tr-msg`). Para resultados de pesquisa no meio de um texto, use `.tr-mark`. Para dar ênfase a uma frase inteira, reescreva a frase.

## Anatomia

1. **Fundo**: `t-mark`, o amarelo marca-texto, com raio `r-sm`.
2. **Texto**: `t-mark-fg`, nos dois temas. O grifo cobre a palavra inteira, para que nenhuma parte da letra fique sobre o fundo da página com contraste baixo.

## Boas práticas

**Use no máximo um grifo por bloco de conteúdo.** Dois grifos competem e nenhum se destaca.

**Grife o fato, nunca um julgamento.** Grife "3 votações" ou "segurança"; nunca grife adjetivos sobre um político.

**Nunca use o amarelo como cor de texto.** Amarelo sobre fundo claro não atinge o contraste mínimo (WCAG 2.2, 1.4.3).

## Acessibilidade

O grifo é só visual. Se o destaque carrega significado, ele precisa estar também no texto.

## Tokens

`t-mark`, `t-mark-fg`, `r-sm`.
