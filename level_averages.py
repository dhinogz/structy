from collections import deque
from statistics import mean


def level_averages(root):
    levels = _level_averages(root)
    return [mean(level) for level in levels]


def _level_averages(root):

    if root is None:
        return []

    levels = []
    stack = [ (root, 0) ]

    while stack:

        current, level_num = stack.pop()

        if level_num == len(levels):
            levels.append([current.val])
        else:
            levels[level_num].append(current.val)
        
        if current.right:
            stack.append((root.right, level_num + 1))
        if current.left:
            stack.append((root.left, level_num + 1))

    return levels


def level_averages(root):
    levels = []
    _level_average(root, levels, 0)
    return [mean(level) for level in levels]

def _level_average(root, levels, level_num):

    if root is None:
        return []

    if level_num == len(levels):
        levels.append([root.val])
    else:
        levels[level_num].append(root.val)

    _level_average(root.left, levels, level_num)
    _level_average(root.right, levels, level_num)