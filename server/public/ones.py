def binary(n):
    if n < 2:
        return str(n)
    return binary(n // 2) + binary(n % 2)

def sum_digit(number):
    result = 0
    for i in str(number):
        result += int(i)
    return result

def main(x, y, d):
    num = [binary(i) for i in range(a, b + 1) if int(binary(i)) % d == 0]
    s = 0
    for i in num:
        s += sum_digit(i)
    return s

if __name__ == "__main__":
    a, b = map(int, input().split())
    c = int(input())
    print(main(a, b, c))






