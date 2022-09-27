import sys

BG = []
while True:
    b = sys.stdin.readline().strip()
    if not b:
        break
    BG.append(list(b))

N     = len(BG[0])
M     = len(BG)
D     = N+M-1
count = []

def width(x):
    c = 0
    y = 0
    for i in range(N):
        if BG[x][y] == '1':
            c += 1
        else:
            if c != 0: count.append(c); c = 0;
        y += 1
    if c != 0: count.append(c)

def length(x):
    c = 0
    y = 0
    for i in range(M):
        if BG[y][x] == '1':
            c += 1
        else:
            if c != 0: count.append(c); c = 0;
        y += 1
    if c != 0: count.append(c)

def diagoA1(x):
    c = 0
    y = 0
    if x+1 < M:
        for i in range(x+1):
            if BG[x-y][y] == '1':
                c += 1
            else:
                if c != 0: count.append(c); c = 0;
            y += 1
        if c != 0: count.append(c)
    elif x+1 > N:
        for i in range(D-x):
            if BG[D-x-y][x-M+1+y] == '1':
                c += 1
            else:
                if c != 0: count.append(c); c = 0;
            y += 1
        if c != 0: count.append(c)
    else:
        for i in range(M):
            if BG[M-1-y][x-M+1+y] == '1':
                c += 1
            else:
                if c != 0: count.append(c); c = 0;
            y += 1
        if c != 0: count.append(c)

def diagoA2(x):
    c = 0
    y = 0
    if x+1 < N:
        for i in range(x+1):
            if BG[x-y][y] == '1':
                c += 1
            else:
                if c != 0: count.append(c); c = 0;
            y += 1
        if c != 0: count.append(c)
    elif x+1 > M:
        for i in range(D-x):
            if BG[M-1-y][x-M+y] == '1':
                c += 1
            else:
                if c != 0: count.append(c); c = 0;
            y += 1
        if c != 0: count.append(c)
    else:
        for i in range(N):
            if BG[x-y][y] == '1':
                c += 1
            else:
                if c != 0: count.append(c); c = 0;
            y += 1
        if c != 0: count.append(c)


for i in range(M): width(i)
for i in range(N): length(i)
if N >= M:
    for i in range(D): diagoA1(i)
elif N < M:
    for i in range(D): diagoA2(i)

mx = max(count)
mh = 0

for i in range(len(count)):
    if count[i] == mx: mh += 1

print(mx,mh)
