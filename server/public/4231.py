import sys
import numpy as np

a = [list(map(int,list(i.strip()))) for i in sys.stdin.readlines()]
a = np.array(a)

max_count = 0
li = []
count = 0

#행 탐색
for k in range(len(a)):
    for i in range(len(a[0])):
        if a[k][i] == 1:
            count += 1
        else:
            max_count = count
            li.append(max_count)
            count = 0
        if i == len(a[0])-1:
            max_count = count
            li.append(max_count)
            count = 0


#열 탐색
for i in range(len(a[0])):
    for k in range(len(a)):
        if a[k][i] == 1:
            count += 1
        else:
            max_count = count
            li.append(max_count)
            count = 0
        if k == len(a)-1:
            max_count = count
            li.append(max_count)
            count = 0


#대각선 오른쪽 탐색
b = []
for i in range(len(a[0])):
    b.append(np.diag(a, i))

for i in range(len(a)-1):
    b.append(np.diag(a, -i-1))

for i in range(len(b)):
    for k in range(len(b[i])):
        if b[i][k] == 1:
            count += 1
        else:
            max_count = count
            li.append(max_count)
            count = 0
        if k == len(b[i])-1:
            max_count = count
            li.append(max_count)
            count = 0



#대각선 왼쪽 탐색
for i in range(len(a)):
    a[i] = a[i][::-1]

c = []

for i in range(len(a[0])):
    c.append(np.diag(a, i))

for i in range(len(a)-1):
    c.append(np.diag(a, -i-1))

for i in range(len(c)):
    for k in range(len(c[i])):
        if c[i][k] == 1:
            count += 1
        else:
            max_count = count
            li.append(max_count)
            count = 0
        if k == len(c[i])-1:
            max_count = count
            li.append(max_count)
            count = 0


print(max(li),li.count(max(li)))