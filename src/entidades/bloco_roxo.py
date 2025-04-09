import random as rd


class BlocoRoxo:
    guardar_buffs = []


    def __init__(self, Mapa, cor,
                 ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA):
        self.mapa = Mapa
        self.reposicionar(ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)
        self.cor = cor

        BlocoRoxo.guardar_buffs.append(self)  # adiciona a lista na classe


    def reposicionar(self, ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA):
        while True:
            self.x = rd.randint(0, (LARGURA_TELA - TAMANHO_INICIAL_COBRA) //
                                TAMANHO_INICIAL_COBRA) * TAMANHO_INICIAL_COBRA
            self.y = rd.randint(0, (ALTURA_TELA - TAMANHO_INICIAL_COBRA) //
                                TAMANHO_INICIAL_COBRA) * TAMANHO_INICIAL_COBRA

            # Verifica se a posição gerada está livre de paredes
            if not self.mapa.parede(self.x, self.y, TAMANHO_INICIAL_COBRA):
                break  # Sai do loop se a posição for válida


    def desenhar_buff1(self, tela, apple_img):
        tela.blit(apple_img,(self.x, self.y)) 


    @classmethod
    def numero_buffs(cls, Mapa, cor, quantidade,
                     ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA):
        for i in range(quantidade):
            cls(Mapa, cor, ALTURA_TELA, LARGURA_TELA, TAMANHO_INICIAL_COBRA)  # cria e adiciona na lista