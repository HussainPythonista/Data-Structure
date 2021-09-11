from stack import *


stack=Stack()
s = "bcabc"

def removeDuplicates(s):
    frequency={}
    for i in range(len(s)):
        if s[i] in frequency:
            frequency[s[i]]+=1
        else:
            frequency[s[i]]=1
    trackingList=[]
    for i in range(len(s)):

        if stack.isEmpty()==True:
            trackingList.append(trackingList)
            stack.push(s[i])
        else:
        
            #else:
                if stack.topElement()<s[i]:
                    #print(s[i])

                    if s[i] not in stack.bucket:

                        trackingList.append(s[i])
                        #print(s[i])
                        stack.push(s[i])
                elif frequency[stack.topElement()]==1:
                    stack.push(s[i])
                        
                else:
                    
                    if frequency[stack.topElement()]>0:
                        poped=stack.pop()
                        if frequency[poped]>1:
                            frequency[poped]-=1
                            stack.push(s[i])
                        else:
                            stack.push(poped)
                    #if s[i] in stack.bucket:
                    

    print(frequency)
print(removeDuplicates(s))
print(stack.bucket)