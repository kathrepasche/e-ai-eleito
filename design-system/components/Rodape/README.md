# Rodape

O rodapé fecha a página com informações que a pessoa espera encontrar no fim: responsável, contato, mapa do site e avisos legais.

O rodapé é o lugar para onde muita gente rola quando se sente perdida ou não acha o que procura ([HDS](https://hds.hel.fi/components/footer)). Ele ajuda a pessoa a se localizar e oferece serviços úteis e informações complementares ([gov.br](https://www.gov.br/ds/components/footer)). No Trama, o componente é o `.tr-footer`, usado dentro de `.tr-inverse` para a versão escura.

**Quando usar.** No fim de todas as páginas do produto, abaixo do `<main>` ([GOV.UK](https://design-system.service.gov.uk/components/footer/), [HDS](https://hds.hel.fi/components/footer), [DKFDS](https://designsystem.dk/komponenter/footer/)).

**Quando não usar.** Não coloque no rodapé conteúdo que a pessoa não vai procurar ali, como notícias ou textos de ajuda de uma tarefa: quase ninguém os encontra no fim da página ([DKFDS](https://designsystem.dk/komponenter/footer/)). Ajuda contextual vai perto da tarefa; veja Oferecer ajuda.

## Anatomia

O rodapé se organiza em quatro áreas, todas opcionais exceto o contêiner ([gov.br](https://www.gov.br/ds/components/footer)). O HDS usa quatro seções equivalentes: navegação, utilidades, personalizada e base ([HDS](https://hds.hel.fi/components/footer)).

1.  **Área de logo**: logo do produto ou do órgão, alinhado ao início. Mais de um logo só quando todos identificam a solução em uso ([gov.br](https://www.gov.br/ds/components/footer)).
2.  **Mapa do site**: `.tr-footer__map`, um conjunto de listas com um título por categoria.
3.  **Informações secundárias**: redes sociais, ações de utilidade (contato, voltar ao topo) e logos de parceiros ou assinaturas ([gov.br](https://www.gov.br/ds/components/footer), [HDS](https://hds.hel.fi/components/footer)).
4.  **Informação legal**: `.tr-footer__legal`, separada das outras áreas por uma borda `--t-border`, com o responsável pelo produto, direitos e links de privacidade, acessibilidade, cookies e termos.

## Tipos

| Tipo             | Uso                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Simples          | Só a informação legal. Sistemas internos e fluxos lineares, nos quais não convém tirar a pessoa da tarefa ([GOV.UK](https://design-system.service.gov.uk/components/footer/)). |
| Com mapa do site | Portais e sites com várias seções. O HDS recomenda no mínimo navegação e base ([HDS](https://hds.hel.fi/components/footer)).                                                   |
| Completo         | Mapa do site, informações secundárias e informação legal.                                                                                                                      |
| Compacto de erro | Informação legal e, se útil, redes sociais. Usado em páginas de erro ([gov.br](https://www.gov.br/ds/templates/erro)).                                                         |

Cada tipo existe em fundo claro e escuro ([gov.br](https://www.gov.br/ds/components/footer), [HDS](https://hds.hel.fi/components/footer)). Para o fundo escuro no tema claro, envolva o rodapé em `.tr-inverse`, que redefine os tokens alias para os valores escuros (D27). Não pinte o rodapé com cores fixas.

## Boas práticas

**Inclua sempre o responsável, o contato e os avisos obrigatórios.** O rodapé informa o órgão ou a empresa responsável, como obter suporte, a declaração de acessibilidade e as informações de cookies ([DKFDS](https://designsystem.dk/komponenter/footer/)). Diga quem detém os direitos sobre o conteúdo e se ele pode ser reutilizado ([GOV.UK](https://design-system.service.gov.uk/components/footer/)). Em produtos para o público brasileiro, o link de privacidade leva à política de tratamento de dados exigida pela LGPD (D25).

**Use nomes curtos e previsíveis nos links legais.** "Privacidade", "Acessibilidade", "Cookies" e "Termos de uso", nos mesmos lugares em todas as páginas. Links de ajuda ficam na mesma posição e funcionam do mesmo jeito em todas as páginas ([GOV.UK](https://design-system.service.gov.uk/components/footer/); WCAG 2.2, 3.2.6).

**Espelhe a navegação principal no mapa do site.** As páginas de primeiro nível da navegação principal aparecem no rodapé, com a mesma estrutura e os mesmos rótulos ([HDS](https://hds.hel.fi/components/footer)). Se o mapa ficar longo demais, crie uma página de mapa do site e coloque o link para ela no rodapé ([gov.br](https://www.gov.br/ds/components/footer)).

**Mantenha a ordem das áreas.** Logo, mapa do site, informações secundárias e informação legal, sempre nessa ordem e com o mesmo layout em todas as páginas ([gov.br](https://www.gov.br/ds/components/footer), [HDS](https://hds.hel.fi/components/footer)).

**Avise quando um link sai do produto.** Links do rodapé que levam para fora do produto usam o ícone de link externo (D14). Se a pessoa estiver no meio de um formulário, avise que os dados digitados podem se perder ([DKFDS](https://designsystem.dk/komponenter/footer/)), com uma mensagem na página, sem `alert()`. Em fluxos lineares, evite links que convidem a sair da tarefa ([GOV.UK](https://design-system.service.gov.uk/components/footer/)).

**Faça** rodapé simples em fluxos de tarefa, com responsável e links legais.

**Não faça** novidades e instruções de tarefa no rodapé, onde ninguém procura.

### Comportamento

**Recolha o mapa do site em telas estreitas.** Nas classes Compacta e Média, cada categoria do mapa vira uma seção recolhível, e só uma lista fica aberta por vez: abrir uma fecha a outra ([gov.br](https://www.gov.br/ds/components/footer)). Use `<details>` com o mesmo atributo `name` em todas as categorias: o próprio HTML garante uma aberta por vez, sem JavaScript. O chevron fica no fim do cabeçalho de cada categoria (D8). Na classe Expandida e maiores, as listas ficam abertas, lado a lado.

> **Divergência entre referências** Em telas pequenas, o gov.br transforma as categorias do mapa em seções recolhíveis ([gov.br](https://www.gov.br/ds/components/footer)), e o HDS oculta as subpáginas de segundo nível ([HDS](https://hds.hel.fi/components/footer)). O Trama recolhe: todos os links continuam alcançáveis em qualquer largura (critério 2). A especificação do gov.br também usa caixa alta nos títulos das categorias; o Trama usa caixa de frase (D1).

## Conteúdo

Títulos de categoria com uma ou duas palavras, em caixa de frase. Links com texto que diz o destino, sem "clique aqui" ([gov.br](https://www.gov.br/ds/components/footer)). Na informação legal, escreva o nome completo do responsável e, se houver sigla, use-a entre parênteses na primeira menção (D24).

## Acessibilidade

**Use o elemento `<footer>`.** Filho direto do `<body>`, ele vira o landmark `contentinfo` ([gov.br](https://www.gov.br/ds/components/footer), [HDS](https://hds.hel.fi/components/footer/accessibility)). Tenha um só por página. Outros landmarks dentro do rodapé, só com `aria-label` descritivo e com moderação ([HDS](https://hds.hel.fi/components/footer/accessibility)). Se o mapa do site for uma navegação, use `<nav aria-label="Mapa do site">`.

**Garanta contraste e alvo de toque.** No fundo escuro, links em `--t-fg-2` sobre `--t-bg` invertido precisam de 4,5:1 (WCAG 2.2, 1.4.3); confira as cores recomendadas de superfície e de leitura ([gov.br](https://www.gov.br/ds/components/footer)). Em telas de toque, cada link tem área mínima de 44px ([gov.br](https://www.gov.br/ds/components/footer); `--c-touch`, D17).

**Pense na ordem do teclado.** Quem usa teclado precisa passar por cada link; uma lista longa no rodapé custa muitas teclas ([HDS](https://hds.hel.fi/components/footer/accessibility)). O link "Pular para o rodapé" ajuda; veja Links de pular.

## Tokens usados

| Token                       | Uso                                   |
|-----------------------------|---------------------------------------|
| `--t-bg` (em `.tr-inverse`) | Fundo do rodapé escuro                |
| `--t-fg-1`                  | Títulos de categoria e links em hover |
| `--t-fg-2`                  | Links                                 |
| `--t-fg-3`                  | Texto da informação legal             |
| `--t-border`                | Divisão da área de informação legal   |
| `--sp-600`, `--sp-800`      | Espaço entre áreas e topo do rodapé   |
| `--t-focus` (invertido)     | Anel de foco no fundo escuro          |

## Considerações por plataforma

### Web desktop

Mostre o mapa do site aberto, em colunas que respeitam o grid. Com largura fixa, o conteúdo do rodapé se alinha ao contêiner e o fundo continua de ponta a ponta ([gov.br](https://www.gov.br/ds/components/footer); D18).

### Web móvel

Recolha o mapa do site em seções, uma aberta por vez, e empilhe os links legais. Mantenha 44px por link.

### Tablets e dobráveis

Na classe Média, mantenha o mapa recolhido. Ao abrir o dobrável e passar para a Expandida, mostre as listas abertas, preservando a categoria que a pessoa tinha aberto como a primeira em foco.

> **Nota** Na impressão, links de privacidade e redes sociais não têm função. Oculte-os e mantenha os contatos ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/print/)). Veja Impressão.

## Recursos

### Relacionados

- Cabeçalho
- Modelos de página: base e erro
- Acordeão
- Modo escuro
- Consentimento de cookies
- Legislação e normas

### Referências

- [Footer (Rodapé)](https://www.gov.br/ds/components/footer) gov.br DS
- [Template de erro](https://www.gov.br/ds/templates/erro) gov.br DS
- [GOV.UK footer](https://design-system.service.gov.uk/components/footer/) GOV.UK Design System
- [Footer](https://designsystem.dk/komponenter/footer/) DKFDS
- [Print](https://designsystem.dk/kom-i-gang/implementering-kode/print/) DKFDS
- [Footer](https://hds.hel.fi/components/footer) Helsinki Design System
- [Footer: accessibility](https://hds.hel.fi/components/footer/accessibility) Helsinki Design System

## Histórico de mudanças

| Data                  | Mudança                      |
|-----------------------|------------------------------|
| 16 de outubro de 2026 | Página criada na versão 1.1. |
