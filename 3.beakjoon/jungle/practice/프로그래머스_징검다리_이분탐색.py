
def check(mid,rocks):
    #mid로 들어온 돌과 돌 사이의 거리가 n개의 바위를 제거 한 뒤 
    #돌 간의 거리보다 작은 지?
    diff = []
    for i in range(len(rocks)-1):
        diff.append(rocks[i+1] - rocks[i])
    
    cnt = 0
    cur = 0
    for j in range(len(diff)):
        cur += diff[j]
        if cur < mid:
            cnt += 1
        else:
            cur = 0
           
    if cnt > n :
        return False
    else:
        return True



# 이분 탐색의 기준은 돌과 돌 사이의 거리 
def solution(distance, rocks, n):
    left = 0
    right = distance + 1
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()

    while left + 1 < right:
        mid = (left + right) // 2
        if check(mid,rocks):
            left = mid 
        else:
            right = mid 

    return left

distance = 10 
rocks = [3,5,7]
n = 2
print(solution(distance,rocks,n))