def find_len_seq(integer):
    set_int = []

    if integer == 1:
        return 1

    while True:

        integer = sum([int(d) ** 2 for d in list(str(integer))])

        if integer in set_int:
            return -1
        set_int.append(integer)

        if integer == 1:
            return len(set_int) + 1

def main():
    n = int(input())
    print(find_len_seq(n))
if __name__ == "__main__":
    main()
