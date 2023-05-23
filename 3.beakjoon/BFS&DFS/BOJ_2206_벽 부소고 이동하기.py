from collections import deque

height, width = map(int,input().split())

graph = [ list(input()) for _ in range(height) ]

def bfs(x,y):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    visited =  [[[0]*2 for _ in range (width)] for _ in range(height)]   
    que = deque()
    que.append((x,y,0))

    while que:
        cx,cy,cnt = que.popleft()

        if cx == height-1 and cy == width-1:
            return visited[cx][cy][cnt]+1
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
        
            if 0 <= nx < height and 0 <= ny < width and not visited[nx][ny][cnt]:
                # 지나갈 수 있는 곳, 벽 부수는 기회 미사용
                if cnt == 0 and graph[nx][ny] == "0":
                    visited[nx][ny][0] = visited[cx][cy][0] + 1
                    que.append((nx,ny,0))
                # 지나갈 수 있는 곳, 벽 부수는 기회 사용
                elif cnt == 1 and graph[nx][ny] == "0":
                    visited[nx][ny][1] = visited[cx][cy][1] + 1
                    que.append((nx,ny,1))
                elif cnt == 0 and graph[nx][ny] == "1":
                    visited[nx][ny][1] = visited[cx][cy][0] + 1
                    que.append((nx,ny,1))
                # 벽인 곳 , 벽 부수는 기회 미사용
    return -1 

print(bfs(0,0))