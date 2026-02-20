from collections import deque



def dfs(v):
    visited[v] = True
    res.append(v)
    for w in adj[v]:
        if visited[w] == False:
            dfs(w)
def bfs(v):
    que = deque()
    que.append(v)
    res.append(v)
    visited[v] = True
   

    while len(que) > 0:
        c = que.popleft()
        for w in adj[c]:
            if visited[w] == False:
                visited[w] = True
                que.append(w)
                res.append(w)
                continue

n, m, v = map(int,input().split())
adj = [[] for _ in range(n+1)]
edges = [list(map(int,input().split())) for _ in range(m)]

for edge in edges:
    
    fr, to = edge
    adj[fr].append(to)
    adj[to].append(fr)
    
for i in range(len(adj)):
    adj[i].sort()


visited = [False] * (n + 1)
res = []

dfs(v)
print(*res)

visited = [False] * (n + 1)
res = []

bfs(v)
print(*res)

   