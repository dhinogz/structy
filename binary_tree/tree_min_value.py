from node import Node
from collections import deque

def tree_min_value_depth(root):
    if root is None:
        return 0

    stack = [root]

    min_value = float("inf")

    while stack:
        current = stack.pop()

        min_value = min(min_value, current.val)

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return min_value


def tree_min_value_breadth(root):
    if root is None:
        return 0

    queue = deque([root])
    min_value = float("inf")

    while queue:
        current = queue.popleft()

        min_value = min(min_value, current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return min_value


def tree_min_value_recursive(root):

    if root is None:
        return float("inf")

    smallest_left_value = tree_min_value_recursive(root.left)
    smallest_right_value = tree_min_value_recursive(root.right)
    
    return min(root.val, smallest_left_value, smallest_right_value)