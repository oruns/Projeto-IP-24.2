from .config_geral import carregar_dados, DIR_CONFIG


# Carregando dados
dados_tela = carregar_dados('tela')

# Recebendo da tela
largura_tela = dados_tela['largura']
altura_tela = dados_tela['altura']

titulo_janela = dados_tela['titulo_jogo']
titulo_menu = dados_tela['titulo_menu']

tamanho_x_botao_menu = dados_tela['tamanho_x_botao_menu']
tamanho_y_botao_menu = dados_tela['tamanho_y_botao_menu']

espacamento_menu = dados_tela['espacamento_menu']