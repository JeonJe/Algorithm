n = int(input())
board_length = 4*n-3

board = [ [' ' for _ in range(board_length)] for _ in range(board_length) ]

def draw_star(n,idx):
    if n == 1:
        board[idx][idx] = "*"
        return 
    
    length = 4*n-3
    for i in range(idx, idx+length):
        #위쪽 가장자리
        board[idx][i] = "*"
        #아래쪽 가장자리
        board[idx+length-1][i] = "*"
        #왼쪽 가장자리
        board[i][idx] = "*"
        #오른쪽 줄 
        board[i][idx+length-1] = "*"
    draw_star(n-1, idx+2)

draw_star(n, 0)

for i in range(board_length):
    print("".join(board[i]))
    
    
