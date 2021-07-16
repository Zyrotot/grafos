import math
from q1 import Grafo
from heapq import heapify 

def caminhosDijkstra(grafo, inicial, pr=True):
    V = range(1, grafo.qtdVertices() + 1)

    distancia = {v:math.inf for v in V}
    antecessor = {v:None for v in V}
    visitado = {v:False for v in V}

    distancia[inicial] = 0
    
    while False in visitado.values():
        d = {v:distancia[v] for v in V if not visitado[v]}
        u = min(d, key=d.get)
        visitado[u] = True

        for v in grafo.vizinhos(u):
            if not visitado[v] and distancia[v] > distancia[u] + grafo.peso(v, u):
                distancia[v] = distancia[u] + grafo.peso(v, u)
                antecessor[v] = u

    if pr:
        for v in V:
            antecessores = []
            x = v
            while not x==inicial:
                antecessores.append(x)
                x = antecessor[x]

            print(f"{v}: {','.join(map(str,antecessores))}; d={distancia[v]}")

    return distancia, antecessor

G = Grafo(arquivo='teste1.grafo')
caminhosDijkstra(G, 1)