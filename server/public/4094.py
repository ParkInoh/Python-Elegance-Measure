import numpy as np

bg = []
while True:
    try:
        bg.append(input())
    except EOFError:
        break

m = len(bg[0])

b = []
for i in bg :
    b.append(list(i))

bingo = np.array(b)

n = len(bingo)

x = []

for i in range(n) :
    for j in range(m) :
        if bingo[i][j] == '1' :
            x.append([i, j])

fin = []
for i in range(len(x)) :
    j = 1
    while x[i][1] + j < m :
        if [x[i][0], x[i][1] + j] in x :
            j +=1
        else :
            break 
    fin.append(j)
    j = 1
    while x[i][0] + j < n :
        if [x[i][0] + j, x[i][1]] in x :
            j +=1
        else :
            break
    fin.append(j)
    j = 1
    while x[i][0] + j < n and x[i][1] + j < m :
        if [x[i][0] + j, x[i][1] + j] in x :
            j += 1
        else :
            break
    fin.append(j)
    j = 1
    while x[i][0] + j < n and x[i][1] - j >= 0 :
        if [x[i][0] + j, x[i][1] - j] in x :
            j += 1
        else :
            break
    fin.append(j)

a = max(fin)
b = fin.count(a)
print(a, b)