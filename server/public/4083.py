import numpy as np
import sys
def bingo(base):
    rows, columns = base.shape
    for i in range(rows):
        count = 0
        for j in range(columns):
            if j == 0:
                if base[i][j] == '1':  count = 1
            else:
                if base[i][j] == '1':
                    if base[i][j-1] == '1':
                        count += 1
                    else:
                        count = 1
                    if j+1 == columns: cnt.append((count))
                else:
                    if count > 0:
                        cnt.append((count))
                        count = 0
    for i in range(columns):
        count = 0
        for j in range(rows):
            if j == 0:
                if base[j][i] == '1': count = 1
            else:
                if base[j][i] == '1':
                    if base[j-1][i] == '1':
                        count += 1
                    else:
                        count = 1
                    if j+1 == rows: cnt.append((count))
                else:
                    if count > 0:
                        cnt.append((count))
                        count = 0
    N = -rows + 1
    M = columns
    for i in range(N, M):
        temp = np.diag(base, k=i)
        count = 0
        for j in range(len(temp)):
            if j == 0:
                if temp[j] == '1':
                    count = 1
                    if j+1 == len(temp): cnt.append((count))
            else:
                if temp[j] == '1':
                    if temp[j-1] == '1':
                        count += 1
                    else:
                        count = 1
                    if j+1 == len(temp): cnt.append((count))
                else:
                    if count > 0:
                        cnt.append((count))
                        count = 0
    base_flip = np.fliplr(base).copy()
    N = -rows + 1
    M = columns
    for i in range(N, M):
        temp = np.diag(base_flip, k=i)
        count = 0
        for j in range(len(temp)):
            if j == 0:
                if temp[j] == '1':
                    count = 1
                    if j+1 == len(temp): cnt.append((count))
            else:
                if temp[j] == '1':
                    if temp[j-1] == '1':
                        count += 1
                    else:
                        count = 1
                    if j+1 == len(temp): cnt.append((count))
                else:
                    if count > 0:
                        cnt.append((count))
                        count = 0
L = []
for x in sys.stdin.readlines():
    line = x.strip("\n")
    L.append(list(line))
base = np.array(L)
cnt = []
bingo(base)
result = {}
for x in cnt:
    if x not in result:
        result[x] = 1
    else:
        result[x] += 1
print(*(max(result), result[max(result)]))