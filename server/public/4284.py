import numpy
import sys

def sero (a,b) :
    length = 1
    while a+2 <= UD :
        if L[a+1][b] == "1" :
            length += 1
            a      += 1
        else : break
    return(length)

def garo (a,b) :
    length = 1
    while b+2 <= LR :
        if L[a][b+1] == "1" :
            length += 1
            b      += 1
        else : break
    return(length)

def daegak1 (a,b) :
    length = 1
    while (a+2 <= UD) and (b+2 <= LR) :
        if L[a+1][b+1] == "1" :
            length += 1
            a += 1
            b += 1
        else : break
    return(length)

def daegak2 (a,b) :
    length = 1
    while (a+2 <= UD) and (b-1 >= 0) :
        if L[a+1][b-1] == "1" :
            length += 1
            a += 1
            b -= 1
        else : break
    return(length)

lines = []

inp = sys.stdin.readlines()
for w in inp :
    w = w.strip()
    ww = w.split()
    lines.append(ww[0])

LR = len(lines[0])
UD = len(lines)
mynum = numpy.zeros(shape=(UD,LR))
long = [0]

Llist=[]
for w in lines :
    Llist.append( list(w))

L = numpy.array(Llist)


for w in range(LR) :
    for i in range(UD) :
        if L[i][w] == "1" :
            L1 = garo(i,w)
            if   L1  > long[0] : long = [L1]
            elif L1 == long[0] : long.append(L1)
            L2 = sero(i,w)
            if   L2  > long[0] : long = [L2]
            elif L2 == long[0] : long.append(L2)
            L3 = daegak1(i,w)
            if   L3  > long[0] : long = [L3]
            elif L3 == long[0] : long.append(L3)
            L4 = daegak2(i,w)
            if   L4  > long[0] : long = [L4]
            elif L4 == long[0] : long.append(L4)

print(long[0], len(long))



