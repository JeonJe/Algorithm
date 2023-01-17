import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) 

n = int(input())
visited = [False] * (n+1)
parent = [0] * (n+1)
que = []
def bfs(v):
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

bfs(1)

for i in range(2,len(parent)):
    print(parent[i])

