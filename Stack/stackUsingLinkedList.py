


print("Hello world")

#I'm going to implement the Stacks using Linked List

#In Stacks the Elements are inserted and deleted in same end

class Node(object):
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class Stack(object):
    def __init__(self):
        self.head=None#head is use for tracking head
        #As memory Purpose I did initialize self.top
        self.top=None#Top use for to track which value in top

    def push(self,valForPush):
        value=valForPush
        #In Stack we perform push operation in InserfFirst Method
        if self.head==None:
            node=Node(value)
            self.head=node
            self.top=node
        else:
            node=Node(value)
            node.next=self.head
            self.top=node
            self.head=node
    
    def pop(self):
        #This Pop Function works in Last in First Out Principle
        
    
    def printValue(self):
        if self.head==None:
            print("No elements to print")
        else:
            printVal=""
            pointer=self.head
            while pointer:
                printVal+=str(pointer.val)+"-->"
                pointer=pointer.next
            print(printVal)

stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.printValue()


