import numpy as np
import sys

Data = sys.stdin.read().splitlines()

Datas=[0]*len(Data)
for i in range(len(Data)):
    Datas[i]=list(map(int,Data[i]))
B = np.array(Datas)
XL = len(B[0])
YL = len(B)
BL=[]

def Init():
    N = 0
    L = []
    return (N, L)

def SUM(N, D, L) :
    N += D
    if (D == 0) & (N > 0):
        L.append(N)
        N = 0
    return (N, L)

def MBL(N, L):
    L.append(N)
    BL.append(max(L))

def XYSum():
    for y in range(YL):
        N, L = Init()
        for x in range(XL):
            N, L = SUM(N, B[y][x], L)
            if x == XL-1:
                MBL(N, L)
    for x in range(XL):
        N, L = Init()
        for y in range(YL):
            N, L = SUM(N, B[y][x], L)
            if y == YL-1:
                MBL(N, L)

def DP(x, y, N, L):
    while True:
        N, L = SUM(N, B[y][x], L)
        if (x == XL-1) | (y == YL-1):
            MBL(N, L)
            break
        x += 1
        y += 1

def DPSum():
    for i in range(XL):
        N, L = Init()
        y = 0
        x = i
        DP(x, y, N, L)
    for i in range(1, YL):
        N, L = Init()
        y = i
        x = 0
        DP(x, y, N, L)

def DN(x, y, N, L):
    while True:
        N, L = SUM(N, B[y][x], L)
        if (x == 0) | (y == YL-1):
            MBL(N, L)
            break
        x -= 1
        y += 1

def DNSum():
    for i in range(XL):
        N, L = Init()
        y = 0
        x = i
        DN(x, y, N, L)
    for i in range(1, YL):
        N, L = Init()
        y = i
        x = XL-1
        DN(x, y, N, L)

XYSum()
DPSum()
DNSum()

print(max(BL), BL.count(max(BL)))
