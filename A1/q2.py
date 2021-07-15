import math
from collections import defaultdict, OrderedDict
from q1 import Grafo

def buscaLargura(grafo, inicial):
    visitado = {}
    distancia = {}
    antecessor = {}
    queue = []

    if inicial > len(grafo.vertices):
        raise Exception("Entrada não válida")

    for vertice in range(0, len(grafo.vertices)):
        visitado[vertice+1] = False
        distancia[vertice+1] = math.inf
        antecessor[vertice+1] = None

    visitado[inicial] = True
    distancia[inicial] = 0
    queue.append(inicial)

    b = grafo.vizinhos(1)

    while queue:
        a = queue.pop(0)
        for vizinho in grafo.vizinhos(a):
            if visitado[vizinho] is False:
                visitado[vizinho] = True
                antecessor[vizinho] = a
                distancia[vizinho] = distancia[antecessor[vizinho]]+1
                queue.append(vizinho)

    resultado = defaultdict(list)
    for vertice, nivel in distancia.items():
        resultado[nivel].append(vertice)
    
    ordResultado = OrderedDict(sorted(resultado.items()))

    return ordResultado

    #debug
    #return visitado, distancia, antecessor

G = Grafo(arquivo='teste1.grafo')

resultado = buscaLargura(G, 1)

for distancia, vertices in resultado.items():
    print(distancia,':', vertices)


'''
#debug
visitados, distancias, antecessores = G.busca()

print('Visitados:')
for vertice, visitado in visitados.items():
    print(vertice, '->', visitado)

print('Distancia:')
for vertice, distancia in distancias.items():
    print(vertice, '->', distancia)

print('Antecessor:')
for vertice, antecessor in antecessores.items():
    print(vertice, '->', antecessor)
'''