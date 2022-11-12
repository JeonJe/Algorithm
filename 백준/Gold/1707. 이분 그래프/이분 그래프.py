from collections import deque 

k = int(input())
global cnt 
cnt = 0



def bfs(v):
    visited[v] = True
    que = deque()
    que.append(v)

    # 처음을 1로 칠함 
    bipartite[v] = 1

    while que:
        p = que.popleft()
        
        for adj in graph[p]:
            if not visited[adj] and bipartite[adj] == 0:
                visited[adj] = True
                bipartite[adj] = -bipartite[p]
                que.append(adj)
            if bipartite[adj] == bipartite[p]:
                return False
    return True

            
for _ in range(k):
    v, e = map(int,input().split())
    graph = [ [] for _ in range(v+1) ]

    for i in range(e):
        fr, to = map(int, input().split())
        graph[fr].append(to)
        graph[to].append(fr)
    
    visited = [False] * (v+1)
    bipartite = [0]*(v+1)
    flag_bip = True

    for j in range(1,v+1):
        if visited[j] == False:
            if not bfs(j):
                flag_bip = False
                break
    print( 'YES' if flag_bip else'NO')

