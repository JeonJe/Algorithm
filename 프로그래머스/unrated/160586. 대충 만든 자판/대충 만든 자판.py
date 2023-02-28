from collections import defaultdict

def solution(keymap, targets):
    answer = []
    dict = defaultdict()

    for k in keymap:
        for index, value in enumerate(k):
            if value in dict.keys():
                dict[value] = min(dict[value], index)
            else:
                dict[value] = index
    
    for T in targets:
        temp = 0
        not_found = False
        for c in T:
            if c not in dict.keys():
                not_found = True
            else:
                temp += dict[c] + 1

        if not_found:
            answer.append(-1)
        else:
            answer.append(temp)

    return answer
