import numpy as np
import sys
input = sys.stdin.readline

bingo = []

w = 0
while (True):
    try:
        bingo.append([])
        bingo[w] = list(input())
        bingo[w].pop()
        w += 1
    except:
        bingo.pop()
        break

width = len(bingo[0])
height = len(bingo)


def f_bingo(bingo, list, A, B):

    for i in range(A):

        count = 0
        for j in range(B):
            if bingo[i][j] == '1':
                count += 1

            if bingo[i][j] == '0' or j == B - 1:

                if count > list[0]:
                    list[0] = count
                    list[1] = 1
                    count = 0

                elif count == list[0]:
                    list[1] += 1
                    count = 0

                else:
                    count = 0


def g_bingo(bingo, list, A, B):
    for i in range(A):
        count = 0

        for j in range(B):
            if bingo[j][i] == '1':
                count += 1

            if bingo[j][i] == '0' or j == B - 1:

                if count > list[0]:
                    list[0] = count
                    list[1] = 1
                    count = 0

                elif count == list[0]:
                    list[1] += 1
                    count = 0

                else:
                    count = 0


def h_bingo(list_1, list_2):

    for i in range(len(list_1)):
        count = 0

        for j in range(len(list_1[i])):

            if list_1[i][j] == '1':
                count += 1

            if list_1[i][j] == '0' or j == len(list_1[i]) - 1:

                if count > list_2[0]:

                    list_2[0] = count
                    list_2[1] = 1
                    count = 0

                elif count == list_2[0]:
                    list_2[1] += 1
                    count = 0

                else:
                    count = 0


def make_diag(alpha, width, height, list_1):
    for w in range(- height + 1, width):
        list_1.append(list(np.diag(alpha, k=w)))


# 가로 빙고 check
long = [0, 0]
f_bingo(bingo, long, height, width)

# 세로 빙고 check
g_bingo(bingo, long, width, height)

a = np.array(bingo)

left_diag = []

make_diag(a, width, height, left_diag)

h_bingo(left_diag, long)

new_bingo = []
for w in range(len(bingo)):
    temp = reversed(bingo[w])
    new_bingo.append(list(temp))

b = np.array(new_bingo)

right_diag = []

make_diag(b, width, height, right_diag)

h_bingo(right_diag, long)

print(*long)

sys.exit()
