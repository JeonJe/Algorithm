import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

n,m = map(int,input().split())
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    fr, to = map(int,input().split())
    graph[fr].append(to)
    graph[to].append(fr)

visited = [False] * (n+1)

res = 0
for i in range(1,len(graph)):
    if visited[i] == False:
        res+=1
        dfs(i)

print(res)
