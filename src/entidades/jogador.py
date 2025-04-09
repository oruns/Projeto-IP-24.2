import pygame as pg


class Jogador:
    def __init__(self, coord_inic, cor, teclas, TAMANHO_INICIAL_COBRA):
        self.coord_inic = coord_inic
        self.direcao = (0, 0)  # começa parado

        self.corpo = [self.coord_inic]

        self.cor = cor
        self.velocidade = TAMANHO_INICIAL_COBRA
        self.teclas = teclas
        self.crescer = False

        self.pontuacao = 0

        self.contador_buffs = 0
        self.contador_veneno = 0  # veneno vezes #########
        self.contador_coroas = 0


    def update(self, keys, debuff, coroa, visibilidade_coroa,
               mapa, BlocoRoxo, Debuff,
               ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA):
        if keys[self.teclas["up"]] and self.direcao != (0, self.velocidade):
            self.direcao = (0, -self.velocidade)
        if keys[self.teclas["down"]] and self.direcao != (0, -self.velocidade):
            self.direcao = (0, self.velocidade)
        if keys[self.teclas["left"]] and self.direcao != (self.velocidade, 0):
            self.direcao = (-self.velocidade, 0)
        if keys[self.teclas["right"]] and self.direcao != (-self.velocidade, 0):
            self.direcao = (self.velocidade, 0)


        if self.corpo:
            nova_parte = (self.corpo[0][0] + self.direcao[0],
                          self.corpo[0][1] + self.direcao[1])
        else:
            nova_parte = self.coord_inic


        # Verificando a colisão com o labirinto
        if mapa.labirinto[nova_parte[1] // TAMANHO_INICIAL_COBRA][nova_parte[0] // TAMANHO_INICIAL_COBRA] == 1:
            self.resetar()
            return


        if (nova_parte[0] < 0 or nova_parte[0] >= LARGURA_TELA or
                nova_parte[1] < 0 or nova_parte[1] >= ALTURA_TELA):
            self.resetar()
            return


        if nova_parte in self.corpo[1:]:
            self.resetar()
            return


        # Verifica se cabeça colidiu com o buff 1
        for buff in BlocoRoxo.guardar_buffs:
            if pg.Rect(nova_parte[0], nova_parte[1], TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA).colliderect(
                    pg.Rect(buff.x, buff.y, TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA)):
                self.pontuacao += 10
                self.contador_buffs += 1
                self.crescer = True
                buff.reposicionar(ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)


        ############# Verifica se a cabeça da cobra colidiu com o debuff ##########
        for debuff in Debuff.guardar_debuffs:
            if pg.Rect(nova_parte[0], nova_parte[1], TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA).colliderect(
                    pg.Rect(debuff.x, debuff.y, TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA)):
                if len(self.corpo) > 1:  # cobra não desaparece
                    self.corpo.pop()  # tira um bloco do corpo da cobra

                    self.contador_veneno += 1  # debuffs coletados
                    debuff.reposicionar(ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
            # pontos de veneno não negativam a pontuação total
                if self.pontuacao >= 10:
                    self.pontuacao -= 10
                    self.contador_veneno += 1
                    debuff.reposicionar(ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
                elif self.pontuacao < 10:
                    self.pontuacao -= self.pontuacao
                    self.contador_veneno += 1
                    debuff.reposicionar(ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)

        ############ verifica se a cabeça da cobra colidiu com a coroa ############
        if visibilidade_coroa and pg.Rect(nova_parte[0], nova_parte[1], TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA).colliderect(
                pg.Rect(coroa.x, coroa.y, TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA)):
            self.contador_coroas += 1
            coroa.reposicionar(mapa, ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)

        self.corpo.insert(0, nova_parte)

        if not self.crescer:
            self.corpo.pop()
        else:
            self.crescer = False

    def desenhar(self, tela, snake_head_img, snake_body_img,
                 TAMANHO_INICIAL_COBRA):
        for segment in self.corpo:
            if segment == self.corpo[0]:
                tela.blit(snake_head_img, (segment[0], segment[1], TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA))
            else:
                tela.blit(snake_body_img, (segment[0], segment[1], TAMANHO_INICIAL_COBRA, TAMANHO_INICIAL_COBRA))




    def resetar(self):
        self.corpo = [self.coord_inic]
        self.direcao = (0, 0)
        self.crescer = False
        # pontuação não reseta mais, porém o jogador é penalizado em -5 pontos por colidir. Não permite ponto negativo.
        self.pontuacao = self.pontuacao = max(0, self.pontuacao - 5)
        pg.time.delay(500)