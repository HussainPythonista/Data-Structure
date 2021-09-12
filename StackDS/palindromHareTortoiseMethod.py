import sys
import os
from typing import Counter
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from stack import *
from linkedList.linkedList import *
def reverse(head):
    prevPointer=None
    currentPointer=None
    pointer=head
    while pointer:
        prevPointer=currentPointer
        currentPointer=pointer
        pointer=pointer.nextReference
        currentPointer.nextReference=prevPointer
    return currentPointer

def isPalindrrome(typle,head,nextStart):
    linkedlist.printElements(nextStart)
    linkedlist.printElements(head)
    if typle=="Odd":
        aPointer=head
        bPointer=nextStart
        while aPointer and bPointer:
            if aPointer.nextReference.nextReference==None:
                aPointer.nextReference=None
            if aPointer.data==bPointer.data :
                aPointer=aPointer.nextReference
                bPointer=bPointer.nextReference
            else: 
                return False
        return True
    else:
        aPointer=head
        bPointer=nextStart
        while aPointer and bPointer:
            if aPointer.data==bPointer.data :
                aPointer=aPointer.nextReference
                bPointer=bPointer.nextReference
            else: 
                return False
        return True
    linkedlist.printElements(head)
    linkedlist.printElements(nextStart)
def middleNode(head):
    if head.nextReference==None or head==None:
        return True
    elif head.nextReference.nextReference==None:
        if head.data==head.nextReference.data:
            return True
        else:
            return False
    else:
        
        tortoise=head
        hare=head
        stopPointer=None
        stop=False
        c=0
        typle=None
        while True:
            hare=hare.nextReference.nextReference
            tortoise=tortoise.nextReference
            #nextStart=tortoise.nextPointer
            if hare.nextReference==None:
                last=hare
                typle="Odd"
                break
            if hare.nextReference.nextReference==None:
                last=hare.nextReference
                typle="Even"
                break
            
        nextStart=tortoise.nextReference
        tortoise.nextReference=None
        reveresedNode=reverse(nextStart)
        return(isPalindrrome(typle,head,reveresedNode))
if __name__=="__main__":
    linkedlist=linkedList()
    linkedlist.addElement(1)
    linkedlist.addElement(2)
    linkedlist.addElement(2)
    linkedlist.addElement(1)#.nextReference.nextReference
    tempHead=linkedlist.head

    print(middleNode(tempHead))
    
