matrix = []
while True:
    try:
        matrix.append(tuple(input()))
    except EOFError:
        break

import numpy as np
matrix = np.array(matrix)
garo, sero = matrix.shape[0], matrix.shape[1]
out_num, out_count = 0, 0
for i in range(garo):
    for j in range(sero):
        if matrix[i, j] == '1' :
            n = 1
            while i+n < garo and j+n < sero and matrix[i+n, j+n] == '1' :
                n += 1
            if n > out_num : out_num, out_count = n, 1
            elif n == out_num : out_count += 1

            n = 1
            while i+n < garo  and j-n >= 0 and matrix[i+n, j-n] == '1' :
                n += 1
            if n > out_num : out_num, out_count = n, 1
            elif n == out_num : out_count += 1

            n = 1
            while i+n < garo and matrix[i+n, j] == '1' :
                n += 1
            if n > out_num : out_num, out_count = n, 1
            elif n == out_num : out_count += 1

            n = 1
            while j+n < sero and matrix[i, j+n] == '1' :
                n += 1
            if n > out_num : out_num, out_count = n, 1
            elif n == out_num : out_count += 1

print(out_num, out_count)


