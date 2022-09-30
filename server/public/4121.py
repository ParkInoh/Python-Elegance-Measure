import numpy as np
import sys

def scan(matrix):
    for i in matrix:
        row = ''.join(i)
        row = row.split('0')
        row = list(filter(None,row))
        for j in row:
            cnt = len(j)
            len_list.append(cnt)

def case_diag(x,y,matrix):
    diag = list()
    for k in range(-x+1,y):
        diag.append(list(np.diag(matrix,k)))
    scan(diag)

My, len_list = [], []
lines = sys.stdin.readlines()
for line in lines: My.append(list(line.strip()))

My     = np.array(My)
My_rot = np.rot90(My)
n, m = My.shape[0], My.shape[1]

scan(My);     case_diag(n,m,My)
scan(My_rot); case_diag(m,n,My_rot)

longest = max(len_list)
print(longest , len_list.count(longest))