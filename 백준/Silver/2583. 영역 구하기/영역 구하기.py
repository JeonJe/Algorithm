from collections import deque 

height, width, k = map(int,input().split())

board = [ [0 for _ in range(width)] for _ in range(height) ]
visited = [ [False for _ in range(width)] for _ in range(height) ]

cnt = 0
for _ in range(k):
    lx,ly ,rx,ry = map(int,input().split())

    for i in range(ry-ly):
        for j in range(rx-lx):
            board[ly+i][lx+j] = 1

def bfs(x,y):
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]

    que = deque()
    que.append((x,y))    
    area = 1
    while que:
        cx, cy = que.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < height and 0 <= ny < width:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    visited[nx][ny] = True 
                    que.append((nx,ny))
                    area+=1
    return area


area = []
for i in range(height):
    for j in range(width):
        if not visited[i][j] and board[i][j] == 0:
            cnt+=1
            visited[i][j] = True
            area.append(bfs(i,j))
print(cnt)
area.sort()
print(*area)