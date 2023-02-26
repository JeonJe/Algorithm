def solution(triangle):
    answer = 0
    len_t = len(triangle)
    dp = [[0] * len_t for _ in range(len_t) ]
    if len_t == 1:
        return triangle[0]
    dp[0][0] =triangle[0][0]

    for i in range(1,len_t):
        for j in range(i+1):
            if j == 0:
                dp[i][j] =  dp[i-1][j]+triangle[i][j]
            elif j == i+1:
                dp[i][j] = dp[i-1][j-1]+triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j]+triangle[i][j], dp[i-1][j-1]+triangle[i][j])


    return max(dp[len_t-1])