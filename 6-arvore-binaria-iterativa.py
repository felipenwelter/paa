# Classe com a definição de um nó: valor, nó esquerdo e nó direito (filhos)
class BSTNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Função que imprime os nós da árvore
def printnode(node):
    #forma recursiva
#    if (node != None):
#        printnode(node.left)
#        print('%s' % node.value)
#        printnode(node.right)

    #forma iterativa
    p = node #raiz
    stack = [] #pilha
    
    while (p != None):

        while (p != None):
            if (p.right != None): #desce primeiro ao nó direito e o armazena
                stack.append(p.right)
            stack.append(p) #armazena o nó raiz
            p = p.left #desce ao nó esquerdo

        p = stack[ stack.__len__()-1 ] #seleciona último nó e remove da pilha
        stack.pop()

        #imprime os nós que não permitem ir a direita
        while ( stack.__len__() > 0) & (p.right == None):
            print("%d" % p.value)
            p = stack[ stack.__len__()-1 ] #seleciona último nó e remove da pilha
            stack.pop()
            
        print("%d" % p.value)  ##imprime nó pai
        
        if ( stack.__len__() > 0):
            p = stack[ stack.__len__()-1 ]
            stack.pop()
        else:
            p = None

            
#Monta manualmente a árvore abaixo:
#          10
#     05        15
#   04  06    12   18
# 02      09
root = BSTNode(10)
root.left = BSTNode(5)
root.left.left = BSTNode(4)
root.left.right = BSTNode(6)
root.left.left.left = BSTNode(2)
root.left.right.right = BSTNode(9)
root.right = BSTNode(15)
root.right.left = BSTNode(12)
root.right.right = BSTNode(18)

printnode(root)