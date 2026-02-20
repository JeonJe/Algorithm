
k, n = map(int,input().split())

arr = [ int(input()) for _ in range(k) ]
arr.sort()

lo = 0 
hi = max(arr)+1

def check(mid):
    cnt = 0
    for i in range(len(arr)):
        cnt += arr[i] // mid
    if cnt >= n :
        return True
    else:
        return False

while lo + 1 <  hi:
    mid = (lo + hi) // 2

    if check(mid):
        lo = mid
    else:
        hi = mid

print(lo)