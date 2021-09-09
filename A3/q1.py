import math
from bibGrafos import Grafo

def checaRetorno(grafo):
    for vertice in range(1, grafo.qtdVertices()+1):
        for vizinho in grafo.vizinhos(vertice):
            if vertice in grafo.vizinhos(vizinho):
                removeRetorno(grafo, vertice, vizinho)
    return None

def removeRetorno(grafo, vertice, vizinho):
    peso = grafo.arestas[vertice, vizinho]
    key = (vertice, vizinho)
    grafo.arestas.pop(key)
    grafo.vertices.append(grafo.rotulo(vertice)+'_linha')
    grafo.tamanho = grafo.tamanho+1
    tamanho = grafo.tamanho
    grafo.arestas[(vertice, tamanho)] = peso 
    grafo.arestas[(tamanho, vizinho)] = peso 
    return None


G = Grafo(arquivo='instancias/fluxo_maximo/wiki.net')
#G = Grafo(arquivo='instancias/fluxo_maximo/fluxo_maximo_aula.net')

result = checaRetorno(G)