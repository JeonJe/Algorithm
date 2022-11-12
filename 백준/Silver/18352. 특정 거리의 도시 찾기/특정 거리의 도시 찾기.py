from collections import deque
import sys

input = sys.stdin.readline
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가

def bfs(v):
    visited[v] = True
    memo[v] = 0
    que = deque()
    que.append(v)

    while que:
        p = que.popleft()

        for adj in graph[p]:
            if not visited[adj]:
                visited[adj] = True
                # memo[adj] = min(memo[adj],memo[p] + 1)
                memo[adj] = memo[p]+1
                que.append(adj)
    
    
n, m, k, x = map(int,input().split())

graph = [ [] for _ in range(n+1)]
visited = [False] * (n+1)
memo = [sys.maxsize] * (n+1)

for _ in range(m):
    fr, to = map(int, input().split())
    graph[fr].append(to)

bfs(x)

min_value = sys.maxsize

if k not in memo:
    print(-1)
else:
    for i in range(1,len(memo)):
        if memo[i] == k:
            print(i)