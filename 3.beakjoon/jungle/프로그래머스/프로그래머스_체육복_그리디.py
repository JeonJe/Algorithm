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
            

            
    
n = 8
lost = [3, 4, 7, 8]
reserve = [1, 2, 3, 4, 5, 7, 8]
print(solution(n,lost,reserve))