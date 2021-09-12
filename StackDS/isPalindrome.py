#For importing the file from nextFolder


import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from stack import *

from linkedList.linkedList import linkedList
stack=Stack()
def isPalindromeOrNot(head):
    pointer=head
    while pointer:
        stack.push(pointer)

        pointer=pointer.nextReference
    
    aPointer=head
    while aPointer:
        if aPointer.data==stack.topElement().data:
            stack.pop()
        else:
            return False
        aPointer=aPointer.nextReference
    if stack.isEmpty()==True:
        return True
    #else:
        

if __name__=="__main__":
    linkedlist=linkedList()
    #linkedlist.addElement(1)
    #linkedlist.addElement(2)
    #linkedlist.addElement(2)
    #linkedlist.addElement(1)
    print(isPalindromeOrNot(linkedlist.head))
