class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.max_allowed_size = 10

    def push(self, value):
        if self.size >= self.max_allowed_size:
            raise OverflowError("Stack overflow")
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        return new_node.value

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    def is_empty(self):
        return self.top is None



stc = Stack()

print(stc.push(1))  # Output: 1