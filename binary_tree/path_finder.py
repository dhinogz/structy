from node import Node



def path_finder(root, target):

    path = _path_finder(root, target)

    if path is None:
        return None
    else:
        return path[::-1]


def _path_finder(root, target):

    if root is None:
        return None
    
    if root.val == target:
        return [root.val]

    left_path = _path_finder(root.left, target)
    if left_path is not None:
        # return [root.val, *left_path]
        
        left_path.append(root.val)
        return left_path

    right_path = _path_finder(root.right, target)
    if right_path is not None:
        # return [root.val, *right_path]
        
        right_path.append(root.val)
        return right_path

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

print(path_finder(a, 'e'))