import numpy as np


stdin = []                            #입력값이 2차원 리스트형태로 여기 들어옴


while True:
    try:
        stdin.append(list(map(int, input().strip())))
    except:
        break


stdin = np.array(stdin, dtype='i1')   #input 값을 행렬로 바꿈, i1=부호있는 8비트 정수형.


n = stdin.shape[0]
m = stdin.shape[1]
rep = 0
num = 0                               #n=행의 개수, m=열의 개수


def find(stdin, A, B):
    if stdin > A:
        A = stdin
        B = 1
    elif stdin == A:
        B += 1
    return stdin, A, B

for x in range(m):
    C = 0
    for y in range(n):
        if stdin[y][x] == 0:
            C = 0; continue
        C += 1
        C, rep,num = find(C, rep, num)

for i in range(n):
    C = 0
    for j in range(m):
        if stdin[i][j] == 0:
            C = 0; continue
        C += 1
        C, rep, num = find(C, rep, num)


D = []


for E in range(1, m):
    D.append(list(np.diag(stdin, k = E)))  # k가 파라매터라서 이건 바꾸면 안 됨.

for E in range(n):
    D.append(list(np.diag(stdin, k = -E)))


F = stdin[::-1]


for E in range(1, m):
    D.append(list(np.diag(F, k = E)))

for E in range(n):
    D.append(list(np.diag(F, k = -E)))

for E in range(len(D)):
    C = 0
    for G in range(len(D[E])):
        if D[E][G] == 0:
            C = 0; continue
        C += 1
        C, rep, num = find(C, rep, num)

if rep == 1:
    stdin = ''.join(lines)
    num = stdin.count('1')

print(rep, num)