from collections import deque
import sys

N, K = map(int,input().split())

end = (100001)
visited = [False] * (end+1)

min_time = sys.maxsize
ways = 0

que = deque()
que.append((N,0))

while que:
    cx,ct = que.popleft()
    visited[cx] = True

    if ct > min_time:
        break

    if cx == K:
        min_time = ct
        ways += 1

    for nx in (cx*2, cx+1, cx-1):
        if 0 <= nx < end+1 and not visited[nx]:
            que.append((nx,ct+1))

print(min_time)
print(ways) 