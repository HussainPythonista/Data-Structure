from stack import *
class postFix(object):
    def __init__(self):
        #PostFixAnswer =abc*+de/+
        self.preference={
            "*":2,
            "/":2,
            "+":3,
            "-":3,
            "^":1,
            "(":0,
            ")":0}
        #The peference is we use for to append and delete the value in stack which one have high priority
        self.stack=Stack()
        self.operators=["*","/","+","-","^"] 
        self.postFix=""
        
    def braces(self,index,valuesInBraces,lengthOfInfix):
        #Braces method which i'm using because i need to handle the Elements in braces
        #val=valuesInBraces

        #For Dummy Tracking index
        newIndex=0

        #Loop which i'm using for access and change the value into postfix which is in the braces
        for i in range(index,lengthOfInfix):

            #Normal Push operation in stack with some condition
            if valuesInBraces[i] in self.operators:
                #if infix[i]=="(" or infix[i]==")":
                self.stack.push(valuesInBraces[i])

            else:

                #If statement is for ignore ( ) braces
                if infix[i]=="(" or valuesInBraces[i]==")":
                    #print(infix[i])
                    pass
                else:
                    #Push operator into the stack for perform operation
                    self.postFix+=valuesInBraces[i]
            if valuesInBraces[i]==")":
                #stack.pop()
                break
        newIndex=i
        return newIndex
    def operation(self,infix):
        #For storing Operation
        
        start=0
        lengthOfInfix=len(infix)-1
        while start<=lengthOfInfix:
            if infix[start]=="(":
                print(True)
                index=self.braces(start,infix,lengthOfInfix)

                #This is i use before the method Creation
                """for i in range(start,lengthOfInfix):
                    if infix[i] in self.operators:
                        #if infix[i]=="(" or infix[i]==")":
                        self.stack.push(infix[i])
                    else:
                        if infix[i]=="(" or infix[i]==")":
                            #print(infix[i])
                            pass
                        else:
                           self.postFix+=infix[i]
                    if infix[i]==")":
                        #stack.pop()
                        break"""
                start=index

            else:
                #For to cheack the operator is exist or not
                if infix[start] in self.operators:

                        #This one is first push
                        if self.stack.isEmpty()==True:
                            #print(preference[infix[start]])
                            self.stack.push(infix[start])
                            start+=1

                        #This If Statement is for preference of current operator
                        elif self.preference[self.stack.topElement()]>self.preference[infix[start]]:
                            if infix[start]!="(" and infix[start]!=")":#For ignore Braces
                                #print(True)
                                self.stack.push(infix[start])
                            start+=1
                        else:

                            #The below condition is for check the right to left Associavity
                            if infix[start]!="^":

                                if infix[start]!="(" or infix[start]!=")":

                                    #pop the high and equal precidance operator
                                    oper=self.stack.pop()
                                    
                                    self.postFix+=oper
                            else:
                                start+=1
                else:
                    #For adding operand into the postfix Variable
                    if infix[start]!=")":
                        #Adding the operand into the postFix
                        self.postFix+=infix[start]
                    start+=1

        #The below while loop is for pop remaining elements and add to the PostFix Variable
        while stack.isEmpty()==False:
            oper=self.stack.pop()
            self.postFix+=oper
        return self.postFix
#print(postFix(infix))
post=postFix()
infix="k+l-m*n+(o^p)*w/v/u*t+q"
infix="a-b+(m^n)*(o+p)-q/r^s*t+z"
print(post.operation(infix))