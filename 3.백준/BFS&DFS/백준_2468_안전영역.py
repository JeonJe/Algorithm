from collections import deque

dx = [ -1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,height,visited):
    visited[x][y] = True
    deq= deque()
    deq.append((x,y))

    while deq:
        cx,cy = deq.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<=nx<n and 0<=ny<n and arr[nx][ny]>height and visited[nx][ny]==False:
                visited[nx][ny] = True
                deq.append((nx,ny))

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, arr))

res = 0

for h in range(max_height):
    visited = [ [False]*n for _ in range(n)]
    temp = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and visited[i][j]==False:
                bfs(i,j,h,visited)
                temp+=1
    if temp > res:
        res = temp

print(res)


