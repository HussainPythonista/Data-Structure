s = "a"
t = "aab"

sortedS=sorted(s)
sortedT=sorted(t)

aPointer=0
bPointer=0
while aPointer<len(s) and bPointer<len(s):

    if sortedS[aPointer]==sortedT[bPointer]:
        aPointer+=1
        bPointer+=1
    else:
        print("Fuck")
        break

print("End")