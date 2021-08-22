import math
from bibGrafos import Grafo

visitado = {}
tempoInicio = {}
tempoTermino = {}
time = 0
list = []

def buscaProfundidade(grafo):
    global visitado
    global tempoInicio
    global tempoTermino
    global time

    for vertice in range(1,  grafo.tamanho+1):
        visitado[vertice] = False
        tempoInicio[vertice] = math.inf
        tempoTermino[vertice] = math.inf

    for vertice in range(1,  grafo.tamanho+1):
        if visitado[vertice] == False:
            visitaProfundidade(grafo, vertice)
 
    return (visitado, tempoInicio, tempoTermino)

def visitaProfundidade(grafo, vertice):
    global visitado
    global tempoInicio
    global tempoTermino
    global time
    global list

    visitado[vertice] = True
    time = time+1
    tempoInicio[vertice] = time

    vizinhos = grafo.vizinhos(vertice)

    for vizinho in vizinhos:
        if visitado[vizinho] == False:
            visitaProfundidade(grafo, vizinho)
    
    time = time+1
    tempoTermino[vertice] = time
    list.insert(0, vertice)

    return True

G = Grafo(arquivo='manha.net')

buscaProfundidade(G)
string = ''

for vertice in list:
    string = string+G.rotulo(vertice)+" -> "

print(string[:-3])