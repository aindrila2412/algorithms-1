'''
	Implementation of Doubly Linked List

	Methods includes:
		- Initialise the doubly linked list 
		- Append to the list 
		- Prepend to the list 
		- Print the doubly linked list 
		- Add node after a node in the middle of the linked list 
		- Add node before a node in the middle of the linked list 
		- Delete a node
			- Deleting the only node present 
			- Deleting the head node 
			- Deleting the last node 
			- Deleting a middle node 
		- Reverse the doubly linked list 
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

	# Add node after a node in the middle of the doubly linked list 
	def add_after_node(self, key, data):
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

	# Add node before a node in the middle of a doubly linked list
	def add_before_node(self, key, data):
		current = self.head 
		while current:
			if current.next is None and current.data == key:
				self.prepend(data)
				return
			elif current.data == key:
				new_node = Node(data)
				temp_prev = current.prev
				temp_prev.next = new_node 
				current.prev = new_node 
				new_node.next = current 
				new_node.prev = temp_prev
				return
			
			current = current.next 

	# Delete a node from the lis t
	def delete_node(self, key):
		current = self.head 
		while current:
			
			if current.data == key and current == self.head:
				# Deleting the only node in the list
				if not current.next:
					current = None 
					self.head = None 
					return

				# Deleting the head node of the list 
				else:
					temp_next = current.next 
					temp_next.prev = None 
					current.next = None 
					current = None
					self.head = temp_next
					return  

			# Remove the middle node from the doubly linked list 
			elif current.data == key:
				if current.next:
					prev_temp = current.prev
					next_temp = current.next
					prev_temp.next = next_temp
					next_temp.prev = prev_temp
					current.prev = None 
					current.next = None 
					current = None 
					return

				# Removing the last node from the doubly linked list 
				else: 	
					prev_temp = current.prev 
					prev_temp.next = None 
					current.prev = None 
					current = None 
					return
			current = current.next 

	# Reverse the doubly linked list 
	def reverse(self):
		current = self.head
		temp = None 
		while current:
			temp = current.prev 
			current.prev = current.next 
			current.next = temp 
			current = current.prev  
		if temp:
			self.head = temp.prev 



doubleList = DoublyLinkedList()
doubleList.append(0)
doubleList.append(1)
doubleList.append(2)
doubleList.append(3)
# doubleList.prepend(2)
# doubleList.prepend(3)
# doubleList.print_list()
# print("\n")
# doubleList.add_after_node(2, 6)
# doubleList.print_list()
# doubleList.add_before_node(2, 6)
# doubleList.print_list()
# doubleList.delete_node(3)
doubleList.print_list()
doubleList.reverse()
print('\n')
doubleList.print_list()


