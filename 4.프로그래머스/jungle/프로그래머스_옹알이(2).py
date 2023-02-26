def check(word):
    can_speak = ["aya", "ye", "woo", "ma"]
    last_word = []
    word = list(word)

    i = 0
    while i < len(word):
        find = False
        for speak in can_speak:
            if ''.join(word[i:i+len(speak)]) == speak:
                if last_word == speak:
                    return False
                last_word = speak
                i+=len(speak)
                find = True

        if not find :
            return False
        
    return True


def solution(babbling):
    res = 0
    for b in babbling:
        if check(b):
            res+=1
    return res



babbling = ["ayaye"]
print(solution(babbling))