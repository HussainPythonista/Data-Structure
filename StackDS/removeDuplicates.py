#removing Letters in sequence of string 
from stack import *
def findLastIndexOfString(s):
    stack = []
    seen = []
    last_occurance = {}
    for i in range(len(s)):
        last_occurance[s[i]] = i
    
    #print(last_occurance)
    
    for i, ch in enumerate(s):
        if( ch in stack ):
            continue
        else:
            while( stack and  stack[-1]>ch  and last_occurance[stack[-1]] > i ):
                stack.pop()
                #seen.remove(removed_char)
            #seen.append(ch)
            stack.append(ch)
            #print(seen,stack)
        # print(stack)
    return ''.join(stack)

string="cbcacdbc"
print(findLastIndexOfString(string))
