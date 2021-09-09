from stack import *

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
stack=Stack()
def stackSequence(pushed,poped):
    global stack
    pushedPointer=0
    poppedPointer=0
    length=len(pushed)-1
    while pushedPointer<=length:
        stack.push(pushed[pushedPointer])
        pushedPointer+=1
stackSequence(pushed,popped)
print(stack.bucket)