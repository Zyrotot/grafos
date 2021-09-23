import math
from bibGrafos import Grafo
from copy import deepcopy
import time

def montas(grafo):
    s = {}
    controle = {}
    contador = 0

    for vertice in grafo.vertices:
        controle[vertice] = {'base': math.pow(2, contador), 'estado': False, 'contador': 0}
        contador = contador + 1

    for num in range(0, int(math.pow(2, grafo.tamanho))):
        s[num] = []
        for vertice in grafo.vertices:
            if controle[vertice]['contador'] == controle[vertice]['base']:
                controle[vertice]['estado'] = not controle[vertice]['estado']
                controle[vertice]['contador'] = 0
            if controle[vertice]['estado']:
                s[num].append(vertice)
            controle[vertice]['contador'] = controle[vertice]['contador'] + 1

    return s

def achaMaximal(grafo, s, tempG):
    maximal = {0:[]}
    para = False
    for vertice in tempG.vertices:
        contador = 0
        while True:
            if para:
                para = False
                break
            try:
                if isinstance(maximal[contador], list):
                    if not maximal[contador]:
                        maximal[contador].append(vertice)
                        para = True
                    else:
                        tem = False
                        for v2 in maximal[contador]:
                            if para:
                                break
                            if (grafo.indice(vertice), grafo.indice(v2)) in tempG.arestas.keys() or (grafo.indice(v2), grafo.indice(vertice)) in tempG.arestas.keys():
                                tem = True
                                contador = contador + 1
                        if not tem:
                            maximal[contador].append(vertice)
                            para = True
            except:
                maximal[contador] = []

    return maximal

def geraTempG(s, grafo):
    tempG = deepcopy(grafo)
    tempG.vertices = []
    tempG.arestas = {}
    for vertice in s:
        tempG.vertices.append(vertice)
        for v2 in s:
            if (grafo.indice(vertice), grafo.indice(v2)) in grafo.arestas.keys():
                tempG.arestas[grafo.indice(vertice), grafo.indice(v2)] = grafo.peso(grafo.indice(vertice), grafo.indice(v2))
            elif (grafo.indice(v2), grafo.indice(vertice)) in grafo.arestas.keys():
                tempG.arestas[grafo.indice(v2), grafo.indice(vertice)] = grafo.peso(grafo.indice(v2), grafo.indice(vertice))

    return tempG

def lawler(grafo):
    max = math.pow(2, grafo.tamanho)
    x = {}

    for num in range(0, int(max)):
        x[num] = None

    s = montas(grafo)

    for num in s:
        if num != 0:
            x[num] = math.inf
            tempG = geraTempG(s[num], grafo)
            maximal = achaMaximal(grafo, s, tempG)
            for grupo in maximal:
                i = list(set(tempG.vertices).difference(maximal[grupo]))
                for con in s:
                    tempS = s[con]
                    tempS.sort()
                    tempI = i
                    tempI.sort()
                    if tempS == tempI:
                        if x[con]+1 < x[num]:
                            x[num] = x[con]+1
        else:
            x[num] = 0

    return x[num], maximal

G = Grafo(arquivo='instancias/coloracao/cor3.net')

x, maximal = lawler(G)
print('Número de cores usadas:', x, '/ Cores por vértice:', maximal)