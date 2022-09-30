import sys
import numpy as np

sboard = []
while True:
    b = sys.stdin.readline()
    b= (" ".join(b)).split()
    if b == []:
        break
    sboard.append(b)

board = np.array(sboard)
row, column = board.shape
nc = nr = nd = kc = kr = kd = n = k = 0
t = ""
for i in range(row):
    for w in range(column):
        if board[i][w] == "0" or w == 0:
            if nc < len(t):
                nc = len(t)
                kc = 0
            if len(t) == nc:
                kc = kc + 1
            t = ""
        if board[i][w] == "1":
            t = t + "1"
for w in range(column):
    for i in range(row):
        if board[i][w] == "0" or i == 0:
            if nr < len(t):
                nr = len(t)
                kr = 0
            if len(t) == nr:
                kr = kr + 1
            t = ""
        if board[i][w] == "1":
            t = t + "1"
r = 0
while r > 1 - row:
    b = np.diag(board, k = r)
    for i in range(b.size):
        if b[i] == "0" or i == 0 :
            if nd < len(t):
                nd = len(t)
                kd = 0
            if len(t) == nd:
                kd = kd + 1
            t = ""
        if b[i] == "1":
            t = t + "1"
    fb = np.diag(np.fliplr(board), k = r)
    for w in range(fb.size):
        if fb[w] == "0" or w == 0:
            if nd < len(t):
                nd = len(t)
                kd = 0
            if len(t) == nd:
                kd = kd + 1
            t = ""
        if fb[w] == "1":
            t = t + "1"

    r -= 1


c = 1
while c < column - 1:
    cb = np.diag(board, k = c)
    for i in range(cb.size):
        if cb[i] == "0" or i == 0 :
            if nd < len(t):
                nd = len(t)
                kd = 0
            if len(t) == nd:
                kd = kd + 1
            t = ""
        if cb[i] == "1":
            t = t + "1"
    fc = np.diag(np.fliplr(board), k = c)
    for w in range(fc.size):
        if fc[w] == "0" or w == 0:
            if nd < len(t):
                nd = len(t)
                kd = 0
            if len(t) == nd:
                kd = kd + 1
            t = ""
        if fc[w] == "1":
            t = t + "1"
    c += 1


nl = [nc, nr, nd]
n  = max(nl)
kl = [kc, kr, kd]
for q in range(3):
    if n != nl[q]:
        kl[q] = 0
k = sum(kl)
print(n, k)

