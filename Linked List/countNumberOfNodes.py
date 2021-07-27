from node import Node
from linkedList import *

def countNumberOfNodes(head):
        #Checking the Node is Empty or Nit
        if head==None:
            print("No Node to count")
        else:

            count=0#Initialize
            pointer=head#Head Pointer
            while pointer:#Traverse Element until reach the Next Reference as None
                #Increase the Value
                count+=1
                #For Next Reference 
                pointer=pointer.nextReference
            return count
ll=linkedList()
ll.addElement(10)
ll.addElement(20)
ll.addElement(30)
print(countNumberOfNodes(ll.head))