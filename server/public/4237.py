import numpy as np
def West_South(a,b,n) : #남서쪽 대각선
    if (a >= N) or (b < 0) or (bingo_board[a][b] == '0') :
        return n
    else :
        n += 1
        a += 1
        b -= 1
        return West_South(a,b,n)
def South(a,b,n) : #남쪽 직선
    if (a >= N) or (bingo_board[a][b] == '0') :
        return n
    else :
        n += 1
        a += 1
        return South(a,b,n)
def East_South(a,b,n) : #남동쪽 대각선
    if (a >= N) or (b >= M) or (bingo_board[a][b] == '0') :
        return n
    else :
        n += 1
        a += 1
        b += 1
        return East_South(a,b,n)
def East(a,b,n) : # 동쪽 직선
    if (b >= M) or (bingo_board[a][b] == '0') :
        return n
    else :
        n += 1
        b += 1
        return East(a,b,n)

arr = []
while True :
    try :
        arr.append((" ".join(input())).split())
    except EOFError :
        break
bingo_board = np.array(arr)
N = len(arr)
M = len(arr[0])
length_4 = []
max_length = 0
cnt = 0
n = 0

for i in range(N) :
    for j in range(M) :
        if bingo_board[i][j] == '1' :
            length_4.append(West_South(i,j,n))
            length_4.append(South(i,j,n))
            length_4.append(East_South(i,j,n))
            length_4.append(East(i,j,n))
            longest = max(length_4)
            length_4.remove(longest)

            if longest > max_length :
                max_length = longest
                cnt = 1
                while longest in length_4 :
                    length_4.remove(longest)
                    cnt += 1
            elif longest == max_length :
                cnt += 1
                while longest in length_4 :
                    length_4.remove(longest)
                    cnt += 1

            length_4 = []

print(str(max_length) + " " + str(cnt))