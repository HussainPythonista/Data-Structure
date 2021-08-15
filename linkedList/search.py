import linkedList as ll
linklist=ll.linkedList()
linklist.addElement(10)
linklist.addElement(40)
linklist.addElement(60)
linklist.addElement(70)
linklist.addElement(20)
class search(object):
    def __init__(self) :
        self.first=linklist.head
    def searchElement(self,valueIWant):
        count=0
        pointer=self.first
        while pointer:
            count+=1
            if pointer.data==valueIWant:
                print("Values FOund At",count)
            
            pointer=pointer.nextReference
searchElement=search()
searchElement.searchElement(10)
        