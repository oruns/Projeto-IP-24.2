import pygame as pg


from random import randint

# constante roxo
class ItemCrescer:
    '''
    Item que faz as cobras crescerem
    '''

    def __init__(self, dados_tela, velocidade):
        altura_tela = dados_tela['altura']
        largura_tela = dados_tela['largura']

        self.reposicionar(altura_tela, largura_tela, velocidade)
        self.cor = (128, 0, 128)  # buff 1 é o bloco roxo


    def reposicionar(self, altura_tela, largura_tela, velocidade):
        self.x = randint(0, (largura_tela - velocidade) // velocidade) * velocidade
        self.y = randint(0, (altura_tela - velocidade) // velocidade) * velocidade


    def desenhar_buff1(self, tela, velocidade):
        pg.draw.rect(tela, self.cor, (self.x, self.y, velocidade, velocidade))