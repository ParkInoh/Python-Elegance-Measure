def rule0failed(pw):
    vowel = 'aeiou'
    for i in pw:
        if i not in vowel:
            continue
        else:
            return False
    return True

def rule1failed(pw):
    alphalist = "abcefgijklmnopqrstuvxyz"*2
    for i in range(len(pw) - 1):
        if pw[i] == pw[i + 1]:
            if pw[i] in alphalist:
                return True            
    return False
def rule2failed(pw):
    vowel = 'aeiou'
    num_vowel = 0
    num_conson = 0
    for i in range(len(pw) - 2):
        if not pw[i].isalpha() or not pw[i+1].isalpha() or not pw[i+2].isalpha():
            continue
        if pw[i] in vowel:
            num_vowel += 1
        else:
            num_conson += 1
        if pw[i + 1] in vowel:
            num_vowel += 1
        else:
            num_conson += 1
        if pw[i + 2] in vowel:
            num_vowel += 1
        else:
            num_conson += 1
    
    return False

    return False
def rule3failed(pw):
    special = "!@#$%&<>?"
    for i in pw:
        if i in special:
            return True
    return False

def pwscore(pw):
    score = 0
    if rule0failed(pw):
        score += 1 # 0?
    if rule1failed(pw):
        score += 2
    if rule2failed(pw):
        score += 4
    if rule3failed(pw):
        score += 8
    return score

def main():
    line = input()
    score = pwscore(line)
    if score == 0:
        print(line)
    else:
        print(score)

if __name__ == "__main__":
    main()

