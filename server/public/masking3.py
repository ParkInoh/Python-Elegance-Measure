# -*- coding: utf-8 -*-
def hide_vowels(word, mark):
    c = []
    for i in word:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            i = mark
        c.append(i)

    return ''.join(c)
    
if __name__ == "__main__":
    a = list(input())
    b = input()
    masked_word = hide_vowels(a, b)
    print(masked_word)
