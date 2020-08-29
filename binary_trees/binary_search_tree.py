# Binary Search Tree (BST)

"""
	- Implementation of BST
	- Insertion of node
	- Traversing BST using pre order traversal
	- Searching in BST

"""
class Node(object):
	def __init__(self, data):
		self.data = data 
		self.left = None
		self.right = None


class BST(object):
	def __init__(self, root):
		self.root = Node(root)

	# Insertion of node in a Binary Search tree
	def insert_node(self, val):
		self.insert_helper(self.root, val)

	def insert_helper(self, current, val):
		if current.data < val:
			if current.right:
				self.insert_helper(current.right, val)
			else:
				current.right = Node(val)
		else:
			if current.left:
				self.insert_helper(current.left, val)
			else:
				current.left = Node(val)

	# Traversing the BST 
	def traverse(self, start, traversal):
		""" Pre order traversal """
		if start:
			traversal += (str(start.data) + "-")
			traversal = self.traverse(start.left, traversal)
			traversal = self.traverse(start.right, traversal)
		return traversal

	# Searching in BST
	def search_BST(self, val):
		return self.search_BST_helper(self.root, val)

	def search_BST_helper(self, current, val):
		if current:
			if current.data == val:
				return True
			elif current.data < val:
				return self.search_BST_helper(current.right, val)
			else:
				return self.search_BST_helper(current.left, val)
		return False






tree = BST(8)
tree.root.left = Node(3)
tree.root.right = Node(10)
tree.root.left.left = Node(1)
tree.root.left.right = Node(6)

tree.insert_node(9)
print(tree.traverse(tree.root, ""))
print(tree.search_BST(12))
