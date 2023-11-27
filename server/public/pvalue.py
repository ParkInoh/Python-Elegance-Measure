def pvalue(ns, target):
    c = [ns[i] * target**(len(ns) - (i + 1)) for i in range(len(ns))]
    return sum(c)

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = int(input())
    print(pvalue(a, b))
