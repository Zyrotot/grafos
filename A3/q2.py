import math
from bibGrafos import Grafo
from copy import deepcopy

def separa(grafo):
    x = deepcopy(grafo.vertices)

    for vertice in x:
        for vizinho in grafo.vizinhos(grafo.indice(vertice)):
            try:
                x.remove(grafo.rotulo(vizinho))
            except:
                pass

    return x


def BFS(grafo, mate, xc, distancia):
    queue = []

    for x in xc:
        if mate[grafo.indice(x)] == None:
            distancia[grafo.indice(x)] = 0
            queue.append(grafo.indice(x))
        else:
            distancia[x] = math.inf
    print(distancia)
    t = grafo.tamanho+1
    distancia[t] = math.inf

    print(distancia)

    while queue:
        x = queue.pop(0)
        if distancia[x]<distancia[t]:
            for vizinho in grafo.vizinhos(x):
                if distancia[mate[vizinho]] == math.inf: #WTF
                    distancia[mate[vizinho]] = distancia[x] + 1
                    queue.append(mate[vizinho])

    state = distancia[t] != math.inf

    print(state)

    return (state)

def DFS(grafo, mate, x, distancia):
    state = False


    return state

def hopcroftKarp(grafo):
    distancia = {}
    mate = {}
    
    m = 0

    for vertice in range(1, grafo.tamanho+1):
        distancia[vertice] = math.inf
        mate[vertice] = None

    xc = separa(grafo)

    while BFS(grafo, mate, xc, distancia):
        for xi in xc:
            if mate[xi]==None:
                if DFS(grafo, mate, xi, distancia):
                    m = m+1
        
    return m, mate

G = Grafo(arquivo='instancias/emparelhamento_maximo/pequeno.net')

num, result = hopcroftKarp(G)
