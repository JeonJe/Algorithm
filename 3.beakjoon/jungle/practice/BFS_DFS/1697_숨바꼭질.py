from collections import deque

N, K = map(int,input().split())
visited = [False] * (100001)
que = deque()
que.append((N,0))

cnt = 0
while que:
    current,cnt = que.popleft()
    visited[current] = True

    if current == K:
        print(cnt)
        break

    for nx in (2 * current, current+1, current-1):
        if 0<= nx < 100001 and not visited[nx]:
            que.append((nx,cnt+1))

