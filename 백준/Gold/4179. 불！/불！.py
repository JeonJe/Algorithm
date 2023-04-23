from collections import deque
import sys
input = sys.stdin.readline

R,C = map(int,input().split())
maps = [list(input().rstrip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

fire_que = deque()
jihoon_que = deque()

for i in range(R):
    for j in range(C):
        if maps[i][j] == "J":
            visited[i][j] = True
            jihoon_que.append([i,j,0])
        elif maps[i][j] == "F":
            maps[i][j] = 0
            fire_que.append([i,j,0])

while fire_que:
    cx,cy,dist = fire_que.popleft()
    
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        
        if 0 <= nx < R and 0<= ny < C:
            if maps[nx][ny] == "J" or maps[nx][ny] == ".":
                maps[nx][ny] = dist+1
                fire_que.append([nx,ny,dist+1])

answer = 0


while jihoon_que:
    cx,cy,dist = jihoon_que.popleft()
    
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if 0 <= nx < R and 0<= ny < C:
            if maps[nx][ny] == "#":
                continue
            
            if not visited[nx][ny] and (maps[nx][ny] =="." or dist+1 < maps[nx][ny]):
                visited[nx][ny] = True
                jihoon_que.append([nx,ny,dist+1])
        else:
            print(dist+1)
            exit(0)
            
print("IMPOSSIBLE")


