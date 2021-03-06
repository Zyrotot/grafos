import math

#define classe para grafo
class Grafo:
    """
    a funcao __init__ e executada ao incializar um objeto
    recebe o nome do arquivo com as infos do grafo ou recebe infos do grafo
    cria o grafo correspondente
    """
    def __init__(self, **kwargs):
        if 'arquivo' in kwargs:
            self.ler(kwargs['arquivo'])
        elif 'tamanho' in kwargs and 'vertices' in kwargs and 'arestas' in kwargs:
            self.defineGrafo(kwargs['tamanho'], kwargs['vertices'], kwargs['arestas'], kwargs['orientado'])
        else:
            raise Exception("Entrada nao valida")

    def ler(self, arquivo):
        arestas = {}
        vertices = []
        orientado = False
        with open(arquivo, "r") as f:
            linhas = f.readlines()
            modo = "vertices"
            for linha in linhas:
                linha = linha.rstrip("\n").split(" ")
                if 'vertices' in linha[0]:
                    tamanho = int(linha[1])
                elif 'edges' in linha[0] or 'arcs' in linha[0]:
                    if 'arcs' in linha[0]:
                        orientado = True
                    modo = "edges"
                else:
                    if modo == "vertices":
                        vertices.append(" ".join(linha[1:]))
                    elif modo == "edges":
                        arestas[(int(linha[0]), int(linha[1]))] = float(linha[2])
            self.defineGrafo(tamanho, vertices, arestas, orientado)

    def defineGrafo(self, tamanho, vertices, arestas, orientado):
        if len(vertices)==tamanho:
            self.orientado = orientado
            self.tamanho = tamanho
            self.vertices = vertices
            self.arestas = arestas
        else:
            raise Exception("Grafo inconsistente")
    
    def qtdVertices(self):
        return self.tamanho
            
    def qtdArestas(self):
        return len(self.arestas)
        
    def grau(self, v):
        return len([a for a in self.arestas if v in a])

    def indice(self, rotulo):
        return self.vertices.index(rotulo)+1
        
    def rotulo(self, v):
        return self.vertices[v-1]
    
    def vizinhos(self, v):
        if self.orientado:
            arestasV = []
            for a in self.arestas:
                if v == a[0]:
                    arestasV.append(list(a))
            for a in arestasV:
                a.remove(v)
        else:  
            arestasV = [list(a) for a in self.arestas if v in a]
            for a in arestasV:
                a.remove(v)
        return {a[0] for a in arestasV}

    def haAresta(self, v, u):
        if self.orientado:
            return (v, u) in self.arestas
        else:
            return (u, v) in self.arestas or (v, u) in self.arestas

    def peso(self, v, u):
        if self.haAresta(v, u):
            try:
                return self.arestas[(v, u)]
            except:
                return self.arestas[(u, v)]
        else:
            return math.inf

#debug
'''
G = Grafo(arquivo='teste1.grafo')
#G = Grafo(tamanho=3, vertices=[1, 'segundo', 3], arestas={(1, 2):10, (1, 1):1})
G = Grafo(arquivo='instancias\ciclo_euleriano\ContemCicloEuleriano.net')


print(G.qtdVertices())
print(G.qtdArestas())
print(G.grau(2))
print(G.rotulo(2))
print(G.vizinhos(2))
print(G.haAresta(2, 1))
print(G.peso(2, 2))
'''