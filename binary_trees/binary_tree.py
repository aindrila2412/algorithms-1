# Binary Tree in Python 

"""
	- Implementation of a binary tree
	- Traversal of Binary Tree
		> In-order
		> Pre-order
		> Post-order
	-
"""

class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None 
		self.right = None 

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





tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))


