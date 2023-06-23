
import sys 
input = sys.stdin.readline 

n = int(input())
board = [ list(map(int,input().split())) for _ in range(n) ]
visited = [ [False for _ in range(n)] for _ in range(n) ]
dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]

def is_right_position(x,y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            return False
        
        if visited[nx][ny]:
            return False
        
    return True

def find_points(board, coordinates, depth, value):
    if depth == 3:
        global answer
        answer = min(answer, value)
        return
    
    for i in range(len(board)):
        for j in range(len(board[i])):

            if is_right_position(i,j):
                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = True
                    value += board[nx][ny]

                find_points(board, coordinates + [(i,j)], depth+1, value)
                
                for k in range(5):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    visited[nx][ny] = False
                    value -= board[nx][ny]

answer = 1e9
find_points(board, [], 0, 0)
print(answer)