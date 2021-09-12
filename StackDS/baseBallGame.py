from os import chroot
from stack import *

ops = ["5","-2","4","C","D","9","+","+"]
stack=Stack()
def baseBallGame(ops):
    global stack
    opretion=["D","C"]
    for i in range(len(ops)):
        if ops[i] in opretion:
            if ops[i]=="C":
                stack.pop()
            elif ops[i]=="D":
                topElement=stack.topElement()
                twiceElemnet=topElement*2
                stack.push(twiceElemnet)
        elif ops[i]=="+":
            val1=stack.pop()
            val2=stack.pop()
            addition=val1+val2
            stack.push(val2)
            stack.push(val1)
            stack.push(addition)
        else:
            stack.push(int(ops[i]))
        #print(65+26)
baseBallGame(ops)

print(sum(stack.bucket))