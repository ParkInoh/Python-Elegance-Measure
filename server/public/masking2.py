

def hide_vowels(word, mark):
    for i in word:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            i = mark
        print(i, end="")

if __name__ == "__main__":
    a = list(input())
    b = input()
    hide_vowels(a, b)
