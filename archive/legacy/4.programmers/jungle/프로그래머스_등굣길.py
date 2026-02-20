

def solution(m, n, puddles):
    graph = [[0]*m for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(len(puddles)):
        puddles[i][0], puddles[i][1] = puddles[i][1], puddles[i][0]

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j ==1:
                continue

            if [i,j] in puddles:
                dp[i][j] = 0
                continue
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % (1000000007)
            
    return dp[n][m]

m = 4
n = 3
puddles = [[2, 2]]
print(solution(m, n, puddles))
