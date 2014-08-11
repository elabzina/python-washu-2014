import finInstrument

class Stock(FinInstrument):

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
			print "Not enough cash to purchase this amount"
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
		

s= Stock("HGN",23)

print s
		

		
		