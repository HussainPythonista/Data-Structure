from stack import *

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
pushed =[2,1,0]
popped = [1,2,0]
stack=Stack()
def stackSequence(pushed,poped):
    global stack
    pushedPointer=0
    poppedPointer=0
    length=len(pushed)-1
    finished=False
    while pushedPointer<=length:
        #print(pushed[pushedPointer])
        stack.push(pushed[pushedPointer])
        pushedPointer+=1
        while stack.isEmpty()==False and stack.topElement()==poped[poppedPointer]:
            stack.pop()
            poppedPointer+=1
        
    if stack.isEmpty()==True:
        print(True)
    else:
        return False
    
print(stackSequence(pushed,popped))
