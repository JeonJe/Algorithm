import sys
input = sys.stdin.readline

n, k = map(int,input().split())

dp = [0]*(k+1)

backpack = [ list(map(int,input().split())) for _ in range(n) ]


for cur_weight, cur_value in backpack:
    visited = [False]*(k+1)
    for i in range(k,cur_weight-1,-1):
        dp[i] = max(dp[i], dp[i-cur_weight] + cur_value)    

print(max(dp))
