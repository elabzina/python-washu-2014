class Node():
    def __init__(self, _value=None, _next=None):
        self.value=_value
        self.next=_next
    def __str__(self):
        return str(self.value) 

class NodeColor(Node):
    def __init__(self, node=None):
        self.value=node.value
        self.color=False
        if (node.next!=None): self.next=NodeColor(node.next)
        else: self.next=None


class LinkedList():
    def __init__(self,value):
        if (not isinstance(value,int)):
            self.last=self.start=Node(None)
            self.len=0
        else: 
            self.last=self.start=Node(value)
            self.len=1

    @staticmethod
    def intCheck(value):
        if (not isinstance((value),int)):
            print "The number you intered is not an interger!"
            return False
        return True

    def addNode(self,new_value):
        if (not LinkedList.intCheck(new_value)): return
        self.last.next=Node(new_value)
        self.last=self.last.next
        self.len+=1

    def addNodeAfter(self,new_value,after_node):
        if (not LinkedList.intCheck(new_value)): return
        search=self.start
        while (search.next!=after_node and search!=None): search=search.next
        if (search==None): 
            print "No such node!"
            return
        tail = after_node.next
        after_node.next = Node(new_value)
        afer_node.next.next=tail
        self.len+=1

    def addNodeBefore(self,new_value,before_node):
        if (not LinkedList.intCheck(new_value)): return
        search=self.start
        while (search.next!=before_node and search!=None): search=search.next
        if (search==None): 
            print "No such node!"
            return
        search.next = Node(new_value)
        search.next.next=before_node
        self.len+=1

    def removeNode(self,node_to_remove):
        search=self.start
        while (search.next!=node_to_remove and search!=None): search=search.next  
        if (search==None): 
            print "No such node!"
            return 
        tail=node_to_remove.next
        search.next=tail
        node_to_remove=None
        self.len-=1

    def removeNodeByValue(self,value):
        if (not LinkedList.intCheck(value)): return
        search=self.start
        while (search!=None):
            if (search.value==value):
                aux=search
                search=search.next
                self.removeNode(aux)
            else: search=search.next
     
    def __str__(self):
        tail=self.start
        out=""
        while (tail!=None):
            out+=str(tail)+" -> " 
            tail=tail.next
        out+="NULL"
        return out

    def length(self):
        s = "Length: "+str(self.len)
        return s

    def reverse(self):
        tail=self.last=self.start
        self.start=None
        while (tail!=None):
            aux=tail
            tail=tail.next
            aux.next=self.start
            self.start=aux
   
    def findCirle(self):
         n = NodeColor(self.start)
         return self.findCircle_(n)

    def findCircle_(self,node):
        if (node==None): return False
        if (node.color): return True
        node.color=True
        return(self.findCircle_(node.next))

def IsNodeofList(l,n):
    while (l!=n and l!=None): l = l.next
    if (l==None): return False
    return True

o = None
o = Node(1)
o.next=Node(3)
o.next.next=Node(4)

a = Node(2)

print IsNodeofList(o,a)

a=o.next

print IsNodeofList(o,a)

'''
k=None
k = LinkedList(1)



k.addNode(1)

k.addNode(3)

k.addNode(4)

print k
print k.length()
k.removeNodeByValue(3)

print k
print k.length()

k.addNode(5)
k.addNode(0)

k.addNode("dasd")

print k
k.reverse()
print k

print k.length()

print k.findCirle()

print k.start
print k.last

a = k.start.next.next

print a

k.removeNode(a)

print k

a = k.start.next
print "sdfsdf"
print a


#.start.next.next = k.start

#print k.findCirle()
'''








