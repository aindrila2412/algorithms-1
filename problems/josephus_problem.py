# An implementation of Josephus Problem

def remove_josephus_node(self, node):
	if self.head:
		# If the node is the head node
		if self.head == node:
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
				if current == node:
					previous.next = current.next 
					current = current.next

def josephus_circle(self, step):
	current = self.head 

	while self.circular_length() > 1:
		count = 1 
		while count != step:
			current = current.next 
			count += 1
		print('KILL: ' + str(current.data))
		self.remove_josephus_node(current)
		current = current.next



