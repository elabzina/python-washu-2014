#this file contains the sorting methods and the wrapper function to calculate the number of reassignments through the use of the global variable counter

counter=0

#the wrapper to 

#Simple bubble sort
def bubble(d):
    global counter
    counter=0
    n = len(d)
    for i in range(0,n):
        for j in range(0,n-i-1):
            counter+=1
            if (d[j+1]<d[j]):
                t = d[j]
                d[j]= d[j+1]
                d[j+1] =t
                
   

#Impoved bubble sort, it stops working if once the whole dataset has been looked through without a single reassignment
def bubbleUpdated(d):
    global counter
    n = len(d)
    flag=True
    for i in range(0,n):
        counter+=1
        if (not flag): exit
        flag=False
        for j in range(0,n-i-1):
            counter+=1
            if (d[j+1]<d[j]):
                t = d[j]
                d[j]= d[j+1]
                d[j+1] =t
                flag=True
  

    

def heap(d):
 
    count=0
    n=len(d)
    for i in range((n / 2)-1,0,-1):
        count+=moveDown(d, i, n);

    for i in range(n-1,0,-1):  
        temp = d[0];
        d[0] = d[i];
        d[i] = temp;
        count+=moveDown(d, 0, i-1)

    #update_last(d)
    return d 

def update_last(d):
    n = len(d)
    temp = d[n-1]
    index = 0
    while (temp>d[index]): index+=1
    for i in range(n-1,index+1,-1): d[i] = d[i-1]
    d[index] = temp
    
    

def moveDown(d,root, bottom):

  count=0
  done = 0;
  while ((root*2 <= bottom) and (not done)):
  
    count+=1
    if (root*2 == bottom):  maxChild = root * 2
    else: 
        count+=1
        if (d[root * 2] > d[root * 2 + 1]):   
            maxChild = root * 2
            count+=1
        else:   maxChild = root * 2 + 1

    count+=1
    if (d[root] < d[maxChild]):
        temp = d[root]
        d[root] = d[maxChild]
        d[maxChild] = temp
        root = maxChild
    else:   done = 1;
    return count

  
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

    