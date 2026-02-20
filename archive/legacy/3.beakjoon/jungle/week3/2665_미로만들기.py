import sys
from collections import deque
n = int(input())

graph = [ list(map(int,input())) for _ in range(n)]
distance = [ [sys.maxsize]*n for _ in range(n)]
visited = [ [False]*n for _ in range(n)]

dx = [ 0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x,y):
    visited[x][y] = True
    distance[x][y] = 0
    que = deque()
    que.append((x,y))

    while que:
        qx,qy = que.popleft()
    
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
                    
            if not visited[nx][ny]:
                visited[nx][ny] = True
                
                if graph[nx][ny] == 1:
                    distance[nx][ny] = distance[qx][qy]
                    que.appendleft((nx,ny))
                elif graph[nx][ny] == 0:
                    distance[nx][ny] = distance[qx][qy]+1
                    que.append((nx,ny))


bfs(0,0)
for i in range(n):
    for j in range(n):
        print(distance[i][j], end=' ')
    print()
print()
print(distance[n-1][n-1])
