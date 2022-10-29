from node import Node
from collections import deque


def tree_includes(root, target):
    if root is None:
        return False

    stack = [root]

    while stack:
        current = stack.pop()
        if current.val == target:
            return True
        
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return False


def tree_includes_queue(root, target):
    if root is None:
        return False

    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current.val == target:
            return True
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return False
    


def tree_includes_recursive(root, target):

    if root is None:
        return False

    if root.val == target:
        return True

    return tree_includes_recursive(root.left, target) or tree_includes_recursive(root.right, target)