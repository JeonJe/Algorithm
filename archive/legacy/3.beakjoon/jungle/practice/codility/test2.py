from collections import deque


def solution(S, C):
    list_s = list(S)
    stack = []
    stack.append((S[0],C[0])) 
    res = 0
    

    for i in range(1,len(list_s)):
        #같은문자가 연속되는 상황이면
        if stack[-1][0] == list_s[i]:
            
            if stack[-1][1] <= C[i]:
                pop_s, pop_c = stack.pop()
                stack.append((list_s[i],C[i]))
                res += pop_c
            #새로 들어온 값이 더 작으면 바로 지운다고 가정 
            else:
                res += C[i]
        else:
            stack.append((list_s[i],C[i]))
    return res

S = "aaaa"
C = [3,4,5,7]
print(solution(S,C))