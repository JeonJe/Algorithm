import sys
input = sys.stdin.readline

n = int(input())
num = int(input())

board = [[0] * n for _ in range(n)]
current = n**2

#남동북서
dx = [1,0,-1,0 ]
dy = [0,1,0,-1]

cx,cy = 0,0
direct = 0

board[0][0] = current
current -= 1

while current > 0:
    nx = cx+dx[direct]
    ny = cy+dy[direct]

    #다음 좌표가 판 안일 경우 
    if 0 <= nx < n and 0 <= ny < n:
        #숫자를 넣을 수 있을 경우 
        if board[nx][ny] == 0:
            board[nx][ny] = current
            current -= 1
            cx,cy = nx,ny
        #숫자가 이미 있는 경우, 방향을 바꿔서 다음 좌표 확인 
        else:
            direct = (direct + 1) % 4
        
    #다음 좌표가 판 밖일 경우, 방향을 바꿔서 다음 좌표 확인 
    else:
        direct = (direct + 1) % 4

#보드 출력 
for i in range(n):
    print(*board[i])

#좌표 출력 
for i in range(n):
    for j in range(n):
        if board[i][j] == num:
            print(i+1,j+1)
            exit(0)


