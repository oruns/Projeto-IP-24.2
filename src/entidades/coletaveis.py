import pygame as pg
import random as rd

#item que faz crescer e somar pontos
class Buff_1:
    guardar_buffs = []

    def __init__(self, Mapa):
        self.mapa = Mapa
        self.reposicionar()
        self.cor = (128, 0, 128)  # buff 1 é o bloco roxo
        Buff_1.guardar_buffs.append(self)  # adiciona a lista na classe

    def reposicionar(self):
        while True:
            self.x = rd.randint(0, (largura - tamanho_cobras) //
                                tamanho_cobras) * tamanho_cobras
            self.y = rd.randint(0, (altura - tamanho_cobras) //
                                tamanho_cobras) * tamanho_cobras

            # Verifica se a posição gerada está livre de paredes
            if not self.mapa.parede(self.x, self.y):
                break  # Sai do loop se a posição for válida

    def desenhar_buff1(self):
        pg.draw.rect(screen, self.cor, (self.x, self.y,
                     tamanho_cobras, tamanho_cobras))

    @classmethod
    def numero_buffs(cls, Mapa, quantidade):
        for i in range(quantidade):
            cls(Mapa)  # cria e adiciona na lista

# debuff veneno diminui o tamanho e subtrai pontos
class Debuff:
    guardar_debuffs = []

    def __init__(self, Mapa):
        self.mapa = Mapa
        self.reposicionar()
        self.cor = (64, 64, 64)  # debuff é o bloco cinza
        Debuff.guardar_debuffs.append(self)  # adiciona a lista na classe

    def reposicionar(self):
        while True:
            self.x = rd.randint(0, (largura - tamanho_cobras) //
                                tamanho_cobras) * tamanho_cobras
            self.y = rd.randint(0, (altura - tamanho_cobras) //
                                tamanho_cobras) * tamanho_cobras

            # Verifica se a posição gerada está livre de paredes
            if not self.mapa.parede(self.x, self.y):
                break  # Sai do loop se a posição for válida

    def desenhar_debuff1(self):
        pg.draw.rect(screen, self.cor, (self.x, self.y,
                     tamanho_cobras, tamanho_cobras))

    @classmethod
    def numero_debuffs(cls, Mapa, quantidade):
        for i in range(quantidade):
            cls(Mapa)  # cria e adiciona na lista


#coroa que garante vitória, se coletada um número determinado de vezes
class Coroas:
    def __init__(self, Mapa):
        self.mapa = Mapa
        self.reposicionar()
        self.cor = (255, 215, 0)  # coroas é o bloco dourado

    def reposicionar(self):
        while True:
            self.x = rd.randint(0, (largura - tamanho_cobras) //
                                tamanho_cobras) * tamanho_cobras
            self.y = rd.randint(0, (altura - tamanho_cobras) //
                                tamanho_cobras) * tamanho_cobras

            # Verifica se a posição gerada está livre de paredes
            if not self.mapa.parede(self.x, self.y):
                break  # Sai do loop se a posição for válida

    def desenhar_coroa(self):
        pg.draw.rect(screen, self.cor, (self.x, self.y,
                     tamanho_cobras, tamanho_cobras))
