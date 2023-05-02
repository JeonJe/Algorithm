
from collections import deque 

graph = [ input() for _ in range(5)]
visited = [[False for _ in range(5)] for _ in range(5)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    
    visited_que = [[False for _ in range(5)] for _ in range(5)]
    que = deque()
    que.append((x,y))
    visited_que[x][y] = True

    cnt = 1
    while que:
        cx,cy = que.popleft() 

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited_que[nx][ny] and visited[nx][ny]:
                visited_que[nx][ny] = True
                que.append((nx,ny))
                cnt+=1

    return cnt == 7

def check():
    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                return bfs(i,j)


def dfs(idx,path,cnt):
    global answer 
    if len(path) >= 7:
        if cnt >= 4:
            if check():
                answer += 1
        return 

    for i in range(idx+1,25):
        path.append(graph[i//5][i%5])
        visited[i//5][i%5] = True
        if graph[i//5][i%5] == "S":
            dfs(i,path,cnt+1)
        else:
            dfs(i,path,cnt)
        
        visited[i//5][i%5] = False
        path.pop()

global answer 
answer = 0
for i in range(25):
    cnt_dasom = 0
    if graph[i//5][i%5] == "S":
        cnt_dasom += 1
    visited[i//5][i%5] = True
    dfs(i,[graph[i//5][i%5]],cnt_dasom)
    visited[i//5][i%5] = False

print(answer)

