from collections import defaultdict

def solution(weights):
    answer = 0
    check_weight = defaultdict(int)

    for w in weights:
        #1배
        if check_weight[w] != 0:
            answer += check_weight[w]
        # 2배
        if (w*2) <= 1000 :
            answer += check_weight[w*2]
    
        #1/2배
        if w % 2 == 0 and 100 <= w*(1/2):
            answer += check_weight[w*(1/2)]

        #3/2배
        if w % 2 == 0 and w*(3/2) <= 1000:
            answer += check_weight[w*(3/2)]

        #2/3배
        if w % 3 == 0 and 100 <= w*(2/3):
            answer += check_weight[w*(2/3)]

        #4/3배
        if w % 3 == 0 and w*(4/3) <= 1000:
            answer += check_weight[w*(4/3)]

        #3/4배
        if w % 4 == 0 and 100 <= w*(3/4):
            answer += check_weight[w*(3/4)]

        check_weight[w] += 1

    return answer 