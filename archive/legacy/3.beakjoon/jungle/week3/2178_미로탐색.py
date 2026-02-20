from collections import deque

#n 가로행 수 
#m 세로열 수 
n, m = map(int,input().split())

graph = [ list(map(int,input())) for _ in range(n)]

visited = [ [False] * m for _ in range(n) ]
memo = [ [0] * m for _ in range(n) ]
#출발지 1,1 -> 0,0 으로 입력
#목적지 N,M -> n-1, m-1


dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y):

    visited[x][y] = True
    que = deque()
    que.append((x,y))
    memo[x][y] = 1

    while que:
        cx,cy = que.popleft()
        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]

            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue

            if visited[nx][ny] == False and graph[nx][ny] == 1:
                visited[nx][ny] = True
                memo[nx][ny] = memo[cx][cy]+ 1 
                que.append((nx,ny))
  
bfs(0,0)
print(memo[n-1][m-1])


