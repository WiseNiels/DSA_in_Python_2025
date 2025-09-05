class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        removed_data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.size -= 1
        return removed_data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data

    def get_size(self):
        return self.size