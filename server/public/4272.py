import sys

list_file = []
while True:
    In = sys.stdin.readline().strip()
    if not In:
        break
    list_file.append(In)

list_ = []
for i in range(len(list_file)):
    list_.append(list(map(int,list_file[i])))

Garo=[]
Sero=[]
Daegak=[]

for i in range(len(list_)):
    for j in range(len(list_[i])):
        #Garo
        k=0
        while True:
            if list_[i][j+k] == 1:
                k+=1
                if j+k == len(list_[i]):
                    Garo.append(k)
                    break
                else:
                    pass
            else:
                Garo.append(k)
                break
        #Sero
        k=0
        while True:
            if list_[i+k][j] == 1:
                k+=1
                if i+k == len(list_):
                    Sero.append(k)
                    break
                else:
                    pass
            else:
                Sero.append(k)
                break
        #Daegak
        k=0
        while True:
            if list_[i+k][j+k] == 1:
                k+=1
                if i+k == len(list_) or j+k == len(list_[i]):
                    Daegak.append(k)
                    break
                else:
                    pass
            else:
                Daegak.append(k)
                break

        k=0
        while True:
            if list_[i+k][j-k] == 1:
                k+=1
                if i+k == len(list_) or j-k == -1:
                    Daegak.append(k)
                    break
                else:
                    pass
            else:
                Daegak.append(k)
                break

Result = Garo + Sero + Daegak

cnt = 0
for i in Result:
    if i == max(Result):
        cnt += 1
    else:
        pass

print(max(Result),cnt)





