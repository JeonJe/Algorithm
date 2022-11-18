import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1) ]
distance = [sys.maxsize] * (n+1)
que = []
def dijkstra(s):
    distance[s] = 0
    heapq.heappush(que,(distance[s], s))
    while que:
        cur_distance, cur_node = heapq.heappop(que)
        if distance[cur_node] < cur_distance:
            continue

        for adj in graph[cur_node]:
            adj_weight, adj_node = adj
            new_distance = cur_distance + adj_weight
            if new_distance < distance[adj_node]:
                distance[adj_node] = new_distance
                heapq.heappush(que,(new_distance,adj_node))


for i in range(m):
    start, end, price = map(int,input().split())
    graph[start].append((price,end))

s, e = map(int,input().split())

dijkstra(s)
print(distance[e])
