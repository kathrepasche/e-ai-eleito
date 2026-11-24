# UploadDeArquivo

O upload de arquivo permite escolher um ou mais arquivos do aparelho, ou arrastá-los para uma área, e enviá-los com um formulário.

O componente do Trama é construído sobre o `<input type="file">` nativo, que recebe foco, funciona com teclado e com tecnologias assistivas, e continua funcionando sem JavaScript ([DKFDS](https://designsystem.dk/komponenter/fil-upload/); [gov.br](https://www.gov.br/ds/components/upload)). A área de soltar (`.tr-dropzone`) é um complemento: a pessoa clica no botão Escolher arquivo ou arrasta arquivos para a área ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)). Depois da escolha, uma lista mostra nome, tamanho e estado de cada arquivo, com a opção de removê-lo ([gov.br](https://www.gov.br/ds/components/upload)).

**Quando usar.** Quando um documento é indispensável para o serviço, como um comprovante, uma petição ou uma planilha a importar, dentro de um formulário ou isolado ([gov.br](https://www.gov.br/ds/components/upload)). Peça arquivos só quando for crítico para entregar o serviço ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)).

**Quando não usar.** Se a informação puder ser digitada em poucos campos, use campos de texto. Se o serviço já tem o documento, ofereça reutilizá-lo ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)). Para organizar e versionar arquivos já enviados, veja Gerenciamento de arquivos.

## Anatomia

1.  **Rótulo** (`.tr-label`): nomeia o documento e diz quantos arquivos.
2.  **Dica** (`.tr-hint`): formatos, tamanho máximo, limite de arquivos e se é possível arrastar ([gov.br](https://www.gov.br/ds/components/upload)).
3.  **Mensagem** (condicional): erro, alerta ou sucesso do componente, acima da área.
4.  **Área de soltar** (`.tr-dropzone`, opcional): borda tracejada `--t-border-control` sobre `--t-surface-1`, sempre visível no desktop.
5.  **Botão Escolher arquivo**: abre o seletor do sistema. Clicar em qualquer ponto da área também o abre ([HDS](https://hds.hel.fi/components/file-input/accessibility); [gov.br](https://www.gov.br/ds/components/upload)).
6.  **Lista de arquivos**: nome, tamanho, estado e botão Remover de cada arquivo ([gov.br](https://www.gov.br/ds/components/upload)).
7.  **Progresso**: um indicador por arquivo durante a transferência ([gov.br](https://www.gov.br/ds/components/upload)).

## Tipos

| Tipo                   | Uso                                                                                                                                                     |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Um arquivo             | Rótulo e dica no singular. Um arquivo novo substitui o anterior, com alerta ([gov.br](https://www.gov.br/ds/components/upload)).                        |
| Vários arquivos (lote) | Arquivos relacionados entre si, com `multiple`. Para documentos sem relação, use um upload para cada ([HDS](https://hds.hel.fi/components/file-input)). |
| Com área de soltar     | Quando arrastar ajuda, sobretudo no desktop. O botão continua disponível ([HDS](https://hds.hel.fi/components/file-input)).                             |
| Envio no formulário    | Padrão. Os arquivos sobem quando a pessoa envia o formulário ([HDS](https://hds.hel.fi/components/file-input)).                                         |
| Envio imediato         | Cada arquivo sobe ao ser escolhido ou solto, com progresso por arquivo ([gov.br](https://www.gov.br/ds/components/upload)). Útil para arquivos grandes. |

## Boas práticas

**Informe formatos e tamanho antes da escolha.** Deixe claro o que é aceito ([DKFDS](https://designsystem.dk/komponenter/fil-upload/)), na dica abaixo do rótulo ([HDS](https://hds.hel.fi/components/file-input)). Quando houver área de soltar, diga na dica que é possível arrastar ([gov.br](https://www.gov.br/ds/components/upload)).

**Verifique o arquivo ao ser escolhido e de novo no servidor.** Cheque tipo e tamanho no navegador para que a pessoa não perca tempo ([DKFDS](https://designsystem.dk/komponenter/fil-upload/)), e use `accept` para filtrar o seletor. A verificação no navegador pode ser contornada: restrinja os tipos e verifique tipo, tamanho e nome no servidor; arquivos de origem não confiável passam por antivírus ([HDS](https://hds.hel.fi/components/file-input/security)).

**No lote, recuse só o arquivo com problema.** Se um dos arquivos não atende aos requisitos, mostre o erro junto dele e aceite os demais ([gov.br](https://www.gov.br/ds/components/upload)). Quando o limite de quantidade é ultrapassado, diga quantos ainda cabem.

**No envio de um arquivo, avise a substituição.** O seletor não permite escolher mais de um, e arrastar vários gera uma mensagem de que só um é aceito. Se já houver um arquivo e a pessoa escolher outro, o mais recente substitui o anterior, e um alerta diz qual foi trocado ([gov.br](https://www.gov.br/ds/components/upload)).

**Mostre o progresso e confirme o resultado.** Um indicador por arquivo ajuda a estimar quanto falta ([Apple](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop); [gov.br](https://www.gov.br/ds/components/upload)). Cada arquivo termina com seu estado: “Enviado” ou o motivo da recusa ([DKFDS](https://designsystem.dk/komponenter/fil-upload/)).

**Destaque a área só quando ela aceita o que está sendo arrastado.** Aplique `.tr-dropzone--active` enquanto o arquivo está sobre a área e remova quando ele sai. Se o arquivo não for aceito, não destaque ([Apple](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

**Trunque nomes longos sem perder o nome.** O nome do arquivo pode terminar em reticências quando não cabe, com o nome completo num tooltip focável ([gov.br](https://www.gov.br/ds/components/upload)), e nunca com menos de três caracteres de uma palavra visíveis.

**Permita conferir, reutilizar e preservar.** Clicar no nome abre o arquivo para conferência ([gov.br](https://www.gov.br/ds/components/upload); [Apple](https://developer.apple.com/design/human-interface-guidelines/file-management)). Ofereça reutilizar arquivos já enviados na mesma jornada, considerando computadores públicos ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)). Ao voltar a uma etapa, mostre os arquivos já escolhidos ([HDS](https://hds.hel.fi/components/file-input)).

**Faça** rótulo que nomeia o documento e limites visíveis antes da escolha.

**Não faça** área sem botão, com rótulo genérico em caixa alta e sem limites.

### Estados e teclado

| Estado                  | Aparência                                                                                                        |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| Vazio                   | Área `--t-surface-1` com borda tracejada `--t-border-control`                                                    |
| Arrastando sobre a área | `.tr-dropzone--active`: borda `--t-brand` e camada `--o-hover` da marca                                          |
| Foco no botão           | Anel de 2px `--t-focus`, em `:focus-visible`                                                                     |
| Enviando                | Progresso por arquivo e botão Cancelar                                                                           |
| Enviado                 | Estado “Enviado” em `--t-success` com ícone                                                                      |
| Substituído             | `.tr-field-msg--warning` com o nome do arquivo novo e do anterior                                                |
| Erro                    | Erro do componente acima da área; erro de um arquivo junto dele na lista                                         |
| Desabilitado            | Só quando a pessoa pode habilitá-lo por uma ação dela, com o motivo ao lado; caso contrário, retire o componente |

**Teclado.** Tab leva ao botão, e Enter ou Espaço abrem o seletor. Na lista, Tab ou as setas percorrem os arquivos, e cada botão Remover é acionado com Enter ou Espaço ([gov.br](https://www.gov.br/ds/components/upload)).

> **Divergência entre referências** *Rótulo:* o gov.br fixa rótulos genéricos como “Envio de arquivos” e “Envio de documentos”; a HDS pede nomear o documento esperado e dizer quantos. Pelo critério de acessibilidade (rótulos que descrevem o propósito, WCAG 2.2, 2.4.6), o Trama nomeia o documento. *Texto da área:* o gov.br grafa o texto da área em caixa alta e itálico; o Trama usa caixa de frase e sem itálico, como em toda a tipografia do sistema. *Cor da área ativa:* o gov.br usa verde durante o arraste; o Trama usa `--t-brand` e reserva `--t-success` para o arquivo enviado. *Confirmação:* a página de microcopy do gov.br recomenda “O arquivo foi enviado com sucesso!”; o Trama diz o que mudou, sem “com sucesso” e sem exclamação: “Arquivo enviado”.

## Conteúdo

**Rótulo.** Nomeie o documento e indique quantos: “Comprovantes de renda”, “Foto do documento de identidade” ([HDS](https://hds.hel.fi/components/file-input)).

**Botão e área.** Textos curtos, porque textos longos dificultam o uso com leitor de tela ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)): “Escolher arquivo”, “Escolher arquivos”, “Arraste os arquivos para cá ou”. A ação de envio do formulário usa “Enviar arquivo” ou “Enviar arquivos”.

**Tamanhos.** Em dicas e mensagens, escreva a unidade por extenso: “até 10 megabytes”. Na lista, use a abreviação, como numa célula de tabela: “1,2 MB”. Use a mesma base de cálculo na dica e na lista ([HDS](https://hds.hel.fi/components/file-input)).

**Erros e alertas.** Diga o que aconteceu e como resolver, sem culpar a pessoa.

| Situação               | Modelo                                                |
|------------------------|-------------------------------------------------------|
| Nenhum arquivo         | Selecione um comprovante de renda                     |
| Formato errado         | O arquivo deve ser PDF, JPG ou PNG                    |
| Grande demais          | O arquivo deve ter menos de 10 megabytes              |
| Vazio                  | O arquivo selecionado está vazio                      |
| Vírus                  | O arquivo selecionado contém vírus                    |
| Protegido por senha    | O arquivo selecionado está protegido por senha        |
| Falha no envio         | Não foi possível enviar o arquivo. Tente de novo      |
| Arquivos demais        | Você pode enviar até 5 arquivos. Ainda cabem 2        |
| Vários num envio de um | Envie um arquivo por vez                              |
| Substituição           | identidade-verso.jpg substituiu identidade-frente.jpg |

Os modelos seguem a lista de situações do GOV.UK ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)). Nas mensagens vindas do servidor, não exponha caminhos de arquivo ou outros detalhes internos ([HDS](https://hds.hel.fi/components/file-input/security)).

## Acessibilidade

- Use o `<input type="file">` nativo ([gov.br](https://www.gov.br/ds/components/upload)) ou um controle que mantenha foco, teclado, suporte a tecnologias assistivas e funcionamento sem JavaScript ([DKFDS](https://designsystem.dk/komponenter/fil-upload/)).
- Arrastar não é acessível para todos; o botão continua sempre presente ([HDS](https://hds.hel.fi/components/file-input/accessibility); WCAG 2.2, 2.5.7).
- Usuários de reconhecimento de voz têm dificuldade para acionar o seletor nativo por comandos; um botão real que abre o seletor resolve isso ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)).
- Associe cada botão Remover ao nome do arquivo: “Remover holerite-setembro.pdf” ([gov.br](https://www.gov.br/ds/components/upload)).
- Anuncie arquivo adicionado, enviado, recusado ou substituído numa região `aria-live="polite"`, com o tipo da mensagem ([gov.br](https://www.gov.br/ds/components/upload)).
- Os textos do componente seguem o idioma da página ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)).

## Tokens usados

| Elemento          | Token                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------|
| Área de soltar    | `--stroke-thick` tracejado, `--t-border-control`, `--t-surface-1`, `--r-lg`, preenchimento `--sp-600` |
| Área ativa        | `--t-brand`, `--o-xs`                                                                                 |
| Lista de arquivos | `.tr-list`: `--t-border-subtle`, `--r-lg`, linha `--d-row`                                            |
| Metadados         | 13/18, `--t-fg-3`                                                                                     |
| Progresso         | `.tr-progress`, `--t-brand`                                                                           |
| Estados           | `--t-success`, `--t-warning`, `--t-danger`                                                            |
| Largura máxima    | 480px; largura total na classe Compacta                                                               |

## Considerações por plataforma

### Web desktop

A área de soltar é mais útil aqui. Deixe-a grande e sempre visível, e responda visualmente quando um arquivo passa sobre ela ([GOV.UK](https://design-system.service.gov.uk/components/file-upload/)). Aceite vários arquivos de uma vez no tipo lote ([Apple](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)).

### Web móvel

Na classe Compacta, o componente ocupa a largura da tela e não há arraste: a pessoa só toca no botão ([gov.br](https://www.gov.br/ds/components/upload)). Esconda a frase “Arraste os arquivos para cá” e use botão em largura total com densidade baixa. O seletor do sistema oferece galeria, câmera e arquivos; use `capture` só quando a foto precisa ser tirada na hora. Mostre o tamanho total antes de enviar, por causa do consumo de dados.

### Tablets e dobráveis

Em tablets, a pessoa pode arrastar arquivos de outro app aberto lado a lado; mantenha a área de soltar visível em janelas Médias e Expandidas. Num dobrável aberto, a área e a lista ficam no mesmo painel.

## Recursos

### Relacionados

- Gerenciamento de arquivos
- Arrastar e soltar
- Indicadores de progresso
- Validação e mensagens de erro
- Privacidade

### Referências

- [Upload](https://www.gov.br/ds/components/upload) gov.br DS
- [Microcopy](https://www.gov.br/ds/padroes/writing/microcopy) gov.br DS
- [Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop) Apple HIG
- [File management](https://developer.apple.com/design/human-interface-guidelines/file-management) Apple HIG
- [File upload](https://design-system.service.gov.uk/components/file-upload/) GOV.UK Design System
- [Vedhæft fil](https://designsystem.dk/komponenter/fil-upload/) Det Fælles Designsystem
- [FileInput](https://hds.hel.fi/components/file-input) Helsinki Design System
- [FileInput: acessibilidade](https://hds.hel.fi/components/file-input/accessibility) Helsinki Design System
- [FileInput: segurança](https://hds.hel.fi/components/file-input/security) Helsinki Design System
- [File input](https://blueprintjs.com/docs/#core/components/file-input) Blueprint

## Histórico de mudanças

| Data                  | Mudança                                                                                                                                                                                                                                          |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 16 de outubro de 2026 | Versão 1.1: integra o Padrão Digital de Governo. Acrescenta a substituição no envio de um arquivo, a recusa por arquivo no lote, o truncamento de nomes, a área ativa, a navegação por teclado na lista e as unidades por extenso nas mensagens. |
| 16 de outubro de 2026 | Página criada.                                                                                                                                                                                                                                   |
