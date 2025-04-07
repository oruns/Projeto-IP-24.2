import pygame as pg


def gerenciar_eventos_jogo(mostrar_grade):
    '''
    Gerenciar os eventos do jogo
    '''
    for event in pg.event.get():
        if event.type == pg.QUIT: # Evento de fechar a janela
            running = False

            return running
        elif event.type == pg.KEYDOWN: # Tecla pressionada
            if event.key == pg.K_j:    # Alterna a grade ao pressionar J
                mostrar_grade = not mostrar_grade


def gerenciar_pontuacoes(jogador_1, jogador_2, largura_tela, tela):
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


def gerenciar_entidades(
    dados_tela, keys,
    jogador_1, jogador_2, item_crescer,
    tela, velocidade
):
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


def iniciar_loop(
    dados_tela,
    jogador_1, jogador_2,
    grade, item_crescer, 
    largura_tela, tela,
    velocidade
):
    '''
    Iniciando loop que mantem o jogo rodando 
    '''
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


        gerenciar_eventos_jogo(mostrar_grade)
        gerenciar_entidades(
            dados_tela, keys,
            jogador_1, jogador_2,
            item_crescer, tela,
            velocidade
        )

        if mostrar_grade:
            grade()

        # Gerenciar pontuacoes
        gerenciar_pontuacoes(jogador_1, jogador_2, largura_tela, tela)

        # Atualizar tela
        pg.display.flip()