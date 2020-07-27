'''
	Implementation of Doubly Linked List

	Methods includes:
		- Initialise the doubly linked list 
		- Append to the list 
		- Prepend to the list 
		- Print the doubly linked list 
		- Add nodes in the middle of the linked list 

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
			while current.next:
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
			print(current.data)
			current = current.next 

	# Add node to the middle of the doubly linked list 
	def add_to_middle(self, key, data):
		current = self.head
		while current:
			if current.next is None and current.data == key:
				self.append(data)
				return 
			elif current.data == key:
				new_node = Node(data)
				temp_next = current.next
				current.next = new_node
				new_node.next = temp_next  
				new_node.prev = current
				temp_next.prev = new_node
				return

			current = current.next 
				

doubleList = DoublyLinkedList()
doubleList.append(0)
doubleList.append(1)
doubleList.prepend(2)
doubleList.prepend(3)
doubleList.print_list()
print("\n")
doubleList.add_to_middle(2, 6)
doubleList.print_list()

