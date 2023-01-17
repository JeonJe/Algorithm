import heapq

dx = [1,0,-1,0]
dy = [0,1,0,-1]


global n
global graph

def dijkstra(x,y,k):
    global n
    global graph
    distance = [[10e9]*(n) for _ in range(n)]
    distance[x][y] = graph[x][y]

    que = []
    heapq.heappush(que, (distance[x][y], x, y))

    while que:
        c_distance,cx,cy = heapq.heappop(que)
        if cx == n-1 and cy == n-1:
            break 
        if distance[cx][cy] < c_distance:
            continue

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nx < n and 0<= ny < n :
                if c_distance+ graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = c_distance+ graph[nx][ny]
                    heapq.heappush(que, (distance[nx][ny], nx, ny))
   
    print(f'Problem {k}: {distance[n-1][n-1]}')

i = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [ list(map(int,input().split())) for _ in range(n) ]
    dijkstra(0,0,i)
    i += 1
