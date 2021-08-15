from linkedList import *

#Load the data

circular=linkedList()

circular.addElement2(10)
circular.addElement2(20)
circular.addElement2(30)
circular.addElement2(40)
circular.addElement2(50)
circular.addElement2(60)
circular.addElement2(70)
circular.addElement2(80)
circular.addElement2(90)
circular.addElement2(100)
def createCircularLinkedList(head):
    #Create circular linkedlist
    forRemember=head
    circular.last.nextReference=head
    pointer=head
    while pointer!=None:
        print(pointer.data)
        if pointer.nextReference==forRemember:
            
            pointer.nextReference=None
        pointer=pointer.nextReference
head=circular.head

#createCircularLinkedList(circular.head)
#Circular Linked List by Recursion
needToStop=0
def byRecursion(head,p):
    global needToStop
    if needToStop==0 or p!=head:
       
        needToStop=1
        print(p.data)
        #p=p.nextReference
        byRecursion(circular.head,p.nextReference)
    needToStop=0
def countNum(head):
    count=0
    pointer=head
    while pointer:
        count+=1
        pointer=pointer.nextReference
    return count-1
#print(countNum(circular.head))
def delete(head,index):
    if index-1==0:
        temp=head.nextReference
        head.nextReference=None
        circular.head=temp
   
    else:
        pointer=head
        count=0
        while pointer:
            count+=1
            #print(pointer.data)
            if count+1==index:

                temp=pointer.nextReference
                #print(temp.nextReference.data)
                #print(temp.data)
                pointer.nextReference=temp.nextReference

            
            pointer=pointer.nextReference
            
    createCircularLinkedList(circular.head)
def insertValueInCircular(head,index,value):
    if index==0:
        temp=head
        node=Node(value)
        node.nextReference=temp
        head=node
    elif index==countNum(circular.head):
        node=Node(value)
        node.nextReference=head
        circular.last=node
        #print(circular.last.nextReference.data)
        #print(node.nextReference.data)
    pointer=head
    count=0
    while pointer:
        count+=1
        if count==index:
            node=Node(value)
            node.nextReference=pointer.nextReference
            pointer.nextReference=node
            break
        
        pointer=pointer.nextReference
    #print(head.nextReference.nextReference.nextReference.nextReference.nextReference.nextReference.nextReference.nextReference.nextReference.data)
    #circular.printElements(head)
    #createCircularLinkedList(head)
index=1
delete(circular.head,index)



