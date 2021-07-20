import math
from q1 import Grafo

def caminhosDijkstra(grafo, inicial, escreve=True):
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

    if escreve:
        for v in V:
            antecessores = []; x = v
            while not x==None:
                antecessores.append(x)
                if x==inicial:
                    break
                x = antecessor[x]
            antecessores.reverse()
            print(f"{v}: {','.join(map(str,antecessores))}; d={distancia[v]}")

    return distancia, antecessor

G = Grafo(arquivo='teste1.grafo')
caminhosDijkstra(G, 2)
