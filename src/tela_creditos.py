import pygame as pg
import sys
from config import *

def mostrar_creditos():
    pg.init()
    pg.mixer.init()

    tela = pg.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pg.display.set_caption("Créditos")
    fonte = pg.font.Font(None, 48)
    clock = pg.time.Clock()

    creditos = [
        "Grupo 9",
        "Anderson Lima - avll",
        "Julio Cesar de Lima - jcbl2",
        "Renata Alves - rgaw",
        "Felipe de Lima - flo",
        "Edenn Weslley - ewss",
        "",
        "Pressione ESC para voltar"
    ]

    while True:
        tela.fill((20, 20, 20))

        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif evento.type == pg.KEYDOWN:
                if evento.key == pg.K_ESCAPE:
                    return  # <- Aqui, para voltar ao menu

        for i, linha in enumerate(creditos):
            texto = fonte.render(linha, True, (255, 255, 255))
            rect = texto.get_rect(center=(LARGURA_TELA//2, 100 + i * 60))
            tela.blit(texto, rect)

        pg.display.flip()
        clock.tick(60)
