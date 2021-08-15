from linkedList import *

ll=linkedList()

listValue=[1,1,1,2,2,3,3,4,4,4,4,5]

ll.insertElement(listValue)

Head=ll.head

def FindDuplicates(head):
    tortoise=head
    hare=head.nextReference
    while hare:
        if tortoise.data==hare.data:
            #hare.nextReference=None
            hare=hare.nextReference
            
            tortoise.nextReference=None
        else:
            temp=hare.nextReference
            node=hare
            #node.nextReference=None
            
            tortoise.nextReference=node
           # node.nextReference=None
            tortoise=tortoise.nextReference
            
    
    return head
val=FindDuplicates(Head)
ll.printElements(val)