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
        else: self.last=self.start=Node(value)

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

    def addNodeBefore(self,new_value,before_node):
        if (not LinkedList.intCheck(new_value)): return
        search=self.start
        while (search.next!=before_node and search!=None): search=search.next
        if (search==None): 
            print "No such node!"
            return
        search.next = Node(new_value)
        search.next.next=before_node

    def removeNode(self,node_to_remove):
        search=self.start
        while (search.next!=node_to_remove and search!=None): search=search.next  
        if (search==None): 
            print "No such node!"
            return 
        tail=node_to_remove.next
        search.next=tail
        node_to_remove=None
    
    def removeNodeByValue(self,value):
        if (not LinkedList.intCheck(new_value)): return
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



