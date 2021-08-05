#from _typeshed import BytesPath
from linkedList import *


answer=linkedList()
def addNumbers(l1,l2):
    listVal1=[]
    listVal2=[]
    #calculate length
    pointer=l1.head
    
    while pointer:
        listVal1.append(pointer.data)
        pointer=pointer.nextReference
    listVal1=listVal1[::-1]
    
    pointer=l2.head
    
    while pointer:
        listVal2.append(pointer.data)
        pointer=pointer.nextReference
    listVal2=listVal2[::-1]
    needTobeAnswer=[]
    carry=0
    while len(listVal1)>=1 or len(listVal2)>=1 or carry==1:
        if listVal1:
            carry+=listVal1.pop()
        if listVal2:
            carry+=listVal2.pop()
        print(carry)
        remaininVal=carry%10
        needTobeAnswer.append(remaininVal)
        carry=carry//10
    print(needTobeAnswer)
    
    

list1=linkedList()
list1.addElement(0)


list2=linkedList()
list2.addElement2(0)
addNumbers(list1,list2)

#answer.printElements(answer.head)