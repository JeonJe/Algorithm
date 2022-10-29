import heapq
from collections import Counter
import sys

input = sys.stdin.readline
T = int(input())

def dijkstra(start):
    distance = [sys.maxsize] * (n + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue,(distance[start],start))

    while queue:
        dist,cur = heapq.heappop(queue)

        if dist < distance[cur]:
            continue

        for adj in graph[cur]:
            nv,ns = adj[0],adj[1]
            cost = dist+ns
            if cost < distance[nv] :
                distance[nv] = cost
                heapq.heappush(queue,(cost,nv))

    return distance

for _ in range(T):
    n,d,c = map(int,input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))

    d = dijkstra(c)

    m = -1
    cnt = 0
    for i in d:
        if i != sys.maxsize:
            cnt+=1
            if m < i:
                m = i

    print(cnt,m)
