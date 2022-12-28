
n = int(input())
# 수의 길이
dp = [ [0] * (10) for i in range(n) ]

for i in range(10):
    dp[0][i] = 1

for i in range(1,n):
    for j in range(10):
        temp = 0
        for k in range(j+1):
            temp += dp[i-1][k]%(10007)
        dp[i][j] = temp 


print(sum(dp[n-1])%(10007))
