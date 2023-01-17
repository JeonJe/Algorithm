from collections import deque

#N 노드의 개수, M 간선의 개수 
N, M = map(int,input().split())


graph_light = [ [] for _ in range (N+1) ]
graph_heavy = [ [] for _ in range (N+1) ]

for i in range(M):
    u, v = map(int,input().split())
    graph_light[v].append(u)
    graph_heavy[u].append(v)

def bfs(x,graph):
    visited = [False]*(N+1)
    visited[x] = True
    que = deque()
    que.append(x)
    cnt = 0
    while que:
        cv = que.popleft()

        for adj in graph[cv]:
            if not visited[adj]:
                cnt+=1
                visited[adj] = True
                que.append(adj)
    return cnt 

cnt = 0
for i in range(1,N+1):
    heavy = bfs(i,graph_heavy)
    light = bfs(i,graph_light)
    if light > (N-1)//2 or heavy >(N-1)//2:
        cnt+=1

print(cnt)

