from collections import deque
from node import Node, a

def tree_sum_breadth_first(root):
    if root is None:
        return 0

    sum = 0
    queue = deque([root])

    while queue:
        current = queue.popleft()
        sum += current.val

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return sum


def tree_sum_depth_first(root):
    if root is None:
        return 0

    sum = 0
    stack = [root]

    while stack:
        current = stack.pop()
        sum += current.val

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return sum


def tree_sum_recursive(root):

    if root is None:
        return 0

    return root.val + tree_sum_recursive(root.left) + tree_sum_recursive(root.right)

