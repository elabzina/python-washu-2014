#This file runs all four sorting algorithms and plots them

from sort_methods import *
from random import *
import plugin 
import numpy as np 
from pylab import * 


X = np.linspace(2,100,98,endpoint=True) 
bubble = plugin.efficiencyMeasure.measureSpeed(bubble,100,50)
#advanced_bubble = plugin.efficiencyMeasure.measureSpeed(bubbleUpdated,100,50)
merge_sort = plugin.efficiencyMeasure.measureSpeed(mergeSort,100,50)
quick_sort= plugin.efficiencyMeasure.measureSpeed(quickSortCall,100,50)
plt.plot(X,bubble,color='r',label='Bubble') 
#plt.plot(X,advanced_bubble,color='b',label='Adjusted Bubble') 
plt.plot(X,merge_sort,color='y',label='MergeSort') 
plt.plot(X,quick_sort,color='g',label='QuickSort')
plt.ylabel("mean(comparisons) for random samples")
plt.xlabel("N of sample")
plt.gca().legend(loc='upper center', shadow=True)
show()
