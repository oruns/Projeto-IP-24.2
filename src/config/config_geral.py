from json import load


# Dependendencia, ponto central falha aqui
# Carregamento do diretorio

# Diretorio com as configuracoes
DIR_CONFIG = './config/'


def carregar_dados(tipo, dir_config):
    '''
    Carregar os dados de um arquivo de configuracao
    Tipo = tela, cores
    '''
    if tipo == 'tela':
        dir_config += "tela.json" 
    elif tipo == 'cores':
        dir_config += "cores.json" 
    elif tipo == 'entidades':
        dir_config += "entidades.json" 
    

    with open(dir_config, "r", encoding="utf-8") as arq:
        dados = load(arq)
    

    return dados