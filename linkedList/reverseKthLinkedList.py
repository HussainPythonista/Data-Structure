#This one is Really hard Problem

#Step's Are:
# 1.We Need to count the number of nodes 


#Loading Data

#from linkedList.linkedList import Node
from typing import no_type_check_decorator
from linkedList import *

listOfNodes=[1,2,3,4,5,6,7,9]#->I need answer like this [3,2,1,6,5,4,7,8]

ll=linkedList()
ll.insertElement(listOfNodes)
#ll.printElements(ll.head)

#Step 1 Count the Data


def countNumberOfNodes(head):
    pointer=head
    count=0
    while pointer:
        count+=1
        pointer=pointer.nextReference
    return count



def reverseLinkedList(head):
    pointer=head
    prev=None
    current=None
    while pointer:
        prev=current
        current=pointer
        pointer=pointer.nextReference
        current.nextReference=prev
    return current
def reverseTheKNode(head,k):
    #Create Dummy Head for set as head
    dummyHead=None

    #tracking variables for reverse
    prev=None
    pointer=head
    length=countNumberOfNodes(head)

    #This both are use for Tracking next Set of Elements
    tail1=None
    tail2=head
    #we should run the loop for until he lenght come below the k
    while length>=k:
        for i in range(k):

            #When ever the loop run the certain nextPointer is always next to the current Pointer
            #  
            nextPointer=pointer.nextReference
            
            #We change the link of node to previous one
            pointer.nextReference=prev
            
            #now set Prev Value current Value
            prev=pointer

            #Move current to the nextPointer
            pointer=nextPointer
        
        #The Head Element is alway in the Prev Node
        if dummyHead==None:
            dummyHead=prev
        
        if tail1==None:
            tail1=tail2
            
        tail1.nextReference=prev
        tail2.nextReference=pointer
        tail2=pointer
        
        
        length-=k
        
    ll.printElements(dummyHead)
    #ll.printElements(newNode)
head=ll.head
k=3
reverseTheKNode(head,k)

