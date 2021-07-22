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
    
    def printElements(self):
        if self.head==None:
            print("There is no element in Head ")

        else:
            #Traverse all the Element in linkedList For Printing
            pointer=self.head

            ValToPrint=""
            while pointer:
                ValToPrint+=str(pointer.data)+"->"
                pointer=pointer.nextReference
            print(ValToPrint)
    def countNumberOfNodes(self):
        if self.head==None:
            print("No Node to count")
        else:
            count=0
            pointer=self.head
            while pointer:
                count+=1
                pointer=pointer.nextReference
            return count
ll=linkedList()
ll.addElement(20)
ll.addElement(30)
ll.addElement(40)
ll.addElement(50)
ll.printElements()
print(ll.countNumberOfNodes())