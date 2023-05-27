
import sys, heapq
input = sys.stdin.readline

def shortest_path(start):
    
    distance[start] = 0
    min_heap = []
    heapq.heappush(min_heap,(0,start))

    while min_heap:
        current_weight, current_node = heapq.heappop(min_heap)

        if distance[current_node] < current_weight:
            continue

        for adj_node, adj_weight in graph[current_node]:
            new_weight = distance[current_node] + adj_weight
            if new_weight < distance[adj_node]:
                distance[adj_node] = new_weight
                heapq.heappush(min_heap, (new_weight, adj_node))

def find_rational_path(node):
    
    if dp[node] == 0:
        for adj_node, _ in graph[node]:
            if distance[node] > distance[adj_node]:
                dp[node] += find_rational_path(adj_node)
    
    return dp[node]


if __name__ == "__main__":
    N, M = map(int,input().split())

    graph = [ [] for _ in range(N+1) ]
    for i in range(M):
        fr, to, weight = map(int,input().split())
        graph[fr].append((to,weight))
        graph[to].append((fr,weight))

    distance = [sys.maxsize]*(N+1)
    #i번째 인덱스에서 출발하여 T에 도착하는 합리적인 이동 경로의 수 
    dp = [0]*(N+1)
    start, end = 1, 2
    dp[end] = 1

    shortest_path(end)
    find_rational_path(start)
    print(dp[start])
