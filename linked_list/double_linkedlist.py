'''
	Implementation of Doubly Linked List

	Methods includes:
		- Initialise the doubly linked list 
		- Append to the list 
		- Prepend to the list 
		- Print the doubly linked list 
'''
class Node:
	def __init__(self, data):
		self.data = data 
		self.next = None
		self.prev = None 

class DoublyLinkedList:
	def __init__(self):
		self.head = None 

	def append(self, data):
		# Check if the list is empty 
		if self.head is None:
			new_node = Node(data)
			new_node.prev = None 
			self.head = new_node 
		else:
			new_node = Node(data)
			current = self.head 
			while current:
				current = current.next 
			current.next = new_node
			new_node.prev = current 
			new_node.next = None 

	def prepend(self, data):
		# Check if the list is empty
		if self.head is None:
			new_node = Node(data)
			snew_node.prev = None 
			self.head = new_node
		else:
			new_node = Node(data)
			self.head.prev = new_node 
			new_node.next = self.head
			self.head = new_node 
			new_node.prev = None 

	def print_list(self):
		current = self.head 
		while current:
			print(current)
			current = current.next 

