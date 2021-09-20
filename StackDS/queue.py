#The Queue which works in first in first out approach
#Which value come first and that value will be delete first
#The Queue Properties are
# 1)Enqueue->Adding value
# 2).Dequeue->Deleting value
# 3).isFull
# 4).IsEmpty
# First and last
# #

class Queue(object):

    def __init__(self,size=None):
        self.first=-1
        self.rear=-1
        self.queue=[]#Bucket using for to store the value
        self.size=size
    def enque(self,value):
        if self.rear<self.size:
            self.queue.append(value)
            self.rear+=1
        else:
            self.isFull()
    def isFull(self):
        if self.rear==self.size:
            print("Queue is Full You should delete some Values And Add New Values")
            return True
        else:
            return False
            
    def dequeue(self):
        if self.isEmpty()==False:
            self.first+=1
            self.queue.pop(self.first)
            #self.first-=1
            self.rear-=1
        else:
            self.isEmpty()

    def isEmpty(self):
        if self.first==self.rear:
            return True
        else:
            return False
            #print("There is no elements to delete")

queue=Queue(5)
queue.enque(0)
queue.enque(1)
queue.enque(3)
queue.enque(4)
queue.enque(5)


queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue.queue)    


        
        

