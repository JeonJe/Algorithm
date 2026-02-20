from collections import deque
import sys
input = sys.stdin.readline

#m은 가로, n은 세로, h은 높이
m, n, h = map(int,input().split())

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]


#수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 
graph = [ [list(map(int,input().split())) for _ in range(n)] for _ in range(h) ]
def bfs():
    que = deque()
    is_initial_zero = False 
    for height in range(h):
        for width in range(n):
            for length in range(m):
                if graph[height][width][length] == 1:
                    que.append([height,width,length])
                    
                if graph[height][width][length] == 0:
                    is_initial_zero = True
    if not is_initial_zero:
        return False

    while que:
        z,x,y = que.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] +1 
                    que.append([nz,nx,ny])
    return True


if not bfs():
    print(0)
else:
    day = -1
    for height in range(h):
        for width in range(n):
            for length in range(m):
                if graph[height][width][length] == 0:
                    print(-1)
                    sys.exit()
                else:
                    day = max(day, graph[height][width][length])
    print(day-1)