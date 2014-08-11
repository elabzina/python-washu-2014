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
		