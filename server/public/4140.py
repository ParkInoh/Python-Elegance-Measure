
import numpy as np

global max_len
max_len = 0
global max_count
max_count = 0


def garocheck(bingo, i, k, garo, max_len, max_count):
    count = 0
    while True:
        if k == garo or bingo[i][k] == 0:
            break;

        if bingo[i][k] == 1:
            count = count + 1
            k = k + 1

    if max_len == count:
        max_count = max_count + 1

    if max_len < count:
        max_len = count
        max_count = 1

    return (max_len, max_count)

def serocheck(bingo, i, k, sero, max_len, max_count):
    count = 0
    while True:
        if i == sero or bingo[i][k] == 0:
            break;

        if bingo[i][k] == 1:
            count = count + 1
            i = i + 1

    if max_len == count:
        max_count = max_count + 1

    if max_len < count:
        max_len = count
        max_count = 1

    return (max_len, max_count)

def daegakdowncheck(bingo, i, k, sero, garo, max_len, max_count):
    count = 0
    while True:
        if i == sero or k == garo or bingo[i][k] == 0:
            break;

        if bingo[i][k] == 1:
            count = count + 1
            i = i + 1
            k = k + 1

    if max_len == count:
        max_count = max_count + 1

    if max_len < count:
        max_len = count
        max_count = 1

    return (max_len, max_count)

def daegakupcheck(bingo, i, k, garo, max_len, max_count):
    count = 0
    while True:
        if i == -1 or k == garo or bingo[i][k] == 0:
            break;

        if bingo[i][k] == 1:
            count = count + 1
            i = i - 1
            k = k + 1

    if max_len == count:
        max_count = max_count + 1

    if max_len < count:
        max_len = count
        max_count = 1

    return (max_len, max_count)

num=[]
sero = 0

while True:

    try:
        a = input()

        garo = len(a)

        for i in range(len(a)):
            num.append(int(a[i]))

        sero = sero + 1
    except EOFError:
        break;

bingo = np.array(num)
bingo = bingo.reshape(sero, garo)

for i in range(bingo.shape[0]):
    for k in range(bingo.shape[1]):
        if bingo[i][k] == 1:
            max_len, max_count = garocheck(bingo, i, k, bingo.shape[1], max_len, max_count)
            max_len, max_count = serocheck(bingo, i, k, bingo.shape[0], max_len, max_count)
            max_len, max_count = daegakdowncheck(bingo, i, k, bingo.shape[0], bingo.shape[1], max_len, max_count)
            max_len, max_count = daegakupcheck(bingo, i, k, bingo.shape[1], max_len, max_count)

print(max_len, max_count)