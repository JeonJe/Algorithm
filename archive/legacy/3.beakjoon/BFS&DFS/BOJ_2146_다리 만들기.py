n = int(input())

board = [list(map(int,input().split())) for _ in range(n) ]
visited = [ [False]* n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 