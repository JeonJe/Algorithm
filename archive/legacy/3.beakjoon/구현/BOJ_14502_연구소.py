import copy
from collections import deque
height, width = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(height)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
virus = []
empty_area = []

def bfs():
    visited = [ [False for _ in range(width)] for _ in range(height)  ]
    for i in range(len(virus)):
        x, y = virus[i]

        visited[x][y] = True
        que = deque()
        que.append([x,y])

        while que:
            cx, cy = que.pop()

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < height and 0 <= ny < width:
                    if not visited[nx][ny] and board[nx][ny] == 0:
                        visited[nx][ny] = True
                        que.append([nx,ny])

    cnt = 0
    for i in range(height):
        for j in range(width):
            if board[i][j] == 0 and not visited[i][j]:
              cnt += 1                    
    return cnt

for i in range(height):
    for j in range(width):
        if board[i][j] == 2:
            virus.append([i, j])
        elif board[i][j] == 0:
            empty_area.append([i, j])
answer = 0
for i in range(len(empty_area)-2):
    for j in range(i+1, len(empty_area)-1):
        for k in range(j+1, len(empty_area)):
            board[empty_area[i][0]][empty_area[i][1]] = 1
            board[empty_area[j][0]][empty_area[j][1]] = 1
            board[empty_area[k][0]][empty_area[k][1]] = 1
            answer = max(answer,bfs())
            board[empty_area[i][0]][empty_area[i][1]] = 0
            board[empty_area[j][0]][empty_area[j][1]] = 0
            board[empty_area[k][0]][empty_area[k][1]] = 0
print(answer)
  