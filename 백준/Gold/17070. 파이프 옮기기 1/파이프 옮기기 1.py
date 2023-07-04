import sys 
input = sys.stdin.readline

N = int(input())
board = [ list(map(int,input().split())) for _ in range(N) ]

# 0 가로, 1 세로, 2 대각선
dp = [ [[0 for _ in range(N) ] for _ in range(N)] for _ in range(3) ]


def memorization():

    dp[0][0][1] = 1
    #0행은 이전 파이프가 가로밖에 올 수 없음
    for i in range(2,N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]

    #0열은 파이프가 올 수 없음
    for i in range(1,N):
        for j in range(1,N):
            if board[i][j] == 0 and board[i][j-1] == 0 and board[i-1][j] == 0:
                dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
            
            if board[i][j] == 0:
                dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
                dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]

    cnt = 0
    for i in range(3):
        cnt += dp[i][N-1][N-1]
    return cnt
    
print(memorization())