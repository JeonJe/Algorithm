
def solution(d, budget):
    d.sort()
    res = 0
    i = 0
    while budget > 0 and i < len(d):
        budget -=  d[i]
        if budget < 0:
            break
        res += 1
        i += 1

    return res