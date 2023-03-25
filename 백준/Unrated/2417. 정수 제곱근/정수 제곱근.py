def check(mid):
    if mid ** (2) >= n:
        return True
    return False

n = int(input())

left = 0
right = n

while left+1 < right:
    mid = (left+right) // 2

    if not check(mid):
        left = mid 
    else:
        right = mid

print(right)
