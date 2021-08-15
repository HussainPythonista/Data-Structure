from linkedList import *



a1=linkedList()
list1=[1]
a1.insertElement(list1)

a1Head=a1.head

a2=linkedList()
list2=[2]
a2.insertElement(list2)

def mergeThem(l1,l2):
    if l1==None and l2==None:
        return None
    elif l1!=None and l2==None:
        return l1
    elif l1==None and l2!=None:
        return l2
    forPrint=linkedList()
    #forPrint.printElements(l1)
    head=None
    #last=None
    if l1.data<=l2.data:
        node=Node(l1.data)
       # print(node.data)
        head=node
        last=node
        l1=l1.nextReference
        
        #l1=l1.nextReference
    elif l1.data>l2.data:
        node=Node(l2.data)
        head=node
        last=node
        l2=l2.nextReference
    aPointer=l1
    bPointer=l2
    #print(l1.data)
    while aPointer and bPointer:
        if aPointer.data<=bPointer.data:
            node=Node(aPointer.data)
            #head=node
            last.nextReference=node
            last=node
            #l1=l1.nextReference
            aPointer=aPointer.nextReference
            last.nextReference=None
            #l1=l1.nextReference
           
        elif aPointer.data>bPointer.data:
            node=Node(bPointer.data)
            #head=node
            last.nextReference=node
            last=node
            #l1=l1.nextReference
            bPointer=bPointer.nextReference
            last.nextReference=None
    if aPointer:
        last.nextReference=aPointer
    if bPointer:
        last.nextReference=bPointer
    forPrint.printElements(head)
        

print(mergeThem(a1.head,a2.head))