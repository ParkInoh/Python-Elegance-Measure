import numpy as np
def R() :
    for x in loc :
        for y in x :
            if (y-1) in x : continue
            elif (y+1) in x :
                stk = 2
                y += 1
                while True :
                    if (y+1) in x :
                        stk += 1
                        y += 1
                    else :
                        break
                res.append(stk)
def C() :
    for x in range(len(loc)-1) :
        for y in range(len(loc[x])) :
            if x > 0 :
                if loc[x][y] in loc[x-1] : continue
            if loc[x][y] in loc[x+1] :
                stk = 2
                tmp4 = loc[x][y]
                ad = 2
                while True :
                    if (x+ad) == len(loc) : break
                    if tmp4 in loc[x+ad] :
                        stk += 1
                        ad += 1
                    else :
                        break
                res.append(stk)
def RD() :
    for x in range(len(loc)-1) :
        for y in range(len(loc[x])) :
            if x > 0 :
                if (loc[x][y]-1) in loc[x-1] : continue
            if loc[x][y]+1 in loc[x+1] :
                stk = 2
                tmp5 = loc[x][y]
                tmp5 += 1
                ad = 2
                while True :
                    if (x+ad) == len(loc) : break
                    elif (tmp5+1) in loc[x+ad] :
                        stk += 1
                        tmp5 += 1
                        ad += 1
                    else :
                        break
                res.append(stk)
def LD() :
    for x in range(len(loc)-1) :
        for y in range(len(loc[x])) :
            if x > 0 :
                if (loc[x][y]+1) in loc[x-1] : continue
            if (loc[x][y]-1) in loc[x+1] :
                stk = 2
                tmp6 = loc[x][y]
                tmp6 -= 1
                ad = 2
                while True :
                    if (x+ad) == len(loc) : break
                    elif (tmp6-1) in loc[x+ad] :
                        stk += 1
                        tmp6 -= 1
                        ad += 1
                    else :
                        break
                res.append(stk)
tmp = []
tmp2 = []
tmp3 = []
res = []
loc = []
while True :
    try :
        tmp.append(str(input()))
    except :
        break
for i in range(len(tmp)) :
    tmp[i] = [char for char in tmp[i]]
    tmp[i] = np.array(tmp[i])
board = np.array(tmp, dtype='U')
for i in range(len(board)) :
    tmp2.append(np.where(board[i] == '1'))
    tmp3.append(tmp2[i][0])
for i in range(len(tmp2)) :
    tmp3[i] = np.array(tmp3[i])
for i in range(len(tmp3)) :
    loc.append(tmp3[i])
R()
C()
RD()
LD()

maxi = max(res)
many = 0
while True :
    if maxi in res :
        res.remove(maxi)
        many += 1
    else : break
print(maxi, many)