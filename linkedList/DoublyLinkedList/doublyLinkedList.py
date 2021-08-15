#In Doubly Linked list the each node contains Previous and Next Reference
#WE can easily access the data in previous node and Next Node


class Node(object):
    def __init__(self,data,prevReference=None,nextReference=None):
        #Get data from the streams
        self.data=data

        #Reference of Previous Node
        self.prevReference=prevReference

        #Reference of Next Node
        self.nextReference=nextReference

class doublyLinkedList(object):
    def __init__(self,head=None):
        #Head is first Node
        self.head=head
    
    def insertNewNode(self,data):
        if self.head==None:

            node=Node(data)
            self.head=node
        else:
            pointer=self.head
            while pointer.nextReference:
                pointer=pointer.nextReference
            node=Node(data)
            node.prevReference=pointer
            pointer.nextReference=node
    def lastNode(self):
        pointer=self.head
        #forward=""
        while pointer.nextReference:
            
            pointer=pointer.nextReference
        return pointer
    def printForward(self):
        pointer=self.head
        forward=""
        while pointer:
            forward+=str(pointer.data)+"-->"
            pointer=pointer.nextReference
        print(forward)

    def printBackward(self):
        last=self.lastNode()
        backPointer=self.head
        backward=""
        while last:
            backward+=str( last.data)+"<--"
            last=last.prevReference
        print(backward)
