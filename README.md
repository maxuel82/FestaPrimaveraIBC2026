# Festa da Primavera IBC 2026

Cardápio para celulares com simulação de consumo, quantidades, resumo das escolhas e total a trocar por dinheirinho da festa. Inclui compartilhamento das escolhas com a família pelo WhatsApp. Não envia pedidos nem reserva produtos.

## Acesso externo

Após habilitar o GitHub Pages, o endereço será:

**https://maxuel82.github.io/FestaPrimaveraIBC2026/**

No repositório, abra **Settings → Pages**. Em **Build and deployment**, escolha **Deploy from a branch**. Selecione a branch **main** e a pasta **/ (root)** e clique em **Save**. Aguarde a publicação e confira o endereço em **Visit site** antes de distribuí-lo.

## Arquivos publicados

- `index.html`: página inicial completa, com estilos e JavaScript no próprio arquivo.
- `.nojekyll`: permite publicar diretamente os arquivos estáticos.

Para atualizar o cardápio publicado, edite `index.html`, faça commit e envie para a branch `main`.

## Mensagem para compartilhar

🌼 Vai aproveitar a Festa da Primavera? Simule as escolhas da sua família e veja quanto trocar por dinheirinho da festa no caixa:

https://maxuel82.github.io/FestaPrimaveraIBC2026/

No caixa, a troca pode ser feita com dinheiro, cartão ou Pix. Depois, use o dinheirinho nas barracas. A simulação não é um pedido nem uma reserva.

## Cardápio em imagem e QR Code

A página inicial oferece acesso ao cardápio completo em imagem. O arquivo QRCodeCardapioFestaPrimavera.png aponta para o simulador on-line e pode ser usado na divulgação.

## Codex pelo celular com o computador desligado

Crie um ambiente no ChatGPT/Codex pela opção **Trabalhar em → Nuvem → Escolha um ambiente → Criar ambiente**, ou em **Configurações → Codex Cloud → Ambientes**. Conecte o GitHub e selecione `maxuel82/FestaPrimaveraIBC2026`. Use o nome **Festa da Primavera IBC 2026**.

Este projeto é estático: não exige compilação nem instalação de pacotes para editar o site. Para prévia, use `python3 -m http.server 8000`. Peça ao Codex para preparar e verificar o ambiente; depois selecione **Publicar** e aguarde a confirmação de ambiente publicado.

No celular, abra o Codex na mesma conta e escolha esse ambiente. Exemplo: “No projeto Festa da Primavera, altere o preço da coxinha para R$ 8, confira o cálculo do total e prepare as alterações para revisão.” O trabalho será executado na nuvem mesmo com o computador desligado.

Revise e salve as alterações no GitHub. A publicação do site acompanha a branch `main` quando o GitHub Pages está configurado. Ao voltar ao computador, sincronize o repositório antes de continuar; mudanças locais ainda não enviadas não aparecem automaticamente na nuvem.

Instruções do projeto para o Codex estão em `AGENTS.md`. Documentação oficial: https://learn.chatgpt.com/docs/environments/cloud-environments.
