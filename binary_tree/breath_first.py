
from collections import deque

def breadth_first_values(root):
    """
    Queue from collections is used to make O(1) pop.
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if root is None:
        return []

    queue = deque([root])
    values = []

    while queue:
        current = queue.popleft()
        values.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return values