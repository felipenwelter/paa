# Exercício utilizando grafos
# Objetivo: verificar se o grafo tem ciclo euleriano e qual é o ciclo
# 1 - montar um grafo simples não direcionado
# 2 - verificar se é conexo (se todos os vértices estão conectados)
# 3 - verificar se os vértices estão em grau par
# 4 - procurar o ciclo euleriano (não é caminho euleriano)
# 5 - dar a complexidade da implementação dos itens 2, 3 e 4

import csv

class Grafo:
    def __init__(self, direcionado=True):
        self.lista_vertices = []
        self.lista_arestas = []

    def newVertice(self, ident):
        self.lista_vertices.append( ident )

    def newAresta(self, v1, v2):
        self.lista_arestas.append ( [v1, v2] )

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


grafo = Grafo()
grafo.importFromTxt()
