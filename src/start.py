import pygame as pg


from config import *
from tela import grade
from entidades import *


# Fatorar em funcoes e classes e outros
def iniciar_jogador(cor, coords_iniciais, controle, velocidade):
    jogador = Jogador(cor, controle, coords_iniciais, velocidade)

    return jogador


def iniciar_entidades(azul, verde, jog_1_coord_inic, jog_2_coord_inic,
                      CONTROLE_WASD, CONTROLE_SETAS, velocidade):
    '''
    Construir o(s) jogador(es), item de crescimento
    '''
    # Construindo jogadores
    jogador_1 = iniciar_jogador(verde, jog_1_coord_inic, CONTROLE_WASD, velocidade)
    jogador_2 = iniciar_jogador(azul, jog_2_coord_inic, CONTROLE_SETAS, velocidade)

    # Construindo item que faz a cobra crescer
    item_crescer = ItemCrescer(dados_tela, velocidade)
    

    return jogador_1, jogador_2, item_crescer


def iniciar_janela_jogo(titulo_janela, altura_tela, largura_tela):
    # Iniciando a tela do jogo
    pg.init()
    pg.display.set_caption(titulo_janela)

    tela = pg.display.set_mode((largura_tela, altura_tela))

    
    return tela


def gerenciar_eventos_jogo():
    '''
    Gerenciar os eventos do jogo
    '''
    for event in pg.event.get():
        if event.type == pg.QUIT: # Evento de fechar a janela
            running = False
        elif event.type == pg.KEYDOWN: # Tecla pressionada
            if event.key == pg.K_j:    # Alterna a grade ao pressionar J
                mostrar_grade = not mostrar_grade


def gerenciar_pontuacoes(jogador_1, jogador_2, tela):
    '''
    Gerenciar pontuacoes dos jogadores na tela
    '''
    # Construindo objeto de texto que representam as pontuacoes
    font = pg.font.SysFont("Arial", 24)
    pontos_texto_1 = font.render(f"Jogador 1: {jogador_1.pontuacao}", True, (255, 255, 255))
    pontos_texto_2 = font.render(f"Jogador 2: {jogador_2.pontuacao}", True, (255, 255, 255))

    # Desenhar pontuacoes na tela
    tela.blit(pontos_texto_1, (10, 10))
    tela.blit(pontos_texto_2, (largura_tela - pontos_texto_2.get_width() - 10, 10))


def gerenciar_entidades(keys, jogador_1, jogador_2, item_crescer, tela):
    '''
    Gerenciar periodicamente as entidadades: jogadores e itens
    '''
    # Atualizar jogadores
    jogador_1.update(keys, item_crescer, dados_tela)
    jogador_2.update(keys, item_crescer, dados_tela)


    if jogador_1.corpo and jogador_2.corpo:
        # Se uma das cobras passa por cima da outra
        if jogador_1.corpo[0] in jogador_2.corpo or jogador_2.corpo[0] in jogador_1.corpo:
            jogador_1.resetar()
            jogador_2.resetar()

    jogador_1.desenhar(tela)
    jogador_2.desenhar(tela)
    item_crescer.desenhar_buff1(tela, velocidade)


def iniciar_loop(jogador_1, jogador_2, item_crescer, tela):
    # Variaveis de controle do jogo
    clock = pg.time.Clock()
    running = True
    mostrar_grade = False  # Variável para controlar a exibição da grade

    # Loop que roda o jogo
    while running:
        # Atualizar tela
        tela.fill("black")
        clock.tick(7)

        # Receber teclas pressionadas pelos jogadores
        keys = pg.key.get_pressed()


        gerenciar_eventos_jogo()
        gerenciar_entidades(keys, jogador_1, jogador_2, item_crescer, tela)

        if mostrar_grade:
            grade()

        # Gerenciar pontuacoes
        gerenciar_pontuacoes(jogador_1, jogador_2, tela)

        # Atualizar tela
        pg.display.flip()


tela = iniciar_janela_jogo(titulo_janela, altura_tela, largura_tela)

# Criando entidades
jogador_1, jogador_2, item_crescer = iniciar_entidades(azul, verde, jog_1_coord_inic,
                                                    jog_2_coord_inic, CONTROLE_WASD,
                                                    CONTROLE_SETAS, velocidade)

iniciar_loop(jogador_1, jogador_2, item_crescer, tela)

# Terminar jogo
pg.quit()