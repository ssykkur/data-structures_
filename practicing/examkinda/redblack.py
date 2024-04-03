import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')


class Color:
    red = 1
    black = 2



class Node:
    
    def __init__(self, data, parent=None, color=Color.red):
        self.data = data
        self.color = color
        self.parent = parent
        self.right = None
        self.left = None
        
    def __repr__(self):
        return str(self.data)


    
class redblackTree:

    def __init__(self):
        self.root = None


    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            self.settle_violation(self.root)

        else:
            self.insert_node(self.root, data)

    def insert_node(self, node, data):
        if data < node.data:
            if node.left:
                self.insert_node(node.left, data)
                
            else:
                node.left = Node(data, node)
                self.settle_violation(node.left)
        else:
            if node.right:
                self.insert_node(node.right, data)
                
            else:
                node.right = Node(data, node)
                logging.debug(f'inserted {node.right} with color {node.right.color} and parent {node} ')
                
                self.settle_violation(node.right)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return

        if data > node.data:
            self.remove_node(data, node.right)
        elif data < node.data:
            self.remove_node(data, node.left)
        
        #found the node
        else:
            parent = node.parent
            #leaf 
            if not node.right and not node.left:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.root = None
                del node
                self.settle_violation(parent)
            #one right 
            elif node.right and not node.left:
                if parent:
                    if parent.left == node:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                else:
                    self.root = node.right
                node.right.parent = parent
                del node
                self.settle_violation(parent)
            #one left
            elif not node.right and node.left:
                if parent:
                    if parent.left == node:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                else:
                    self.root = node.left
                node.left.parent = parent
                del Node
                self.settle_violation(parent)
            #two 
            else:
                predecessor = self.get_predecessor(node.left)

                temp = predecessor.data
                predecessor.data = node.data

                node.data = temp
                self.remove_node(predecessor)

    
    def get_predecessor(self):
        if node.right:
            self.get_predecessor(node.right)
        return node
                    

    def settle_violation(self, node):
        
        #checking for double red
        while node != self.root and self.is_red(node) and self.is_red(node.parent):
            
            parent_node = node.parent
            grandparent_node = parent_node.parent

            if grandparent_node.left == parent_node:
                uncle = grandparent_node.right
                #uncle is red => recolor
                if self.is_red(uncle):
                    self.recolor(uncle)
                    self.recolor(parent_node)
                    self.recolor(grandparent_node)

                    node = grandparent_node
                #uncle is black => rotation and recolor
                else:
                    if parent_node.right == node:
                        self.rotate_left(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    self.recolor(grandparent_node)
                    self.recolor(parent_node)
                    self.rotate_right(grandparent_node)
            else:
                uncle = grandparent_node.left
                #uncle is red => recolor
                if self.is_red(uncle):
                    self.recolor(uncle)
                    self.recolor(parent_node)
                    self.recolor(grandparent_node)
                    node = grandparent_node
                #uncle is black => rotation and recolor
                else:
                    if parent_node.left == node:
                        self.rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent
                    
                    self.recolor(grandparent_node)
                    self.recolor(parent_node)
                    self.rotate_left(grandparent_node)
        
        if self.is_red(self.root):
            
            self.recolor(self.root)

            
    def recolor(self, node):
        if node.color == Color.red:
            node.color = Color.black
            logging.info(f'recoloring {node} to black')
        else:
            node.color = Color.red
            logging.info(f'recoloring {node} to red')

        
    def is_red(self, node):
        if not node:
            return False
        return node.color == Color.red 


    def rotate_left(self, node):

        logging.info(f'left rotation on {node}')

        temp_right = node.right
        t = temp_right.left

        temp_right.left = node
        node.right = t

        if t:
            t.parent = node
        
        temp_parent = node.parent
        node.parent = temp_right
        temp_right.parent = temp_parent

        if temp_parent:
            if temp_parent.right == node:
                temp_parent.right = temp_right
            else:
                temp_parent.left = temp_right
        else:
            self.root = temp_right


    def rotate_right(self, node):

        logging.info(f'right rotation on {node}')

        temp_left = node.left
        t = temp_left.right

        temp_left.right = node
        node.left = t
        
        if t:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left

        if temp_parent:
            if temp_parent.right == node:
                temp_parent.right = temp_left
            else:
                temp_parent.left = temp_left
        else:
            self.root = temp_left


    def traverse(self):
        if self.root:
            self.in_order_traversal(self.root)

    
    def in_order_traversal(self, node):
        if node.left:
            self.in_order_traversal(node.left)
        print(node)
        if node.right:
            self.in_order_traversal(node.right)



if __name__ == '__main__':
    rdt = redblackTree()
    rdt.insert(21)
    rdt.insert(30)
    rdt.insert(18)
    rdt.insert(19)

    rdt.traverse()
    
    
    
