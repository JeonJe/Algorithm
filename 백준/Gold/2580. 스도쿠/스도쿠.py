import sys
input = sys.stdin.readline


n = 9
board = [list(map(int,input().split())) for _ in range(n)]

def check_row(target,x):
    for i in range(n):
        if board[x][i] == target:
            return False
    return True 
    
def check_col(target,y):
    for i in range(n):
        if board[i][y] == target:
            return False
    return True

def check_squre(target,x,y):
    left_top_x = (x//3) * 3 
    left_top_y = (y//3) * 3
    
    for i in range(3):
        for j in range(3):
            if board[left_top_x + i][left_top_y + j] == target:
                return False
    return True


def dfs(idx):
    if idx == len(zero):
        for i in range(n):
            print(*board[i])
        exit(0)
    
    for i in range(1,10):
        nx = zero[idx][0]
        ny = zero[idx][1]

        if check_row(i,nx) and check_col(i,ny) and check_squre(i,nx,ny):
            board[nx][ny] = i
            dfs(idx+1)
            board[nx][ny] = 0

zero = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            zero.append([i,j])

dfs(0)