def is_digit(a):
    c = []
    for i in a:
        if i.isdigit():
            c.append(int(i))
        else:
            c.append(i)
    return c
def div(a, b):
    count = 0
    c = is_digit(b)
    for j in c:
        try:
            result = a // j
            a %= j
            count += 1
            if result == 0:
                break
            print(result)
        except ZeroDivisionError:
            print(f"({count})")
        except TypeError:
            break
if __name__ == "__main__":
    dividend = int(input())
    divisor = list(input().split())
    div(dividend, divisor)
