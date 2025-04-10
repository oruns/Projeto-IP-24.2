import tkinter as tk
import importlib
from tkinter import messagebox
import os


import pygame as pg


def show_popup(txt):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Erro", txt)
    root.destroy()


def iniciar_tela(ALTURA_TELA, LARGURA_TELA, TITULO_MENU):
    '''
    Iniciar tela do menu
    '''
    # Configurações da tela do jogo
    tela = pg.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pg.display.set_caption(TITULO_MENU)

    return tela


def adicionar_fonte():
    '''
    Define a fonte para o texto de todos os botões do menu
    '''
    font_path = pg.font.match_font('comicsansms')  # Ou adicione uma TTF customizada
    font = pg.font.Font(font_path, 36)

    return font


def adicionar_som(get_path_asset):
    ''''''
    # Path dos arquivos de som
    
    hover_sound_path = get_path_asset('hover_sound.wav')
    click_sound_path = get_path_asset('mouse_click.wav')

    hover_sound = pg.mixer.Sound(hover_sound_path) if os.path.exists(hover_sound_path) else None
    click_sound = pg.mixer.Sound(click_sound_path) if os.path.exists(click_sound_path) else None
    
    return hover_sound, click_sound


def construindo_fundo(ALTURA_TELA, LARGURA_TELA, get_path_asset):
    '''
    Construindo uma imagem de fundo ao menu
    '''
    fundo_path = get_path_asset('fundo_menu.png')
    fundo = pg.image.load(fundo_path) if os.path.exists(fundo_path) else None
    fundo = pg.transform.scale(fundo, (LARGURA_TELA, ALTURA_TELA)) if fundo else None

    return fundo


def desenhando_fundo(COR_BACKGROUND, fundo, tela):
    '''
    Desenhando o fundo na tela, se houver
    '''
    if fundo:
        tela.blit(fundo, (0, 0))
    else:
        tela.fill(COR_BACKGROUND)


def construindo_botoes(BOTAO_MENU_ALTURA, BOTAO_MENU_LARGURA,
                    ESPACAMENTO_MENU, LARGURA_TELA, num_botoes,
                    y_start):
    '''
    Desenhar botoes na tela
    '''
    buttons = []

    # Desenhando botoes na tela
    for i in range(num_botoes):
        x = (LARGURA_TELA - BOTAO_MENU_LARGURA) // 2
        y = y_start + i * (BOTAO_MENU_ALTURA + ESPACAMENTO_MENU)
        rect = pg.Rect((x, y), (BOTAO_MENU_LARGURA, BOTAO_MENU_ALTURA))
        buttons.append(rect)
    
    return buttons


def desenhando_botao(cor_borda, cor_normal, cor_hover, cor_texto,
                     fonte, rect, tela, texto, ativo, borda=10):
    pg.draw.rect(tela, cor_borda, rect)
    inner_rect = rect.inflate(-2 * borda, -2 * borda)
    cor_fundo = cor_hover if ativo else cor_normal
    pg.draw.rect(tela, cor_fundo, inner_rect)

    texto_render = fonte.render(texto, True, cor_texto)
    texto_rect = texto_render.get_rect(center=inner_rect.center)
    tela.blit(texto_render, texto_rect)

# Função para carregar módulos
# Função para carregar módulos
def carregar_modulo(acao):
    if acao == "jogar":
        nome_modulo = "main"
        __import__(nome_modulo)
    elif acao == "credits":
        import tela_creditos
        tela_creditos.mostrar_creditos()
    else:
        show_popup(f"Ação desconhecida: {acao}")

    import main
    # try:
    #     modulo = importlib.import_module(nome_modulo)
    #     if hasattr(modulo, "main"):
    #         pg.display.quit()
    #         modulo.main()
    #     else:
    #         show_popup(f"O módulo '{nome_modulo}' não possui uma função 'main'.")
    # except ModuleNotFoundError:
    #     show_popup(f"O módulo '{nome_modulo}' não foi encontrado.")
    # except ImportError as e:
    #     show_popup(f"Erro ao importar o módulo '{nome_modulo}': {e}")