class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0

    def __repr__(self):
        return str(self.data)


class AVLTree:

    def __init__(self):
        self.root = None

    def remove(self, data):
        if not self.root:
            self.root = Node(data)

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
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1

        self.handle_violation(node)

    def remove_node(self, data, node):
        if node is None:
            return
        
        if data > node.data:
            self.remove_node(data, node.right_node)
        elif data < node.data:
            self.remove_node(data, node.left_node)

        else:
            #leaf case
            if not node.left_node and not node.right_node:
                parent = node.parent
                if parent:
                    if parent.left_node == node:
                        parent.left_node = None
                    else:
                        parent.right_node = None
                else:
                    self.root = None
                del node
                self.handle_violation(parent)

            #right node
            elif not node.left_node and node.right_node:
                parent = node.parent
                if parent:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    else:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node
                node.right_node.parent = parent
                del node
                self.handle_violation(parent)

            #left node
            elif node.left_node and not node.right_node:
                parent = node.parent
                if parent:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    else:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node
                node.left_node.parent = parent
                del node 
                self.handle_violation(parent)

            #two nodes:
            else:
                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                
                self.remove_node(data, predecessor)

    def rotate_right(self, node):
        print(f'right rotation on node{node}')
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
        
        node.height = max(self.calc_height(node.left_node),
                            self.calc_height(node.right_node)) + 1

        temp_left_node.height = max(self.calc_balance(temp_left_node.left_node),
                                    self.calc_height(temp_left_node.right_node)) + 1
    
    def rotate_left(self, node):
        print(f'left rotation on node {node}')
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
        
        node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
        temp_right_node.height = max(self.calc_height(temp_right_node.left_node), self.calc_height(temp_right_node.right_node)) + 1

    def get_predecessor(self, data, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node


    #checking balance from bottom up
    def handle_violation(self, node):
        while node is not None:
            node.height = max(self.calc_height(node.left_node),
                                self.calc_height(node.right_node)) + 1
            self.violation_helper(node)
            node = node.parent

            
    def violation_helper(self, node):
            balance = self.calc_balance(node)
            #left heavy
            if balance > 1:
                #left right heavy
                if self.calc_balance(node.left_node) < 0:
                    self.rotate_left(node.left_node)
                self.rotate_right(node)
            #right heavy
            if balance < -1:
                #right left heavy
                if self.calc_balance(node.right_node) > 0:
                    self.rotate_right(node.right_node)
                self.rotate_left(node)


    def calc_height(self, node):
        if node is None:
            return -1

        return node.height
    

    def calc_balance(self, node):
        if node is None:
            return 0
        
        return self.calc_height(node.left_node) - self.calc_height(node.right_node)


if __name__ == '__main__':
    avl = AVLTree()
    avl.insert(16)
    avl.insert(15)
    avl.insert(17)