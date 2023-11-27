from math import sqrt
a, b, c = map(float, input().split())
x, y, z = map(float, input().split())
u, i, o = (a + x), (b + y), (c + z)
s = (a + b + c) / 2
s2 = (x + y + z) / 2
s3 = (u + i + o) / 2
q = sqrt(s*(s-a)*(s-b)*(s-c))
w = sqrt(s2*(s2 - x)*(s2 - y)*(s2 - z))
e = sqrt(s3*(s3 - u)*(s3 - i)*(s3 - o))
print(f"{q:.2f}")
print(f"{w:.2f}")
print(f"{e:.2f}")

class tri:
    