import numpy as np
import sys

a, ml, result = [], 0, 0
lines = sys.stdin.readlines()
for i in lines: a.append(list(map(int, i.strip())))
a = np.array(a)

row = []
for i in a          : row.append(i)
for i in np.rot90(a): row.append(i)
for i in range(-len(a)+1, len(a[0])): row.append(np.diag(a,i))
for i in range(-len(a[0])+1, len(a)): row.append(np.diag(np.rot90(a),i))

for i in range(len(row)):
    count = 0
    for j in range(len(row[i])):
        if row[i][j] == 0:
            count = 0
            continue
        count += 1
        if count > ml:
            ml = count
            result = 1
        elif count == ml:
            result += 1

print(ml,result)