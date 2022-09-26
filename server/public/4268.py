def rotate(arr):
    N,M = len(arr),len(arr[0])
    temp = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
             temp[j][N-1-i] = arr[i][j]
    for i in range(len(temp)):
        temp[i]="".join(temp[i])
    return temp

def line(bingo):
    temp,arr=[],[]
    k=0
    for i in range(len(bingo)):
        temp.append(bingo[i].split("0"))
        arr.append(list(bingo[i]))
    temp=sum(temp,[])
    for i in range(len(temp)):
        k=list(temp[i])
        maxi.append(len(k))
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j]=='1':
                temp=0
                i_=i
                j_=j
                while j_<len(arr[0]) and i_<len(arr) and arr[i_][j_]=='1':
                    temp+=1
                    i_+=1
                    j_+=1
                maxi.append(temp)

bingo=[]
maxi=[0]
while True:
    try:
        bingo.append(input())
    except:
        break
line(bingo)
line(rotate(bingo))
print(max(maxi),maxi.count(max(maxi)))
