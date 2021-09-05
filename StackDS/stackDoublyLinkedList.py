#This is My Approach for Creating Stack which is Everything in O(1) Complexity

class Node(object):
    def __init__(self,data,next=None,prevRef=None):
        self.data=data
        self.nextRef=next
        self.prevRef=prevRef
class StackLinkList(object):

    def __init__(self):
        #The bucket Which I'm Useing is for accessing the value in Fast
        #Because Accessing the Element in Dictionary take O(1) complexity
        self.address={}
        self.top=None
        self.head=None
        self.last=None
        self.lastPrev=None
        self.index=0
    
    def push(self,valueToPush):
        #Push is performed in O{1}
        #No need to worry about Complexity
        #If Nothing in head then head is the first Node
        if self.head==None:
            node=Node(valueToPush)
            self.address[self.index]=node
            self.head=node
            #Here Last Node is Top Element in the Bucket
            self.last=node
            self.index+=1
        else:
            
            node=Node(valueToPush)
            #We should Track previous Element of Last Node 
            #Because the Stack is operated in Last In First Out (LIFO)
            #We need to track this Then only We can set Previous Node as Last Node
            node.prevRef=self.last
            self.last.nextRef=node
            #We Need Add the New Node in Last Next then only It will e consider as Last Element
            #Set last Node as Current Last
            self.last=node
            #This is Main Task Which is Help us to track and Access the Elements in O(1) timeComplexity
            self.address[self.index]=node
            self.index+=1
    def pop(self):
        if self.head.nextRef==None:
            self.head=None
            self.last=None
            print("None Value")
            self.address.pop(0)
            self.index-=1
            
        elif self.head==None:
            print("There is No elements To Pop")

        else:
            
            tempData=self.last.prevRef
            
            self.last.prevRef.nextRef=None
            self.last=tempData
            self.address.pop(self.index-1)
            self.index-=1

    def peek(self,index):
        print(len(self.address)-1)
        if index>len(self.address)-1:
            return "Out of Index"
        else:
          return self.address[index].data
    
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False

            
    def printValue(self):
        pointer=self.head
        printVal=""
        while pointer:
            printVal+=str(pointer.data)+"-->"
            pointer=pointer.nextRef
        print(printVal)
    
    def printBackword(self):
        if self.head==None:
            print("No Value To Print")
        else:
            
            pointer=self.last
            printVal=""
            while pointer:
                printVal+=str(pointer.data)+"<--"
                pointer=pointer.prevRef
            print(printVal)
            
stack=StackLinkList()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)




print(stack.peek(0))
stack.printValue()
stack.printBackword()
            
    

