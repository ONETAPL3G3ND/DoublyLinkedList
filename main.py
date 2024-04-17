class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return
            current = current.next

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)

    dll.prepend(0)

    dll.display_forward()
    dll.display_backward()

    dll.delete(2)

    dll.display_forward()
    dll.display_backward()
