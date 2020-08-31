# Binary Search Tree (BST)

"""
	- Implementation of BST
	- Insertion of node
	- Traversing BST using pre order traversal
	- Searching in BST
	- Checking the BST property holds
	- Delete element from BST

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

	# Delete element from Binary Seach Tree
	def delete_node(self, target):
		def find_max(node):
			while node.right:
				node = node.right 
			return node.data

		def delete_node_helper(target, node):
			# If node is null 
			if node is not None:
				# If target is smaller than the node, move left 
				if target < node.data:
					node.left = delete_node_helper(target, node.left)
				elif target > node.data:
					node.right = delete_node_helper(target, node.right)
				else:
					# Node is found,
					# Check if the node has 2 children nodes 
					if node.left and node.right:
						# Replace current node with predecessor data (can also work around successor - right )
						node.data = find_max(node.left)
						node.left = delete_node_helper(node.data, node.left)

						# with successor 
						# node.data = find_max(node.right)
						# node.right = delete_node_helper(node.data, node.right)
					else:
						# If there is a single child node,
						# Return whichever present
						node = node.left or node.right

			return node

		delete_node_helper(target, self.root)


tree = BST(50)
tree.root.left = Node(40)
tree.root.right = Node(70)
tree.root.left.left = Node(20)
tree.root.left.right = Node(45)
tree.root.left.left.left = Node(10)
tree.root.left.left.right = Node(30)
tree.root.left.left.left.left = Node(5)
tree.root.left.left.left.right = Node(15)
tree.root.left.left.left.right.left = Node(7)
tree.root.left.left.left.right.right = Node(18)
tree.root.left.left.left.left.left = Node(3)
tree.root.left.left.left.left.right = Node(8)
tree.root.right.left = Node(60)
tree.root.right.right = Node(99)

# tree.insert_node(9)
print(tree.traverse(tree.root, ""))
# print(tree.search_BST(12))
# print(tree.check())
tree.delete_node(20)

print(tree.traverse(tree.root, ""))

