# Decisões transversais

O Trama 1.0 sintetizou as referências de design system públicas. A versão 1.1 integrou o Padrão Digital de Governo (gov.br DS) a todo o sistema e reavaliou cada regra em conflito. Estas decisões valem para todas as páginas e componentes.

## Critério quando as referências divergem

Nesta ordem:

1. Evidência: a regra apoiada por pesquisa com usuários ou dado citado na fonte vence.
2. Acessibilidade: a opção que atende WCAG 2.2 AA com mais margem vence.
3. Contexto brasileiro: em linguagem, formatos, leis e convenções do Brasil, o gov.br pesa mais, porque é a única referência escrita para o público brasileiro.
4. Convergência: a posição da maioria das referências vence.
5. A decisão fica registrada na própria página, numa nota "Divergência entre referências", com quem diz o quê e o que o Trama decidiu.

## Decisões D1 a D27

- **D1 Capitalização.** Caixa de frase em títulos, botões, navegação, abas e rótulos. Nomes próprios e siglas mantêm maiúsculas. O gov.br usa iniciais maiúsculas em botões e títulos; o Trama segue Fluent, GOV.UK e DKFDS, e registra a divergência.
- **D2 Confirmações.** Diga o que mudou ("Arquivo enviado", "Endereço atualizado"). Sem "com sucesso" e sem exclamação.
- **D3 Formatos de dado.** Aceite qualquer formato digitado (espaços, pontos, hífens, barras), normalize no sistema, nunca bloqueie caracteres durante a digitação. Mostre o formato esperado no texto de ajuda. Formatar o valor exibido ao sair do campo é permitido; máscara que impede digitar ou apagar é proibida. (GOV.UK pede evitar máscara; gov.br recomenda máscara dinâmica; esta é a síntese.)
- **D4 Ordem dos botões.** Em páginas e formulários: ação principal primeiro, alinhada ao início do conteúdo, secundárias depois. Em diálogos, drawers e barras de ação de painéis: ações alinhadas ao fim, com a principal por último (à direita). Empilhados no celular: principal em cima.
- **D5 Senhas.** Mínimo de 8 caracteres, sem máximo, colar permitido, botão "Mostrar senha", sem campo de confirmação quando houver "Mostrar senha". Medidor de força com texto (Fraca, Média, Forte) e dicas.
- **D6 Erros.** Nunca culpe a pessoa, mesmo quando o erro foi dela. Tom neutro, sem humor, sem "Ops". Diga o que aconteceu e como resolver.
- **D7 Vocabulário controlado.** Use: "Pesquisar" (não "Buscar"); "Baixar" (não "Fazer download"); "Enviar arquivo"; "Excluir" (não "Deletar"); "Entrar" e "Sair"; "Continuar" em fluxos de tarefa e "Próximo" só em fluxos de leitura passiva (onboarding, carrossel); "Voltar" e "Concluir" (última etapa). O componente `campo-busca` passa a se chamar "Campo de pesquisa" e o padrão `busca` passa a se chamar "Pesquisa" (ids continuam iguais).
- **D8 Indicador de expansão.** Em acordeões e seções recolhíveis, chevron no fim do cabeçalho, para baixo quando fechado e para cima quando aberto. Em árvores, listas hierárquicas e linhas de tabela expansíveis, indicador no início.
- **D9 Desabilitado.** Se a pessoa não pode habilitar o elemento por uma ação dela, retire-o da interface. Se pode, mostre desabilitado e explique por quê (texto próximo ou tooltip focável). Nunca desabilite o botão de envio de formulário: valide ao enviar. Menus, abas, diálogos e tooltips não têm item desabilitado sem explicação.
- **D10 Estados.** Hover e pressionado são uma camada na cor do primeiro plano do próprio elemento com opacidade `--o-hover` (0,16 claro, 0,30 escuro) e `--o-pressed`; a marca usa os tokens pré-calculados `--t-brand-hover` e `--t-brand-pressed`. Um único hover, um único foco e um único item ativo por vez. A interação direta da pessoa tem prioridade. "Ativo/atual" (`aria-current`) é para navegação e ação imediata; "Selecionado" (`aria-selected`/`aria-checked`) é para coleções e ação posterior. Detalhes na página `estados`.
- **D11 Densidade.** Três níveis (`data-density="alta"`, padrão, `"baixa"`), em passos de 4px. Baixa é obrigatória em toque e na classe Compacta; alta só com apontador fino (mouse, trackpad), em tabelas, listas longas e ferramentas; nunca em alertas e mensagens. Mínimos: 4px de área de leitura entre conteúdo e borda; área de ação de 24px com mouse e `--c-touch` (44px) no toque, e a área de ação pode ultrapassar a superfície visível. Detalhes na página `densidade`.
- **D12 Foco.** Anel de 2px sólido `--t-focus` afastado 2px, só em `:focus-visible` (clique não mostra foco). Foco tênue (`.tr-focus-subtle`, 1px) para foco movido pelo sistema sem ação de teclado.
- **D13 Foco inicial.** Página nova ou etapa nova: foco no título H1. Diálogo informativo: no botão Fechar. Diálogo de ação: no primeiro campo, ou na ação principal se não houver campo. Diálogo destrutivo: na ação segura (Cancelar).
- **D14 Links.** Abra na mesma aba por padrão. Link que sai do domínio do produto leva o ícone de link externo (`.tr-link--external`) com texto acessível "(site externo)". Se abrir em nova aba, diga "(abre em nova aba)" no texto do link.
- **D15 Truncamento.** Nunca trunque títulos, itens de menu e navegação, rótulos de botão, mensagens de erro, validação ou notificação: quebre a linha. Truncamento é permitido em células de tabela, breadcrumb, nomes de arquivo e chips, sempre com o texto completo acessível (tooltip focável ou `title` + nome acessível), e nunca deixando menos de três caracteres de uma palavra. Detalhes em `excesso-conteudo`.
- **D16 Tipografia.** Body de 16px como base, mínimo de 12px. Espaços entre blocos de texto tokenizados (defina na página `tipografia`). Sem itálico em placeholder e sem caixa alta em títulos.
- **D17 Alvo de toque.** 44 x 44px (`--c-touch`).
- **D18 Grid.** Classes de janela do Trama mantidas. Novo: largura fixa (conteúdo centralizado com `max-width`, para conteúdo informativo e portais) e largura fluida (para sistemas e ferramentas). Na Compacta, sempre fluida.
- **D19 Espaçamento fino.** `--sp-50` e `--sp-150` só para ajustes internos de texto e ícone. Margens de segurança vizinhas não se somam: vale a maior.
- **D20 Movimento.** Além de respeitar `prefers-reduced-motion`, ofereça no produto um controle explícito para desligar animações não essenciais.
- **D21 Unidades.** Por extenso em texto corrido e rótulos acessíveis. Abreviações padronizadas (min, h, d, kB, MB) só em eixos de gráfico, células e cartões compactos, com a unidade nomeada no título ou cabeçalho.
- **D22 Diálogo.** No máximo duas ações no rodapé. Exceção: alerta de alterações não salvas (Salvar, Não salvar, Cancelar). Nunca "Saiba mais" como botão de diálogo.
- **D23 Mensagens temporárias.** Só toasts informativos sem ação somem sozinhos (mínimo de 7s, pausados em hover e foco). Mensagens com ação, de erro ou de alerta ficam até a pessoa fechar ou resolver.
- **D24 Escrita em pt-BR.** "Você", no singular. Parágrafos de até 4 linhas. Rótulos de ação com até 2 palavras (3 quando inevitável), sem artigo. Comece a frase pelo objetivo. Não negue um termo negativo. Evite estrangeirismos com equivalente comum. Sigla: nome completo na primeira vez, com a sigla entre parênteses.
- **D25 Legislação.** Meta WCAG 2.2 AA. Produtos para o público brasileiro observam a Lei nº 13.146/2015 (Estatuto da Pessoa com Deficiência, art. 63) e a Lei nº 13.709/2018 (LGPD). Produtos para órgãos públicos também observam a Lei nº 14.129/2021 e o eMAG. Detalhes em `legislacao`.
- **D26 Camadas.** `--z-0` conteúdo e formulários; `--z-1` cabeçalho, cards elevados, bordas de rolagem; `--z-2` flutuantes de baixa prioridade (menus, seletores, notificações); `--z-3` navegação flutuante e cabeçalho fixo; `--z-4` diálogo, tooltip, carregamento bloqueante. A elevação acompanha a camada.
- **D27 Fundo escuro no tema claro.** Use `.tr-inverse` para rodapés e faixas escuras: ele redefine os tokens alias para os valores escuros.
