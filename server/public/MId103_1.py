#푸는방법을 3가지로 나눔 모두 동일결과를 낸다.
def hamming1(s1, s2):
    ans = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ans += 1
        return ans

def hamming2(s1, s2):
    ans = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            ans += 1
    return ans

def hamming3(s1, s2):
    return len([1 for c1, c2 in zip(s1, s2) if c1 != c2])

if __name__ == "__main__":
    line1 = input()
    line2 = input()
    print(hamming2(line1, line2))