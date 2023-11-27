def pvalue(ns, target):
    num = [target ** (len(ns) - (i + 1)) for i in range(len(ns))]
    c = list(zip(ns, num))
    s = 0
    for (i, v) in c:
        s += i * v
    return s

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = int(input())
    print(pvalue(a, b))
