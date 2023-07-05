import copy 

t = int(input())

def rotate_45(board):
  origin = copy.deepcopy(board)
  # 45도 이동 
  for i in range(n):
    # X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
    board[i][((n+1)//2)-1] = origin[i][i]
    # X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다.
    board[i][-i-1] = origin[i][((n+1)//2)-1]
    # X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
    board[((n+1)//2)-1][i] = origin[-1-i][i]
    # X의 가운데 행을 X의 주 대각선으로 옮긴다.
    board[i][i] = origin[((n+1)//2)-1][i]

def rotate(board, d):
  if d < 0:
    d += 360
  
  cnt = d // 45

  for _ in range(cnt):
    rotate_45(board)
  

def print_board(board):
  for i in range(len(board)):
    print(*board[i])

for _ in range(t):
  n, d = map(int,input().split())
  board = [list(map(int,input().split())) for _ in range(n)]


  rotate(board, d)
  print_board(board)
