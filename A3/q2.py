import math
from bibGrafos import Grafo
from copy import deepcopy

def hopcroftKarp(grafo):
    distancia = {}
    mate = {}
    
    m = 0

    for vertice in range(1, grafo.tamanho+1):
        distancia[vertice] = math.inf
        mate[vertice] = None
    
    return m, mate

def separa(grafo):
    x = deepcopy(grafo.vertices)

    for vertice in x:
        for vizinho in grafo.vizinhos(int(vertice)):
            try:
                x.remove(str(vizinho))
            except:
                pass

    return x


def BFS(grafo, mate, distancia):
    state = False

    return state

def DFS(grafo, mate, distancia):
    state = False


    return state

G = Grafo(arquivo='instancias/emparelhamento_maximo/pequeno.net')

#num, result = hopcroftKarp(G)
x = separa(G)
print(x)