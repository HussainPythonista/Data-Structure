def calculator(s):
    num=0
    stack=[]
    sign=1
    result=0
    hit=False
    for i in range(len(s)):
        if s[i].isdigit()==True:
            num=num*10+int(s[i])
            #print(num)

        
        #print(num)
        else:
            if s[i] in "+-" or num!=0:
                #num=0
                hit=True
                result+=num*sign
                sign=1 if s[i]=="+" else -1

                num=0 
            if s[i]=="(":
                stack.append(result)
                stack.append(sign)
                sign=1
                result=0
            elif s[i]==")":
                result=result*stack.pop()    
                result+=stack.pop()
                num=0
            #print(num)
            result+=num*sign
            num=0
    result += num*sign
    return result
#num
s = "321"
print(calculator(s))