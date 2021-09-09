import math
from bibGrafos import Grafo
from copy import deepcopy

def checaRetorno(grafo):
    grafo_retorno = grafo
    for vertice in range(1, grafo.tamanho+1):
        for vizinho in grafo.vizinhos(vertice):
            if vertice in grafo.vizinhos(vizinho):
                grafo_retorno = removeRetorno(grafo, vertice, vizinho)
    return grafo_retorno

def removeRetorno(grafo, vertice, vizinho):
    peso = grafo.arestas[vertice, vizinho]
    key = (vertice, vizinho)
    grafo.arestas.pop(key)
    grafo.vertices.append(grafo.rotulo(vertice)+'_linha')
    grafo.tamanho = grafo.tamanho+1
    tamanho = grafo.tamanho
    grafo.arestas[(vertice, tamanho)] = peso 
    grafo.arestas[(tamanho, vizinho)] = peso 
    return grafo

def geraResidual(grafo):
    grafo_residual = grafo
    arestas = grafo_residual.arestas
    extra = {}
    for aresta in arestas:
        key = (aresta[1], aresta[0])
        extra[key] = 0
    grafo_residual.arestas = {**arestas, **extra}
    return grafo_residual

def edmondsKarp(grafo, fonte, sorvedouro, residual):
    visitado = {}
    antecessor = {}
    queue = []

    for vertice in range(1, grafo.tamanho+1):
        visitado[vertice] = False
        antecessor[vertice] = None
    
    visitado[fonte] = True
    queue.append(fonte)
    while queue:
        v = queue.pop(0)
        for vizinho in grafo.vizinhos(v):
            key = (v, vizinho)
            if visitado[vizinho] is False and residual.arestas[key] > 0:
                visitado[vizinho] = True
                antecessor[vizinho] = v
                if vizinho == sorvedouro:
                    p = [sorvedouro]
                    w = sorvedouro
                    while w is not fonte:
                        w = antecessor[w]
                        p.append(w)
                    return(p)
                queue.append(vizinho)
    return None

def fordFulkerson(grafo, fonte, sorvedouro, residual):
    fluxo = {}
    for aresta in grafo.arestas:
        fluxo[aresta] = 0

    while True:
        w = edmondsKarp(grafo, fonte, sorvedouro, residual)
        if w is not None:
            cf = math.inf
            for count  in range(0, len(w)-1):
                key = (w[count+1], w[count])
                fluxot = residual.arestas[key]
                if cf > fluxot:
                    cf = fluxot

            for aresta in w:
                for aresta2 in w:
                    if (aresta, aresta2) in grafo.arestas:
                        fluxo[(aresta, aresta2)] = fluxo[(aresta, aresta2)] + cf
                        residual.arestas[(aresta, aresta2)] = residual.arestas[(aresta, aresta2)] - cf
        else:
            break

    print(fluxo)
    return None

def fluxoMaximo(grafo):
    tamanho = grafo.tamanho
    grafo_retorno = checaRetorno(grafo)
    grafo_residual = deepcopy(grafo)
    grafo_residual = geraResidual(grafo_residual)
    
    fordFulkerson(grafo_retorno, 1, tamanho, grafo_residual)
    return None

G = Grafo(arquivo='instancias/fluxo_maximo/wiki.net')
#G = Grafo(arquivo='instancias/fluxo_maximo/fluxo_maximo_aula.net')

result = fluxoMaximo(G)