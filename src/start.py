import pygame as pg


from config import *


# Iniciando a tela do jogo
pg.init()
pg.display.set_caption(titulo_janela)

screen = pg.display.set_mode((largura_tela, altura_tela))


def Grade():
    # Desenhando a cobra
    for x in range(0, largura_tela, tamanho_inicial_cobra):
        for y in range(0, altura_tela, tamanho_inicial_cobra):
            # Construindo cobra no objeto do pygame
            rect = pg.Rect(x, y, tamanho_inicial_cobra, tamanho_inicial_cobra)

            # Desenhando na tela
            pg.draw.rect(screen, 'red', rect, 1)


# Construindo jogadores
jogador_1 = Jogadores(jog_1_coord_inic, verde, controle_wasd)
jogador_2 = Jogadores(jog_2_coord_inic, azul, controle_setas)

########### VARIAVEIS NOVAS ###########
coroando = Coroas(Map)    #o map está relacionado ao mapa, quando houver um mapa ele deve ser atribuído nos locais de Map

############ aumentar número de buffs e debuffs ###########
Buff_1.numero_buffs(Map, 15)
Debuff.numero_debuffs(Map, 10)

running = True
clock = pg.time.Clock()
mostrar_grade = False  # Variável para controlar a exibição da grade
#timer da coroa
visibilidade_coroa = False
clock_contagem_coroa = pg.time.get_ticks()
tempo_espera_coroa = 0

while running:
    screen.fill("black")
    clock.tick(7)  
    keys = pg.key.get_pressed()
    tempo_atual = pg.time.get_ticks()


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_j:  # Alterna a grade ao pressionar J
                mostrar_grade = not mostrar_grade
     
    ########## timer apenas no codigo para aparecer a coroa########
    if not visibilidade_coroa and tempo_atual - clock_contagem_coroa >= 15000:
        coroando.reposicionar()
        visibilidade_coroa = True

 # mudança do jogador
    jogador_1.update(keys, Buff_1.guardar_buffs,
                     Debuff.guardar_debuffs, coroando)
    jogador_2.update(keys, Buff_1.guardar_buffs,
                     Debuff.guardar_debuffs, coroando)

    ######## condição de vitória #########
    if jogador_1.pontuacao >= 100 or jogador_2.pontuacao >= 100:
        pg.quit()
    if jogador_1.contador_coroas == 3 or jogador_2.contador_coroas == 3:
        pg.quit()    ###### pode ser alterada sem muitos problemas. Apenas fecha o jogo se uma dessas condições for concluida.

    if jogador_1.corpo and jogador_2.corpo:
        if jogador_1.corpo[0] in jogador_2.corpo or jogador_2.corpo[0] in jogador_1.corpo:
            jogador_1.resetar()
            jogador_2.resetar()

   ############## mudança no número de buffs e debuffs #################
    for buff in Buff_1.guardar_buffs:
        buff.desenhar_buff1()

    for debuff in Debuff.guardar_debuffs:
        debuff.desenhar_debuff1()

    ######### COROA VISIVEL NO MAPA ########
    if visibilidade_coroa:
        coroando.desenhar_coroa()

    jogador_1.desenhar()
    jogador_2.desenhar()

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

    screen.blit(pontos_texto_1, (200, 0))
    screen.blit(pontos_texto_2, (largura -
                pontos_texto_2.get_width() - 200, 0))

    screen.blit(buff_texto_1, (100, 780))
    screen.blit(buff_texto_2, (largura - pontos_texto_2.get_width() - 250, 780))

    screen.blit(veneno_texto_1, (280, 780))
    screen.blit(veneno_texto_2, (largura -
                veneno_texto_2.get_width() - 85, 780))

    screen.blit(coroa_texto_1, (1, 370))
    screen.blit(coroa_texto_1_, (5, 390))

    screen.blit(coroa_texto_2, (largura -
                veneno_texto_2.get_width() - -67, 370))
    screen.blit(coroa_texto_2_, (largura -
                veneno_texto_2.get_width() - -75, 390))

    pg.display.flip()

pg.quit()
