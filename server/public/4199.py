import numpy as np
import sys

def count_lst(lst) :
    global max_cnt,cnt,m,m_c,temp
    max_cnt = []
    cnt = 0
    for w in range(len(lst)) :
        if lst[w] == 1 : 
            cnt += 1
        else :
            max_cnt.append(cnt)
            cnt = 0
    if max_cnt != [] :
        m = max(max_cnt)
        m_c = max_cnt.count(m)
    else : return

    if mylst[-1][0] < m : 
        mylst.append((m,m_c))
    elif mylst[-1][0] == m :
        temp = list(mylst[-1])
        temp[1] = int(temp[1])
        temp[1] += m_c
        mylst[-1] = tuple(temp)


line = sys.stdin.readlines()
my = [ w for w in line]
for w in range(len(line)) :
    my[w] = my[w].rstrip()
x = len(my)
y = len(my[0])
L=[]
mylst = [(0,0)]
for w in my :
    L.append(list(w))
for w in range(0,x) :
    L[w] = list(map(int,L[w]))
L = np.pad(L, pad_width=((1, 1), (1, 1)), mode='constant', constant_values=0)
x += 2
y += 2
mymatrix = np.array(L)
for j in range(y) : count_lst(mymatrix[:, j])
for w in range(x) : count_lst(mymatrix[w, :])
for i in range(1-x, y): count_lst(np.diag(mymatrix,k=i))
mymatrix = np.fliplr(mymatrix)
for i in range(1-x, y): count_lst(np.diag(mymatrix,k=i))
print(mylst[-1][0],mylst[-1][1])