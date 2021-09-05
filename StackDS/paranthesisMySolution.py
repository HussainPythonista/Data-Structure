class Stack(object):
    def __init__(self):
        self.bucket=[]
        self.top=0
    def push(self,appendVal):
        #print(appendVal)
        self.bucket.append(appendVal)
    def pop(self):
        if self.isEmpty():
            return False
        return self.bucket.pop()
       
    def isEmpty(self):
        if len(self.bucket)==0:
            return True
        return False

def matchingParanthesis(string):
    stack=Stack()
    for i in range(len(string)):
        if string[i]=="(" or string[i]=="{" or string[i]=="[":
            stack.push(string[i])
        elif string[i]==")" or string[i]=="}" or string[i]=="]":
            if stack.pop()==False:
               return False
    if stack.isEmpty():
        return True
    else:
        return False
string="[a+b]*(x+2y)*{gg+kk}"
print(matchingParanthesis(string))
