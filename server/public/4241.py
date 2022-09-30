x=[]
while True:
    try:
        x.append(list(map(int,list(input()))))
        continue
    except:
        break

ga = []
se = []
de1 = []
de2 = []
for i in x:
    a = 0
    for j in i:
        if j == 1 :
            a = a + 1
        else :
            if a == 0 :
                pass
            else :
                ga.append(a)
                a = 0
    if a != 0:
        ga.append(a)
        a = 0

for j in range(len(x[0])) :
    a = 0
    for i in range(len(x)):
        if x[i][j] == 1 :
            a = a+1
        else :
            if a == 0:
                pass
            else :
                se.append(a)
                a = 0
    if a != 0:
        se.append(a)
        a = 0

NEW = []
for i in range(len(x) + len(x[0]) - 1) :
    NEW.append([])

for i in range(len(x[0])) :
    for j in range(len(x)) :
        NEW[i+j].append(x[j][i])

for i in NEW:
    a = 0
    for j in i:
        if j == 1 :
            a = a + 1
        else :
            if a == 0 :
                pass
            else :
                de1.append(a)
                a = 0
    if a != 0:
        de1.append(a)
        a = 0

NEW1 = []
for i in range(len(x) + len(x[0]) - 1) :
    NEW1.append([])

for i in range(len(x[0])) :
    for j in range(len(x)) :
        NEW1[i-j+len(x)-1].append(x[j][i])

for i in NEW1:
    a = 0
    for j in i:
        if j == 1 :
            a = a + 1
        else :
            if a == 0 :
                pass
            else :
                de2.append(a)
                a = 0
    if a != 0:
        de2.append(a)
        a = 0

LIST = [max(ga),max(se),max(de1),max(de2)]
M = max(LIST)

print("{0} {1}".format(max(LIST),ga.count(M)+se.count(M)+de1.count(M)+de2.count(M)))












