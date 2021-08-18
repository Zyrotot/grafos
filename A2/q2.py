import math
from bibGrafos import Grafo

visitado = {}
tempoInicio = {}
tempoTermino = {}
antecessor = {}
time = 0
list = []

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
    global list

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
    list.insert(0, vertice)

    return True

'''
G = Grafo(arquivo='teste1.grafo')

buscaProfundidade(G)

print(list)
'''