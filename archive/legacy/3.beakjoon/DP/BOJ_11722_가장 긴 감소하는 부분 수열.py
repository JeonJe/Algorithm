n = int(input())
nums = list(map(int,input().split()))

dp = [1] * (n)

for i in range(1,n):
    temp = 0

    for j in range(i-1,-1,-1):
        if nums[j] > nums[i]:
            temp = max(temp,dp[j])
    temp += 1
    dp[i] = temp 

print(max(dp))

    