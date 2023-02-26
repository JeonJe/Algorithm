import sys
n, m = map(int,input().split())


graph = []

for i in range(m):
    fr,to,weight = map(int,input().split())
    graph.append((fr,to,weight))

distance = [sys.maxsize]*(n+1) 
distance[1] = 0

cycle = False
for i in range(n):
    for j in range(m):
        cur_v = graph[j][0]
        adj_v = graph[j][1]
        weight = graph[j][2]

        if distance[cur_v] != sys.maxsize and distance[adj_v] > distance[cur_v] + weight:
            distance[adj_v] = distance[cur_v] + weight
            if i == n - 1:
                cycle = True
if cycle:
    print(-1)
else:
    for i in range(2,len(distance)):
        if distance[i] == sys.maxsize:
            distance[i] = -1    
    res = distance[2:]
    for r in res:
        print(r)
    



