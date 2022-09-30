import numpy as np

bingo = []

while True:
    try:
        bingo.append(list(map(int, input().strip())))
    except:
        break

bingo = np.array(bingo, dtype='i1')

N, M, L, num = bingo.shape[0], bingo.shape[1], 0, 0

def find(a,b,c):
    if a > b:
        b = a
        c = 1
    elif a == b:
        c += 1
    return a,b,c

for x in range(M):
    c = 0
    for y in range(N):
        if bingo[y][x] == 0:
            c = 0; continue
        c += 1
        c,L,num = find(c,L,num)

for i in range(N):
    c = 0
    for j in range(M):
        if bingo[i][j] == 0:
            c = 0; continue
        c += 1
        c,L,num = find(c,L,num)

d = []

for a in range(1, M):
    d.append(list(np.diag(bingo, k = a)))
for a in range(N):
    d.append(list(np.diag(bingo, k = -a)))

Bingo = bingo[::-1]
for a in range(1, M):
    d.append(list(np.diag(Bingo, k = a)))
for a in range(N):
    d.append(list(np.diag(Bingo, k = -a)))

for a in range(len(d)):
    c = 0
    for b in range(len(d[a])):
        if d[a][b] == 0:
            c = 0; continue
        c += 1
        c,L,num = find(c,L,num)

if L == 1:
    bingo = ''.join(lines)
    num = bingo.count('1')

print(L, num)