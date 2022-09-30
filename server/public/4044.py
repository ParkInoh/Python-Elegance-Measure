import numpy as np

def depend(arr):
    lenlist = []
    arr = ''.join(str(_) for _ in arr).split("0")
    for i in range(len(arr)):
        lenlist.append(len(arr[i]))
    result = (max(lenlist), lenlist.count(max(lenlist))) 
    if result[0] == 0:
        return (0, 0)
    return result

arr = []
revarr = []
dia = []
result = 0
while True:
    try : line = list(map(int, input()))
    except : break
    arr.append(line)
arr = np.array(arr)
revarr = arr[:, ::-1]

for i in range(len(arr)):
    dia.append(depend(np.diag(arr, -i)))
    dia.append(depend(np.diag(revarr,- i)))
    dia.append(depend(arr[i]))

for i in range(len(arr[0])):
    dia.append(depend(arr[:, i]))

for i in range(1,len(arr[0])):
    dia.append(depend(np.diag(arr, i)))
    dia.append(depend(np.diag(revarr, i)))
dia.sort(reverse=True)

for i in range(len(dia)):
    if dia[i][0] == dia[0][0]:
        result += dia[i][1]
print(dia[0][0], result)
