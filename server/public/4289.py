import numpy
import sys

def height_check(mymatrix, n):
    bingo_list=[0,0]
    for w in range(n) :
         count=0
         count_list=[]
         for i in range(n) :
              if   mymatrix[w][i] == "0" :
                count_list.append(count)
                count  = 0
              elif mymatrix[w][i] == "1" :
                count += 1

         for k in range(len(count_list)):
              if   count_list[k] == bingo_list[0] :
                 bingo_list[1] += 1
              elif count_list[k] > bingo_list[0]  :
                 bingo_list[1] = 1
                 bingo_list[0] = count_list[k]
              else :
                  pass
    return(bingo_list)

def width_check(mymatrix, n):
    bingo_list=[0,0]
    for w in range(n) :
         count=0
         count_list=[]
         for i in range(n) :
              if   mymatrix[i][w] == "0" :
                count_list.append(count)
                count  = 0
              elif mymatrix[i][w] == "1" :
                count += 1

         for k in range(len(count_list)):
              if   count_list[k] == bingo_list[0] :
                 bingo_list[1] += 1
              elif count_list[k] > bingo_list[0]  :
                 bingo_list[1] = 1
                 bingo_list[0] = count_list[k]
              else :
                  pass
    return(bingo_list)

while True:
    my = sys.stdin.readline().strip()
    if my == "":  break
    lines.append(my)

lines=my.split()
n = len(lines)

L=[]
for w in lines :
    L.append( list(w))
mymatrix= numpy.array(L)

h = height_check(mymatrix, n)
w = width_check(mymatrix,n)
if h[0] > w[0] :
    print("".join(h))
if h[0] < w[0] :
    print("".join(w))
if h[0] == w[0] :
    h[1] += w[1]
    print("".join(h))








