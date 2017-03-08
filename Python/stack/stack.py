# Stacks are thought of like a stack of paper
# First in is last out
# LIFO -> Last In, First Out

class Stack:
	def __init__(self):
		self.items = []
	
	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		ret = self.items[-1]
		self.items = self.items[:-1]
		return ret
	
	def size(self):
		return len(self.items)
	
	def dump(self):
		self.items = []
	
	def view(self):
		print self.items
	
