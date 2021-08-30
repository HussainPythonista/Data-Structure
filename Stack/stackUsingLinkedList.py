

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

        if self.top==None or self.head==None:
            print("There is No element in Bucket to pop")
        else:
            tempHead=self.top.next
            self.top=tempHead
            self.head=tempHead

    def topValue(self):#To Know,Which elements in the Top
        if self.top==None:
            print("None")
        else:
            print(self.top.val)

    def peek(self,index):
        #Out of all function this Peek fuction is Run in O(index) Time Complexity
        returnValue=0
        if self.head==None:
            print('Nope')
        else:
            pointer=self.head
            for i in range(1,index):
                pointer=pointer.next
            returnValue= pointer.val
        print(returnValue)
    

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
    def isEmpty(self):
        #TO Know About the Stack is Empty or not
        if self.top==None:
            return True
        else:
            return False
    def isFull(self):
        #In this Case the function is Only FOr Understanding because the Linked List 
        #Is store the value is Heap Memory Because it is Dyanamic in nature
        #So This Is Only For Understanding Purpose
        """
            In This Case We should understand If cant Create the Node Then only the Heap memory Is Full
        """
        pass
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)
stack.peek(3)
stack.printValue()


