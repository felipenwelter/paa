# Exercício utilizando grafos
# Objetivo: verificar se o grafo tem ciclo euleriano e qual é o ciclo
# 1 - montar um grafo simples não direcionado
# 2 - verificar se é conexo (se todos os vértices estão conectados)
# 3 - verificar se os vértices estão em grau par
# 4 - procurar o ciclo euleriano (não é caminho euleriano)
# 5 - dar a complexidade da implementação dos itens 2, 3 e 4

import csv

class Grafo:
    def __init__(self, direcionado=False):
        self.vertices = []
        self.visitedVertices = []
        self.adjacent = []
        self.arestas = []

    def newVertice(self, ident):
        self.vertices.append( ident )
        self.visitedVertices.append(0)
        self.adjacent.append( [] )

    def newAresta(self, v1, v2):
        self.arestas.append( [v1, v2] )

    def montaAdjacentes(self):
        for i in self.arestas:
            self.adjacent[i[0]-1].append( i[1] )
            self.adjacent[i[1]-1].append( i[0] )

    def importFromTxt(self):
        nLine = 0
        with open('./paa/graphs-exercise/graph-content.txt', newline='') as inputfile:
            for row in csv.reader(inputfile):
                nLine += 1
                if (nLine == 1): #na primeira linha encontra todos os vertices
                    for i in row:
                        self.newVertice( int(i) )
                else: #nas demais linhas encontra as arestas
                    self.newAresta( int(row[0]), int(row[1]) )
        self.montaAdjacentes()

    def depth_search(self,vIndex): # recebe o index do vertice a fazer a busca em profundidade
        self.visitedVertices[ vIndex ] = 1 # marca vertice como visitado (pelo seu indice)
        for adj in self.adjacent[ vIndex ]: # para cada vértice adjacente (busca pelo índice)
            if (self.visitedVertices[ self.vertices.index(adj) ] == 0): # verifica se ainda não foi visitado
                self.depth_search( self.vertices.index(adj) ) # busca nos vertices ligados, passando o index

    def isConnected(self): # verifica se grafo é conexo
        self.depth_search(0)  #busca nos vertices ligados, passando o index de um elemento qualquer
        if (self.visitedVertices.count(0) > 0): #verifica se algum vertice nao foi visitado após a busca
            return False
        else:
            return True


grafo = Grafo()
grafo.importFromTxt()
isConnected = grafo.isConnected()
print("grafo conexo? %r" % isConnected)


#Ref:
#http://www.professeurs.polymtl.ca/michel.gagnon/Disciplinas/Bac/Grafos/Busca/busca.html#Prof