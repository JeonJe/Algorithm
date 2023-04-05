



k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]


def solution(k, m, score):
    score.sort(reverse = True)
    res = 0
    for i in range(0,len(score),m):
        #m개 만큼 돌 수 있으면
        if i + m - 1 < len(score):
            small = score[i + m - 1]
            res += small * m
    return res


print(solution(k,m,score))