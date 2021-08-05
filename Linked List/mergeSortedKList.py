from linkedList import *
#For perform sort Technique
#I need to push all values in single list
forSortPerform=[]

##LinkedList 1

l1=linkedList()
array=[1,4,5]
l1.insertElement(array)
forSortPerform.append(l1.head)#Append linkedList1

#LinkedList2
array2=[1,3,4]
l2=linkedList()
l2.insertElement(array2)
#l2.printElements(l2.head)

forSortPerform.append(l2.head)#Append linkedList2

#LinkedList3
array3=[2,6]
l3=linkedList()
l3.insertElement(array3)
#l3.printElements(l3.head)
forSortPerform.append(l3.head)#Append linkedList3
def conqure(left,Right):
    """left=left[0]
    right=Right[0]"""
    aPointer=left[0]
    bPointer=Right[0]
    
    temphead=None
    last=None
    #tempLast=None
    if aPointer.data<bPointer.data:
        node=Node(aPointer.data)
        temphead=aPointer
        last=aPointer
        aPointer=aPointer.nextReference
    elif bPointer.data>=bPointer.data:
        node=Node(bPointer.data)
        temphead=bPointer
        last=bPointer
        bPointer=bPointer.nextReference
    
    
    #else:
    while aPointer!=None and bPointer!=None:
        if aPointer.data<=bPointer.data:
            node=Node(aPointer.data)
            last.nextReference=aPointer
            last=aPointer
            aPointer=aPointer.nextReference
            last.nextReference=None
            
        elif aPointer.data>bPointer.data:
            node=Node(bPointer.data)
            last.nextReference=node
            last=node
            bPointer=bPointer.nextReference
            last.nextReference=None
        #last=last.nextReference
            

    while aPointer!=None:
        node=Node(aPointer.data)
        last.nextReference=node
        last=node
        aPointer=aPointer.nextReference
    while bPointer!=None:
        node=Node(bPointer.data)
        last.nextReference=node
        last=node
        bPointer=bPointer.nextReference
    return temphead
    #temphead.nextReference.nextReference.data)
#conqure(l1,l2)
def mergerSort(listValue):
    
    if len(listValue)<=1:#==1:
        return listValue[0]
    else:   
        
        mid=len(listValue)//2
        leftSide= listValue[:mid]
        rightSide=listValue[mid:]
        left=mergerSort(leftSide)
        right=mergerSort(rightSide)
       
    return conqure(leftSide,rightSide)
    
        
    #else:
    
        
val=[1,2,3,4,5,6,7,8,]
val=(mergerSort(forSortPerform))

forToKnow=linkedList()
forToKnow.printElements(val)
#forToKnow.printElements(Right[0])