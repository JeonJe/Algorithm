from collections import deque

N ,M = map(int,input().split())

stu = [ i for i in range(1,N+1)]

compare = [ list(map(int,input().split())) for _ in range(M) ]
graph = [ []  for _ in range (N+1) ]
in_degree = [0]*(N+1)

for fr, to in compare:
    graph[fr].append(to)
    in_degree[to] += 1

que = deque() 

for i in range(1,N+1):
    if in_degree[i] == 0:
        que.append(i)
res = []

while que:
    cur = que.popleft()
    res.append(cur)

    for adj in graph[cur]:
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
            que.append(adj)

print(*res)