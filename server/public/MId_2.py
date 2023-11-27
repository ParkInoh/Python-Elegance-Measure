def iseven(n):
    return n % 2 == 0

def prgraph(symbol, num):
    for i in range(1, num + 1):
        _ = prline(symbol, 2 * i) if iseven(i) else prline(symbol, 2 * i + 1)

def prline(symbol, num):
    print(symbol * num)
    
if __name__ == "__main__":
    items = input().split()
    prgraph(items[0], int(items[1])   )