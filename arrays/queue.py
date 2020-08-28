"""
Implementation of Queue 
"""
class Queue(object):
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		if not self.is_empty():
			return self.items.pop()

	def add(self, item):
		self.items.append(item)

	def is_empty(self):
		return len(self.items) == 0

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def __len__(self):
		return self._size()

	def _size(self):
		return len(self.items)

	def print_items(self):
		for i in self.items:
			print(i)


x = Queue()
x.enqueue(1)
x.add(2)
x.add(3)
x.add(4)
x.print_items()

