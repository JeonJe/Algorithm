import sys
from collections import deque


cnt = 0 

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N = int(input())
graph = [ list(map(int,input().split())) for _ in range(N) ]


def dfs(i,j,k):
   
    queue = deque()
    queue.append((i,j))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] > k:
                    visited[nx][ny] = True 
                    queue.append((nx,ny))
    return cnt

max_h = 0
for i in graph:
    max_h = max(max_h,max(i))

res = 0
temp = [] 
for k in range(max_h+1):
    cnt = 0
    visited = [ [False]* N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and not visited[i][j]:
                cnt+=1
                dfs(i,j,k) 
    temp.append(cnt)
                
print(max(temp))
