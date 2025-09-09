from collections import deque

# Definição do nó
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Definição da árvore binária
class BinaryTree:
    def __init__(self):
        self.root = None

    # -------------------------------------------------
    # Etapa 1: Implementar a inserção automática por nível
    # -------------------------------------------------
    
    def insert_level_order(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node.left:
                node.left = new_node
                return
            else:
                q.append(node.left)

            if not node.right:
                node.right = new_node
                return
            else:
                q.append(node.right)

    # -----------------------------------------
    # Etapa 2: Implementar as funções de travessia
    # -----------------------------------------

    def inorder(self, node):
        if not node:
            return []
        return self.inorder(node.left) + [node.data] + self.inorder(node.right)

    def preorder(self, node):
        if not node:
            return []
        return [node.data] + self.preorder(node.left) + self.preorder(node.right)

    def postorder(self, node):
        if not node:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.data]

    def level_order(self):
        if not self.root:
            return []
        result = []
        q = deque([self.root])
        while q:
            node = q.popleft()
            result.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return result

    # -------------------------
    # Etapa 3: Implementar os algoritmos de verificação estrutural
    # -------------------------

    # Árvore perfeita -> todos os níveis cheios
    def is_perfect(self):
        def depth(node):
            d = 0
            while node:
                d += 1
                node = node.left
            return d

        def check(node, level, d):
            if not node:
                return True
            if not node.left and not node.right:
                return d == level + 1
            if not node.left or not node.right:
                return False
            return check(node.left, level + 1, d) and check(node.right, level + 1, d)

        d = depth(self.root)
        return check(self.root, 0, d)

    # Árvore completa -> todos os níveis cheios, exceto o último, preenchido da esquerda p/ direita
    def is_complete(self):
        if not self.root:
            return True
        q = deque([self.root])
        flag = False
        while q:
            node = q.popleft()
            if node:
                if flag:
                    return False
                q.append(node.left)
                q.append(node.right)
            else:
                flag = True
        return True

    # Regular -> Todos os nós tem 0 ou 2 filhos
    def is_regular(self):
        def check(node):
            if not node:
                return True
            if (node.left and not node.right) or (node.right and not node.left):
                return False
            return check(node.left) and check(node.right)
    
        return check(self.root)


    # Balanceada -> diferença entre alturas das subárvores ≤ 1
    def is_balanced(self, node=None):
        def check(node):
            if not node:
                return 0, True
            lh, lb = check(node.left)
            rh, rb = check(node.right)
            return 1 + max(lh, rh), lb and rb and abs(lh - rh) <= 1
        return check(self.root)[1]

    # Desbalanceada → contrário de balanceada
    def is_unbalanced(self):
        return not self.is_balanced()

    # -------------------------
    # Função de classificação final
    # -------------------------

    def classify(self):
        classes = []
        if self.is_perfect():
            classes.append("Perfeita")
        if self.is_complete():
            classes.append("Completa")
        if self.is_regular():
            classes.append("Regular")
        if self.is_balanced():
            classes.append("Balanceada")
        if self.is_unbalanced():
            classes.append("Desbalanceada")
        return classes
        
    def print_tree(self, node=None, level=0, prefix="Raiz: "):
        if node is None:
            node = self.root
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.data))
            if node.left or node.right:
                if node.left:
                 self.print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self.print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")


if __name__ == "__main__":
    valores = [1, 2, 3, 4, 5, 6, 7]
    arvore = BinaryTree()
    for v in valores:
        arvore.insert_level_order(v)

    print("In-Order:", arvore.inorder(arvore.root))
    print("Pré-Order:", arvore.preorder(arvore.root))
    print("Pós-Order:", arvore.postorder(arvore.root))
    print("Level-Order:", arvore.level_order())
    print("Classificação da árvore:", arvore.classify())
    print("\nÁrvore (deitada):")
    arvore.print_tree()
