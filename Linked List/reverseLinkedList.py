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

    def reverseLinkedListWithArray(self):
        array=[]
        pointer=ll.head
        iterator=-1
        while pointer:
            iterator+=1
            array.append(pointer.data)
            pointer=pointer.nextReference
        prev=None
        
        ll.head=Node(array[iterator])
        prev=ll.head
        while iterator>0:
            iterator-=1
            prev.nextReference=Node(array[iterator])
            prev=prev.nextReference
           # prev.n
            
    def  recursiveMethod(self,prevPointer,pointer):
       # print(ll.head.data)
        if pointer.nextReference==None:
            ll.head=pointer
            pointer.nextReference=prevPointer
            return
        self.recursiveMethod(pointer,pointer.nextReference)
        pointer.nextReference=prevPointer
        #return
        
reverseVal=reverse()
#ll=linkedList()

reverseVal.add(40)
reverseVal.add(50)
reverseVal.add(10)
reverseVal.add(20)
reverseVal.add(30)
#reverseVal.reverseElements()
#reverseVal.reverseAnotherMethod()
prevPointer=None
pointer=ll.head

#reverseVal.recursive(prevPointer,pointer)
#reverseVal.reverseLinkedListWithArray()
prevPointer=None
pointer=ll.head
reverseVal.recursiveMethod(prevPointer,pointer)
ll.printElements(ll.head)
