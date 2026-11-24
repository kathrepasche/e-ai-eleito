# Aviso de silêncio

O aviso de silêncio mostra quando um político não discursou nem apresentou projeto sobre uma pauta da pessoa num período.

**Quando usar.** No card do político e no perfil, quando a ausência de manifestação sobre uma pauta escolhida é informação relevante.

**Quando não usar.** Para erros e alertas do sistema, use `.tr-msg`. Para faltas em votação, use o ícone de voto "Faltou".

## Anatomia

1. **Contêiner**: fundo `t-warning-subtle`, borda `t-warning-border`, raio `r-lg`.
2. **Texto**: período e pauta em negrito; termina com o bordão "E aí, eleito?" quando couber.

## Boas práticas

**Sempre diga o período.** "Faz 30 dias", "nos últimos 3 meses".

**Silêncio é dado, não acusação.** Não use palavras como "sumiu" ou "omisso" no aviso.

**No máximo um aviso por card**, com até duas pautas.

## Tokens

`t-warning-subtle`, `t-warning-border`, `r-lg`, `sp-300`, `sp-400`.
