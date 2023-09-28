import sys

sys.setrecursionlimit(100000) 

n = int(input())
visited = [False] * (n+1)
parent = [0] * (n+1)
que = []
def dfs(v):
    visited[v] = True
    que.append(v)

    while que:
        p = que.pop(0)

        for i in graph[p]:
            if visited[i] == False:        
                visited[i] = True
                que.append(i)
                parent[i] = p


graph = [ [] for _ in range(n+1) ]

for _ in range(n-1):

    fr, to = map(int,input().split())
    graph[fr].append(to)
    graph[to].append(fr)


dfs(1)

for i in range(2,len(parent)):
    print(parent[i])

