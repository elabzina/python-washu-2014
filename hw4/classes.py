class Node():
    def __init__(self, _value=None, _next=None):
        self.value=_value
        self.next=_next
    def __str__(self):
        return str(self.value) 

class LinkedList():
    #pointers to the first and last nodes of the link are stored, also len stores the number of nodes.
    #in case of the cycles len stops making sense; overall 
    def __init__(self,value=None):
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

 #Computation complexity is 1, since the node is just added to the end, while the end is stored as self.last No way to make it more efficient.
    def addNode(self,new_value):
        if (not LinkedList.intCheck(new_value)): return
        self.last.next=Node(new_value)
        self.last=self.last.next
        self.len+=1

#Without checking whether this code is in this list, the complexity is 1, hence it's know where exactly to add it. Including the check, the complexity is proportional to the length of the list, 
#and since this is not a sorted list or something similar, there's no way to improve it
    def addNodeAfter(self,new_value,after_node):
        if (not LinkedList.intCheck(new_value)): return
        search=self.start
        while (search.next!=after_node and search!=None): search=search.next
        if (search==None): 
            print "No such node!"
            return
        tail = after_node.next
        after_node.next = Node(new_value)
        after_node.next.next=tail
        self.len+=1

#Exactly the same situation as in the previous case.
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


#Exactly the same situation as in the previous case.
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



#All nodes are looked at it one by one. The complexity equals to the number of the nodes. Because of the structure of the data, no way exists to decrease this number.
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
        if (self.isCycle()): return "The list contains cycles and can't be displayed properly"
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

   #function to understand whether the list has a cycle
   #the idea is to move the lookup pointer node by node in the list cheching whether the link of the pointer is linked 
   #to a node behind the lookup pointer
    def isCycle(self):
        if (self.start==None): return False
        if (self.start.next==self.start):return True
        search = self.start
        lookup=self.start.next
        while (lookup.next!=None):
            while (search.next!=lookup):
                if (lookup.next==search): return True
                search=search.next
            lookup=lookup.next
            search=self.start
        return False

          














