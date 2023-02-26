
#N이 열의 개수 
#M이 행의 개수 
from collections import deque
import sys

N, M = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(N) ]

dx = [ -1,-1,0,1,1,1,0,-1 ]
dy = [ 0,-1,-1,-1,0,1,1,1 ]

def bfs(x,y):
    visited = [ [False] * M for _ in range(N) ]
    que = deque()
    que.append((x,y,0))
    visited[x][y] = True
    ans =  sys.maxsize
    while que:
        cx,cy,cnt = que.popleft()

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 1:
                    ans = min(ans, cnt+1)
                    break
                if not visited[nx][ny] and graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append((nx,ny,cnt+1))
                
    return ans

ans = -1
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            ans = max(ans,bfs(i,j))

print(ans)