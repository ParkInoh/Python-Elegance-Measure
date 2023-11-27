def mysort(num):
    n, m, k = num[0], num[1], num[2]
    if n > m:
        num[0], num[1] = m, n        
    if num[0] > k:
        del num[2]
        num = [k] + num
    elif num[1] > k:
        del num[2]
        num.insert(1, k)
    return num

if __name__ == "__main__":
    arr = [int(input()), int(input())]
    arr.append(abs(arr[0]**2, ar{1]**2))
    print(" ".join(list(map(str, arr))))
