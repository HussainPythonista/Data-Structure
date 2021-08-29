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
        if self.top<self.stackSize-1:
            self.top+=1
            self.bucket.append(value)
        else:
            print("StackOverFlow")
            print("You need to pop some values to add new Values")

    def pop(self):
        #We use Pop function, for take out value from top in the bucket

        if self.top==0:

            print("StackUnderFlow")
            print("There is No element for pop")
       
        self.bucket.pop()
        self.top-=1
    def isEmpty(self):
        if self.top==-1:
            print(True)
        else:
            print(False)
    
    def isFull(self):
        if self.top==self.stackSize-1:
            print(True)
        else:
            print(False)

    def peek(self,index):
        #We use Peek for Accesing Element
        newIndex=self.top-index+1
        if  newIndex<self.stackSize and newIndex>=0:

            print(self.bucket[newIndex],""+"is Found")
        else:
            print("You game me a Out of Index")
stack=Stack(5)
stack.push(10)
stack.push(20)
stack.push(15)
stack.push(20)
stack.push(15)
#stack.peek(2)
stack.peek(8)


