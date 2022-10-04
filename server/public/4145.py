import numpy as np

down = dict()
right = dict()
cross1 = dict()
cross2 = dict()

def downline(x, y, i, j, t):
    if x >= Bingo.shape[0]:
        return
    elif Bingo[x][y] == '0':
        down[i, j] = t-1
        return
    down[i, j] = t
    t += 1
    downline(x+1, y, i, j, t)

def rightline(x, y, i, j, t):
    if y >= Bingo.shape[1]:
        return
    elif Bingo[x][y] == '0':
        right[i, j] = t-1
        return
    right[i, j] = t
    t += 1
    rightline(x, y+1, i, j, t)

def crossline1(x, y, i, j, t):
    if x >= Bingo.shape[0] or y >= Bingo.shape[1]:
        return
    elif Bingo[x][y] == '0':
        cross1[i, j] = t-1
        return
    cross1[i, j] = t
    t += 1
    crossline1(x+1, y+1, i, j, t)

def crossline2(x, y, i, j, t):
    if x >= Bingo.shape[0] or y < 0:
        return
    elif Bingo[x][y] == '0':
        cross2[i, j] = t-1
        return
    cross2[i, j] = t
    t += 1
    crossline2(x+1, y-1, i, j, t)

maximum = []
bingo = []

while True:
    try:
        li = list(input())
        bingo.append(li)
    except:
        Bingo = np.array(bingo)
        for i, row in enumerate(Bingo):
            for j, val in enumerate(row):
                downline(i, j, i, j, 1)
                rightline(i, j, i, j, 1)
                crossline1(i, j, i, j, 1)
                crossline2(i, j, i, j, 1)

        maximum.append(max(down.values()))
        maximum.append(max(right.values()))
        maximum.append(max(cross1.values()))
        maximum.append(max(cross2.values()))

        L = max(maximum)
        cnt = 0

        if L == 0:
            print(L, cnt)
        else:
            if L == max(down.values()):
                cnt += list(down.values()).count(L)
            if L == max(right.values()):
                cnt += list(right.values()).count(L)
            if L == max(cross1.values()):
                cnt += list(cross1.values()).count(L)
            if L == max(cross2.values()):
                cnt += list(cross2.values()).count(L)

            if L == 1:
                print(L, int(cnt/4))
            else:
                print(L, cnt)
        break