from collections import deque 

F,S,G,U,D = map(int,input().split())
move = [U,-D]
visited = [False for _ in range(F+1)]

def bfs(start, desti):
    if start == desti:
        return 0
    que = deque()
    que.append((start,0))
    visited[start] = True

    while que:
        current,cnt = que.popleft()
        if current == desti:
            return cnt
        
        for i in move:
            nx = current + i
            if nx <= 0 or nx > F or visited[nx]:
                continue
            visited[nx] = True
            que.append((nx,cnt+1))
    return -1


result = bfs(S,G)
print(result if result != -1 else "use the stairs")

