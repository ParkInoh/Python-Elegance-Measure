
def cnt_jewels(jewels):
    jewels_dict = {}
    largest_num = 0
    jewels_num = len(jewels)
    for jewel in jewels:
        if jewel in jewels_dict.keys():
            jewels_dict[jewel] += 1
        else:
            jewels_dict[jewel] = 1
    largest_num = max(jewels_dict.values())
    print(largest_num)
    print(f"{largest_num / jewels_num:.2f}")
if __name__ == "__main__":
    items = input().split()
    cnt_jewels(items)