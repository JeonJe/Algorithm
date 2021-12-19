
# # import sys
sys.stdin = open("input.txt",'rt')

n = int(input())
arr = list(map(int,input.split()))
arr=[]
arr.append(0)
arr.append(map(int,input().split()))

dp = [0]*1001
dp[1] = 1

for i in range(2,n+1):
    max_temp = 0
    for k in range(i-1,0,-1):
        if arr[i] > arr[k]:
            max_temp = max(max_temp,dp[k])
    dp[i] = max_temp+1

print(max(dp))

