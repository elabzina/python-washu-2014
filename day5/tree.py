class Tree():
	def __init__(self,x=None):
		self.left = None
		self.right = None
		self.value = x
	
	def value(self,x):
		self.value = x
		
	def left(self,x):
		self.left = Tree(x)

	def right(self,x):
		self.right = Tree(x)
	
	
x=Tree(1)
x.left(2)
x.right(3)
x.value(8)