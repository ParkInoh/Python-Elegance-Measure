def mystr(x):
    return f"{x:02}"

def count_in(k, hour, m, sec):
    return 1 if k in mystr(hour) or k in mystr(m) or k in mystr(sec) else 0

def main():
    n = int(input())
    k = input()
    count = 0
    for hour in range(0, n+1):
        for m in range(0, 60):
            for sec in range(0, 60):
                count += count_in(k, hour, m, sec)
    print(count)   
if __name__ == "__main__":
    main()