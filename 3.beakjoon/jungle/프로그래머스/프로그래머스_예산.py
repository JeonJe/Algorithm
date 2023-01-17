
def solution(d, budget):
    d.sort()
    res = 0
    i = 0
    while budget > 0 or i < len(d):
        budget -=  d[i]
        if budget < 0:
            break
        res += 1
        i += 1

    return res


d = [1,3,2,5,4]
budget = 9

print(solution(d,budget))