def get_median():
    numbers = list(map(float,input().split()))
    numbers.sort()
    median = 0
    if len(numbers) % 2 == 1:
        median = numbers[(len(numbers) + 1) // 2 - 1]
    elif len(numbers) % 2 == 0:
        median = numbers[(len(numbers) // 2) - 1] + numbers[len(numbers) // 2]) / 2
    return median

if __name__ == "__main__":
    print(f"{get_median():.1f}")