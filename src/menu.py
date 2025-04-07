import pygame as pg


import importlib
import os
import tkinter as tk
from tkinter import messagebox
from json import load


from config import *


def show_popup(text):
    # Exibe um popup usando Tkinter
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter


    messagebox.showinfo("Erro", text)
    root.destroy()


def inicializar_menu():
    # Configurações da tela do jogo
    tela = pg.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pg.display.set_caption(TITULO_MENU)



botao_multiplayer = pg.Rect((LARGURA_TELA // 2 - BOTAO_MENU_ALTURA // 2, Y_START_BTN + i * (BOTAO_MENU_ALTURA + ESPACAMENTO_MENU)),
                (BOTAO_MENU_ALTURA, BOTAO_MENU_ALTURA))


#for escondido, gerou todos os botoes?
buttons = [
    botao_multiplayer,
]


# Variáveis para controle de entrada e redesenho
using_mouse = False
selected_index = 0  
redraw = True  # Só redesenha quando necessário


# Carregar logo
DIR_LOGO_MENU = dir_imgs + "logo.jpg"
LOGO = pg.image.load(DIR_LOGO_MENU)
LOGO = pg.transform.scale(LOGO, (250, LOGO_MENU_ALTURA))  


# Função para desenhar os botões
def draw_button(button, text, color):
    pg.draw.rect(tela, color, button, border_radius=10)
    text_render = font.render(text, True, BLACK)
    text_rect = text_render.get_rect(center=button.center)
    tela.blit(text_render, text_rect)

# Função para desenhar o menu 
def draw_menu():
    global redraw
    if redraw:
        tela.fill(GREEN)

        # Desenhar a logo no topo
        tela.blit(logo, (LARGURA_TELA // 2 - logo.get_width() // 2, logo_y_pos))

        mouse_pos = pg.mouse.get_pos()

        for i, button in enumerate(buttons):
            color = HOVER_COLOR if (using_mouse and button.collidepoint(mouse_pos)) or (not using_mouse and i == selected_index) else GRAY
            draw_button(button, button_texts[i], color)

        pg.display.flip()
        redraw = False  # Evita redesenho desnecessário

# Função para carregar e executar um módulo
def carregar_modulo(nome_modulo):
    try:
        modulo = importlib.import_module(nome_modulo)
        if hasattr(modulo, "main"):
            modulo.main()
        else:
            text = f"O módulo '{nome_modulo}' não possui uma função 'main'."
            show_popup(text)
    except ModuleNotFoundError:
            text = f"O módulo '{nome_modulo}' não foi encontrado."
            show_popup(text)
    except ImportError as e:
            text = f"Erro ao importar o módulo '{nome_modulo}': {e}"
            show_popup(text)

# Loop principal do jogo
running = True

while running:
    draw_menu()  # Apenas redesenha se necessário

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False  

        elif event.type == pg.MOUSEBUTTONDOWN:
            using_mouse = True
            for i, button in enumerate(buttons):  # Verifica todos os botões
                if button.collidepoint(event.pos):
                    if i == 0:
                        carregar_modulo("singleplayer")
                    elif i == 1:
                        carregar_modulo("multiplayer")
                    elif i == 2:
                        carregar_modulo("credits")
                    elif i == 3:
                        running = False  
                    redraw = True

        elif event.type == pg.MOUSEMOTION:
            using_mouse = True
            redraw = True  

        elif event.type == pg.KEYDOWN:
            using_mouse = False
            if event.key in (pg.K_UP, pg.K_w):
                selected_index = (selected_index - 1) % len(buttons)
                redraw = True
            elif event.key in (pg.K_DOWN, pg.K_s):
                selected_index = (selected_index + 1) % len(buttons)
                redraw = True
            elif event.key == pg.K_RETURN:
                if selected_index == 0:
                    carregar_modulo("singleplayer")
                elif selected_index == 1:
                    carregar_modulo("multiplayer")
                elif selected_index == 2:
                    carregar_modulo("credits")
                elif selected_index == 3:
                    running = False  
                redraw = True

# Encerra o pygame
pg.quit()
