from linkedList import *


listValue=[1,2,3,4,5]
 
ll=linkedList()
ll.insertElement(listValue)

nowHead=ll.head

def count(head):
    pointer=head
    count=1
    while pointer.nextReference:
        count+=1
        pointer=pointer.nextReference
    return count

def initializAtMiddle(head):
    forMid=count(head)
    midValue=forMid//2
    
    pointer=head
    c=0#For equalize mid and running Pointer
    while pointer:
        
        if c==midValue:
            print(pointer.data)
            return pointer
        pointer=pointer.nextReference
        c+=1

#By Hare and Tortoise Algorithm


#It is fast and memory Efficient
def findMiddle(head):
    hare=head#For Fast Move
    tortoise=head#For Slow Move
    while hare and hare.nextReference:
    #Because we dont have only even and odd number we get both
        #Tortoise jumps one pointer at a time
        tortoise=tortoise.nextReference
        #Hare Jumps Two pointer At a time
        hare=hare.nextReference.nextReference#
        
        #data=tortoise.data
        #return
    #print(data)
    #return tortoise.data
print(findMiddle(nowHead))
