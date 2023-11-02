from collections import deque 

n = int(input())
graph = [list(input()) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def BFS(i,j,graph,visited):
    cur_color = graph[i][j]
    que = deque()
    que.append((i,j))

    while que:
        cx,cy = que.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny <n:
                if not visited[nx][ny] and graph[nx][ny] == cur_color:
                    visited[nx][ny] = True
                    que.append((nx,ny))
    return 

answer1 = 0
visited = [ [False for _ in range(n)] for _ in range(n) ]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True 
            BFS(i,j,graph,visited)
            answer1+=1

for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"

answer2 = 0
visited = [ [False for _ in range(n)] for _ in range(n) ]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True 
            BFS(i,j,graph,visited)
            answer2+=1

print(answer1,answer2)

