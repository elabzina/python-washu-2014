#This is a straight-forward implementaion of the task
import helper
from collections import defaultdict
		
class FinInstument(object):

    def __init__(self, name, type):
		self.name = name
		self.type = type
		self.amount = 0

    def getName(self):
        return self.name

    def getType(self):
        return self.type

	def buy(x):
		return True
	
	def sell(x):
		return True
		
	def out(self):
		print self
	
	def validate(x):
		return True
		
	
    def __str__(self):
        return "%s %s" % (self.amount, self.name)
		
		
class Stock(FinInstument):

	def __init__(self, name, price):
		FinInstument.__init__(self, name, "Stock")
		self.price = price
			
	def validate(x, cash):
		check=globalValidate(x)
		if (not check): return False
		if (not is_integer(x)):
			print "The input is not an interger"
			return False
		if x*self.price < cash:
			print "Not enough money to purchase this amount"
			return False
			
	def buy(x, cash):
		if (not self.validate(x,cash)): return 0
		self.amount+= x
		#self.price is random
		return (cash - self.price*x)
		
	def sell(x):
		if (x > self.amount):
			print "Not have enough stocks of this type"
			return 0
		self.amount-=x
		#self price is random
		return x*self.price
   
class FinCollection(object):

	def __init__(self, type):
		self.type = type
		#self.pile = defaultdict(list)
		self.pile = list()
		
	def __str__(self):
		for key in self.pile.items(): print self.pile[key]
	
	def add(self, fin):
		self.pile.append(fin)
		
	
class MutualFond(FinInstument):

	def __init__(self,name):
		FinInstument.__init__(self,name,"MutualFond")
		
	
	
	
k = Stock("Jgjhgj",978)
l = Stock("kjhj",98)
t = FinCollection("Stock")
t.add(k)
t.add(l)


print k
print l
print t

		



		