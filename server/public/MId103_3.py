def median(s1, s2):
    min_len = min(len(s1), len(s2))
    reminder = s1[min_len:] if s1[min_len:] != '' else s2[min_len:]
    result = ''
    for i in range(min_len):
        if i % 2 == 0:
            result += s1[i]
        else:
            result += s2[i]       
    return result + reminder
if __name__ == "__main__":
    words = input().split()
    words.sort()
    nwords = len(words)
    midi = nwords // 2
    if nwords % 2 == 0:
        medword = median(words[midi - 1], words[midi])
    else:
        medword = words[midi]
    print(medword)
