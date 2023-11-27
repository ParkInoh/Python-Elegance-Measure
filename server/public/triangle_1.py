from math import sqrt

class Triangle(object):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def __add__(self, t2):
        return Triangle(self.a + t2.a, self.b + t2.b, self.c + t2.c)
    def __str__(self):
        s = self.heron(self.a, self.b, self.c)
        area = self.getarea(s, self.a, self.b, self.c)
        return f"{area:.2f}"
    @staticmethod
    def heron(a, b, c):
        h = (a + b + c) / 2
        return h
    @staticmethod
    def getarea(s, a, b, c):
        return sqrt(s * (s - a) * (s - b) * (s - c))

def main():
    tl1 = input().split()
    tl2 = input().split()
    t1 = Triangle(float(tl1[0]), float(tl1[1]), float(tl1[2]))
    t2 = Triangle(float(tl2[0]), float(tl2[1]), float(tl2[2]))
    t3 = t1 + t2
    print(t1)
    print(t2)
    print(t3)

if __name__ == "__main__":
    main()
