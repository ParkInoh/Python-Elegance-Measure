
import numpy as np

def fx(x_f,y_f) :
    x = x_f
    y = y_f
    point = 0
    points = []
    while True :   #right
        try :
            if int(stdin[x, y]) == 1 :
                point += 1
                x += 1
            else :
                break
        except IndexError :
            break
    points.append(point)
    x = x_f
    y = y_f
    point = 0
    while True :   #down
        try :
            if int(stdin[x, y]) == 1 :
                point += 1
                y += 1
            else :
                break
        except IndexError :
            break
    points.append(point)
    x = x_f
    y = y_f
    point = 0
    while True :   #rightdown
        try :
            if int(stdin[x, y]) == 1 :
                point += 1
                x += 1
                y += 1
            else :
                break
        except IndexError :
            break
    points.append(point)
    x = x_f
    y = y_f
    point = 0
    while True :   #rightup
        try :
            if int(stdin[x, y]) == 1 and x >= 0:
                point += 1
                x += -1
                y += 1
            else :
                break
        except IndexError :
            break
    points.append(point)
    best = max(points)
    count = points.count(best)
    return [best,count]


lines=[]
highth = 0
while True :
    try :
        line = list(input())
        lines.append(line)
        highth += 1
    except EOFError :
        break
n = len(lines[0])
stdin = np.array(lines)
max_point = 0
result = 0

for y in range(n) :
    for x in range(highth) :
        aa = fx(x,y)
        if aa[0] > max_point :
            max_point = aa[0]
            result = 0
        if aa[0] == max_point :
            result += aa[1]

print(f'{max_point} {result}')