# Tabelas

Uma tabela organiza dados em linhas e colunas para que as pessoas encontrem valores específicos, os comparem e ajam sobre os registros.

Elas são exigentes para quem usa tecnologia assistiva; antes de criar uma, confirme que ela é necessária ([HDS](https://hds.hel.fi/components/table/accessibility)) e prefira tabelas simples, com um nível de cabeçalho ([gov.br DS](https://www.gov.br/ds/components/table)).

O componente `.tr-table` estiliza a tabela HTML nativa. A barra de título, a barra contextual, a ordenação, a seleção, a expansão de linha, a pesquisa e a paginação são camadas opcionais em volta dela.

## Quando usar

- Para comparar informação em linhas e colunas ([GOV.UK](https://design-system.service.gov.uk/components/table/)).
- Quando a pessoa precisa achar um valor específico ou comparar itens segundo vários parâmetros ([DKFDS](https://designsystem.dk/komponenter/tables/)).
- Para selecionar registros e agir sobre eles em lote, em sistemas de gestão.
- Como alternativa textual de um gráfico.

## Quando não usar

- **Para montar layout.** Use a grade ([GOV.UK](https://design-system.service.gov.uk/components/table/)).
- **Para um único parâmetro.** Use uma lista ([DKFDS](https://designsystem.dk/komponenter/tables/)). O HDS sugere outro formato com menos de 4 linhas ou menos de 3 colunas ([HDS](https://hds.hel.fi/components/table)).
- **Quando o ponto principal é um padrão, como uma evolução.** Use um gráfico ([DKFDS](https://designsystem.dk/komponenter/tables/)).
- **Para pares de chave e valor de um objeto.** Use a lista de resumo ([Geist](https://vercel.com/geist/table)).

## Anatomia

1.  **Barra de título (opcional).** Título da tabela em uma linha e até quatro ações utilitárias lado a lado; com mais de quatro, as demais vão para um menu "Mais ações" ([gov.br DS](https://www.gov.br/ds/components/table)). Use `.tr-table-bar`. Sem barra, use `<caption>`.
2.  **Barra contextual (opcional).** Aparece logo abaixo da barra de título quando há linhas selecionadas, com a contagem e as ações que valem para a seleção ([gov.br DS](https://www.gov.br/ds/components/table)). Use `.tr-table-bar--context`.
3.  **Cabeçalho da tabela (obrigatório).** Nomeia o conteúdo de cada coluna, com a unidade.
4.  **Linhas.** Dados, elementos interativos, seleção no início e expansão.
5.  **Colunas.** A largura acompanha o conteúdo ([gov.br DS](https://www.gov.br/ds/components/table)).
6.  **Rodapé de totais (opcional).** Linha de total em `<tfoot>` ([Ontario](https://designsystem.ontario.ca/components/detail/tables.html)).
7.  **Barra de paginação (opcional).** Paginação com escolha de linhas por página, abaixo da tabela ([gov.br DS](https://www.gov.br/ds/components/table)).

## Tipos

| Variação                        | Uso                                                                                                                                                                                                      |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Zebrada                         | Só em tabelas longas, com muitas linhas e colunas ([DKFDS](https://designsystem.dk/komponenter/tables/), [HDS](https://hds.hel.fi/components/table)).                                                    |
| Com colunas ou linhas agrupadas | Só quando não for possível simplificar. Separe os grupos com bordas mais fortes (`--stroke-thick`) e use `scope="colgroup"` ou `scope="rowgroup"` ([gov.br DS](https://www.gov.br/ds/components/table)). |
| Ordenável                       | Cabeçalhos ordenáveis viram botões `.tr-sort`.                                                                                                                                                           |
| Com seleção                     | Checkbox no início de cada linha e no cabeçalho, com barra contextual.                                                                                                                                   |
| Com linha expansível            | Mostra conteúdo complementar da linha sem sair da tabela.                                                                                                                                                |

## Boas práticas

**Alinhe texto à esquerda, números e valores monetários à direita e ícones ao centro.** Identificadores, telefones, CEPs e datas, que não se somam, ficam à esquerda ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy), [Ontario](https://designsystem.ontario.ca/components/detail/tables.html)). Alinhe o cabeçalho como a coluna.

**Formate números no padrão brasileiro.** Ponto como separador de milhar e vírgula decimal, com o mesmo número de casas na coluna ([gov.br DS](https://www.gov.br/ds/padroes/writing/microcopy), [DKFDS](https://designsystem.dk/komponenter/tables/)). Use algarismos tabulares (classe `.num`).

**Coloque a unidade no cabeçalho.** Não repita "min" ou "R\$" em cada célula ([Ontario](https://designsystem.ontario.ca/components/detail/tables.html)).

**Um valor por célula e nenhuma célula vazia.** Escreva "Não informado", "0" ou "Não se aplica", conforme o caso ([gov.br DS](https://www.gov.br/ds/components/table), [Ontario](https://designsystem.ontario.ca/components/detail/tables.html)).

**Quebre a linha nas células; trunque só quando o espaço for fixo.** O conteúdo das células quebra linha por padrão ([gov.br DS](https://www.gov.br/ds/components/table)). Se truncar, use `.tr-truncate`, deixe pelo menos três caracteres da palavra e ofereça o texto completo em tooltip focável.

### Ordenação

**Ordene por um parâmetro por vez.** A pessoa ordena uma coluna de cada vez; a coluna ordenada mostra o estado ativo e a seta no sentido da ordem ([gov.br DS](https://www.gov.br/ds/components/table)). O primeiro clique ordena em ordem crescente e o seguinte inverte. O `<th>` ordenado leva `aria-sort="ascending"` ou `"descending"`; colunas ordenáveis sem ordem ativa mostram a seta dupla de `.tr-sort` e não levam `aria-sort`. Cabeçalhos não ordenáveis não usam a cor de interação.

**Mantenha sempre uma ordenação ativa.** Uma tabela ordenável começa ordenada, em geral pela primeira coluna ou por uma data ([DKFDS](https://designsystem.dk/komponenter/tables/)). Com paginação, a ordem vale para todas as páginas e volta à página 1. Em tabelas com colunas agrupadas, só as colunas do nível mais próximo das linhas são ordenáveis ([gov.br DS](https://www.gov.br/ds/components/table)).

> **Divergência entre referências** O gov.br alterna o cabeçalho entre três estados: sem ordenação, crescente e decrescente ([gov.br DS](https://www.gov.br/ds/components/table)). O DKFDS exige que a tabela ordenável tenha sempre uma ordenação ativa ([DKFDS](https://designsystem.dk/komponenter/tables/)). Nenhuma das fontes cita pesquisa. O Trama adota dois estados, crescente e decrescente, porque a ordem padrão de uma tabela também é uma ordenação e precisa estar declarada em `aria-sort` para quem usa leitor de tela.

### Seleção

**Selecione com checkbox no início da linha.** A linha selecionada recebe o estado selecionado. Com algumas linhas marcadas, o checkbox do cabeçalho fica intermediário; com todas, marcado ([gov.br DS](https://www.gov.br/ds/components/table)). O estado intermediário é a propriedade `indeterminate` do checkbox, definida por script.

**Mostre as ações da seleção na barra contextual.** Ela aparece abaixo da barra de título com a contagem, como "2 linhas selecionadas", e as ações em lote ([gov.br DS](https://www.gov.br/ds/components/table)). Anuncie a contagem em `role="status"` e mantenha o foco no checkbox que a pessoa marcou. Ações que não dependem de seleção, como Baixar, ficam sempre na barra de título.

> **Divergência entre referências** O DKFDS deixa os botões de ação em lote sempre visíveis e, quando nada está selecionado, explica o que fazer se a pessoa os acionar ([DKFDS](https://designsystem.dk/komponenter/tables/)). O gov.br mostra essas ações numa barra contextual que surge com a seleção ([gov.br DS](https://www.gov.br/ds/components/table)), e o HDS põe as ações em lote acima da tabela ([HDS](https://hds.hel.fi/components/table)). O Trama adota a barra contextual, que evita botões desabilitados (D9), e compensa a mudança de interface anunciando a contagem em região viva.

### Linha expansível

**Coloque o indicador de expansão no início da linha.** O fim da linha costuma ter outros botões ([gov.br DS](https://www.gov.br/ds/padroes/design/collapse)). Chevron para baixo na linha recolhida e para cima na expandida; o conteúdo expandido fica numa linha logo abaixo, com sombra interna que marca a hierarquia (`.tr-row-expanded`) ([gov.br DS](https://www.gov.br/ds/components/table)).

**Mantenha o conteúdo expandido simples.** Prefira texto ou uma lista; não coloque tabelas, cards ou outros componentes complexos dentro da linha ([gov.br DS](https://www.gov.br/ds/components/table)).

### Pesquisa na tabela

**Abra a pesquisa a partir da barra de título.** O botão Pesquisar mostra o campo sobre a barra de título, com um botão Fechar ao lado. Enquanto a pessoa digita, a tabela mostra só as linhas que contêm o termo e destaca as ocorrências ([gov.br DS](https://www.gov.br/ds/components/table)). Marque as ocorrências com `<mark class="tr-mark">` e anuncie a quantidade de resultados em `aria-live="polite"` ([DKFDS](https://designsystem.dk/komponenter/tables/)).

### Estados e comportamento

- **Hover de linha**: camada `--t-surface-1`. Em tabelas longas sem interação, o hover ajuda a acompanhar a linha; o cursor continua o padrão ([gov.br DS](https://www.gov.br/ds/components/table)).
- **Linha selecionada**: checkbox marcado e fundo `--t-brand-subtle`.
- **Vazio**: o estado vazio substitui a estrutura inteira (cabeçalho, linhas, colunas e paginação), para que a pessoa não leia informação irrelevante ([gov.br DS](https://www.gov.br/ds/padroes/design/emptystates), [Geist](https://vercel.com/geist/table)). Se o vazio veio de pesquisa ou filtro, mantenha a barra de título e ofereça "Limpar filtros".
- **Carregando**: linhas de skeleton com as colunas finais.
- **Rolagem vertical**: em tabelas longas dentro de uma área com altura limitada, a barra de título, o cabeçalho e a paginação ficam fixos e só as linhas rolam ([gov.br DS](https://www.gov.br/ds/components/table)). O cabeçalho fixo ganha sombra quando há linhas por baixo, como em `.tr-scroll`.
- **Rolagem horizontal**: barra de título e paginação ficam fixas e o conteúdo rola; uma sombra na borda indica que há mais colunas ([gov.br DS](https://www.gov.br/ds/components/table), [HDS](https://hds.hel.fi/components/table)).

### Densidade

A densidade afeta toda a estrutura da tabela, linhas e colunas ([gov.br DS](https://www.gov.br/ds/components/table)). Com `data-density`, o preenchimento vertical das células (`--d-cell-y`) é `--sp-150` na alta, `--sp-300` na padrão e `--sp-400` na baixa. A alta só vale com apontador fino, para otimizar telas com muitos dados; a baixa é obrigatória no toque.

**Faça** alinhe valores à direita, com a unidade no cabeçalho, separador de milhar e casas decimais iguais.

**Não faça** alinhar números à esquerda, repetir a moeda em cada célula e variar as casas decimais.

## Conteúdo

- Escreva o título da tabela em uma linha: o que ela mostra, o recorte e o período ([gov.br DS](https://www.gov.br/ds/components/table)).
- Use nomes de coluna curtos, de preferência menores que os dados; "Data inicial" e "Data final" podem virar "Início" e "Fim" quando o título já diz que são datas ([gov.br DS](https://www.gov.br/ds/components/table)). O cabeçalho é lido em cada célula pelo leitor de tela ([HDS](https://hds.hel.fi/components/table/accessibility)).
- Abreviações de unidade (min, h, kB) só nas células, com a unidade nomeada no cabeçalho.
- Rotule as ações com até duas palavras: Pesquisar, Baixar, Excluir.

## Acessibilidade

**Use sempre a estrutura semântica.** `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>` e `<td>` ([gov.br DS](https://www.gov.br/ds/components/table)), com `scope="col"` e `scope="row"` ([GOV.UK](https://design-system.service.gov.uk/components/table/)) (WCAG 2.2, 1.3.1).

**Dê nome à tabela.** Use `<caption>` ou o título da barra referenciado por `aria-labelledby` ([HDS](https://hds.hel.fi/components/table/accessibility)).

**Só os controles entram na ordem de Tab.** Checkboxes, botões de expansão, cabeçalhos ordenáveis e links recebem foco em ordem de leitura; células de dados não são focáveis, e quem usa leitor de tela percorre as células com os comandos de tabela. Torne o contêiner de rolagem focável com `tabindex="0"`, `role="region"` e nome ([HDS](https://hds.hel.fi/components/table/accessibility)).

> **Divergência entre referências** O gov.br orienta navegar de célula em célula com a tecla Tab ([gov.br DS](https://www.gov.br/ds/components/table)). O HDS torna focável só o contêiner de rolagem ([HDS](https://hds.hel.fi/components/table/accessibility)). Pelo critério de acessibilidade, o Trama não põe células na ordem de Tab: uma tabela com muitas células obrigaria quem navega por teclado a centenas de paradas, e os leitores de tela já oferecem navegação por célula.

**Dê nome aos controles das linhas.** Inclua o identificador da linha no nome acessível: "Selecionar protocolo 1834", "Detalhes do protocolo 1834" ([gov.br DS](https://www.gov.br/ds/components/table)). O botão de expansão usa `aria-expanded` e `aria-controls`.

**Cabeçalhos ordenáveis são botões.** O rótulo visível não muda; a seta é decorativa e o estado vai em `aria-sort` no `<th>` ([gov.br DS](https://www.gov.br/ds/components/table), [Geist](https://vercel.com/geist/table)).

## Tokens usados

| Elemento                                            | Token                                                       |
|-----------------------------------------------------|-------------------------------------------------------------|
| Fundo das células e da barra de título              | `--t-surface-raised`                                        |
| Fundo do cabeçalho, hover de linha, linha expandida | `--t-surface-1`                                             |
| Barra contextual, linha selecionada                 | `--t-brand-subtle`                                          |
| Texto do cabeçalho, das células                     | Body small 14/20 peso 600 `--t-fg-2`; Body small `--t-fg-1` |
| Linha sob o cabeçalho, entre registros              | `--t-border`, `--t-border-subtle`                           |
| Preenchimento das células                           | `--d-cell-y` vertical, `--sp-400` horizontal                |
| Sombra do cabeçalho fixo e da linha expandida       | `--t-shadow-key`, camada `--z-1`                            |
| Ocorrência da pesquisa                              | `--t-mark`, `--t-mark-fg`                                   |
| Raio do contêiner                                   | `--r-lg`                                                    |

## Considerações por plataforma

### Web desktop

Permita redimensionar colunas quando os dados variam de largura ([HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)). Fixe cabeçalho e paginação na rolagem vertical em tabelas longas.

### Web móvel

Na classe Compacta, a tabela rola na horizontal dentro do contêiner, e as ações das barras de título e contextual se agrupam em um único menu ([gov.br DS](https://www.gov.br/ds/components/table)). Ofereça pesquisa e paginação para reduzir o que a pessoa precisa percorrer ([gov.br DS](https://www.gov.br/ds/components/table)). Para dados que não se comparam, uma lista de cards pode substituir a tabela ([HDS](https://hds.hel.fi/components/table)). Use densidade baixa.

### Tablets e dobráveis

Em janela média, priorize as colunas essenciais e leve as demais para a linha expandida ou para o detalhe. Em layouts de dois painéis, a tabela vai no painel principal e o detalhe da linha atual no secundário ([HIG](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)).

## Recursos

### Relacionados

- Listas
- Lista de resumo
- Paginação
- Estados vazios
- Densidade
- Excesso de conteúdo

### Referências

- [Table](https://www.gov.br/ds/components/table) gov.br DS
- [Padrão Collapse](https://www.gov.br/ds/padroes/design/collapse) gov.br DS
- [Empty States](https://www.gov.br/ds/padroes/design/emptystates) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables) Apple HIG
- [Table](https://design-system.service.gov.uk/components/table/) GOV.UK Design System
- [Tabeller](https://designsystem.dk/komponenter/tables/) DKFDS
- [Table](https://hds.hel.fi/components/table) Helsinki Design System
- [Table: accessibility](https://hds.hel.fi/components/table/accessibility) Helsinki Design System
- [Tables](https://designsystem.ontario.ca/components/detail/tables.html) Ontario Design System
- [Table](https://vercel.com/geist/table) Geist

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                                                                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Entram a barra de título com até 4 ações, a barra contextual de seleção, o checkbox intermediário, a linha expansível com indicador no início (D8), a pesquisa com destaque, a ordenação por um parâmetro, cabeçalho e paginação fixos, densidades (D11) e o estado vazio que substitui a estrutura. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                                                                                                                        |
