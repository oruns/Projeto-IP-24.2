class Mapa:
    def __init__(self, LARGURA_TELA, ALTURA_TELA, TAMANHO_INICIAL_COBRA, modelo_mapa):
        self.LARGURA_TELA = LARGURA_TELA
        self.ALTURA_TELA = ALTURA_TELA
        self.TAMANHO_INICIAL_COBRA = TAMANHO_INICIAL_COBRA

        print(modelo_mapa)
        self.labirinto = modelo_mapa


    def desenha_labirinto(self, tela, bush_img, plano_img):
        for y, linha in enumerate(self.labirinto):
            for x, celula in enumerate(linha):
                if celula == 1:
                    tela.blit(bush_img, (x * self.TAMANHO_INICIAL_COBRA, y * self.TAMANHO_INICIAL_COBRA, self.TAMANHO_INICIAL_COBRA, self.TAMANHO_INICIAL_COBRA))
                elif celula==0:
                    tela.blit(plano_img, (x * self.TAMANHO_INICIAL_COBRA, y * self.TAMANHO_INICIAL_COBRA, self.TAMANHO_INICIAL_COBRA, self.TAMANHO_INICIAL_COBRA))

                    

    def parede(self, x, y, TAMANHO_INICIAL_COBRA):
        """Retorna True se a posição (x, y) for uma parede, False caso contrário"""
        coluna = x // TAMANHO_INICIAL_COBRA
        linha = y // TAMANHO_INICIAL_COBRA

        return self.labirinto[linha][coluna] == 1  # 1 representa parede