# Ícones de voto

Os ícones de voto mostram como o político se posicionou numa votação, sempre ao lado do texto.

**Quando usar.** Em cards, históricos, placares e tabelas comparativas, para indicar voto a favor, voto contra, abstenção, falta ou discurso.

**Quando não usar.** Para status de sistema (sucesso, erro, alerta), use as mensagens e badges do kit. Sozinhos, sem rótulo, eles não são suficientes.

## Anatomia

1. **Ícone**: círculo de `icon-md`, contorno `stroke-thick` em `currentColor`.
2. **Rótulo**: texto obrigatório ao lado, em peso 600.

## Tipos

| Tipo | Classe | Forma |
| --- | --- | --- |
| A favor | `.ee-voto--sim` | Círculo cheio com check |
| Contra | `.ee-voto--nao` | Círculo vazado com X |
| Abstenção | `.ee-voto--abst` | Círculo vazado com traço |
| Falta | `.ee-voto--falta` | Círculo tracejado vazio |
| Discurso | `.ee-voto--fala` | Balão |

## Boas práticas

**Diferencie os votos pela forma, nunca pela cor.** Todos os ícones usam a mesma cor de texto. Verde para "sim" e vermelho para "não" sugerem que um voto é certo e o outro errado, e isso quebra a neutralidade do produto.

**Sempre mostre o rótulo.** A informação não pode depender só da forma ou da cor (WCAG 2.2, 1.4.1).

**Use "A favor" e "Contra" no histórico e "Sim" e "Não" em tabelas estreitas.**

## Acessibilidade

O ícone leva `aria-hidden="true"`; o rótulo em texto é o que o leitor de tela anuncia.

## Tokens

`icon-md`, `stroke-thick`, `t-fg-1`, `t-bg`.
