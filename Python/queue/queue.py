# Queues are more like a line at a grocery store
# It's fair as in first one in, first one out
# Aka FIFO

class Queue:
	def __init__(self):
		self.items = []
		
	def empty(self):
		return len(self.items) == 0
		
	def size(self):
		return len(self.items)

	def front(self):
		return self.items[0]

	def back(self):
		return self.items[-1]

	def push(self, item):
		self.items.append(item)

	def pop(self):
		ret = self.items[0]
		self.items = self.items[1:]
		return ret

	def view(self):
		print self.items
		
