def find_1(mylist):
    global result
    cnt=0
    for i in range(len(mylist)):
        if mylist[i]=="1":
             cnt+=1
        else:
            result[cnt]=result[cnt]+1
            cnt=0
            continue
    result[cnt]=result[cnt]+1

import sys

mymatrix=[]
for line in sys.stdin:
    temp_input=line.strip("\n")
    if len(temp_input)==0:
        continue
    mymatrix.append(temp_input)

n=len(mymatrix)   #세로
m=len(mymatrix[0]) #가로
result=[]

for i in range(max(n,m)+1):
    result.append(0)

downlist=[]
for j in range(m):
    x=[]
    for i in range(n):
        x.append(mymatrix[i][j])
    downlist.append(x)

L_diag=[]
R_diag = []
if m>1 and n>1:
    for i in range(m):
        y=[]
        for j in range(i+1):
            if j>=n:
                break
            y.append(mymatrix[j][i-j])
        L_diag.append(y)

    for i in range(1,n):
        y=[]
        x1 = m-1
        y1 = i

        for j in range(min(m,n)):
            if y1+j >= n or x1-j < 0:
                break
            y.append(mymatrix[y1+j][x1-j])
        L_diag.append(y)


    for i in range(m):
        z=[]
        for j in range(n):
            if j<n and (i+j)<m:
                z.append(mymatrix[j][i+j])
        R_diag.append(z)

    for i in range(1,n):
        z=[]
        for j in range(n):
            if (i+j)<n and j<m:
                z.append(mymatrix[i+j][j])
        R_diag.append(z)


for i in range(len(mymatrix)):
    find_1(mymatrix[i])

for i in range(len(downlist)):
    find_1(downlist[i])

for i in range(len(L_diag)):
    find_1(L_diag[i])

for i in range(len(R_diag)):
    find_1(R_diag[i])

for i in range(len(result)-1,-1,-1):
    if result[i]!=0:
        print(i,result[i])
        break