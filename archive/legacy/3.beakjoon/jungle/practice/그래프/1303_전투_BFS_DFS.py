from collections import deque 

N, M = map(int,input().split())

graph = [ input() for _ in range(M) ]
visited = [ [False] * N for _ in range(M) ]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j):
    que = deque()
    visited [i][j] = True
    que.append((i,j))
    n = 1
    cur_color = graph[i][j]
    while que:
        x, y = que.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] == cur_color:
                visited[nx][ny] = True 
                que.append((nx,ny))
                n += 1
    return n 



white, blue = 0,0 
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            n = 0
            n = bfs(i,j)
            if graph[i][j] == 'W':
                white += n ** 2
            else:
                blue += n ** 2

print(white, blue)