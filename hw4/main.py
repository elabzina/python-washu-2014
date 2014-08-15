from classes import *

#This file contains a few examples/test of LinkedList class


k = LinkedList()

#add Items
#only integers can be added, other inputs will cause an error

k.addNode(2)
k.addNode(3)
k.addNode(6)
k.addNode(7)
k.addNode("lkjlkj")
k.addNode(24.234)
k.addNode(9)
k.addNode(10)
k.addNode(3)


print k

#remove by value

k.removeNodeByValue(3)

print k

#remove a node (by pointer)

p = k.start.next.next
k.removeNode(p)

print k

#add node after

p = k.start.next.next.next
k.addNodeAfter(3444,p)

print k

#add node before

k.addNodeBefore(222,p)

print k

#Check for cycles

#no cycle:

print k.isCycle()

#create a cycle

a = k.start.next.next.next.next.next
a.next=k.start.next.next

print k.isCycle()

#print k
#print l

#This line is always necessary, becauses the compiler sometimes doesn't 'clean' the memory between running sessions
k = None