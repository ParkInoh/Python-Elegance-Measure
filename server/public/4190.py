import numpy as np

def xcheck(array,ax,ay) :
    if ax >= x or ay >= y :
        return 0
    else :
        if array[ay][ax] == 1:
            ax += 1
            return xcheck(array,ax,ay) + 1
        else :
            return 0

def ycheck(array,ax,ay) :
    if ax >= x or ay >= y :
        return 0
    else :
        if array[ay][ax] == 1:
            ay += 1
            return ycheck(array,ax,ay) + 1
        else :
            return 0

def xycheck(array,ax,ay) :
    if ax >= x or ay >= y :
        return 0
    else :
        if array[ay][ax] == 1:
            ay += 1
            ax += 1
            return xycheck(array,ax,ay) + 1
        else :
            return 0
def yxcheck(array,ax,ay) :
    if ax <= 0 or ay >= y :
        return 0
    else :
        if array[ay][ax] == 1:
            ay += 1
            ax -= 1
            return yxcheck(array,ax,ay) + 1
        else :
            return 0

li1 = []

while True:
    try :
        li1.append(input())
    except : break

li2 = []
for t in range(len(li1)):
    y = li1[t]
    y = list(map(int,y))
    li2.append(y)

arr = np.array(li2)
x = arr.shape[1]
y = arr.shape[0]
length = 0
maxlen = [0,0]

for yl in range(y) :
    for xl in range(x) :
        length = xcheck(arr,xl,yl)
        if length > maxlen[0] :
            maxlen[0] = length
            maxlen[1] = 1

        elif length == maxlen[0] :
            maxlen[1] += 1

length = 0

for yl in range(y) :
    for xl in range(x) :
        length = ycheck(arr,xl,yl)
        if length > maxlen[0] :
            maxlen[0] = length
            maxlen[1] = 1

        elif length == maxlen[0] :
            maxlen[1] += 1

length = 0

for yl in range(y) :
    for xl in range(x) :
        length = xycheck(arr,xl,yl)
        if length > maxlen[0] :
            maxlen[0] = length
            maxlen[1] = 1

        elif length == maxlen[0] :
            maxlen[1] += 1

length = 0

for yl in range(y) :
    for xl in range(x) :
        length = yxcheck(arr,xl,yl)
        if length > maxlen[0] :
            maxlen[0] = length
            maxlen[1] = 1

        elif length == maxlen[0] :
            maxlen[1] += 1

text = " ".join(str(t) for t in maxlen)
print(text)