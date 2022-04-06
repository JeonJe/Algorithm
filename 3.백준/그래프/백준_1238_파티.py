#N개의 마을 (v의 개수 )
#M개의 단방향 도로 (간선의 개수)
import sys
import heapq
input = sys.stdin.readline
N,M,X = map(int,input().split())

graph = [ [] for _ in range(N+1)]

for _ in range (M):
    S,E,T = map(int,input().split())
    graph[S].append((E,T))

def dijkstra(start):

    distance[start] = 0
    queue = []

    heapq.heappush(queue,(distance[start],start))

    while queue:
        dist, cur_node = heapq.heappop(queue)

        if distance[cur_node] < dist:
            continue

        for adj in graph[cur_node]:
            nv,nw = adj[0],adj[1]
            cost = dist + nw

            if cost < distance[nv]:
                distance[nv] = cost
                heapq.heappush(queue,(cost,nv))


#X번째 마을에 모였다가 다시 각자의 집에 돌아가야함

res = [0]*(N+1)
for i in range(1,N+1):
    distance = [sys.maxsize] * (N + 1)
    #i번째 마을에서 각 마을로 최단거리 경로 구함
    dijkstra(i)
    #X까지 최단 거리
    res[i] += distance[X]
    distance = [sys.maxsize] * (N + 1)
    dijkstra(X)
    res[i] += distance[i]


print(max(res))

