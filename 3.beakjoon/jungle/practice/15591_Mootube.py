from collections import deque 
import sys
N, Q = map(int,input().split())

graph = [ [] for _ in range(N+1) ]


def bfs(K,V):
    que = deque()
    visited = [False] *(N+1)
    que.append((V, sys.maxsize))
    visited[V] = True 
    cnt = 0

    while que:
        cv, cUSADO = que.popleft()
        for adj_v,adj_weight in graph[cv]:
            if not visited[adj_v]:
                visited[adj_v] = True
                USADO = min((cUSADO, adj_weight))
                que.append((adj_v, USADO))
                if USADO >= K:
                    cnt+=1
    return cnt 

for i in range(N-1):
    fr, to, weight = map(int,input().split())
    graph[fr].append((to,weight))
    graph[to].append((fr,weight))

for _ in range(Q):
    K, V  = map(int,input().split())
    cnt = 0
    cnt = bfs(K,V)
    print(cnt)

