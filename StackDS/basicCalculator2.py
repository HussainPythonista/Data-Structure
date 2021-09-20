def calculate(s):
    number=[str(i) for i in range(9)]
    operator="+"
    num=0
    stack=[]
    for i in range(len(s)):
        if s[i] in number:
            #print(s[i])
            num=num*10+int(s[i])
            
        if not s[i].isdigit() or i==len(s)-1:
            if operator=="+":
                stack.append(num)
            elif operator=="-":
                stack.append(-num)
            elif operator=="/":
                divide=stack.pop()
                d=divide//num
                stack.append(d)
            elif operator=="*":
                m=stack.pop()
                multiply=m*num
                stack.append(multiply)
            num=0
            operator=s[i]

    print(sum(stack))

s="2147483647"
print(calculate(s))