from collections import deque 

height, width = map(int,input().split())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

graph = [ list(input()) for _ in range(height) ]
coin_points = []
for i in range(height):
    for j in range(width):
        if graph[i][j] == "o":
            coin_points.append((i, j))

coinA = coin_points[0]
coinB = coin_points[1]

def bfs():
    
    que = deque()
    que.append((coinA[0],coinA[1], coinB[0],coinB[1],0))

    while que:
        coinA_x, coinA_y, coinB_x, coinB_y, cnt = que.popleft()
      
        if cnt >= 10:
            return -1 
        
        for i in range(4):
            coinA_nx = coinA_x + dx[i]
            coinA_ny = coinA_y + dy[i]
            coinB_nx = coinB_x + dx[i]
            coinB_ny = coinB_y + dy[i]

            if 0 <= coinA_nx < height and 0<= coinA_ny < width and 0 <= coinB_nx < height and 0<= coinB_ny < width:
                if graph[coinA_nx][coinA_ny] == "#":
                    coinA_nx, coinA_ny = coinA_x, coinA_y
                if graph[coinB_nx][coinB_ny] == "#":
                    coinB_nx, coinB_ny = coinB_x, coinB_y
                que.append((coinA_nx, coinA_ny, coinB_nx, coinB_ny,cnt+1))
                
            elif 0 <= coinA_nx < height and 0<= coinA_ny < width:
                return cnt+1
            elif 0 <= coinB_nx < height and 0<= coinB_ny < width:
                return cnt+1
            else:
                continue
                    

print(bfs())