class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def insert(self, data):
        new_node = Node(data)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def pop_left(self):
        if not self._length:
            raise IndexError("pop from empty list") 
        removed_data = self.head
        self.head = removed_data.next
        removed_data.next = None
        self._length -= 1
        return removed_data.data
    
    def pop_right(self):
        if not self._length:
            raise IndexError("pop from empty list")
        if self._length == 1:
            self.head = self.tail = None
        current = self.head
        while current.next != self.tail:
            current = current.next
        removed_data = self.tail
        current.next = None
        self.tail = current
        self._length -= 1
        return removed_data.data
    

    def remove(self, data):
        if not self._length:
            raise ValueError("remove from empty list")
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if not current:
            raise ValueError(f"{data} not found in list")
        if previous:
            previous.next = current.next
        else:
            self.head = current.next
        if current == self.tail:
            self.tail = previous
        self._length -= 1
