import sys

n = int(input())

coins = [1,2,5,7]
dp = [sys.maxsize]*(n+1)
dp[0] = 0

for i in range(1,n+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin] + 1)
        else:
            continue
print(dp[n])