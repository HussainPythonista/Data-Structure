from linkedList import *

headA=linkedList()
listVal1=[2,1,8,4,5]
headA.insertElement(listVal1)
headA.printElements(headA.head)

headB=linkedList()
listVal1=[5,6,1,8,4,5]
headB.insertElement(listVal1)
headB.printElements(headB.head)


def reverse(head):
    current=head
    prev=None
    while current:
        pointer=current.nextReference
        current.nextReference=prev
        prev=current
        current=pointer
    return prev
def findIntersection(headA,headB):
    reverseA=reverse(headA.head)
    reverseB=reverse(headB.head)
    
    aPointer=reverseA
    
    bPointer=reverseB
    while aPointer and bPointer:
        #print(aPointer.data)
        if aPointer.data==bPointer.data:
            print(aPointer.data,bPointer.data)
            aPointer=aPointer.nextReference
            bPointer=bPointer.nextReference
        else:
            break
findIntersection(headA,headB)