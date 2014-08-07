from collections import defaultdict

class School():
	def __init__(self, school_name=""):
		self.school_name = school_name
		self.raw = defaultdict(list)
		self.db = dict()
		
	def __str__(self):
		return "Hey, this is %s school, bro!" % (self.school_name)
   
	def add(self,name,grade):
		self.raw[grade].append(name)
		self.db = dict(self.raw)
		for key, value in self.db.items(): self.db[key]=set(self.db[key])

	def grade(self, grade):
		if (grade in self.db.keys()): return (self.db[grade])
		return None
	
	def sort(self):
		dump = dict(self.raw) 
		for key, value in dump.items(): 
			dump[key].sort()
			dump[key]=tuple(dump[key])
		return(dict(sorted(dump.items())))
		
	
		


	
