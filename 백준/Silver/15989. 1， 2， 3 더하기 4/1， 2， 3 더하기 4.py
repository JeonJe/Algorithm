t = int(input())

n = 10000
dp = [1]*(n+1)
for i in range(2,n+1):
    dp[i] += dp[i-2]
for i in range(3,n+1):
    dp[i] += dp[i-3]
        
for _ in range(t):
    n = int(input())
    print(dp[n])
