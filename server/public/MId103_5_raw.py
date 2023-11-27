def find_len_seq(integer):
    num_seq = 1
    set_int = []

    if integer == 1:
        return num_seq
    
    while True:
        new_integer = 0
        int_list = list(str(integer))

        for i in range(0, len(int_list)):
            new_integer += int(int_list[i]) ** 2
        num_seq += 1
        integer = new_integer

        for i in range(0, len(set_int)):
            if set_int[i] == integer:
                return -1
        set_int.append(integer)
        
        if integer == 1:
            return num_seq

def main():
    n = int(input())
    print(find_len_seq(n))
if __name__ == "__main__":
    main()
