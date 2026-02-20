n, k = map(int,input().split())

coins = [ int(input()) for _ in range(n) ]

# dp = [ [0]*(k+1) for _ in range(n) ]
dp = [0]*(k+1) 
# for i in range(n):
    # dp[i][0] = 1 
dp[0] = 1

for i in range(n):
    for j in range(1,k+1):
        if j >= coins[i]:
            dp[j] = dp[j] + dp[j-coins[i]]

print(dp[k])
