import pygame as pg


import random as rd


class Coroa:
    def __init__(self, mapa, coroa_img,
                 ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA):
        self.mapa = mapa
        self.reposicionar(mapa, ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
        self.image = coroa_img.convert_alpha()
        self.image = pg.transform.scale(self.image, (TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA))


    def reposicionar(self, Mapa, ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA):
        while True:
            self.x = rd.randint(0, (LARGURA_TELA - TAMANHO_INICIAL_COBRA) //
                                TAMANHO_INICIAL_COBRA) * TAMANHO_INICIAL_COBRA
            self.y = rd.randint(0, (ALTURA_TELA - TAMANHO_INICIAL_COBRA) //
                                TAMANHO_INICIAL_COBRA) * TAMANHO_INICIAL_COBRA

            # Verifica se a posição gerada está livre de paredes
            if not self.mapa.parede(self.x, self.y, TAMANHO_INICIAL_COBRA):
                break  # Sai do loop se a posição for válida


    def desenhar_coroa(self, tela, coroa_img):
        tela.blit(coroa_img,(self.x, self.y)) 