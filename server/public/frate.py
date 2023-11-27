def freq_rate():
    a = input()
    b = a.upper()
    b_len = len(b)
    freq = []
    for c in b:
        if c.isalpha():
            freq.append(b.count(c))
    maxcnt = max(freq)
    for i in b:
        if i.isalpha() == False:
            b_len -= 1
    frate = maxcnt / b_len
    print(f"{frate:.2f}")
if __name__ == "__main__":
    freq_rate()
