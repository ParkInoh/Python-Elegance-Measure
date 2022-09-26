import sys

M = []
while '' not in M :
    line = sys.stdin.readline()
    M.append(line.strip('\n'))
del M[-1]
N = []
c = {}
for i in range(len(M)) :
    for w in range(len(M[0])) :
        L1,L2,L3,L4,f,g,h,o,p,q = 0,0,0,0,0,0,0,0,0,0
        if M[i][w] == 0 : pass
        else :
                  #가로
            while M[i][w+f] != '0' :
                L1 += 1
                f += 1
                if w+f == len(M[0]) : break
            N.append(L1)
            if L1 not in c.keys() : c[L1] = 1
            else                  : c[L1] += 1
                   #세로
            while M[i+g][w] != '0' :
                L2 += 1
                g += 1
                if i+g == len(M) : break
            N.append(L2)
            if L2 not in c.keys() : c[L2] = 1
            else                  : c[L2] += 1
                  #우하향
            while M[i+h][w+o] != '0' :
                L3 += 1
                h += 1
                o += 1
                if i+h == len(M) or w+o == len(M[0]) : break
            N.append(L3)
            if L3 not in c.keys() : c[L3] = 1
            else                  : c[L3] += 1
                  #좌하향
            while M[i+p][w-q] != '0' :
                L4 += 1
                p += 1
                q += 1
                if i+p == len(M) or w-q == -1 : break
            N.append(L4)
            if L4 not in c.keys() : c[L4] = 1
            else                  : c[L4] += 1
print(str(max(N)) + ' ' + str(c[max(N)]))