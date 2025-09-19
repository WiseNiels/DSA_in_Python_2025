

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
    
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def dft_pre_order_iterative(self):
        if not self.root:
            raise Exception("Tree is empty")
        stack = [self.root]
        
        visited = []
        while stack:
            visited_node = stack.pop()
            visited.append(visited_node.data)
            if visited_node.left:
                stack.append(visited_node.left)
            if visited_node.right:
                stack.append(visited_node.right)
            if visited_node.left:
                stack.append(visited_node.left) 
        return visited
        
        