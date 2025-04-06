import pygame as pg


#tamanho cobra constantes
#Colocar dados em arquivo separado
class Jogador:
    def __init__(self, altura_tela, largura_tela, coord_inicial, cor, teclas_direcoes, velocidade_cobra):
        self.receber_dados_tela(altura_tela, largura_tela)
        self.receber_dados_movimento(coord_inicial, teclas_direcoes, velocidade_cobra)
        self.montar_corpo(cor, coord_inicial)

        self.pontuacao = 0
    
    
    def montar_corpo(self, cor, coord_inicial):
        self.cor = cor
        self.corpo = [self.coord_inicial]
        self.crescer = False


    def receber_dados_tela(self, altura_tela, largura_tela):
        '''
        Receber dados relativos a janela do jogo
        '''
        self.altura_tela = altura_tela 
        self.largura_tela = largura_tela
    

    def receber_dados_movimento(self, coord_inicial, teclas_direcoes, velocidade_cobra):
        '''
        Receber dados relativos ao movimento dos jogadores
        '''
        self.posicao = (0, 0) # Começa parado
        self.velocidade = velocidade_cobra
        self.coord_inicial = coord_inicial
        self.teclas_direcoes = teclas_direcoes


    # Self dentro das funcoes ou como parametros? Contexto?
    def analisar_movimento(self, tecla_pressionada):
        '''
        Mudar a direcao do jogador, segundo as teclas do teclado
        '''
        teclas = self.teclas 
        direcao = self.direcao
        velocidade = self.velocidade

        tecla_up = teclas['up']
        tecla_down = teclas['down']
        tecla_left = teclas['left']
        tecla_right = teclas['right']

        if tecla_pressionada[tecla_up] and direcao != (0, velocidade):
            self.direcao = (0, -velocidade)
        if tecla_pressionada[tecla_down] and direcao != (0, -velocidade):
            self.direcao = (0, velocidade)
        if tecla_pressionada[tecla_left] and direcao != (velocidade, 0):
            self.direcao = (-velocidade, 0)
        if tecla_pressionada[tecla_right] and direcao != (-velocidade, 0):
            self.direcao = (velocidade, 0)


    def update(self, tecla_pressionada, buff_1):
        '''
        Atualizar o jogador de acordo com o andamento do jogo
        '''
        self.analisar_movimento(tecla_pressionada)


        corpo = self.corpo

        if corpo:
            nova_parte = (corpo[0][0] + self.direcao[0], corpo[0][1] + self.direcao[1])
        else:
            nova_parte = self.inicio


        if (nova_parte[0] < 0 or nova_parte[0] >= self.largura_tela or
                nova_parte[1] < 0 or nova_parte[1] >= self.altura_tela):
            self.resetar()
            return
        if nova_parte in corpo[1:]:
            self.resetar()
            return
        if pg.Rect(nova_parte[0], nova_parte[1], tamanho_inicial_cobra, tamanho_inicial_cobra).colliderect(
                pg.Rect(buff_1.x, buff_1.y, tamanho_inicial_cobra, tamanho_inicial_cobra)):
            self.pontuacao += 10
            self.crescer = True
            buff_1.reposicionar()

        corpo.insert(0, nova_parte)

        if not self.crescer:
            corpo.pop()
        else:
            self.crescer = False

    def desenhar(self):
        for segment in self.corpo:
            pg.draw.rect(screen, self.cor, (segment[0], segment[1], tamanho_inicial_cobra, tamanho_inicial_cobra))

    def resetar(self):
        self.corpo = [self.inicio]
        self.direcao = (0, 0)
        self.crescer = False
        self.pontuacao = 0
        pg.time.delay(500)