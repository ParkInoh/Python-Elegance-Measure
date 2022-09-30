import numpy as np

raw = []

while True:
    try:
        raw.append(list(map(int,list(input()))))
    except:
        break

arr = np.array(raw)

L = 0
lenlist = []




for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
            L += 1
        else:
            if L != 0:
                lenlist.append(L)
                L = 0
    if L != 0:
        lenlist.append(L)
        L = 0


for j in range(len(arr[0])):
    for i in range(len(arr)):
        if arr[i][j] == 1:
            L += 1
        else:
            if L != 0:
                lenlist.append(L)
                L = 0
    if L != 0:
        lenlist.append(L)
        L = 0


for x in range(len(arr[0])):
    y = 0
    while x <= len(arr[0])-1 and y <= len(arr)-1:
        if arr[y][x] == 1:
            L += 1
        else:
            if L != 0:
                lenlist.append(L)
                L = 0
        x += 1
        y += 1
    if L != 0:
        lenlist.append(L)
        L = 0

for y in range(1, len(arr)):
    x = 0
    while x <= len(arr[0])-1 and y <= len(arr)-1:
        if arr[y][x] == 1:
            L += 1
        else:
            if L != 0:
                lenlist.append(L)
                L = 0
        x += 1
        y += 1
    if L != 0:
        lenlist.append(L)
        L = 0


for x in range(len(arr[0])):
    y = 0
    while x >= 0 and y <= len(arr)-1:
        if arr[y][x] == 1:
            L += 1
        else:
            if L != 0:
                lenlist.append(L)
                L = 0
        x -= 1
        y += 1
    if L != 0:
        lenlist.append(L)
        L = 0

for y in range(1, len(arr)):
    x = len(arr[0]) - 1
    while x <= len(arr[0])-1 and y <= len(arr)-1:
        if arr[y][x] == 1:
            L += 1
        else:
            if L != 0:
                lenlist.append(L)
                L = 0
        x += 1
        y += 1
    if L != 0:
        lenlist.append(L)
        L = 0










print(max(lenlist),lenlist.count(max(lenlist)) )