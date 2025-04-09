import pygame as pg

import random as rd


from entidades import BlocoRoxo, Coroa, Debuff, Jogador
from mapa import Mapa, modelo_mapa
from tela import grade

import gerenciamento as grm


# As configuracoes e as imagens (carregadas em variaveis),
# estarao prontamente disponiveis
from config import *
from imgs import *


# Iniciando o pygame
pg.init()


# Iniciando a tela
tela = pg.display.set_mode((LARGURA_TELA, ALTURA_TELA))

pg.display.set_caption(TITULO_JOGO)


# Iniciando entidades
jogador_1 = Jogador(jog_1_coord_inic, GREEN, controles['wasd'], TAMANHO_INICIAL_COBRA)
jogador_2 = Jogador(jog_2_coord_inic, ROSA, controles['setas'], TAMANHO_INICIAL_COBRA)
mapa = Mapa(LARGURA_TELA, ALTURA_TELA, TAMANHO_INICIAL_COBRA, modelo_mapa)
coroa = Coroa(mapa, coroa_img, ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)


# Criando buffs e debuffs, e seus objetos
BlocoRoxo.numero_buffs(mapa, COR_BLOCO_ROXO, 15,
                       ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
Debuff.numero_debuffs(mapa, GRAY2, 10,
                      ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)


running = True # Define se o jogo esta rodando
mostrar_grade = False  # Controlar a exibição da grade
visibilidade_coroa = False
tempo_espera_coroa = 0

clock = pg.time.Clock()
clock_contagem_coroa = pg.time.get_ticks()


# Loop principal do jogo
while running:
    tela.fill("black")
    clock.tick(10) # Controlar velocidade do jogo

    # Teclas pressionadas pelo usuario nesse momento
    keys = pg.key.get_pressed()

    tempo_atual = pg.time.get_ticks()


    mapa.desenha_labirinto(tela, bush_img, plano_img)

    mostrar_grade, running = grm.gerenciadores.gerenciar_eventos_jogo(mostrar_grade, running)
    

    # Timer apenas no codigo para aparecer a coroa
    if not visibilidade_coroa and tempo_atual - clock_contagem_coroa >= 15000:
        coroa.reposicionar(mapa, ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
        visibilidade_coroa = True


    grm.gerenciadores.atualizar_jogadores(
        jogador_1, jogador_2,
        keys, Debuff.guardar_debuffs, coroa,
        visibilidade_coroa, mapa, BlocoRoxo, Debuff,
        ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA
    )


    # Checar se algum jogador venceu
    grm.gerenciadores.checar_vitoria(jogador_1, jogador_2)

    # Checar se os jogadores colidiram
    grm.gerenciadores.testar_colisao(jogador_1, jogador_2)


    # Desenhando buffs
    for buff in BlocoRoxo.guardar_buffs:
        buff.desenhar_buff1(tela, apple_img)

    # Desenhando debuffs
    for debuff in Debuff.guardar_debuffs:
        debuff.desenhar_debuff1(tela, hole_img)

    # Desenhar coroa
    if visibilidade_coroa:
        coroa.desenhar_coroa(tela, coroa_img)

    # Desenhar jogadores na tela
    jogador_1.desenhar(tela, snake_head_img, snake_body_img, TAMANHO_INICIAL_COBRA)
    jogador_2.desenhar(tela, snake_head_img, snake_body_img, TAMANHO_INICIAL_COBRA)
  
    # Desenhar grade
    if mostrar_grade:
        grade(ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA, tela)


    # Criando textos para serem desenhados
    font = pg.font.SysFont("Arial", 17)

    pontos_texto_1 = font.render(
        f"Placar 1: {jogador_1.pontuacao}", True, WHITE)
    pontos_texto_2 = font.render(
        f"Placar 2: {jogador_2.pontuacao}", True, WHITE)
    buff_texto_1 = font.render(
        f"Buff 1: {jogador_1.contador_buffs}", True, WHITE)
    buff_texto_2 = font.render(
        f"Buff 2: {jogador_2.contador_buffs}", True, WHITE)
    veneno_texto_1 = font.render(
        f"Veneno 1: {jogador_1.contador_veneno}", True, WHITE)
    veneno_texto_2 = font.render(
        f"Veneno 2: {jogador_2.contador_veneno}", True, WHITE)
    coroa_texto_1 = font.render(f"C1", True, WHITE)
    coroa_texto_1_ = font.render(
        f"{jogador_1.contador_coroas}", True, WHITE)
    coroa_texto_2 = font.render(f"C2", True, WHITE)
    coroa_texto_2_ = font.render(
        f"{jogador_2.contador_coroas}", True, WHITE)


    # Desenhando textos na tela
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


    # Atualizando a tela
    pg.display.flip()

# Encerrando jogo
pg.quit()
