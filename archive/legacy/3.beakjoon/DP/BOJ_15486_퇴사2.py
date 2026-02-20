
n = int(input())

seq = [list(map(int,input().split())) for _ in range(n)]
dp = [0]*(n+1)

for i in range(n-1,-1,-1):
    Ti = seq[i][0]
    Pi = seq[i][1]

    if i + Ti <= n:
        dp[i] = max(dp[i+1], dp[i+Ti]+Pi)
    else:
        dp[i] = dp[i+1]

print(max(dp))