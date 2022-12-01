import sys
n = int(input())
matrix = [ list(map(int,input().split())) for _ in range(n) ]
dp = [ [0]*(n) for _ in range(n) ]

#주 대각선을 제외한 대각선
for diagonal in range(1,n):
    #대각선이 점점 짧아짐
    for i in range(n - diagonal):
        #현재 대각선에서 몇 번째 원소인지를 정하는 것
        j = i + diagonal
        dp[i][j] = sys.maxsize
        for k in range(i,j):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+matrix[i][0]*matrix[k][1]*matrix[j][1])


print(dp[0][-1])