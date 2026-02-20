import heapq
import sys
input = sys.stdin.readline
def dijkstra(start):
    distance[start] = 0
    queue = []

    heapq.heappush(queue,(distance[start],start))

    while queue:
        dist, cnode = heapq.heappop(queue)

        if distance[cnode] < dist:
            continue

        for adj in graph[cnode]:
            nv,nw = adj[0],adj[1]
            cost = dist+nw

            if cost < distance[nv]:
                distance[nv] = cost
                heapq.heappush(queue,(cost,nv))

#도시 개수(정점개수)
N = int(input())
#버스 개수 (간선 개수)
M= int(input())

graph = [ [] for i in range(N+1)]
distance = [sys.maxsize] *(N+1)

for i in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

S, E = map(int,input().split())
dijkstra(S)
print(distance[E])