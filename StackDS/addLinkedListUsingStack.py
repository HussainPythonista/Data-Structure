import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from stack import *
from linkedList.linkedList import *

ll=linkedList()

def addTwoNumbers(head1,head2):
    aPointer=head1
    bPointer=head2
    aPointerStack=[]
    bPointerStack=[]
    #print(aPointer.data)
    while aPointer:
        aPointerStack.append(aPointer)
        aPointer=aPointer.nextReference
    
    while bPointer:
        bPointerStack.append(bPointer)
        bPointer=bPointer.nextReference
    answerStack=[]
    carry=0
    while aPointerStack and bPointerStack:
        addition=aPointerStack.pop().data+bPointerStack.pop().data+carry
        carry=addition//10
        
        answerStack.append(addition%10)
    
    while aPointerStack:
        remaining=aPointerStack.pop().data+carry
        carry=remaining//10
        answerStack.append(remaining%10)
    while bPointerStack:
        remaining=bPointerStack.pop().data+carry
        carry=remaining//10
        answerStack.append(remaining%10)
    if carry!=0:
        answerStack.append(carry)
    answerLinkedList=linkedList()
    for i in range(len(answerStack)):
        answerLinkedList.addElement(answerStack.pop())
    
    ll.printElements(answerLinkedList.head)

head1=linkedList()
head2=linkedList()

head1.addElement(0)


head2.addElement(7)
head2.addElement(3)


addTwoNumbers(head1.head,head2.head)