import math
from bibGrafos import Grafo

visitado = {}
tempoInicio = {}
tempoTermino = {}
antecessor = {}
time = 0

def buscaProfundidade(grafo):
    global visitado
    global tempoInicio
    global tempoTermino
    global antecessor
    global time

    for vertice in range(1,  grafo.tamanho+1):
        visitado[vertice] = False
        tempoInicio[vertice] = math.inf
        tempoTermino[vertice] = math.inf
        antecessor[vertice] = None

    for vertice in range(1,  grafo.tamanho+1):
        if visitado[vertice] == False:
            visitaProfundidade(grafo, vertice)
 
    return (visitado, tempoInicio, antecessor, tempoTermino)

def visitaProfundidade(grafo, vertice):
    global visitado
    global tempoInicio
    global tempoTermino
    global antecessor
    global time

    visitado[vertice] = True
    time = time+1
    tempoInicio[vertice] = time

    vizinhos = grafo.vizinhos(vertice)

    for vizinho in vizinhos:
        if visitado[vizinho] == False:
            antecessor[vizinho] = vertice
            visitaProfundidade(grafo, vizinho)
    
    time = time+1
    tempoTermino[vertice] = time

    return True

def transporAresta(grafo):
    arestasT = []
    for aresta in grafo.arestas:
        arestaT = [aresta[1], aresta[0]]
        arestasT.append(arestaT)
        
    grafo.arestas = arestasT

    return grafo
'''
G = Grafo(arquivo='teste1.grafo')

buscaProfundidade(G)

print(tempoInicio)
print(tempoTermino)


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