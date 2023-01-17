from collections import deque 

R,C = map(int,input().split())
global visited,cnt,find
find = False
graph = [list(input()) for _ in range(R)]
visited = [ [False]*(C) for _ in range(R) ]

dx = [-1,0,1]
dy = [1,1,1]

def dfs(x,y):
    global visited,cnt,find
    visited[x][y] = True
    
    if y == C-1 :
        find = True
        cnt+=1
        return 

    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < R and 0<= ny < C and not visited[nx][ny] and graph[nx][ny]!= 'x':
            dfs(nx,ny)
            if find:
                return 

cnt = 0
for i in range(R):
    find = False
    dfs(i,0)
        

print(cnt)