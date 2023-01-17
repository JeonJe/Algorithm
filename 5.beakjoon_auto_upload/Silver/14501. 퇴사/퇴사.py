n = int(input())


arr = [list(map(int,input().split())) for _ in range(n)]

dp = [0]*(n+1)

for i in range(n-1,-1,-1):
    t = arr[i][0]
    p = arr[i][1]
    
    if i + t <= n:
        dp[i] = max(dp[i+1], p + dp[i+t])
    else:
        dp[i] = dp[i+1]

print(max(dp))