from linkedList import *

findLoop=linkedList()
findLoop.addElement2(10)
findLoop.addElement2(30)
findLoop.addElement2(40)
findLoop.addElement2(50)

findLoop.addElement2(60)
findLoop.addElement2(70)
findLoop.addElement2(80)

def isLoop(head):
    slowMove=head
    fastMove=head
    pointer=head
    lastRef=findLoop.last
    while pointer.nextReference:
        
        if pointer.nextReference.data==40:
            makeLoop=pointer.nextReference
            lastRef.nextReference=makeLoop
        elif slowMove==fastMove:
            return True
            
        pointer=pointer.nextReference
        slowMove=slowMove.nextReference
        fastMove=fastMove.nextReference.nextReference
loop=findLoop.head
print(isLoop(loop))
    

