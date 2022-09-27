import numpy as np

se = []

while True:
    try:
        se.append(list(map(int, input().strip())))
    except:
        break

se = np.array(se, dtype='i1')

n, m, L, number = se.shape[0], se.shape[1], 0, 0


for x in range(m):
    cnt = 0
    for y in range(n):
        if se[y][x] == 0:
            cnt = 0; continue
        cnt += 1
        if cnt > L:
            L = cnt;
            number = 1
        elif cnt == L:
            number += 1

for i in range(n):
    cnt = 0
    for j in range(m):
        if se[i][j] == 0:
            cnt = 0; continue
        cnt += 1
        if cnt > L:
            L = cnt;
            number = 1
        elif cnt == L:
            number += 1

d = []

for a in range(1, m):
    d.append(list(np.diag(se, k = a)))
for a in range(n):
    d.append(list(np.diag(se, k = -a)))

es = se[::-1]
for a in range(1, m):
    d.append(list(np.diag(es, k = a)))
for a in range(n):
    d.append(list(np.diag(es, k = -a)))

for a in range(len(d)):
    cnt = 0
    for b in range(len(d[a])):
        if d[a][b] == 0:
            cnt = 0; continue
        cnt += 1
        if cnt > L:
            L = cnt;
            number = 1
        elif cnt == L:
            number += 1

if L == 1:
    se = ''.join(lines)
    number = se.count('1')

print(L, number)