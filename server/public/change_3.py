def change(currency, money, k = []):
    if len(currency) == 0:
        return ' '.join(k)
    c = money // currency[0]
    k.append(str(c))
    money %= currency[0]
    del currency[0]
    return change(currency, money, k)

if __name__ == "__main__":
    a = list(map(int, input().split()))
    b = int(input())
    print(change(a, b))
