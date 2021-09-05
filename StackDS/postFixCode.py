from stack import Stack


preference={"+":1,"-":1,"*":2,"/":2}
stack=Stack()

def opertation(string):
    global preference,s
    operand=["-","+","*","/"]
    postFix=""
    lastPlace=len(string)-1
    i=0
    while i<=lastPlace:
        if string[i] not in operand:
            
            postFix+=string[i]
            #print(postFix[i])
            i+=1
        else:
            if stack.isEmpty()==True:
                stack.push(string[i])
                i+=1
            elif preference[stack.bucket[stack.top]]==preference[string[i]]:
                strVal=stack.pop()
                postFix+=strVal
            else:
                stack.push(string[i])
                i+=1
                
    if stack.isEmpty()==False:
        for i in range(len(stack.bucket)):
            postFix+=(stack.pop())
    print(postFix)
needToPerform="a+b*e"
opertation(needToPerform)

#print(s.bucket)