N = int(input())

graph = [ list(map(int,input().split())) for _ in range(N) ]

graph[0][0] = 1
graph[0][1] = 1

#0은 가로, 1은 세로, 2는 대각선
global cnt 
cnt = 0
def dfs(x,y,direction):
    global cnt
    if x == N-1 and y == N-1:
       cnt += 1
       return  
    #가로로 가는 경우 -> 이전이 대각선이거나 가로여야 함 
    
    if y+1 < N:
        if (direction == 0 or direction == 2) and graph[x][y+1] == 0:
            dfs(x,y+1,0)
    if x+1 < N:
        #세로로 가는 경우  -> 이전이 대각선이거나 세로여야 함
        if (direction == 1 or direction == 2) and graph[x+1][y] == 0:
            dfs(x+1,y,1)

    if x+1 < N and y+1 < N:
        if graph[x+1][y] == 0 and graph[x][y+1] == 0 and graph[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)
    #대각선으로 가는 경우 -> 모든 경우에 대각선으로 갈 수 있음

dfs(0,1,0)
print(cnt)