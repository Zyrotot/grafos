import math
from bibGrafos import Grafo
from copy import deepcopy

def checaRetorno(grafo):
    grafo_retorno = grafo
    for vertice in range(1, grafo.qtdVertices()+1):
        for vizinho in grafo.vizinhos(vertice):
            if vertice in grafo.vizinhos(vizinho):
                grafo_retorno = removeRetorno(grafo, vertice, vizinho)
    return grafo_retorno

def removeRetorno(grafo, vertice, vizinho):
    peso = grafo.arestas[vertice, vizinho]
    key = (vertice, vizinho)
    grafo.arestas.pop(key)
    grafo.vertices.append(grafo.rotulo(vertice)+'_linha')
    grafo.tamanho = grafo.tamanho+1
    tamanho = grafo.tamanho
    grafo.arestas[(vertice, tamanho)] = peso 
    grafo.arestas[(tamanho, vizinho)] = peso 
    return grafo

def geraResidual(grafo):
    grafo_residual = grafo
    arestas = grafo_residual.arestas
    extra = {}
    for aresta in arestas:
        key = (aresta[1], aresta[0])
        extra[key] = 0
    grafo_residual.arestas = {**arestas, **extra}
    return grafo_residual

def fordFulkerson(grafo, fonte, sorvedouro, residual):
    return None

def fluxoMaximo(grafo):
    tamanho = grafo.tamanho
    grafo_retorno = checaRetorno(grafo)
    grafo_residual = deepcopy(grafo)
    grafo_residual = geraResidual(grafo_residual)
    
    fordFulkerson(grafo_retorno, 1, tamanho, grafo_residual)

    print(grafo_retorno.arestas)
    print(grafo_residual.arestas)
    return None

#G = Grafo(arquivo='instancias/fluxo_maximo/wiki.net')
G = Grafo(arquivo='instancias/fluxo_maximo/fluxo_maximo_aula.net')

result = fluxoMaximo(G)