import pygame
import importlib
import os
import tkinter as tk
from tkinter import messagebox
from json import load
from config import *

# Inicializa o Pygame
pygame.init()
pygame.mixer.init()

def show_popup(text):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Erro", text)
    root.destroy()

# Configurações da tela do jogo
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption(titulo_menu)

font_path = pygame.font.match_font('comicsansms')  # Ou adicione uma TTF customizada
font = pygame.font.Font(font_path, 36)

hover_sound_path = os.path.join("assets", "hover_sound.wav")
click_sound_path = os.path.join("assets", "mouse_click.wav")
hover_sound = pygame.mixer.Sound(hover_sound_path) if os.path.exists(hover_sound_path) else None
click_sound = pygame.mixer.Sound(click_sound_path) if os.path.exists(click_sound_path) else None

fundo_path = os.path.join("assets", "fundo_menu.png")
fundo = pygame.image.load(fundo_path) if os.path.exists(fundo_path) else None
fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela)) if fundo else None

# Tamanho dos botões
tamanho_x = tamanho_x_botao_menu
altura_y = tamanho_y_botao_menu

button_texts = ["Jogar", "Créditos", "Sair"]
num_botoes = len(button_texts)
total_altura = num_botoes * altura_y + (num_botoes - 1) * espacamento_menu
y_start = (altura_tela - total_altura) // 2

buttons = []
for i in range(num_botoes):
    x = (largura_tela - tamanho_x) // 2
    y = y_start + i * (altura_y + espacamento_menu)
    rect = pygame.Rect((x, y), (tamanho_x, altura_y))
    buttons.append(rect)

# Controle
selected_index = 0
using_mouse = False
redraw = True
hover_states = [False] * len(buttons)

# Cores
BACKGROUND = (10, 20, 30)
BOTAO = (50, 50, 50)
HOVER = (0, 170, 160)
TEXTO = (255, 255, 255)
BORDA = (255, 255, 255)

# Funções de desenho
def draw_button(rect, text, active=False):
    cor = HOVER if active else BOTAO
    pygame.draw.rect(tela, cor, rect, border_radius=12)
    pygame.draw.rect(tela, BORDA, rect, 3, border_radius=12)

    txt = font.render(text, True, TEXTO)
    sombra = font.render(text, True, (0, 0, 0))
    sombra_rect = sombra.get_rect(center=(rect.centerx + 2, rect.centery + 2))
    txt_rect = txt.get_rect(center=rect.center)

    tela.blit(sombra, sombra_rect)
    tela.blit(txt, txt_rect)

def draw_menu():
    if fundo:
        tela.blit(fundo, (0, 0))
    else:
        tela.fill(BACKGROUND)

    mouse_pos = pygame.mouse.get_pos()

    for i, botao in enumerate(buttons):
        hovering = botao.collidepoint(mouse_pos)
        if hovering and not hover_states[i] and hover_sound:
            hover_sound.play()
        hover_states[i] = hovering

        ativo = (using_mouse and hovering) or (not using_mouse and i == selected_index)
        draw_button(botao, button_texts[i], ativo)

    pygame.display.flip()

# Função para carregar módulos
def carregar_modulo(acao):
    if acao == "jogar":
        nome_modulo = "entidades.main"
    elif acao == "credits":
        show_popup("Créditos:\nFeito😎")
        return
    else:
        show_popup(f"Ação desconhecida: {acao}")
        return

    try:
        modulo = importlib.import_module(nome_modulo)
        if hasattr(modulo, "main"):
            pygame.display.quit()
            modulo.main()
        else:
            show_popup(f"O módulo '{nome_modulo}' não possui uma função 'main'.")
    except ModuleNotFoundError:
        show_popup(f"O módulo '{nome_modulo}' não foi encontrado.")
    except ImportError as e:
        show_popup(f"Erro ao importar o módulo '{nome_modulo}': {e}")

# Loop principal
running = True
while running:
    draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            using_mouse = True
            for i, botao in enumerate(buttons):
                if botao.collidepoint(event.pos):
                    if click_sound:
                        click_sound.play()
                    if i == 0:
                        carregar_modulo("jogar")
                    elif i == 1:
                        carregar_modulo("credits")
                    elif i == 2:
                        running = False
                    redraw = True

        elif event.type == pygame.MOUSEMOTION:
            using_mouse = True
            redraw = True

        elif event.type == pygame.KEYDOWN:
            using_mouse = False
            if event.key in (pygame.K_UP, pygame.K_w):
                previous_index = selected_index
                selected_index = (selected_index - 1) % num_botoes
                if selected_index != previous_index and hover_sound:
                    hover_sound.play()
                redraw = True
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                previous_index = selected_index
                selected_index = (selected_index + 1) % num_botoes
                if selected_index != previous_index and hover_sound:
                    hover_sound.play()
                redraw = True
            elif event.key == pygame.K_RETURN:
                if click_sound:
                    click_sound.play()
                if selected_index == 0:
                    carregar_modulo("jogar")
                elif selected_index == 1:
                    carregar_modulo("credits")
                elif selected_index == 2:
                    running = False
                redraw = True


pygame.quit()
