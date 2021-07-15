import math
from collections import defaultdict

#define classe para grafo
class BuscaLargura:
    """
    a função __init__ é executada ao incializar um objeto
    recebe o nome do arquivo com as infos do grafo ou recebe infos do grafo
    cria o grafo correspondente
    """
    def __init__(self, **kwargs):
        if 'arquivo' in kwargs:
            self.ler(kwargs['arquivo'])
        elif 'tamanho' in kwargs and 'vertices' in kwargs and 'arestas' in kwargs:
            self.defineGrafo(kwargs['tamanho'], kwargs['vertices'], kwargs['arestas'])
        else:
            raise Exception("Grafo de entrada em formato não válido")
        
        if 'vertice' in kwargs and kwargs['vertice'] <= len(self.vertices):
            self.inicio = kwargs['vertice']
        elif 'vertice' in kwargs and kwargs['vertice'] > len(self.vertices):
            raise Exception("Declare um vertice existente")
        else:
            raise Exception("Declare o vertice de inicio da busca")

    def ler(self, arquivo):
        arestas = {}
        vertices = []
        with open(arquivo, "r") as f:
            linhas = f.readlines()            
            for linha in linhas:
                linha = linha.rstrip("\n").split(" ")
                if 'vertices' in linha[0]:
                    tamanho = int(linha[1])
                else:
                    if len(linha) == 2:
                        vertices.append(linha[1])
                    elif len(linha) == 3:
                        arestas[(int(linha[0]), int(linha[1]))] = float(linha[2])
            self.defineGrafo(tamanho, vertices, arestas)

    def vizinhos(self, v):
        arestasV = [list(a) for a in self.arestas if v in a]
        for a in arestasV:
            a.remove(v)
        return {a[0] for a in arestasV}


    def defineGrafo(self, tamanho, vertices, arestas):
        if len(vertices)==tamanho:
            self.tamanho = tamanho
            self.vertices = vertices
            self.arestas = arestas
        else:
            raise Exception("Grafo inconsistente")

    def busca(self):
        visitado = {}
        distancia = {}
        antecessor = {}
        queue = []

        for vertice in range(0, len(self.vertices)):
            visitado[vertice+1] = False
            distancia[vertice+1] = math.inf
            antecessor[vertice+1] = None

        visitado[self.inicio] = True
        distancia[self.inicio] = 0
        queue.append(self.inicio)

        b = self.vizinhos(1)

        while queue:
            a = queue.pop(0)
            for vizinho in self.vizinhos(a):
                if visitado[vizinho] is False:
                    visitado[vizinho] = True
                    antecessor[vizinho] = a
                    distancia[vizinho] = distancia[antecessor[vizinho]]+1
                    queue.append(vizinho)

        resultado = defaultdict(list)
        for vertice, nivel in distancia.items():
            resultado[nivel].append(vertice)

        return resultado

        #debug
        #return visitado, distancia, antecessor

G = BuscaLargura(arquivo='teste1.grafo', vertice=1)
for distancia, vertices in G.busca().items():
    print(distancia,':', vertices)


'''
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