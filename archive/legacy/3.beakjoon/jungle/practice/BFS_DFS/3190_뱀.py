from collections import deque

N = int(input())

#오른쪽 ,아래,왼쪽, 위 순 
dx = [1,0,-1,0]
dy = [0,1,0,-1]

num_apple = int(input())
board =  [[0] * N for _ in range(N)]

#뱀이 있는 좌표들을 담는 큐

snake = deque( )
snake.appendleft((0,0))

for i in range(num_apple):
    apple_row, apple_col = map(int,input().split())
    board[apple_row-1][apple_col-1] = 1

num_command = int(input())
commands = deque()

for i in range(num_command):
    command = input().split()
    commands.append((int(command[0]), command[1]))

#뱀은 처음에 오른쪽 방향으로 이동 
direct = 0
cur_row, cur_col = 0, 0
sec = 0

while True:
    #뱀의 다음 위치 확인
    if len(commands) > 0:
        s, d = commands[0][0], commands[0][1]
        if sec == s:
            if d == 'D':
                direct = (direct + 1) % 4
            if d == 'L' :
                direct = (direct - 1) % 4
            commands.popleft()
    n_row, n_col = cur_row+dy[direct], cur_col+dx[direct]

    #판 밖이면 게임 끝
    if n_row < 0 or n_row >= N or n_col < 0 or n_col >= N:   
        print(sec+1)
        break
    #자기 자신과 부딪혔다면 게임 끝
    if (n_row, n_col) in snake:
        print(sec+1)
        break

    #다음 좌표에 아무것도 없으면? 머리 이동, 과거 포인트 지우기, 몸통 한개 줄이기
    if board[n_row][n_col] == 0:
        snake.appendleft((n_row,n_col))
        snake.pop()
        cur_row = n_row
        cur_col = n_col

    #다음 좌표에 사과가 있다면?, 머리 위치만 추가 
    elif board[n_row][n_col] == 1:
        snake.appendleft((n_row, n_col))
        cur_row = n_row
        cur_col = n_col
        board[n_row][n_col] = 0
    sec += 1
