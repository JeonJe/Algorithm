
n = int(input())

dp = [1e9] *(n+5)
#i부터 1을 만들기 위한 연산 횟수 
dp[0],dp[1] = 0,0
dp[2],dp[3] = 1,1

for i in range(4,n+5):
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 ==0:
        dp[i] = min(dp[i], dp[i//2]+1)
 
    dp[i] = min(dp[i], dp[i-1]+1)

print(dp[n])

