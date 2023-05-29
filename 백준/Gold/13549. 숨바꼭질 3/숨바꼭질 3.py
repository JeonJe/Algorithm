from collections import deque, defaultdict

n, m = map(int,input().split())

if n == m:
    print(0)
    exit(0)

que = deque()
que.append((n,0))
visited = defaultdict(bool)

while que:
    cx, time = que.popleft()
        
    if cx == m:
        print(time)
        break

    if not visited[cx]:
        visited[cx] = True
    if cx*2 <= 2*m and not visited[cx*2]:
        que.append((cx*2, time))
    if cx-1 >= -2*m and not visited[cx-2]:
        que.append((cx-1, time+1))
    if cx+1 <= 2*m and not visited[cx+1]:
        que.append((cx+1, time+1))


