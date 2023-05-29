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

    for next in [cx*2, cx-1, cx+1]:
        if 0 <= next <= 100000 and not visited[next]:
            if next == cx*2:
                que.appendleft((next, time))
            else:
                que.append((next, time+1))
        