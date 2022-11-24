

#세로의 크기 M,
#가로의 크기 N
from collections import deque
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
    

#시간초과 dfs 
# def dfs(x,y):
#     stack = deque()
#     stack.append((x,y))
#     visited[x][y] = True
    
#     cnt = 0
#     while stack:
#         i, j = stack.pop()

#         if i == M-1 and j == N-1:
#             cnt+=1

#         weight = graph[i][j] 
#         for k in range(4):
#             nx = i+dx[k]
#             ny = j+dy[k]

#             if 0<= nx < M and 0<= ny < N:
#                 if graph[nx][ny] < weight:
#                     stack.append((nx,ny))
#                     visited[x][y] = True 
#                     dp[nx][ny] += 1

            
dfs(0,0)
print(dp[0][0])
# for i in range(M):
#     print(dp[i])
# print(dp[M-1][N-1])
