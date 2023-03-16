def check(m):
    if m*(m+1)//2 <= n:
        return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())

    left = 1
    right = n

    while left+1< right:
        mid = (left+right)//2

        if check(mid):
            left = mid
        else:
            right = mid
    print(left)