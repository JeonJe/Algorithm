import sys
n = int(input())
m = int(input())
graph = [ [sys.maxsize]*(n+1) for _ in range(n+1) ]

for i in range(m):
    fr, to, cost = map(int,input().split())
    
    graph[fr][to] = min(graph[fr][to], cost)

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a == b:
                graph[a][b] = 0
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j] if graph[i][j] != sys.maxsize else 0,end=' ')
    print()

