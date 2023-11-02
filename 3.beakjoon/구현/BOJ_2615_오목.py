from collections import deque 

n = 19
board = [list(map(int,input().split())) for _ in range(n)]

#북,북동,동,남동
dx = [-1,-1,0,1]
dy = [0,1,1,1]

def find_omok(x, y, color):
 
    #현재 좌표를 기준으로 상하, 좌우, 대각선(2개) 돌려서 5목 만들어지는지 확인
    for i in range(4):
        points = []
        points.append((x,y))

        cx,cy = x,y
        #한쪽방향으로 확인
        while True:
            nx,ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == color:
                if (nx, ny) not in points:
                    points.append((nx,ny))
                cx, cy = nx, ny
            else:
                break
        
        #반대방향으로 확인
        while True:
            nx,ny = cx - dx[i], cy - dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == color:
                if (nx, ny) not in points:
                    points.append((nx,ny))
                cx, cy = nx, ny
            else:
                break
        
        if len(points) == 5:
            print(color)
            points.sort(key=lambda  x : (x[1],x[0]))
            print(points[0][0]+1, points[0][1]+1)
            exit(0)

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            find_omok(i,j,board[i][j])

print(0)