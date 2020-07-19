'''
	Implementation of Circular Linked List

	Methods includes:
		- Create the circular linked list 
		- Append item to the list 
		- Prepend item to the list
		- Print out the entire list 
		- Remove nodes from the circular linked list 
		- Split the list into two halves
'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None 

class Circular_Linked_List:
	def __init__(self):
		self.head = None

	# Prepend items to the list
	def prepend(self, data):
		new_node = Node(data)
		current = self.head 
		new_node.next = self.head 

		if not self.head:
			new_node.next = new_node
		else:
			while current.next != self.head:
				current = current.next 
			current.next = new_node
		self.head = new_node

	# Append items to the list
	def append(self, data):
		# If the linked list is empty, add the node and make the second node as the first node (circular list)
		if not self.head:
			self.head = Node(data)
			self.head.next = self.head
		else:
			new_node = Node(data)
			current = self.head 
			# Check if the next is not the end 
			while current.next != self.head:
				current = curent.next 
			# Make the last element as the new node data 
			current.next = new_node
			# Point the last node to the head node
			new_node.next = self.head 

	# Print the entire list 
	def print_list(self):
		current = self.head 
		while current:
			print(current.data)
			current = current.next 
			if current == self.head:
				break

	# Removing node from the circular linked list with unique nodes 
	def remove_nodes(self, key):
		if self.head:
			# If the key is the head node data
			if self.head.data == key:
				current = self.head 
				while current.next != self.head:
					current = current.next 
				if self.head == self.head.next:
					self.head = None 
				else:
					current.next = self.head.next 
					self.head = self.head.next
			else:
				current = self.head 
				previous = None 
				while current.next != self.head:
					previous = current 
					current = current.next 
					if current.data == key:
						previous.next = current.next 
						current = current.next

	# Get the length of the circular linked list
	def circular_length(self):
		current = self.head 
		previous = None 
		count = 0
		while current:
			count += 1
			current = current.next 
			if current == self.head:
				break
		return count

	# Split the list into two halves 
	def split_list(self):
		current = self.head 
		list_size = self.circular_length()
		mid_size = list_size // 2
		counter = 0

		while current and counter < mid_size:
			previous = current 
			current = current.next 
			counter += 1

		previous.next = self.head 

		new_list = Circular_Linked_List()

		while current.next != self.head:
			new_list.append(current.data)
			current = current.next 
		new_list.append(current.data)
		self.print_list()
		print('\n')
		new_list.print_list()


cllist = Circular_Linked_List()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
# cllist.print_list()
# cllist.remove_nodes("A")
# cllist.print_list()
# print(cllist.circular_length())
cllist.split_list()