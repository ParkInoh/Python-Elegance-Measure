
#2차원 배열 입력
import sys
M = []
cnt=0
while True:
    inp = sys.stdin.readline().strip()
    if inp == '':
        break
    M.append(list(inp))
    cnt += 1

xlen = len(M[0])
ylen = cnt


for i in range(ylen):
    for j in range(xlen):
        L = 0
        k = 0
        if M[i][j]=='1':
            #case1 : 아래
            L0 = 0
            for x in range(i, ylen):
                if M[x][j]=='1':
                    L0 += 1
                elif M[x][j]=='0':
                    break
            L = L0
            k = 1
            #case2 : 오른쪽
            L0 = 0
            for y in range(j, xlen):
                if M[i][y]=='1':
                    L0 += 1
                elif M[i][y]=='0':
                    break
            if L0 > L:
                L = L0
                k = 1
            elif L0 == L and L0 != 1:
                k += 1
            #case3 : 오른쪽대각선
            L0 = 0
            x = i
            y = j
            for z in range(min(xlen-j, ylen-i)):
                if M[x][y]=='1':
                    L0 += 1
                elif M[x][y]=='0':
                    break
                x += 1
                y += 1
            if L0 > L:
                L = L0
                k = 1
            elif L0 == L and L0 != 1:
                k += 1
            #case3 : 왼쪽대각선
            L0 = 0
            x = i
            y = j
            while True:
                if M[x][y]=='1':
                    L0 += 1
                elif M[x][y]=='0':
                    break
                if x==ylen-1 or y==0:
                    break
                x += 1
                y -= 1
                
            if L0 > L:
                L = L0
                k = 1
            elif L0 == L and L0 != 1:
                k += 1
                
            M[i][j] = (L, k)





#최대길이 구하기
maxlen = 0
rescnt = 0
for i in range(ylen):
    for j in range(xlen):
        if int(M[i][j][0])>maxlen:
            maxlen = int(M[i][j][0])

#최대길이 수 구하기
for i in range(ylen):
    for j in range(xlen):
        if int(M[i][j][0])==maxlen:
            rescnt += int(M[i][j][1])
            
print(maxlen, rescnt)







            



















                    
