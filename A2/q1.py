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
        time = 0

    for vertice in range(1,  grafo.tamanho+1):
        if visitado[vertice] == False:
            visitaProfundidade(grafo, vertice)
 
    return (visitado, tempoInicio, antecessor, tempoTermino)

def buscaProfundidadeAdaptado(grafo, sortTempo):
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
        time = 0

    for vertice in sortTempo:
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
    arestasT = {}
    arestas = grafo.arestas
    for aresta in arestas:
        arestasT[aresta[1], aresta[0]] = arestas[aresta]
        
    grafo.arestas = arestasT

    return grafo

def buscaAntecessor(vertice, antecessores):
    con = set()
    for antecessor in antecessores:
        if vertice == antecessores[antecessor]:
            con.add(vertice)
            con.add(antecessor)
            con = con.union(buscaAntecessor(antecessor, antecessores))
            
    return con

def conexaoForte(grafo):
    global visitado
    global tempoInicio
    global tempoTermino
    global antecessor
    global time
    
    result = {}
    result['visitado'], result['tempoInicio'], result['antecessor'], result['tempoTermino'] = buscaProfundidade(grafo)
    
    sortTempo = {k: v for k, v in sorted(tempoTermino.items(), key=lambda item: item[1], reverse=True)}

    Gt = transporAresta(G)

    resultT = {}
    resultT['visitado'], resultT['tempoInicio'], resultT['antecessor'], resultT['tempoTermino'] = buscaProfundidadeAdaptado(Gt, sortTempo)

    forteCon = []

    antList = list()

    for antecessor in resultT['antecessor']:
        antList.append(antecessor)

    while antList:
        ant = antList.pop(0)
        conSet = buscaAntecessor(ant, resultT['antecessor'])
        if conSet != set():
            forteCon.append(conSet)
        for x in conSet:
            try:
                antList.remove(x)
            except:
                pass

    return forteCon

G = Grafo(arquivo='teste1.grafo')

result = conexaoForte(G)
print(result)