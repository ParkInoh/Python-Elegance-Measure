import numpy as np
st=[]
for w in range(51) :
    try: st.append(input())
    except : break
l=[]
for w in st :
    l.append(list(w))
l = np.array(l)
l2 = np.transpose(l)
l3 = np.fliplr(l)
sc = []

def cal(str) :
    val = 0
    for w in str :
        val+=int(w)
    return val

def cal2(li) :
    e = li.split('0')
    for h in e :
        sc.append(cal(h))

for w in st :
    a = w.split('0')
    for j in a :
        sc.append(cal(j))

for w in l2.tolist() :
    res = ''.join(s for s in w)
    b = res.split('0')
    for k in b :
        sc.append(cal(k))

c = -(len(l)-1)

for w in range(len(l)+len(l[0])-1) :
    d = ''.join(s for s in np.diag(l,k=c).tolist())
    e = ''.join(j for j in np.diag(l3,k=c).tolist())
    cal2(d)
    cal2(e)
    c+=1

print(max(sc), sc.count(max(sc)))













