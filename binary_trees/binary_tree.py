# Binary Tree in Python 

"""
	- Implementation of a binary tree
	- Traversal of Binary Tree
		> In-order
		> Pre-order
		> Post-order
	- Level Order traversal
	- Reverse Level order traversal
	- Height of a tree

"""

class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None 
		self.right = None 

"""
Implementation of Queue 
"""
class Queue(object):
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		if not self.is_empty():
			return self.items.pop()

	def add(self, item):
		self.items.append(item)

	def is_empty(self):
		return len(self.items) == 0

	def peek(self):
		if not self.is_empty():
			return self.items[-1].value

	def __len__(self):
		return self._size()

	def _size(self):
		return len(self.items)

	def print_items(self):
		for i in self.items:
			print(i)

""" Binary Tree """

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self, ttype):
		if ttype == "preorder":
			return self.preorder_traversal(tree.root, "")
		if ttype == "inorder":
			return self.inorder_traversal(tree.root, "")
		if ttype == "postorder":
			return self.postorder_traversal(tree.root, "")
		if ttype == "levelorder":
			return self.level_order_traversal(tree.root)
		if ttype == "reverse_levelorder_traversal":
			return self.reverse_levelorder_traversal(tree.root)

	# Pre-order traversal
	def preorder_traversal(self, start, traversal):
		""" Root -> Left -> Right """
		if start:
			traversal += (str(start.value) + '-')
			traversal = self.preorder_traversal(start.left, traversal)
			traversal = self.preorder_traversal(start.right, traversal)
		return traversal

	# In-order traversal 
	def inorder_traversal(self, start, traversal):
		""" Left -> Root -> Right """
		if start:
			traversal = self.inorder_traversal(start.left, traversal)
			traversal += (str(start.value) + '-')
			traversal = self.inorder_traversal(start.right, traversal)
		return traversal

	# Post-order traversal 
	def postorder_traversal(self, start, traversal):
		""" Left -> Right -> Root """
		if start:
			traversal = self.postorder_traversal(start.left, traversal)
			traversal = self.postorder_traversal(start.right, traversal)
			traversal += (str(start.value) + '-')
		return traversal

	# Level Order Traversal of Binary Tree

	""" Implementing the Level order traversal """
	def level_order_traversal(self, start):
		""" Left node first then right node """
		if start is None:
			return 

		queue = Queue()
		queue.enqueue(start)
		traversal = ""

		while len(queue) > 0:
			traversal += (str(queue.peek()) + "-")

			node = queue.dequeue()
			if node.left:
				queue.enqueue(node.left)
			if node.right:
				queue.enqueue(node.right)
		return traversal

	""" Implementing the reverse Level order traversal """
	def reverse_levelorder_traversal(self, start):
		""" Rigt node first then left node """
		if start is None:
			return
		queue = Queue()
		stack = list()
		traversal = ""
		queue.enqueue(start)

		while len(queue) > 0:
			node = queue.dequeue()
			stack.append(node)

			if node.right:
				queue.enqueue(node.right)
			if node.left:
				queue.enqueue(node.left)
		while len(stack) > 0:
			node = stack.pop().value
			traversal += (str(node) + "-")
		return traversal


	# Calculating the height of the binary tree 
	def height_tree(self, node):
		if node is None:
			return -1 
		left_node_height = self.height_tree(node.left)
		right_node_height = self.height_tree(node.right)

		return 1 + max(left_node_height, right_node_height)




tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)


print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))
print(tree.print_tree('levelorder'))
print(tree.print_tree('reverse_levelorder_traversal'))
print(tree.height_tree(tree.root))



