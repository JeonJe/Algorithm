import sys 

input = sys.stdin.readline
n, k = map(int,input().split())
# dp = [ [0]*(k+1) for i in range(n+1) ]
dp = [0] * (k+1)

# for i in range(1,n+1):
    # dp[i][0] = 1
dp[0] = 1

coins = [ int(input()) for _ in range(n) ]
# coins.insert(0,0)

for coin in coins:
    for j in range(1, k+1):
        if j - coin >= 0:
            dp[j] += dp[j-coin]
        # dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

print(dp[k])

