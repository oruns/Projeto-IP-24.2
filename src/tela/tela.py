import pygame as pg


def grade(ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA, tela):
    for x in range(0, LARGURA_TELA, TAMANHO_INICIAL_COBRA):
        for y in range(0, ALTURA_TELA, TAMANHO_INICIAL_COBRA):
            rect = pg.Rect(x, y, TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA)
            pg.draw.rect(tela, 'red', rect, 1)