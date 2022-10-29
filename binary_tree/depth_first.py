from node import Node

def depth_first_values(root):

    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        current = stack.pop()
        values.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return values

def depth_first_values_recursive(root):

    if not root:
        return []

    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    
    return [ root.val, *left_values, right_values.val ] 
        