#this file contains the sorting methods and the wrapper function to calculate the number of comparisons through the use of the global variable counter
#the wrapper to unify all the sorting methods to return the number of comparisons
counter = 0

#This function is used for the tests. Returns sorted d in an explicit form.
def getDataSet(sortMethod,d):
    sortMethod(d)
    return d

def wrapMethod(sortMethod,d):
    global counter
    counter = 0
    sortMethod(d)
    return counter

#Simple bubble sort
def bubble(d):
    global counter
    n = len(d)
    for i in range(0,n):
        for j in range(0,n-i-1):
            counter+=1
            if (d[j+1]<d[j]):
                t = d[j]
                d[j]= d[j+1]
                d[j+1] =t
                
   

#Impoved bubble sort, it stops working once the whole dataset has been looked through without a single reassignment
def bubbleUpdated(d):
    global counter
    n = len(d)
    flag=True
    for i in range(0,n):
        if (not flag): exit
        flag=False
        for j in range(0,n-i-1):
            counter+=1
            if (d[j+1]<d[j]):
                t = d[j]
                d[j]= d[j+1]
                d[j+1] =t
                flag=True
  

    

#mergeSort
def mergesort(d):
    a = mergeSort(d)
    for i in range(0,len(a)): d[i]=a[i]
           
def mergeSort(d):
    global counter
    n = len(d)
    counter+=1
    if len(d) <= 1: return d
    middle = len(d) / 2
    left = d[0:middle]
    right = d[middle:n] 
    left = mergeSort(left)
    right = mergeSort(right)
    result = merge(left, right)
    return result

def merge(left,right):
     global counter
     result=[]
     counter+=1
     while (len(left) > 0 or len(right) > 0):
        counter+=1
        if (len(left) > 0 and len(right) > 0):
            counter+1
            if (left[0] <= right[0]):
                result.append(left[0])
                left = left[1:len(left)]
            else:
                result.append(right[0])
                right = right[1:len(right)]
        else:   
            counter+=1
            if (len(left) > 0):
                    result.append(left[0])
                    left = left[1:len(left)]    
            else:   
                    counter+1
                    if (len(right) > 0):
                        result.append(right[0])
                    right = right[1:len(right)]
        
     return result 
#quickSort

#to unify this function with the rest of the sorting methods to be called with the wrapper function
def quickSortCall(d):
    quickSort(d,0,len(d)-1)

def quickSort(S, p, r):
    if (p < r):
        q = Partition(S, p, r)
        quickSort(S, p, q-1)
        quickSort(S, q+1,r)


def Partition(S, p, r):
    global counter
    counter+=1
    x = S[r]
    counter+=1
    i = p-1 
    for j in range(p,r):
        if (S[j] <= x):
            i = i+1
            t = S[j]
            S[j]= S[i]
            S[i] = t 
            counter+=4
    t=S[r]
    S[r]=S[i+1] 
    S[i+1]=t
    counter+=4
    return i+1

    