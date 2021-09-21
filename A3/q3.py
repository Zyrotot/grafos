import math
from bibGrafos import Grafo
from copy import deepcopy

def lawler(grafo):
    max = math.pow(2, grafo.tamanho)
    x = {}

    for num in range(0, int(max)):
        x[num] = None

    x[0] = 0
    s = montas(grafo)
    return x, g

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

G = Grafo(arquivo='instancias/coloracao/cor3.net')

#x, g = lawler(G)
s = montas(G)