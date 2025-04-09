#documentacao
#selecionar erros importantes na revisao
#os mapas nem sempre serao quadrados

#TODO
# gerar catalogo dinamicametne
# esse arquivo sera dividido em subarquivos, uso agr so pra comecar a rascunhar

from pathlib import Path


caminho_pasta_mapas = 'mapa/mapas/'


def receber_catalogo():
  '''Receber lista de todos os mapas existentes'''

  # Nome do arquivo com a lista de todos os mapas existentes
  nome_catalogo = 'catalogo.txt'

  # Lendo o arquivo
  arquivo_catalogo = Path(caminho_pasta_mapas) / nome_catalogo
  conteudo_arquivo = arquivo_catalogo.read_text()
  nome_mapas = conteudo_arquivo.splitlines()

  return nome_mapas


def carregar_mapa(nome_mapa):
  '''
  Carrega o arquivo do mapa
  '''
  mapa = []

  # Lendo conteudo do arquivo
  arquivo_mapa = Path(caminho_pasta_mapas) / nome_mapa
  conteudo_arquivo = arquivo_mapa.read_text()

  # Adicionando as linhas do mapa
  linhas_mapa = conteudo_arquivo.splitlines()

  for linha in linhas_mapa:
    mapa.append(linha)
    
  return mapa


def obter_dados_mapa(mapa):
  '''
  Obter varios dados relacionados ao mapa
  '''
  # Calcular as dimensoes do mapa
  tamanho_horizontal = len(mapa[0])
  tamanho_vertical = len(mapa)

  # Juntar todos os dados
  dados_mapa = {
    'tamanho_horizontal': tamanho_horizontal,
    'tamanho_vertical': tamanho_vertical,
  }

  return dados_mapa


class Mapa:
  def __init__(self, dados_mapa):
    self.receber_dados(dados_mapa)
  

  def receber_dados(self, dados_mapa):
    '''
    Preencher o objeto no momento da instanciacao
    '''
    self.__tamanho_horizontal = dados['tamanho_horizontal']
    self.__tamanho_vertical = dados['tamanho_vertical']


mapa = carregar_mapa('teste_mapa.mp')
dados = obter_dados_mapa(mapa)
m = Mapa(dados)
print(m)

# print(receber_catalogo())