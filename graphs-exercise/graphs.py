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
        self.visitedArestas = []
        self.adjacent = []
        self.arestas = []
        self.eulerCycle = []

    def newVertice(self, ident):
        self.vertices.append( ident )
        self.visitedVertices.append(0)
        self.adjacent.append( [] )

    def newAresta(self, v1, v2):
        self.arestas.append( [v1, v2] )
        self.visitedArestas.append(0)

    def montaAdjacentes(self):
        for i in self.arestas:
            nPos1 = self.vertices.index(i[0])
            nPos2 = self.vertices.index(i[1])
            self.adjacent[nPos1].append( i[1] )
            self.adjacent[nPos2].append( i[0] )

    def importFromTxt(self):
        nLine = 0
        with open('./graphs-exercise/graph-content.txt', newline='') as inputfile:
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
        return (self.visitedVertices.count(0) == 0) #verifica se algum vertice nao foi visitado após a busca

    def isAllPair(self): #verifica se todos os vertices tem grau par
        for i in self.adjacent:
            if (len(i) % 2) > 0:
                return False
        return True


    def getArestaPosition(self,v1,v2):
        nPos = self.arestas.count([v1,v2])
        if nPos == 0:
            nPos = self.arestas.index([v2,v1])
        else:
            nPos = self.arestas.index([v1,v2])
        return nPos

    def alreadyVisitedAresta(self,v1,v2):
        nPos = self.getArestaPosition(v1,v2)
        return (self.visitedArestas[nPos] == 1)

    def depth_search_subcycle(self,vIndex,startV): # recebe o index do vertice a fazer a busca em profundidade
        
        # busca o menor subgrafo possível retornando ao vértice de origem (startV)

        # adiciona esse menor subgrafo no eulerCycle

        # para os demais vertices, busca o menor subgrafo possível, retornando à origem (startV)
        
        # adiciona no eulerCycle (no meio) 


        #ref https://www.youtube.com/watch?v=9dXQOMNptM8

        v1 = self.vertices[vIndex]

        if (vIndex != startV):
            try:
                lFound = False
                lFound = self.adjacent[vIndex].index( self.vertices[startV]) #compara para saber se é o menor subciclo
            except:
                print(x)

            if lFound:
                # fim do subciclo, recomeca
                print('fim do subciclo')
            else:
                # vai voltar, entao força o próximo vértice
                print('x')


        for adj in self.adjacent[ vIndex ]: # para cada vértice adjacente (busca pelo índice)
            v2 = adj
            nPos = self.getArestaPosition(v1,v2)
            if not (self.alreadyVisitedAresta(v1,v2)): # verifica se ainda não foi visitado
                self.visitedArestas[nPos] = 1
                self.eulerCycle.append(v1)
                self.depth_search_subcycle( self.vertices.index(adj),startV ) # busca nos vertices ligados, passando o index
            else:
                if (vIndex == startV):
                    self.eulerCycle.append(v1)






    def Hierholzer(self): #funcao para identificar circuito euleriano
        self.depth_search_subcycle(0,0)



grafo = Grafo()
grafo.importFromTxt()
isConnected = grafo.isConnected()
isPair = grafo.isAllPair()
grafo.Hierholzer()

print("grafo conexo? %r" % isConnected)
print("cada vertice tem numero par de arestas? %r" % isPair)
print("Euler Cycle: %r" % grafo.eulerCycle)


#Ref:
#http://www.professeurs.polymtl.ca/michel.gagnon/Disciplinas/Bac/Grafos/Busca/busca.html#Prof
#https://paginas.fe.up.pt/~rossetti/rrwiki/lib/exe/fetch.php?media=teaching:1011:cal:08_2.09_1.grafos6.pdf
