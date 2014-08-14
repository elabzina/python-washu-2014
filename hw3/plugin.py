#This file contains two static functions to measure the number of the comparisons for a given sorting algorithm. sortMethod is the parameter linking to a sorting algorithm
#measureSpeedSingle this is the function which runs the sorting algorithm iter times for a random array of the length N
#measureSpeed applies measureSpeedSingle to arrays of length from 2 to maxN iter times each. It returns the average number of comparisons for each i, this output is used for the plot  

from random import *
from sort_methods import wrapMethod

class efficiencyMeasure(object):

    @staticmethod
    def measureSpeedSingle(sortMethod,N,iter):
        average = 0
        iter1 = iter/1.0
        for i in range(1,iter):
            average+=wrapMethod(sortMethod,[randint(1,N) for _ in range(N)])/iter1
        return round(average,2)
    
    @staticmethod
    def measureSpeed(sortMethod,maxN,iter):
        result=[] 
        for i in range(2,maxN): result.append(efficiencyMeasure.measureSpeedSingle(sortMethod,i,iter))
        return result


