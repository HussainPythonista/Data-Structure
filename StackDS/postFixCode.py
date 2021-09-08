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
#infix="a-b+(m^n)*(o+p)-q/r^s*t+z"
def postFix(infix):
    global preference,stack,operators
    
    postFix=""
    start=0
    lengthOfInfix=len(infix)-1

    while start<=lengthOfInfix:
        if infix[start]=="(":
            for i in range(start,lengthOfInfix):
                if infix[i] in operators:
                    #if infix[i]=="(" or infix[i]==")":
                    stack.push(infix[i])
                else:
                    if infix[i]=="(" or infix[i]==")":
                        #print(infix[i])
                        pass
                    else:
                        postFix+=infix[i]
                if infix[i]==")":
                    #stack.pop()
                    break
            
            start=i

            
        else:
            
            if infix[start] in operators:
                    if stack.isEmpty()==True:
                        #print(preference[infix[start]])
                        stack.push(infix[start])
                        start+=1
                    elif preference[stack.topElement()]>preference[infix[start]]:
                        if infix[start]!="(" and infix[start]!=")":
                            #print(True)
                            stack.push(infix[start])
                        start+=1
                    else:
                        if infix[start]!="^":
                            if infix[start]!="(" or infix[start]!=")":

                                oper=stack.pop()
                                #print(oper)
                            #print(oper)
                            #if  infix[start]!="(" and infix[start]!=")":
                                postFix+=oper
                        else:
                            start+=1
            else:
                if infix[start]!=")":
                    
                    postFix+=infix[start]
                start+=1
    while stack.isEmpty()==False:
        oper=stack.pop()
        postFix+=oper
    return postFix
print(postFix(infix))