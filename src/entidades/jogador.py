import pygame as pg


#tamanho cobra constantes
<<<<<<< HEAD
# Colocar dados em arquivo separado
class Jogador:
    def __init__(self, altura_tela, largura_tela, coord_inicial, cor, teclas_direcoes, velocidade_cobra):
        self.receber_dados_tela(altura_tela, largura_tela)
        self.receber_dados_movimento(coord_inicial, teclas_direcoes, velocidade_cobra)
=======
#Colocar dados em arquivo separado
class Jogador:
    def __init__(self, cor, controles, coord_inicial, velocidade):
        self.receber_dados_movimento(controles, velocidade)
>>>>>>> 311b799e66e8cc5e7890c417ce411e52da67e5bd
        self.montar_corpo(cor, coord_inicial)

        self.pontuacao = 0
    
    
    def montar_corpo(self, cor, coord_inicial):
<<<<<<< HEAD
=======
        self.coord_inicial = coord_inicial
>>>>>>> 311b799e66e8cc5e7890c417ce411e52da67e5bd
        self.cor = cor
        self.corpo = [self.coord_inicial]
        self.crescer = False


<<<<<<< HEAD
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
=======
    def receber_dados_movimento(self, controles, velocidade):
        '''
        Receber dados relativos ao movimento dos jogadores
        '''
        self.direcao_atual = (0, 0) # Começa parado
        self.velocidade = velocidade
        self.controles = controles


    def mudar_direcao(self, controles, direcao_atual, tecla_pressionada, velocidade):
        tecla_up = controles['up']
        tecla_down = controles['down']
        tecla_left = controles['left']
        tecla_right = controles['right']


        if tecla_pressionada[tecla_up] and direcao_atual != (0, velocidade):
            self.direcao_atual = (0, -velocidade)
        if tecla_pressionada[tecla_down] and direcao_atual != (0, -velocidade):
            self.direcao_atual = (0, velocidade)
        if tecla_pressionada[tecla_left] and direcao_atual != (velocidade, 0):
            self.direcao_atual = (-velocidade, 0)
        if tecla_pressionada[tecla_right] and direcao_atual != (-velocidade, 0):
            self.direcao_atual = (velocidade, 0) 
>>>>>>> 311b799e66e8cc5e7890c417ce411e52da67e5bd


    # Self dentro das funcoes ou como parametros? Contexto?
    def analisar_movimento(self, tecla_pressionada):
        '''
        Mudar a direcao do jogador, segundo as teclas do teclado
        '''
<<<<<<< HEAD
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
=======
        controles = self.controles
        direcao_atual = self.direcao_atual
        velocidade = self.velocidade

        self.mudar_direcao(controles, direcao_atual, tecla_pressionada, velocidade)


    def update(self, tecla_pressionada, buff_1, dados_tela):
        '''
        Atualizar o jogador de acordo com o andamento do jogo
        '''
        # Atualizar o movimento do jogador
>>>>>>> 311b799e66e8cc5e7890c417ce411e52da67e5bd
        self.analisar_movimento(tecla_pressionada)


        corpo = self.corpo
<<<<<<< HEAD

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
        if pg.Rect(nova_parte[0], nova_parte[1], tamanho_cobras, tamanho_cobras).colliderect(
                pg.Rect(buff_1.x, buff_1.y, tamanho_cobras, tamanho_cobras)):
            self.pontuacao += 10
            self.crescer = True
            buff_1.reposicionar()
=======
        direcao_atual = self.direcao_atual
        coord_inicial = self.coord_inicial
        velocidade = self.velocidade

        
        altura_tela = dados_tela['altura']
        largura_tela = dados_tela['largura']

        # Se o corpo da cobra ainda tem partes,
        # Falta comentar
        if corpo:
            # Falta comentar
            nova_parte = (corpo[0][0] + direcao_atual[0], corpo[0][1] + direcao_atual[1])
        else:
            nova_parte = coord_inicial


        # Se a cobrar sair da tela, recomecar jogo
        if (nova_parte[0] < 0 or nova_parte[0] >= largura_tela or
                nova_parte[1] < 0 or nova_parte[1] >= altura_tela):
            self.resetar()
            return
        # Falta comentar
        if nova_parte in corpo[1:]:
            self.resetar()
            return
        if pg.Rect(nova_parte[0], nova_parte[1], velocidade, velocidade).colliderect(
                pg.Rect(buff_1.x, buff_1.y, velocidade, velocidade)):
            self.pontuacao += 10
            self.crescer = True
            buff_1.reposicionar(altura_tela, largura_tela, velocidade)
>>>>>>> 311b799e66e8cc5e7890c417ce411e52da67e5bd

        corpo.insert(0, nova_parte)

        if not self.crescer:
            corpo.pop()
        else:
            self.crescer = False

<<<<<<< HEAD
    def desenhar(self):
        for segment in self.corpo:
            pg.draw.rect(screen, self.cor, (segment[0], segment[1], tamanho_cobras, tamanho_cobras))

    def resetar(self):
        self.corpo = [self.inicio]
        self.direcao = (0, 0)
=======

    def desenhar(self, tela):
        velocidade = self.velocidade
        corpo = self.corpo

        for segment in corpo:
            pg.draw.rect(tela, self.cor, (segment[0], segment[1], velocidade, velocidade))


    def resetar(self):
        self.corpo = [self.coord_inicial]
        self.direcao_atual = (0, 0)
>>>>>>> 311b799e66e8cc5e7890c417ce411e52da67e5bd
        self.crescer = False
        self.pontuacao = 0
        pg.time.delay(500)