from collections import deque

def solution(s):
    answer = 0
    s = list(s)
    compare_char = ""
    same, diff = 0,0
    for c in s:
        if not compare_char:
            compare_char = c
        
        if compare_char == c:
            same+=1
        else:
            diff+=1
        
        if same == diff:
            answer+=1
            same = 0
            diff = 0
            compare_char = ""
    if compare_char:
        answer += 1
    return answer
