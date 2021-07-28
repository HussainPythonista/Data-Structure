import insertBegin

from linkedList import *
class insertValue(object):
    def __init__(self):
        ll=linkedList()
        self.first=ll.head
    def insert(self,index,value):
        if index==1:
            #insertBegin.insertBegin(value)
            node=Node(value)
            node.nextReference=self.first
            self.first=node
        else:
            count=0
            pointer=self.first
            while pointer:
                count+=1
                if count==index:
                    node=Node(value)
                    node.nextReference=pointer.nextReference
                    pointer.nextReference=node
                
                pointer=pointer.nextReference
    def insetElementInSortedList(self,value):
        if ll.head == None:
            #print(True)
            ll.head=Node(value)
        
        elif ll.head.data>value:
            temp=ll.head
            node=Node(value)
            node.nextReference=temp
            ll.head=node
        
        else:
            prev=None
            pointer=ll.head
            lastElement=ll.last
            while pointer:
                
                if  pointer.data>value:
                    temp=pointer
                    node=Node(value,pointer)
                    node.nextReference=temp
                    prev.nextReference=node
                    break
                if lastElement.data<value:
                   #print(lastElement.data)
                   node=Node(value)
                   lastElement.nextReference=node
                   lastElement= node

                prev=pointer
                pointer=pointer.nextReference
    def add(self,val):
        #print(val)
        ll.addElement2(val)
            
    def printVal(self,head):
        ll.printElements(head)
   


insertVal=insertValue()
ll=linkedList()
insertVal.add(10)
insertVal.add(20)
insertVal.add(30)
insertVal.insetElementInSortedList(35)
ll.printElements(ll.head)

#insertVal.printVal(ll.head)




        
