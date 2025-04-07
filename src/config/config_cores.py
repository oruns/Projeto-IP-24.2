from .config_geral import carregar_dados, DIR_CONFIG


# Carregando dados
dados_cores = carregar_dados('cores', DIR_CONFIG)


# Recebendo cores
verde = tuple(dados_cores['verde'])
azul = tuple(dados_cores['azul'])