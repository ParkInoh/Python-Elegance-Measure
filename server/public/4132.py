import numpy as np
import sys
input_ = sys.stdin.readlines()
data = [list(map(int, i.strip())) for i in input_]
data = np.array(data, dtype=np.int8)

def value(x,y,z):
    if x > y:
        y = x; z = 1
    elif x == y:
        z += 1
    return x, y, z

n = data.shape[0]
m = data.shape[1]
length = 0
num = 0

for i in range(n):
    cnt = 0
    for j in range(m):
        if data[i][j] == 0: cnt = 0; continue
        cnt += 1
        cnt, length, num = value(cnt,length,num)

for i in range(m):
    cnt = 0
    for j in range(n):
        if data[j][i] == 0: cnt = 0; continue
        cnt += 1
        cnt,length,num = value(cnt,length,num)


d = []

for i in range(n):
    d.append(list(np.diag(data, k = -i)))
for i in range(1, m):
    d.append(list(np.diag(data, k = i)))


data = np.rot90(data)
for i in range(m):
    d.append(list(np.diag(data, k = -i)))
for i in range(1, n):
    d.append(list(np.diag(data, k = i)))


for i in range(len(d)):
    cnt = 0
    for j in range(len(d[i])):
        if d[i][j] == 0: cnt = 0; continue
        cnt += 1
        cnt,length,num = value(cnt,length,num)

# 제일 긴게 길이가 1일때 예외처리
if length == 1:
    data = ''.join(input_)
    num = data.count('1')

print(length, num)