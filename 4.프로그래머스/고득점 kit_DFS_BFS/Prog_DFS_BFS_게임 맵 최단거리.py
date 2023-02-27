from collections import deque 


def solution(maps):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    def bfs(x,y):
        visited = [[False] * width for _ in range(height)]
        visited[x][y] = True
        que = deque()
        que.append((0,0,1))

        while que:
            cx, cy, cdistance = que.popleft()
            if cx == height - 1 and cy == width - 1:
                return cdistance
            for i in range(4):
                nx = cx + dx[i] 
                ny = cy + dy[i]

                if 0<= nx < height and 0<= ny < width and maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append((nx,ny,cdistance+1))

        return -1
        
    answer = 0
    height = len(maps)
    width = len(maps[0])
    answer = bfs(0,0)
    return answer



maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

print(solution(maps))