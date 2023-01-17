n = int(input())

first_row = [ i for i in range(1,n+1) ]
second_row = [ int(input()) for _ in range(n) ]
graph = [ [] for _ in range(n+1) ]



for i in range(len(first_row)):
    graph[i+1].append(second_row[i])


def dfs(start, cur):
    visited[cur] = True 

    for adj in graph[cur]:
        if not visited[adj]:
            dfs(start, adj)
        
        elif visited[adj] and adj == start:
            res.append(start)

        
res = []
for i in range(1,len(graph)):
    visited = [False] * (n+1)
    if not visited[i]:
        dfs(i, i)


print(len(res))
for r in res:
    print(r)
    