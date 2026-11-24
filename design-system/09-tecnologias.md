# Tecnologias

## IA generativa

Recursos de inteligência artificial (IA) generativa mostram onde a IA atua, deixam claro o que ela faz e não faz, convidam à verificação e mantêm a pessoa no comando do resultado.

A IA generativa usa modelos de aprendizado de máquina para criar e transformar texto, imagens e outros conteúdos ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Ela pode poupar tempo e tem riscos próprios: a mesma entrada pode gerar resultados muito diferentes, e o modelo pode produzir conteúdo plausível e falso, as chamadas alucinações ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). O Fluent descreve como objetivo construir uma confiança adequada, sem prometer mais do que o recurso entrega ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)).

Ofereça IA generativa só onde ela traz valor claro e específico, e garanta uma boa experiência para quem não pode ou não quer usá-la, com um caminho sem IA sempre que possível ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)).

O Padrão Digital de Governo trata a IA de dois lados. Num, pede que os serviços sejam compreensíveis para pessoas e máquinas e compatíveis com assistentes virtuais, com a IA apoiando a classificação e a organização do conteúdo ([gov.br DS](https://www.gov.br/ds/introducao/principios)). No outro, sugere oferecer um chatbot, se possível, para ajudar a pessoa a encontrar informação ([gov.br DS](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)), e publica modelos em Figma para interfaces conversacionais ([gov.br DS](https://www.gov.br/ds/introducao/o-que-ha-de-novo)). Esta página cobre os recursos de IA que o produto oferece e a preparação do produto para assistentes de terceiros.

### Princípios

O Trama adota os cinco princípios que o Fluent define para IA responsável: ser transparente, definir expectativas adequadas, prevenir o excesso de confiança, manter a pessoa no controle e coletar feedback sobre os resultados ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)).

#### Transparência

**Mostre onde e quando a IA atua.** Avisar quando e onde o produto usa IA define expectativas e deixa a pessoa escolher conscientemente. Nunca faça alguém pensar que está interagindo com uma pessoa ou lendo conteúdo escrito por uma pessoa quando é IA ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Marque todo conteúdo gerado e sinalize cada ponto de entrada de IA antes da interação ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)).

**Diferencie a IA de pessoas.** Não sugira que a IA tem emoções, consciência ou vínculos; use primeira pessoa só quando for funcional; distinga IA de humanos em nomes, pronomes e elementos visuais ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)). No Trama, recursos de IA têm nomes de função ("Resumo automático", "Sugestão de resposta") e nunca usam avatar de pessoa.

**Mostre a base do resultado.** Deixe a pessoa verificar fontes e precisão ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)). Atribuições explicam a razão de um resultado sem detalhar o modelo; mantenha-as factuais e evite jargão estatístico ([HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning)). Prefira "Com base em 3 documentos do processo" a um percentual de confiança.

#### Expectativas

**Diga o que o recurso faz e o que não faz.** Esclarecer capacidades e limites ajuda a pessoa a formar um modelo mental correto. Para entradas abertas, ofereça sugestões de exemplo; informe limitações conhecidas logo de início e explique por que resultados ruins acontecem ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Use o texto de exemplo do campo de pedido e o tooltip do ponto de entrada para definir o escopo ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)).

**Ajude a pessoa a refazer pedidos bloqueados.** Quando um pedido não puder ser atendido, oriente como ter sucesso na próxima vez e ofereça exemplos de pedidos melhores ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Quando um recurso estiver indisponível, explique o motivo ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)).

#### Prevenção do excesso de confiança

**Apresente o resultado como algo a conferir.** Inclua o aviso de verificação em todo conteúdo gerado, nunca apresente o resultado como plenamente confiável e diferencie visualmente conteúdo gerado de conteúdo comum ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)). O Fluent lista a sobreconfiança como um tipo de dano: a pessoa aceita o resultado sem análise crítica, muitas vezes porque a interface não incentiva a verificação ([Fluent 2](https://fluent2.microsoft.design/ai-harm)).

**Crie um ponto de revisão antes de aplicar.** O resultado aparece primeiro como prévia; só entra no documento, formulário ou mensagem quando a pessoa escolhe "Inserir" ou "Aplicar". O Fluent recomenda pontos de atrito que estimulem o pensamento crítico antes de agir ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)).

**Limite o que pede ao modelo.** Evite pedir fatos ao modelo, a menos que ele tenha acesso a informação verificada e atual, e não use conteúdo gerado onde uma alucinação possa causar dano ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Avise quando uma resposta for parcial: o dano de um resultado incompleto é maior quando a pessoa não percebe ([Fluent 2](https://fluent2.microsoft.design/ai-harm)).

#### Controle

**Deixe a pessoa editar, desfazer e gerar novamente.** Mostre controles como Editar, Desfazer e Gerar novamente perto do conteúdo gerado, e confirme quando um ajuste fez efeito ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Permita descartar conteúdo indesejado ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Considere oferecer versões alternativas para a pessoa escolher ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)).

**Peça confirmação antes de ações irreversíveis.** Não automatize ações destrutivas nem difíceis de desfazer, como excluir arquivos ou comprar em nome da pessoa, e confirme antes de qualquer ação significativa ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Quando um agente age com autonomia, informe que ele foi ativado, o que o aciona, o que acessa e o que pode fazer, e deixe a pessoa aprovar ou rejeitar cada ação ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)).

**Nunca ative a IA em silêncio.** Avise quando a IA é ativada e mostre em configurações como mudar o comportamento global, dizendo exatamente onde fica a opção ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)).

#### Feedback

**Ofereça avaliação rápida e categorias específicas.** Deixe o feedback sempre voluntário, num lugar claro que não interrompa a tarefa, com uma forma rápida de avaliar positivo e negativo e um caminho para detalhar ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Ao detalhar, use categorias específicas, e diga quais dados vão junto com o feedback ([Fluent 2](https://fluent2.microsoft.design/ai-harm)). Aja imediatamente sobre o feedback recebido e mantenha o efeito ([HIG](https://developer.apple.com/design/human-interface-guidelines/machine-learning)).

#### Compatibilidade com assistentes virtuais

**Prepare o conteúdo para ser lido por máquinas.** Assistentes virtuais, leitores de tela e mecanismos de pesquisa leem a mesma estrutura. Use títulos em ordem, rótulos ligados aos campos, tabelas com cabeçalho e textos de link que façam sentido fora de contexto, e não guarde informação essencial só em imagem. Mantenha nomes de serviços, documentos e etapas iguais em toda a interface, para que um assistente consiga citá-los. Isso atende ao princípio de compreensão e compatibilidade do gov.br ([gov.br DS](https://www.gov.br/ds/introducao/principios)). Veja HTML acessível e WAI-ARIA.

**Ofereça o assistente conversacional como caminho a mais.** Um chat com IA pode ajudar a pessoa a encontrar uma informação, como sugere o gov.br ([gov.br DS](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)), desde que a página de ajuda, a pesquisa e o contato com uma pessoa continuem disponíveis. Diga no início da conversa que a pessoa está falando com um sistema de IA. Veja Oferecer ajuda.

> **Divergência entre referências** O gov.br sugere oferecer um chatbot, se possível, como recurso de ajuda ([gov.br DS](https://www.gov.br/ds/padroes/design/ajuda-comunicacao)). A HIG pede usar IA generativa só onde ela traz valor claro e manter uma boa experiência para quem não pode ou não quer usá-la ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)), e o Fluent pede não prometer mais do que o recurso entrega ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)). Nenhuma fonte cita pesquisa. Pelo critério de acessibilidade, o Trama decide: o assistente conversacional é opcional e nunca é o único caminho para ajuda, pesquisa ou atendimento.

### Padrões visuais

| Padrão                  | Uso no Trama                                                                                                                                                            |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rótulo de IA            | `.tr-badge--info` com o texto "Gerado com IA" no topo de todo resultado e em pontos de entrada. Nunca use só um ícone.                                                  |
| Superfície do resultado | `.tr-card` separado do conteúdo da pessoa até que ela aplique o resultado. Depois de aplicado, o conteúdo passa a ser da pessoa e o histórico registra a origem.        |
| Fontes                  | Links logo abaixo do texto gerado, apontando para o trecho de origem.                                                                                                   |
| Aviso de verificação    | `.tr-caption` em `--t-fg-3`, sempre visível, sem precisar expandir.                                                                                                     |
| Ações                   | Ação principal de aplicar (`.tr-btn--primary`), seguida de Editar e Gerar novamente; avaliação com dois botões de ícone com `aria-label`.                               |
| Raciocínio              | Acordeão "Como este resumo foi feito", em linguagem não técnica, como os painéis de raciocínio do Fluent ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)). |

#### Espera

**Descreva o que está acontecendo.** Mensagens que descrevem o trabalho real ajudam mais que um status vago ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). O Fluent sugere não mostrar indicador em esperas abaixo de 1 segundo, usar spinner entre 1 e 3 segundos e, acima disso, barra de progresso ou um texto que mostre que o processo continua; em chat com IA, mostre o indicador de resposta imediatamente ([Fluent 2](https://fluent2.microsoft.design/wait-ux)). Mostre o texto à medida que é gerado, com um botão Parar. Veja Carregamento e espera.

### Padrões de conteúdo

| Situação           | Use                                                                                                                       | Evite                       |
|--------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| Aviso em resultado | Conteúdo gerado com IA pode conter erros. Confira as fontes antes de usar.                                                | Resposta verificada.        |
| Espera             | Lendo 3 documentos do processo…                                                                                           | Pensando… / Processando…    |
| Conclusão          | Resumo gerado a partir de 3 documentos.                                                                                   | Pronto. Espero ter ajudado. |
| Pedido bloqueado   | Não é possível gerar este conteúdo. Tente descrever o documento que você quer resumir.                                    | Ops, algo deu errado.       |
| Erro               | Não foi possível ler o arquivo Contrato 2025 porque ele está protegido por senha. Envie outra versão ou continue sem ele. | Erro no processamento.      |
| Feedback detalhado | Informação incorreta · Resposta incompleta · Sem fontes · Fontes duvidosas · Conteúdo inseguro ou ofensivo · Outro        | Dê sua opinião.             |
| Dados do feedback  | Ao enviar, o pedido e a resposta são incluídos.                                                                           | Ajude-nos a melhorar.       |

As mensagens de espera usam verbo no gerúndio e as de conclusão, no particípio, como no padrão de conteúdo de espera do Fluent ([Fluent 2](https://fluent2.microsoft.design/wait-ux)). Mensagens de erro dizem o que falhou, por quê e oferecem dois caminhos ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)). As categorias de feedback adaptam a lista do Fluent ([Fluent 2](https://fluent2.microsoft.design/ai-harm)). Mensagens de sistema que relatam o que a IA fez ficam em terceira pessoa, numa frase curta ([Fluent 2](https://fluent2.microsoft.design/handoffs)).

**Faça** rotule o conteúdo e relate o que foi feito de forma factual.

**Não faça** dê à IA rosto, emoções ou certeza.

### Privacidade e inclusão

**Peça permissão antes de usar dados pessoais e use o mínimo.** Deixe claro se os dados vão para um servidor, o que é compartilhado e se é usado para treinar modelos, e ofereça sempre uma forma de recusar ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Mostre o que fica guardado na memória de um agente e como é usado ([Fluent 2](https://fluent2.microsoft.design/responsible-AI)). Produtos para o público brasileiro tratam esses dados conforme a Lei nº 13.709/2018, a Lei Geral de Proteção de Dados Pessoais (LGPD). Veja Privacidade e Legislação e normas.

**Não infira características pessoais.** Modelos tendem a favorecer a informação mais comum e podem reproduzir estereótipos. Peça à pessoa a informação necessária em vez de deduzir atributos pessoais ou culturais, e teste com pessoas diversas ([HIG](https://developer.apple.com/design/human-interface-guidelines/generative-ai)). Veja Inclusão.

### Acessibilidade

Anuncie o início e o fim da geração com `role="status"`, sem ler cada palavra enquanto o texto é gerado. Mantenha o foco onde estava durante a geração. O rótulo "Gerado com IA" é texto, para ser lido por leitores de tela. Botões de avaliação com ícone têm `aria-label` e `aria-pressed`.

### Considerações por plataforma

#### Web desktop

Mostre o resultado num painel lateral ao lado do conteúdo, para que a pessoa compare sem perder o contexto. Veja Painéis e split view.

#### Web móvel

Use um drawer inferior para o resultado e mantenha o aviso, as fontes e a ação de aplicar visíveis sem rolagem extensa.

#### Tablets e dobráveis

Com dois painéis, mostre o documento num lado e o resultado no outro. Ao fechar o aparelho, preserve o resultado ainda não aplicado.

### Recursos

#### Relacionados

- Privacidade
- Inclusão
- Carregamento e espera
- Feedback
- Desfazer e refazer
- Oferecer ajuda
- HTML acessível e WAI-ARIA

#### Referências

- [Princípios do Design System](https://www.gov.br/ds/introducao/principios) gov.br DS
- [Ajuda e comunicação](https://www.gov.br/ds/padroes/design/ajuda-comunicacao) gov.br DS
- [O que há de novo](https://www.gov.br/ds/introducao/o-que-ha-de-novo) gov.br DS
- [Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai) Apple HIG
- [Machine learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning) Apple HIG
- [Responsible AI](https://fluent2.microsoft.design/responsible-AI) Fluent 2
- [Types of AI harm](https://fluent2.microsoft.design/ai-harm) Fluent 2
- [Handoffs](https://fluent2.microsoft.design/handoffs) Fluent 2
- [Wait UX](https://fluent2.microsoft.design/wait-ux) Fluent 2

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                               |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta compatibilidade com assistentes virtuais, o assistente conversacional como caminho opcional, a referência à LGPD e rótulos de ação com até duas palavras. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                        |

## Impressão

Páginas que as pessoas guardam, como comprovantes, resumos e relatórios, precisam funcionar no papel e em PDF, com só o conteúdo que faz sentido fora da tela.

Mesmo em serviços digitais, muita gente imprime ou salva em PDF uma confirmação, um resumo de respostas ou uma tabela para levar a uma reunião. Na web, a impressão passa pela caixa de diálogo do navegador, que já oferece intervalo de páginas, cópias, orientação, escala e destino em PDF. O trabalho da aplicação é preparar a página com uma folha de estilos de impressão e, quando fizer sentido, oferecer uma ação de imprimir fácil de achar.

O DKFDS resume o objetivo: estruturar as páginas para que funcionem bem também impressas, escondendo o que não é relevante no papel, o que poupa espaço e tinta e dá uma visão mais clara do que importa ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/print/)).

### Boas práticas

#### Ação de imprimir

**Torne a impressão fácil de encontrar onde ela é útil.** Coloque a ação de imprimir num lugar padrão e previsível ([HIG](https://developer.apple.com/design/human-interface-guidelines/printing)). O DKFDS recomenda colocar links de função como "Imprimir" e "Abrir como PDF" no topo da página, onde a pessoa os vê antes de interagir com o conteúdo, e evitar o rodapé e posições pouco convencionais ([DKFDS](https://designsystem.dk/komponenter/funktionslink/)). Ofereça a ação em páginas de confirmação, resumos de respostas, recibos e relatórios. Em outras páginas, deixe a impressão para o menu do navegador.

**Use um rótulo que diga o que vai ser impresso.** Escreva "Imprimir comprovante" ou "Imprimir resumo". O DKFDS recomenda acompanhar ícones de função com uma palavra e, se for preciso escolher só um, preferir a palavra; "imprimir" está entre os poucos ícones convencionais que podem ficar sozinhos quando falta espaço, como numa tabela ([DKFDS](https://designsystem.dk/komponenter/funktionslink/)). Nesse caso, dê ao botão um `aria-label`. Use o ícone de impressora, que o gov.br associa a Imprimir entre os significados mínimos de ícones ([gov.br DS](https://www.gov.br/ds/introducao/padrao-minimo)). Veja Iconografia.

**Trate a impressão como ação de apoio.** O HDS classifica imprimir entre as ações suplementares de um formulário, que ajudam a pessoa sem serem essenciais para preenchê-lo ([HDS](https://hds.hel.fi/patterns/forms/form-building)). Use um botão secundário ou sutil (`.tr-btn--subtle`), nunca o primário. Se a pessoa não deve concluir o processo sem imprimir, use um botão com mais destaque ([DKFDS](https://designsystem.dk/komponenter/funktionslink/)).

**Mostre a ação só quando imprimir for possível.** Se não houver nada para imprimir, retire a ação da tela. Enquanto os dados carregam, não mostre a ação; ela aparece junto com o conteúdo que vai imprimir.

**Use a caixa de diálogo do navegador.** Ofereça intervalo de páginas, cópias e frente e verso pela interface do sistema ([HIG](https://developer.apple.com/design/human-interface-guidelines/printing)). Na web, chame `window.print()` e não recrie esses controles. Se o produto tiver opções próprias, como incluir ou não anexos, mostre-as antes de abrir a caixa do navegador, separe as avançadas com divulgação progressiva e, se possível, mostre uma prévia do efeito ([HIG](https://developer.apple.com/design/human-interface-guidelines/printing)).

#### Folha de estilos de impressão

**Esconda o que não funciona no papel.** Botões não têm função impressa e devem ser ocultados; no cabeçalho, mostre só o essencial e esconda menu, links e botões; no rodapé, mantenha contatos e esconda links como política de privacidade, que não funcionam impressos; não repita a mesma informação no cabeçalho e no rodapé ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/print/)). O GOV.UK oferece uma classe específica para remover elementos da versão impressa ([GOV.UK](https://design-system.service.gov.uk/styles/layout/)). No Trama, esconda também a navegação do cabeçalho, a navegação lateral, o rail, a barra inferior, as barras de ferramentas, os toasts, os links de pular e os banners de cookies. No rodapé, mantenha só o nome do órgão ou da empresa e os contatos.

**Imprima texto escuro sobre fundo branco.** Remova cores e imagens de fundo: o GOV.UK removeu fundos coloridos do banner de cookies na impressão e corrigiu o fundo azul da marca que aparecia ao imprimir o cabeçalho ([GOV.UK](https://design-system.service.gov.uk/components/cookie-banner/), [GOV.UK](https://design-system.service.gov.uk/components/header/)), e passa a cor do texto para preto puro ao imprimir ([GOV.UK](https://design-system.service.gov.uk/community/whats-new/)). No Trama, a impressão usa sempre os valores do tema claro, mesmo que a tela esteja em modo escuro, e substitui fundos semânticos por borda de `--stroke-thin` mais o texto do estado. Faixas com `.tr-inverse`, como o rodapé, também voltam aos valores claros.

**Não dependa de cor para transmitir significado.** Muitas impressoras são monocromáticas, e o gov.br lembra que uma impressão em preto e branco ou de má qualidade muda as cores de um gráfico ([gov.br DS](https://www.gov.br/ds/padroes/design/grafico)). Badges, tags e mensagens precisam do texto do estado ("Aprovado", "Pendente"), como as Diretrizes de Acessibilidade para Conteúdo Web (WCAG) 2.2 já exigem na tela, no critério 1.4.1.

**Desfaça o comportamento responsivo que atrapalha no papel.** O DKFDS sugere manter tabelas responsivas no formato normal de tabela na impressão ([DKFDS](https://designsystem.dk/kom-i-gang/implementering-kode/print/)). No Trama, remova a rolagem horizontal de `.tr-table-wrap`, abra acordeões e abas com conteúdo relevante e mostre o texto completo de campos truncados.

**Controle as quebras de página.** Evite quebrar dentro de linhas de tabela, cards, itens de lista de resumo e figuras com `break-inside: avoid`, e nunca deixe um título sozinho no fim da página (`break-after: avoid`). Repita o cabeçalho de tabelas longas usando `<thead>`.

**Mostre o destino de links importantes.** Links não funcionam no papel. Depois de links para documentos ou páginas que a pessoa precisa consultar, imprima o endereço entre parênteses, e esconda o ícone de link externo (`.tr-link--external`), que não tem função no papel. Não faça isso em links de navegação, que já estão ocultos.

**Inclua o contexto que se perde fora da tela.** Uma folha impressa precisa dizer de onde veio: nome do serviço, título da página, data e hora da impressão e, em comprovantes, o número de protocolo. Não imprima dados sensíveis que estão mascarados na tela.

``` code
@media print {
  :root { color-scheme: light; }
  body { background: #FFFFFF; color: #000000; }
  .tr-btn, .tr-nav, .tr-rail, .tr-bottom-nav, .tr-header__nav,
  .tr-skiplinks, .tr-toolbar, .tr-toast, .tr-pagination { display: none !important; }
  .tr-inverse { --t-bg: #FFFFFF; --t-fg-1: #15191E; --t-fg-2: #3E4650;
    --t-fg-3: #5A636E; --t-border: #C9CED4; --t-link: #0E6E6E; }
  .tr-link--external::after { display: none; }
  .tr-table-wrap { overflow: visible; border: 0; }
  .tr-table tr, .tr-card, .tr-summary > *, figure { break-inside: avoid; }
  h1, h2, h3 { break-after: avoid; }
  .tr-badge, .tr-msg { background: none; border: 1px solid currentColor; }
  a[href^="http"]::after { content: " (" attr(href) ")"; }
}
@page { margin: 2cm; }
```

**Faça** coloque a ação de imprimir no topo, com um rótulo que nomeia o conteúdo.

**Não faça** esconda a impressão no fim da página nem a apresente como ação principal.

> **Divergência entre referências** A HIG aceita desativar ou ocultar a ação de imprimir quando não há nada para imprimir ([HIG](https://developer.apple.com/design/human-interface-guidelines/printing)). O gov.br pede retirar da interface o elemento que a pessoa não consegue habilitar por uma ação dela ([gov.br DS](https://www.gov.br/ds/fundamentos-visuais/estados)). Pelo critério de acessibilidade, o Trama decide pela retirada: um botão desabilitado sem explicação é anunciado pelo leitor de tela e não diz à pessoa o que fazer.

### Acessibilidade

A ação de imprimir é um `<button>`, porque executa uma função. O DKFDS lembra que um link de função pode ser `<a>` ou `<button>` conforme a função ([DKFDS](https://designsystem.dk/komponenter/funktionslink/)). Quando a ação gera um PDF para baixar, use um link com o formato e o tamanho do arquivo no texto. PDFs gerados pelo produto precisam de estrutura de títulos, ordem de leitura e texto alternativo.

### Considerações por plataforma

#### Web desktop

É onde a impressão em papel é mais comum. Respeite Mod+P, que abre a caixa de impressão do navegador, sem reatribuir o atalho ([HIG](https://developer.apple.com/design/human-interface-guidelines/keyboards)). Teste a impressão em A4, o tamanho padrão no Brasil, e em Carta.

#### Web móvel

No celular, "imprimir" quase sempre significa salvar em PDF ou compartilhar. Ofereça também "Baixar PDF" ou "Enviar por e-mail" em comprovantes, porque o caminho de impressão do navegador móvel é pouco visível.

#### Tablets e dobráveis

Nenhuma consideração adicional para Tablets e dobráveis. A folha de impressão independe da classe de janela em que a página estava.

### Recursos

#### Relacionados

- Revisar respostas e confirmação
- Gerenciamento de arquivos
- Lista de resumo
- Tabelas
- Botões
- Rodapé

#### Referências

- [Padrão mínimo](https://www.gov.br/ds/introducao/padrao-minimo) gov.br DS
- [Estados](https://www.gov.br/ds/fundamentos-visuais/estados) gov.br DS
- [Gráfico](https://www.gov.br/ds/padroes/design/grafico) gov.br DS
- [Printing](https://developer.apple.com/design/human-interface-guidelines/printing) Apple HIG
- [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards) Apple HIG
- [Print](https://designsystem.dk/kom-i-gang/implementering-kode/print/) DKFDS
- [Funktionslink](https://designsystem.dk/komponenter/funktionslink/) DKFDS
- [Layout](https://design-system.service.gov.uk/styles/layout/) GOV.UK Design System
- [Cookie banner](https://design-system.service.gov.uk/components/cookie-banner/) GOV.UK Design System
- [Header](https://design-system.service.gov.uk/components/header/) GOV.UK Design System
- [What’s new](https://design-system.service.gov.uk/community/whats-new/) GOV.UK Design System
- [Form building](https://hds.hel.fi/patterns/forms/form-building) Helsinki Design System

### Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                  |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. A ação de imprimir passa a ser retirada da tela quando não há o que imprimir; entram o ícone de impressora, o tratamento de `.tr-inverse` e de links externos no papel. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                           |

