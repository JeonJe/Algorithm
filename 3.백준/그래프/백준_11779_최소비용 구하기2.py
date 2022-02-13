import heapq
import sys
# sys.stdin = open('input.txt', 'r')
# import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [[] for _ in range(n+1)]

# for i in range(1,n+1):
#     visited[i] = i

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
res = []

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0 ,start))


    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        # (2, 2) (3, 3)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                visited[i[0]].append(now)
                heapq.heappush(q, (cost, i[0]))

    visited[end].append(end)
    # print(visited)

    return visited[end]

res = dijkstra(start)


# print(distance)
print(distance[end])
#
# # print(visited)
num_of_path = len(res)
print(num_of_path)
#
print(' '.join(list(map(str, res))))