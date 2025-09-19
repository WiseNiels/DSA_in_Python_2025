from collections import deque


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
    
    
    class BinarySearchTree:
        def __init__(self):
            self.root = None
            
        def breadth_first_traversal(self):
            if not self.root:
                raise Exception("Tree is empty")
            queue = deque()
            queue.append(self.root)
            
            visited = []
            while queue:
                visited_node = queue.popleft()
                visited.append(visited_node.data)
                if visited_node.left:
                    queue.append(visited_node.left)
                if visited_node.right:
                    queue.append(visited_node.right)
            return visited
            
            