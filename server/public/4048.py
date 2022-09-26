import numpy as np
L = []
i, accu, count, accucount, temp = 0, 0, 0, 0, 0

while True:
    try:
        a = list(input())
        if a == []: break
        L.append(a)
        i += 1
        j = len(a)
    except EOFError:
        break
        
matrix = np.array(L)

def endtemp(count):
    global temp
    if count == 1:
        if temp == 0:
            temp = 1
            return True
        else: return False
    else:
        temp = 0
        return True
    
def ending(count):
    global accu, accucount, temp
    if count > accu: 
        accu = count
        accucount = 1
        temp = 1
    elif endtemp(count) == True and count == accu and count != 0: accucount += 1   

def right(x, y, count):
    if matrix[x][y] == '1':
        count += 1
        if y + 1 < j: right(x, y + 1, count)
        else: ending(count)
    else:
        ending(count)
        
def down(x, y, count):
    if matrix[x][y] == '1':
        count += 1
        if x + 1 < i: down(x + 1, y, count)
        else: ending(count)
    else:
        ending(count)
        
def rdown(x, y, count):
    if matrix[x][y] == '1':
        count += 1
        if x + 1 < i and y + 1 < j: rdown(x + 1, y + 1, count)
        else: ending(count)
    else:
        ending(count)
        
def ldown(x, y, count):
    if matrix[x][y] == '1':
        count += 1
        if x + 1 < i and y - 1 >= 0: ldown(x + 1, y - 1, count)
        else: ending(count)
    else:
        ending(count)
        
for x in range(i):
    for y in range(j):
        right(x, y, count)
        down(x, y, count)
        rdown(x, y, count)
        ldown(x, y, count)
        
print(accu, accucount)
