import numpy as np
import sys
a=[list(map(int,list(i.strip()))) for i in sys.stdin.readlines()]
gasedae=[]
c=[]
d=[]
z=0
k=0

#가로길이
for i in range(len(a)):
    List=[]
    for j in range(len(a[0])):
        if a[i][j] ==1 and z>k:
            z+=1
        elif a[i][j] ==1 and z<=k:
            z+=1
            k+=1
        else:
            z=0
            if k!=0:
                List.append(k)
            k=0
    List.append(k)
    k=0
    z=0
    gasedae.append(max(List))
 



for i in range (-len(a)+1,len(a[0])):
    c.append(np.diag(a,i))

for i in range (len(c)):
    List=[]
    for j in range (len(c[i])):
        if c[i][j] ==1 and z>k:
            z+=1
        elif c[i][j] ==1 and z<=k:
            z+=1
            k+=1
        else:
            z=0
            if k!=0:
                List.append(k)
            k=0
    List.append(k)
    k=0
    z=0
    gasedae.append(max(List))


b=np.rot90(a)
b=np.array(b)

for i in range(len(b)):
    List=[]
    for j in range(len(b[0])):
        if b[i][j] ==1 and z>k:
            z+=1
        elif b[i][j] ==1 and z<=k:
            z+=1
            k+=1
        else:
            z=0
            if k!=0:
                List.append(k)
            k=0
    List.append(k)
    k=0
    z=0
    gasedae.append(max(List))
  





for i in range (-len(b)+1,len(b[0])):
    d.append(np.diag(b,i))

for i in range (len(d)):
    List=[]
    for j in range (len(d[i])):
        if d[i][j] ==1 and z>k:
            z+=1
        elif d[i][j] ==1 and z<=k:
            z+=1
            k+=1
        else:
            z=0
            if k!=0:
                List.append(k)
            k=0
    List.append(k)
    k=0
    z=0
    gasedae.append(max(List))



print(max(gasedae), gasedae.count(max(gasedae)))

