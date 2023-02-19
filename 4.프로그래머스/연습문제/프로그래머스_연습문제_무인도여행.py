import sys 
sys.setrecursionlimit(10**6)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def solution(maps):

    def dfs(x,y):
        global cnt
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < height and 0<= ny < width :
                if maps[nx][ny] != "X" and not visited[nx][ny]:
                    cnt += int(maps[nx][ny])
                    dfs(nx,ny)
        
    global cnt
    answer = []
    width = len(maps[0])
    height = len(maps)
    visited = [[False] * (width) for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if maps[i][j] != "X" and not visited[i][j]:
                cnt = 0
                cnt += int(maps[i][j])
                dfs(i,j)
                answer.append(cnt)
        
    if len(answer) > 0:
        answer.sort()
    else:
        answer.append(-1)
    return answer



maps = 	["X591X", "X1X5X", "X231X", "1XXX1"]

print(solution(maps))