t = 1 
n, l = 5,1000

seq = [ list(map(int,input().split())) for _ in range(n) ]
dp = [[0 for _ in range(l)] for _ in range(n+1)]

for i in range(1,n+1):
    cur_point, cur_cal = seq[i-1]
    for j in range(1,l+1):
        if j < cur_cal:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_point] + cur_point)
print(max(dp))