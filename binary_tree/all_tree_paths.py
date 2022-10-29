from node import Node



def all_tree_paths(root):

    if root is None:
        return []
    
    if root.left is None and root.left is None:
        return [ [root.val] ]

    paths = []

    left = all_tree_paths(root.left)
    for sub_path in left:
        paths.append([root.val, *sub_path])

    right = all_tree_paths(root.right)
    for sub_path in right:
        paths.append([root.val, *sub_path])

    return paths

def all_tree_paths(root):

    if root is None:
        return []

    stack = [root]
    temp = []
    res = []

    while stack:
        current = stack.pop()

        if current.left:
            stack.append(current.left)
            temp.append(current.val)
        else:
            res.append(temp)

        if current.right:
            stack.append(current.right)
            temp.append(current.val)
        else:
            res.append(temp)

    return res
    


        