
def leaf_list(root):
    leafs = []
    _leaf_list(root, leafs)
    return leafs

def _leaf_list(root, leafs):

    if root is None:
        return

    if root.left is None and root.right is None:
        leafs.append(root.val)

    _leaf_list(root.left, leafs)
    _leaf_list(root.right, leafs)