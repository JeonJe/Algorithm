import sys
t = int(input())

dp = [[0] * 30 for _ in range(30)]


for _ in range(t):
    N, M = map(int, input().split())
    # mCn = m! / n!(m-n)!
    for i in range(30):
        for j in range(30):
            if i == 1:
                dp[i][j] = j
            else:
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    print(dp[N][M])