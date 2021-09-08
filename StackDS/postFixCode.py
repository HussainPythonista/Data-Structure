from stack import *


infix="k+l-m*n+(o^p)*w/v/u*t+q"

#PostFixAnswer =abc*+de/+

preference={
    "*":2,
    "/":2,
    "+":3,
    "-":3,
    "^":1,
    "(":0,
    ")":0

}
#The peference is we use for to append and delete the value in stack which one have high priority
stack=Stack()

operators=["*","/","+","-","^"]
infix="a-b+(m^n)*(o+p)-q/r^s*t+z"
def postFix(infix):
    global preference,stack,operators
    
    postFix=""
    start=0
    lengthOfInfix=len(infix)-1

    while start<=lengthOfInfix:
        if infix[start]=="(":
            for i in range(start-1,lengthOfInfix):
                if infix[start]==")":
                    for j in range(start-1,-1,-1):
                        if infix[j] in operators:
                            poped=stack.pop()
                            postFix+=poped
                        break
                else:
                    if infix[i] in operators:
                        stack.push(infix[i])
                    else:
                        postFix+=infix[i]
                start=i

        else:
            
            if infix[start] in operators:
                if stack.isEmpty()==True:
                    #print(preference[infix[start]])
                    stack.push(infix[start])
                    start+=1
                elif preference[stack.topElement()]>preference[infix[start]]:
                    #if infix[start]!="(" and infix[start]!=")":
                        #print(True)
                    stack.push(infix[start])
                    start+=1
                else:
                    if infix[start]!="^":
                        
                        oper=stack.pop()
                        #print(oper)
                        #if  infix[start]!="(" and infix[start]!=")":
                        postFix+=oper
                    else:
                        start+=1
            else:
                postFix+=infix[start]
                start+=1
    while stack.isEmpty()==False:
        oper=stack.pop()
        postFix+=oper
    return postFix
print(postFix(infix))