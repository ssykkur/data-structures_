class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return
        
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            #leaf node scenario
            if node.left_node is None and node.right_node is None:
                print(f'removing leaf node {node.data}')
                parent = node.parent
            
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:
                    self.root = None
                
                del node
            #rem a node with a single right child
            elif node.left_node is None and node.right_node is not None:
                parent = node.parent
                print('minus a node with right child')
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                if parent is None:
                    self.root = node.right_node
                
                node.right_node.parent = parent
                del node
            #removing a node with a single left child
            elif node.right_node is None and node.left_node is not None:
                parent = node.parent 
                print('minus a node with left child')
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node
            # removing a node with two children 
            else:
                print('removing a node with two children')
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
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left_node:
            return self.get_min_value(node.left_node)
        return node.data

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_node:
            return self.get_max_value(node.right_node)
        return node.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)
        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)

    

bst = BinarySearchTree()
bst.insert(1)
bst.insert(15)
bst.insert(8)
bst.insert(25)
bst.insert(4)
bst.insert(56)
bst.remove(4)
bst.remove(15)

bst.traverse()