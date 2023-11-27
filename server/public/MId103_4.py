def mknum(line, digit):
    line = list(line)
    for i, c in enumerate(line):
        if c == 'X':
            line[i] = str(digit)
    snum = ''.join(line)
    number = int(snum)
    return number

def main():
    line1 = input()
    line2 = input()
    count = 0
    for a in range(10):
        for b in range(10):
            # if a == b:
            #     continue
            n1 = mknum(line1, a)
            n2 = mknum(line2, b)
            if n1 > n2:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
