n = int(input())
nums = list(map(int,input().split()))

if n == 1:
    print(nums[0])
    exit(0)

LIS_sum = [0]*(n)
LIS_sum[0] = nums[0]

for i in range(1,n):
    
    temp = 0
    for j in range(i-1,-1,-1):
        if nums[j] < nums[i]:
            temp = max(temp, LIS_sum[j])
    
    LIS_sum[i] = temp+nums[i]
    

print(max(LIS_sum))