import numpy as np
temp = []
findLength = []

def cntMaxLength(s): # s: 1차원 리스트, return (최대길이, 갯수)
    maxLength = 0
    cnt = 0
    now = 0
    for i in s:
        if i == 1: now += 1
        else:
            if now > maxLength:
                maxLength = now
                cnt = 1
            elif now == maxLength and now != 0: cnt += 1
            now = 0
    if now > maxLength: return(now, 1)
    if now == maxLength: return(maxLength, cnt+1)
    return (maxLength, cnt)
                
while True:
    try: 
        s = map(int, input())
        temp.append(list(s))
    except: 
        break

n = len(temp)
m = len(temp[0])

arr = np.array(temp)
arr2 = np.flip(arr, axis=1)

for i in range(n):      findLength.append(cntMaxLength(arr[i, :]))
for i in range(m):      findLength.append(cntMaxLength(arr[:, i]))
for i in range(1-n, m): findLength.append(cntMaxLength(np.diag(arr, k=i)))
for i in range(1-n, m): findLength.append(cntMaxLength(np.diag(arr2, k=i)))
findLength.sort(key=lambda x : -x[0])
L = findLength[0][0]
k = 0
for i in findLength:
    if L == i[0]: k += i[1]
    else        : break
print(L, k)