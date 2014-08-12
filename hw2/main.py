from classes import *
from functions import *
import random
from collections import defaultdict
import numbers
	

#the log is stored as a binary file in the working directory. If the user chooses Y, the program continues 

print "Do you want to keep the old log? (Y/N)"
activeLog(raw_input()=="Y")

p = Portfolio()
p.addCash(300.50)
print p
s = Stock(20,"HFH")
p.buyStock(5,s)
print p
mf1 = MutualFond("BRT")
mf2 = MutualFond("GHT")
p.buyMutualFund(10.3, mf1)
print p
p.buyMutualFund(2,mf2)
print p
p.sellMutualFund("BRT",3)
print p
p.sellMutualFund("HFH",1)
print p
p.withdrawCash(50)
print p
p.history()






