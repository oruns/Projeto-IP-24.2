import pygame as pg


from random import randint

# constante roxo
class ItemCrescer:
    '''
    Item que faz as cobras crescerem
    '''

    def __init__(self):
        self.reposicionar()
        self.cor = (128, 0, 128)  # buff 1 é o bloco roxo


    def reposicionar(self, altura_tela, largura_tela, tamanho_cobras):
        self.x = randint(0, (largura_tela - tamanho_cobras) // tamanho_cobras) * tamanho_cobras
        self.y = randint(0, (altura_tela - tamanho_cobras) // tamanho_cobras) * tamanho_cobras


    def desenhar_buff1(self):
        pg.draw.rect(screen, self.cor, (self.x, self.y, tamanho_cobras, tamanho_cobras))