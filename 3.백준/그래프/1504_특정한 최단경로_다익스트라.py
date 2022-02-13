import sys
import heapq
input = sys.stdin.readline

N,E = map(int,input().split())
graph = [ [] for i in range(N+1) ]

for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1,v2 = map(int,input().split())

def find_shortest_path(start_v,end_v):
    distance = [sys.maxsize] * (N + 1)
    dijkstra(start_v,distance)
    return distance[end_v]

def dijkstra(start,distance):

    distance[start] = 0
    queue = []

    heapq.heappush(queue,(distance[start],start))

    while queue:
        dist, cv = heapq.heappop(queue)

        if distance[cv] < dist:
            continue

        for adj in graph[cv]:
            nv,nw = adj[0],adj[1]

            cost = dist+nw
            if cost < distance[nv]:
                distance[nv] = cost
                heapq.heappush(queue,(cost,nv))



a=find_shortest_path(1,v1)
b=find_shortest_path(v1, v2)
c=find_shortest_path(v2, N)

d=find_shortest_path(1,v2)
e=find_shortest_path(v2, v1)
f=find_shortest_path(v1, N)

res = min(a+b+c,d+e+f)

print('-1' if res >= sys.maxsize else res)