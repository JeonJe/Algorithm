


def is_vowels(chr):
    if chr in ['a','e','i','o','u']:
        return True
    else:
        return False
    
def is_good_password(password):
    #모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    find_vowels = False

    for chr in password:
        if is_vowels(chr):
            find_vowels = True
            break

    if not find_vowels:
        return False
    
    #모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    consonants_cnt = 0
    vowels_cnt = 0
    prev = password[0]
    if is_vowels(prev):
        vowels_cnt = 1
    else:
        consonants_cnt = 1

    for i in range(1,len(password)):
        if is_vowels(prev) and is_vowels(password[i]):
            vowels_cnt += 1
        
        elif not is_vowels(prev) and not is_vowels(password[i]):
            consonants_cnt += 1
        
        elif is_vowels(prev) and not is_vowels(password[i]):
            vowels_cnt = 0
            consonants_cnt = 1
        else:
            vowels_cnt = 1
            consonants_cnt = 0
        if consonants_cnt == 3 or vowels_cnt == 3:
            return False
        prev = password[i]

    #같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    prev = password[0]
    for i in range(1,len(password)):
        if password[i] == prev:
            if password[i] == 'e' or password[i] == 'o':
                pass
            else:
                return False
        prev = password[i]
    
    return True 
                

while True:
    password = input()

    if password == "end":
        break

    if is_good_password(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')