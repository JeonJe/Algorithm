from collections import deque

N,M = map(int,input().split())

graph = [list(map(int,input())) for _ in range(N) ]
visited_unuse_chance= [ [False]*(M) for _ in range(N) ]
visited_use_chance = [ [False]*(M) for _ in range(N) ]

distance = [ [99]*(M) for _ in range(N) ]


dx = [0,0,1,-1]
dy = [1,-1,0,0]
global res 
res = 1e9

def bfs(x,y):
    global res
    cnt = 1
    que = deque()
    
    que.append((1,0,x,y))
    graph[0][0] = 2
    visited_unuse_chance[0][0] = True
    distance[0][0] = 1
    
    while que:
        cnt,use_chance,cx,cy = que.popleft()
      
        if cx == N-1 and cy == M-1:
            print(cnt)
            exit()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nx < N and 0<= ny < M:
             
                #벽을 부순적이 없고, 다음이 벽이 아닌 곳에 방문한적이 없을 때
                if graph[nx][ny] == 0 and use_chance == 0 and not visited_unuse_chance[nx][ny]:
                    visited_unuse_chance[nx][ny] = True
                    que.append((cnt+1,use_chance,nx,ny))
                #벽을 부순적이 있고, 다음이 벽이 아닌 곳에 방문한적이 없을 때
                elif graph[nx][ny] == 0 and use_chance == 1 and not visited_use_chance[nx][ny]:
                    visited_use_chance[nx][ny] = True
                    que.append((cnt+1,use_chance,nx,ny))
                #벽을 부순적은 없고, 다음이 벽인 곳에 방문한적이 없을 때
                elif graph[nx][ny] == 1 and use_chance == 0 and not visited_unuse_chance[nx][ny]:
                    visited_unuse_chance[nx][ny] = True
                    que.append((cnt+1,1,nx,ny))
                

    print( res if res != 1e9 else -1 )

bfs(0,0)
