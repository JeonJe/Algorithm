import sys
N,C = map(int,input().split())

def check(candidate):
    
    f = arr[0]
    cnt = 1
    for i in range(1,len(arr)):
        if arr[i] >= f + mid:
            cnt += 1
            f = arr[i]
            
    if cnt < C:
        return False
    else:
        return True 


arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()


lo = 0
hi = max(arr) - min(arr) + 1

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if(check(mid)): lo = mid
    else: hi = mid

print(lo)