# Explicação da proposta

A explicação da proposta conta, em linguagem simples, o que uma votação muda e os principais argumentos dos dois lados.

**Quando usar.** No formulário "O que você pensa" do Modo eleição e na página de uma votação, aberta pelo botão "Entender a proposta".

**Quando não usar.** Para o texto oficial completo, leve à fonte oficial da Câmara ou do Senado com um link.

## Anatomia

1. **Gatilho**: botão "Entender a proposta" / "Fechar explicação" com `aria-expanded`.
2. **Lista de definição** (`<dl>`): "O que muda", "Quem é a favor diz", "Quem é contra diz".
3. **Rodapé**: resultado no Congresso e link para a fonte oficial.

## Boas práticas

**Os argumentos a favor e contra têm o mesmo tamanho e aparecem sempre na mesma ordem.**

**Sem adjetivos e sem conclusão.** A explicação nunca diz qual lado está certo.

**Todo texto passa por revisão humana antes de publicar.**

## Acessibilidade

O gatilho é um `<button>` com `aria-expanded` e `aria-controls` apontando para a explicação.

## Tokens

`t-surface-1`, `r-lg`, `sp-400`, `sp-200`.
