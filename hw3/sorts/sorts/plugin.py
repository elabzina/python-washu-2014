#This file contains two static functions to measure the number of the reassignments for a given sorting algorithm. sortMethod is the parameter links to a sorting algorithm
#measureSpeedSingle this is the function which runs the sorting algorithm iter times for a random array of the length N
#measureSpeed applies measureSpeedSingle to arrays of length from 1 to maxN iter times each. It returns the average number of reassignments for each i, this output is used for the plot  

from random import *

class efficiencyMeasure(object):
    @staticmethod
    def wrapMethod(sortMethod,d):
        global counter
        counter=0
        sortMethod(d)
        return counter

    @staticmethod
    def measureSpeedSingle(sortMethod,N,iter):
        average = 0
        iter1 = iter/1.0
        for i in range(1,iter):
            average+=efficiencyMeasure.wrapMethod(sortMethod,[randint(1,N) for _ in range(N)])/iter1
        return round(average,2)
    
    @staticmethod
    def measureSpeed(sortMethod,maxN,iter):
        result=[] 
        for i in range(1,maxN): result.append(efficiencyMeasure.measureSpeedSingle(sortMethod,i,iter))
        return result


