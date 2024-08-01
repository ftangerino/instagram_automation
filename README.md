### README

# Automação de Comentários no Instagram

## Descrição

Este script utiliza o Selenium para automatizar o processo de login no Instagram, navegação até um perfil específico e postagem de comentários na última publicação disponível. Ele monitora continuamente novas postagens e comenta automaticamente quando uma nova publicação é detectada. Tudo isso baseado na img src obtida através do webscrapping do instagram.

## Pré-requisitos

- Python 3.x
- Selenium
- Webdriver do navegador de sua preferência (ChromeDriver, GeckoDriver para Firefox, etc.)

## Instalação

1. Clone este repositório ou faça o download dos arquivos.
2. Instale as dependências necessárias:
   ```sh
   pip install selenium
   ```

3. Baixe o webdriver correspondente ao navegador que você deseja usar e adicione-o ao seu PATH.

## Uso

1. Abra o arquivo `instagram_bot.py` e edite as variáveis `username`, `password`, `profile_url` e `comment_text`, `last_posted_img_src` com suas informações.
2. Execute o script:
   ```sh
   python instagram_bot.py
   ```

## Funcionalidades

- **Login no Instagram**: Faz login automaticamente no Instagram usando as credenciais fornecidas.
- **Navegação até o perfil**: Navega até o perfil especificado.
- **Comentário na última postagem**: Comenta na última postagem disponível no perfil.
- **Monitoramento contínuo**: Monitora continuamente novas postagens e comenta automaticamente quando uma nova postagem é detectada.

## Tratativas de Erros

- O script inclui tratativas para diversos pontos críticos, como falha ao iniciar o driver, login, navegação e comentário na postagem.
- Mensagens de erro são exibidas no console para facilitar a identificação de problemas.

## Nota

- Use este script com responsabilidade e de acordo com os Termos de Uso do Instagram.
- Evite intervalos muito curtos para não ser bloqueado pelo Instagram.

## Sugestões e Melhorias

- Uso de cookies para evitar relogar toda vez que o script for executado.


---

Modificações e melhorias são sempre bem vindas.