def largest_component(graph):
  
  visited = set()
  max_count = 0

  for node in graph:
    if node not in visited:
      stack = [node]
      count = 0

      while stack:
        current = stack.pop()
        if current not in visited:
          for neighbour in graph[current]:
            stack.append(neighbour)
          visited.add(current)

          count += 1  
    max_count = max(max_count, count)

  return max_count