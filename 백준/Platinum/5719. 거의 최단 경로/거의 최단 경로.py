import sys 
import heapq
from collections import deque

def shortest_paht(S,graph_going,distance):


    distance[S] = 0
    que = []
    heapq.heappush(que,(0,S))

    #S->D까지 최단 경로를 찾음
    while que:
        cur_distance, cur_node = heapq.heappop(que)

        if distance[cur_node] < cur_distance:
            continue

        # for adj_weight,adj_node in graph_going[cur_node]:
        for i in graph_going[cur_node]:
            new_dist = distance[cur_node] + graph_going[cur_node][i]
            if distance[i] >  new_dist:
                distance[i] = new_dist
                heapq.heappush(que,(new_dist , i))

    return distance

   
def bfs(S,D,graph_back,distance,remove_list):
    path = deque()
    path.append(D)

    while path:
        curr = path.popleft()
        
        if curr == S:
            continue

        for adj_cur, adj_weight in graph_back[curr]:
            if distance[adj_cur] == distance[curr] - graph_going[adj_cur][curr]:
                if (adj_cur, curr) not in remove_list:
                    remove_list.append((adj_cur,curr))
                    path.append(adj_cur)

    return remove_list

while True:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    graph_going = [dict() for _ in range(N)]
    graph_back = [[] for _ in range(N)]

    S, D = map(int,input().split())

    for i in range(M):
        u,v,p = map(int,input().split())
        # graph_going[u].append((p,v))
        graph_going[u][v] = p
        graph_back[v].append((u,p))

    distance = [sys.maxsize]*(N+1)
    distance = shortest_paht(S,graph_going,distance)

    remove_list = []
    remove_list = bfs(S,D,graph_back,distance,remove_list)
    for u,v in remove_list:
        del graph_going[u][v]
        # for weight,node in graph_going[u]:
        #         if v == node:
        #             graph_going[u].remove((weight,node))
        #             break

    distance = [sys.maxsize]*(N+1)
    distance = shortest_paht(S,graph_going,distance)

    print(distance[D] if distance[D] != sys.maxsize else -1)