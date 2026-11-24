# Paginacao

A paginação divide uma lista longa em páginas e permite ir para a anterior, a próxima ou uma página específica.

Use a paginação para percorrer resultados de pesquisa, listas de casos, registros de uma tabela e conteúdos divididos em várias páginas ([GOV.UK](https://design-system.service.gov.uk/components/pagination/), [gov.br DS](https://www.gov.br/ds/components/pagination)). É um componente de navegação sequencial ([gov.br DS](https://www.gov.br/ds/padroes/design/navegacao)). O gov.br organiza a paginação em módulos: setas, identificadores de página, reticências, exibição (itens por página), informação (intervalo) e atalho (ir para a página) ([gov.br DS](https://www.gov.br/ds/components/pagination)). No Trama, o componente é o `.tr-pagination` com itens `.tr-page-btn`; a página atual usa fundo `--t-brand`.

**Quando usar.** Quando mostrar tudo deixaria o carregamento lento, quando a maioria só precisa das primeiras páginas ([GOV.UK](https://design-system.service.gov.uk/components/pagination/)) e quando a pessoa precisa saber o tamanho do conjunto ou chegar ao fim. O HDS indica páginas com mais de 36 itens por vista, pelo menos três páginas ou total desconhecido ([HDS](https://hds.hel.fi/components/pagination)).

**Quando não usar.** Com uma única página, não mostre a paginação ([GOV.UK](https://design-system.service.gov.uk/components/pagination/)). Para fluxos lineares, use o botão “Continuar” e o link de voltar, ou o indicador de etapas. Para listas em que a pessoa não precisa ir ao fim, use um botão secundário “Mostrar mais” ([gov.br DS](https://www.gov.br/ds/components/pagination), [HDS](https://hds.hel.fi/components/pagination)).

## Anatomia

1.  **Contêiner**: `<nav>` com nome, como “Paginação dos resultados”.
2.  **Anterior e Próxima** (obrigatórios): links nas pontas, com texto e seta ([gov.br DS](https://www.gov.br/ds/components/pagination)).
3.  **Identificadores de página**: links só com números, altura `--d-control` e largura mínima igual à altura. Com três dígitos ou mais, o item cresce na horizontal, como a pílula do gov.br ([gov.br DS](https://www.gov.br/ds/components/pagination)).
4.  **Página atual**: fundo `--t-brand`, texto `--t-on-brand` em peso 600 e `aria-current="page"`.
5.  **Reticências** (opcional): indicam páginas omitidas entre a primeira e a última.
6.  **Itens por página** (opcional): select que define o tamanho da página.
7.  **Intervalo** (opcional): texto com o intervalo exibido e o total.
8.  **Ir para a página** (opcional): select com todas as páginas, a atual selecionada ([gov.br DS](https://www.gov.br/ds/components/pagination)).

## Tipos

| Tipo            | Uso                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Padrão          | No fim do conteúdo da tela, centralizada, com os identificadores sempre visíveis ([gov.br DS](https://www.gov.br/ds/components/pagination)).                                                                                                                    |
| Contextual      | Integrada a uma tabela ou a uma lista de cards. Só Anterior e Próxima são obrigatórios; itens por página, intervalo e ir para a página são opcionais e cada módulo pode alinhar ao início ou ao fim ([gov.br DS](https://www.gov.br/ds/components/pagination)). |
| Entre conteúdos | Guias divididos em páginas: Anterior e Próxima empilhados, com o título da página vizinha ([GOV.UK](https://design-system.service.gov.uk/components/pagination/), [Geist](https://vercel.com/geist/pagination)).                                                |
| Compacta        | Classe Compacta: Anterior, Próxima, primeira e última, com “Página 5 de 100” no centro ([DKFDS](https://designsystem.dk/komponenter/paginering/)).                                                                                                              |
| Mostrar mais    | Botão secundário no fim da lista; enquanto carrega, um indicador ocupa o lugar dos novos itens ([gov.br DS](https://www.gov.br/ds/components/pagination), [Geist](https://vercel.com/geist/load-more-button)).                                                  |

## Boas práticas

**Mostre sempre a página atual, a primeira e a última.** A primeira e a última dão noção do tamanho do conjunto ([DKFDS](https://designsystem.dk/komponenter/paginering/), [GOV.UK](https://design-system.service.gov.uk/components/pagination/)).

**Com até sete páginas, mostre todas.** A partir de oito, use reticências depois da primeira, antes da última ou nos dois lugares, conforme a posição da página atual ([DKFDS](https://designsystem.dk/komponenter/paginering/), [gov.br DS](https://www.gov.br/ds/components/pagination)). No tamanho mínimo, limite os identificadores a quatro ([gov.br DS](https://www.gov.br/ds/components/pagination)).

**Mantenha a largura constante.** Mostre sempre a mesma quantidade de elementos, seja qual for a página atual ([HDS](https://hds.hel.fi/components/pagination)). Ao avançar para uma página vizinha, só o destaque muda de lugar ([gov.br DS](https://www.gov.br/ds/components/pagination)).

**Ofereça atalhos em listas longas.** Permita saltar para a última página ou para qualquer página sem passar pelas intermediárias ([gov.br DS](https://www.gov.br/ds/components/pagination)). Use o módulo “Ir para a página” ou as reticências interativas.

**Reticências interativas, com cuidado.** No gov.br, o botão de reticências abre uma lista das páginas ocultas, com rolagem acima de quatro itens; ao escolher uma, a paginação se reorganiza com a página atual no centro ([gov.br DS](https://www.gov.br/ds/components/pagination)). No Trama, as reticências são texto oculto da leitura por padrão; use a versão interativa só quando não houver o módulo “Ir para a página”, como botão com nome que diga o intervalo, “Escolher entre as páginas 2 e 97”.

> **Divergência entre referências** O gov.br torna as reticências um botão que abre a lista de páginas ocultas ([gov.br DS](https://www.gov.br/ds/components/pagination)). O HDS trata as reticências como decoração, sem nome acessível ([HDS](https://hds.hel.fi/components/pagination/accessibility)), e GOV.UK e DKFDS as mostram como texto ([GOV.UK](https://design-system.service.gov.uk/components/pagination/), [DKFDS](https://designsystem.dk/komponenter/paginering/)). A versão 1.0 do Trama proibia a interação. O Trama passa a aceitar a versão interativa como alternativa ao atalho, porque ela atende a recomendação de acesso direto a qualquer página, e mantém o texto como padrão, posição da maioria e opção com menos paradas de Tab.

**Oculte Anterior na primeira página e Próxima na última.** ([GOV.UK](https://design-system.service.gov.uk/components/pagination/), [DKFDS](https://designsystem.dk/komponenter/paginering/), [Geist](https://vercel.com/geist/pagination)). O HDS mantém os dois sempre visíveis ([HDS](https://hds.hel.fi/components/pagination)); o Trama oculta, porque um link sem destino só ocupa espaço, e mantém a largura constante reservando o espaço.

**Aplique filtros e ordenação à lista inteira.** Depois de filtrar, ordenar ou mudar os itens por página, volte para a primeira página do novo resultado ([GOV.UK](https://design-system.service.gov.uk/components/pagination/)). Redirecione endereços de páginas que não existem mais para a primeira.

**Evite rolagem infinita.** Ela causa problemas para quem usa teclado ([GOV.UK](https://design-system.service.gov.uk/components/pagination/)) e impede chegar ao rodapé. O gov.br apresenta a rolagem automática como forma de paginação vertical ([gov.br DS](https://www.gov.br/ds/components/pagination)); o Trama não a adota, pelo critério de acessibilidade, e oferece o botão “Mostrar mais”.

**Faça** Na primeira página, oculte Anterior e mostre a última página para dar a dimensão da lista.

**Não faça** Esconda o total de páginas e use setas sem texto e sem nome acessível.

### Estados

Repouso, hover, pressionado, foco e atual ([gov.br DS](https://www.gov.br/ds/components/pagination)). Hover e pressionado são camadas `--o-hover` e `--o-pressed` sobre a cor do item, como no gov.br, que usa as opacidades de superfície ([gov.br DS](https://www.gov.br/ds/components/pagination)). A página atual não tem hover. Não há item desabilitado: Anterior e Próxima somem nas pontas.

### Densidade

Use a densidade padrão (itens de `--c-h-md`) na maioria dos casos; a baixa (`--c-h-lg`) na classe Compacta e em toque; a alta (`--c-h-sm`) dentro de tabelas e outros componentes operados com mouse ([gov.br DS](https://www.gov.br/ds/components/pagination)). O gov.br vai de 24px a 40px; o Trama sobe um passo em cada nível para manter 32px como menor altura com mouse e 44px de área de ação no toque.

### Comportamento

Cada página tem endereço próprio, para permitir voltar, recarregar e compartilhar. Ao trocar de página, decida para onde vai o foco: às vezes para o início dos resultados; em muitos casos, é melhor não mover ([HDS](https://hds.hel.fi/components/pagination/accessibility)). Com carregamento sem recarregar, anuncie o novo intervalo numa região `aria-live`. As listas de “Itens por página” e “Ir para a página” seguem o padrão dropdown e fecham com Esc ([gov.br DS](https://www.gov.br/ds/components/pagination)).

## Conteúdo

Use “Anterior” e “Próxima” com texto e seta. Na paginação entre conteúdos, use o título da página vizinha como rótulo ([Geist](https://vercel.com/geist/pagination)). Mostre o número da página no `<title>` do documento, como “Resultados da pesquisa (página 2 de 4)” ([GOV.UK](https://design-system.service.gov.uk/components/pagination/)). Escreva o intervalo por extenso, com separador de milhar: “Mostrando 41 a 60 de 1.982 processos” ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy)). Os rótulos dos módulos são “Itens por página” e “Ir para a página”, ao lado do campo.

## Acessibilidade

**Envolva em `<nav>` com nome e use o elemento certo.** Links `<a>` para as páginas, `<button>` para ações, como as reticências interativas, e select para os atalhos ([gov.br DS](https://www.gov.br/ds/components/pagination)).

**Dê nome a cada número.** Use “Página 3” e indique a última, como “Página 100, última página” ([HDS](https://hds.hel.fi/components/pagination/accessibility), [DKFDS](https://designsystem.dk/komponenter/paginering/)). O gov.br sugere “Ir para a página 1” ([gov.br DS](https://www.gov.br/ds/components/pagination)); o Trama prefere o nome mais curto, que começa pelo que é visível e é o mesmo em HDS e DKFDS (WCAG 2.2, 2.5.3).

**Marque a atual com `aria-current="page"`.** E destaque-a além da cor, com fundo preenchido e peso 600 (WCAG 2.2, 1.4.1).

**Teclado.** Tab e Shift+Tab percorrem os itens; Enter e Espaço ativam; nas listas, setas para cima e para baixo; Esc fecha ([gov.br DS](https://www.gov.br/ds/components/pagination)).

**Dê texto aos controles de ícone.** Setas sem texto, na paginação contextual ou compacta, levam nome acessível e tooltip ([DKFDS](https://designsystem.dk/komponenter/paginering/)).

## Tokens usados

| Token                              | Uso                                                      |
|------------------------------------|----------------------------------------------------------|
| `--t-brand`, `--t-on-brand`        | Página atual                                             |
| `--o-hover`, `--o-pressed`         | Hover e pressionado                                      |
| `--t-fg-1`                         | Números e rótulos                                        |
| `--c-h-sm`, `--c-h-md`, `--c-h-lg` | Altura dos itens por densidade                           |
| `--sp-100`, `--sp-200`, `--sp-400` | Espaço entre itens; margem interna; espaço entre módulos |
| `--r-md`                           | Raio dos itens                                           |
| `--t-focus`                        | Anel de foco                                             |

## Considerações por plataforma

### Web desktop

Mostre a primeira, a última, a atual e pelo menos uma vizinha de cada lado ([GOV.UK](https://design-system.service.gov.uk/components/pagination/)). Em tabelas, use o tipo contextual com itens por página e intervalo.

### Web móvel

Mantenha a paginação numa linha, centralizada ([DKFDS](https://designsystem.dk/komponenter/paginering/), [gov.br DS](https://www.gov.br/ds/components/pagination)). Na classe Compacta, use densidade baixa e o tipo compacto; reduza identificadores com reticências e oculte os módulos menos relevantes do tipo contextual ([gov.br DS](https://www.gov.br/ds/components/pagination)).

### Tablets e dobráveis

Em layouts de dois painéis, a paginação fica no pé do painel da lista e muda só a lista; o detalhe aberto permanece. Ao abrir o dobrável e passar de Compacta para Média, troque o tipo compacto pelo padrão, mantendo a página atual.

> **Nota** A HIG não tem paginação numerada. O controle de página da HIG, uma fileira de pontos, representa páginas de uma lista plana; a HIG desaconselha mais de cerca de 10 pontos ([HIG](https://developer.apple.com/design/human-interface-guidelines/page-controls)). O Trama não usa pontos para paginar listas.

## Recursos

### Relacionados

- Tabelas
- Pesquisa
- Estruturar a navegação
- Carregamento e espera

### Referências

- [Pagination (Paginação)](https://www.gov.br/ds/components/pagination) gov.br DS
- [Navegação](https://www.gov.br/ds/padroes/design/navegacao) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls) Apple HIG
- [Pagination](https://design-system.service.gov.uk/components/pagination/) GOV.UK Design System
- [Paginering](https://designsystem.dk/komponenter/paginering/) DKFDS
- [Pagination](https://hds.hel.fi/components/pagination) Helsinki Design System
- [Pagination: accessibility](https://hds.hel.fi/components/pagination/accessibility) Helsinki Design System
- [Pagination](https://vercel.com/geist/pagination) Geist
- [Load More Button](https://vercel.com/geist/load-more-button) Geist

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Torna a paginação modular (itens por página, intervalo, ir para a página), acrescenta o tipo contextual, as reticências interativas opcionais, o crescimento do identificador com três dígitos e as densidades. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                   |
