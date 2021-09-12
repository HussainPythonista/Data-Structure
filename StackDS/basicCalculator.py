from stack import *

polynomial = "(1+(4+5+2)-3)+(6+8)"
stack=Stack()
miniStack=Stack()
def basicCalculator(polynomial):
    s=polynomial
    global stack,miniStack
    operators=["+","-"]
    i=0
    while i<len(s)-1:
        #print(s[i])
        if s[i]=="(" or s[i]==")":
            #pass
            i+=1
        else:
            if s[i] not in operators:
                stack.push(s[i])
                i+=1
            #else:
            if s[i]=="-" and len(stack.bucket)==1:
                miniStack.push(s[i])
                i+=1
            elif s[i]=="+" and len(stack.bucket)==1:
                miniStack.push(s[i])
                i+=1
            if len(stack.bucket)>=2:
                val2=stack.pop()
                val1=stack.pop()
                popedVal=miniStack.pop()
                if popedVal=="+":
                    operation=int(val1)+int(val2)
                    stack.push(operation)
                if popedVal=="-":
                    operation=int(val1)-int(val2)
                    stack.push(operation)
basicCalculator(polynomial)
#print(miniStack.bucket)
print(stack.bucket)