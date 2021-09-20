def dequeTheStringPattern(string):
    stack=[["","1"]]
    i=0
    previous=1
    while i <len(string):
    #for i in range(len(string)):
        
        if string[i].isdigit()==True:
            
            previous=string[i]
            #stack.append(["",f"{string[i]}"])
            #print(previous)
        elif string[i]=="[":
            stack.append(["",f"{previous}"])
            #j=i
            #tempString=""
            previous=1
        elif string[i].isalpha():
            tempPointer=i
            tempString=""
            while string[tempPointer]!="]" and string[i].isdigit()==False:
                tempString+= string[tempPointer]
                
                tempPointer+=1
            stack[-1][0]=tempString
            tempString=""
           # print(tempString)
        i+=1
    print(stack)
string="3[[a]2[bc]]"
dequeTheStringPattern(string)

#print(2*"a")