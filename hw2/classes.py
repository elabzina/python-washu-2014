import random
from functions import *
  
class FinInstrument(object):

#initialization of the common fields of all financial instruments
    def __init__(self, name, type):
        self.name = name
        self.type = type 
        self.amount = 0

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def buy(self, x,cash):
        return 0
    
    def sell(self, x):
        return 0

    def validate(x):
        return True
    
    def __str__(self):
        return "%s %s" % (self.amount, self.name)

    def getType(self):
        return self.type


class Stock(FinInstrument):

	def __init__(self, price,name):
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
		return (x*self.price)

	def sell(self, x):
		if (x > self.amount):
			print "Not have enough stocks of this type"
			return 0
		self.amount-=x
		#self price is random
		return x*self.price*(0.5+random.random())

class MutualFond(FinInstrument):

	def __init__(self, name, price=1):
		FinInstrument.__init__(self, name, "mutual funds")
		self.price = price
			
	def validate(self, x, cash):
		check=globalValidate(x)
		if (not check): return False
		if (x>100 or ((x+self.amount)>100)):
			print "The input is not a share"
			return False
		if x*self.price > cash:
			print "Not enough cash to purchase this amount"
			return False
		return True
			
	def buy(self, x, cash):
		if (not self.validate(x,cash)): return 0
		self.amount= +x
		#self.price is randomreturn(cash - self.price*x)
		return (x*self.price)

	def sell(self, x):
		if (not globalValidate(x)): return 0
		if (x > 100):
			print "Not have enough stocks of this type"
			return 0
		self.amount-=x
		#self price is random
		return x*self.price*(0.9 + random.random()*0.3)

#Bond is for simplicity considered "the opposite" of stock

class Bond(FinInstrument):

	def __init__(self, price,name):
		FinInstrument.__init__(self, name, "bond")
		self.price = price

			
	def validate(self, x, cash):
		check=globalValidate(x)
		if (not check): return False
		if (not isinstance(x, int)):
			print "The input is not an interger"
			return False
		return True

	def buy(self, x, cash):
		if (not self.validate(x,cash)): return 0
		self.amount= +x
		#self.price is randomreturn(cash - self.price*x)
		return (-x*self.price)*(1 + random.random())

	def sell(self, x):
		if (not globalValidate(x)): return 0
		if (x>self.amount): return 0
		self.amount-=x
		#self price is random
		return -x*self.price

      
class FinList(object):

    def __init__(self,type):
        self.db =[]
        self.type=type

    def append(self,obj):
        self.db.append(obj)

    def __str__(self):
        st=self.type+": "
        if (len(self.db)==0): return st+"\t none\n"
        for i in range(0, len(self.db)): 
            if i>0: st+='\t'
            st+=  ('\t'+str(self.db[i]))
            if i<len(self.db): st+='\n'
        return st
    
    def getIndex(self,name):
        for i in range(0, len(self.db)): 
            if self.db[i].name==name: return i
        return -1

    #the function returns the expense of the deal, the relevant changes of the amount are side effects within class 
    def buy(self,obj,x,cash):
        index = self.getIndex(obj.name)
    #if there is already this type of the fininstument, the attempt is to change its anount
        if (index>-1): return self.db[index].buy(x,cash) 
    #if this a new fininstument
        obj1 = obj
        deal = obj1.buy(x,cash)
        if (deal>0): self.db.append(obj1)
        return deal

    def sell(self,name,x):
        index = self.getIndex(name)
        deal=0
        if (index>-1): 
            deal=self.db[index].sell(x)       
            if (self.db[index].amount==0):
                del self.db[index]
        return deal
       
class Portfolio():

    def __init__(self,cash=0):
        self.stocks = FinList("stocks")
        self.mf = FinList("mutual funds")
        self.cash=cash
            
    def addCash(self,cash):
        if (not globalValidate(cash)): return "Enter a correct amount!"
        self.cash+=cash
        writeLog("Cash added: " + str(round(cash,2)) + " residual: " + str(round(self.cash,2)))
           
    def withdrawCash(self,cash):
        if (not globalValidate(cash)): return "Enter a correct amount!"
        if (cash > self.cash): return "Not enough money to withdraw"
        self.cash-=cash
        if (cash>0): writeLog("Cash withdrawn: " + str(round(cash,2)) + " residual: " + str(round(self.cash,2)))
        
    def buyStock(self, amount, stock):
        change = self.stocks.buy(stock,amount,self.cash)
        self.cash-= change
        if (change>0):  writeLog("Stock bought: " + str(amount) + " " + stock.name + " for " + str(round(change,2)) + " residual: " + str(round(self.cash,2)))
              
    def sellStock(self, amount, name):
        change = self.stocks.sell(name, amount)
        self.cash+= change
        if (change>0):  writeLog("Stock sold: " + str(amount) + " " + name + " for " + str(round(change,2))  + " residual: " + str(round(self.cash,2)))
          
    def buyMutualFund(self, amount, mf):
        change = self.mf.buy(mf,amount,self.cash) 
        self.cash-= change
        if (change>0):  writeLog("Mutual funds bought: " + str(amount) + " " + mf.name + " for " + str(round(change,2)) + " residual: " + str(round(self.cash,2))) 
      
    def sellMutualFund(self, name, amount):
        change = self.mf.sell(name, amount)
        self.cash+= change
        if (change>0):  writeLog("Mutual funds sold: " + str(amount) + " " + name + " for " + str(round(change,2)) + " residual: " + str(round(self.cash,2))) 

    def __str__(self):
        return ("cash:\t \t" + str(round(self.cash,2)) +  '\n' + str(self.stocks) + str(self.mf) + '\n'+'\n') 

    def history(self):
        outLog()
      
      
  # this is a class to show the inheritance. Bonds are added         

class PortfolioBond(Portfolio):

    def __init__(self,cash=0):
        Portfolio.__init__(self, cash=0)
        self.bonds=FinList("bonds")
            
           
    def buyBond(self, amount, stock):
        change = self.bonds.buy(stock,amount,self.cash)
        self.cash-= change
        if (-change>0):  writeLog("Bonds bought: " + str(amount) + " " + stock.name + " for " + str(round(-change,2)) + " residual: " + str(round(self.cash,2)))
              
    def sellBond(self, amount, name):
        change = self.bonds.sell(name, amount)
        self.cash+= change
        if (-change>0):  writeLog("Bonds sold: " + str(amount) + " " + name + " for " + str(round(-change,2))  + " residual: " + str(round(self.cash,2)))
          
    
    def __str__(self):
        return ("cash:\t \t" + str(round(self.cash,2)) +  '\n' + str(self.stocks) + str(self.bonds) + str(self.mf)  + '\n'+'\n') 
    
   
      