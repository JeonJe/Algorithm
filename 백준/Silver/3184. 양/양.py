import sys
sys.setrecursionlimit(10**6)
R,C = map(int,input().split())

#row의 수 는 R

graph = [ input() for _ in range(R) ]
visited = [ [False]*(C+1) for _ in range(R+1) ]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

global goat
global wolf 

res = [0,0]

def dfs(x,y):

    if graph[x][y] == 'v':
        global wolf
        wolf += 1
    
    elif graph[x][y] == 'o':
        global goat
        goat += 1 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0<= ny < C:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == '#':
                    continue 
                dfs(nx, ny)


for i in range(R):
    for j in range(C):
        if graph[i][j] != '#':
            if not visited[i][j]:
                visited[i][j] = True
                goat, wolf = 0, 0
                dfs(i,j)
                if goat > wolf:
                    res[0] += goat
                else:
                    res[1] += wolf
print(*res)