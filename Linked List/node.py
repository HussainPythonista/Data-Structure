  
    
    
    
def revesrseLinkedList(self):
        pointer=self.head
        prev=None
        while pointer:
            current=pointer.nextReference
            pointer.nextReference=prev
            prev =pointer
            pointer=current
        self.head=prev
    
def insertValueInSortedList(self,valueNeedToAdd):
        #Below is ONE METHOD
        if self.head==None:
            print("There is Node For Search and Add To it")
        elif self.head.data>valueNeedToAdd:
            self.addElementsBegin(valueNeedToAdd)
        elif self.last.data<valueNeedToAdd:
                self.last.nextReference=Node(valueNeedToAdd)
        else:
            
            pointer=self.head
            while pointer.nextReference:
                if pointer.nextReference.data>valueNeedToAdd:
                    node=Node(valueNeedToAdd)
                    node.nextReference=pointer.nextReference
                    pointer.nextReference=node
                    
                    break
                pointer=pointer.nextReference
            
        
        #ANOTHER METHOD

        pointer=self.head
        prevPointer=None
        while pointer:
            prevPointer=pointer
            if prevPointer.data<valueNeedToAdd and  pointer.nextReference.data>valueNeedToAdd:
                node=Node(valueNeedToAdd)
                node.nextReference=pointer.nextReference
                prevPointer.nextReference=node

            
            pointer=pointer.nextReference

