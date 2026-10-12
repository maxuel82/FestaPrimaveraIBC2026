# Festa da Primavera IBC 2026

## Projeto

Este repositório contém um cardápio e simulador de consumo para celulares, publicado pelo GitHub Pages. A página principal é `index.html`, com HTML, CSS e JavaScript no próprio arquivo. Não precisa de compilação, npm ou banco de dados.

## Alterações

- Responda ao usuário em português do Brasil.
- Edite `index.html` para alterar o site. Preserve o layout para celulares, as quantidades, o resumo, o total e o compartilhamento pelo WhatsApp.
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
