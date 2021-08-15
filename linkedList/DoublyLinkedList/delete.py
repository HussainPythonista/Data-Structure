from doublyLinkedList import *
dd=doublyLinkedList()

dd.insertNewNode(10)
dd.insertNewNode(20)
dd.insertNewNode(30)
dd.insertNewNode(40)
dd.insertNewNode(50)
def deleteNode(head,value):
    if head.data==value:
        ref=head.nextReference
        dd.head=ref
        dd.head.prevReference=None
    elif value==dd.lastNode().data:
        prevOfLast=dd.lastNode().prevReference
        dd.lastNode().prevReference.nextReference=None
    else:
        pointer=head
        while pointer:
            if value==pointer.data:
                pointer.prevReference.nextReference=pointer.nextReference
                pointer.nextReference.prevReference=pointer.prevReference

            pointer=pointer.nextReference
    dd.printForward()
    dd.printBackward()
deleteNode(dd.head,30)