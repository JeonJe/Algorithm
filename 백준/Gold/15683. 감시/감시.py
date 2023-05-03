import copy

height,width = map(int,input().split())
board = [ list(map(int,input().split())) for _ in range(height) ]
cctv = []
answer = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def update_board(x,y,dir):
    dir = dir % 4

    while True:
        x += dx[dir]
        y += dy[dir]

        if x < 0 or x >= height or y < 0 or y >= width or copy_board[x][y] == 6:
            return 
        if 0 < copy_board[x][y] < 6:
            continue
        copy_board[x][y] = 7

        
for i in range(height):
    for j in range(width):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv.append((i,j))
        if board[i][j] == 0:
            answer += 1

cctv_length = len(cctv)
for i in range(4**(cctv_length)):
    temp  = i
    copy_board = copy.deepcopy(board)
    #cctv 한개씩 방향을 바꿔가며 사각지대 확인
    for j in range(cctv_length):
        dir = temp % 4
        temp = temp // 4

        x = cctv[j][0]
        y = cctv[j][1]

        if board[x][y] == 1:
            update_board(x,y,dir)
        elif board[x][y] == 2:
            update_board(x,y,dir)
            update_board(x,y,dir+2)
        elif board[x][y] == 3:
            update_board(x,y,dir)
            update_board(x,y,dir+1)
        elif board[x][y] == 4:
            update_board(x,y,dir)
            update_board(x,y,dir+1)
            update_board(x,y,dir+2)
        else:
            update_board(x,y,dir)
            update_board(x,y,dir+1)
            update_board(x,y,dir+2)
            update_board(x,y,dir+3)

        cnt_zero = 0
        for i in range(height):
            for j in range(width):
                if copy_board[i][j] == 0:
                    cnt_zero+=1
        answer = min(answer, cnt_zero)

print(answer)
