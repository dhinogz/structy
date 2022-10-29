from collections import deque

def tree_levels(root):
    """
    Return a 2 dimensional list. Each siblist represents 
    a level in the tree

    Iterative Approach:
        Store root and level 0 as a tuple in preffered data structure
        While data structure exists
        Get current node and level
        If the level is equal to the length of our list of lists
            Append current val in a list
        else
            Append current val in list index level_num in list
        
        If next node exists (right or left)
            Add node to data structure as a tuple with level + 1

    """

    if root is None:
        return []

    levels = []
    queue = deque( [ (root, 0) ] )

    while queue:
        current, level_num = queue.popleft()

        if level_num == len(levels):
            levels.append([current.val])
        else:
            levels[level_num].append(current.val)
        
        if current.left:
            queue.append((current.left, level_num+1))

        if current.right:
            queue.append((current.right, level_num+1))

    return levels




    # if root is None:
    #     return []

    # levels = []
    # stack = [ (root, 0) ]

    # while stack:

    #     current, level = stack.pop()

    #     if level == len(levels):
    #         levels.append( [ current.val ] )
    #     else:
    #         levels[level].append([current.val])

    #     if current.right:
    #         stack.append((current.right, level+1))
    #     if current.left:
    #         stack.append((current.left, level+1))


    # return levels



def tree_levels(root):
    levels = []
    _tree_levels(root, levels, 0)
    return levels

def _tree_levels(root, levels, level_num):

    if root is None:
        return []

    if len(levels) == level_num:
        levels.append([root.val])
    else:
        levels[level_num].append(root.val)

    _tree_levels(root.left, levels, level_num + 1)
    _tree_levels(root.right, levels, level_num + 1)
