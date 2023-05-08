from collections import deque

def bfs(z,x,y):
    dz = [0,0,0,0,1,-1]
    dx = [-1,0,1,0,0,0]
    dy = [0,1,0,-1,0,0]
    
    que = deque()    
    que.append((z,x,y,0))

    while que:
        cz,cx,cy,dist = que.popleft()
        if cz == end[0] and cx == end[1] and cy == end[2]:
            return dist
        
        for i in range(6):
            nz = cz + dz[i]
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nz < L and 0<= nx < R and 0<= ny < C:
                if not visited[nz][nx][ny] and graph[nz][nx][ny] != '#':
                    visited[nz][nx][ny] = True
                    que.append((nz,nx,ny,dist+1))

    return -1    



while True:
    L,R,C = map(int,input().split())
    if L == 0 and R == 0 and C == 0:
        break
    graph = []
    visited = [[ [False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    start,end = [],[]

    for _ in range(L):
        graph.append([list(input()) for _ in range(R)])
        input()
    
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if graph[i][j][k] == "S":
                    start = [i,j,k]
                elif graph[i][j][k] == "E":
                     end = [i,j,k]

    if start:                 
        visited[start[0]][start[1]][start[2]] = True
        result = bfs(start[0],start[1],start[2])
        print(f'Escaped in {result} minute(s).' if result != -1 else "Trapped!")