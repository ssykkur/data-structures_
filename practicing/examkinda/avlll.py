import logging

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class Node:
    
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.right = None
        self.left = None
        self.height = 0

    def __repr__(self):
        return str(self.data)
        


class AvlTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            logging.debug(f'inserted root {self.root}')
        else:
            self.insert_node(data, self.root)
    

    def insert_node(self, data, node):
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data, node)
                node.height = max(self.calc_height(node.right), self.calc_height(node.left)) + 1
                logging.debug(f'inserted {node.left}')

        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data, node)
                node.height = max(self.calc_height(node.right), self.calc_height(node.left)) + 1
                logging.debug(f'inserted {node.right}')

        self.settle_violation(node)


    def settle_violation(self, node):
        
        while node:
            node.height = max(self.calc_height(node.right), self.calc_height(node.left)) + 1
            self.violation_util(node)
            node = node.parent
    

    def violation_util(self, node):
        balance = self.calc_balance(node)
        #left heavy
        if balance > 1:
            #left right heavy
            if self.calc_balance(node.left) < 0:
                self.rotate_left(node.left)
            self.rotate_right(node)
        #right heavy
        if balance < -1:
            #right left heavy
            if self.calc_balance(node.right) > 0:
                self.rotate_right(node.right)
            self.rotate_left(node)


    def calc_height(self, node):
        if not node:
            return -1
        return node.height


    def calc_balance(self, node):
        if not node:
            return 0
        return self.calc_height(node.left) - self.calc_height(node.right)
    

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
            if temp_right.parent.right == node:
                temp_parent.right = temp_right
            else:
                temp_parent.left = temp_right
        else:
            self.root = temp_right

        node.height = max(self.calc_height(node.right), self.calc_height(node.left)) + 1

        temp_right.height = max(self.calc_height(temp_right.right), self.calc_height(temp_right.left)) + 1
    

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
        temp_left.parent = temp_parent

        if temp_parent:
            if temp_parent.right == node:
                temp_parent.right = temp_left
            else:
                temp_parent.left = temp_left
        else:
            self.root = temp_left

        node.height = max(self.calc_height(node.right), self.calc_height(node.left)) + 1
        temp_left.height = max(self.calc_height(temp_left.right), self.calc_height(temp_left.left)) + 1


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

    avl = AvlTree()
    avl.insert(20)
    avl.insert(15)
    avl.insert(14)
    print(avl.root.left.height)
    
    


    
    
    