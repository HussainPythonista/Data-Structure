from doublyLinkedList import *
dd=doublyLinkedList()
dd.insertNewNode(20)
dd.insertNewNode(30)
dd.insertNewNode(40)
dd.insertNewNode(50)
dd.insertNewNode(60)
dd.insertNewNode(70)

def insertInBetween(head,index,data):
    #Create head for transform next node
    pointer=head

    #for finding index because i insert value after Particular Index
    count=0

    #I move Until next Pointer Get None
    while pointer:
        
        #If count ==index then I reached what index i want
        #So I insert Which Value I want After certain index
        if count==index-1:

            #I store the address of previous Reference for future use
            prev=pointer
            #print(prev.data)

            #Create Node
            node=Node(data)
            #I set node prev Reference as prev(which already stored)
            node.prevReference=prev
            #Set nextReference as pointer nextReference Address
            node.nextReference=pointer.nextReference
            #print(node.prevReference.data)

            #This one is Important
            #Because i set pointer's nextReferece is 50 then 50's prevReferce 40
            #I set 50's previous reference as newly Created Node
            pointer.nextReference.prevReference=node

            #Set Next Reference is created Node
            pointer.nextReference=node
        count+=1
        pointer=pointer.nextReference
        
head=dd.head

insertInBetween(head,3,90)
dd.printForward()
dd.printBackward()