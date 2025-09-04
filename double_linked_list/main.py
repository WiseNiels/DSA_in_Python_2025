class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0
        
    # adiciona no final
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._length += 1
        return self
    
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._length += 1
        return self


    def pop_left(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self._length -= 1
        return removed_data

    def pop_right(self):
        if not self.tail:
            return None
        removed_data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self._length -= 1
        return removed_data


    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self._length -= 1
                return True
            current = current.next
        return False
    
    def remove_value(self, data):
       if not self._length:
           raise ValueError("List is empty")
       if self.head.data == data:
           return self.pop_left()
       if self.tail.data == data:
           return self.pop_right()
       previous_node = self.head
       current_node = self.head.next
       while current_node:
           if current_node.data == data:
               previous_node.next = current_node.next
               if current_node.next:
                   current_node.next.prev = previous_node
               self._length -= 1
               return True
           previous_node = current_node
           current_node = current_node.next
       return False
   
    
    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False