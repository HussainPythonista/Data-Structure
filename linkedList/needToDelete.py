while count!=k:
            if tempPointer.nextReference==None:
                newHead= reverse(pointer)
                pointer.nextReference=q
                return newHead
            tempPointer=tempPointer.nextReference
            count+=1
        newHead=reverse(pointer)
        pointer.nextReference=tempPointer
        q=tempPointer

    return tempVal
