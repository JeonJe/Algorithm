import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
dp = [[0,0] for _  in range(n)]
dp[0][0] = nums[0]

if len(nums) == 1:
    print(dp[0][0])
    exit()

res = -1e9
for i in range(1,len(nums)):
    dp[i][0] = max(nums[i], dp[i-1][0]+nums[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + nums[i])
    res = max(res,dp[i][0], dp[i][1])

print(res)
