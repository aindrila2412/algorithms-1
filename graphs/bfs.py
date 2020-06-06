# Implementation of Breadth First search

"""
    Using a queue

    ---------
    Parameters
    ---------
    An adjacency list

    ---------
    Returns
    ---------
    The traversed graph from the starting node

    ---------
    Time Complexity
    ---------
    O(V+E)

    ---------
    Test Cases
    ---------
    starting_node = "B"
    => ['B', 'D', 'E', 'G', 'F', 'A', 'C']
"""
def bfs(graph, visited, starting_node):
    visited.append(starting_node)
    queue.append(starting_node)

    while(len(queue) != 0):
        element = queue.pop(0)
        for i in graph[element]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    print(visited)

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : ['G'],
  'E' : ['F'],
  'F' : [],
  'G': ['A']
}

# Create an empty list to mark the visited nodes
visited = list()

# Create an empty queue
queue = list()

bfs(graph, visited, 'B')
