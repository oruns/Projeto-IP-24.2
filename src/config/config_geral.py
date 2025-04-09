from json import load


# Diretorio com as configuracoes
DIR_CONFIG = './config/'
DIR_ASSETS = './assets/'


# Se der errado acima, use:
# DIR_CONFIG = '../../config/'


def carregar_dados(tipo):
    '''
    Carregar os dados de um arquivo de configuracao
    Tipo = tela, cores
    '''
    dir_config = DIR_CONFIG


    if tipo == 'tela':
        dir_config += "tela.json" 
    elif tipo == 'cores':
        dir_config += "cores.json" 
    elif tipo == 'entidades':
        dir_config += "entidades.json" 
    elif tipo == 'diretorios_projeto':
        dir_config += "diretorios.json" 
    

    with open(dir_config, "r", encoding="utf-8") as arq:
        dados = load(arq)
    

    return dados


def get_path_asset(nome):
    dir_assets = DIR_ASSETS
    nome_arquivo = dir_assets + nome

    return nome_arquivo