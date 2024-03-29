import sys

input = sys.stdin.readline
T = int(input())


for _ in range(T):
    arr =[]
    n = int(input())

    dp = [ [0 for _ in range(n)] for _ in range(2)]

    for _ in range(2):
        arr.append(list(map( int, input().split())))

    if n == 1:
        print(max(arr[0][0],arr[1][0]))
    else:
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[1][0] + arr[0][1]
        dp[1][1] = arr[0][0] + arr[1][1]

        for i in range (2,n):
            dp[0][i] = max(dp[1][i-1],dp[1][i-2]) + arr[0][i]
            dp[1][i] = max(dp[0][i-1],dp[0][i-2]) + arr[1][i]

        print(max(dp[0][n-1],dp[1][n-1]))




