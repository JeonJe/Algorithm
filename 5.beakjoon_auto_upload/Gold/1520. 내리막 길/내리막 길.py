
#세로의 크기 M,
#가로의 크기 N
import sys
input = sys.stdin.readline

M,N = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(M) ]
visited = [ [False] * N for _ in range(M) ]
dp = [ [-1] * N for _ in range(M) ]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    height = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] < height:
                dp[x][y] += dfs(nx,ny)
    return dp[x][y]
    
dfs(0,0)
print(dp[0][0])
