from math import sqrt

class Tri(object):
    def __init__(self, a):
        self.a = a
    
    def __add__(self, ot):
        self.a = list(map(float, self.a))
        ot.a = list(map(float, ot.a))
        return [self.a[i] + ot.a[i] for i in range(3)]
    
    def __repr__(self):
        s = (self.a[0] + self.a[1] + self.a[2]) / 2
        result = sqrt(s * (s - self.a[0]) * (s - self.a[1]) * (s - self.a[2]))
        return f"{result:.2f}"

if __name__ == "__main__":
    a = list(map(float, input().split()))
    b = list(map(float, input().split()))
    at = Tri(a)
    bt = Tri(b)
    ct = Tri(at + bt)

    print(at)
    print(bt)
    print(ct)
