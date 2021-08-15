from linkedList import *
#from node import Node
ll=linkedList()
#node=Node()
def insertBegin(data):
    newNode=Node(data)
    newNode.nextReference=ll.head
    ll.head=newNode
