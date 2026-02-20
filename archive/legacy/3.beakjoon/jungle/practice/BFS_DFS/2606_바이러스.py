n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1) ]
global cnt 
cnt = 0

for _ in range(m):
    fr, to = map(int,input().split())
    graph[fr].append(to)
    graph[to].append(fr)

visited  = [False]*(n+1)

def dfs(x):
    global cnt
    visited[x] = True
    
    for adj in graph[x]:
        if not visited[adj]:
            cnt+=1
            visited[x] = True
            dfs(adj)
visited[1] = True
dfs(1)
print(cnt)