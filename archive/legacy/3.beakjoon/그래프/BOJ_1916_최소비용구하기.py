import heapq, sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1) ]
min_heap = []

for i in range(m):
    fr,to,weight = map(int,input().split())
    graph[fr].append((to,weight))
    
start, end = map(int,input().split())

def shortest_path(start,end):
    distance = [sys.maxsize] * (n+1)
    distance[start] = 0
    heapq.heappush(min_heap,(0, start))

    while min_heap:
        current_weight, current_node = heapq.heappop(min_heap)

        if distance[current_node] < current_weight:
            continue

        for adj_node, adj_weight in graph[current_node]:
            new_weight = distance[current_node] + adj_weight

            if new_weight < distance[adj_node]:
                distance[adj_node] = new_weight
                heapq.heappush(min_heap,(new_weight,adj_node))
    print(distance[end])
    
    
shortest_path(start,end)
