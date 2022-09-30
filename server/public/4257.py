import numpy as np
import sys
def check1(bingo, i, j, n) :
    if bingo[i][j] == 1 :
        n += 1
    if bingo[i][j] == 0 or j == len(bingo[0])-1  :
        Bingo.append(n)
        return
    j +=1
    check1(bingo, i, j, n)
def check2(bingo, i, j, n) :
    if bingo[i][j] == 1 :
        n += 1
    if  bingo[i][j] == 0 or i == len(bingo)-1 :
        Bingo.append(n)
        return
    i += 1
    check2(bingo, i, j, n)
def check3(bingo, i, j, n) :
    if bingo[i][j] == 1 :
        n += 1
    if bingo[i][j] == 0 or i == len(bingo)-1 or j == len(bingo[0])-1  :
        Bingo.append(n)
        return
    i += 1
    j += 1
    check3(bingo, i, j, n)
def check4(bingo, i, j, n) :
    if bingo[i][j] == 1 :
        n += 1
    if bingo[i][j] == 0 or i == len(bingo)-1 or j == 0  :
        Bingo.append(n)
        return
    i += 1
    j -= 1
    check4(bingo, i, j, n)
bingo = []
Bingo = []
while True :
    data = (list(map(int, sys.stdin.readline().strip('\n'))))
    if not data :
        break
    bingo.append(data)
bingo = np.array(bingo)
for i in range(0, len(bingo)):
    for j in range(0, len(bingo[0])) :
        if bingo[i][j] == 1 :
            n = 0
            for k in range(0,4) :
                if j != len(bingo[0])-1 and k ==0 :
                    if bingo[i][j+1] == 1 : check1(bingo, i, j, n)
                elif  i != len(bingo)-1 and k == 1:
                    if bingo[i+1][j] == 1 : check2(bingo, i, j, n)
                elif i != len(bingo)-1 and j != len(bingo[0])-1 and k ==2 :
                    if bingo[i+1][j+1] == 1 : check3(bingo, i, j, n)
                elif i != len(bingo)-1 and j != 0 and k ==3 :
                    if bingo[i+1][j-1] == 1 : check4(bingo, i, j, n)
a = max(Bingo)
b = Bingo.count(a)
print(a, b)



