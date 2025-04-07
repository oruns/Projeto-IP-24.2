import pygame as pg

def iniciar_jogador(cor, controle, coords_iniciais, Jogador, velocidade):
    jogador = Jogador(cor, controle, coords_iniciais, velocidade)

    return jogador


def iniciar_entidades(
    cores, coords_iniciais, controles,
    dados_tela, velocidade,
    Jogador, ItemCrescer
):
    '''
    Construir o(s) jogador(es), item de crescimento
    '''

    # Recebendo valores
    azul = cores['azul']
    verde = cores['verde']

    jog_1_coord_inic = coords_iniciais['jogador_1_coord_inic']
    jog_2_coord_inic = coords_iniciais['jogador_2_coord_inic']

    CONTROLE_WASD = controles['wasd']
    CONTROLE_SETAS = controles['setas']

    # Construindo jogadores
    jogador_1 = iniciar_jogador(verde, CONTROLE_WASD, jog_1_coord_inic, Jogador, velocidade)
    jogador_2 = iniciar_jogador(azul, CONTROLE_SETAS, jog_2_coord_inic, Jogador, velocidade)

    # Construindo item que faz a cobra crescer
    item_crescer = ItemCrescer(dados_tela, velocidade)
    

    return jogador_1, jogador_2, item_crescer


def iniciar_janela_jogo(titulo_janela, altura_tela, largura_tela):
    # Iniciando a tela do jogo
    pg.init()
    pg.display.set_caption(titulo_janela)

    tela = pg.display.set_mode((largura_tela, altura_tela))

    
    return tela
