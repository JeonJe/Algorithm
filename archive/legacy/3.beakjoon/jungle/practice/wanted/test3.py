import sys
input = sys.stdin.readline
N = int(input())
A = [ i for i in range(N+1) ]
B = [ i for i in range(N+1) ]

dp = [0] * (N+1)
dp[1] = 1

for i in range(2,N+1):
    
    temp_max = 0
    for j in range(i,0,-1):
        if A[i] > B[j] and dp[j] > temp_max:
            temp_max = dp[j]
    dp[i] = temp_max+1
    
print(max(dp))