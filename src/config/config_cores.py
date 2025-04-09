from .config_geral import carregar_dados, DIR_CONFIG


# Carregando dados
dados_cores = carregar_dados('cores')


# Recebendo cores
GREEN = tuple(dados_cores['verde'])
BLUE = tuple(dados_cores['azul'])
BLACK = tuple(dados_cores["preto"])
DARK_GRAY = tuple(dados_cores["cinza_escuro"])
GRAY = tuple(dados_cores["cinza"])
GREEN = tuple(dados_cores["verde"])
HOVER_COLOR = tuple(dados_cores["cor_mouse"])
WHITE = tuple(dados_cores["branco"])
COR_BORDA_MENU = tuple(dados_cores["borda_menu"])
COR_HOVER_MENU = tuple(dados_cores["hover_menu"])
COR_BACKG_RESERVA_MENU = tuple(dados_cores["background_reserva_menu"])