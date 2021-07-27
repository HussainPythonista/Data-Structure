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
        self.sumValue=0
        self.maxValue=0
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

    def sumAllElement(self):
        if self.head.nextReference==None:
            self.sumValue+= self.head.data
            return self.sumValue
        else:
            self.sumValue+= self.head.data
            self.head=self.head.nextReference
            self.sumAllElement()
        return self.sumValue

    def maxVal(self):
        
        if self.head.nextReference!=None:
            #print(self.head.data)
            if self.maxValue<self.head.data:
                self.maxValue=self.head.data
                
                self.head=self.head.nextReference
                self.maxVal()
            else:
                self.head=self.head.nextReference
                self.maxVal()
        else:
            
            if (self.head.data>self.maxValue):
                self.maxValue=self.head.data
        return self.maxValue
      
    def searchElement(self,find):
        if self.head==None:
            return "Nope"
        elif self.head.data==find:
            return ("Found",self.count)
       
        self.count+=1
        self.head=self.head.nextReference
        return self.searchElement(find)
       # return
    
        
ll=LinkedList()
ll.addElements(50)

ll.addElements(90)
ll.addElements(190)
ll.addElements(43)
ll.addElements(322)
ll.addElements(9)
ll.addElements(19)
ll.revesrseLinkedList()
print(ll.printElementsRecursion())