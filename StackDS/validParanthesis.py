from stack import *

stack=Stack()
def correctBrace(comingParanthesis,popped):
    matchPara={
    "}":"{",
    "]":"[",
    ")":"("
    }
    return matchPara[popped]==comingParanthesis

def validParanthesis(paranthesis):
    global stack
    para=paranthesis
    
    openParanthesis=["{","[","("]
    closeParanthesis={"}","]",")"}
    for i in range(len(para)):
        if para[i] in openParanthesis:
            stack.push(para[i])
        if para[i] in closeParanthesis:
            popedVal=stack.pop()
            #print(popedVal,para[i])
            if correctBrace(popedVal,para[i])==True:
                pass
            else:
                return False
    if stack.isEmpty()==True:
        return True
    else:
        return False
    
paranthesis="([])"
print(validParanthesis(paranthesis))