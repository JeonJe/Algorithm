
def check(mid):

    total = 0
    for each in seq:
        total += mid // each
    
    if total >= m:
        return True
    else:
        return False

n, m = map(int,input().split())
seq = list(map(int,input().split()))

left = 0
right = max(seq) * m 

while left + 1 < right:
    mid = (left + right) // 2

    if not check(mid):
        left = mid
    else:
        right = mid

print(right)