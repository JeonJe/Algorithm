import sys, heapq
input = sys.stdin.readline

V,E,P = map(int,input().split())
graph = [ [] for _ in range(V+1)]

for _ in range(E):
    fr,to,weight = map(int,input().split())
    graph[fr].append((to,weight))
    graph[to].append((fr,weight))

def dijkstra(start):
    distance = [sys.maxsize]* (V+1)
    distance[start] = 0

    min_heap = []
    heapq.heappush(min_heap,(0, start))

    while min_heap:
        current_weight, current_node = heapq.heappop(min_heap)

        if distance[current_node] < current_weight :
            continue
        
        for adj_node, adj_weight in graph[current_node]:
            new_weight = adj_weight + distance[current_node]

            if new_weight < distance[adj_node]:
                distance[adj_node] = new_weight
                heapq.heappush(min_heap,(new_weight, adj_node))
    
    return distance
            
shortest_path_from_one = dijkstra(1)
init_to_friend = shortest_path_from_one[P]
init_to_desti = shortest_path_from_one[V]
shortest_path_from_friend = dijkstra(P)
friend_to_desti = shortest_path_from_friend[V]
print("SAVE HIM" if init_to_desti >= init_to_friend + friend_to_desti else "GOOD BYE")