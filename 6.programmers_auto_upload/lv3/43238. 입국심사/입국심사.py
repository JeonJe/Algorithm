
def check(target,times,n):
    cnt = 0
    for time in times:
        cnt += ( target // time )
    if cnt >= n:
        return True 

    return False

def solution(n, times):
    left = -1
    right = max(times) * n

    while (left+1 < right):
        mid = (left+right) // 2

        if not check(mid,times,n):
            left = mid
        else:
            right = mid
    
    return right