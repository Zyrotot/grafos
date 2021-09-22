import math
from bibGrafos import Grafo
from collections import deque
from copy import deepcopy
import time

distancia = {}
mate = {}

def separa(grafo):
    x = deepcopy(grafo.vertices)

    for vertice in x:
        for vizinho in grafo.vizinhos(grafo.indice(vertice)):
            try:
                x.remove(grafo.rotulo(vizinho))
            except:
                pass

    return x

def BFS(grafo, xc):
    global mate
    global distancia
    
    queue = deque()

    for x in xc:
        if mate[grafo.indice(x)] == None:
            distancia[grafo.indice(x)] = 0
            queue.append(grafo.indice(x))
        else:
            distancia[x] = math.inf

    distancia[None] = math.inf

    while queue:
        x = queue.popleft()
        if distancia[x]<distancia[None]:
            for vizinho in grafo.vizinhos(x):
                if distancia[mate[vizinho]] == math.inf: 
                    distancia[mate[vizinho]] = distancia[x] + 1
                    queue.append(mate[vizinho])

    state = distancia[None] != math.inf

    return (state)

def DFS(grafo, x):
    global mate
    global distancia

    if x != None:
        for vizinho in grafo.vizinhos(x):
            if distancia[mate[vizinho]] == distancia[x]+1:
                if DFS(grafo, mate[vizinho]):
                    mate[vizinho] = x
                    mate[x] = vizinho
                    return True
        distancia[x] = math.inf
        return False
    return True

def hopcroftKarp(grafo):
    global mate
    global distancia
    
    m = 0

    for vertice in range(1, grafo.tamanho+1):
        distancia[vertice] = math.inf
        mate[vertice] = None

    xc = separa(grafo)

    while BFS(grafo, xc):
        for xi in xc:
            if mate[grafo.indice(xi)]==None:
                if DFS(grafo, grafo.indice(xi)):
                    m = m+1
        
    return m, mate

G = Grafo(arquivo='instancias/emparelhamento_maximo/pequeno.net')

num, result = hopcroftKarp(G)
print(num, result)
