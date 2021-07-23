


class Node(object):
    def __init__(self,data,nextReference=None):
        #data that means value to store
        self.data=data
        
        #nextrefernce of current Node

        self.nextReference=nextReference
 
class LinkedList(object):
    def __init__(self,head=None):
        #Pointer for FirstNode
        self.head=head
        self.count=0
        self.valToPrint=""
    def addElements(self,data):
        if self.head==None:
           self.head=Node(data)
           return self.head
        else:
            return self.lastElement(data,self.head)
    #Printing all elements
    def lastElement(self,val,current):
        if current.nextReference==None:
            current.nextReference=Node(val)
            return
        else:
           return self.lastElement(val,current.nextReference)
    
    def countNumberOfElement(self,node):
        if node==None:
            return 0
        else:
            #self.head=self.head.nextReference
            #self.count+=1
            return 1+self.countNumberOfElement(node.nextReference)
        

    def printElementsRecursion(self):
        if self.head.nextReference!=None:
            self.count+=1
            self.valToPrint+=str(self.head.data)+"-->"
            self.head=self.head.nextReference
            self.printElementsRecursion()
            return
        else:
            self.count+=1
            self.valToPrint+=str( self.head.data)
    
    #Method 1

    def getCount(self):
        if self.head.nextReference==None:
           self.count+=1
        else:
            self.count+=1
            self.head=self.head.nextReference
            self.getCount()
        #Before The I find the answer,I tried lot of times
        #The Mistake I had made is "I forgot to return what I want"
        return (self.count)

    #Method 2

    def getCount2(self):
        if self.head.nextReference==None:
            return 1
        else:
            self.head=self.head.nextReference
            return 1+self.getCount2()
ll=LinkedList()
ll.addElements(50)
ll.addElements(90)
ll.addElements(1090)
ll.addElements(90)
ll.addElements(90)
#ll.addElements(90)

#print(ll.getCount())
#print(ll.getCount2())
