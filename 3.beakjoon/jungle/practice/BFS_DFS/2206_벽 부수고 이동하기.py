from collections import deque

N,M = map(int,input().split())

graph = [list(map(int,input())) for _ in range(N) ]
visited = [ [[0]*(2) for _ in range(M)] for _ in range(N) ]


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    que = deque()
    que.append((x,y,0))
    visited[x][y][0] = 1

    while que:
        cx,cy, use_chacne = que.popleft()

        if cx == N-1 and cy == M-1:
            print(visited[cx][cy][use_chacne])
            exit()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nx < N and 0<= ny < M and not visited[nx][ny][use_chacne]:
                #벽을 부순적이 없고, 방문할 수 있으면서, 빈칸인 곳
                if use_chacne == 0 and graph[nx][ny] == 0:
                    visited[nx][ny][use_chacne] = visited[cx][cy][use_chacne] + 1
                    que.append((nx,ny,use_chacne))
                #벽을 부순적이 없고, 방문할 수 있으면서, 벽인 곳 -> 벽을 부수고 이동경로 탐색 
                elif use_chacne == 0 and graph[nx][ny] == 1:
                    visited[nx][ny][1] = visited[cx][cy][use_chacne] + 1
                    que.append(((nx,ny,1)))
                #벽을 부순적이 있고, 방문할 수 있으면서, 빈칸인 곳
                elif use_chacne == 1 and graph[nx][ny] == 0:
                    visited[nx][ny][use_chacne] = visited[cx][cy][use_chacne] + 1
                    que.append((nx,ny,use_chacne))
                
    print(-1)

bfs(0,0)