from config_geral import carregar_dados, DIR_CONFIG


# Carregando dados
dados_tela = carregar_dados('tela', DIR_CONFIG)

# Recebendo da tela
largura_tela = dados_tela['largura']
altura_tela = dados_tela['altura']
titulo_janela = dados_tela['titulo_janela']