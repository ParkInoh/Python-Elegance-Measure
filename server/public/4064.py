import numpy as np
collect_line = list(map(int, list(input())))
column = len(collect_line)
row = 1
while True:
    try:
        collect_line+=list(map(int, list(input())))
        row+=1
    except EOFError:
        break

myArray = np.array(collect_line).reshape(row,column)
myArray_fliplr=np.fliplr(myArray)
large=dict()

def line2(rowORcolumn):
    for i in range(0,rowORcolumn):
        if rowORcolumn == row:
            some = myArray[i,:]
        else :
            some = myArray[:,i]
        n=0
        for j, h in enumerate(some,start=1):
            if h==1:
                n+=1
                if j==len(some) or some[j]==0:
                    try:
                        large[n]+=1
                    except :
                        large[n]=1
            else :
                n=0

def diagonal2(putArray):
    for i in range(-row+1,column):
        some=np.diag(putArray, k=i)  #한 대각선
        n=0
        for j, h in enumerate(some,start=1):
            if h==1:
                n+=1
                if j==len(some) or some[j]==0:
                    try:
                        large[n]+=1
                    except :
                        large[n]=1
            else :
                n=0

line2(row)
line2(column)
diagonal2(myArray)
diagonal2(myArray_fliplr)

keymax= max(large.keys())
print(keymax,large[keymax])
