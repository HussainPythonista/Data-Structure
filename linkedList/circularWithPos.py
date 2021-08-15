from linkedList import *

ll=linkedList()
listValue=[]

ll.insertElement(listValue)

def createCircle(listToCircle,last,position):
    pointer=listToCircle
    count=0
    circle=None
    while pointer:
        #print(pointer.data)
        if count==position:
            circle=pointer
        pointer=pointer.nextReference
        count+=1
    last.nextReference=circle
head=ll.head
last=ll.last
position=-1
createCircle(head,last,position)


def isHasCircle(circleList):
    pointer=circleList
    memoization=[]
    while pointer:
        #print(memoization)
        if pointer not in memoization:
            memoization.append(pointer)
        else:
            return True
            #pointer.nextReference=None
            
        pointer=pointer.nextReference
    return False
    #return (memoization)
val=isHasCircle(head)
print(val)