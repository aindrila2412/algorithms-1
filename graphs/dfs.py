# Implementation of Breadth First search

"""
    Using a stack

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
    starting_node = "A"
    => ['A', 'B', 'D', 'G', 'E', 'F', 'C']
"""
def dfs(graph, visited, starting_node):
    if starting_node not in visited:
        visited.append(starting_node)
        stack.append(starting_node)
        while(len(stack) != 0):
            stack.pop()
            for i in graph[starting_node]:
                dfs(graph, visited, i)

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

# Create an empty stack for keeping a check
stack = list()

dfs(graph, visited, 'A')
print(visited)
