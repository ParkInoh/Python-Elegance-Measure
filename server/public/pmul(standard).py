def main(a, b):
    ans = [0 for _ in range(len(a) + len(b) - 1)]
    for (i, n1) in enumerate(a):
        for (j, n2) in enumerate(b):
            ans[i + j] += (n1 * n2)
    ans = list(map(str, ans))
    return ' '.join(ans)
if __name__ == "__main__":
    p1 = list(map(int, input().split()))
    p2 = list(map(int, input().split()))
    print(main(p1, p2))
    


