import pygame as pg


from config import *
from entidades import *
from tela import grade

from gerenciamento import inicializacao as inc
from gerenciamento import gerenciadores as grc


tela = inc.iniciar_janela_jogo(titulo_janela, altura_tela, largura_tela)

# Criando entidades
coords_iniciais = {
    'jogador_1_coord_inic': jog_1_coord_inic,
    'jogador_2_coord_inic': jog_2_coord_inic
}

controles = {
    'wasd': CONTROLE_WASD,
    'setas': CONTROLE_SETAS
}

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
    largura_tela, tela,
    velocidade
)


# Terminar jogo
pg.quit()