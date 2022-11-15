from collections import deque


def undirected_path_breadth(edges, node_A, node_B):

    graph = build_graph(edges)

    queue = deque([node_A])
    visited = set()

    while queue:
        current = queue.popleft()
        if current not in visited:
            if current == node_B:
                return True
            for neighbour in graph[current]:
                queue.append(neighbour)

        visited.add(current)

    return False


def undirected_path_depth(edges, node_A, node_B):
  
  graph = build_graph(edges)
  
  stack = [node_A]
  
  visited = set()
  
  while stack:
    current = stack.pop()
    if current not in visited:
      if current == node_B:
        return True

      for neighbour in graph[current]:
        stack.append(neighbour)
        
    visited.add(current)
  
  return False
  
  
  
def build_graph(edges):
  graph = {}
  
  for edge in edges:
    a, b = edge
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
      
    graph[a].append(b)
    graph[b].append(a)
  
  return graph