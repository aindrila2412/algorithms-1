# Binary Search Tree (BST)

"""
	- Implementation of BST
	- Insertion of node
	- Traversing BST using pre order traversal
	- Searching in BST
	- Checking the BST property holds

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
		if self.root is None:
			self.root = Node(val)
		else:
			self.insert_helper(self.root, val)

	def insert_helper(self, current, val):
		if current.data < val:
			if current.right:
				self.insert_helper(current.right, val)
			else:
				current.right = Node(val)
		elif current.data > val:
			if current.left:
				self.insert_helper(current.left, val)
			else:
				current.left = Node(val)
		else:
			print('Value already exists!!')

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
		if self.root:
			found = self.search_BST_helper(self.root, val)

			if found:
				return True
			else:
				return False

	def search_BST_helper(self, current, val):
		if current:
			if current.data == val:
				return True
			elif current.data < val:
				return self.search_BST_helper(current.right, val)
			else:
				return self.search_BST_helper(current.left, val)
		return False

	# Check if the BST holds true
	def check(self):
		def helper(node, lower=float('-inf'), upper=float('inf')):
			if not node:
				return True 

			val = node.data 

			if val <= lower or val >= upper:
				return False

			# val is passed as lower, because all the children in the right subtree
			# should be greater than that
			if not helper(node.right, val, upper):
				return False 
			# val is passed as upper, because all the children in the left subtree
			# should be smaller than that
			if not helper(node.left, lower, val):
				return False 

			return True
			
		return helper(self.root)


tree = BST(8)
tree.root.left = Node(3)
tree.root.right = Node(10)
tree.root.left.left = Node(1)
tree.root.left.right = Node(6)

tree.insert_node(9)
print(tree.traverse(tree.root, ""))
print(tree.search_BST(12))
print(tree.check())
