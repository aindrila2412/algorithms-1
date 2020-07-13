# Implementation of stack data structure

class Stack():
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def is_empty(self):
		return self.items == []

	def peek(self):
		if not self.is_empty():
			return self.items[-1]

	def get_items(self):
		return self.items

stack = Stack()
stack.push('A')
stack.push('B')
print(stack.get_items())
print(stack.peek())


