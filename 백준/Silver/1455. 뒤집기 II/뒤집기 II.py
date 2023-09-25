
height, width = map(int, input().split())

board = [list(map(int,input())) for _ in range(height)]

cnt = 0

# 오른쪽 최하단부터 왼쪽 최상단까지 이동
# 값이 0 이면 현재 위치 0,0부터 i,j까지 모든 값을 뒤집음
# 횟수 증가

for i in range(height-1,-1, -1):
  for j in range(width-1,-1,-1):
    if board[i][j] == 1:
      cnt += 1
      for a in range(i+1):
        for b in range(j+1):
          if board[a][b] == 0:
            board[a][b] = 1
          else:
            board[a][b] = 0
print(cnt)