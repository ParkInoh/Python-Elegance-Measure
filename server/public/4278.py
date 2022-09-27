import numpy as np
x=[]
while True:
    try:
        x.append(list(map(int,input())))
    except:
        break
garo=0
sero=0
dae1=0
dae2=0
f=-1
f2=-1
li=[]
li2=[]
li3=[]
def fx(h,j):
    for i in j:

        for k in range(len(i)):
            if i[k]==1:
                h+=1
            else:
                li.append(h)

                h=0
        li.append(h)
        h=0
z=np.rot90(x)
fx(garo,x)

fx(sero,z)
for i in range(len(x[0])+len(x)-1):
    li2.append([])
for i in x:
    f+=1
    for k in range(len(i)):
        li2[f+k].append(x[f][k])

for i in range(len(z[0])+len(z)-1):
    li3.append([])
for i in z:
    f2+=1
    for k in range(len(i)):
        li3[f2+k].append(z[f2][k])
fx(dae1,li2)
fx(dae2,li3)
maxgab=max(li)
print(maxgab,li.count(maxgab))






