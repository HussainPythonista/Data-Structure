import linkedList as ll
linklist=ll.linkedList()

class swapHead(object):
    def __init__(self):
        self.first=None
    def add(self,data):
        linklist.addElement(data)
        
    
        #linklist.printElements()
    def swap(self,needToSwap):
        if self.first.data == needToSwap:
            print("No Need To Swap")
        else:
            head=self.first
            pointer=self.first
            prev=None
            while pointer:
                if pointer.data==needToSwap:
                    self.first=pointer
                    prev.nextReference=pointer.nextReference
                    self.first.nextReference=head

            #This is One method
                """while pointer.nextReference:
                #point=pointer
                if pointer.nextReference.data==needToSwap:
                    temp=pointer.nextReference
                    pointer.nextReference=pointer.nextReference.nextReference
                    self.first=temp
                    self.first.nextReference=head
                    """

                prev=pointer
                pointer=pointer.nextReference
   
s=swapHead()
#s.add(10)
s.add(10)
s.add(20)
s.add(30)
s.add(40)
s.add(50)
s.first=linklist.head
s.swap(40)
linklist.printElements(s.first)
#s.printValue(s.first)
