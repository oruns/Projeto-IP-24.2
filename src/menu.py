import pygame as pg


import os


from config import *
import menu as mn


# Inicializa o Pygame
pg.init()
pg.mixer.init()


# Iniciando o menu
# funcao de desenhar menu
tela = mn.iniciar_tela(ALTURA_TELA, LARGURA_TELA, TITULO_MENU)
font = mn.adicionar_fonte()
fundo = mn.construindo_fundo(ALTURA_TELA, LARGURA_TELA, get_path_asset)
hover_sound, click_sound = mn.adicionar_som(get_path_asset)


num_botoes = len(TXT_BTNS_MENU)
total_altura_menu = num_botoes * BOTAO_MENU_ALTURA + (num_botoes - 1) * ESPACAMENTO_MENU
y_start = (ALTURA_TELA - total_altura_menu) // 2


# Controle, indica o botao pressionado no menu
selected_index = 0


buttons = mn.construindo_botoes(BOTAO_MENU_ALTURA, BOTAO_MENU_LARGURA,
                             ESPACAMENTO_MENU, LARGURA_TELA,
                             num_botoes, y_start)


w = True
hover_states = [False] * len(buttons)


COR_BOTAO_MENU = (50, 50, 50)
COR_TEXTO_MENU = (255, 255, 255)


# Posições dos botões
y_start = ALTURA_TELA // 2 - (2 * (BOTAO_MENU_ALTURA + ESPACAMENTO_MENU) // 2)


# Posições da logo (logo acima dos botões)
logo_height = 200
logo_y_pos = y_start - logo_height - 20  # Logo acima dos botões, com um espaçamento de 20 pixels


# Variáveis para controle de entrada e redesenho
using_mouse = False
selected_index = 0  
redraw = True  # Só redesenha quando necessário


# Carregando logo
# logo_path = get_path_asset('logo.jpg')
os.chdir(DIR_IMGS)

logo = pg.image.load('logo.jpg')
logo = pg.transform.scale(logo, (250, logo_height))  


# Preenchendo fundo da tela
if fundo:
    tela.blit(fundo, (0, 0))
else:
    tela.fill(COR_BACKG_RESERVA_MENU)


mouse_pos = pg.mouse.get_pos()

# Desenhando botoes na tela
for i, botao in enumerate(buttons):
    hovering = botao.collidepoint(mouse_pos)


    if hovering and not hover_states[i] and hover_sound:
        hover_sound.play()
    hover_states[i] = hovering


    ativo = (using_mouse and hovering) or (not using_mouse and i == selected_index)
    mn.desenhando_botao(COR_BORDA_MENU, COR_BOTAO_MENU, COR_HOVER_MENU, COR_TEXTO_MENU,
                        font, botao, tela, TXT_BTNS_MENU[i], ativo)


# Atualizando a tela
pg.display.flip()


# Loop principal
running = True

while running:
    mn.desenhando_fundo(COR_BACKG_RESERVA_MENU, fundo, tela)

    # Tratando os eventos do jogo
    for event in pg.event.get():
        # Terminando o jogo
        if event.type == pg.QUIT:
            running = False  

        # Qualquer botao do mouse eh pressionado
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
                    elif i == 2:
                        running = False
                    redraw = True

        # Mouse em movimento
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
                os.chdir('../src/')

                if click_sound:
                    click_sound.play()
                if selected_index == 0:
                    mn.carregar_modulo("jogar")
                elif selected_index == 1:
                    mn.carregar_modulo("credits")
                elif selected_index == 2:
                    running = False
                redraw = True


# Encerra o Pygame
pg.quit()