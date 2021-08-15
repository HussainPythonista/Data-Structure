from linkedList import *


ll=linkedList()


def totalCountOfList(head):
    count=1
    pointer=head
    while pointer:
        
        pointer=pointer.nextReference
        count+=1
    return count

#totalCountOfList()

listValue=[1,2,3]
ll.insertElement(listValue)
Head=ll.head
def deleteNodeFromLast(head,index):
    totalValPresent=totalCountOfList(head)
    if head==None:
        return
    elif head.nextReference==None and index>totalValPresent:
        return 
    elif head.nextReference==None and index==1:
        head=None
        return
    else:
        #print(totalValPresent)
        indexIwantDelete=totalValPresent-index
        #print(indexIwantDelete)
        pointer=head.nextReference
        count=1
        prevRef=head
        print(indexIwantDelete)
        if indexIwantDelete==1:
            head=pointer
        while pointer:
            count+=1
            if count==indexIwantDelete:
                tempNext=pointer.nextReference
                prevRef.nextReference=tempNext
                
            pointer=pointer.nextReference
            prevRef=prevRef.nextReference
            
    ll.printElements(head)
val=deleteNodeFromLast(Head,1)
print(val)

