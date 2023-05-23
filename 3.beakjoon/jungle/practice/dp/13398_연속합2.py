import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = [[0,0] for _  in range(n)]
dp[0][0] = nums[0]

if n == 1:
    print(nums[0])
    exit(0)

answer = -1e9
for i in range(1,n):
    dp[i][0] = max(nums[i], dp[i-1][0]+nums[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]+nums[i])
    answer = max(answer,dp[i][0], dp[i][1])

print(answer)
