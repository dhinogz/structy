from node import Node


def how_high(root):

    if root is None:
        return -1

    return 1 + max(how_high(root.left), how_high(root.right))