from stack import *

polynomial = "72147483647"
#polynomial="(1+(4+5+2)-3)+(6+8)"
#polynomial="(1 + 1)"
#polynomial=" 2-1 + 2"
#polynomial="(1)"
polynomial="-2+1"
stack=Stack()
miniStack=Stack()

def basicCalculator(polynomial):
    s=polynomial
    global stack,miniStack
    operators=["+","-"]
    i=0
    perform=False
    while i<len(s):
        #print(s[i])
        if s[i]=="(" or s[i]==")" or s[i]==" ":
            #s=s.replace(s[i],"")
            i+=1
        else:
            if s[i] not in operators :
                #print(s[i])
                stack.push(s[i])
                i+=1
            else:
                if s[i]=="-":
                    miniStack.push(s[i])
                    i+=1
                if s[i]=="+":
                    miniStack.push(s[i])
                    i+=1
                perform=True
                #print(miniStack.bucket)
            if len(stack.bucket)>=2:
                #print(True)
                val2=stack.pop()
                val1=stack.pop()
                popedVal=miniStack.pop()
                if popedVal=="+":
                    operation=int(val1)+int(val2)
                    stack.push(operation)
                if popedVal=="-":
                    operation=int(val1)-int(val2)
                    stack.push(operation)
            #print(stack.bucket)   
    if perform==True:
        return (stack.bucket)

    if perform==False:
        ans=""
        for i in range(len(s)):
            if s[i]=="(" or s[i]==")" or s[i]==" ":
                pass
            else:
                ans+=s[i]
        return ans
print(basicCalculator(polynomial))
#print(miniStack.bucket)
