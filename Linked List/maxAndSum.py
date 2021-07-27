
from linkedList import *

ll.addElement(30)
ll.addElement(10)
ll.addElement(60)
ll.addElement(40)

class someOperations(object):
    def maxValue(self,head):
        maxVal=0
        while head!=None:
            if maxVal<head.data:
                maxVal=head.data
            head=head.nextReference
            
        return maxVal

    #Sum Of all Nodes
    def sumOfValues(self,head):
        sumVal=0
        pointer=head
        while pointer:
            sumVal+=pointer.data
            pointer=pointer.nextReference
        return sumVal
    
operations=someOperations()
print(operations.maxValue(ll.head))
print(operations.sumOfValues(ll.head))
