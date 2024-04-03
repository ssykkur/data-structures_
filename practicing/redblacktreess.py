class Color:
    RED = 1
    BLACK = 2 


class Node:
    def __init__(self, data, parent=None, color=Color.RED):
        self.data = data
        self.parent = parent
        self.color = color
        self.right_node = None
        self.left_node = None
    
    def __repr__(self):
        return str(self.data)


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.settle_violation(self.root)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_node: 
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                self.settle_violation(node.left_node)
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                self.settle_violation(node.right_node)
    
    def settle_violation(self, node):

                                    #checking for double red
        while node != self.root and self.is_red(node) and self.is_red(node.parent):
            
            parent_node = node.parent
            grandparent_node = parent_node.parent

            if parent_node == grandparent_node.left_node:
                uncle = grandparent_node.right_node

                #uncle is red (1black depth) => recolor, 
                if self.is_red(uncle):
                    self.recolor(grandparent_node)
                    self.recolor(parent_node)
                    self.recolor(uncle)
                    node = grandparent_node
                #uncle is black (2black depth so need to rotate) => rotation + recolor
                else:
                    #straighten up the tree (right heavy situation)
                    if node == parent_node.right_node:
                        self.rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent
                    
                    self.recolor(parent_node)
                    self.recolor(grandparent_node)
                    self.rotate_right(grandparent_node)
            else:
                print('1')
                uncle = grandparent_node.left_node

                #uncle is red => recolor
                if self.is_red(uncle):
                    self.recolor(grandparent_node)
                    self.recolor(parent_node)
                    self.recolor(uncle)
                    node = grandparent_node
                else:
                    if node == parent_node.left_node:
                        
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent
                    
                    self.recolor(parent_node) 
                    self.recolor(grandparent_node)
                    self.rotate_left(grandparent_node)
            
        if self.is_red(self.root):
            self.recolor(self.root)
    
    def recolor(self, node):
        if node.color == Color.RED:
            node.color = Color.BLACK
            print(f'recoloring {node} to black')
        else:
            node.color = Color.RED
            print(f'recoloring {node} to red')
        
    def is_red(self, node):
        if node is None:
            return False
        
        return node.color == Color.RED

    def traverse(self):
        if self.root:
            self.in_order_traversal(self.root)

    def in_order_traversal(self, node):
        if node.left_node:
            self.in_order_traversal(node.left_node)
        print(node)
        if node.right_node:
            self.in_order_traversal(node.right_node)

    def rotate_right(self, node):
        print(f'right rotation on {node}')

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node

        temp_left_node.parent = temp_parent

        if temp_left_node.parent:
            if temp_left_node.parent.left_node == node:
                temp_left_node.parent.left_node = temp_left_node
            else:
                temp_left_node.parent.right_node = temp_left_node
        else:
            self.root = temp_left_node

    def rotate_left(self, node):
        print(f'left rotation on {node}')

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent:
            if temp_right_node.parent.left_node == node:
                temp_right_node.parent.left_node = temp_right_node
            else:
                temp_right_node.parent.right_node = temp_right_node
        else:
            self.root = temp_right_node


if __name__ == '__main__':
    tee = RedBlackTree()
    tee.insert(30)
    tee.insert(40)
    tee.insert(45)
    tee.insert(44)
    tee.traverse()
    
    
