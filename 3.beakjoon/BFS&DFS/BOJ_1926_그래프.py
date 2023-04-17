from collections import deque

n,m = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    que = deque()
    graph[i][j] = 2
    que.append((i,j))
    area = 1

    while que:
        cx,cy = que.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0<= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 2
                    area += 1
                    que.append((nx,ny))
    return area


cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt+=1
            max_area = max(max_area,bfs(i,j))

print(cnt,max_area)