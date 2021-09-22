from bibGrafos import Grafo
from itertools import chain, combinations
import math

def lawler(grafo):
    X = {i:None for i in range(2**grafo.tamanho)}
    X[0] = 0
    S_ = list(chain.from_iterable(combinations(grafo.vertices, r) for r in range(len(grafo.vertices)+1)))

    for S in S_[1:]:
        s = S_.index(S)
        X[s] = math.inf
        arestas = {(grafo.indice(elem),viz):1 for elem in S for viz in grafo.vizinhos(grafo.indice(elem)) if grafo.indice(elem) <= viz}
        G_ = Grafo(tamanho=len(S), vertices=S, arestas=arestas, orientado=False)
        print(I(G_))

def I(grafo):
    S_ = list(chain.from_iterable(combinations(grafo.vertices, r) for r in range(len(grafo.vertices)+1)))[1:]
    sub = []
    for S in S_:
        entra = True
        for a in S:
            for b in S:
                if grafo.haAresta(grafo.indice(a), grafo.indice(b)):
                    entra = False
        if entra:
            sub.append(S)

    todo_sub = list(chain.from_iterable(combinations(sub, r) for r in range(len(sub)+1)))[1:]
    
    fim = []   

    for aa in todo_sub:
        entra = True
        for bb in aa:
            for cc in aa:
                if not bb == cc:
                    if len([value for value in cc if value in bb]) > 0:
                        entra = False
        if entra:
            fim.append(aa)

    fim2=[]
    entra = True
    for aa in fim:
        verts = []
        for b in bb:
            verts.append(b)
        if not verts==list(grafo.vertices):
            entra = False
        if entra:
            fim2.append(aa)
    
    for a in fim2:
        print(len(a))
    return fim2



G = Grafo(arquivo='instancias/coloracao/cor3.net')
lawler(G)


"""
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
"""