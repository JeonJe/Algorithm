from collections import deque, defaultdict
import sys

N, K = map(int,input().split())

end = 100000
visited = [False] * (end+1)
res = defaultdict(int)
min_time = sys.maxsize
ways = 0

que = deque()
que.append((N,0))

while que:
    cx,ct = que.popleft()
    visited[cx] = True

    if cx == K:
        min_time = min(min_time,ct)
        ways += 1

    if ct > min_time:
        break

    for nx in (cx*2, cx+1, cx-1):
        if 0 <= nx < end+1 and not visited[nx]:
            que.append((nx,ct+1))

print(min_time)
print(ways)