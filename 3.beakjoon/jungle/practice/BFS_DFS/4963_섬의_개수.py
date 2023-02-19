import sys 
sys.setrecursionlimit(10**5)

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(x,y):
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < h and 0<= ny < w and not visited[nx][ny]:
            if graph[nx][ny] == 1:
                visited[nx][ny] = True 
                dfs(nx,ny)
    return

while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break

    graph = [ list(map(int,input().split())) for _ in range(h) ]
    visited = [[False]*(w) for _ in range(h)]
    res = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(i,j)
                res += 1
    print(res)
                

