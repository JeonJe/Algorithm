from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

height = 12
width = 6
board = [ list(input()) for _ in range(height)]
answer = 0
#뿌요 떨어짐
def down(board):
    for i in range(height-1,-1,-1):
        for j in range(width):
            x = i
            while True:
                x += 1
                if x >= height or board[x][j] != ".":
                    break
                board[x][j] = board[x-1][j]
                board[x-1][j] = "."

def bfs(i,j,visited,board):

    que = deque()
    que.append((i,j))
    points = [[i,j]]
    color = board[i][j]
    
    while que:
        cx,cy = que.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < height and 0<= ny < width and not visited[nx][ny]:
                if color == board[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx,ny))
                    points.append((nx,ny))

    if len(points) >= 4:
        for x, y in points:
            board[x][y] = "."
        return True
    else:
        return False



#뿌요 연쇄
def bomb(board):

    visited = [ [False for _ in range(width)] for _ in range(height) ]
    find = False
    for i in range(height):
        for j in range(width):
            if board[i][j] != "." and not visited[i][j]:
                visited[i][j] = True
                if bfs(i,j,visited,board):
                    find = True
    return find

cnt = 0
while True:
    down(board)
    if bomb(board):
        cnt+=1
    else:
        print(cnt)
        break

