from collections import deque

N, K = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())
virus = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    que = deque(virus)
    while que:
        cval, cx, cy, sec  = que.popleft()
        if sec == S:
            break

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = cval
                    que.append((cval,nx,ny, sec+1))
    

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus.append((graph[i][j],i, j, 0))

virus.sort()
bfs()
print(graph[X-1][Y-1])
