# -*- coding: utf-8 -*-

a = input()
b = a.split()

def f():
    sum = 0
    for i in b[1:]:
        sum += int(i)
        print(b[0] * sum)
    
f()
