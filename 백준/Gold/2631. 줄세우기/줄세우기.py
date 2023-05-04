n = int(input())
nums = [int(input()) for _ in range(n)]

dp = [0]*(n)
dp[0] = 1

#i번째까지 LIS
for i in range(1,n):
    temp = 0
    for j in range(i-1,-1,-1):
        if nums[j] < nums[i]:
            temp = max(temp, dp[j])
    dp[i] = temp+1
print(n-max(dp))