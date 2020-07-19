'''
	Implementation of Circular Linked List
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


cllist = Circular_Linked_List()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()
cllist.remove_nodes("A")
cllist.print_list()