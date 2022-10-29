from node import Node
from collections import deque



def tree_value_count(root: Node, target: int) -> int:

    if root is None:
        return 0

    match = 1 if root.val == target else 0

    return match + tree_value_count(root.left, target, target) + tree_value_count(root.right, target, target)



def tree_value_count(root: Node, target: int):

    if root is None:
        return 0

    count = 0
    stack = [root]

    while stack:
        current = stack.pop()
        
        if current.val == target:
            count += 1

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)


    return count


def tree_value_count_q(root: Node, target: int):

    if root is None:
        return 0

    count = 0
    queue = deque([root])

    if queue:
        current = queue.popleft()

        if current.val == target:
            count += 1
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

