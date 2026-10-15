# Festa da Primavera IBC 2026

## Projeto

Este repositório contém um cardápio e simulador de consumo para celulares, publicado pelo GitHub Pages. A página principal é `index.html`, com HTML, CSS e JavaScript no próprio arquivo. O cardápio é carregado de `itens.json`. Não precisa de compilação, npm ou banco de dados.

## Alterações

- Ao publicar mudanças no HTML, incremente a versão exibida no rodapé em uma unidade centesimal (1.00 → 1.01 → 1.02) e atualize a data e hora no fuso America/Sao_Paulo (Brasília), incluindo o atributo datetime. Faça isso uma vez por publicação, junto com as alterações, antes do commit e envio ao GitHub.

- Responda ao usuário em português do Brasil.
- Edite `index.html` para alterar a interface e `itens.json` para alterar o cardápio. Preserve o layout para celulares, as quantidades, o resumo, o total e o compartilhamento pelo WhatsApp.
- A simulação não envia pedidos nem reserva produtos. Preserve essa informação e o fluxo de troca por dinheirinho no caixa.
- Altere preços, produtos e regras da festa conforme o pedido do usuário.
- Preserve os nomes dos arquivos de imagem referenciados pela página e o endereço https://maxuel82.github.io/FestaPrimaveraIBC2026/ usado pelos QR Codes.
- Arquivos HTML de ideias ou rascunhos não são a página publicada.
- Não envie anexos da conversa, capturas de tela ou dependências locais ao GitHub sem necessidade para o pedido.

## Verificação e ambiente na nuvem

- Para visualizar: `python3 -m http.server 8000` na raiz do projeto (no Windows, use `python` quando necessário).
- Confira a página em largura de celular, os botões de quantidade, os totais, a limpeza e os links após alterar o comportamento.
- O site estático não exige instalação de dependências. Python é necessário apenas para o servidor de prévia e ferramentas auxiliares.
- `gerar_divulgacao_qr.py` é uma ferramenta opcional de geração de artes; usa qrcode, Pillow, OpenCV e fontes do Windows. Não a execute em Linux sem adaptar as fontes. Os arquivos gerados já estão no repositório.
- `verificar-cardapio.cjs`, quando disponível, contém uma cópia antiga do JavaScript; não o trate como prova de que a página atual funciona.

## GitHub e celular

O repositório é `maxuel82/FestaPrimaveraIBC2026`, com branch principal `main`. Para trabalhar com o computador desligado, selecione no celular um ambiente publicado do Codex Cloud associado a este repositório. Alterações só ficam disponíveis no GitHub quando salvas em commit e enviadas. Alterações integradas em `main` podem atualizar o site no GitHub Pages.

### Envio pela nuvem quando o terminal falhar

- Se o terminal falhar ao conectar ao proxy, verifique o conector do GitHub disponível na sessão antes de concluir que não é possível enviar alterações.
- Confira o repositório e a permissão de escrita pelo conector. Leia o arquivo na branch `main` e use seu SHA atual ao atualizar arquivos de texto, evitando sobrescrever alterações de outras conversas.
- Use o conector para enviar as alterações autorizadas; esse caminho não depende do computador ligado. Para alterações locais, compare com a versão remota atual antes do envio.
- Após o envio, releia o arquivo no GitHub e informe o commit criado. Diferencie envio confirmado ao repositório de publicação confirmada no GitHub Pages; não afirme que o site foi atualizado sem verificar a publicação.
- Se faltarem contexto ou alterações solicitadas em outra conversa, peça o conteúdo ao usuário; não presuma acesso ao histórico de outras tarefas.

## Tabela de preços em JSON

- A fonte principal dos produtos, preços, promoções e disponibilidade é `itens.json`. Preserve os IDs dos itens existentes, mesmo ao mudar seus nomes ou ordem.
- Para atualizações apenas do cardápio, incremente `versao` e atualize `atualizadoEm` em Brasília no JSON. A versão do site no HTML identifica alterações da interface e pode permanecer igual em publicações apenas de dados.
- `precoPromocional: null` significa sem promoção; um preço promocional deve ser menor que o preço normal. `esgotado: true` bloqueia novas adições. Use números em reais, com ponto para centavos.
- A página consulta o JSON ao abrir e pelo botão “Atualizar cardápio”. Esse botão mantém quantidades por ID, recalcula preços e remove itens esgotados ou removidos das escolhas com um aviso.
- O HTML inclui uma tabela inicial para abertura rápida e falhas de rede. Ao publicar alterações do HTML, sincronize também o bloco `initial-table` com o JSON. Após alterações apenas do JSON, o rodapé da tabela mostra a versão efetivamente carregada; em caso de falha a página avisa que não conferiu as atualizações.
- Publique HTML e JSON juntos quando ambos mudarem e valide os dados, os totais, promoções, esgotados, saldo, troco e compartilhamento. Não reintroduza o botão do cardápio em imagem.
