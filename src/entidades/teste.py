import pygame as pg
import random as rd

pg.init()
# configurações da tela
largura, altura = 920, 800
screen = pg.display.set_mode((largura, altura))
pg.display.set_caption("Jogo da Cobrinha com Labirinto")
tamanho_cobras = 20
tamanho_celula = 20

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
ROSA = (255, 192, 203)
CINZA = (64, 64, 64)  # Veneno ########
DOURADO = (255, 215, 0)  # coroa da vitória #########


class Mapa:
    def __init__(self, largura, altura, tamanho_cobras):
        self.largura = largura
        self.altura = altura
        self.tamanho_cobras = tamanho_cobras

        self.labirinto = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
                0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0,
                0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

    def desenha_labirinto(self, tela):
        for y, linha in enumerate(self.labirinto):
            for x, celula in enumerate(linha):
                if celula == 1:
                    pg.draw.rect(
                        tela, AZUL,
                        (x * self.tamanho_cobras, y * self.tamanho_cobras, self.tamanho_cobras, self.tamanho_cobras))

    def parede(self, x, y):
        """Retorna True se a posição (x, y) for uma parede, False caso contrário"""
        coluna = x // tamanho_cobras
        linha = y // tamanho_cobras
        return self.labirinto[linha][coluna] == 1  # 1 representa parede


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

############# debuff veneno ###########


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


########### coroa para auto win ###########
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


def Grade():
    for x in range(0, largura, tamanho_cobras):
        for y in range(0, altura, tamanho_cobras):
            rect = pg.Rect(x, y, tamanho_cobras, tamanho_cobras)
            pg.draw.rect(screen, 'red', rect, 1)


# jogadores
jogador_1 = Jogadores(60, 400, (0, 255, 0), {
    "up": pg.K_w, "down": pg.K_s, "left": pg.K_a, "right": pg.K_d
})
jogador_2 = Jogadores(840, 400, (255, 192, 203), {
    "up": pg.K_UP, "down": pg.K_DOWN, "left": pg.K_LEFT, "right": pg.K_RIGHT
})
########### VARIAVEIS NOVAS ###########
Map = Mapa(largura, altura, tamanho_cobras)
coroando = Coroas(Map)

############ aumentar número de buffs e debuffs ###########
Buff_1.numero_buffs(Map, 15)
Debuff.numero_debuffs(Map, 10)

running = True
clock = pg.time.Clock()
mostrar_grade = False  # Variável para controlar a exibição da grade
visibilidade_coroa = False
clock_contagem_coroa = pg.time.get_ticks()
tempo_espera_coroa = 0

while running:
    screen.fill("black")
    clock.tick(7)
    keys = pg.key.get_pressed()
    tempo_atual = pg.time.get_ticks()

    Map.desenha_labirinto(screen)

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
        pg.quit()

    if jogador_1.corpo and jogador_2.corpo:
        if jogador_1.corpo[0] in jogador_2.corpo or jogador_2.corpo[0] in jogador_1.corpo:
            jogador_1.resetar()
            jogador_2.resetar()

    jogador_1.desenhar()
    jogador_2.desenhar()

    ############## mudança no número de buffs e debuffs #################
    for buff in Buff_1.guardar_buffs:
        buff.desenhar_buff1()

    for debuff in Debuff.guardar_debuffs:
        debuff.desenhar_debuff1()

    ######### COROA VISIVEL NO MAPA ########
    if visibilidade_coroa:
        coroando.desenhar_coroa()

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