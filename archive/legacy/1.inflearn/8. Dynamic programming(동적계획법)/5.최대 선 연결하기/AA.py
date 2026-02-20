import sys

# sys.stdin = open("input.txt",'r') 

N = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
dp = [0] * (N+1)
dp[1] = 1

for i in range(2,N+1):
    
    temp_max = 0
    for j in range(i,0,-1):
        if arr[i] > arr[j]:
            temp_max = max(temp_max,dp[j])
    dp[i] = temp_max+1
    
print(max(dp))

