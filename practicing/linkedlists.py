class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
    
    def __repr__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    #O(1)
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
    #O(1)
    def size_of_list(self):
        return self.num_of_nodes

    #O(n)
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            #thats why O(n)
            actual_node = self.head
            while actual_node.next_node is not None:
                actual_node = node.next_node

            actual_node.next_node = new_node
            new_node.next_node = None
    #O(n)
    def remove(self, data):
        if self.head is None:
            return
        
        actual_node = self.head
        previous_node = None
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node
        if actual_node is None:
            return
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node

        


    #O(n)
    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node
            
            

if __name__ == '__main__':
    linked_list = LinkedList()
    
    linked_list.insert_start(10)
    linked_list.insert_start('adam')
    linked_list.remove('10')
    
    linked_list.traverse()