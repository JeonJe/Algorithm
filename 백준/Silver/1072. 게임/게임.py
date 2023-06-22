
X,Y = map(int, input().split())
Z = Y * 100 // X

left = 0
right = 1000000000

while left + 1 < right:
    #추가 게임 수 
    mid = (left + right) // 2
    
    if (Y+mid) * 100 // (X+mid) > Z:
        right = mid
    else:
        left = mid

if Z >= 99:    
    print(-1)
else:
    print(right)