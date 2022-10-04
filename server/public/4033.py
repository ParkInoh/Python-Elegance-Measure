# -*- coding: utf-8 -*-
"""
Created on Wed May 25 12:07:56 2022

@author: KK
"""

import numpy as np
import sys

image = np.array([list(map(int,x[:-1])) for x in sys.stdin.readlines()])
#print(image)
image = np.array(image)
#print(image.shape)
#print(n)
#print(inp)

row = np.array(image)
column = row.T
trans = np.rot90(row)
dig_range = range( -row.shape[0]+1, row.shape[1] )
dig1 = []
dig2 = []
for i in dig_range:
    dig1.append(list(np.diag(row,i)))
    dig2.append(list(np.diag(trans,-i)))
datas = [row, column, dig1, dig2]

mem = [0]*50

for lines in datas:
    for line in lines:
        cnt=0
        #print(line)
        for k in line:
            if(k==0):
                mem[cnt] += 1;
                cnt=0
            else:
                cnt += 1
        if(line[-1]==1):
            mem[cnt] += 1;

idx = 49
while(mem[idx]==0): idx-=1
mem = mem[:idx+1]

#print(mem)
print(len(mem)-1,end=" ")
print(mem[-1])

