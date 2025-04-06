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

buffando1 = ItemCrescer()

running = True
clock = pg.time.Clock()
mostrar_grade = False  # Variável para controlar a exibição da grade

while running:
    screen.fill("black")
    clock.tick(7)  
    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_j:  # Alterna a grade ao pressionar J
                mostrar_grade = not mostrar_grade

    jogador_1.update(keys, buffando1)
    jogador_2.update(keys, buffando1)

    if jogador_1.corpo and jogador_2.corpo:
        if jogador_1.corpo[0] in jogador_2.corpo or jogador_2.corpo[0] in jogador_1.corpo:
            jogador_1.resetar()
            jogador_2.resetar()

    jogador_1.desenhar()
    jogador_2.desenhar()
    buffando1.desenhar_buff1()

    if mostrar_grade:
        Grade()

    font = pg.font.SysFont("Arial", 24)
    pontos_texto_1 = font.render(f"Jogador 1: {jogador_1.pontuacao}", True, (255, 255, 255))
    pontos_texto_2 = font.render(f"Jogador 2: {jogador_2.pontuacao}", True, (255, 255, 255))

    screen.blit(pontos_texto_1, (10, 10))
    screen.blit(pontos_texto_2, (largura_tela - pontos_texto_2.get_width() - 10, 10))

    pg.display.flip()

pg.quit()