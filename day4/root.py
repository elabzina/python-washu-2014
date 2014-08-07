def sqr(n,g):
	nw = g - (g**2 - n)/(2*g)
	return nw	
 
 
def f_sqr(n,g,p=0.001,max_steps=10000000):
	g = float(g)
	n = float(n)
	nw = sqr(n,g)
	cp = 1
	steps = 0
	while (cp > p) and (steps<max_steps):
		nq = sqr(n,g)
		cp = abs(nq - g)
		g = nq
		steps+=1		
	return g

print f_sqr(9,1)