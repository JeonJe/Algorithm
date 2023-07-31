from collections import deque

height, width = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(height)]
visited = [[False] * width for _ in range(height)]

cnt = 0
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,-1,-1,-1,0,1,1,1]
def bfs(x,y):
  que = deque()
  que.append((x,y))    

  while que:
      cx, cy = que.pop()
      for i in range(8):
          nx = cx + dx[i]
          ny = cy + dy[i]

          if 0 <= nx < height and 0 <= ny < width:
              if not visited[nx][ny] and graph[nx][ny] == 1:
                  visited[nx][ny] = True
                  que.append((nx, ny))
  return 

for i in range(height):
    for j in range(width):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            bfs(i,j)

print(cnt)