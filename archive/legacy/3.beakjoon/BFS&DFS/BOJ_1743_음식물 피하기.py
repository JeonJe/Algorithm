import sys 
sys.setrecursionlimit(10**6)
height, width, num_trash = map(int,input().split())

graph = [ ['.'] * width for _ in range( height )]
visited = [ [False]*width for _ in range(height) ]

global cnt
answer = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y):
    global cnt 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < height and 0<= ny < width and not visited[nx][ny] and graph[nx][ny] == "#":
            visited[nx][ny] = True
            cnt+=1
            dfs(nx,ny)
    
    return 
                
for _ in range(num_trash):
    x,y = map(int,input().split())
    graph[x-1][y-1] = "#"

for i in range(height):
    for j in range(width):
        if not visited[i][j] and graph[i][j] == '#':
            visited[i][j] = True
            cnt = 1
            dfs(i,j)
            answer = max(answer, cnt)

print(answer)