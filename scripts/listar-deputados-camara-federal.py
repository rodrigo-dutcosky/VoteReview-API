### DADOS ABERTOS: https://dadosabertos.camara.leg.br/swagger/api.html

import json
import requests

URL = "https://dadosabertos.camara.leg.br/api/v2"

def listar():
    
    ### criando uma requisicao para buscar dados de um deputado em especifico atraves de seu identificador
    response = requests.get(URL + "/deputados?ordem=ASC&ordenarPor=nome")
    
    ### carregando o conteudo da resposta concluida com sucesso utilizando o pacote json
    _content = json.loads(response.content)
    
    ### criando uma lista para guardar os IDs
    lista = []
    
    ### iterando sob os objetos do conteudo da resposta (deputados)
    for obj in _content.get("dados"):
        
        ### coletando o ID do objeto (deputado) da iteracao
        uid = obj.get("id")
        
        ### adicionando o valor do ID na lista criada antes de iniciar a iteracao
        lista.append(uid)
        
        
    ### retornando o objeto list contendo o ID de todos os deputados
    return lista



def buscar(uid:int):

    ### criando uma requisicao para buscar dados de um deputado em especifico atraves de seu identificador
    response = requests.get(URL + "/deputados/" + str(uid))
    
    ### checar o status da resposta para seguir adiante com o resto da funcao
    if response.status_code == 200:
        
        ### carregando o conteudo da resposta concluida com sucesso utilizando o pacote json
        _content = json.loads(response.content)

        ### retornando o valor da chave "dados", que contem o objeto referente ao deputado em especifico.
        return _content.get("dados")
    
    return {}


######################################################################################################################################################################################################################################################################################################################################################################################################


### formato define function
def camara():
    
    deputados = []

    for uid in listar():

        deputado = buscar(uid)
        deputados.append(deputado)
        
    return deputados


### formato list comprehension
camara = lambda : [buscar(uid) for uid in listar()]

