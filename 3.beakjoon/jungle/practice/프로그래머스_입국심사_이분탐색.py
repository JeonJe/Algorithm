

def check(target,times):
    cnt = 0
    for time in times:
        cnt += ( target // time )
    if cnt >= n:
        return True 

    return False
#심사원 수
#각 심사원 시간 
def solution(n, times):
    
    left = -1
    right = max(times) * n

    while (left+1 < right):
        mid = (left+right) // 2

        if not check(mid,times):
            left = mid
        else:
            right = mid
    
    return right


n = 6
times = [7,10]

print(solution(n,times))