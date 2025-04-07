import pygame as pg


from .config_geral import carregar_dados, DIR_CONFIG


# Controles para as cobras
CONTROLE_WASD = {
    "up": pg.K_w, "down": pg.K_s, "left": pg.K_a, "right": pg.K_d
}

CONTROLE_SETAS= {
    "up": pg.K_UP, "down": pg.K_DOWN, "left": pg.K_LEFT, "right": pg.K_RIGHT
}


# Carregando dados
dados_entidades = carregar_dados('entidades')


# Recebendo dados das cobras
tamanho_inicial_cobra = dados_entidades['tamanho_inicial_cobra']
velocidade = dados_entidades['velocidade_cobra']
jog_1_coord_inic = dados_entidades['jogador_1_coord_inicial']
jog_2_coord_inic = dados_entidades['jogador_2_coord_inicial']