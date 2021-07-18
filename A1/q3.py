from q1 import Grafo

def cicloEuleriano(grafo):
    visitado = {}

    for aresta in grafo.arestas:
        visitado[aresta] = False

    odd = 0
    inicial = 1

    for vertice in range(0, len(grafo.vertices)):
        if(grafo.grau(vertice+1)%2) != 0:
            inicial = vertice+1
            odd = odd+1

    if odd not in [0, 2]:
        return(False, None)

    e, ciclo = buscaCiclo(grafo, inicial, visitado)

    return e, ciclo

def buscaCiclo(grafo, vertice, visitados):
    tciclo = []
    inicial = vertice

    if not vertice and not visitados:
        return False, None 

    while False in visitados.values():
        for aresta, estado in visitados.items():
            if vertice in aresta and estado == False:
                for item in aresta:
                    if item != vertice and visitados[aresta] == False:
                        tciclo.append(vertice)
                        vertice = item
                        visitados[aresta] = True

        if vertice == inicial:
            tciclo.append(vertice)
            e = True
            break

    subvisitados = {}
    subvertice  = 0

    for aresta, estado in visitados.items():
        if estado == False:
            subvisitados[aresta] = estado

    for vertice in tciclo:
        for aresta in subvisitados:
            if vertice in aresta:
                subvertice = vertice

    sube, subtciclo = buscaCiclo(grafo, subvertice, subvisitados)

    if sube == True:
        for i in range(0, len(tciclo)):
            if tciclo[i] == subtciclo[0]:
                tciclo.pop(i)
                tciclo = tciclo[:i] + subtciclo + tciclo[i:]
                break
    else:
        return e, tciclo

    return e, tciclo

G = Grafo(arquivo='teste1.grafo')

e, ciclo = cicloEuleriano(G)

print(e, ciclo)