def numvowels(word):
    n = 0
    word.lower()
    for c in word:
        if c in "aeiou":
            n += 1
    return n
def vcap(word):
    s = ''
    for c in word:
        if c in "aeiou":
            s += c.upper()
        else:
            s += c
    return s
def main():
    line = input()
    words = line.split()
    mv_words = []
    mvw_ratio = []
    ratio_str = []
    max_vowels = 0
    for x in words:
        nvowels = numvowels(x)
        mvw_ratio.append(nvowels)
        if max_vowels < nvowels:
            max_vowels = nvowels
    i = 0
    for x in words:
        if numvowels(x) == max_vowels:
            mv_words.append(vcap(x))
            ratio = mvw_ratio[i] / len(x)
            ratio_str.append(f"{ratio:.2f}")
        i += 1

    # print(mv_words)
    # print(ratio_str)
    print(" ".join(mv_words))
    print(" ".join(ratio_str))


if __name__ == "__main__":
    main()
