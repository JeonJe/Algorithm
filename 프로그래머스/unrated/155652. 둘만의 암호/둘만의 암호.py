
def solution(s, skip, index):
    answer = ''

    alpha = [chr(i) for i in range(97,123)]
    for i in skip:
        alpha.remove(i)
    alpha *= 4

    for a in s:
        answer += alpha[alpha.index(a)+index]
        
    return answer