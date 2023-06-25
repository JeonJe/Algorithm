cnt = 0
n = int(input())

dp = [0]*(51)

dp[0] = 1
dp[1] = 1
dp[2] = 3
dp[3] = 5

for i in range(4,51):
    dp[i] = (dp[i-2] + dp[i-1] + 1) % 1000000007

print(dp[n])
