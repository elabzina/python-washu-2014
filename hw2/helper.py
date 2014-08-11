import numbers

def validate(x):
	if (not isinstance(x, numbers.Number)): 
		print "Wrong format. The input is not a number."
		return False
		
	if x<=0: 
		print "The input must be possitive."
		return False
	return True
