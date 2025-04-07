import pygame as pg
import random as rd
from coletaveis import Buff_1
from coletaveis import Debuff
from coletaveis import Coroas
#possíveis novas adições


class Jogadores:
    def __init__(self, x, y, cor, teclas):
        self.inicio = (x, y)
        self.cor = cor
        self.corpo = [self.inicio]
        self.velocidade = tamanho_cobras
        self.direcao = (0, 0)  # começa parado
        self.teclas = teclas
        self.crescer = False
        self.pontuacao = 0
        self.contador_buffs = 0
        self.contador_veneno = 0  # veneno vezes #########
        self.contador_coroas = 0

    def update(self, keys, lista_buffs, debuff, coroa):

        if keys[self.teclas["up"]] and self.direcao != (0, self.velocidade):
            self.direcao = (0, -self.velocidade)
        if keys[self.teclas["down"]] and self.direcao != (0, -self.velocidade):
            self.direcao = (0, self.velocidade)
        if keys[self.teclas["left"]] and self.direcao != (self.velocidade, 0):
            self.direcao = (-self.velocidade, 0)
        if keys[self.teclas["right"]] and self.direcao != (-self.velocidade, 0):
            self.direcao = (self.velocidade, 0)

        if self.corpo:
            nova_parte = (self.corpo[0][0] + self.direcao[0],
                          self.corpo[0][1] + self.direcao[1])
        else:
            nova_parte = self.inicio

        # verificando a colisão com o labirinto
        if Map.labirinto[nova_parte[1] // tamanho_cobras][nova_parte[0] // tamanho_cobras] == 1:
            self.resetar()
            return

        if (nova_parte[0] < 0 or nova_parte[0] >= largura or
                nova_parte[1] < 0 or nova_parte[1] >= altura):
            self.resetar()
            return

        if nova_parte in self.corpo[1:]:
            self.resetar()
            return

        # verifica se cabeça colidiu com o buff 1
        for buff in Buff_1.guardar_buffs:
            if pg.Rect(nova_parte[0], nova_parte[1], tamanho_cobras, tamanho_cobras).colliderect(
                    pg.Rect(buff.x, buff.y, tamanho_cobras, tamanho_cobras)):
                self.pontuacao += 10
                self.contador_buffs += 1
                self.crescer = True
                buff.reposicionar()

        ############# Verifica se a cabeça da cobra colidiu com o debuff ##########
        for debuff in Debuff.guardar_debuffs:
            if pg.Rect(nova_parte[0], nova_parte[1], tamanho_cobras, tamanho_cobras).colliderect(
                    pg.Rect(debuff.x, debuff.y, tamanho_cobras, tamanho_cobras)):
                if len(self.corpo) > 1:  # cobra não desaparece
                    self.corpo.pop()  # tira um bloco do corpo da cobra

                    self.contador_veneno += 1  # debuffs coletados
                    debuff.reposicionar()
            # pontos de veneno não negativam a pontuação total
                if self.pontuacao >= 10:
                    self.pontuacao -= 10
                    self.contador_veneno += 1
                    debuff.reposicionar()
                elif self.pontuacao < 10:
                    self.pontuacao -= self.pontuacao
                    self.contador_veneno += 1
                    debuff.reposicionar()

        ############ verifica se a cabeça da cobra colidiu com a coroa ############
        if visibilidade_coroa and pg.Rect(nova_parte[0], nova_parte[1], tamanho_cobras, tamanho_cobras).colliderect(
                pg.Rect(coroa.x, coroa.y, tamanho_cobras, tamanho_cobras)):
            self.contador_coroas += 1
            coroa.reposicionar()

        self.corpo.insert(0, nova_parte)

        if not self.crescer:
            self.corpo.pop()
        else:
            self.crescer = False

    def desenhar(self):
        for segment in self.corpo:
            pg.draw.rect(
                screen, self.cor, (segment[0], segment[1], tamanho_cobras, tamanho_cobras))

    def resetar(self):
        self.corpo = [self.inicio]
        self.direcao = (0, 0)
        self.crescer = False
        # pontuação não reseta mais, porém o jogador é penalizado em -5 pontos por colidir. Não permite ponto negativo.
        self.pontuacao = self.pontuacao = max(0, self.pontuacao - 5)
        pg.time.delay(500)
