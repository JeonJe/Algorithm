from collections import deque

t = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    while que:
        cx, cy = que.pop()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < height and  0 <= ny < width:
                if not visited[nx][ny] and graph[nx][ny] == "#":
                    que.append((nx,ny))
                    visited[nx][ny] = True

for _ in range(t):
    height, width = map(int,input().split())
    graph = [ list(input()) for _ in range(height) ]
    visited = [ [False for _ in range(width)] for _ in range(height) ]
    answer = 0
    for i in range(height):
        for j in range(width):
            if not visited[i][j] and graph[i][j] == "#":
                answer += 1
                bfs(i,j)
    print(answer)  


