from collections import deque 
import math

N, L, R = map(int,input().split())

global open_country,visited,graph
graph = [list(map(int,input().split())) for _ in range(N)]

open_country = []

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def bfs(x,y):
    global visited,graph
    open_country  = [] 
    visited[x][y] = True
    que = deque()
    que.append((x,y))
    open_country.append((x,y))

    while que:
        cx, cy = que.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0<= ny < N and not visited[nx][ny]:  
                if L <= abs(graph[cx][cy] - graph[nx][ny]) <= R:
                    visited[nx][ny] = True
                   
                    open_country.append((nx,ny))
                    que.append((nx,ny))
    return open_country

def day():
    global visited,graph
    change_country_num = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                open_countrys = bfs(i,j)

                if len(open_countrys) <= 1:
                    continue
                s = 0
                for x,y in open_countrys:
                    s += graph[x][y]
                avg = s // len(open_countrys)

                for x,y in open_countrys:
                    graph[x][y] = avg

                change_country_num += len(open_countrys)

    if change_country_num == 0 :
        return True
    else:
        return False
  


cnt = 0
while True:
    visited = [[False]*(N) for _ in range(N)]
    
    if day():
        break
    cnt+=1

print(cnt)
