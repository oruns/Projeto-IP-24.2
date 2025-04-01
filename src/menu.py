import pygame
import importlib
import tkinter as tk
from tkinter import messagebox

# Importa o módulo de configurações
import config as g  

# Inicializa o Pygame
pygame.init()

def show_popup(text):
    #Exibe um popup usando Tkinter
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    messagebox.showinfo("Erro", text)
    root.destroy()

# Configurações da tela do jogo
screen = pygame.display.set_mode((g.largura, g.altura))
pygame.display.set_caption(f"{g.NOME_DO_JOGO}")

# Definição das cores (extraídas do config)
WHITE = g.WHITE
BLACK = g.BLACK
GRAY = g.GRAY
DARK_GRAY = g.DARK_GRAY
GREEN = g.GREEN
HOVER_COLOR = g.HOVER_COLOR  # Cor para hover

# Define a fonte para o texto nos botões
font = pygame.font.Font(None, 50)

# Tamanho dos botões e espaçamento
button_width, button_height = 250, 60
spacing = 20

# Posições dos botões
y_start = g.altura // 2 - (2 * (button_height + spacing) // 2)

# Posições da logo (logo acima dos botões)
logo_height = 200  
logo_y_pos = y_start - logo_height - 20  # Logo acima dos botões, com um espaçamento de 20 pixels

buttons = [
    pygame.Rect((g.largura // 2 - button_width // 2, y_start + i * (button_height + spacing)),
                (button_width, button_height))
    for i in range(4)
]
button_texts = ["Singleplayer", "Multiplayer", "Créditos", "Sair"]

# Variáveis para controle de entrada e redesenho
using_mouse = False
selected_index = 0  
redraw = True  # Só redesenha quando necessário

# Carregar logo
logo = g.game_logo
logo = pygame.transform.scale(logo, (250, logo_height))  # Ajusta o tamanho da logo

# Função para desenhar os botões
def draw_button(button, text, color):
    pygame.draw.rect(screen, color, button, border_radius=10)
    text_render = font.render(text, True, BLACK)
    text_rect = text_render.get_rect(center=button.center)
    screen.blit(text_render, text_rect)

# Função para desenhar o menu 
def draw_menu():
    global redraw
    if redraw:
        screen.fill(GREEN)

        # Desenhar a logo no topo
        screen.blit(logo, (g.largura // 2 - logo.get_width() // 2, logo_y_pos))

        mouse_pos = pygame.mouse.get_pos()

        for i, button in enumerate(buttons):
            color = HOVER_COLOR if (using_mouse and button.collidepoint(mouse_pos)) or (not using_mouse and i == selected_index) else GRAY
            draw_button(button, button_texts[i], color)

        pygame.display.flip()
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

        elif event.type == pygame.MOUSEBUTTONDOWN:
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

        elif event.type == pygame.MOUSEMOTION:
            using_mouse = True
            redraw = True  

        elif event.type == pygame.KEYDOWN:
            using_mouse = False
            if event.key in (pygame.K_UP, pygame.K_w):
                selected_index = (selected_index - 1) % len(buttons)
                redraw = True
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                selected_index = (selected_index + 1) % len(buttons)
                redraw = True
            elif event.key == pygame.K_RETURN:
                if selected_index == 0:
                    carregar_modulo("singleplayer")
                elif selected_index == 1:
                    carregar_modulo("multiplayer")
                elif selected_index == 2:
                    carregar_modulo("credits")
                elif selected_index == 3:
                    running = False  
                redraw = True

# Encerra o Pygame
pygame.quit()
