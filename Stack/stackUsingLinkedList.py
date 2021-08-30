print("Hello world")

#I'm going to implement the Stacks using Linked List

#In Stacks the Elements are inserted and deleted in same end

class Node(object):
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class stack(object):
    def __init__(self):
        self.head=None#head is use for tracking head
        #As memory Purpose I did initialize self.top
        self.top=None#Top use for to track which value in top

    def push(self,valForPush):
        value=valForPush
        #In 

