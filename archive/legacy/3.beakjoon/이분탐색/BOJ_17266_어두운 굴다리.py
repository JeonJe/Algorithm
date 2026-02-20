def check(mid):
    prev = 0
    for i in range(1,len(points)-1):
        if points[i] - mid <= prev:
            prev = points[i] + mid
        else:
            return False 
        
    return points[-1] - prev <= 0
    
    
n = int(input())
M = int(input())
points = list(map(int,input().split()))
points.insert(0,0)
points.append(n)

left = 0
right = n

while left + 1 < right:
    mid = (left+right) // 2

    if check(mid):
        right = mid 
    else:
        left = mid

print(right)