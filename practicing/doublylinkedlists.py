class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

    def __repr__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_of_nodes = 0
    
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def insert_start(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node

    def traverse_forward(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    def traverse_backward(self):
        actual_node = self.tail

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.previous_node


if __name__ == '__main__':

    dls = DoublyLinkedList()
    dls.insert_end(1)
    dls.insert_end(2)
    dls.insert_end(3)
    dls.insert_end(4)
    dls.insert_end(5)
    dls.insert_start(6)
    dls.insert_start(7)
    dls.insert_start(8)
    dls.insert_start(9)
    dls.traverse_forward()