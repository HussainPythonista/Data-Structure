from linkedList import *

firstList=linkedList()
firstList.addElement(10)
#firstList.addElement(11)
firstList.addElement(11)
firstList.addElement(17)
firstList.addElement(20)
firstList.addElement(41)
firstList.addElement(43)
firstList.addElement(44)
firstList.addElement(46)
firstList.addElement(49)
firstList.addElement(90)
firstList.addElement(98)
firstList.addElement(104)
firstList.addElement(200)
firstHead=firstList.head
#firstList.printElements(firstHead)


secondList=linkedList()
secondList.addElement(9)
secondList.addElement(12)
#secondList.addElement(13)
secondList.addElement(16)
secondList.addElement(21)
secondList.addElement(22)
secondList.addElement(56)
secondList.addElement(89)
secondList.addElement(99)
secondHead=secondList.head
#secondList.printElements(secondHead)

def mergeTwoList(first,second):
    last=None
    dummy=None
    if first.data<second.data:
        node=Node(first.data)
        last=node
        dummy=node
        first=first.nextReference
    elif first.data>second.data:
        node=Node(second.data)
        last=node
        dummy=node

        second=second.nextReference
    while first!=None and second!=None:
        if first.data<second.data:
            
            node=Node(first.data)
            last.nextReference=node
            #dummy=node
            last=node
            first=first.nextReference
            last.nextReference=None
        elif first.data>second.data:

            node=Node(second.data)
            last.nextReference=node
            #dummy=node
            last=node
            second=second.nextReference
            last.nextReference=None
    
    if second!=None:
        last.nextReference=second
    if first!=None:
        last.nextReference=first
    ll.printElements(dummy)
    #10->11->15->17->20
    #9->12->16
    
first=firstHead
second=secondHead
mergeTwoList(first,second)
