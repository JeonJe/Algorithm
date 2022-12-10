n = int(input())

graph = [ list(map(int,input())) for _ in range(n) ]
visited = [ [False]*n for _ in range(n) ]
answer = []

global cnt 
dx = [0,0,-1,1]
dy = [1,-1,0,0]


def dfs(x,y):
    global cnt 
    visited[x][y] = True 
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<= nx < n and 0<= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt += 1
                dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            cnt = 1
            dfs(i,j)
            
            answer.append(cnt)
answer.sort()
print(len(answer))
for ans in answer:
    print(ans)

