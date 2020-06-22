# Implementation of Dijkstra Algorithm  


"""
    Using a queue

    ---------
    Parameters
    ---------
    An object of vertices and edges and their respective weights

    ---------
    Returns
    ---------
    Shortest distances to all the nodes from the initial node (s)

    ---------
    Time Complexity
    ---------
    O(V+E) as we are doing a BFS

    ---------
    Test Cases
    ---------
    # Graph = {'U': {'X': 1, 'W': 5, 'V': 2}, 'W': {'Y': 1, 'X': 3, 'Z': 5, 'U': 5, 'V': 3}, 'V': {'X': 2, 'U': 2, 'W': 3}, 'Y': {'X': 1, 'Z': 1, 'W': 1}, 'X': {'Y': 1, 'U': 1, 'W': 3, 'V': 2}, 'Z': {'Y': 1, 'W': 5}}
    # Starting Node: 'X'
    => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}
"""
def dijkstra(graph, visited, queue, values, starting_node):
	# Set initial node as 0 and rest of the node as infinity
	for i in graph:
		if i == starting_node:
			values[i] = 0
		else:
			values[i] = float('inf')

	visited.append(starting_node)
	queue.append(starting_node)

	while(len(queue) != 0):
		element = queue.pop(0)
		print(element)
		for i in graph[element]:
			# print(graph[element][i])
			if values[element] + graph[element][i] < values[i]:
				values[i] = values[element] + graph[element][i]
			if i not in visited:
				visited.append(i)
				queue.append(i)

# graph = {
#     'U': {'V': 2, 'W': 5, 'X': 1},
#     'V': {'U': 2, 'X': 2, 'W': 3},
#     'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
#     'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
#     'Y': {'X': 1, 'W': 1, 'Z': 1},
#     'Z': {'W': 5, 'Y': 1},
# }
graph = {
	'start': {'A': 5, 'B': 2},
    'A': {'start': 1, 'C': 4, 'D': 2},
    'B': {'A': 8, 'D': 7},
    'C': {'D': 6, 'finish': 3},
    'D': {'finish': 1},
    'finish': {}
}

visited = []
queue = []

# Dictionary to keep the distances to all the nodes
values = {}

starting_node = str(input())

dijkstra(graph, visited, queue, values, starting_node)
print(values)