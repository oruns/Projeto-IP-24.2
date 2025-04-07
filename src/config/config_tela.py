import pygame as pg


from .config_geral import carregar_dados, DIR_CONFIG


# Carregando dados
dados_tela = carregar_dados('tela')


# Recebendo da tela
BOTAO_MENU_LARGURA = dados_tela['botao_menu_largura']
BOTAO_MENU_ALTURA = dados_tela['botao_menu_altura']

ESPACAMENTO_MENU = dados_tela['espacamento_menu']

LARGURA_TELA = dados_tela['largura']
ALTURA_TELA = dados_tela['altura']

TITULO_JOGO = dados_tela['titulo_jogo']
TITULO_MENU = dados_tela['titulo_menu']

TEXTOS_BOTOES_MENU = ["Singleplayer", "Multiplayer", "Créditos", "Sair"]


### Constantes
Y_START_BTN = ALTURA_TELA // 2 - (2 * (BOTAO_MENU_ALTURA + ESPACAMENTO_MENU) // 2)

#confuso
LOGO_MENU_ALTURA = 200  
LOGO_Y = Y_START_BTN - LOGO_MENU_ALTURA - 20  # Logo acima dos botões, com um espaçamento de 20 pixels


### Objetos do pygame

# Define a fonte para o texto nos botões
FONT_MENU = pg.font.Font(None, 50)