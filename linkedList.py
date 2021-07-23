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
                #This one is for achive something i want through Traverse
                ValToPrint+=str(pointer.data)+"->"
                pointer=pointer.nextReference
            print(ValToPrint)
    def countNumberOfNodes(self):
        #Checking the Node is Empty or Nit
        if self.head==None:
            print("No Node to count")
        else:

            count=0#Initialize
            pointer=self.head#Head Pointer
            while pointer:#Traverse Element until reach the Next Reference as None
                #Increase the Value
                count+=1
                #For Next Reference 
                pointer=pointer.nextReference
            return count
    
    def maxValue(self):
        maxVal=0
        pointer=self.head
        while pointer:
            if maxVal<pointer.data:
                maxVal=pointer.data
                pointer=pointer.nextReference
        return maxVal
    
    #Sum Of all Nodes
    def sumOfValues(self):
        sumVal=0
        pointer=self.head
        while pointer:
            sumVal+=pointer.data
            pointer=pointer.nextReference
        return sumVal
        
    
ll=linkedList()

ll.addElement(20)

ll.addElement(30)
ll.addElement(80)
#print(ll.reachingLastElement())
ll.printElements()

print(ll.maxValue())