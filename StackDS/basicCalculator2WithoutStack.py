def calculator(s):
    resultIWant=0
    lastNumberISaw=0
    currentNumberImWorkingWith=0
    operator="+"
    for i in range(len(s)):
        if s[i].isdigit()==True:
            #print(s[i])
            currentNumberImWorkingWith=currentNumberImWorkingWith*10+int(s[i])
        if s[i].isdigit()==False or i==len(s)-1:
            #print(s[i])
            if operator=="+":
                resultIWant+=lastNumberISaw
                lastNumberISaw=currentNumberImWorkingWith
            elif operator=="-":
                resultIWant+=lastNumberISaw
                lastNumberISaw=-currentNumberImWorkingWith
            elif operator=="*":
                resultIWant+=currentNumberImWorkingWith*lastNumberISaw
                lastNumberISaw=0
            elif operator=="/":
                resultIWant+=lastNumberISaw//currentNumberImWorkingWith
                lastNumberISaw=0
            operator=s[i]
            currentNumberImWorkingWith=0
            #print(lastNumberISaw)
    resultIWant+=lastNumberISaw
    print(resultIWant)

s="2*3+3/3"
print(calculator(s))