from collections import deque 

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []
dx, dy = [1,0,-1,0], [0,1,0,-1]
answer = 1e9

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])
            board[i][j] = 0

def spread_virus(pick):
    visited = [[False for _ in range(N)] for _ in range(N)]
    que = deque()

    #선택한 바이러스 처음 위치 
    for point in pick:
      vx = virus[point][0]
      vy = virus[point][1]
      visited[vx][vy] = True
      que.append([vx,vy,0])
    
    max_time = -1
    while que:
      que_size = len(que)
      for i in range(que_size):
        cx,cy, dist = que.popleft()
        max_time = max(dist, max_time)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append([nx,ny,dist+1])
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and not visited[i][j]:
                return 1e9
    # 바이러스를 빈틈없이 퍼트릴 수 있는 경우 
    return max_time
    
# M개 바이러스 선택
def dfs(idx, pick):
    if len(pick) == M:
        global answer 
        for point in pick:
            board[virus[point][0]][virus[point][1]] = 2

        answer = min(answer, spread_virus(pick))

        for point in pick:
            board[virus[point][0]][virus[point][1]] = 0
        return
    
    for i in range(idx+1, len(virus)):
        pick.append(i)
        dfs(i, pick)
        pick.remove(i)

dfs(-1,[])
print(answer if answer != 1e9 else -1)