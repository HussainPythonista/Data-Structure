from linkedList import *

firstList=linkedList()

firstList.addElement2(10)
firstList.addElement2(40)
firstList.addElement2(50)
firstList.addElement2(60)
firstList.addElement2(70)
firstList.addElement2(80)
firstList.addElement2(90)
firstHead=firstList.head
#firstList.printElements(firstHead)

secondList=linkedList()

secondList.addElement2(100)
secondList.addElement2(200)
secondList.addElement2(300)
secondList.addElement2(400)
secondList.addElement2(500)
#secondList.printElements(secondList.head)

def concadeneate(first,second):
    concate=linkedList()
    first.last.nextReference=second.head
    concate.printElements(first.head)
concadeneate(firstList,secondList)

