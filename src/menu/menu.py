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


def desenhando_botao(COR_BORDA, COR_BOTAO, COR_HOVER, COR_TEXTO,
                      font, rect, tela, text, active=False):
    # Decidindo a cor do botao
    cor = COR_HOVER if active else COR_BOTAO

    # Desenhando o botao na tela
    pg.draw.rect(tela, cor, rect, border_radius=12)
    pg.draw.rect(tela, COR_BORDA, rect, 3, border_radius=12)

    # Construindo o texto do botao
    txt = font.render(text, True, COR_TEXTO)
    txt_rect = txt.get_rect(center=rect.center)

    # Construindo a sombra do botao
    sombra = font.render(text, True, (0, 0, 0))
    sombra_rect = sombra.get_rect(center=(rect.centerx + 2, rect.centery + 2))

    # Desenhando a sombra e o texto na tela
    tela.blit(sombra, sombra_rect)
    tela.blit(txt, txt_rect)


# Função para carregar módulos
def carregar_modulo(acao):
    if acao == "jogar":
        nome_modulo = "main"
    elif acao == "credits":
        show_popup("Créditos:\nFeito😎")
        return
    else:
        show_popup(f"Ação desconhecida: {acao}")
        return

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