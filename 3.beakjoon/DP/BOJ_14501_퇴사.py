import sys
input = sys.stdin.readline

n = int(input())
Ti = [0]*(n+1)
Pi = [0]*(n+1)

for i in range(n):
    t, p = map(int,input().split())
    Ti[i] = t
    Pi[i] = p

dp = [0]*(n+1)
for i in range(n-1,-1,-1):
    if i + Ti[i] <= n:
        dp[i] = max(dp[i+1], dp[i+Ti[i]]+Pi[i])
    else:
        dp[i] = dp[i+1]

print(max(dp))
