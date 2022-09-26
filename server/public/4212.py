
import numpy as np
import sys


bingo = []
while True :
    line = sys.stdin.readline().strip()
    if not line : break
    bingo.append(list(map(int,line)))
bingo = np.array(bingo)


matrix = []
rows, cols = np.nonzero(bingo)
for row, col in zip(rows, cols) :
    matrix.append((row, col))


result = dict()
direction = [(0, 1), (1, 1), (1, 0), (1, -1)]
for r, c in matrix :
    for i, w in direction :
        if (r+i, c+w) in matrix and (r-i, c-w) not in matrix :
            count = 1
            mat = (r, c)
            while True :
                mat = (mat[0]+i, mat[1]+w)
                if mat in matrix : count += 1
                else : break
            if count not in result :
                result[count] = 0
            result[count] += 1


result = sorted(result.items(), key=lambda x : x[0], reverse=True)
l, k = result[0]
print(l, k)
