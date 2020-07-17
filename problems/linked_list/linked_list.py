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

	# Count the number of occurances of nodes in the linked list 
	def count_occurances(self):
		check_items = {}
		current = self.head 

		while current:
			if current.head in check_items:
				check_items[current.head] += 1
				current = current.next
			else:
				check_items[current.head] = 1
				current = current.next

	# Count occurance of a specific node value in a linked list (iterative approach) 
	def count_occurance_by_node_iterative(self, val):
		count = 0
		current = self.head 

		while current:
			if current.data == val:
				count += 1
			current = current.next 
		return count 

	# Count occurance of a specific node value in a linked list (recursive approach)
	def count_occurance_by_node_recursive(self, val, node):
		if not node:
			return 0
		if node.data == val:
			return 1 + self.count_occurance_by_node_recursive(val, node.next)
		else:
			return self.count_occurance_by_node_recursive(val, node.next)

	# Rotate the nodes of the linked list k times from the right 
	def rotate(self, k):
		# Rotate only if we have more than 1 element 
		if self.head and self.head.next:
			p = self.head 
			q = self.head 
			current = self.head 
			count = 0
			previous = None 

			while current:
				count += 1
				current = current.next 
			if count > 0:
				k %= count

			while p and count >= k + 1:
				previous = p 
				p = p.next 
				q = q.next 
				count -= 1
			p = previous 

			while q:
				previous = q 
				q = q.next 
			q = previous 

			q.next = self.head 
			self.head = p.next 
			p.next = None 

	# Check if the linked list is a palindrome

	##########################################
	# USING STRING
	##########################################
	def check_palindrome_string(self):
		s = ""
		current = self.head 
		while current:
			s += str(current.data)
			current = current.next 
		# print(s)
		return s == s[::-1]

	##########################################
	# USING STACKS
	##########################################
	def check_palindrome_stack(self):
		stack = []
		current = self.head 

		# Add values to the stack 
		while current:
			stack.append(current.data)
			current = current.next
		current = self.head
		# Loop again and check if the values are same 
		while current:
			data = stack.pop()
			print(data, current.data)
			if data != current.data:
				return False 
			current = current.next 
		return True

	##########################################
	# USING TWO POINTERS
	##########################################
	def check_palindrome_two_pointers(self):
		if self.head:
			p = self.head 
			q = self.head 
			stack = []
			i = 0
			while p:
				stack.append(p)
				p = p.next 
				i += 1

			count = 1
			while count <= i//2 + 1:
				if stack[-count].data != q.data:
					return False 
				q = q.next 
				count += 1
			return True 
		else:
			return True


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(4)
llist.append(4)
llist.append(2)
llist.append(1)
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
# print('\n')
# llist.swap_nodes('A', 'x')
# llist.print_list()

# print(llist_2.count_occurences_iterative(1))
# print(llist_2.count_occurences_recursive(llist_2.head, 1))
# print('\n\n')
# llist.rotate(21)
# llist.print_list()
print(llist.check_palindrome_two_pointers())

