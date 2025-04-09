import pygame as pg


import random as rd


# As configuracoes e as imagens (carregadas em variaveis),
# estarao prontamente disponiveis
from config import *
from imgs import *

from entidades import BlocoRoxo, Coroa, Debuff, Jogador

from mapa import Mapa, modelo_mapa


# Iniciando o jogo
pg.init()


# Configurações da tela
tela = pg.display.set_mode((LARGURA_TELA, ALTURA_TELA))

pg.display.set_caption(TITULO_JOGO)


def Grade():
    for x in range(0, LARGURA_TELA, TAMANHO_INICIAL_COBRA):
        for y in range(0, ALTURA_TELA, TAMANHO_INICIAL_COBRA):
            rect = pg.Rect(x, y, TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA)
            pg.draw.rect(tela, 'red', rect, 1)


# Jogadores
jogador_1 = Jogador(60, 400, (0, 255, 0), {
    "up": pg.K_w, "down": pg.K_s, "left": pg.K_a, "right": pg.K_d
}, TAMANHO_INICIAL_COBRA)

jogador_2 = Jogador(840, 400, (255, 192, 203), {
    "up": pg.K_UP, "down": pg.K_DOWN, "left": pg.K_LEFT, "right": pg.K_RIGHT
}, TAMANHO_INICIAL_COBRA)


########### VARIAVEIS NOVAS ###########
mapa = Mapa(LARGURA_TELA, ALTURA_TELA, TAMANHO_INICIAL_COBRA, modelo_mapa)
coroando = Coroa(mapa, coroa_img,
                 ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)

############ aumentar número de buffs e debuffs ###########
BlocoRoxo.numero_buffs(mapa, COR_BLOCO_ROXO, 15,
                       ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
Debuff.numero_debuffs(mapa, GRAY2, 10,
                      ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)


running = True
clock = pg.time.Clock()
mostrar_grade = False  # Variável para controlar a exibição da grade
visibilidade_coroa = False
clock_contagem_coroa = pg.time.get_ticks()
tempo_espera_coroa = 0

while running:
    tela.fill("black")
    clock.tick(7)
    keys = pg.key.get_pressed()
    tempo_atual = pg.time.get_ticks()

    mapa.desenha_labirinto(tela, bush_img, plano_img)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_j:  # Alterna a grade ao pressionar J
                mostrar_grade = not mostrar_grade

    ########## timer apenas no codigo para aparecer a coroa########
    if not visibilidade_coroa and tempo_atual - clock_contagem_coroa >= 15000:
        coroando.reposicionar(mapa, ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
        visibilidade_coroa = True

# mudança do jogador
    # jogador_1.update(keys,
    #                  Debuff.guardar_debuffs, coroando,
    #                  mapa, BlocoRoxo, Debuff,
    #                  ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
    jogador_1.update(keys, Debuff.guardar_debuffs, coroando,
                     visibilidade_coroa, mapa, BlocoRoxo, Debuff,
                     ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
    jogador_2.update(keys, Debuff.guardar_debuffs, coroando,
                     visibilidade_coroa, mapa, BlocoRoxo, Debuff,
                     ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
    # jogador_2.update(keys,
    #                  Debuff.guardar_debuffs, coroando,
    #                  mapa, BlocoRoxo, Debuff,
    #                  ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)

  ######## condição de vitória #########
    if jogador_1.pontuacao >= 100 or jogador_2.pontuacao >= 100:
        pg.quit()
    if jogador_1.contador_coroas == 3 or jogador_2.contador_coroas == 3:
        pg.quit()

    if jogador_1.corpo and jogador_2.corpo:
        if jogador_1.corpo[0] in jogador_2.corpo or jogador_2.corpo[0] in jogador_1.corpo:
            jogador_1.resetar()
            jogador_2.resetar()

    jogador_1.desenhar(tela, snake_head_img, snake_body_img, TAMANHO_INICIAL_COBRA)
    jogador_2.desenhar(tela, snake_head_img, snake_body_img, TAMANHO_INICIAL_COBRA)

    ############## mudança no número de buffs e debuffs #################
    for buff in BlocoRoxo.guardar_buffs:
        buff.desenhar_buff1(tela, apple_img)

    for debuff in Debuff.guardar_debuffs:
        debuff.desenhar_debuff1(tela, apple_img)

    ######### COROA VISIVEL NO MAPA ########
    if visibilidade_coroa:
        coroando.desenhar_coroa(tela, coroa_img)

    if mostrar_grade:
        Grade()
########## NOVOS TEXTOS ###########
    font = pg.font.SysFont("Arial", 17)
    pontos_texto_1 = font.render(
        f"Placar 1: {jogador_1.pontuacao}", True, (255, 255, 255))
    pontos_texto_2 = font.render(
        f"Placar 2: {jogador_2.pontuacao}", True, (255, 255, 255))
    buff_texto_1 = font.render(
        f"Buff 1: {jogador_1.contador_buffs}", True, (255, 255, 255))
    buff_texto_2 = font.render(
        f"Buff 2: {jogador_2.contador_buffs}", True, (255, 255, 255))
    veneno_texto_1 = font.render(
        f"Veneno 1: {jogador_1.contador_veneno}", True, (255, 255, 255))
    veneno_texto_2 = font.render(
        f"Veneno 2: {jogador_2.contador_veneno}", True, (255, 255, 255))
    coroa_texto_1 = font.render(f"C1", True, (255, 255, 255))
    coroa_texto_1_ = font.render(
        f"{jogador_1.contador_coroas}", True, (255, 255, 255))
    coroa_texto_2 = font.render(f"C2", True, (255, 255, 255))
    coroa_texto_2_ = font.render(
        f"{jogador_2.contador_coroas}", True, (255, 255, 255))

    tela.blit(pontos_texto_1, (0, 800))
    tela.blit(pontos_texto_2, (LARGURA_TELA -
                pontos_texto_2.get_width() - 0, 800))

    tela.blit(buff_texto_1, (100, 800))
    tela.blit(buff_texto_2, (LARGURA_TELA - pontos_texto_2.get_width() - 80, 800))

    tela.blit(veneno_texto_1, (180, 800))
    tela.blit(veneno_texto_2, (LARGURA_TELA -
                veneno_texto_2.get_width() - 180, 800))

    tela.blit(coroa_texto_1, (300, 800))
    tela.blit(coroa_texto_1_, (330, 800))

    tela.blit(coroa_texto_2, (LARGURA_TELA -
                veneno_texto_2.get_width() - 250, 800))
    tela.blit(coroa_texto_2_, (LARGURA_TELA -
                veneno_texto_2.get_width() - 220, 800))

    pg.display.flip()

pg.quit()