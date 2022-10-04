import sys, numpy

def bingo(i, j, dr, dc):
    if possible(n-i, m-j, dr, dc) == 1: return bingo_max

    while -1 < i < n and -1 < j < m:
        if mymatrix[i][j] == '1': break
        else                    : i += dr; j += dc

    if possible(n-i, m-j, dr, dc) == 1: return bingo_max

    count = 0
    while -1 < i < n and -1 < j < m:
        if mymatrix[i][j] == '1': count += 1
        else: break
        i += dr; j += dc

    if count > bingo_max[0]:
        bingo_max[0] = count; bingo_max[1] = 1
    elif count == bingo_max[0] and count != 0:
        bingo_max[1] += 1
    else: pass

    if -1 < i < n and -1 < j < m: return bingo(i, j, dr, dc)
    else                        : return bingo_max

def possible(r, c, dr, dc):
    if dr == 0:
        if c < bingo_max[0]: return 1
    elif dc == 0:
        if r < bingo_max[0]: return 1
    else                   : return 0

lines = []
while True:
    my = sys.stdin.readline().strip()
    if my == "":  break
    lines.append(my)

n = len(lines)
m = len(lines[0])
mynum = numpy.zeros(shape=(n, m))

L = []
for w in lines:
    L.append(list(w))

mymatrix = numpy.array(L)
bingo_max = [0, 0]

# 세로 비교
for j in range(m):
    res = bingo(0, j, 1, 0)

# 가로 비교
for i in range(n):
    res = bingo(i, 0, 0, 1)

# 대각선(오른쪽위->왼쪽아래)
for j in range(bingo_max[0]-1, m):
    res = bingo(0, j, 1, -1)
for i in range(1, n-bingo_max[0]+1):
    res = bingo(i, m-1, 1, -1)

# 대각선(왼쪽위->오른쪽아래)
for j in range(m-bingo_max[0], -1, -1):
    res = bingo(0, j, 1, 1)
for i in range(1, n-bingo_max[0]+1):
    res = bingo(i, 0, 1, 1)

print(bingo_max[0], bingo_max[1])