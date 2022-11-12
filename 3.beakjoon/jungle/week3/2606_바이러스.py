n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1) ]

global cnt 
cnt = 0
def dfs(v):
    global cnt
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            cnt+=1
            dfs(i)

visited = [False] * (n+1)
for _ in range(m):
    fr, to = map(int,input().split())
    graph[fr].append(to)
    graph[to].append(fr)

dfs(1)
print(cnt)