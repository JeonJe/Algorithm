import sys
from collections import deque 
#세로의 크기 N
#가로의 크기 M

N,M = map(int,input().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

graph = [input() for _ in range(N)]
coins = []

que = deque()
cnt = 0
def bfs():
    while que:
        x1,y1, x2, y2, cnt = que.popleft()
        if cnt >= 10:
            return -1 
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
        
            #동전의 다음 이동이 판 안쪽인 경우 
            if 0<= nx1 < N and 0 <= ny1 < M and 0<=nx2<N and 0<= ny2 <M:
                if graph[nx1][ny1] == '#':
                    nx1 = x1 
                    ny1 = y1
                if graph[nx2][ny2] == '#':
                    nx2 = x2 
                    ny2 = y2
                que.append((nx1,ny1,nx2,ny2,cnt+1))
            #동전의 다음 이동이 바깥쪽인 경우
            #2번 동전이 밖으로 떨어진 경우 
            elif 0<= nx1 < N and 0 <= ny1 < M:
                return cnt + 1
            #1번 동전이 밖으로 떨어진 경우 
            elif 0<= nx2 < N and 0 <= ny2 < M:
                return cnt + 1

            else:
                continue


for i in range(N):
    for j in range(M):
        if graph[i][j] == 'o':
            coins.append((i,j))

que.append((coins[0][0],coins[0][1],coins[1][0], coins[1][1],0))
print(bfs())

