
t = int(input())

for _ in range(t):
    #k층
    k = int(input())
    #n호
    n = int(input())
    dp = [ [0]*(n+1) for _ in range(k+1) ]

    for i in range(n+1):
        dp[0][i] = i
    
    for i in range(1,k+1):
        for j in range(n+1):
            for z in range(j+1):
                dp[i][j] += dp[i-1][z]

    print(dp[k][n])

