import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.right = None
        self.left = None

    def __repr__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_r(data, self.root)
    
    def traverse(self):
        if not self.root:
            return 
        else:
            self.traverse_r(self.root)

    def insert_r(self, data, node):
        if data < node.data:
            if node.left:
                self.insert_r(data, node.left)
            else:
                node.left = Node(data, node)
        else:
            if node.right:
                self.insert_r(data, node.right)
            else:
                node.right = Node(data, node)

    def traverse_r(self, node):
        if node.left:
            self.traverse_r(node.left)
        print(node)
        if node.right:
            self.traverse_r(node.right)
    


if __name__ == '__main__':

    tr = Tree()
    tr.insert(20)
    tr.insert(30)
    tr.insert(15)
    tr.insert(16)
    tr.insert(25)
    tr.traverse()

