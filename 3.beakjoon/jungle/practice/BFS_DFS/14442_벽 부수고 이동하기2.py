from collections import deque

N, M, K = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]
visited = [ [ [0] * (K+1) for _ in range(M)] for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y):
    queue = deque()
    queue.append((x,y,0))
    visited[x][y][0] = 1

    while queue:
        cx,cy,use_chance = queue.popleft()

        if cx == N-1 and cy == M-1:
            print(visited[cx][cy][use_chance])
            exit()

        for i in range(4): 
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nx < N and 0<= ny < M  :
               #벽을 아직 부술 수 있고, 방문할 수 있으면서, 빈칸인 곳
                if use_chance <= K and graph[nx][ny] == 0 and not visited[nx][ny][use_chance]:
                    visited[nx][ny][use_chance] = visited[cx][cy][use_chance] + 1
                    queue.append((nx,ny,use_chance))
                #벽을 아직 부술 수 있고, 방문할 수 있으면서, 벽인 곳 -> 벽을 부수고 이동경로 탐색 
                elif use_chance < K and graph[nx][ny] == 1 and not visited[nx][ny][use_chance+1]:
                    visited[nx][ny][use_chance+1] = visited[cx][cy][use_chance] + 1
                    queue.append(((nx,ny,use_chance + 1)))
    print(-1)


bfs(0,0)
