import sys
import numpy as np

def horiz(i, j):
    oneSeq = 0
    while(j < col):
        if arr[i][j] == '0':
            break
        oneSeq += 1
        j += 1
    return oneSeq

def verti(i, j):
    oneSeq = 0
    while(i < row):
        if arr[i][j] == '0':
            break
        oneSeq += 1
        i += 1
    return oneSeq

def diag1(i, j):
    oneSeq = 0
    while(i < row and j < col):
        if arr[i][j] == '0':
            break
        oneSeq += 1
        i += 1; j += 1
    return oneSeq

def diag2(i, j):
    oneSeq = 0
    while(i < row and j >= 0):
        if arr[i][j] == '0':
            break
        oneSeq += 1
        i += 1; j -= 1
    return oneSeq

def res(i, j):
    result = [horiz(i, j), verti(i, j), diag1(i, j), diag2(i, j)]
    return (max(result), result.count(max(result)))

inp = []
for line in sys.stdin:
    inp.append(list(line.strip()))
arr = np.array(inp)

global row, col
row, col = arr.shape
best = [0, 0]
for i in range(row):
    for j in range(col):
        if arr[i][j] == '1':
            cur = res(i, j)
            if best[0] < cur[0]:
                best = list(cur)
            elif best[0] == cur[0]:
                best[1] += cur[1]
print(*best)