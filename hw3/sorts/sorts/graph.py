#This file runs all three algorithms and plots them

from sort_methods import *
from random import *
import plugin 
import numpy as np 
from pylab import * 

X = np.linspace(2,50,49,endpoint=True) 
bubble = plugin.efficiencyMeasure.measureSpeed(bubble,50,50)
advanced_bubble = plugin.efficiencyMeasure.measureSpeed(bubbleUpdated,50,50)
quick_sort= plugin.efficiencyMeasure.measureSpeed(quickSortCall,50,50)
plot(X, bubble,color='r') 
plot(X, advanced_bubble,color='b') 
plot(X, quick_sort,color='g')
show()
#print count1

#count1 = method.efficiencyMeasure.measureSpeed(heapSort,50,50)
#print count1
#d = [1,0,0,2,2,4,2,23,232,23,34,345,345,34653,364,234,0]
#print d
#counter = 0
#d = [randint(1,20) for _ in range(20)]
 #d= np.random.choice(49,49) 
#print d
#wrapQuickSort(d)
#print d









