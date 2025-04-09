import pygame as pg


from config import *
from entidades import *
from tela import grade

from gerenciamento import inicializacao as inc
from gerenciamento import gerenciadores as grc


pg.init()


FONT_MENU = pg.font.Font(None, 50)

tela = inc.iniciar_janela_jogo(TITULO_JOGO, ALTURA_TELA, LARGURA_TELA)


# Criando entidades
jogador_1, jogador_2, item_crescer = inc.iniciar_entidades(
    dados_cores, coords_iniciais,
    controles, dados_tela, velocidade,
    Jogador, ItemCrescer
)


# Iniciando loop do jogo
grc.iniciar_loop(
    dados_tela,
    jogador_1, jogador_2,
    grade, item_crescer,
    LARGURA_TELA, tela,
    velocidade
)


# Terminar jogo
pg.quit()