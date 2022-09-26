import numpy as np
b=[]
while True:
    try:
        a = list(input())
        b += [a]
    except:
        break
c = []
d = []
M = np.array(b)
for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] == "1":
            ma = []
            if len(M[0])-j >= len(M)-i:
                f = len(M)-i
            elif len(M[0])-j <= len(M)-i:
                f = len(M[0])-j
            if j+1 >= len(M)-i :
                t = len(M)-i
            elif j+1 <= len(M)-i :
                t = j+1
            k = 0
            for z in range(len(M[0])-j):
                if M[i][j+z] == "1":
                    k += 1
                else: break
            ma += [k]
            k = 0
            for z in range(f):
                if M[i+z][j+z] == "1":
                    k += 1
                else: break
            ma += [k]
            k = 0
            for z in range(t):
                if M[i+z][j-z] == "1":
                    k+=1
                else: break
            ma += [k]
            k = 0
            for z in range(len(M)-i):
                if M[i+z][j] == "1":
                    k+=1
                else: break
            ma += [k]
            mk = max(ma)
            nk = ma.count(mk)
            c += [[mk,nk]]
            d += [mk]
            b[i][j] = (mk,nk)
for i in c:
    if i[0]==1:
        i[1]=1
md = max(d)
n = 0
for i in c:
   if i[0]==md:
    n+=i[1]
print(f"{md} {n}")





