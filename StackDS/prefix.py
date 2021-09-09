#from StackDS.postFixCode import postFix
from stack import *

preference={
    "*":2,
    "/":2,
    "+":3,
    "-":3,
    "^":1,
    "(":0,
    ")":0}
#The peference is we use for to append and delete the value in stack which one have high priority
stack=Stack()
operators=["*","/","+","-","^"] 
preFixStr=""
infix="k+l-m*n+(o^p)*w/v/u*t+q"
#infix="k^l^m^j"
def braceOperations(index,reversedInfix):
    global stack,operators,preFixStr
    for i in range(index,len(infix)):
        #print(reversedInfix[i])
        #print(reversedInfix[i])
        if reversedInfix[i] in operators:
            stack.push(reversedInfix[i])
        else:
            if reversedInfix[i]==")" or reversedInfix[i]=="(" :
                pass
            else:
                
                preFixStr+=reversedInfix[i]
        if reversedInfix[i]=="(":
                break
    return i
def preFix(infix):
    global preference,stack,operators,preFixStr
    #preFix=""
    reversedInfix=infix[::-1]
    start=0
    lastElement=len(reversedInfix)-1
    #print(reversedInfix)
    while start<=lastElement:
       # print(reversedInfix[start])
        if reversedInfix[start]==")":
            #print(infix[start])
            #print(True)
            start=braceOperations(start,reversedInfix)
        else:
            #print("ST")
            #print(reversedInfix[start])
            if reversedInfix[start] in operators:
                if stack.isEmpty()==True:
                    stack.push(reversedInfix[start])
                    start+=1
                elif preference[reversedInfix[start]]<=preference[stack.topElement()]:
                    stack.push(reversedInfix[start])
                    start+=1
                else:
                    if reversedInfix[start]!="(" or reversedInfix[start]!=")":
                        preFixStr+=stack.pop()
            else:
                if reversedInfix[start]!="(":
                    preFixStr+=reversedInfix[start]

                start+=1
            
    while stack.isEmpty()==False:
        preFixStr+=stack.pop()
    return preFixStr[::-1]
print(preFix(infix))
print(stack.bucket)