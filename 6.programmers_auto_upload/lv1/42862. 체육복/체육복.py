def solution(n, lost, reserve):
    ans = n - len(lost)
    lost.sort()
    reserve.sort()
    
    for i in range(len(lost)):
        len_reserve = len(reserve)
        for j in range(len_reserve):
            if abs(lost[i] - reserve[j]) <= 1:
                ans += 1
                del reserve[j]
                break
    # print(ans)
    return ans