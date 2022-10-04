import numpy as np
arr = np.array([],dtype=int)
raw = 0
col = 0
while True:
      try:
        a = list(map(int,input()))
        col = len(a)
        raw += 1
        arr = np.append(arr,a)
      except:
              break
arr = np.reshape(arr,(raw,col))
cnt = 0
cntcol = 0
k = 0
lcol = []
M = 0
l = []
bingoraw = 0
bingo = 0
for i in range(0,raw):
    for j in range(0,col):
        if arr[i][j] == 1:
            cnt+=1
            if j == col-1 and cnt >= M:
                M = cnt
                l.append(M)
        else:
            if cnt >= M and cnt != 0:
                M = cnt
                bingoraw += 1
                l.append(M)
            cnt = 0
    cnt = 0

onecnt = 0
for i in range(0,col):
    for j in range(0,raw):
        if arr[j][i] == 1:
            onecnt += 1
            cntcol += 1
            if j == raw -1:
                if cntcol >= k and cntcol != 0:
                    k = cntcol
                    bingo += 1
                    lcol.append(k)
        else:
            if cntcol >= k and cntcol !=0:
                k = cntcol
                bingo += 1
                lcol.append(k)
            cntcol=0
    cntcol = 0
pcnt = 0
pM = 0
pbingo = 0
pl = []
for i in range(-raw+1,col):
    pcnt = 0
    p = np.diag(arr,k=i)
    for j in range(len(p)):
        if p[j] == 1:
            pcnt += 1
            if j == len(p)-1 and pcnt >= pM:
                pM = pcnt
                pl.append(pM)

        else:
            if pcnt >= pM and pcnt != 0:
                pM = pcnt
                pbingo += 1
                pl.append(pM)
            pcnt = 0
qcnt = 0
qM = 0
qbingo = 0
ql = []
for i in range(-raw+1,col):
    qcnt = 0
    q = np.diag(np.fliplr(arr),k=i)
    for j in range(len(q)):
        if q[j] == 1:
            qcnt += 1
            if j == len(q)-1 and qcnt >= qM:
                qM = qcnt
                ql.append(qM)
        else:
            if qcnt >= qM and qcnt != 0:
                qM = qcnt
                qbingo += 1
                ql.append(qM)
            qcnt = 0
sorted(l)
sorted(lcol)
sorted(pl)
answer = l + lcol + pl + ql

ansbingo = 0
for i in answer:
    if i == max(answer):
        ansbingo += 1

if max(answer) == 1:
    print(max(answer),onecnt)
else:
    print(max(answer),ansbingo)