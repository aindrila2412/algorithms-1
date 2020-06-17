# Implementation of Strongly Connected components in a directed graph

"""
    Using a stacks and lists

    ---------
    Parameters
    ---------
    An adjacency list

    ---------
    Returns
    ---------
    Lists containting strongly connected components

    ---------
    Time Complexity
    ---------
    O(V+E)

    ---------
    Test Cases
    ---------
    Input: {'A': ['B'], 'B': ['C', 'D'], 'C': ['A'], 'D': ['E'], 'E': ['F'], 'F': ['D', 'G'], 'G': ['H'], 'H': ['I'], 'I': ['J'], 'J': ['G', 'K'], 'K': []}
    => SCC :  [['B', 'C', 'A'], ['E', 'F', 'D'], ['H', 'I', 'J', 'G'], ['K']]

"""
def reverse_graph(graph):
	check_array = []
	transpose_graph = {}
	for i in graph:
		check_array.append(i)
		transpose_graph[i] = []

	# for i in check_array:
	# 	for j in range(0, len(check_array), 1):
	# 		for k in graph[check_array[j]]:
	# 			if k == i:
	# 				transpose_graph[i].append(check_array[j])
	
	for i in range(0, len(check_array), 1):
		for j in graph[check_array[i]]:
			transpose_graph[j].append(check_array[i]) 

	return transpose_graph

# Performing DFS on the initial graph and returning the topological sorted stack
def dfs(graph, starting_node, visited):
	if starting_node not in visited:
		visited.append(starting_node)
		stack.append(starting_node)
		while (len(stack) != 0):
			stack.pop()
			for i in graph[starting_node]:
				dfs(graph, i, visited)
		visited_stack.append(starting_node)

# Performing DFS on the reversed list and returning the strongly connected components
def dfs_second(graph, starting_node, new_visited, check):
	if starting_node not in new_visited:
		new_visited.append(starting_node)
		for i in graph[starting_node]:
			dfs_second(graph, i, new_visited, check)
		check.append(starting_node)
	if len(check) != 0:
		new_visited_stack.append(check)

# Finding strongly connected components by performing DFS twice
def strongly_connected_components(graph, starting_node):
	# DFS on the initial graph
	visited = list()
	dfs(graph, starting_node, visited)

	# Reverse the ordering of the graph
	transpose_graph = reverse_graph(graph)

	# DFS on the reverse graph
	new_visited = list()
	while visited_stack:
		popped = visited_stack.pop()
		# print(popped)
		check = []
		dfs_second(transpose_graph, popped, new_visited, check = [])
	final_list = []

	# Remove empty array from the final array
	for element in new_visited_stack:
		if element not in final_list:
			final_list.append(element)
	# return final set of list of strongly connected components
	return final_list

# graph = {
# 	'A' : ['B'],
# 	'B' : ['C'],
# 	'C' : ['D', 'E'],
# 	'D' : ['A'],
# 	'E' : ['F'],
# 	'F' : ['G'],
# 	'G' : ['E', 'H'],
# 	'H' : []
# }


graph = {
 'A' : ['B'],
 'B' : ['C', 'D'],
 'C' : ['A'],
 'D' : ['E'],
 'E' : ['F'],
 'F' : ['D', 'G'],
 'G' : ['H'],
 'H' : ['I'],
 'I' : ['J'],
 'J' : ['G', 'K'],
 'K' : []
}

# Create an empty stack for keeping a check
stack = list()
visited_stack = list()
new_visited_stack = list()
# check = []

final = strongly_connected_components(graph, "A")
print(final)
