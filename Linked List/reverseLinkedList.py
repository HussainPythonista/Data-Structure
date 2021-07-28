from linkedList import *
ll=linkedList()
class reverse(object):
    #def __init__(self):
       
        
    def add(self,data):
        ll.addElement(data)
    def printVal(self,head):
        ll.printElements(head)
    def reverseElements(self):
        prev=None
        pointer=ll.head
        while pointer!=None:
            dummyPointer=pointer.nextReference
            
            pointer.nextReference=prev
            prev=pointer
            pointer=dummyPointer
        ll.head=prev

    def reverseAnotherMethod(self):
        bPrev=None
        prev=None
        pointer=ll.head
        while pointer !=None:
            bPrev=prev
            prev=pointer
            
            pointer=pointer.nextReference
            prev.nextReference=bPrev
            #pointer.nextReference=prev
            
        ll.head=prev
    
reverseVal=reverse()
#ll=linkedList()

reverseVal.add(40)
reverseVal.add(50)
reverseVal.add(10)
reverseVal.add(20)
reverseVal.add(30)
reverseVal.reverseElements()
reverseVal.reverseAnotherMethod()
head= ll.head


ll.printElements(head)
prevPointer=None
pointer=ll.head

reverseVal.recursive(prevPointer,pointer)
