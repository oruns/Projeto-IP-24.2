import pygame as pg
import random as rd


from json import load


from jogador import Jogador


# diretorio melhor maneira?
# Abrindo JSON
dir_tela_config = "../../config/tela.json" 
with open(dir_tela_config, "r", encoding="utf-8") as arq:
    dados = load(arq)

# Recebendo dados do JSON
largura_tela = dados['largura']
altura_tela = dados['altura']


pg.init()

# Configurações da tela
largura_tela_tela, altura_tela_tela = 920, 800


screen = pg.display.set_mode((largura_tela, altura_tela))
pg.display.set_caption("Jogo da Cobrinha-nome generico")


# Colocar dados em arquivo separado


# Dados das cobras
tamanho_cobras = 20
velocidade_cobra = 20

jog_1_coord_inic = (20, 20)
jog_2_coord_inic = (880, 20)


# Cores
verde = (0, 255, 0)
azul = (0, 0, 255)



controle_wasd = {
    "up": pg.K_w, "down": pg.K_s, "left": pg.K_a, "right": pg.K_d
}

controle_setas = {
    "up": pg.K_UP, "down": pg.K_DOWN, "left": pg.K_LEFT, "right": pg.K_RIGHT
}


class Buff_1:
    def __init__(self):
        self.reposicionar()
        self.cor = (128, 0, 128)  # buff 1 é o bloco roxo

    def reposicionar(self):
        self.x = rd.randint(0, (largura_tela - tamanho_cobras) // tamanho_cobras) * tamanho_cobras
        self.y = rd.randint(0, (altura_tela - tamanho_cobras) // tamanho_cobras) * tamanho_cobras

    def desenhar_buff1(self):
        pg.draw.rect(screen, self.cor, (self.x, self.y, tamanho_cobras, tamanho_cobras))


def Grade():
    # Desenhando a cobra
    for x in range(0, largura_tela, tamanho_cobras):
        for y in range(0, altura_tela, tamanho_cobras):
            # Construindo cobra no objeto do pygame
            rect = pg.Rect(x, y, tamanho_cobras, tamanho_cobras)

            # Desenhando na tela
            pg.draw.rect(screen, 'red', rect, 1)


# Construindo jogadores
jogador_1 = Jogadores(jog_1_coord_inic, verde, controle_wasd)
jogador_2 = Jogadores(jog_2_coord_inic, azul, controle_setas)

buffando1 = Buff_1()

running = True
clock = pg.time.Clock()
mostrar_grade = False  # Variável para controlar a exibição da grade

while running:
    screen.fill("black")
    clock.tick(7)  
    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_j:  # Alterna a grade ao pressionar J
                mostrar_grade = not mostrar_grade

    jogador_1.update(keys, buffando1)
    jogador_2.update(keys, buffando1)

    if jogador_1.corpo and jogador_2.corpo:
        if jogador_1.corpo[0] in jogador_2.corpo or jogador_2.corpo[0] in jogador_1.corpo:
            jogador_1.resetar()
            jogador_2.resetar()

    jogador_1.desenhar()
    jogador_2.desenhar()
    buffando1.desenhar_buff1()

    if mostrar_grade:
        Grade()

    font = pg.font.SysFont("Arial", 24)
    pontos_texto_1 = font.render(f"Jogador 1: {jogador_1.pontuacao}", True, (255, 255, 255))
    pontos_texto_2 = font.render(f"Jogador 2: {jogador_2.pontuacao}", True, (255, 255, 255))

    screen.blit(pontos_texto_1, (10, 10))
    screen.blit(pontos_texto_2, (largura_tela - pontos_texto_2.get_width() - 10, 10))

    pg.display.flip()

pg.quit()
