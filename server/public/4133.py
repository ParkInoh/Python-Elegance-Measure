#-------------------------------------------------------------------------------
# Author:      Lee Seo Yeon
# Created:     29-05-2022
#-------------------------------------------------------------------------------

import numpy as np

def find(arr):
    array = np.append(arr, np.array([0]))
    sum = 0
    for i in array:
        if i == 1 : sum += 1
        else:
            result.append(sum)
            sum = 0

arr, result = [], []

while(1):
    try:
        line = list(input())
        arr.append(line)
    except:
        arr = np.array(arr, dtype=int)
        for i in range(len(arr)):
            find(arr[i,:])
            find(np.diag(arr,-i))
            find(np.diag(arr[:,::-1],-i))
        for j in range(len(arr[0])):
            find(arr[:,j])
            if j != 0:
                find(np.diag(arr,j))
                find(np.diag(arr[:,::-1],j))
        break

print(max(result), result.count(max(result)))