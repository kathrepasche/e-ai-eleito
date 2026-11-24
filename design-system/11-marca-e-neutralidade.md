# Marca e neutralidade

Esta seção reúne as decisões próprias do E aí, Eleito?. Ela prevalece sobre as seções herdadas do Trama quando houver conflito.

## Decisões da marca

| Id | Decisão |
| --- | --- |
| EE1 | A identidade muda a família de marca (azul-tinta), os neutros (papel e grafite), o grifo, a tipografia (Space Grotesk e Inter) e os raios. Texto, foco e status vêm do Trama, com contraste remedido sobre o papel. |
| EE2 | Votos nunca usam verde ou vermelho. Os ícones de voto mudam só a forma, com rótulo em texto. |
| EE3 | Todos os políticos aparecem no mesmo formato e com o mesmo peso visual. O presidente aparece como sugestão, e o cargo pode ser ocultado. |
| EE4 | O amarelo `t-mark` nunca é cor de texto. Em grifo, cobre a palavra inteira, com `t-mark-fg` por cima. |
| EE5 | Argumentos a favor e contra de uma proposta têm o mesmo tamanho e aparecem sempre na mesma ordem. |
| EE6 | Listas de candidatos ficam em ordem alfabética. Nada de ranking, pódio ou recomendação de voto. |
| EE7 | Toda votação e decisão mostrada tem link para a fonte oficial e passa por revisão humana antes de publicar. |
| EE8 | Texto corrido nunca abaixo de 16px no produto. |

## Tom de voz por situação

| Situação | Exemplo |
| --- | --- |
| Cargo vazio | "Por aqui, nenhum senador sabe que você está de olho. Ainda." |
| Silêncio | "Faz 30 dias que não fala de segurança. E aí, eleito?" |
| Falta | "Faltou à votação de quarta." |
| Cobrança | "E aí, Marina? Cobre direto" |
| Mensagem pronta | Sempre uma pergunta educada, nunca uma acusação. |
| Erro de formulário | Direto e sem humor: "Confira o e-mail: parece que falta algo." |

## Páginas principais

- **Início**: faixa grafite (`.tr-inverse`) com "Na urna aparece FIM. Pra gente, é só o começo."
- **Tô de olho**: barra de cargos fixa (`.ee-cargos`), uma seção por cargo, cards de político (`.ee-politico`).
- **Perfil do político**: panorama, placar de votos (`.ee-placar`), histórico filtrável por pauta, área de cobrança (`.ee-cobrar`).
- **Cargos**: o que cada cargo faz e o que não é com ele.
- **Modo eleição "Fica ou troca?"**: balanço do mandato, formulário com explicação da proposta (`.ee-proposta`) e comparativo em tabela (`.tr-table`).
