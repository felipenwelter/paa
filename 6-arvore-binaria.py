# Classe com a definição de um nó: chave, valor, nó esquerdo e nó direito (filhos)
class BSTNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Função que imprime os nós da árvore
def printnode(node):
    if (node != None):
        printnode(node.left)
        print('%s' % node.value)
        printnode(node.right)

#Monta manualmente a árvore abaixo:
#         10
#     05      15
#   04  06  12   18
# 02 
root = BSTNode(10)
root.left = BSTNode(5)
root.left.left = BSTNode(4)
root.left.right = BSTNode(6)
root.left.left.left = BSTNode(2)
root.right = BSTNode(15)
root.right.left = BSTNode(12)
root.right.right = BSTNode(18)

printnode(root)