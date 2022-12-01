n = int(input())

graph = [ list(map(int,input().split())) for _ in range(n)]
dp = [ [0]*n for _ in range(n) ]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        weight = graph[i][j]
        #오른쪽
        if j + weight >= n or dp[i][j] == 0:
            pass
        else:
            dp[i][j+weight] += dp[i][j]

        #아래
        if i + weight >= n or dp[i][j] == 0:
            pass
        else:
            dp[i+weight][j] += dp[i][j]


print(dp[n-1][n-1])
