def syg(a, b):
    num = [str(i) for i in range(a, b + 1)]
    count = [1 for j in num for k in j if k in '369']
    return sum(count)
            
if __name__ == "__main__":
    x, y = map(int, input().split())
    print(syg(x, y))
