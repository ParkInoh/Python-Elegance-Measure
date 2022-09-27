import numpy as np
c=[]
while True:
    try:
        c.append(list(map(int,list(input()))))
        continue
    except:
        break
p=np.array(c)

lista=[]
listc1=[]
for i in range(len(p)+len(p[0])-1):
    listc1.append([])
listd1=[]
for i in range(len(p) + len(p[0]) - 1):
    listd1.append([])

for i in range(len(p)): #가로
    counta = 0
    for j in range(len(p[0])):
        listc1[i+j].append(p[i][j])#대각선1
        listd1[i - j + len(p[0]) - 1].append(p[i][j])#대각선2

        if p[i][j] == 1:
            counta += 1
        else:
            if counta == 0:
                pass
            else:
                lista.append(counta)
                counta = 0

    lista.append(counta)
    counta = 0

for i in range(len(p[0])): #세로
    countb = 0
    for j in range(len(p)):
        if p[j][i] == 1:
            countb += 1
        elif countb > 0:
            lista.append(countb)
            countb = 0

    lista.append(countb)
    countb = 0

for i in range(len(listc1)):#대각선1
    countc = 0
    for j in range(len(listc1[i])):
        if listc1[i][j]==1:
            countc += 1
        else:
            if countc==0:
                pass
            else:
                lista.append(countc)
                countc = 0
    lista.append(countc)
    countc = 0

for i in range(len(listd1)): #대각선2
    countd = 0
    for j in range(len(listd1[i])):
        if listd1[i][j]==1:
            countd += 1
        else:
            if countd==0:
                pass
            else:
                lista.append(countd)
                countd = 0
    lista.append(countd)
    countd = 0


M=max(lista)
num=lista.count(M)

print(f'{M} {num}')