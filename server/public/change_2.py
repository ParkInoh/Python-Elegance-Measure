def change(currency, money):
    c = money // currency[0]
    if len(currency) == 1:
        print(c)
    else:
        money %= currency[0]
        del currency[0]
        print(c, end = ' ')
        return change(currency, money)

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = int(input())
    change(a, b)
