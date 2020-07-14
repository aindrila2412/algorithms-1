'''
	- Creating a Linked list
	- Appening to the linked list (begin, end, middle)
	- Deleting from a linked list (begin, middle) (value, position)
	- Counting the number of nodes
	- Reversing the nodes (iterative and recursive)
	- Print the linked list
'''


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# Prints all the elements of a linked list
	def print_list(self):
		current_node = self.head 
		while current_node:
			print(current_node.data)
			current_node = current_node.next

	# Add a node to the beginning of the linked list
	def prepend(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	# Add a node in the middle of the linked list 
	def insert_after_node(self, prev_node, data):
		if not prev_node:
			print('Previous node does not exists!')
			return
		new_node = Node(data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	# Adding to the end of the linked list
	def append(self, data):
		new_node = Node(data)
		# Check if the linked list is empty 
		if self.head is None:
			self.head = new_node
			return

		last_node = self.head
		while last_node.next:
			last_node = last_node.next
		last_node.next = new_node

	# Deleting the node 
	def delete_node(self, key):
		# Delete the head node 
		current_node = self.head 
		if current_node and current_node.data == key:
			self.head = current_node.next 
			current_node = None
			return 
		# Delete the other nodes 
		previous = None 
		while current_node and current_node.data != key:
			previous = current_node
			current_node = current_node.next 

		if current_node is None:
			return 
		previous.next = current_node.next
		current_node = None

	# Delete node using position 
	def delete_node_position(self, pos):
		if self.head:
			current_node = self.head 
			# Check if the position is 0
			if pos == 0:
				self.head = current_node.next
				current_node = None
				return 
			# If the position is not the first element
			previous = None 
			counter = 0
			while current_node and counter != pos:
				previous = current_node
				current_node = current_node.next 
				counter += 1

			if current_node is None:
				return 

			previous.next = current_node.next
			current_node = None

	# Count the number of nodes in the linked list using iterative approach
	def count_nodes_iterative(self):
		count = 0
		current_node = self.head 
		while current_node:
			count += 1
			current_node = current_node.next
		return count

	# Count the number of nodes using recursive approach 
	def count_nodes_recursion(self, node):
		if node is None:
			return 0
		return 1 + self.count_nodes_recursion(node.next)

	# Swap 2 nodes in a linked list
	def swap_nodes(self, key_one, key_two):
		if key_one == key_two:
			return 
		previous_one = None 
		current_one = self.head 

		while current_one and current_one.data != key_one:
			previous_one = current_one
			current_one = current_one.next 

		previous_two = None 
		current_two = self.head

		while current_two and current_two.data != key_two:
			previous_two = current_two
			current_two = current_two.next 

		if not previous_one or not previous_two:
			return 

		if previous_one:
			previous_one.next = current_two
		else: 
			self.head = current_two

		if previous_two:
			previous_two.next = current_one
		else:
			self.head = current_one

		# Swap the two nodes 
		current_one.next, current_two.next = current_two.next, current_one.next

	# Reverse a linked list using iterative approach 
	def reverse_nodes(self):
		previous = None 
		current = self.head 

		while current:
			nxt = current.next 
			current.next = prev 
			prev = current
			current = nxt 
		self.head = prev 

	# Reverse a linked list using recursive approach 
	def reverse_nodes_recursive(self):
		def _reverse_nodes_recursive(current, previous):
			if not current:
				return previous 
			nxt = current.next 
			current.next = previous
			previous = current
			current = nxt
			return(_reverse_nodes_recursive(current, prev))
		self.head = _reverse_nodes_recursive(current = self.head, previous = None)

	# Merge two sorted linked lists 
	def merge_nodes(self, llist):
		p = self.head 
		q = llist.head
		s = None 

		if not p:
			return q
		if not q:
			return p 

		if p and q:
			if p.data <= q.data:
				s = p
				p = s.next
			else:
				s = q 
				q = s.next 
			new_head = s 
		while p and q:
			if p.data <= q.data:
				s.next = p 
				s = p 
				p = s.next 
			else:
				s.next = q
				s = q 
				q = s.next 
		if not p:
			s.next = q
		if not q:
			s.next = p 
		return new_head

	# Merge two sorted linked lists using divide and conquer 
	def merge_nodes_divide_and_conquer(self, llist):
		p = self.head 
		q = llist.head 
		s = None 

		if not p:
			return q 
		if not q:
			return p

		while p and q:
			if p.data <= q.data:
				p.next = self.merge_nodes_divide_and_conquer(p.next, q)
				return p 
			else:
				q.next = self.merge_nodes_divide_and_conquer(p, q.next)
				return q 

	# Remove duplicates from a linked list 
	def remove_duplicates(self):
		current = self.head 
		previous = None 
		check_items = {}

		while current:
			if current.data in check_items:
				previous.next = current.next 
				current = None 
			else:
				check_items[current.data] = 1
				previous = current 
			current = previous.next

	# Get the N-th element from the end of the linked list 
	# Method 1
	def get_nth_last_node(self, nth):
		count = self.count_nodes_iterative()
		current = self.head 
		while current:
			if count == nth:
				print(current.data)
				return current.data 
			count -= 1
			current = current.next 
		if current is None:
			return 

	# Method 2
	def get_nth_node_without_count(self, nth):
		p = self.head 
		q = self.head 
		count = 0
		while q:
			count += 1
			if count >= nth:
				break 
			q = q.next 

		if not q:
			print(str(nth) + "is greater than the number of nodes in the list")
		while p and q.next:
			q = q.next 
			p = p.next 
		return p.data



	


llist = LinkedList()
llist.append('T')
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('x')
llist.append('ahah')
llist.print_list()
# print('\n')
# llist.prepend('J')
# llist.print_list()
# print('\n')
# llist.insert_after_node(llist.head.next, "L")
# llist.print_list()
# print('\n')
# llist.delete_node('C')
# llist.print_list()
# llist.delete_node_position(3)
# llist.print_list()
# print('\n')
# print(llist.count_nodes_iterative())

# print ('\n')
# print(llist.count_nodes_recursion(llist.head))
print('\n')
llist.swap_nodes('A', 'x')
llist.print_list()
