import insertBegin

from linkedList import *
class insertValue(object):
    def __init__(self):
        self.first=None
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
   


insertVal=insertValue()
ll=linkedList()
ll.addElement(10)
ll.addElement(20)
ll.addElement(30)
ll.addElement(40)
ll.addElement(50)
ll.addElement(60)
insertVal.insetElementInSortedList(5)
head=ll.head
ll.printElements(head)



#print(insertVal.first.data)



        
