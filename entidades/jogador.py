import pygame as pg

# Colocar dados em arquivo separado
class Jogador:
    def __init__(self, altura_tela, largura_tela, coord_inicial, cor, teclas, velocidade):
        self.receber_dados_tela(altura_tela, largura_tela)

        self.cor = cor
        self.corpo = [self.inicio]
        self.crescer = False

        self.teclas = teclas

        self.pontuacao = 0

    

    def receber_dados_tela(self, altura_tela, largura_tela):
        '''
        Receber dados relativos a janela do jogo
        '''
        self.altura_tela = altura_tela 
        self.largura_tela = largura_tela
    

    def receber_dados_movimento(self, coord_inicial, velocidade):
        '''
        Receber dados relativos ao movimento dos jogadores
        '''
        self.direcao = (0, 0) # Começa parado
        self.velocidade = velocidade
        self.coord_inicial = coord_inicial


    def update(self, keys, buff_1):
        if keys[self.teclas["up"]] and self.direcao != (0, self.velocidade):
            self.direcao = (0, -self.velocidade)
        if keys[self.teclas["down"]] and self.direcao != (0, -self.velocidade):
            self.direcao = (0, self.velocidade)
        if keys[self.teclas["left"]] and self.direcao != (self.velocidade, 0):
            self.direcao = (-self.velocidade, 0)
        if keys[self.teclas["right"]] and self.direcao != (-self.velocidade, 0):
            self.direcao = (self.velocidade, 0)

        if self.corpo:
            nova_parte = (self.corpo[0][0] + self.direcao[0], self.corpo[0][1] + self.direcao[1])
        else:
            nova_parte = self.inicio

        if (nova_parte[0] < 0 or nova_parte[0] >= self.largura_tela or
                nova_parte[1] < 0 or nova_parte[1] >= self.altura_tela):
            self.resetar()
            return
        if nova_parte in self.corpo[1:]:
            self.resetar()
            return
        if pg.Rect(nova_parte[0], nova_parte[1], tamanho_cobras, tamanho_cobras).colliderect(
                pg.Rect(buff_1.x, buff_1.y, tamanho_cobras, tamanho_cobras)):
            self.pontuacao += 10
            self.crescer = True
            buff_1.reposicionar()

        self.corpo.insert(0, nova_parte)

        if not self.crescer:
            self.corpo.pop()
        else:
            self.crescer = False

    def desenhar(self):
        for segment in self.corpo:
            pg.draw.rect(screen, self.cor, (segment[0], segment[1], tamanho_cobras, tamanho_cobras))

    def resetar(self):
        self.corpo = [self.inicio]
        self.direcao = (0, 0)
        self.crescer = False
        self.pontuacao = 0
        pg.time.delay(500)