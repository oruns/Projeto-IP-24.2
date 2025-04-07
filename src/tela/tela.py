import pygame as pg


# Colocar dados nas funcoes nao na importacoa
def grade(altura_tela, largura_tela, tamanho_inic_cobra, screen):
    # Desenhando a cobra
    for x in range(0, largura_tela, tamanho_inic_cobra):
        for y in range(0, altura_tela, tamanho_inic_cobra):
            # Construindo cobra no objeto do pygame
            rect = pg.Rect(x, y, tamanho_inic_cobra, tamanho_inic_cobra)

            # Desenhando na tela
            pg.draw.rect(screen, 'red', rect, 1)