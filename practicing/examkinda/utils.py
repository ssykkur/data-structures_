def rotate_left(node):
    
    temp_node = node.right
    t = node.right.left

    temp_node.left = node
    node.right = t

    if t:
        t.parent = node
    
    temp_parent = node.parent
