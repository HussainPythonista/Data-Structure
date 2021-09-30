
def decode(string):
    decoded=""
    
    #else:
    stack=[["","1"]]
    i=0
    previous=1
    digit=0
    while i <len(string):
    #for i in range(len(string)):
        
        if string[i].isdigit()==True:
            digit=digit*10+int(string[i])
            
        if string[i]=="[":
            previous=digit
            stack.append(["",previous])
            digit=0
            previous=1
        elif string[i].isalpha() :
            stack[-1][0]+=string[i]
        if string[i]=="]":
            popedElement=stack.pop()
            multiplied=popedElement[0]*int(popedElement[1])
            stack[-1][0]+=multiplied

        #print(stack)
        
        i+=1
    return(stack[0][0]*int(stack[0][1]))
    #print(decoded)
string="100[leetcode]"

print(decode(string))
#print(2*"a")