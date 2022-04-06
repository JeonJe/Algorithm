import heapq
import sys

input = sys.stdin.readline
v,e = map(int,input().split())
s = int(input())

graph = [ [] for i in range(v+1) ]
distance = [sys.maxsize]*(v+1)
queue = []

for i in range(e):
    iu,iv,iw = map(int,input().split())
    #u에서 v까지 w거리를 그래프에 튜플로 넣음
    graph[iu].append((iv,iw))

def dijkstra(start):
    #시작점의 거리는 0
    distance[start] = 0

    heapq.heappush(queue,(distance[start],start))

    while queue:
        #인접노드 중 최단거리 노드까지의 거리와 노드번호를 가져옴
        dist,cur = heapq.heappop(queue)

        #이미 방문해서 distance[cur]가 작아졌으면 다음 노드 확인
        if distance[cur] < dist:
            continue

        #cur의 노드의 주변 노드 확인
        for adj in graph[cur]:
            nv, vw = adj[0],adj[1]
            #cur까지의 거리 + 주변노드까지 거리의 합
            cost = dist + vw
            #주변 노드까지 한 번에 가는 것보다 현재 cur 노드를 거쳐 가는 것이 더 빠르다면
            #갱신하고, 거리와 노드 번호를 추가
            if cost < distance[nv]:
                distance[nv]= cost
                heapq.heappush(queue,(cost,nv))

dijkstra(s)

for i in range(1,v+1):

    print("INF" if distance[i]==sys.maxsize else distance[i])


