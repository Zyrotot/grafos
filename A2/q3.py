import math
from bibGrafos import Grafo

def agmKruskal(grafo, escreve=True):
    V = range(1, grafo.qtdVertices() + 1)

    A = set([])
    S = {v:{v} for v in V}

    E = [i[0] for i in sorted(grafo.arestas.items(), key=lambda item: item[1])]
    
    for aresta in E:
        u, v = aresta
        if not S[u] == S[v]:
            A.add(aresta)
            x = S[u].union(S[v])
            for y in x:
                S[y] = x
    
    if escreve:
        somatorio = 0
        for a in A:
            somatorio += grafo.peso(a[0], a[1])
        print(somatorio)
        print(', '.join(['-'.join(str(e) for e in a) for a in A]))

    return A

G = Grafo(arquivo='instancias\\arvore_geradora_minima\\agm_tiny.net')
agmKruskal(G)
