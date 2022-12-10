from collections import deque 

n, m, k = map(int,input().split())

graph = [ ['.'] * m for _ in range( n ) ]
visited = [[False]*m for _ in range(n)]

for _ in range(k):
    i, j = map(int,input().split())
    graph[i-1][j-1] = '#'

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def bfs(i,j):
    visited[i][j] = True
    que = deque()
    que.append((i,j))
    cnt = 1
    while que:
        qx,qy = que.popleft()

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] == '#':
                visited[nx][ny] = True 
                que.append((nx,ny))
                cnt += 1
    return cnt
    
k = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == '#':
            k = max(k, bfs(i,j))
print(k)