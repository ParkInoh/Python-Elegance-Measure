def change(currency, money, k):
    if k == 0:
        return ' '.join(currency)
    c = money // currency[0]
    money %= currency[0]
    del currency[0]
    currency.append(str(c))
    k -= 1
    return change(currency, money, k)

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = int(input())
    print(change(a, b, len(a)))

