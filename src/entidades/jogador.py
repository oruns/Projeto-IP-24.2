import pygame as pg


#tamanho cobra constantes
#Colocar dados em arquivo separado
class Jogador:
    def __init__(self, cor, controles, coord_inicial, velocidade):
        self.receber_dados_movimento(coord_inicial, controles, velocidade)
        self.montar_corpo(cor)

        self.pontuacao = 0
    
    
    def montar_corpo(self, cor):
        self.cor = cor
        self.corpo = [self.coord_inicial]
        self.crescer = False


    def receber_dados_movimento(self, coord_inicial, controles, velocidade):
        '''
        Receber dados relativos ao movimento dos jogadores
        '''
        self.direcao_atual = (0, 0) # Começa parado
        self.velocidade = velocidade
        self.coord_inicial = coord_inicial
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


    # Self dentro das funcoes ou como parametros? Contexto?
    def analisar_movimento(self, tecla_pressionada):
        '''
        Mudar a direcao do jogador, segundo as teclas do teclado
        '''
        controles = self.controles
        direcao_atual = self.direcao_atual
        velocidade = self.velocidade

        self.mudar_direcao(controles, direcao_atual, tecla_pressionada, velocidade)


    def update(self, tecla_pressionada, buff_1, dados_tela):
        '''
        Atualizar o jogador de acordo com o andamento do jogo
        '''
        # Atualizar o movimento do jogador
        self.analisar_movimento(tecla_pressionada)


        corpo = self.corpo
        direcao_atual = self.direcao_atual
        direcao_atual = self.direcao_atual
        velocidade = self.velocidade

        
        altura_tela = dados_tela['altura']
        largura_tela = dados_tela['largura']

        # Se o corpo da cobra ainda tem partes,
        # Falta comentar
        if corpo:
            # Falta comentar
            nova_parte = (corpo[0][0] + direcao_atual[0], corpo[0][1] + direcao_atual[1])
        else:
            nova_parte = direcao_atual


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
            buff_1.reposicionar()

        corpo.insert(0, nova_parte)

        if not self.crescer:
            corpo.pop()
        else:
            self.crescer = False


    def desenhar(self, tela):
        velocidade = self.velocidade
        corpo = self.corpo

        for segment in corpo:
            pg.draw.rect(tela, self.cor, (segment[0], segment[1], velocidade, velocidade))


    def resetar(self):
        self.corpo = [self.inicio]
        self.direcao = (0, 0)
        self.crescer = False
        self.pontuacao = 0
        pg.time.delay(500)