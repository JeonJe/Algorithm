from collections import deque
#가로의 크기 N, 세로의 크기 M
M , N  = map(int,input().split())

visited = [ [False] * (M) for _ in range(N)]
graph = [ list(input()) for _ in range(N) ]

blue, white = 0, 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    visited[x][y] = True
    que = deque()
    que.append((x,y))
    cur = graph[x][y]
    cnt = 1
    while que:
        cx,cy = que.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nx < N and 0<= ny <M:
                if not visited[nx][ny] and graph[nx][ny] == cur:
                    visited[nx][ny] = True
                    que.append((nx,ny))
                    cnt+=1
    return cnt ** 2



for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            s = bfs(i,j)
            if graph[i][j] == 'W':
                white += s
            else:
                blue += s

print(white, blue)