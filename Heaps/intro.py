# As regras da Heap são:
# 1. A árvore é um heap máximo se o valor de cada nó for maior ou igual ao valor de seus filhos.
# 2. A árvore é um heap mínimo se o valor de cada nó for menor ou igual ao valor de seus filhos.
# 3. A árvore é uma árvore completa, ou seja, todos os níveis da árvore estão completamente preenchidos,
#    exceto possivelmente o último nível, que é preenchido da esquerda para a direita


class MaxBinaryHeap:
    def __init__(self):
        self.itens = []

    def insert(self, item):
        self.itens.append(item)
        self.move_up()

        return self

    def move_up(self):
        child_idx = len(self.itens) - 1

        while child_idx > 0:
            parent_idx = (child_idx - 1) // 2

            if self.itens[child_idx] <= self.itens[parent_idx]:
                break

            self.swap(child_idx, parent_idx)
            child_idx = parent_idx

    def swap(self, idx1, idx2):
        self.itens[idx1], self.itens[idx2] = self.itens[idx2], self.itens[idx1]

    def remove_max(self):
        if len(self.itens) == 0:
            return None

        if len(self.itens) == 1:
            return self.itens.pop()

        max_item = self.itens[0]

        end_idx = len(self.itens) - 1
        self.swap(0, end_idx)
        self.itens.pop()

        self.move_down()

        return max_item

    def move_down(self):
        parent_idx = 0
        
        while True:
            left_child_idx = 2 * parent_idx + 1
            right_child_idx = 2 * parent_idx + 2
            largest_idx = parent_idx

            if (
                left_child_idx < len(self.itens)
                and self.itens[left_child_idx] > self.itens[largest_idx]
            ):
                largest_idx = left_child_idx
            if (
                right_child_idx < len(self.itens)
                and self.itens[right_child_idx] > self.itens[largest_idx]
            ):
                largest_idx = right_child_idx

            if largest_idx == parent_idx:
                break

            self.swap(parent_idx, largest_idx)
            parent_idx = largest_idx
