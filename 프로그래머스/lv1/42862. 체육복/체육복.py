def solution(n, lost, reserve):

    set_reserve = list(set(reserve)-set(lost))
    set_lost = list(set(lost)-set(reserve))
    ans = n - len(set_lost)
    for i in range(len(set_lost)):
        for j in range(len(set_reserve)):
            if abs(set_lost[i] - set_reserve[j]) <= 1:
                ans += 1
                del set_reserve[j]
                break
    return ans
            
