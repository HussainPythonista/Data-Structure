from linkedList import *

def reverseLinkedList(head):
    prevRef=None
    current=prevRef
    pointer=head
    while pointer:
        prevRef=current
        current=pointer
       
        pointer=pointer.nextReference
        current.nextReference=prevRef
    
    return current

list1=linkedList()
array=[0]


list1.insertElement(array)


def addTwoNumbers(list1,list2):
    justToKnow=linkedList()
    aPointerHead=reverseLinkedList(list1.head)
    bPointerHead=reverseLinkedList(list2.head)
    aPointer=aPointerHead
    bPointer=bPointerHead
    carry=0
    result=[]
    while aPointer!=None and bPointer!=None :
        sumValue=aPointer.data+bPointer.data+carry
        result.append(sumValue%10)
        carry=sumValue//10
        aPointer=aPointer.nextReference
        bPointer=bPointer.nextReference
    while aPointer:
        sumValue= aPointer.data+carry
        result.append(sumValue%10)
        carry=sumValue//10
        aPointer=aPointer.nextReference
    while bPointer:
        sumValue= bPointer.data+carry
        result.append(sumValue%10)
        carry=sumValue//10
        bPointer=bPointer.nextReference
    if carry!=0:
        result.append(carry)
    print(result)
list2=linkedList()
array2=[7,3]


list2.insertElement(array2)
addTwoNumbers(list1,list2)