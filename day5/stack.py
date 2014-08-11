class Queue():
	def __init__(self, x=None):
		self.d=list()
		if (x): self.d.append(x)
		
	def __str__(self):
		return str(self.d)

	def enqueue(self,x):
		self.d.append(x)
	
	def dequeue(self):
		return (self.d.pop())
		

class Stack():
	def __init__(self, x=None):
		self.d=list()
		if (x): self.d.append(x)
		
	def __str__(self):
		return str(self.d)

	def push(self,x):
		self.d.append(x)
	
	def pop(self):
		return (self.d.pop(0))	
		
x  = Queue()
x.enqueue(1)
x.enqueue(3)
x.enqueue(2)
x.enqueue(34)

print x
print x.dequeue()
print x

print 'kjsehfksjfhksjfhks'

x  = Stack()
x.push(1)
x.push(3)
x.push(2)
x.push(34)

print x
print x.pop()
print x

print x.pop()
print x













	
		