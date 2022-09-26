import numpy as np
bingo_list = []
while True:
    try:
        bingo_list.append(list(input()))
    except:
        break
for i in range(len(bingo_list)) :
    bingo_list[i] = list(map(int, bingo_list[i]))
length_list = []
temp = 0
count = 0
bingo_list = np.array(bingo_list)
bingo_list = np.pad(bingo_list, ((1,1),(1,1)), 'constant', constant_values=int(0))

#row
for i in range(len(bingo_list)) :
    bingo_list[i] = list(map(int, bingo_list[i]))  #int형으로 변환
    for j in range(0, len(bingo_list[0])-1):
        if bingo_list[i][j] == bingo_list[i][j+1] and bingo_list[i][j] == 1 :
            count += 1
        elif bingo_list[i][j] == 1 and bingo_list[i][j+1] == 0:
            count += 1
            length_list.append(count)
            count = 0
        else:
            count = 0

#column
for i in range(len(bingo_list[0])) :
    for j in range(len(bingo_list)-1) :
        if bingo_list[j][i] == bingo_list[j+1][i] and bingo_list[j][i] == 1 :
            count += 1
        elif bingo_list[j][i] == 1 and bingo_list[j+1][i] == 0:
            count += 1
            length_list.append(count)
            count = 0
        else:
            count = 0

#diagonal_1
m = len(bingo_list[0])
while True :
    line = np.diag(bingo_list, k = m)
    count = 0
    for i in range(0, len(line)-1):
        if line[i] == line[i+1] and line[i] == 1 :
            count += 1
        elif line[i] == 1 and line[i+1] == 0 :
            count += 1
            length_list.append(count)
            count = 0
        else :
            count = 0
    m -= 1
    if m == - len(bingo_list) + 1 :
        break

#diagonal_2
bingo_list = np.fliplr(bingo_list)
m = len(bingo_list[0])
while True :
    line = np.diag(bingo_list, k = m)
    count = 0
    for i in range(0, len(line)-1):
        if line[i] == line[i+1] and line[i] == 1 :
            count += 1
        elif line[i] == 1 and line[i+1] == 0 :
            count += 1
            length_list.append(count)
            count = 0
        else :
            count = 0
    m -= 1
    if m == - len(bingo_list) + 1 :
        break
length_list.sort()
length_list.reverse()
num = {}
for i in length_list :
    try: num[i] += 1
    except: num[i]=1
print(list(num.keys())[0], num[list(num.keys())[0]])