import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

graph = [ [] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

start = int(input())
visited = [ False for i in range(n+1)  ]
answer = 0

def dfs(cur,visited):
    global answer 

    for adj in graph[cur]:
        if not visited[adj]:
            visited[adj] = True
            answer += 1
            dfs(adj, visited)
        

dfs(start, visited)
print(answer)