"""
The size of the tree is the total number of nodes in a tree. 
You are required to return the size of a binary tree given the root node of the tree.
"""
# Iterative approach
def size_tree(self, start):
	count = 0
	if start is None:
		return count

	queue = Queue()
	queue.enqueue(node)

	while len(queue) > 0:
		count += 1
		node = queue.dequeue()

		if node.left:
			queue.enqueue(node.left)
		if node.right:
			queue.enqueue(node.right)

	return count



	
