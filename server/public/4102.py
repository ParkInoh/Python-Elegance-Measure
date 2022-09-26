import numpy as np

lst = []

while True:
    try:
        my_input = list(input())
        lst.append(my_input)

    except EOFError:
        break

my_arr = np.array(lst)
my_arr = my_arr.astype(int)
row, col = my_arr.shape
result_lst = [[(0,0) for j in range(col)] for i in range(row)]
row_count = 0
col_count = 0
rdi_count = 0
ldi_count = 0


for i in range(row):
    for w in range(col):
        if my_arr[i][w] == 1:
            first_i = i
            first_w = w
            #오른쪽 길이
            while my_arr[i][w] == 1:
                col_count+=1
                if w >= col-1: break#10
                w+=1

            w = first_w
            #아래 길이
            while my_arr[i][w] == 1:
                row_count+=1
                if i >= row-1: break
                i+=1

            i = first_i
            #오른쪽 대각
            while my_arr[i][w] == 1:
                rdi_count+=1
                if w >= col-1 or i >= row-1: break
                i+=1
                w+=1

            i = first_i
            w = first_w
            #왼 대각
            while my_arr[i][w] == 1:
                ldi_count+=1
                if w <= 0 or i >= row-1: break
                i+=1
                w-=1

            i = first_i
            w = first_w

            count_lst=[col_count, row_count, rdi_count, ldi_count]
            k = max(count_lst)
            l = count_lst.count(k)
            result_lst[i][w] = (k,l)
            row_count = 0
            col_count = 0
            rdi_count = 0
            ldi_count = 0
        else:
            pass
result1 = 0
result2 = 0
for i in range(row):
    for w in range(col):
        if result1 == result_lst[i][w][0]:
            result2+=result_lst[i][w][1]
        elif result1 < result_lst[i][w][0]:
            result1 = result_lst[i][w][0]
            result2 = result_lst[i][w][1]
        else :
            pass
print(result1, result2)
