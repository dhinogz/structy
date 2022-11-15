def connected_components_count_recursive(graph):
    visited = set()

    count = 0
    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1
    return count
    

def explore(graph, current, visited):
  
    if current in visited:
        return False
      
    visited.add(current)
    
    for neighbour in graph[current]:
        explore(graph, neighbour, visited)
        
    return True


def connected_components_count(graph):
  
    visited = set()
    count = 0
  
    for node in graph:
        if node not in visited:
            stack = [node]
        
            while stack:
                current = stack.pop()
                if current not in visited:
                    for neighbour in graph[current]:
                        stack.append(neighbour)
                    visited.add(current)
            
            count += 1  
      
    return count
        



print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}))