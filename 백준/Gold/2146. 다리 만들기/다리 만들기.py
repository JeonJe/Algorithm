from collections import deque

# 10
# 1 1 1 0 0 0 0 1 1 1
# 1 1 1 1 0 0 0 0 1 1
# 1 0 1 1 0 0 0 0 1 1
# 0 0 1 1 1 0 0 0 0 1
# 0 0 0 1 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]


def bfs_land(i,j,cnt_land):

    deq = deque()
    deq.append((i,j))
    visited[i][j] = True
    map[i][j] = cnt_land

    while deq:
        x,y = deq.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0<= ny< N and map[nx][ny] ==1 and not visited[nx][ny]:
                visited[nx][ny] = True
                deq.append((nx,ny))
                map[nx][ny] = cnt_land

#각 섬에 대해서 다른섬까지 최소거리
def find(land_num,m):
    global res
    dist = [ [-1]*N for _ in range(N)]
    deq = deque()

    for i in range(N):
        for j in range(N):
            #섬이면 위치를 넣고, 거리를 0으로 만듬
            if map[i][j] == land_num:
                deq.append((i,j))
                dist[i][j] = 0
    while deq:
        x, y = deq.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            #맵 밖
            if nx < 0 or ny <0 or nx>=N or ny >= N:
                continue

            #다른 섬과 닿았다면 최소거리를 찾기 위해 비교
            if map[nx][ny] > 0 and map[nx][ny] !=land_num:
                return min(m,dist[x][y])


            #원래 바다이면서 간척이 안된 곳
            if map[nx][ny]==0 and dist[nx][ny] == -1:
                #간척을 시킴
                dist[nx][ny] = dist[x][y]+1
                deq.append((nx,ny))



N = int(input())
map = [ list(map(int,input().split())) for _ in range(N)]
visited = [ [False] *N for _ in range(N)]


cnt_land = 1
m = 999999
res = []
for i in range(N):
    for j in range(N):
        #처음 방문하는 섬
        if not visited[i][j] and map[i][j] ==  1:
            bfs_land(i,j,cnt_land)
            cnt_land +=1


for i in range(1,cnt_land):
    res.append(find(i,m))

print(min(res))