class Node:
    
    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent

    def __repr__(self):
        return str(self.data)

class BinarySearchTree:

    def __init__(self):
        #can access the root node exclusively
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data):
        if node is None:
            return
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            #leaf node 
            if node.left_node is None and node.right_node is None:
                print(f'removing a leaf node {node}')
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:
                    self.root = None

                del node
            #
            elif node.left_node is None and node.right_node is not None:
                print(f'del node with 1 right child {node}')
                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent

                del node
            
            elif node.left_node is not None and node.right_node is None:
                print(f'del node with 1 right left {node}')
                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent

                del node
    
            else:
                print(f'removing a node with 2: {node}')
                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)
            

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)


    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                #left node exist, continue\start the recursive cycle
                self.insert_node(data, node.left_node)
            else:
                #no left node => create one
                node.left_node = Node(data, node) 
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)


    def get_min(self):
        if self.root:
           return self.get_min_val(self.root)


    def get_min_val(self, node):
        if node.left_node:
           return self.get_min_val(node.left_node)
        return node


    def get_max(self):
        if self.root:
            return self.get_max_val(self.root)


    def get_max_val(self, node):
        if node.right_node:
            return self.get_max_val(node.right_node)

        return node


    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)


    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)
        print(node)
        if node.right_node:
            self.traverse_in_order(node.right_node)
        


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(12)
    bst.insert(4)
    bst.insert(11)
    bst.insert(-1)
    bst.insert(50)
    bst.insert(-30)
    bst.traverse()
   
    print(f'max value is {bst.get_max()}')
    print(f'min value is {bst.get_min()}')

    
    