#This File Majorly i have focus on Create Stack class and working with that

class Stack(object):
    #Stack has major ADT(Abstact Data Type)
    def __init__(self,stackSize=None):

        #stackSize describes how much data should stack contain
        #If the bucket size is Full then we could not push the Value Into it
        self.stackSize=stackSize

        #The Stack which i named as bucket we should consider stack memory is like bucket
        #When we push some balls in bucket we cannot take the ball which we was Push inside the bucket
        #We should take out all the balls stays before the first ball,thenonly we take the first ball
        self.bucket=[]
        #Top Variable which i use for track the top element in Bucket 
        self.top=-1

    def push(self,value):
        #This function I use for to add values in bucket
        #this one is works in Last In First Out Mechanism
        if self.stackSize!=None:
            if self.top<self.stackSize-1:
                self.top+=1
                self.bucket.append(value)
            else:
                print("StackOverFlow")
                print("You need to pop some values to add new Values")
        else:
            self.top+=1
            self.bucket.append(value)

    def pop(self):
        #We use Pop function, for take out value from top in the bucket

        if self.top==-1:

            return ("StackUnderFlow")
            #return ("There is No element for pop")
       
        
        self.top-=1
        return self.bucket.pop()
    def isEmpty(self):
        if self.top==-1:
            return (True)
        else:
            return (False)
    
    def isFull(self):
        if self.stackSize!=None:
            if self.top==self.stackSize-1:
                print(True)
            else:
                print(False)
        else:
            return None

    def peek(self,index):
        #We use Peek for Accesing Element
        newIndex=self.top-index
        if  newIndex<self.stackSize and newIndex>=0:

            return (self.bucket[newIndex],""+"is Found")
        else:
            #("You game me a Out of Index")
            return None
    
    def topElement(self):
        #tHis method returns the top most element in stack
        if self.top==-1:
            return None
        else:
            return self.bucket[-1]

stack=Stack(5)
#stack.push(10)
#stack.push(12)
#stack.push(15)
#stack.push(20)
#stack.push(7)
