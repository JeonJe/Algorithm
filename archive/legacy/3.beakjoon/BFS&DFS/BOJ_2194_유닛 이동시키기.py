from collections import deque, defaultdict
import sys 
input = sys.stdin.readline 

def is_next_valid_place(nx,ny):

    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return False
    if nx < 0 or nx >= n or ny + (b-1) < 0 or ny + (b-1) >= m:
        return False
    if nx + (a-1) < 0 or nx + (a-1) >= n or ny < 0 or ny >= m:
        return False
    if nx + (a-1) < 0 or nx + (a-1) >= n or ny + (b-1) < 0 or ny + (b-1) >= m:
        return False

    return True 
    
def is_next_no_barrier(nx,ny):

    for i in range(nx, nx + a):
        for j in range(ny, ny + b):
            if barriers[i][j]:
                return False
    return True 

n, m, a, b, k = map(int,input().split())

barriers_points = [list(map(int,input().split())) for _ in range(k)]
barriers = [[False for _ in range(m)] for _ in range(n)]
for x,y in barriers_points:
    barriers[x-1][y-1] = True 

start = list(map(int,input().split()))
start[0] -= 1
start[1] -= 1

end = list(map(int,input().split()))
end[0] -= 1
end[1] -= 1

visited = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]
que = deque()
que.append((start,0))
visited = defaultdict(int)
visited[(start[0], start[1])] = 1
# visited.append(start)

        
while que:
    cur_points, dist = que.popleft()

    if cur_points[0] == end[0] and cur_points[1] == end[1]:
        print(dist)
        exit(0)

    for i in range(4):
        nx = cur_points[0] + dx[i]
        ny = cur_points[1] + dy[i]
        if is_next_valid_place(nx,ny):
            if is_next_no_barrier(nx,ny):
                if visited[(nx,ny)] == 0:
                    visited[(nx,ny)] = 1
                    que.append(([nx,ny], dist+1))

print(-1)