from collections import deque

n,m = map(int,input().split())
graph = [ [] for _ in range(n+1) ]
in_degree = [0] * (n+1)

def topological_sort():
    res = []
    for i in range(1,n+1):
        if in_degree[i] == 0:
            que.append(i)

    while que:
        p = que.popleft()
        res.append(p)
        for adj in graph[p]:
            in_degree[adj] -= 1
            if in_degree[adj] == 0:
                que.append(adj)

    print(*res)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    in_degree[b] += 1

que = deque() 



topological_sort()


