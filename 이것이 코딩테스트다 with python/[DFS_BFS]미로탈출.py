from _collections import deque

def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4): # 4방향에 대해서
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=N or ny >=M or graph[nx][ny] == 0: # 이동할 수 없으면 패스
                continue

            if graph[nx][ny] == 1: # 처음 이동하는 칸이면
                graph[nx][ny] = graph[x][y] + 1 # 이전 칸까지 이동 횟수 + 1
                queue.append((nx,ny))

    return graph[N-1][M-1] #도착지까지 최단 횟수 


dx = [-1,+1,0,0]
dy = [0,0,-1,+1]

N,M = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input())))

print(bfs(graph,0,0))

