# Skeleton

Um skeleton reserva o espaço e imita a forma do conteúdo que ainda está chegando, para que a página apareça na hora e não salte quando os dados chegam.

A melhor experiência de carregamento termina antes de a pessoa perceber. Quando não dá, mostre algo o quanto antes: uma tela em branco parece defeito ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/loading)). O skeleton desenha blocos neutros nas posições de títulos, linhas de texto, imagens e linhas de tabela. A pessoa entende a estrutura da página antes do conteúdo e já pode usar o que carregou.

**Use um skeleton** quando dados assíncronos preenchem um layout conhecido e a espera passa de um segundo: linhas de tabela, grades de cards, blocos de perfil, listas ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/skeleton/usage), [Geist](https://vercel.com/geist/skeleton)).

**Não use um skeleton** quando a estrutura do conteúdo é desconhecida; use spinner ou barra de progresso. Não use em processos longos, em elementos fixos do layout como abas e barras de aplicativo ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/skeleton/usage)), nem como decoração permanente ou substituto de um estado vazio ([Geist](https://vercel.com/geist/skeleton)). Para uma única ação em andamento, use spinner. Para atualizar uma região que já tem conteúdo, mantenha o conteúdo à vista e use o bloqueio de região com spinner (`.tr-region-busy`), que esmaece o que está atrás ([gov.br DS](https://www.gov.br/ds/components/loading)).

## Anatomia

1.  **Blocos**: retângulos em `--t-surface-2` com raio que imita o elemento final.
2.  **Brilho** (onda): faixa mais clara em `--t-border-subtle` que atravessa os blocos em laço.
3.  **Região**: o contêiner que agrupa os blocos e informa o carregamento às tecnologias assistivas.

Mostre só a estrutura essencial. Um skeleton de pessoa mostra avatar, nome e cargo, sem detalhes como o indicador de presença ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/skeleton/usage)).

## Tipos

| Forma          | Raio       | Imita                                                                             |
|----------------|------------|-----------------------------------------------------------------------------------|
| Linha de texto | `--r-md`   | Títulos e parágrafos. Altura igual à altura de linha do estilo tipográfico final. |
| Pílula         | `--r-pill` | Avatares, badges e chips.                                                         |
| Arredondado    | `--r-md`   | Botões e campos.                                                                  |
| Quadrado       | `--r-lg`   | Imagens e miniaturas, com o mesmo raio do card.                                   |

Escolha a forma conforme o elemento que vai aparecer ([Geist](https://vercel.com/geist/skeleton)). O Trama usa a animação de onda, que o [Fluent 2](https://fluent2.microsoft.design/components/web/react/core/skeleton/usage) recomenda como padrão por dar a transição mais suave quando muitos blocos aparecem juntos.

## Boas práticas

**Use as medidas do conteúdo final.** Um bloco de 200 por 20 que vira um texto de 80 por 16 parece falha. Mantenha largura e altura para que nada se desloque quando os dados chegam ([Geist](https://vercel.com/geist/skeleton)). Isso também evita mudanças de layout que tiram a pessoa do lugar.

**Varie a largura das linhas de texto.** Linhas de comprimentos diferentes, com a última mais curta, leem como parágrafo; linhas iguais leem como tabela.

**Peça os dados ao mesmo tempo.** Requisições simultâneas evitam que partes da página surjam em momentos diferentes. Se o carregamento escalonado for inevitável, sincronize a animação de todos os blocos para a página não parecer agitada ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/skeleton/usage)).

**Mantenha utilizável o que já carregou.** O skeleton substitui só a região que espera; navegação e ações da página continuam ativas ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/loading)).

**Use o skeleton só na primeira carga.** Ele substitui conteúdo que ainda não existe. Ao recarregar dados que a pessoa já está vendo, trocar o conteúdo por blocos apaga o que ela lia; prefira manter o conteúdo e indicar a atualização com spinner ou bloqueio de região, que no gov.br DS corresponde ao scrim de inibição sobre uma área temporariamente indisponível ([gov.br DS](https://www.gov.br/ds/components/scrim)).

**Não coloque controles focáveis dentro do skeleton.** Se um botão ou campo é coberto pelo efeito, desative-o ou tire-o da ordem de tabulação com `tabindex="-1"` ([Blueprint](https://blueprintjs.com/docs/#core/components/skeleton), [Geist](https://vercel.com/geist/skeleton)).

**Faça** imite a forma e o ritmo do texto que vai chegar.

**Não faça** use um único bloco genérico que não diz nada sobre a estrutura.

### Estados e comportamento

- **Carregando**: os blocos aparecem imediatamente, sem atraso, porque reservar espaço evita saltos.
- **Revelação**: troque o skeleton pelo conteúdo com um esmaecimento curto de `--m-fast`, mantendo as dimensões.
- **Falha**: se os dados não chegarem, substitua o skeleton por uma mensagem de erro na mesma região, com a ação de tentar de novo.
- **Sem dados**: se a resposta vier vazia, mostre o estado vazio, nunca o skeleton.
- **Movimento reduzido**: com `prefers-reduced-motion`, os blocos ficam estáticos ([Geist](https://vercel.com/geist/skeleton)). O mesmo vale quando a pessoa desliga as animações não essenciais no controle do próprio produto.
- **Espera longa**: se o carregamento passa do esperado, acrescente um texto de status e, quando o sistema permitir, a opção de cancelar e voltar à tarefa anterior ([gov.br DS](https://www.gov.br/ds/components/loading)).

## Conteúdo

O skeleton não tem texto visível. O nome acessível da região diz o que está carregando, por exemplo "Pedidos recentes, carregando". Quando a espera passa de alguns segundos, acrescente fora dos blocos um texto curto como "Pesquisando pedidos …" ([Fluent 2](https://fluent2.microsoft.design/wait-ux)). Esse texto descreve o que está acontecendo para quem não vê os blocos ([gov.br DS](https://www.gov.br/ds/components/loading)).

## Acessibilidade

- Marque a região com `aria-busy="true"` durante o carregamento e volte para `false` quando todos os blocos forem substituídos, para que o leitor de tela espere o conjunto completo ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/skeleton/usage)).
- Anuncie o fim do carregamento com `aria-live="polite"` no contêiner de destino, não nos blocos; a conclusão precisa chegar a quem usa tecnologia assistiva ([gov.br DS](https://www.gov.br/ds/components/loading)) ([Geist](https://vercel.com/geist/skeleton)). Use poucas regiões vivas, só para blocos grandes ou importantes ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/skeleton/usage)).
- Os blocos são decorativos e não recebem foco. Ao terminar o carregamento, não mova o foco da pessoa ([Fluent 2](https://fluent2.microsoft.design/components/web/react/core/skeleton/usage)).
- Respeite `prefers-reduced-motion`; o brilho em laço não pisca, não usa variações intensas de cor e não ultrapassa três flashes por segundo ([gov.br DS](https://www.gov.br/ds/components/loading); WCAG 2.2, 2.3.1).

> **Divergência entre referências** O gov.br DS não tem componente de skeleton: trata todo carregamento com o componente Loading, determinado ou indeterminado, e com scrim quando bloqueia uma área ([gov.br DS](https://www.gov.br/ds/components/loading)). Fluent 2, Geist e Blueprint documentam o skeleton para layouts conhecidos. Pelo critério de convergência, o Trama mantém o skeleton na primeira carga de layouts conhecidos e adota do gov.br as regras de acessibilidade do carregamento e o bloqueio de região para atualizações.

## Tokens usados

| Elemento              | Token                           |
|-----------------------|---------------------------------|
| Bloco                 | `--t-surface-2`                 |
| Brilho da onda        | `--t-border-subtle`             |
| Raios                 | `--r-md`, `--r-lg`, `--r-pill`  |
| Espaço entre linhas   | `--sp-300`                      |
| Curva da onda         | `--m-linear`                    |
| Revelação do conteúdo | `--m-fast`, `--m-ease-standard` |

Os dois tokens de cor mudam com o tema; no modo escuro, o bloco continua um pouco mais claro que a superfície.

## Considerações por plataforma

### Web desktop

Em tabelas, mostre o cabeçalho real e o skeleton apenas nas linhas, com a quantidade de linhas que a primeira página costuma ter.

### Web móvel

Mostre blocos suficientes para preencher a primeira tela, não a lista inteira. Em redes lentas, o skeleton evita a tela em branco enquanto a primeira resposta chega.

### Tablets e dobráveis

O skeleton segue a grade da classe de janela atual: duas colunas de cards numa tela, três na outra. Se o dobrável abrir durante o carregamento, redesenhe o skeleton para o novo layout em vez de esticar o anterior.

## Recursos

### Relacionados

- Carregamento e espera
- Spinner
- Indicadores de progresso
- Estados vazios
- Cards

### Referências

- [Loading](https://developer.apple.com/design/human-interface-guidelines/loading) Apple HIG
- [Loading](https://www.gov.br/ds/components/loading) gov.br DS
- [Scrim](https://www.gov.br/ds/components/scrim) gov.br DS
- [Skeleton](https://fluent2.microsoft.design/components/web/react/core/skeleton/usage) Fluent 2
- [Wait UX](https://fluent2.microsoft.design/wait-ux) Fluent 2
- [Skeleton](https://vercel.com/geist/skeleton) Geist
- [Skeleton](https://blueprintjs.com/docs/#core/components/skeleton) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                      |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Restringe o skeleton à primeira carga, indica o bloqueio de região para atualizações, acrescenta a espera longa com Cancelar e as regras de acessibilidade do carregamento. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                               |
