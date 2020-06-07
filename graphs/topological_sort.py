# Implementation of Topological Sort using DFS

"""
    Using a stack and set

    ---------
    Parameters
    ---------
    An adjacency list

    ---------
    Returns
    ---------
    Topological order of the traversed graph

    ---------
    Time Complexity
    ---------
    O(V+E)

    ---------
    Test Cases
    ---------
    => Topological Order:  ['F', 'E', 'C', 'D', 'B', 'A']
"""

def topological_sort(graph):
    def dfs(graph, explored, starting_node, stack):
        # global stack
        explored.add(starting_node)
        for i in graph[starting_node]:
            if i not in explored:
                dfs(graph, explored, i, stack)
        stack.append(starting_node)

    explored = set()
    stack = list()
    for i in graph:
        if i not in explored:
            dfs(graph, explored, i, stack)
    print("Topological Order: ", stack[:: -1])

graph = {
 'A' : [],
 'B' : [],
 'C' : ['D'],
 'D' : ['B'],
 'E' : ['A', 'B'],
 'F' : ['C', 'A']
}

topological_sort(graph)
