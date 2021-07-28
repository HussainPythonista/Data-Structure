
class Node(object):#This is A Node Which
    def __init__(self,data,nextReference=None):
        #data means data i want to store
        self.data=data
        
        #reference To the Next Node
        self.nextReference=nextReference

#This is actual Linked List
#Here Only we perform whole operations

   
    
class linkedList(object):
    def __init__(self,head=None):
        #Head is Pointer node 
        # it is Present in stack and pointing to the first node in Linked List

        self.head=head
        self.last=None#This One is used for fast method

    #The Below Method is Slowest One Because Every Time When I Add Element 
    #It Checks For Last Node
    #Last Node Contains Next Pointer as None
    def addElement(self,data):

        if self.head==None:
            self.head=Node(data,None)
        else:
            #I have created one pointer  for easy to handle in while loop
            pointer=self.head

            #The loop will run until the next Refernce is None
            while pointer.nextReference is not None: #I take pointer.nextRefernce because i want to check nextReference to be None

                pointer=pointer.nextReference
            pointer.nextReference=Node(data,None)
    def addElement2(self,data):
        if self.head==None:
            #Create an Object
            node=Node(data)
            
            #Set head as that Node because before the head is None
            self.head=node
            self.last=node
        else:

            #Before the adding node the last Position will be remain as None
            #Now I need To change the Last NextReference as Current Creating Node
            #The Set That Node As Last Node As final
            node=Node(data)
            self.last.nextReference=node
            self.last=node
    
    def printElements(self):
        if self.head==None:
            print("There is no element in Head ")

        else:
            #Traverse all the Element in linkedList For Printing
            pointer=self.head

            ValToPrint=""
            while pointer:
                #This one is for achive something i want through Traverse
                ValToPrint+=str(pointer.data)+"->"
                pointer=pointer.nextReference
            print(ValToPrint)
    def insetElementInSortedList(self,value):
        if self.head == None:
            self.head=Node(value)
        elif self.head.data>value:
            temp=self.head
            node=Node(value)
            node.nextReference=temp
            self.head=node
        else:
            prev=None
            pointer=self.head
            while pointer:
                
                if  pointer.data>value:
                    temp=pointer
                    node=Node(value,pointer)
                    node.nextReference=temp
                    prev.nextReference=node
                    break
                prev=pointer
                pointer=pointer.nextReference
            
    def reverse(self):
        
        bPrev=None
        prev=None
        pointer=self.head
        while pointer !=None:
            bPrev=prev
            prev=pointer
            
            pointer=pointer.nextReference
            prev.nextReference=bPrev
            #pointer.nextReference=prev
            
        self.head=prev
    
    def findDuplicates(self):

        
        pointer=self.head
        prev=pointer.nextReference
        while prev:
            if pointer.data==prev.data:
                print(prev.data)
                #prev.nextReference=None
                prev=prev.nextReference
            elif pointer.data!=prev.data:
                pointer=prev
                prev=prev.nextReference
            pointer.nextReference=prev
            
ll=linkedList()
ll.addElement(5)
ll.addElement(5)
ll.addElement(5)
ll.addElement(6)
ll.addElement(6)
ll.addElement(7)
ll.addElement(7)
ll.addElement(7)
ll.addElement(7)
#ll.printElements(ll.head)
#ll.reverse()

pointer=ll.head
prevPointer=None
ll.findDuplicates()
ll.printElements()
