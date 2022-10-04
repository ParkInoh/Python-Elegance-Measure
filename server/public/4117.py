import sys
import numpy as np

a, b = [], sys.stdin.readlines()                   # input
for i in b: a.append(list(map(int, i.strip())))
a = np.array(a, dtype=np.int8)

def value(a,b,c):                                  # calculate
    if a > b:
        b = a; c = 1
    elif a == b:
        c += 1
    return a,b,c

def solve(a,cmp,ans):
    n, m, ad = a.shape[0], a.shape[1], []          # ad: matrix_a + matrix_diagonal
    for i in range(len(a)): ad.append(list(a[i]))
    for i in range(n)     : ad.append(list(np.diag(a, k = -i)))
    for i in range(1, m)  : ad.append(list(np.diag(a, k = i)))

    for i in range(len(ad)):                       # Row search
        cnt = 0
        for j in range(len(ad[i])):
            if ad[i][j] == 0: cnt = 0; continue
            cnt += 1
            cnt,cmp,ans = value(cnt,cmp,ans)

    return cmp, ans

cmp, ans = solve(a,0,0); a = np.rot90(a)           # main
cmp, ans = solve(a,cmp,ans)

if cmp == 1: b = ''.join(b); ans = b.count('1')    # exception (cmp == 1)

print(cmp,ans)                                     # output