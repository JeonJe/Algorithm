import sys
input = sys.stdin.readline 

n = int(input())

board = [list(input()) for _ in range(n)]
user_data = [list(input()) for _ in range(n)]

dx = [ 1,1,0,-1,-1,-1,0,1 ]
dy = [ 0,-1,-1,-1,0,1,1,1 ]

lose = False

def print_board():
        for i in range(n):
            for j in range(n):
                if not lose and board[i][j] == "*":
                    board[i][j] = "."
                print(board[i][j],end='')
            print()
        
def udpate_board(board,i,j):
    global lose
    bomb_cnt = 0
    
    if board[i][j] == "*":
        lose = True
        return 
    
    #주변 지뢰 숫자를 카운트해서 보드에 업데이트 
    for z in range(8):
        nx = i + dx[z]
        ny = j + dy[z]

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == "*":
                bomb_cnt += 1
    
    board[i][j] = bomb_cnt

for i in range(n):
    for j in range(n):
        #유저가 클릭한 곳이라면
        if user_data[i][j] == "x":
            #보드 업데이트 
            udpate_board(board,i,j)
        
print_board()
