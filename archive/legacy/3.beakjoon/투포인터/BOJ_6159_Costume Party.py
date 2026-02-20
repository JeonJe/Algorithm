
n, s = map(int,input().split())

cows = [int(input()) for _ in range(n)]
cows.sort()

left , right = 0, n-1
cnt = 0

while left < right:
    
    if cows[left] + cows[right] <= s :
        cnt += right - left
        left += 1
    else:
        right -= 1

print(cnt)