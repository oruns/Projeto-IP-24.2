import pygame as pg
import os
from config import *
import menu as mn

# Inicializa o Pygame
pg.init()
pg.mixer.init()

# Iniciando o menu
tela = mn.iniciar_tela(ALTURA_TELA, LARGURA_TELA, TITULO_MENU)
font = mn.adicionar_fonte()
hover_sound, click_sound = mn.adicionar_som(get_path_asset)

# Carregando imagem de fundo do menu
os.chdir(DIR_IMGS)
fundo = pg.image.load('menu.png')
fundo = pg.transform.scale(fundo, (LARGURA_TELA, ALTURA_TELA))

# Parâmetros dos botões
BOTAO_MENU_LARGURA = 532
BOTAO_MENU_ALTURA = 90
ESPACAMENTO_MENU = 8
BORDA_BOTAO_MENU = 5
POSICAO_Y_INICIAL_BOTAO = 510

# Controle dos botões
TXT_BTNS_MENU = ["Jogar", "Créditos", "Sair"]
num_botoes = len(TXT_BTNS_MENU)

selected_index = 0
using_mouse = False
redraw = True
hover_states = [False] * num_botoes

buttons = mn.construindo_botoes(
    BOTAO_MENU_ALTURA,
    BOTAO_MENU_LARGURA,
    ESPACAMENTO_MENU,
    LARGURA_TELA,
    num_botoes,
    POSICAO_Y_INICIAL_BOTAO
)

# Loop principal
running = True
while running:
    mn.desenhando_fundo(COR_BACKG_RESERVA_MENU, fundo, tela)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.MOUSEBUTTONDOWN:
            using_mouse = True
            for i, botao in enumerate(buttons):
                if botao.collidepoint(event.pos):
                    if click_sound:
                        click_sound.play()
                    if i == 0:
                        mn.carregar_modulo("jogar")
                    elif i == 1:
                        mn.carregar_modulo("credits")
                        pg.event.clear()  # <- ESSENCIAL AQUI
                    elif i == 2:
                        running = False
                    redraw = True

        elif event.type == pg.MOUSEMOTION:
            using_mouse = True
            redraw = True

        elif event.type == pg.KEYDOWN:
            using_mouse = False
            if event.key in (pg.K_UP, pg.K_w):
                previous_index = selected_index
                selected_index = (selected_index - 1) % num_botoes
                if selected_index != previous_index and hover_sound:
                    hover_sound.play()
                redraw = True
            elif event.key in (pg.K_DOWN, pg.K_s):
                previous_index = selected_index
                selected_index = (selected_index + 1) % num_botoes
                if selected_index != previous_index and hover_sound:
                    hover_sound.play()
                redraw = True
            elif event.key == pg.K_RETURN:
                if click_sound:
                    click_sound.play()
                if selected_index == 0:
                    os.chdir('../src/')  
                    mn.carregar_modulo("jogar")
                elif selected_index == 1:
                    mn.carregar_modulo("credits")
                    pg.event.clear()  # <- Limpa os eventos ao voltar dos créditos
                elif selected_index == 2:
                    running = False
                redraw = True


    if redraw:
        mouse_pos = pg.mouse.get_pos()
        for i, botao in enumerate(buttons):
            hovering = botao.collidepoint(mouse_pos)
            if hovering and not hover_states[i] and hover_sound:
                hover_sound.play()
            hover_states[i] = hovering

            ativo = (using_mouse and hovering) or (not using_mouse and i == selected_index)
            mn.desenhando_botao(COR_BORDA_MENU, COR_BOTAO_MENU, COR_HOVER_MENU, COR_TEXTO_MENU,
                                font, botao, tela, TXT_BTNS_MENU[i], ativo, BORDA_BOTAO_MENU)

        pg.display.flip()
        redraw = False

pg.quit()
