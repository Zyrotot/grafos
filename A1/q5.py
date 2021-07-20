from q1 import Grafo
import math

def floydWarshall(grafo):
    vertices = grafo.qtdVertices()
    distancia = [[y for y in range(vertices)] for x in range(vertices)]

    for i in range(vertices):
            for j in range(vertices):
                distancia[i][j] = grafo.peso(i+1, j+1) 

    dist = list(map(lambda i: list(map(lambda j: j, i)), distancia))

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                distancia[i][j] = min(distancia[i][j], (distancia[i][k] + distancia[k][j]))
                
    resposta = escreveResposta(distancia, vertices)

    return resposta

def escreveResposta(distancia, vertices):
    resposta = {}
    for numero in range(vertices):
        resposta[numero+1] = distancia[numero]

    return resposta

G = Grafo(arquivo='teste1.grafo')

matriz = floydWarshall(G)

for vertice in matriz:
    print(vertice,':', matriz[vertice])