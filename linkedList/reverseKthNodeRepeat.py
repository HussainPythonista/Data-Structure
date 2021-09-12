from linkedList import *

#node
def reverse(head):
    prev=None
    pointer=None
    next=head
    while next!=None:
        prev=pointer
        pointer=next
        next=next.nextReference
        pointer.nextReference=prev
    return pointer
def reverseLinkedList(head,k):
    count=1
    pointer=head
    while count!=k:
        #print(pointer.data)
        if pointer.nextReference==None:
            return head
        pointer=pointer.nextReference
        count+=1
    newHead=pointer
    q=pointer
    tempVal=None
    #tempPointer=pointer.nextReference
    while (1):
        pointer=head
        #tempPointer=q.nextReference
        tempPointer=None
        if tempPointer==None:
           tempVal=reverse(pointer)
           return tempVal
        q.nextReference=None
        q=tempPointer
        head=tempPointer
        count=1
    
        

linkedList=linkedList()
k=3
for i in range(3):
    linkedList.addElement(i)
linkedList.printElements(linkedList.head)
reverseLinkedList(linkedList.head,k)

#linkedList.printElements(reverse(linkedList.head))
linkedList.printElements(linkedList.head)