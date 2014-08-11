from definitions import *

class FinInstrument(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type 
        self.amount = 0

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def buy(self, x,cash):
        return True
    
    def sell(self, x):
        return True

    def out(self):
        print self

    def validate(x):
        return True
    
    def __str__(self):
        return "%s %s" % (self.amount, self.name)


class Stock(FinInstrument):

	def __init__(self, name, price):
		FinInstrument.__init__(self, name, "Stock")
		self.price = price
			
	def validate(self, x, cash):
		check=globalValidate(x)
		if (not check): return False
		if (not isinstance(x, int)):
			print "The input is not an interger"
			return False
		if x*self.price > cash:
			print "Not enough cash to purchase this amount"
			return False
		return True
			
	def buy(self, x, cash):
		if (not self.validate(x,cash)): return 0
		self.amount+= x
		#self.price is randomreturn(cash - self.price*x)
		return (cash - x*self.price)

	def sell(self, x):
		if (x > self.amount):
			print "Not have enough stocks of this type"
			return 0
		self.amount-=x
		#self price is random
		return x*self.price*(0.5+random.random())

class MutualFond(FinInstrument):

	def __init__(self, name):
		FinInstrument.__init__(self, name, "Stock")
		self.price = 1
			
	def validate(self, x, cash):
		check=globalValidate(x)
		if (not check): return False
		if (x>100):
			print "The input is not a share"
			return False
		if x*self.price > cash:
			print "Not enough cash to purchase this amount"
			return False
		return True
			
	def buy(self, x, cash):
		if (not self.validate(x,cash)): return 0
		self.amount+= x
		#self.price is randomreturn(cash - self.price*x)
		return (cash - x*self.price)

	def sell(self, x):
		if (x > self.amount):
			print "Not have enough stocks of this type"
			return 0
		self.amount-=x
		#self price is random
		return x*self.price*(0.9 + random.random()*0.3)


class FinList(object):

    def __init__(self, type):
        self.type=type
        self.db =[]

    def __str__(self):
        for i in range(0,self.db.count()): print self.db[i]
   
        
         

