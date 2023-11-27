def main(curency, money):
    b = list()
    for e in curency:
        b.append(str(money // e))
        money %= e
    return " ".join(b)

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = int(input())
    print(main(a, b))

