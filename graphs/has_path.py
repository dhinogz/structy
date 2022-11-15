from collections import deque


def has_path_depth(graph, src, dst):

    stack = [src]

    while stack:
        current = stack.pop()
        if current == dst:
            return True
        for neighbour in graph[current]:
            stack.append(neighbour)

    return False


def has_path_breadth(graph, src, dst):

    queue = deque([src])

    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        for neighbour in graph[current]:
            queue.append(neighbour)

    return False


def has_path_recursive(graph, src, dst):

    if src == dst:
        return True
    for neighbour in graph[src]:
        if has_path_recursive(graph, neighbour, dst):
            return True 
    return False