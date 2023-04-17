dx = [0,0, 1, 1]
dy = [0,1, 1, 0]
def remove_block(m,n,board):
    removes = set()
    for i in range(m):
        for j in range(n):
            cur = board[i][j]
            if cur == 0:
                continue
            cnt = 1
            for k in range(1,4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<= nx < m and 0<= ny < n:
                    if board[nx][ny] == cur:
                        cnt+=1
                    else:
                        break

            if cnt == 4:
                for k in range(4):
                    removes.add((i + dx[k],j+dy[k]))
    for x, y in removes:
        board[x][y] = 0
    return len(removes)

def move_block(m,n, board):
    for i in range(m-1,-1,-1):
        for j in range(n):
            temp = board[i][j]
            k = i
            find_zero = False
            while k+1 < m and board[k+1][j] == 0:
                find_zero = True
                k+=1
            if find_zero:
                board[i][j] = 0
                board[k][j] = temp

def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    while True:
        cnt_block = remove_block(m,n,board)
        if cnt_block == 0:
            return answer 
        else:
            answer += cnt_block
        move_block(m,n,board)
        
m  = 6
n = 6
board =	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m,n,board))